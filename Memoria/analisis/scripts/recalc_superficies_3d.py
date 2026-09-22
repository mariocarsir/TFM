# -*- coding: utf-8 -*-
"""Recalculo CERRADO de V1a / V1b / V2 con las superficies medidas sobre el modelo
3D de PVsyst por Mario (19/09/2026) y con sus cuatro respuestas del mismo dia.

Revision 2 -- 19/09/2026. Cambios frente a la revision 1:

  1. EL LUCERNARIO ES HORIZONTAL (0 grados). Mario: "el tragaluz, su pendiente es 0,
     es horizontal". Cae la hipotesis de ~35 grados de la rev.1 (la coincidencia
     578,9109/472 = 1/cos(35,4) era casualidad numerica) y cae tambien la hipotesis
     vieja de 5 grados heredada de catastro. Superficie desarrollada = superficie
     en planta: no hay correccion angular que aplicar.

  2. NINGUNA de las tres superficies lleva margenes descontados. Mario: "es la
     superficie maxima que se podria llegar a ocupar". Los factores de reduccion
     (0,80 vidrio activo; 0,70 retranqueos/equipos; 0,82 empaquetado en sheds;
     0,90 ocupacion de marquesina) se aplican DESDE CERO sobre las tres cifras.

  3. LOS PATIOS YA ESTAN EXCLUIDOS. Mario midio poligonos de tejado independientes
     por seccion sobre la planta en H, no un rectangulo envolvente con agujeros.
     El hueco entre las patas de la H queda fuera por construccion. Verificado
     sobre 'Prompts/Capturas/situacion 3D V1 y V2.png' (los dos patios estan
     modelados como huecos pasantes: se ve el fondo a traves de ellos) y sobre
     'Prompts/Capturas/superficies v1 y v2.png' (marcado por secciones).
     => Se adopta lo que la rev.1 llamaba LECTURA B. Las lecturas A y C se borran.

  4. FUENTE DE LA GEOMETRIA: planos de catastro a escala 1:1, trazados a mano en
     el editor 3D de PVsyst (no hay importacion de CAD para sombreados). Dato para
     declarar en la fase 1.4 de ERMA.

  5. El reparto de strings de V2 (126 frente a 127) queda ABIERTO por decision
     expresa de Mario: "conforme avancemos en PVsyst veremos". Se calculan las dos.

Reutiliza el modelo solar horario calibrado de solar.py (desviacion -1,3 % frente
al informe PVsyst del trabajo previo) y la carga horaria canonica de 8.760 h.
"""
import numpy as np, pandas as pd, os

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
EGEO = ETOT - 365.0                        # escenario con geotermia
Lg = L * EGEO / ETOT

# --- generacion, misma cadena de perdidas que el trabajo previo ------------
def p(kWp, tilt, az, shad, soil=0.010):
    G, _ = poa(tilt, az)
    Geff = G * 0.999 * (1 - shad) * (1 - soil) * (1 - 0.019)
    Tc = Tamb + Geff / 20.0
    return np.maximum(kWp * (Geff / 1000) * (1 - 0.0024 * (Tc - 25))
                      * 0.991 * 1.005 * 0.979 * 0.990 * 0.985 * 0.998, 0)

DENS = 226.7        # W/m2 de modulo, REC Alpha Pure-RX 470 Wp
WMOD = 470.0        # W por modulo
AMOD = 2.073        # m2 por modulo
NS   = 12           # modulos en serie por string (el del trabajo previo)
PINV = 100.0        # kWac por Huawei SUN2000-100KTL-M2
SMAX = 20           # strings maximos por inversor (10 MPPT x 2 entradas) -- VERIFICAR

# --- superficies MAXIMAS IDEALES medidas sobre el 3D (sin margenes) --------
S_V1A = 578.9109    # lucernario, plano HORIZONTAL
S_V1B = 2756.8828   # cubierta de las alas de la H, ya neta de lucernario y patios
S_V2  = 3536.0      # huella de marquesinas

