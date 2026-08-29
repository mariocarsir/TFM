# -*- coding: utf-8 -*-
"""Las tres variantes como ALTERNATIVAS EXCLUYENTES (no combinadas).

Responde al punto 5 del prompt de Mario del 29/08/2026: para cada variante por
separado, C_D sin bateria, C_D con bateria, bateria minima para varios objetivos y
tipologia de autoconsumo resultante.
"""
import numpy as np
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L = np.load("L.npy"); LIT = np.load("LIT.npy"); ETOT = L.sum() / 1000
OCU = 13.2                       # m2/kWp en suelo
ANETA = 588401 * 0.85            # parcela util

def p(kWp, tilt, az, shad, soil=0.010):
    G, _ = poa(tilt, az)
    Geff = G * 0.999 * (1 - shad) * (1 - soil) * (1 - 0.019)
    Tc = Tamb + Geff / 20.0
    return np.maximum(kWp * (Geff / 1000) * (1 - 0.0024 * (Tc - 25))
                      * 0.991 * 1.005 * 0.979 * 0.990 * 0.985 * 0.998, 0)

k1a = 472 * 0.80 * 125 / 1000
k1b = (3111 - 472 - 408) * 0.70 * 0.82 * 226.7 / 1000
k2 = 3332.0 * 0.90 * 226.7 / 1000
V1 = p(k1a, 5, -30, 0.005, soil=0.020) + p(k1b, 10, -30, 0.039)
V2 = p(k2, 8, -30, 0.010)
U = p(1, 30, 0, 0.020)                       # planta en suelo, por kWp

AH = 0.70 * (L - LIT).sum() / 1000 * (1 - 3.2 / 5.5)
EG = ETOT - AH; Lg = L * EG / ETOT

def sim(P, load, cap, eta=0.92, pm=None):
    pm = cap if pm is None else pm
    soc = 0.; imp = 0.; exc = 0.; pd = 0.
    for a, l in zip(P, load):
        n = a - l
        if n > 0:
            ch = min(n, pm, (cap - soc) / eta); soc += ch * eta; exc += n - ch
        else:
            ds = min(-n, pm, soc * eta); soc -= ds / eta; imp += (-n - ds); pd = max(pd, ds)
    return (1 - imp / load.sum()) * 100, exc / 1000, imp / 1000, pd

def min_cap(P, load, obj, hi=80000.):
    if sim(P, load, hi)[0] < obj: return None
    if sim(P, load, 0.)[0] >= obj: return 0.
    lo = 0.
    for _ in range(15):
        m = (lo + hi) / 2
        if sim(P, load, m)[0] >= obj: hi = m
        else: lo = m
    return hi

def min_kwp(load, obj, cap, hi=12000.):
    """kWp minimo de planta en suelo para alcanzar obj con una bateria dada."""
    if sim(U * hi, load, cap)[0] < obj: return None
    lo = 0.
    for _ in range(16):
        m = (lo + hi) / 2
        if sim(U * m, load, cap)[0] >= obj: hi = m
        else: lo = m
    return hi

print("=" * 92)
print("A) CADA VARIANTE POR SEPARADO, SIN BATERIA  (demanda %.0f MWh/ano)" % ETOT)
print("=" * 92)
print(f"{'Variante':30s} {'kWp':>8s} {'E_PV':>8s} {'A_PV':>7s} {'C_D':>7s} {'exced':>8s} {'red':>7s}")
print("-" * 92)
CASOS = [("V1 Cubierta (BIPV+liberada)", V1, k1a + k1b),
         ("V2 Marquesinas 3.332 m2", V2, k2)]
for kw in (1000, 1500, 2000, 2250, 2500, 3000):
    CASOS.append((f"V3 Planta suelo {kw/1000:.2f} MWp", U * kw, float(kw)))
