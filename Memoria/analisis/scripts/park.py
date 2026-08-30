import numpy as np
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000
def prod(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
PARK=2461.
k2=PARK*0.70*0.90*226.7/1000; V2=prod(k2,8,-30,0.010)
k1a=472*0.80*125/1000; V1a=prod(k1a,5,-30,0.005,soil=0.020)
k1b=(3111-472-408)*0.70*0.82*226.7/1000; V1b=prod(k1b,10,-30,0.039)
AH=0.70*(L-LIT).sum()/1000*(1-3.2/5.5); EG=ETOT-AH; Lg=L*EG/ETOT
def row(lab,P,k):
    a=np.minimum(P,L).sum()/1000; e=P.sum()/1000; ag=np.minimum(P,Lg).sum()/1000
    print(f"{lab:38s} {k:7.1f} {e:7.0f} {a/e*100:6.1f}% {a/ETOT*100:6.1f}% {ag/EG*100:7.1f}% {e-a:6.0f}")
print(f"PARKING = {PARK:.0f} m2   ->  marquesina {PARK*0.70:.0f} m2   modulo {PARK*0.70*0.90:.0f} m2")
print()
print(f"{'Escenario':38s} {'kWp':>7s} {'E_PV':>7s} {'A_PV':>7s} {'C_D':>7s} {'C_Dgeo':>8s} {'exced':>6s}")
print("-"*82)
row("V2  Marquesinas parking (2.461 m2)",V2,k2)
row("V1a+V1b  (cubierta completa)",V1a+V1b,k1a+k1b)
row("V1+V2  TODO in-situ",V1a+V1b+V2,k1a+k1b+k2)
U=prod(1,30,0,0.020)
ons=(V1a+V1b+V2).sum()/1000
print()
print("=== HUECO RESTANTE PARA LA PLANTA EN SUELO ===")
for lab,dem in [("sin geotermia (3.832 MWh)",ETOT),("con geotermia (%.0f MWh)"%EG,EG)]:
    r=dem-ons; kw=r*1000/U.sum()
    print(f"  {lab:32s}: faltan {r:6.0f} MWh -> V3 = {kw/1000:5.2f} MWp = {kw*13.2/10000:5.2f} ha ({kw*13.2:6.0f} m2)")
print()
print("=== CONJUNTO COMPLETO V1+V2+V3 (con geotermia, balance anual 100 %) ===")
kw3=(EG-ons)*1000/U.sum(); TOT=V1a+V1b+V2+prod(kw3,30,0,0.020)
a=np.minimum(TOT,Lg).sum()/1000
print(f"  Potencia total {k1a+k1b+k2+kw3:.0f} kWp | E_PV {TOT.sum()/1000:.0f} MWh | C_D real {a/EG*100:.1f} % | excedentes {TOT.sum()/1000-a:.0f} MWh")
def sim(P,load,cap,eta=0.92):
    soc=0.;imp=0.
    for p,l in zip(P,load):
        n=p-l
        if n>0: soc+=min(n,(cap-soc)/eta)*eta
        else:
            ds=min(-n,soc*eta); soc-=ds/eta; imp+=(-n-ds)
    return (1-imp/load.sum())*100
print()
print("  Con bateria sobre ese conjunto:")
for cap in [1000,2000,3000,4000]:
    print(f"    {cap/1000:4.1f} MWh -> C_D {sim(TOT,Lg,cap):5.1f} %")