# --- factores de reduccion (se aplican desde cero) -------------------------
F_VIDRIO = 0.80     # fraccion de vidrio activo del lucernario BIPV
F_RETR   = 0.70     # retranqueos, equipos que permanecen, pasillos, casetones
F_SHED   = 0.82     # empaquetado en filas a 10 grados
F_MARQ   = 0.90     # ocupacion de modulo sobre la marquesina
WP_BIPV  = 125      # Wp/m2 de vidrio FV para VLT ~20 %

k1a  = S_V1A * F_VIDRIO * WP_BIPV / 1000
A1b  = S_V1B * F_RETR * F_SHED                 # m2 netos de modulo disponibles
k1b  = A1b * DENS / 1000
A2   = S_V2 * F_MARQ
k2   = A2 * DENS / 1000


def strings(kWp_bruto, ns=NS):
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


print("=" * 104)
print("RECALCULO CERRADO CON LAS SUPERFICIES DEL MODELO 3D  (rev.2, 19/09/2026)")
print(f"Consumo sin geotermia {ETOT:.1f} MWh/ano   |   con geotermia {EGEO:.1f} MWh/ano")
print("=" * 104)

print("\n--- A) DE SUPERFICIE MAXIMA IDEAL A POTENCIA BRUTA ---")
print(f"{'Variante':34s} {'sup 3D':>10s} {'factores':>22s} {'m2 utiles':>10s} {'kWp bruto':>10s}")
print(f"{'V1a BIPV lucernario (0 grd)':34s} {S_V1A:10.4f} {'x0,80 vidrio':>22s} "
      f"{S_V1A*F_VIDRIO:10.1f} {k1a:10.2f}")
print(f"{'V1b cubierta alas de la H':34s} {S_V1B:10.4f} {'x0,70 x0,82':>22s} {A1b:10.1f} {k1b:10.2f}")
print(f"{'V2 marquesinas':34s} {S_V2:10.4f} {'x0,90':>22s} {A2:10.1f} {k2:10.2f}")

print("\n--- B) AJUSTE A STRINGS ENTEROS DE 12 MODULOS ---")
ns1b, nm1b, k1b_r, am1b = strings(k1b)
ns2,  nm2,  k2_r,  am2  = strings(k2)
print(f"{'Caso':34s} {'strings':>8s} {'modulos':>8s} {'kWp':>9s} {'m2 mod':>9s} {'cabe?':>7s}")
print(f"{'V1b techo por superficie':34s} {ns1b:8d} {nm1b:8d} {k1b_r:9.2f} {am1b:9.1f} "
      f"{'si' if am1b<=A1b else 'NO':>7s}")
print(f"{'V2 opcion 127 strings':34s} {ns2:8d} {nm2:8d} {k2_r:9.2f} {am2:9.1f} "
      f"{'si' if am2<=A2 else 'NO':>7s}")
ns2b = ns2 - 1
k2_b = ns2b * NS * WMOD / 1000
print(f"{'V2 opcion 126 strings (7x18)':34s} {ns2b:8d} {ns2b*NS:8d} {k2_b:9.2f} "
      f"{ns2b*NS*AMOD:9.1f} {'si':>7s}")
print(f"{'V1a BIPV (sin string fijo)':34s} {'-':>8s} {'-':>8s} {k1a:9.2f} "
      f"{S_V1A*F_VIDRIO:9.1f} {'si':>7s}")

print("\n--- C) RESTRICCION ELECTRICA DE V1b: entradas DC por inversor ---")
print(f"  Techo por superficie: {ns1b} strings. Con 3 x SUN2000-100KTL-M2 salen "
      f"{ns1b/3:.1f} strings/inversor.")
print(f"  Limite supuesto por inversor: {SMAX} strings (10 MPPT x 2 entradas). "
      f"{'EXCEDIDO' if ns1b/3 > SMAX else 'OK'}")