for lab, P, k in CASOS:
    e = P.sum() / 1000; a = np.minimum(P, L).sum() / 1000
    cd, exc, imp, _ = sim(P, L, 0.)
    print(f"{lab:30s} {k:8.0f} {e:8.0f} {a/e*100:6.1f}% {cd:6.1f}% {exc:8.0f} {imp:7.0f}")

print()
print("=" * 92)
print("B) BATERIA MINIMA PARA CADA OBJETIVO DE C_D REAL, VARIANTE A VARIANTE")
print("=" * 92)
for lab, P, k in CASOS:
    techo = sim(P, L, 1e9)[0]
    linea = f"{lab:30s} techo con bateria infinita = {techo:5.1f} %  |  "
    trozos = []
    for obj in (50, 60, 70, 80, 90):
        c = min_cap(P, L, obj)
        trozos.append(f"{obj}%: " + ("--" if c is None else f"{c/1000:.2f} MWh"))
    print(linea + "  ".join(trozos))

print()
print("=" * 92)
print("C) V3 SOLA: QUE HACE FALTA PARA 80 / 85 / 90 % DE C_D REAL")
print("=" * 92)
print(f"{'obj':>5s} {'MWp':>7s} {'BESS MWh':>9s} {'ha':>6s} {'% parcela':>10s} {'C_D':>7s} {'exced MWh':>10s}")
print("-" * 92)
for obj in (80, 85, 90, 95):
    best = None
    for kw in range(500, 8001, 250):
        c = min_cap(U * kw, L, obj)
        if c is None: continue
        cost = kw * 0.55 + c * 0.30           # k€ orientativos, solo para ordenar
        if best is None or cost < best[0]: best = (cost, kw, c)
    if best is None:
        print(f"{obj:4d}% inalcanzable"); continue
    _, kw, c = best
    cd, exc, imp, pd = sim(U * kw, L, c)
    print(f"{obj:4d}% {kw/1000:7.2f} {c/1000:9.2f} {kw*OCU/10000:6.2f} {kw*OCU/ANETA*100:9.1f}% {cd:6.1f}% {exc:10.0f}")

print()
print("=" * 92)
print("D) COMPROBACION DE LA HIPOTESIS DE MARIO: 2,25-2,50 MWp -> 80-90 %?")
print("=" * 92)
for kw in (2250, 2500):
    print(f"  V3 = {kw/1000:.2f} MWp (E_PV {U.sum()*kw/1000:.0f} MWh, {U.sum()*kw/1000/ETOT:.2f}x la demanda)")
    for cap in (0, 2000, 4000, 6000, 8000, 12000):
        cd, exc, imp, pd = sim(U * kw, L, cap)
        print(f"      BESS {cap/1000:5.1f} MWh -> C_D {cd:5.1f} %  exced {exc:5.0f} MWh  red {imp:5.0f} MWh  P_desc {pd:4.0f} kW")

print()
print("=" * 92)
print("E) EXCEDENTES: LO QUE DECIDE LA TIPOLOGIA (con excedentes / sin excedentes)")
print("=" * 92)
print("Horas con vertido y energia vertida, SIN bateria:")
for lab, P, k in CASOS:
    n = int((P > L).sum()); exc = np.maximum(P - L, 0).sum() / 1000
    print(f"  {lab:30s} {n:5d} h/ano con excedente ({n/87.60:5.1f} %)  {exc:7.0f} MWh")
print()
print("Bateria minima para vertido CERO (permitiria 'sin excedentes' sin recortar):")
for lab, P, k in CASOS[:2]:
    lo, hi = 0., 60000.
    if np.maximum(P - L, 0).sum() == 0:
        print(f"  {lab:30s} no vierte nunca: 0 MWh"); continue
    for _ in range(16):
        m = (lo + hi) / 2
        if sim(P, L, m)[1] < 0.5: hi = m
        else: lo = m
    print(f"  {lab:30s} {hi/1000:.2f} MWh")
