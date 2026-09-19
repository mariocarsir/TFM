# -*- coding: utf-8 -*-
"""Recalculo de V1a / V1b / V2 con las superficies MEDIDAS SOBRE EL MODELO 3D
de PVsyst por Mario (19/09/2026), sustituyendo las estimaciones por catastro/KMZ.

Superficies nuevas:
    V1a lucernario   578,9109 m2   (antes 472 m2, catastro)
    V1b cubierta   2.756,8828 m2   (antes 1.562 m2 NETOS tras 0,70; ojo: ambiguedad)
    V2 marquesinas 3.536      m2   (antes 3.332 m2, huella F1-F8 del KMZ)

Reutiliza el modelo solar horario calibrado de solar.py (desviacion -1,3 % frente
al informe PVsyst del trabajo previo) y la carga horaria canonica de 8.760 h.
"""
import numpy as np, pandas as pd, io, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)
exec(open("solar.py", encoding="utf-8").read().split("# --- CALIBRACION")[0])

# --- carga horaria canonica (kW) -------------------------------------------
CSV = os.path.join(BASE, "..", "..", "..", "Datos", "PVsyst", "Entradas",
                   "carga_horaria_CPD_general_8760.csv")
raw = pd.read_csv(CSV, sep=";", skiprows=[1], decimal=",")
L = raw.iloc[:, 1].to_numpy(dtype=float)
assert len(L) == 8760, len(L)
ETOT = L.sum() / 1000                      # MWh/ano
# escenario con geotermia: -365 MWh/ano, repartidos proporcionalmente
EGEO = ETOT - 365.0
Lg = L * EGEO / ETOT

# --- generacion, misma cadena de perdidas que el trabajo previo ------------
def p(kWp, tilt, az, shad, soil=0.010):
    G, _ = poa(tilt, az)
    Geff = G * 0.999 * (1 - shad) * (1 - soil) * (1 - 0.019)
    Tc = Tamb + Geff / 20.0
    return np.maximum(kWp * (Geff / 1000) * (1 - 0.0024 * (Tc - 25))
                      * 0.991 * 1.005 * 0.979 * 0.990 * 0.985 * 0.998, 0)

DENS = 226.7        # W/m2 de modulo, REC Alpha Pure-RX
WMOD = 470.0        # W por modulo
AMOD = 2.073        # m2 por modulo

# --- superficies ------------------------------------------------------------
S_V1A_3D = 578.9109
S_V1B_3D = 2756.8828
S_V2_3D  = 3536.0
PATIOS   = 408.0    # patios interiores medidos en pixeles sobre PlantaCPD.png

# V1a: BIPV, factor de vidrio activo 0,80 y 125 Wp/m2 (VLT ~20 %)
k1a = S_V1A_3D * 0.80 * 125 / 1000

# V1b: dos lecturas de la cifra de Mario
#   A  la cifra es BRUTA y aun incluye los patios  -> restarlos y aplicar 0,70 x 0,82
#   B  la cifra ya excluye lucernario y patios     -> aplicar solo 0,70 x 0,82
k1b_A = (S_V1B_3D - PATIOS) * 0.70 * 0.82 * DENS / 1000
k1b_B = S_V1B_3D * 0.70 * 0.82 * DENS / 1000
#   C  (lectura ERRONEA que hay que evitar: tomarla como superficie neta)
k1b_C = S_V1B_3D * 0.82 * DENS / 1000

# V2: huella x 0,90 de ocupacion de modulo
k2 = S_V2_3D * 0.90 * DENS / 1000


