# -*- coding: utf-8 -*-
"""V2 recalculada con la huella de marquesinas medida en el KMZ (F1..F8)."""
import numpy as np
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); ETOT=L.sum()/1000
def p2(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
F=[479,433,419,142,224,404,383,361,487]
print(f"Marquesinas F1..F8 medidas en el KMZ: {sum(F)} m2 (recinto 'Parking - General' 6.252 m2)")
for lab,huella in [("hipotesis previa 2.461 x 0,70",2461*0.70),("KMZ: huella real F1..F8",sum(F))]:
    k=huella*0.90*226.7/1000; P=p2(k,8,-30,0.010)
    a=np.minimum(P,L).sum()/1000
    print(f"  {lab:32s} huella {huella:6.0f} m2 -> {k:6.1f} kWp | {P.sum()/1000:5.0f} MWh/ano | "
          f"A_PV {a/(P.sum()/1000)*100:5.1f} % | C_D {a/ETOT*100:5.2f} %")
