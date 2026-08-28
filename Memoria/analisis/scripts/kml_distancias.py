# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, math, sys, io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
NS={'k':'http://www.opengis.net/kml/2.2'}
r=ET.parse('kmz/doc.kml').getroot(); R=6378137.0
pm_all=[]
for pm in r.iter('{http://www.opengis.net/kml/2.2}Placemark'):
    n=pm.find('k:name',NS); nm=n.text.strip() if n is not None and n.text else ''
    for g in ('Point','Polygon'):
        for geo in pm.iter('{http://www.opengis.net/kml/2.2}'+g):
            c=geo.find('.//k:coordinates',NS)
            if c is None or not c.text: continue
            pts=[(float(t.split(',')[0]),float(t.split(',')[1])) for t in c.text.split() if ',' in t]
            pm_all.append((nm,g,pts))
def xy(p,lat0): return (math.radians(p[0])*R*math.cos(math.radians(lat0)), math.radians(p[1])*R)
lat0=40.60
LAY=[x for x in pm_all if x[0]=='Layout1'][0][2]
CPD=[x for x in pm_all if x[0]=='CPD' and x[1]=='Point'][0][2][0]
Q=[xy(p,lat0) for p in LAY]; c=xy(CPD,lat0)
cx=sum(q[0] for q in Q)/len(Q); cy=sum(q[1] for q in Q)/len(Q)
def seg_d(p,a,b):
    ax,ay=a; bx,by=b; px,py=p; dx,dy=bx-ax,by-ay
    t=0 if dx==dy==0 else max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-(ax+t*dx),py-(ay+t*dy))
def d2lay(p):
    q=xy(p,lat0); return min(seg_d(q,Q[i],Q[(i+1)%len(Q)]) for i in range(len(Q)))
# rumbo parcela desde el CPD
ang=math.degrees(math.atan2(cx-c[0],cy-c[1]))%360
rumbo=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSO","SO","OSO","O","ONO","NO","NNO"][int((ang+11.25)//22.5)%16]
print(f"Parcela: centroide a {math.dist(c,(cx,cy))/1000:.2f} km del CPD, rumbo {ang:.0f}° ({rumbo})")
print(f"         borde mas cercano al CPD: {d2lay(CPD)/1000:.2f} km\n")
print(f"{'Subestacion / punto':45s} {'d(CPD)':>8s} {'d(parcela)':>11s}")
print("-"*68)
seen=set()
for nm,g,pts in pm_all:
    if g!='Point' or nm in ('CPD','Parking') or nm in seen: continue
    seen.add(nm)
    p=pts[0]; q=xy(p,lat0)
    print(f"{' '.join(nm.split())[:45]:45s} {math.dist(c,q)/1000:7.2f} km {d2lay(p)/1000:9.2f} km")
