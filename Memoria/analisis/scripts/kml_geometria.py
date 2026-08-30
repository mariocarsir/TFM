# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET, math, io, sys
NS={'k':'http://www.opengis.net/kml/2.2'}
t=ET.parse('doc.kml'); r=t.getroot()

def txt(e,tag):
    x=e.find('k:'+tag,NS)
    return x.text.strip() if x is not None and x.text else None

def parse_coords(s):
    pts=[]
    for tok in s.replace('\n',' ').split():
        p=tok.split(',')
        if len(p)>=2: pts.append((float(p[0]),float(p[1])))
    return pts

def area_m2(pts):
    # proyeccion equirectangular local
    if len(pts)<3: return 0.0
    lat0=sum(p[1] for p in pts)/len(pts)
    R=6378137.0
    xy=[(math.radians(x)*R*math.cos(math.radians(lat0)), math.radians(y)*R) for x,y in pts]
    a=0.0
    for i in range(len(xy)):
        x1,y1=xy[i]; x2,y2=xy[(i+1)%len(xy)]
        a+=x1*y2-x2*y1
    return abs(a)/2.0

def perim_m(pts):
    lat0=sum(p[1] for p in pts)/len(pts); R=6378137.0
    xy=[(math.radians(x)*R*math.cos(math.radians(lat0)), math.radians(y)*R) for x,y in pts]
    return sum(math.dist(xy[i],xy[(i+1)%len(xy)]) for i in range(len(xy)))

# recorrer placemarks con su ruta de folders
out=[]
def walk(node,path):
    for ch in node:
        tag=ch.tag.split('}')[-1]
        if tag in ('Document','Folder'):
            n=txt(ch,'name') or ''
            walk(ch,path+[n])
        elif tag=='Placemark':
            n=txt(ch,'name') or ''
            for g,kind in [('Polygon','poly'),('LineString','line'),('Point','pt')]:
                for geo in ch.iter('{http://www.opengis.net/kml/2.2}'+g):
                    c=geo.find('.//k:coordinates',NS)
                    if c is None or not c.text: continue
                    pts=parse_coords(c.text)
                    out.append((path,n,kind,pts))
walk(r,[])

for path,n,kind,pts in out:
    p='/'.join([x for x in path if x])
    if kind=='poly':
        A=area_m2(pts)
        print(f"POLY  {p} | {n:28s} A={A:10.0f} m2 = {A/10000:7.3f} ha  perim={perim_m(pts):8.0f} m  n={len(pts)}")
    elif kind=='pt':
        print(f"PT    {p} | {n:28s} lon={pts[0][0]:.6f} lat={pts[0][1]:.6f}")
    else:
        L=perim_m(pts+[pts[0]])/2 if len(pts)>1 else 0
        # longitud real de la polilinea
        lat0=sum(q[1] for q in pts)/len(pts); R=6378137.0
        xy=[(math.radians(x)*R*math.cos(math.radians(lat0)), math.radians(y)*R) for x,y in pts]
        LL=sum(math.dist(xy[i],xy[i+1]) for i in range(len(xy)-1))
        print(f"LINE  {p} | {n:28s} L={LL:8.0f} m  n={len(pts)}")
