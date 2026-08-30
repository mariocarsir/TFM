import numpy as np, pandas as pd
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000
noIT=L-LIT
def produce(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
print("=== EFECTO DE SUSTITUIR AIR-COOLING POR GEOTERMIA (variante 1) ===")
print(f"  Consumo actual: total {ETOT:.0f} | IT {LIT.sum()/1000:.0f} | no-IT {noIT.sum()/1000:.0f} MWh/año | PUE {ETOT/(LIT.sum()/1000):.3f}")
COOL_FRAC=0.70                      # del no-IT, la parte que es refrigeracion (resto: UPS, iluminacion, aux)
cool=noIT.sum()/1000*COOL_FRAC
print(f"  Refrigeracion estimada: {cool:.0f} MWh/año ({COOL_FRAC*100:.0f} % del no-IT)")
for seer0,seer1 in [(3.2,5.0),(3.2,5.5),(3.0,6.0)]:
    new_cool=cool*seer0/seer1; ahorro=cool-new_cool
    newtot=ETOT-ahorro; newpue=newtot/(LIT.sum()/1000)
    print(f"  SEER {seer0} -> {seer1}: ahorro {ahorro:5.0f} MWh/año ({ahorro/ETOT*100:4.1f} %) | "
          f"nuevo consumo {newtot:6.0f} MWh | PUE {newpue:.3f}")
AHORRO=cool*(1-3.2/5.5); Lg=L*(ETOT-AHORRO)/ETOT; EG=Lg.sum()/1000
print(f"\n  --> escenario central adoptado: consumo pasa de {ETOT:.0f} a {EG:.0f} MWh/año (PUE 1,482 -> {EG/(LIT.sum()/1000):.3f})\n")
print("=== ESCENARIO COMBINADO EN EL PROPIO EMPLAZAMIENTO (V1a + V1b + V2) ===")
PARK=[3000,4500,6000]
V1a=produce(472*0.80*125/1000,5,-30,0.005,soil=0.020)
V1b=produce(3111-472-408 and (3111-472-408)*0.70*0.82*226.7/1000,10,-30,0.039)
print(f"{'Escenario':46s} {'kWp':>7s} {'E_PV':>7s} {'C_D vs 3832':>12s} {'C_D vs geot.':>13s} {'A_PV':>6s}")
print("-"*95)
for pk in PARK:
    V2=produce(pk*0.70*0.90*226.7/1000,8,-30,0.010)
    for lab,P,kwp in [("V1a+V1b (solo cubierta)",V1a+V1b,(472*0.8*125+ (3111-472-408)*0.7*0.82*226.7)/1000),
                      (f"V1a+V1b+V2 parking {pk} m2",V1a+V1b+V2,(472*0.8*125+(3111-472-408)*0.7*0.82*226.7+pk*0.7*0.9*226.7)/1000)]:
        if lab.startswith("V1a+V1b (") and pk!=PARK[0]: continue
        a=np.minimum(P,L).sum()/1000; ag=np.minimum(P,Lg).sum()/1000
        print(f"{lab:46s} {kwp:7.0f} {P.sum()/1000:7.0f} {a/ETOT*100:11.1f}% {ag/EG*100:12.1f}% {a/P.sum()*100:5.1f}%")
print("\n=== HUECO QUE QUEDA POR CUBRIR CON PLANTA EN SUELO (V3) ===")
U=produce(1,30,0,0.020)
V2m=produce(4500*0.70*0.90*226.7/1000,8,-30,0.010)
onsite=(V1a+V1b+V2m)
rest=EG-onsite.sum()/1000
print(f"  Con geotermia + toda la FV in-situ (parking 4.500 m2): quedan {rest:.0f} MWh/año por cubrir")
print(f"  V3 para cerrar el balance anual: {rest*1000/U.sum()/1000:.2f} MWp = {rest*1000/U.sum()*13.2/10000:.2f} ha")