def strings(kWp_bruto, ns=12):
    """Redondeo a strings enteros de ns modulos (criterio conservador, a la baja)."""
    nmod = int(kWp_bruto * 1000 // WMOD)
    nstr = nmod // ns
    return nstr, nstr * ns, nstr * ns * WMOD / 1000, nstr * ns * AMOD


def balance(P, load, cap=0.0, eta=0.92):
    soc = 0.0; imp = 0.0; exc = 0.0
    for a, l in zip(P, load):
        n = a - l
        if n > 0:
            ch = min(n, cap, (cap - soc) / eta) if cap > 0 else 0.0
            soc += ch * eta; exc += n - ch
        else:
            ds = min(-n, cap, soc * eta) if cap > 0 else 0.0
            soc -= ds / eta; imp += (-n - ds)
    epv = P.sum() / 1000
    eauto = (load.sum() - imp) / 1000
    return dict(E_PV=epv, E_auto=eauto, exced=exc / 1000, red=imp / 1000,
                A_PV=eauto / epv * 100 if epv else 0,
                C_D=eauto / (load.sum() / 1000) * 100,
                horas=int((P > load).sum()), pico=P.max())


print("=" * 100)
print("RECALCULO CON SUPERFICIES DEL MODELO 3D DE PVsyst  (19/09/2026)")
print(f"Consumo sin geotermia {ETOT:.1f} MWh/ano   |   con geotermia {EGEO:.1f} MWh/ano")
print("=" * 100)

print("\n--- A) POTENCIA INSTALABLE ---")
filas = [("V1a BIPV lucernario", S_V1A_3D, k1a, "0,80 vidrio activo x 125 Wp/m2"),
         ("V1b lectura A (bruta, -patios)", S_V1B_3D, k1b_A, "-408 patios x 0,70 x 0,82 x 226,7"),
         ("V1b lectura B (ya neta de patios)", S_V1B_3D, k1b_B, "x 0,70 x 0,82 x 226,7"),
         ("V1b lectura C (ERRONEA)", S_V1B_3D, k1b_C, "x 0,82 x 226,7  <- NO usar"),
         ("V2 marquesinas", S_V2_3D, k2, "x 0,90 x 226,7")]
print(f"{'Caso':36s} {'sup 3D':>10s} {'kWp bruto':>10s}  criterio")
for lab, s, k, crit in filas:
    print(f"{lab:36s} {s:10.1f} {k:10.1f}  {crit}")

print("\n--- B) AJUSTE A STRINGS ENTEROS DE 12 MODULOS ---")
print(f"{'Caso':30s} {'strings':>8s} {'modulos':>8s} {'kWp real':>9s} {'m2 modulo':>10s}")
sistemas = {}
for lab, kb in [("V1b lectura A", k1b_A), ("V1b lectura B", k1b_B), ("V2 marquesinas", k2)]:
    ns, nm, kr, am = strings(kb)
    sistemas[lab] = kr
    print(f"{lab:30s} {ns:8d} {nm:8d} {kr:9.2f} {am:10.1f}")
print(f"{'V1a BIPV (sin string fijo)':30s} {'-':>8s} {'-':>8s} {k1a:9.2f} {S_V1A_3D*0.80:10.1f}")

kA = sistemas["V1b lectura A"]; kB = sistemas["V1b lectura B"]; kV2 = sistemas["V2 marquesinas"]

# --- perfiles de generacion -------------------------------------------------
P1a = p(k1a, 5, -30, 0.005, soil=0.020)
P1bA = p(kA, 10, -30, 0.039)
P1bB = p(kB, 10, -30, 0.039)
PV2 = p(kV2, 8, -30, 0.010)

CASOS = [
    ("V1a BIPV lucernario", P1a, k1a),
    ("V1b cubierta - lectura A", P1bA, kA),
    ("V1b cubierta - lectura B", P1bB, kB),
    ("V1 total (A) = V1a+V1bA", P1a + P1bA, k1a + kA),
    ("V1 total (B) = V1a+V1bB", P1a + P1bB, k1a + kB),
    ("V2 marquesinas", PV2, kV2),
    ("V1(A)+V2", P1a + P1bA + PV2, k1a + kA + kV2),
    ("V1(B)+V2", P1a + P1bB + PV2, k1a + kB + kV2),
]

for etiqueta, load, tot in (("C) SIN GEOTERMIA", L, ETOT), ("D) CON GEOTERMIA", Lg, EGEO)):
    print(f"\n--- {etiqueta}  (demanda {tot:.0f} MWh/ano) ---")
    print(f"{'Caso':28s} {'kWp':>8s} {'E_PV':>8s} {'kWh/kWp':>8s} {'A_PV':>7s} "
          f"{'C_D':>7s} {'exced':>7s} {'h vert':>7s} {'pico kW':>8s}")
    for lab, P, k in CASOS:
        r = balance(P, load)
        print(f"{lab:28s} {k:8.1f} {r['E_PV']:8.1f} {r['E_PV']*1000/k:8.0f} "
              f"{r['A_PV']:6.1f}% {r['C_D']:6.2f}% {r['exced']:7.1f} {r['horas']:7d} {r['pico']:8.0f}")

print("\n--- E) SENSIBILIDAD DE LA TRANSPARENCIA DEL VIDRIO BIPV (V1a) ---")
print(f"{'VLT':>12s} {'Wp/m2':>7s} {'kWp':>7s} {'E_PV':>8s} {'C_D 3832':>9s} {'C_D 3467':>9s}")
for vlt, d in [("alta (>30 %)", 90), ("media (~20 %)", 125), ("baja (~10 %)", 160)]:
    kk = S_V1A_3D * 0.80 * d / 1000
    PP = p(kk, 5, -30, 0.005, soil=0.020)
    e = PP.sum() / 1000
    print(f"{vlt:>12s} {d:7d} {kk:7.1f} {e:8.1f} {e/ETOT*100:8.2f}% {e/EGEO*100:8.2f}%")

print("\n--- F) COMPARACION CONTRA LAS CIFRAS ANTIGUAS ---")
k1a_old = 472 * 0.80 * 125 / 1000
k1b_old = (3111 - 472 - 408) * 0.70 * 0.82 * DENS / 1000
k2_old = 3332.0 * 0.90 * DENS / 1000
print(f"{'':22s} {'antes':>10s} {'ahora (A)':>10s} {'ahora (B)':>10s} {'delta A':>9s}")
print(f"{'V1a kWp':22s} {k1a_old:10.1f} {k1a:10.1f} {k1a:10.1f} {(k1a/k1a_old-1)*100:+8.1f}%")
print(f"{'V1b kWp':22s} {k1b_old:10.1f} {kA:10.1f} {kB:10.1f} {(kA/k1b_old-1)*100:+8.1f}%")
print(f"{'V2 kWp':22s} {k2_old:10.1f} {kV2:10.1f} {kV2:10.1f} {(kV2/k2_old-1)*100:+8.1f}%")

print("\n--- G) COHERENCIA GEOMETRICA: 3D FRENTE A CATASTRO / KMZ ---")
tot3d = S_V1A_3D + S_V1B_3D
for lab, ref in [("catastro", 3111.0), ("Google Earth", 3070.0), ("KMZ dibujado", 3020.0)]:
    print(f"  V1a+V1b 3D = {tot3d:8.1f} m2  vs  {lab:14s} {ref:7.1f} m2  -> {(tot3d/ref-1)*100:+6.1f}%")
print(f"  Si la cifra de V1b NO descuenta los patios, el forjado equivalente seria "
      f"{S_V1B_3D-PATIOS:.1f} m2 frente a los 2.231 m2 de catastro ({(S_V1B_3D-PATIOS)/2231*100-100:+.1f} %).")
