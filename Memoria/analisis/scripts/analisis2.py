import pandas as pd, glob, os, numpy as np
base=r"C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Datos\Consumo CPD\Mensual"
NUM=['PUE','Contador Gral','Contador A','Contador B','Pot Gral','Pot A','Pot B']
def load(f):
    if f.lower().endswith(".csv"):
        d=pd.read_csv(f,sep=";",header=0,dtype=str,encoding="latin-1")
        d.columns=[c.strip() for c in d.columns]
        d['Fecha']=pd.to_datetime(d['Fecha'],format="%d/%m/%Y %H:%M",errors='coerce')
        for c in NUM:
            d[c]=pd.to_numeric(d[c].astype(str).str.strip().str.replace(',','.',regex=False),errors='coerce')
    else:
        d=pd.read_excel(f,header=0); d.columns=[str(c).strip() for c in d.columns]
        d['Fecha']=pd.to_datetime(d['Fecha'],errors='coerce')
        for c in NUM: d[c]=pd.to_numeric(d[c],errors='coerce')
    return d.dropna(subset=['Fecha'])
rows=[]
for f in sorted(glob.glob(os.path.join(base,"*"))):
    d=load(f)
    g=d['Contador Gral'].dropna(); a=d['Contador A'].dropna(); b=d['Contador B'].dropna()
    Eg=(g.iloc[-1]-g.iloc[0])/1000.0                 # MWh  (contador en kWh)
    Eit=(a.iloc[-1]-a.iloc[0])+(b.iloc[-1]-b.iloc[0])# MWh  (contadores A/B ya en MWh)
    rows.append(dict(fich=os.path.basename(f), ini=d['Fecha'].min(), fin=d['Fecha'].max(),
        n=len(d), dias=round((d['Fecha'].max()-d['Fecha'].min()).total_seconds()/86400,2),
        E_gral_MWh=round(Eg,2), E_IT_MWh=round(Eit,2), E_noIT_MWh=round(Eg-Eit,2),
        PUE=round(Eg/Eit,3), P_med=round(d['Pot Gral'].mean(),1),
        P_max=round(d['Pot Gral'].max(),1),
        P_min=round(d.loc[d['Pot Gral']>50,'Pot Gral'].min(),1)))
t=pd.DataFrame(rows)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
print(t.to_string()); print()
# normalizar a mes de 30,44 d y anualizar
t['E_gral_dia']=t.E_gral_MWh/t.dias
print("=== TOTALES ANUALIZADOS (media diaria x 365) ===")
print(f"Consumo GENERAL     : {t.E_gral_dia.mean()*365:8.1f} MWh/año   (media {t.E_gral_dia.mean()*1000/24:6.1f} kW)")
print(f"Consumo IT (A+B)    : {(t.E_IT_MWh/t.dias).mean()*365:8.1f} MWh/año")
print(f"Consumo NO-IT       : {(t.E_noIT_MWh/t.dias).mean()*365:8.1f} MWh/año")
print(f"PUE medio ponderado : {t.E_gral_MWh.sum()/t.E_IT_MWh.sum():.3f}")
print(f"P media global      : {t.P_med.mean():.1f} kW | P max {t.P_max.max():.1f} kW | P min {t.P_min.min():.1f} kW")