ns1b_cfg = 3 * SMAX                     # 60 strings, 20 por inversor
k1b_cfg = ns1b_cfg * NS * WMOD / 1000
print(f"  Configuracion electricamente limpia: {ns1b_cfg} strings (3 x {SMAX}) = "
      f"{ns1b_cfg*NS} modulos = {k1b_cfg:.2f} kWp")
print(f"     superficie de modulo {ns1b_cfg*NS*AMOD:.1f} m2 sobre {A1b:.1f} m2 utiles "
      f"({ns1b_cfg*NS*AMOD/A1b*100:.1f} % de ocupacion)")
print(f"     ratio DC/AC = {k1b_cfg/(3*PINV):.3f}   (trabajo previo: 1,13)")
print(f"  Alternativa de maxima superficie: {ns1b} strings = {k1b_r:.2f} kWp, "
      f"ratio {k1b_r/(3*PINV):.3f}, pero exige 4 inversores (ratio "
      f"{k1b_r/(4*PINV):.3f}) o alargar el string por encima de {NS} modulos.")

print("\n--- D) REPARTO DE INVERSORES DE V2 (decision DIFERIDA por Mario) ---")
for lab, nst, kk in [("127 strings", ns2, k2_r), ("126 strings (7x18)", ns2b, k2_b)]:
    ninv = int(np.ceil(nst / SMAX))
    print(f"  {lab:20s} {kk:7.2f} kWp  minimo {ninv} inversores  "
          f"ratio DC/AC {kk/(ninv*PINV):.3f}  "
          f"{'reparto no uniforme (127 es primo)' if nst == 127 else 'reparto uniforme 7 x 18'}")

# --- perfiles de generacion -------------------------------------------------
P1a  = p(k1a,     0,   0, 0.005, soil=0.020)   # HORIZONTAL
P1b  = p(k1b_cfg, 10, -30, 0.039)              # configuracion de trabajo, 338,40 kWp
P1bT = p(k1b_r,   10, -30, 0.039)              # techo por superficie, 355,32 kWp
PV2  = p(k2_r,     8, -30, 0.010)              # 127 strings
PV2b = p(k2_b,     8, -30, 0.010)              # 126 strings

CASOS = [
    ("V1a BIPV lucernario 0 grd", P1a, k1a),
    ("V1b cubierta (3x20 strings)", P1b, k1b_cfg),
    ("V1b techo por superficie", P1bT, k1b_r),
    ("V1 total = V1a + V1b", P1a + P1b, k1a + k1b_cfg),
    ("V1 total con techo V1b", P1a + P1bT, k1a + k1b_r),
    ("V2 marquesinas 127 strings", PV2, k2_r),
    ("V2 marquesinas 126 strings", PV2b, k2_b),
    ("V1 + V2 (127 strings)", P1a + P1b + PV2, k1a + k1b_cfg + k2_r),
    ("V1 + V2 (126 strings)", P1a + P1b + PV2b, k1a + k1b_cfg + k2_b),
]

for etiqueta, load, tot in (("E) SIN GEOTERMIA", L, ETOT), ("F) CON GEOTERMIA", Lg, EGEO)):
    print(f"\n--- {etiqueta}  (demanda {tot:.0f} MWh/ano) ---")
    print(f"{'Caso':30s} {'kWp':>8s} {'E_PV':>8s} {'kWh/kWp':>8s} {'A_PV':>7s} "
          f"{'C_D':>7s} {'exced':>7s} {'h vert':>7s} {'pico kW':>8s}")
    for lab, P, k in CASOS:
        r = balance(P, load)
        print(f"{lab:30s} {k:8.1f} {r['E_PV']:8.1f} {r['E_PV']*1000/k:8.0f} "
              f"{r['A_PV']:6.1f}% {r['C_D']:6.2f}% {r['exced']:7.1f} {r['horas']:7d} {r['pico']:8.0f}")

