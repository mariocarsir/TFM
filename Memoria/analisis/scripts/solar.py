import numpy as np, pandas as pd
LAT,LON,TZ,ALT=40.60,-3.72,1,741
# GlobHor y DiffHor mensuales del informe PVsyst (PVGIS 5.3 TMY, Tres Cantos)
GH=[79.2,95.3,149.8,151.5,207.5,232.2,240.9,207.4,167.1,116.6,72.4,65.9]
DH=[22.95,27.77,45.66,68.96,76.51,72.53,60.21,49.78,46.02,37.82,28.28,21.96]
TA=[3.48,6.15,10.02,9.79,17.21,23.55,27.55,25.85,21.91,12.80,7.02,4.82]
idx=pd.date_range("2025-01-01 00:30",periods=8760,freq="h")
doy=idx.dayofyear.values; hh=idx.hour.values+0.5; mo=idx.month.values
# --- posicion solar (NOAA simplificado) ---
g=2*np.pi/365*(doy-1)
eqt=229.18*(0.000075+0.001868*np.cos(g)-0.032077*np.sin(g)-0.014615*np.cos(2*g)-0.040849*np.sin(2*g))
dec=(0.006918-0.399912*np.cos(g)+0.070257*np.sin(g)-0.006758*np.cos(2*g)+0.000907*np.sin(2*g)
     -0.002697*np.cos(3*g)+0.00148*np.sin(3*g))
tst=hh*60+eqt+4*LON-60*TZ
ha=np.radians(tst/4-180)
la=np.radians(LAT)
cz=np.sin(la)*np.sin(dec)+np.cos(la)*np.cos(dec)*np.cos(ha)
cz=np.clip(cz,-1,1); z=np.arccos(cz); el=np.pi/2-z
saz=np.arctan2(np.sin(ha),np.cos(ha)*np.sin(la)-np.tan(dec)*np.cos(la))  # 0=Sur,+O
E0=1367*(1+0.033*np.cos(2*np.pi*doy/365))
I0h=np.maximum(E0*cz,0)
# --- reparto horario de la GlobHor mensual, proporcional a cielo claro (Haurwitz) ---
am=np.where(cz>0.01,1/np.maximum(cz,0.01),0)
cs=np.where(cz>0.01,1098*cz*np.exp(-0.059*am),0)
gh=np.zeros(8760); dh=np.zeros(8760)
for m in range(1,13):
    k=mo==m; s=cs[k].sum()
    gh[k]=cs[k]/s*GH[m-1]*1000            # Wh/m2 por hora
    kt_m=DH[m-1]/GH[m-1]
    # fraccion difusa horaria via Erbs sobre el kt horario, reescalada al total mensual
    kt=np.where(I0h[k]>1,gh[k]/np.maximum(I0h[k],1),0)
    fd=np.where(kt<=0.22,1-0.09*kt,np.where(kt<=0.8,0.9511-0.1604*kt+4.388*kt**2-16.638*kt**3+12.336*kt**4,0.165))
    d=gh[k]*np.clip(fd,0,1); d*= (DH[m-1]*1000)/max(d.sum(),1)
    dh[k]=np.minimum(d,gh[k])
bh=gh-dh
bn=np.where(cz>0.05,bh/np.maximum(cz,0.05),0)
Tamb=np.array([TA[m-1] for m in mo])+6*np.sin(np.pi*np.clip((hh-6)/12,0,1))-3
def poa(tilt_deg,az_deg,albedo=0.20):
    """Hay-Davies. az: 0=Sur, negativo=Este (convenio PVsyst)."""
    b=np.radians(tilt_deg); ga=np.radians(az_deg)
    ci=(np.sin(dec)*np.sin(la)*np.cos(b)-np.sin(dec)*np.cos(la)*np.sin(b)*np.cos(ga)
        +np.cos(dec)*np.cos(la)*np.cos(b)*np.cos(ha)
        +np.cos(dec)*np.sin(la)*np.sin(b)*np.cos(ga)*np.cos(ha)
        +np.cos(dec)*np.sin(b)*np.sin(ga)*np.sin(ha))
    ci=np.maximum(ci,0)
    Ai=np.clip(bn/1367,0,1)
    Rb=np.where(cz>0.05,ci/np.maximum(cz,0.05),0)
    dif=dh*(Ai*Rb+(1-Ai)*(1+np.cos(b))/2)
    ref=gh*albedo*(1-np.cos(b))/2
    return np.maximum(bh*Rb+dif+ref,0), ci
# --- CALIBRACION contra el trabajo previo: 10 grados / -30 grados ---
G,_=poa(10,-30)
print(f"CALIBRACION  GlobHor modelo = {gh.sum()/1000:8.1f} kWh/m2  (PVsyst 1785,8)")
print(f"             DiffHor modelo = {dh.sum()/1000:8.1f} kWh/m2  (PVsyst  558,4)")
print(f"             GlobInc 10/-30 = {G.sum()/1000:8.1f} kWh/m2  (PVsyst 1937,6)  desv {(G.sum()/1000/1937.6-1)*100:+.1f}%")
np.save("gh.npy",gh); np.save("dh.npy",dh); np.save("bh.npy",bh); np.save("bn.npy",bn)
np.save("cz.npy",cz); np.save("Tamb.npy",Tamb)
print("\n--- GlobInc anual (kWh/m2) por configuracion ---")
for t,a,lab in [(0,0,"horizontal"),(5,-30,"tragaluz 5 grd"),(10,-30,"cubierta previa 10 grd"),
                (15,-30,"15 grd"),(25,0,"25 grd Sur"),(30,0,"30 grd Sur"),(35,0,"35 grd Sur"),(37,0,"37 grd Sur (optimo)")]:
    Gx,_=poa(t,a); print(f"  {lab:24s} {Gx.sum()/1000:7.1f}   ({Gx.sum()/gh.sum():.3f} x GlobHor)")
