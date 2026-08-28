# -*- coding: utf-8 -*-
"""Variante 3 sobre la parcela del KMZ (Layout1, 58,8 ha): capacidad y cobertura con BESS."""
import numpy as np, math, xml.etree.ElementTree as ET
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy"); LIT=np.load("LIT.npy"); ETOT=L.sum()/1000

# ---------- geometria de la parcela ----------
NS={'k':'http://www.opengis.net/kml/2.2'}
r=ET.parse('kmz/doc.kml').getroot()
R=6378137.0
def pts_of(name):
    for pm in r.iter('{http://www.opengis.net/kml/2.2}Placemark'):
        n=pm.find('k:name',NS)
        if n is not None and n.text and n.text.strip()==name:
            c=pm.find('.//k:coordinates',NS)
            return [(float(t.split(',')[0]),float(t.split(',')[1])) for t in c.text.split() if ',' in t]
P=pts_of('Layout1'); CPD=pts_of('CPD')[0]
lat0=sum(p[1] for p in P)/len(P)
def xy(p): return (math.radians(p[0])*R*math.cos(math.radians(lat0)), math.radians(p[1])*R)
Q=[xy(p) for p in P]; c=xy(CPD)
A=abs(sum(Q[i][0]*Q[(i+1)%len(Q)][1]-Q[(i+1)%len(Q)][0]*Q[i][1] for i in range(len(Q))))/2
cx=sum(q[0] for q in Q)/len(Q); cy=sum(q[1] for q in Q)/len(Q)
def seg_d(p,a,b):
    ax,ay=a; bx,by=b; px,py=p; dx,dy=bx-ax,by-ay
    t=0 if dx==dy==0 else max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-(ax+t*dx),py-(ay+t*dy))
dmin=min(seg_d(c,Q[i],Q[(i+1)%len(Q)]) for i in range(len(Q)))
dmax=max(math.dist(c,q) for q in Q)
W=max(q[0] for q in Q)-min(q[0] for q in Q); H=max(q[1] for q in Q)-min(q[1] for q in Q)
print("="*78)
print("PARCELA CANDIDATA (poligono 'Layout1' del TFM.kmz)")
print("="*78)
print(f"  Superficie bruta            {A:9.0f} m2 = {A/10000:6.2f} ha")
print(f"  Envolvente aprox.           {W:6.0f} m (E-O) x {H:6.0f} m (N-S)")
print(f"  Distancia CPD -> borde mas cercano  {dmin/1000:5.2f} km   (punto mas lejano {dmax/1000:5.2f} km)")

# ---------- capacidad instalable ----------
OCU=13.2                      # m2 de parcela por kWp (GCR 0,40 fijo 30 grd + viales/margenes/CT)
for util,lab in [(1.00,"bruto teorico"),(0.85,"neto realista (servidumbres, drenaje, retranqueos)")]:
    kw=A*util/OCU
    print(f"  Capacidad {lab:52s} {kw/1000:7.2f} MWp")
Aneta=A*0.85; KWMAX=Aneta/OCU

U=produce=None
def prod(kWp,tilt=30,az=0,shad=0.020,soil=0.010):
    G,_=poa(tilt,az); Geff=G*0.999*(1-shad)*(1-soil)*(1-0.019); Tc=Tamb+Geff/20.0
    return np.maximum(kWp*(Geff/1000)*(1-0.0024*(Tc-25))*0.991*1.005*0.979*0.990*0.985*0.998,0)
U=prod(1); YF=U.sum()
print(f"\n  Y_F (30 grd Sur, Tres Cantos)      {YF:6.0f} kWh/kWp/ano")
print(f"  Produccion si se ocupa TODA la parcela: {KWMAX*YF/1e6:6.1f} GWh/ano "
      f"= {KWMAX*YF/1000/ETOT:5.1f} veces el consumo anual del CPD ({ETOT:.0f} MWh)")
print(f"  Potencia pico de esa planta        {(U*KWMAX).max()/1000:6.1f} MW  frente a los "
      f"{L.max()/1000:.2f} MW de punta del CPD")

# ---------- barrido FV + BESS ----------
def sim(kWp,cap,eta=0.92,pmax=None):
    P=U*kWp; soc=0.0; imp=0.0; exc=0.0
    pm=cap if pmax is None else pmax        # C-rate 1 por defecto
    for p,l in zip(P,L):
        n=p-l
        if n>0:
            ch=min(n,pm,(cap-soc)/eta); soc+=ch*eta; exc+=n-ch
        else:
            ds=min(-n,pm,soc*eta); soc-=ds/eta; imp+=(-n-ds)
    return (1-imp/L.sum())*100, exc/1000, imp/1000

print("\n"+"="*78)
print("AUTOSUFICIENCIA REAL (C_D) SEGUN FV INSTALADA Y BATERIA")
print("="*78)
caps=[0,1000,2000,3000,4000,6000,8000,12000]
print(f"{'MWp':>6s} {'ha':>6s} {'%parc':>6s} " + "".join(f"{c/1000:7.1f}" for c in caps))
print(f"{'':>6s} {'':>6s} {'':>6s} " + "".join(f"{'MWh':>7s}" for c in caps))
print("-"*78)
grid={}
for kWp in [1000,1500,2000,2500,3000,4000,5000,7000,10000]:
    row=""
    for cp in caps:
        cd,_,_=sim(kWp,cp); grid[(kWp,cp)]=cd; row+=f"{cd:7.1f}"
    print(f"{kWp/1000:6.2f} {kWp*OCU/10000:6.2f} {kWp*OCU/Aneta*100:5.1f}% {row}")

print("\n"+"="*78)
print("CONFIGURACIONES MINIMAS PARA CADA OBJETIVO (busqueda fina)")
print("="*78)
for obj in [80,90,95,100]:
    best=None
    for kWp in range(500,20001,250):
        for cp in range(0,40001,500):
            cd,exc,imp=sim(kWp,cp)
            if cd>=obj:
                cost=kWp*0.55+cp*0.30      # indice relativo: 0,55 kEUR/kWp FV + 0,30 kEUR/kWh BESS
                if best is None or cost<best[0]: best=(cost,kWp,cp,cd,exc,imp)
                break
    if best:
        _,kWp,cp,cd,exc,imp=best
        print(f"  C_D >= {obj:3d} %  ->  FV {kWp/1000:5.2f} MWp ({kWp*OCU/10000:5.2f} ha = "
              f"{kWp*OCU/Aneta*100:4.1f} % de la parcela) + BESS {cp/1000:5.1f} MWh  "
              f"[C_D real {cd:5.1f} %, excedentes {exc:5.0f} MWh, red {imp:4.0f} MWh]")
    else:
        print(f"  C_D >= {obj:3d} %  ->  INALCANZABLE dentro del barrido (hasta 20 MWp / 40 MWh)")
