# -*- coding: utf-8 -*-
"""Genera la serie horaria de consumo del CPD en el formato CSV que importa PVsyst V8.

Fuente canonica: Datos/Consumo CPD/Mensual/ (12 ficheros, 5 min, dic-2024 -> nov-2025).
Formato exigido por el manual v8-1 (seccion 7 «Self-consumption»): CSV con ';',
1a columna fecha dd/mm/aaaa hh:mm, 2a columna valores con la unidad en la 2a fila,
ano de 365 dias (nunca bisiesto).
"""
import pandas as pd, numpy as np, glob, os

BASE = r"C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Datos\Consumo CPD\Mensual"
OUT = r"C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\.claude\worktrees\pvsyst-variante1\Datos\PVsyst\Entradas"
NUM = ['Contador Gral', 'Contador A', 'Contador B', 'Pot Gral', 'Pot A', 'Pot B']


def load(f):
    if f.lower().endswith(".csv"):
        d = pd.read_csv(f, sep=";", header=0, dtype=str, encoding="latin-1")
        d.columns = [c.strip() for c in d.columns]
        d['Fecha'] = pd.to_datetime(d['Fecha'], format="%d/%m/%Y %H:%M", errors='coerce')
        for c in NUM:
            d[c] = pd.to_numeric(d[c].astype(str).str.strip().str.replace(',', '.', regex=False), errors='coerce')
    else:
        d = pd.read_excel(f, header=0)
        d.columns = [str(c).strip() for c in d.columns]
        d['Fecha'] = pd.to_datetime(d['Fecha'], errors='coerce')
        for c in NUM:
            d[c] = pd.to_numeric(d[c], errors='coerce')
    return d.dropna(subset=['Fecha'])


P = [load(f)[['Fecha', 'Pot Gral', 'Pot A', 'Pot B']] for f in sorted(glob.glob(os.path.join(BASE, "*")))]
D = pd.concat(P).sort_values('Fecha').set_index('Fecha')
n0 = len(D)
D = D[(D['Pot Gral'] > 50) & (D['Pot Gral'] < 800)]          # filtro de huecos de telemedida
H = D.resample('h').mean().dropna(subset=['Pot Gral'])
H['IT'] = H['Pot A'] + H['Pot B']
print(f"registros 5 min: {n0} -> {len(D)} tras filtro ({100 * (n0 - len(D)) / n0:.2f} % descartado)")
print(f"serie horaria real: {H.index.min()} -> {H.index.max()}  ({len(H)} h)")

# --- ano tipo civil 2025 (365 dias): diciembre se toma de 2024, resto de 2025 ---
idx = pd.date_range("2025-01-01 00:00", periods=8760, freq="h")
prof_G = H.groupby([H.index.month, H.index.hour])['Pot Gral'].mean()
prof_IT = H.groupby([H.index.month, H.index.hour])['IT'].mean()


def serie(col, prof):
    src = {}
    for ts, v in H[col].items():
        src.setdefault((ts.month, ts.day, ts.hour), []).append(v)
    out, nrel, nprof = [], 0, 0
    for t in idx:
        k = (t.month, t.day, t.hour)
        if k in src:
            out.append(float(np.mean(src[k]))); nrel += 1
        else:
            out.append(float(prof.get((t.month, t.hour), np.nan))); nprof += 1
    s = pd.Series(out, index=idx).interpolate().bfill().ffill()
    return s, nrel, nprof


G, nr, npf = serie('Pot Gral', prof_G)
IT, _, _ = serie('IT', prof_IT)
print(f"horas con dato real: {nr} ({100 * nr / 8760:.1f} %)  |  rellenadas con perfil mes-hora: {npf}")

# reescalado a las cifras canonicas (energia medida por diferencia de contadores)
REAL_G, REAL_IT = 3831.96, 2585.08     # MWh/ano
G = G * REAL_G * 1000 / G.sum()
IT = IT * REAL_IT * 1000 / IT.sum()
NOIT = G - IT

for nom, s in [("General (3.832 MWh)", G), ("IT (2.585 MWh)", IT), ("no-IT (1.247 MWh)", NOIT)]:
    print(f"{nom:24s} media {s.mean():7.1f} kW   min {s.min():7.1f}   max {s.max():7.1f}   total {s.sum() / 1000:8.1f} MWh")
print(f"PUE resultante: {G.sum() / IT.sum():.3f}")


def escribe(serie_kw, fichero, etiqueta):
    lin = ["Date;" + etiqueta, ";kW"]
    for t, v in serie_kw.items():
        lin.append(f"{t.strftime('%d/%m/%Y %H:%M')};{v:.2f}".replace('.', ','))
    p = os.path.join(OUT, fichero)
    with open(p, "w", encoding="latin-1", newline="\r\n") as fh:
        fh.write("\n".join(lin) + "\n")
    print("escrito:", p, f"({len(lin)} lineas)")


escribe(G, "carga_horaria_CPD_general_8760.csv", "Consumo general CPD")
escribe(NOIT, "carga_horaria_CPD_noIT_8760.csv", "Consumo no-IT (HVAC+aux)")

m = (G.resample('MS').sum() / 1000).round(1)
print("\nBalance mensual del consumo general (MWh):")
print(m.to_string())
