import numpy as np, pandas as pd
exec(open("solar.py").read().split("# --- CALIBRACION")[0])
L=np.load("L.npy")
def produce(kWp,tilt,az,shad,eff_stc=0.2259,gamma=-0.0024,
            soil=0.010,iam=0.019,hor=0.001,irr=0.009,qual=-0.005,mism=0.021,ohm=0.010,
            inv=0.015,unav=0.002,Uc=20.0,bifac=0.0):
    G,_=poa(tilt,az)
    Geff=G*(1-hor)*(1-shad)*(1-soil)*(1-iam)*(1+bifac)
    Tc=Tamb+Geff/Uc                                   # Faiman, Uv=0
    Pdc=kWp*(Geff/1000)*(1+gamma*(Tc-25))*(1-irr)*(1-qual)*(1-mism)*(1-ohm)
    Pac=Pdc*(1-inv)*(1-unav)
    return np.maximum(Pac,0), Geff
# --- VERIFICACION contra el trabajo previo ---
P,Ge=produce(102,10,-30,shad=0.039)
print("=== VERIFICACION MODELO (variante cubierta central del trabajo previo) ===")
print(f"  GlobEff  modelo {Ge.sum()/1000:7.1f} kWh/m2   PVsyst 1806,3   desv {(Ge.sum()/1000/1806.3-1)*100:+.1f}%")
print(f"  E_PV     modelo {P.sum()/1000:7.2f} MWh       PVsyst  166,55  desv {(P.sum()/1000/166.55-1)*100:+.1f}%")
print(f"  Y_F      modelo {P.sum()/1000/102*1000:7.0f} kWh/kWp   PVsyst    1641")
print(f"  PR       modelo {P.sum()/1000/(Ge.sum()/1000*450*0.2259/1000)*100*0.0+ (P.sum()/(102*Ge.sum()/1000))*100:7.2f} %       PVsyst   84,67")
cd_prev_hvac=np.minimum(P,np.load("L.npy")-np.load("LIT.npy")).sum()/(np.load("L.npy")-np.load("LIT.npy")).sum()*100
print(f"  C_D sobre solo HVAC  {P.sum()/ (np.load('L.npy')-np.load('LIT.npy')).sum()*100:5.2f} %   (trabajo previo 13,22 %)")
print(f"  C_D sobre consumo TOTAL {P.sum()/L.sum()*100:5.2f} %  <-- la cifra que importa en el TFM")
np.save("poa_ok.npy",[1])
