import numpy as np
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000
def prod(kWp,tilt,az,shad,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
V1a=prod(472*0.80*125/1000,5,-30,0.005,soil=0.020); k1a=472*0.80*125/1000
k1b=(3111-472-408)*0.70*0.82*226.7/1000; V1b=prod(k1b,10,-30,0.039)
print(f"{'Escenario':44s} {'kWp':>6s} {'E_PV':>6s} {'A_PV':>6s} {'C_D':>6s} {'exced':>6s}")
print("-"*80)
def row(lab,P,k):
    a=np.minimum(P,L).sum()/1000; e=P.sum()/1000
    print(f"{lab:44s} {k:6.0f} {e:6.0f} {a/e*100:5.1f}% {a/ETOT*100:5.1f}% {e-a:6.0f}")
row("V1a  BIPV tragaluz",V1a,k1a)
row("V1b  Cubierta convencional (post-geotermia)",V1b,k1b)
row("V1   = V1a + V1b",V1a+V1b,k1a+k1b)
for pk in [3000,4500,6000]:
    k2=pk*0.70*0.90*226.7/1000; row(f"V2   Marquesinas parking {pk} m2",prod(k2,8,-30,0.010),k2)
for hect in [1,2,2.81]:
    k3=hect*10000/13.2; row(f"V3   Planta suelo {hect} ha",prod(k3,30,0,0.020),k3)
print()
k2=4500*0.70*0.90*226.7/1000
row("TODO in-situ (V1+V2 4.500 m2)",V1a+V1b+prod(k2,8,-30,0.010),k1a+k1b+k2)
