"""Cálculo auxiliar de `seleccion-modulos-por-variante.md` (27/09/2026).

Densidad (W/m²), n.º de módulos y kWp sobre las superficies netas ya cerradas,
longitud máxima de string por tensión y ocupación orientativa de la V3.
Datos de ficha: ver §8 del documento (fuentes). Tmín = −10 °C es PROVISIONAL
(pendiente de AEMET, fase 1.3).
"""
import math

T_MIN = -10.0          # °C, provisional
DT = 25.0 - T_MIN      # 35 K

# nombre: (Pmax W, largo m, ancho m, Voc V, beta_Voc %/°C, Isc A, Vsys V)
MODULOS = {
    "AIKO-A475-MAH54Mw (monovidrio)": (475, 1.757, 1.134, 41.24, -0.22, 14.35, 1500),
    "AIKO-A475-MAH54Dw (vidrio-vidrio)": (475, 1.757, 1.134, 41.24, -0.22, 14.35, 1500),
    "REC Alpha Pure-RX 470": (470, 1.728, 1.205, 65.7, -0.24, 8.95, 1000),
    "LONGi LR7-54HTH-465M": (465, 1.800, 1.134, 39.55, -0.23, 14.93, 1500),
    "Trina TSM-440NEG9RC.27": (440, 1.762, 1.134, 52.2, -0.24, 10.67, 1500),
    "Jinko JKM525N-54HL4M-BDV": (525, 1.961, 1.134, 41.23, -0.25, 15.88, 1500),
    "LONGi LR8-66HYD-670M": (670, 2.382, 1.134, 50.12, -0.200, 16.86, 1500),
    "JA JAM66D45-630/LB": (630, 2.382, 1.134, 48.90, -0.250, 16.18, 1500),
    "Trina TSM-620NEG19RC.20": (620, 2.382, 1.134, 49.6, -0.24, 15.91, 1500),
}

SUPERFICIE_NETA = {"V1b": 1582.5, "V2": 3182.4}   # m² de módulo
GCR_V3, EXTRA_V3 = 0.40, 1.20                      # estimacion-preliminar-variantes.md §5.4

for nombre, (p, largo, ancho, voc, beta, isc, vsys) in MODULOS.items():
    area = largo * ancho
    dens = p / area
    voc_max = voc * (1 + (-beta / 100) * DT)
    linea = f"{nombre:36s} A={area:.4f} m²  {dens:6.1f} W/m²  Voc(Tmín)={voc_max:6.2f} V"
    for vinv in (1000, 1100, 1500):
        linea += f"  Ns@{vinv}={math.floor(min(vinv, vsys) / voc_max)}"
    for var, sup in SUPERFICIE_NETA.items():
        n = math.floor(sup / area)
        linea += f" | {var}: {n} uds {n * p / 1000:.1f} kWp"
    m2_kwp = 1 / (dens / 1000 * GCR_V3) * EXTRA_V3
    linea += f" | V3: {m2_kwp:.2f} m²/kWp = {10000 / m2_kwp:.0f} kWp/ha"
    print(linea)
