import pandas as pd, glob, os, numpy as np
base=r"C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Datos\Consumo CPD\Mensual"
NUM=['PUE','Contador Gral','Contador A','Contador B','Pot Gral','Pot A','Pot B']
def load(f):
    if f.lower().endswith(".csv"):
        d=pd.read_csv(f,sep=";",header=0,dtype=str,encoding="latin-1")
        d.columns=[c.strip() for c in d.columns]
        d['Fecha']=pd.to_datetime(d['Fecha'],format="%d/%m/%Y %H:%M",errors='coerce')
        for c in NUM: d[c]=pd.to_numeric(d[c].astype(str).str.strip().str.replace(',','.',regex=False),errors='coerce')
    else:
        d=pd.read_excel(f,header=0); d.columns=[str(c).strip() for c in d.columns]
        d['Fecha']=pd.to_datetime(d['Fecha'],errors='coerce')
        for c in NUM: d[c]=pd.to_numeric(d[c],errors='coerce')
    return d.dropna(subset=['Fecha'])
P=[]
for f in sorted(glob.glob(os.path.join(base,"*"))):
    d=load(f)[['Fecha','Pot Gral','Pot A','Pot B']]
    P.append(d)
D=pd.concat(P).sort_values('Fecha').set_index('Fecha')
D=D[(D['Pot Gral']>50)&(D['Pot Gral']<800)]
H=D.resample('h').mean().dropna()
H['IT']=H['Pot A']+H['Pot B']; H['noIT']=H['Pot Gral']-H['IT']
print("serie horaria:",H.index.min(),"->",H.index.max(),len(H),"horas")
# construir 8760 canonico ano-tipo: dic2024..nov2025 remapeado a ano civil
prof=H.groupby([H.index.month,H.index.hour])['Pot Gral'].mean()
profIT=H.groupby([H.index.month,H.index.hour])['IT'].mean()
idx=pd.date_range("2025-01-01 00:30",periods=8760,freq="h")
L=np.array([prof.get((m,h),H['Pot Gral'].mean()) for m,h in zip(idx.month,idx.hour)])
LIT=np.array([profIT.get((m,h),H['IT'].mean()) for m,h in zip(idx.month,idx.hour)])
# reescalar al consumo real medido
REAL=3831.96
L=L*REAL*1000/L.sum(); LIT=LIT*2585.08*1000/LIT.sum()
np.save("L.npy",L); np.save("LIT.npy",LIT)
print(f"\nCarga 8760 (kW): media {L.mean():.1f}  min {L.min():.1f}  max {L.max():.1f}  total {L.sum()/1000:.1f} MWh")
print(f"IT   8760 (kW): media {LIT.mean():.1f}  total {LIT.sum()/1000:.1f} MWh")
print(f"noIT 8760 (kW): media {(L-LIT).mean():.1f}  total {(L-LIT).sum()/1000:.1f} MWh   PUE {L.sum()/LIT.sum():.3f}")
m=pd.Series(L,index=idx).resample('MS').sum()/1000
print("\nBalance mensual del consumo GENERAL (MWh):")
print(m.round(1).to_string())
