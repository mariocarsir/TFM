# -*- coding: utf-8 -*-
"""Viabilidad tecnica de una linea directa CPD <-> planta FV (3 km) en BT frente a MT.

Responde a la objecion de que 3 km de linea directa son imposibles: lo son en baja
tension, no en media. Caida de tension y perdidas por el metodo clasico trifasico:
    dU = raiz(3) * I * (R*cos(phi) + X*sin(phi))
    P_perdidas = 3 * I^2 * R
"""
import math

L_KM   = 3.0        # longitud de la linea directa
P_MW   = 2.5        # potencia a transportar (planta en suelo del TFM)
COSPHI = 1.0        # la FV se opera a factor de potencia unidad

# (tension_V, etiqueta, R_ohm_km, X_ohm_km, n_conductores_por_fase)
CASOS = [
    (  400, "BT 400 V, 240 mm2 Al x1/fase",   0.125, 0.080,  1),
    (  400, "BT 400 V, 240 mm2 Al x10/fase",  0.125, 0.080, 10),
    (20000, "MT 20 kV, 150 mm2 Al subterr.",  0.206, 0.110,  1),
    (20000, "MT 20 kV, LA-110 aereo",         0.307, 0.400,  1),
]

print(f"Linea directa de {L_KM:.1f} km transportando {P_MW:.2f} MW (cos phi = {COSPHI})\n")
print(f"{'Caso':34s} {'I (A)':>9s} {'dU (V)':>9s} {'dU (%)':>8s} {'Perd (kW)':>10s} {'Perd (%)':>9s}")
print("-" * 84)
for U, lab, r_km, x_km, n in CASOS:
    I = P_MW * 1e6 / (math.sqrt(3) * U * COSPHI)
    R = r_km * L_KM / n
    X = x_km * L_KM / n
    dU = math.sqrt(3) * I * (R * COSPHI + X * math.sin(math.acos(COSPHI)))
    pl = 3 * I**2 * R / 1000
    print(f"{lab:34s} {I:9.0f} {dU:9.0f} {dU/U*100:7.1f}% {pl:10.1f} {pl/(P_MW*1000)*100:8.2f}%")

print("""
Lectura: en BT la corriente es de ~3.600 A y ni con diez conductores de 240 mm2 por
fase la caida de tension baja del 58 %: inviable, como se habia anticipado. En MT a
20 kV la misma potencia son ~72 A, con caida y perdidas por debajo del 0,5 %: es una
linea de distribucion completamente ordinaria. La objecion a la linea directa es, por
tanto, una objecion a hacerla en baja tension, no al concepto.""")
