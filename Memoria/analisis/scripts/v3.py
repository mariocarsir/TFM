import numpy as np, pandas as pd
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); ETOT=L.sum()/1000
def produce(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019)
    Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
U=produce(1,30,0,0.020); YF=U.sum()   # kWh/kWp/ano unitario
print(f"Planta en suelo 30 grd Sur, Tres Cantos:  Y_F = {YF:.0f} kWh/kWp/ano")
print(f"Ocupacion:  13,2 m2/kWp  =  1,32 ha/MWp  (GCR 0,40 + 20 % viales/margenes/CT)\n")
print("=== A) COBERTURA EN BALANCE ANUAL NETO (excedentes vertidos y compensados) ===")
for pct in [50,80,100]:
    E=ETOT*pct/100; kWp=E*1000/YF; ha=kWp*13.2/10000
    P=U*kWp; auto=np.minimum(P,L).sum()/1000
    print(f"  {pct:3d} % del consumo -> {kWp/1000:5.2f} MWp | {ha:5.2f} ha ({kWp*13.2:7.0f} m2) | "
          f"E_PV {E:6.0f} MWh | autoconsumo real {auto:5.0f} MWh = C_D {auto/ETOT*100:4.1f} % | "
          f"excedentes {E-auto:5.0f} MWh ({(E-auto)/E*100:4.1f} %) | pico {P.max()/1000:4.2f} MW")
print("\n=== B) AUTOSUFICIENCIA REAL SIN BATERIA (C_D) frente a potencia instalada ===")
print(f"{'MWp':>6s} {'ha':>6s} {'E_PV MWh':>9s} {'C_D %':>7s} {'A_PV %':>7s} {'exced MWh':>10s}")
best=0
for kWp in [250,500,757,1000,1500,2000,2130,3000,5000,10000,20000]:
    P=U*kWp; a=np.minimum(P,L).sum()/1000; e=P.sum()/1000
    print(f"{kWp/1000:6.2f} {kWp*13.2/10000:6.2f} {e:9.0f} {a/ETOT*100:7.2f} {a/e*100:7.1f} {e-a:10.0f}")
    best=max(best,a/ETOT*100)
print(f"\n  ASINTOTA: con potencia infinita el C_D sin bateria satura en "
      f"{np.minimum(U*1e9,L).sum()/L.sum()*100:.1f} % -> es la fraccion del consumo que ocurre de dia.")
print("\n=== C) QUE HARIA FALTA PARA 80 % REAL: FV + BATERIA ===")
def sim(kWp,cap,eta=0.92):
    P=U*kWp; soc=0.0; imp=0.0
    for p,l in zip(P,L):
        net=p-l
        if net>0:
            ch=min(net,(cap-soc)/eta*1.0); soc+=ch*eta
        else:
            ds=min(-net,soc*eta); soc-=ds/eta; imp+= (-net-ds)
    return 1-imp/L.sum()
for kWp,cap in [(2130,0),(2130,2000),(2500,3000),(3000,4000),(3500,5000),(4000,6000)]:
    cd=sim(kWp,cap)*100
    print(f"  FV {kWp/1000:4.2f} MWp ({kWp*13.2/10000:4.2f} ha) + bateria {cap/1000:4.1f} MWh -> C_D {cd:5.1f} %")
