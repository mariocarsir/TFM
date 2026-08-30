# -*- coding: utf-8 -*-
"""V3 sobre la parcela de 58,8 ha: objetivo 99 %, escenarios combinados y dimensionado del BESS."""
import numpy as np, math
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000
OCU=13.2; ANETA=588401*0.85
def prod(kWp,tilt=30,az=0,shad=0.020,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
U=prod(1)
def sim(P,load,cap,eta=0.92,pm=None):
    pm=cap if pm is None else pm
    soc=0.;imp=0.;exc=0.;pd=[]
    for p,l in zip(P,load):
        n=p-l
        if n>0:
            ch=min(n,pm,(cap-soc)/eta); soc+=ch*eta; exc+=n-ch; pd.append(0)
        else:
            ds=min(-n,pm,soc*eta); soc-=ds/eta; imp+=(-n-ds); pd.append(ds)
    return (1-imp/load.sum())*100, exc/1000, imp/1000, max(pd) if pd else 0

print("="*80); print("A) OBJETIVO 99 % Y ASINTOTA"); print("="*80)
for obj in [98,99,99.5]:
    best=None
    for kWp in range(1000,25001,250):
        for cp in range(0,60001,500):
            cd,exc,imp,pdis=sim(U*kWp,L,cp)
            if cd>=obj:
                cost=kWp*0.55+cp*0.30
                if best is None or cost<best[0]: best=(cost,kWp,cp,cd,exc,imp,pdis)
                break
    if best:
        _,kWp,cp,cd,exc,imp,pdis=best
        print(f"  C_D >= {obj:4.1f} % -> FV {kWp/1000:5.2f} MWp ({kWp*OCU/10000:5.2f} ha, "
              f"{kWp*OCU/ANETA*100:4.1f} % parcela) + BESS {cp/1000:4.1f} MWh / {pdis/1000:4.2f} MW "
              f"| exced {exc:5.0f} MWh | red {imp:4.0f} MWh")
    else:
        print(f"  C_D >= {obj:4.1f} % -> no alcanzado hasta 25 MWp / 60 MWh")

print("\n"+"="*80); print("B) COMBINACION CON LO QUE YA HAY EN EL EMPLAZAMIENTO"); print("="*80)
# V1 (BIPV tragaluz + cubierta liberada) y V2 (marquesinas 2.461 m2) del analisis anterior
k1a=472*0.80*125/1000; k1b=(3111-472-408)*0.70*0.82*226.7/1000; k2=2461*0.70*0.90*226.7/1000
def prod2(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
ONS=prod2(k1a,5,-30,0.005,soil=0.020)+prod2(k1b,10,-30,0.039)+prod2(k2,8,-30,0.010)
kONS=k1a+k1b+k2
AH=0.70*(L-LIT).sum()/1000*(1-3.2/5.5); EG=ETOT-AH; Lg=L*EG/ETOT   # con geotermia
print(f"  FV in situ ya contabilizada (V1+V2): {kONS:.0f} kWp, {ONS.sum()/1000:.0f} MWh/ano")
print(f"  Demanda con geotermia: {EG:.0f} MWh/ano (-{AH:.0f} MWh)\n")
for lab,load,base in [("sin geotermia",L,ONS),("con geotermia",Lg,ONS)]:
    for obj in [80,95]:
        best=None
        for kWp in range(0,20001,250):
            for cp in range(0,40001,500):
                cd,exc,imp,pdis=sim(base+U*kWp,load,cp)
                if cd>=obj:
                    cost=kWp*0.55+cp*0.30
                    if best is None or cost<best[0]: best=(cost,kWp,cp,cd,exc,imp,pdis)
                    break
        if best:
            _,kWp,cp,cd,exc,imp,pdis=best
            print(f"  {lab} | C_D>={obj}% -> V3 {kWp/1000:5.2f} MWp ({kWp*OCU/10000:5.2f} ha, "
                  f"{kWp*OCU/ANETA*100:4.1f} % parcela) + BESS {cp/1000:4.1f} MWh  [real {cd:5.1f} %]")

print("\n"+"="*80); print("C) SI SE OCUPARA TODA LA PARCELA (planta comercial + PPA)"); print("="*80)
KM=ANETA/OCU
print(f"  {KM/1000:.1f} MWp | {KM*U.sum()/1e6:.1f} GWh/ano | pico {(U*KM).max()/1000:.1f} MW")
a=np.minimum(U*KM,L).sum()/1000
print(f"  Autoconsumido directo por el CPD: {a:.0f} MWh ({a/ETOT*100:.1f} % de su consumo) "
      f"-> el {(1-a/(KM*U.sum()/1000))*100:.1f} % de la produccion se vertiria a red")