print("\n--- G) EFECTO AISLADO DE PASAR EL LUCERNARIO DE 5 GRD A HORIZONTAL ---")
for t, a, lab in [(5, -30, "hipotesis vieja 5 grd / -30"), (0, 0, "HORIZONTAL 0 grd")]:
    G, _ = poa(t, a)
    Px = p(k1a, t, a, 0.005, soil=0.020)
    print(f"  {lab:30s} GlobInc {G.sum()/1000:7.1f} kWh/m2   E_PV {Px.sum()/1000:6.1f} MWh   "
          f"{Px.sum()/1000*1000/k1a:5.0f} kWh/kWp")

print("\n--- H) SENSIBILIDAD DE LA TRANSPARENCIA DEL VIDRIO BIPV (V1a, 0 grd) ---")
print(f"{'VLT':>14s} {'Wp/m2':>7s} {'kWp':>7s} {'E_PV':>8s} {'C_D 3832':>9s} {'C_D 3467':>9s}")
for vlt, d in [("alta (>30 %)", 90), ("media (~20 %)", 125), ("baja (~10 %)", 160)]:
    kk = S_V1A * F_VIDRIO * d / 1000
    e = p(kk, 0, 0, 0.005, soil=0.020).sum() / 1000
    print(f"{vlt:>14s} {d:7d} {kk:7.1f} {e:8.1f} {e/ETOT*100:8.2f}% {e/EGEO*100:8.2f}%")

print("\n--- I) SENSIBILIDAD DE V1a A SOMBRAS Y SUCIEDAD (plano horizontal) ---")
print(f"{'sombras':>9s} {'suciedad':>9s} {'E_PV MWh':>9s} {'C_D 3832':>9s}")
for sh in (0.005, 0.05, 0.10, 0.15):
    for so in (0.020, 0.030):
        e = p(k1a, 0, 0, sh, soil=so).sum() / 1000
        print(f"{sh*100:8.1f}% {so*100:8.1f}% {e:9.1f} {e/ETOT*100:8.2f}%")

print("\n--- J) COMPARACION CONTRA LAS CIFRAS ANTERIORES ---")
k1a_old = 472 * 0.80 * 125 / 1000
k1b_old = (3111 - 472 - 408) * F_RETR * F_SHED * DENS / 1000
k2_old  = 3332.0 * F_MARQ * DENS / 1000
print(f"{'':26s} {'catastro/KMZ':>13s} {'rev.1 (lect.A)':>15s} {'rev.2 CERRADA':>14s}")
print(f"{'V1a kWp':26s} {k1a_old:13.1f} {57.9:15.1f} {k1a:14.2f}")
print(f"{'V1b kWp':26s} {k1b_old:13.1f} {304.56:15.2f} {k1b_cfg:14.2f}")
print(f"{'V2 kWp':26s} {k2_old:13.1f} {716.28:15.2f} {k2_r:14.2f}")

print("\n--- K) COHERENCIA GEOMETRICA: 3D FRENTE A CATASTRO / KMZ ---")
tot3d = S_V1A + S_V1B
for lab, ref in [("catastro", 3111.0), ("Google Earth", 3070.0), ("KMZ dibujado", 3020.0)]:
    print(f"  V1a+V1b 3D = {tot3d:8.1f} m2  vs  {lab:14s} {ref:7.1f} m2  -> {(tot3d/ref-1)*100:+6.1f}%")
print(f"  Con los patios YA excluidos, el forjado del 3D ({S_V1B:.1f} m2) supera en "
      f"{(S_V1B/2231-1)*100:+.1f} % el forjado de catastro (2.231 m2).")
print("  Se adopta la medicion 3D (fuente: catastro 1:1 trazado a mano en PVsyst) y se")
print("  declara la desviacion en la fase 1.4 de ERMA.")
