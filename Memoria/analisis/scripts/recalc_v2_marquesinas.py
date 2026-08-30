# -*- coding: utf-8 -*-
"""Recalculo completo con V2 = 3.332 m2 de huella de marquesinas (F1..F8 del TFM.kmz)."""
import numpy as np
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000
OCU=13.2; ANETA=588401*0.85
def p(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)

HUELLA=3332.0                       # F1..F8 medidas en el KMZ, confirmado por Mario
k1a=472*0.80*125/1000               # BIPV tragaluz
k1b=(3111-472-408)*0.70*0.82*226.7/1000   # cubierta liberada por la geotermia
k2 =HUELLA*0.90*226.7/1000          # marquesinas
V1a=p(k1a,5,-30,0.005,soil=0.020); V1b=p(k1b,10,-30,0.039); V2=p(k2,8,-30,0.010)
U=p(1,30,0,0.020)                   # planta en suelo unitaria

AH=0.70*(L-LIT).sum()/1000*(1-3.2/5.5); EG=ETOT-AH; Lg=L*EG/ETOT
print(f"Huella marquesinas {HUELLA:.0f} m2 -> modulo {HUELLA*0.90:.0f} m2 -> {k2:.1f} kWp")
print(f"Demanda: total {ETOT:.0f} MWh | con geotermia {EG:.0f} MWh (-{AH:.0f})\n")

def row(lab,P,k):
    e=P.sum()/1000; a=np.minimum(P,L).sum()/1000; ag=np.minimum(P,Lg).sum()/1000
    print(f"{lab:34s} {k:7.1f} {e:7.0f} {a/e*100:6.1f}% {a/ETOT*100:6.1f}% {ag/EG*100:7.1f}% {e-a:7.0f}")
    return e,a
print(f"{'Escenario':34s} {'kWp':>7s} {'E_PV':>7s} {'A_PV':>7s} {'C_D':>7s} {'C_Dgeo':>8s} {'exced':>7s}")
print("-"*82)
row("V1a BIPV tragaluz",V1a,k1a)
row("V1b Cubierta liberada",V1b,k1b)
row("V1 total",V1a+V1b,k1a+k1b)
row("V2 Marquesinas (3.332 m2)",V2,k2)
ONS=V1a+V1b+V2; kONS=k1a+k1b+k2
row("V1+V2 TODO in situ",ONS,kONS)

print("\n=== HUECO RESTANTE PARA LA PLANTA EN SUELO (balance anual) ===")
for lab,dem in [("sin geotermia",ETOT),("con geotermia",EG)]:
    r=dem-ONS.sum()/1000; kw=r*1000/U.sum()
    print(f"  {lab:16s}: faltan {r:6.0f} MWh -> V3 = {kw/1000:5.2f} MWp = {kw*OCU/10000:5.2f} ha "
          f"({kw*OCU/ANETA*100:4.1f} % de la parcela)")

def sim(P,load,cap,eta=0.92,pm=None):
    pm=cap if pm is None else pm
    soc=0.;imp=0.;exc=0.;pd=0.
    for a,l in zip(P,load):
        n=a-l
        if n>0:
            ch=min(n,pm,(cap-soc)/eta); soc+=ch*eta; exc+=n-ch
        else:
            ds=min(-n,pm,soc*eta); soc-=ds/eta; imp+=(-n-ds); pd=max(pd,ds)
    return (1-imp/load.sum())*100, exc/1000, imp/1000, pd

def min_cap(P,load,obj,hi=60000.):
    if sim(P,load,hi)[0]<obj: return None
    if sim(P,load,0.)[0]>=obj: return 0.
    lo=0.
    for _ in range(14):
        m=(lo+hi)/2
        if sim(P,load,m)[0]>=obj: hi=m
        else: lo=m
    return hi
def buscar(base,load,obj,kmax=12000,step=250):
    best=None
    for kw in range(0,kmax+1,step):
        c=min_cap(base+U*kw,load,obj)
        if c is None: continue
        cost=kw*0.55+c*0.30
        if best is None or cost<best[0]: best=(cost,kw,c)
    if best is None: return None
    _,kw,c=best; cd,exc,imp,pd=sim(base+U*kw,load,c)
    return kw,c,cd,exc,imp,pd

print("\n=== V3 + BESS NECESARIOS SOBRE V1+V2 (autosuficiencia REAL) ===")
for lab,load in [("sin geotermia",L),("con geotermia",Lg)]:
    for obj in [80,90,95,99]:
        r=buscar(ONS,load,obj)
        if r is None: print(f"  {lab:14s} {obj:2d}% -> inalcanzable"); continue
        kw,c,cd,exc,imp,pd=r
        print(f"  {lab:14s} {obj:2d}% -> V3 {kw/1000:5.2f} MWp ({kw*OCU/10000:5.2f} ha = {kw*OCU/ANETA*100:4.1f} % parcela)"
              f" + BESS {c/1000:5.2f} MWh / {pd/1000:4.2f} MW | total FV {(kONS+kw)/1000:5.2f} MWp | real {cd:5.1f} %")

print("\n=== ESCALERA DE BATERIA SOBRE EL CONJUNTO DE BALANCE ANUAL (con geotermia) ===")
kw3=(EG-ONS.sum()/1000)*1000/U.sum(); TOT=ONS+U*kw3
print(f"  V1+V2+V3 = {kONS+kw3:.0f} kWp ({kw3/1000:.2f} MWp en suelo), E_PV {TOT.sum()/1000:.0f} MWh")
for cap in [0,1000,2000,3000,4000,6000]:
    cd,exc,imp,pd=sim(TOT,Lg,cap)
    print(f"    BESS {cap/1000:4.1f} MWh -> C_D real {cd:5.1f} % (excedentes {exc:5.0f} MWh, red {imp:4.0f} MWh)")

print("\n=== OBJETIVO 80 % EERR DEL BORRADOR DE RD ===")
for lab,load,dem in [("sin geotermia",L,ETOT),("con geotermia",Lg,EG)]:
    r=buscar(ONS,load,80)
    kw,c,cd,_,imp,_=r
    print(f"  {lab:14s}: {kw*OCU/10000:.2f} ha + {c/1000:.1f} MWh -> {cd:.1f} % real; "
          f"quedarian {imp:.0f} MWh/ano de red ({imp/dem*100:.1f} %)")
