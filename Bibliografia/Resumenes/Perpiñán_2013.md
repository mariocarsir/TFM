---
title: "Energía Solar Fotovoltaica"
tipo: manual
autor: "Oscar Perpiñán Lamigueiro"
anio: 2013
densidad: exhaustivo
fecha_resumen: 2026-08-16
fuente_original: Bibliografia/PDFs/ApuntesFotovoltaica_Perpinan.pdf
tags: [fotovoltaica, radiacion-solar, celula-solar, generador-fv, SFCR, SFA, almacenamiento, bombeo, seguridad-electrica]
related: []
---

# Energía Solar Fotovoltaica (Perpiñán Lamigueiro, 2013)

## Referencia IEEE
[1] O. Perpiñán Lamigueiro, *Energía Solar Fotovoltaica*, v. 1.5. Madrid, España, mar. 2013. [En línea]. Disponible: http://procomun.wordpress.com/documentos/libroesf

## Nota sobre la naturaleza de la fuente
Manual/libro docente de libre distribución (licencia CC BY-NC-SA 3.0 España), 192 páginas en el PDF fuente (175 pp. de contenido numerado + preliminares y bibliografía), sin ISBN ni editorial. El archivo fuente en este proyecto está guardado con el nombre `ApuntesFotovoltaica_Perpinan.pdf`, pero su contenido interno (metadatos del PDF y portada) confirma que es exactamente este mismo libro — no se trata de apuntes de clase distintos. Cubre geometría solar, radiación solar, teoría de la célula solar, asociación de dispositivos FV, sistemas conectados a red (SFCR), sistemas autónomos (SFA), sistemas de bombeo (SFB) y seguridad eléctrica, con apéndices de ejercicios resueltos. Todos los cálculos y gráficas del libro están generados con el paquete `solaR` (R-project), del propio autor.

**Dos advertencias importantes para su uso en el TFM:**
1. La normativa española que cita (RD 1578/2008, RD 1699/2011, RD 1565/2010, RD 436/2004, RD 1663/2000) está **desactualizada**: fue derogada/sustituida por el RD 244/2019 (regulación vigente de autoconsumo). No citar el contenido normativo de este documento como vigente; solo sirve como contexto histórico/metodológico.
2. El capítulo de almacenamiento (cap. 7, Sistemas Fotovoltaicos Autónomos) trata **exclusivamente baterías de plomo-ácido** (p. 94: "la variada gama de acumuladores que se emplean en los SFA se basan, casi en su totalidad, en la tecnología de ácido-plomo"). No contiene datos de baterías de ion-litio, la tecnología previsible para el almacenamiento del CPD del TFM. Es útil para la metodología de dimensionado (LLP), conceptos de ciclado/degradación, definiciones de capacidad y regulador de carga — no para las cifras técnicas de la química de la batería ni para las curvas V-t de una batería de litio.

## Resumen
Manual docente que cubre de forma completa la ingeniería de sistemas fotovoltaicos: desde la geometría solar y el cálculo de radiación incidente en superficies inclinadas, pasando por la física de la célula solar y su modelado eléctrico, hasta el diseño de los tres grandes tipos de sistemas fotovoltaicos (conexión a red, autónomos y de bombeo) y su seguridad eléctrica. Cada capítulo combina desarrollo teórico con ecuaciones trazables, tablas de valores de referencia, gráficas de comportamiento y ejercicios resueltos con datos numéricos completos. El capítulo 7 (Sistemas Fotovoltaicos Autónomos) desarrolla en detalle el método de dimensionado por probabilidad de pérdida de carga (LLP) y la física del acumulador de plomo-ácido, siendo la referencia metodológica más directamente aplicable al dimensionado de almacenamiento del TFM, aunque limitada a esta química de batería. El capítulo 6 (SFCR) aporta la base de nomenclatura estándar (STC, performance ratio, productividad) y los procedimientos de configuración eléctrica generador-inversor aplicables al campo FV del CPD.

## Contenido técnico

### Capítulo 1. Introducción (pp. 1-4)
Clasificación de aplicaciones fotovoltaicas en tres grandes grupos (figura 1.1): conectados a red (sobre suelo o en edificación), autónomos (profesionales, electrificación rural, pequeño consumo) y de bombeo. Los sistemas conectados a red no necesitan acumulación; los autónomos casi siempre la requieren. Dato de mercado (p. 4, según *Global Market Outlook for Photovoltaics until 2016*, EPIA [13]): potencia FV mundial instalada a finales de 2011 superior a 69 GW, con Europa liderando (>51 GW, ~75% del total mundial), seguida de Japón (5 GW), EEUU (4,4 GW) y China (3,1 GW). **Dato histórico, no usar como cifra de mercado actual.**

### Capítulo 2. Geometría Solar (pp. 5-23)

**2.1 Geometría del movimiento terrestre**

- Distancia Sol-Tierra (ec. 2.1): $r = r_0\{1 + 0{,}017\sin[2\pi(d_n-93)/365]\}$, con $d_n$ día del año y $r_0 = 1{,}496\times10^8$ km = 1 UA.
- Corrección por excentricidad (ec. 2.2): $\epsilon_0 = (r_0/r)^2 = 1 + 0{,}033\cos(2\pi d_n/365)$.
- Declinación solar (ec. 2.3, aproximación estándar): $\delta = 23{,}45°\cdot\sin\left(\dfrac{2\pi(d_n+284)}{365}\right)$. Alternativa más precisa de Spencer (ecs. 2.4-2.6), en radianes, con desarrollo en serie de Fourier de $X = 2\pi(d_n-1)/365$.
- Valores característicos: equinoccios $\delta=0$; solsticio de junio (día 172-173) $\delta=23{,}45°$; solsticio de diciembre (día 355-356) $\delta=-23{,}45°$.
- Sistema de ejes terrestres (vectores $\vec\mu_p$ polar, $\vec\mu_{ec}$ ecuatorial, $\vec\mu_\perp$) y vector solar referido a ellos (ec. 2.7): $\vec\mu_s = [\cos\delta\cos\omega]\vec\mu_{ec} - [\cos\delta\sin\omega]\vec\mu_\perp + \sin\delta\cdot\vec\mu_p$.
- Sistema de ejes locales (vectores $\vec\mu_c$ cenital, $\vec\mu_h$ horizonte, $\vec\mu_\perp$) y vector solar (ec. 2.8): $\vec\mu_s = [\cos\psi_s\sin\theta_{zs}]\vec\mu_h - [\sin\psi_s\sin\theta_{zs}]\vec\mu_\perp + \cos\theta_{zs}\cdot\vec\mu_c$.
- Matriz de giro entre ejes terrestres y locales (ecs. 2.9-2.10), en función de la latitud $\phi$.
- Ángulo cenital solar (ec. 2.12): $\cos\theta_{zs} = \cos\delta\cos\omega\cos\phi + \sin\delta\sin\phi$.
- Relaciones adicionales (ecs. 2.13-2.16) para acimut solar $\psi_s$ y altura solar $\gamma_s$ (complementaria del cenital).
- Ángulo horario de amanecer/atardecer (ec. 2.17): $\omega_s = -\arccos(-\tan\delta\tan\phi)$; extendida (ec. 2.18) para contemplar días/noches polares.
- **2.1.2 Hora oficial y hora solar**: ecuación del tiempo EoT (ec. 2.19, en minutos): $EoT = 229{,}18\cdot(-0{,}0334\sin M + 0{,}04184\sin(2M+3{,}5884))$, con $M = 2\pi d_n/365{,}24$. Conversión hora oficial → hora solar (ec. 2.20): $\omega = 15(TO-AO-12) + \Delta\lambda + EoT/4$, donde $AO$ es el adelanto por horario de verano y $\Delta\lambda = \lambda_L - \lambda_H$ (longitud local menos longitud del huso horario). Ejemplo numérico resuelto para A Coruña, 23 abril 2010, 12:00 h oficial → $\omega=-37{,}94°$.

**2.2 Geometría de la radiación incidente en sistemas fotovoltaicos** — desarrolla el ángulo de incidencia $\theta_s$ (ángulo entre vector solar y normal al generador) para cada tipología de seguimiento:

| Tipología | Ángulo de incidencia (coseno) | Ecuaciones |
|---|---|---|
| Sistema estático orientado al ecuador | ec. 2.22 | $\cos\theta_s=\cos\delta\cos\omega\cos(\beta-\lvert\phi\rvert)-\text{signo}(\phi)\sin\delta\sin(\beta-\lvert\phi\rvert)$ |
| Sistema estático con orientación arbitraria $\alpha$ | ec. 2.24 | vector director ec. 2.23 |
| Eje horizontal Norte-Sur | ec. 2.34 | $\cos\theta_s=\cos\delta\sqrt{\sin^2\omega+(\cos\omega\cos\phi+\tan\delta\sin\phi)^2}$; $\beta=\lvert\psi_{ns}\rvert$ (ec. 2.35), $\alpha=(\pi/2)\text{signo}(\omega)$ (ec. 2.36) |
| Eje horizontal N-S con lamas inclinadas $\lambda$ | ec. 2.42 | generaliza el caso anterior |
| Eje horizontal Este-Oeste | ec. 2.47 | $\cos\theta_s=\cos\delta\sqrt{\cos^2\omega+\tan^2\delta}$ (no depende de la latitud) |
| Eje inclinado ángulo $\lambda$ (genérico) | ec. 2.51/2.55 | caso particular $\lambda=\lvert\phi\rvert$ = seguimiento polar: $\cos\theta_s=\cos\delta$ (ecs. 2.56-2.58) |
| Doble eje | ec. 2.59-2.61 | $\beta=\theta_z$, $\alpha=\psi_s$, $\cos\theta_s=1$ (apuntamiento perfecto) |
| Eje acimutal (inclinación fija, gira en acimut) | ec. 2.62-2.64 | $\cos\theta_s=\cos(\beta-\theta_z)$ |

Todas las deducciones usan matrices de giro entre sistemas de ejes móviles y locales (ecs. 2.39, 2.40, 2.48-2.50, 2.52). Gráficas 2.13, 2.15, 2.17, 2.18: mapas de nivel del coseno del ángulo de incidencia (hora solar × día del año) para latitud 40°N, mostrando la mejora sucesiva de apuntamiento: estático → eje horizontal N-S → acimutal → doble eje (éste último con $\cos\theta_s=1$ constante).

### Capítulo 3. Radiación Solar (pp. 25-38)

- Constante solar: $B_0 = 1367\ \text{W/m}^2$ (promedio OMM).
- Irradiancia extra-atmosférica en plano horizontal (ec. 3.1): $B_0(0)=B_0\cdot\epsilon_0\cdot\cos\theta_{zs}$; irradiación diaria (ec. 3.2): $B_{0d}(0) = -\frac{T}{\pi}B_0\epsilon_0(\omega_s\sin\phi\sin\delta+\cos\delta\cos\phi\sin\omega_s)$.
- **Tabla 3.1** — Días promedio (Cooper, [34]) por mes con su $d_n$: Ene 17, Feb 45, Mar 74, Abr 105, May 135, Jun 161, Jul 199, Ago 230, Sep 261, Oct 292, Nov 322, Dic 347.
- Masa de aire (ec. 3.3): $AM = 1/\cos\theta_{zs}$.
- Componentes de la irradiancia: directa $B$, difusa $D$, albedo $R$ (o $AL$); global $G=B+D+R$ (ec. 3.4).
- Nomenclatura estándar (ec. 3.5): `Forma_tiempo,promedio(lugar)`, p. ej. $G_{d,m}(I)$ = media mensual de irradiación global diaria en el plano del generador.
- Índice de claridad diario/mensual (ecs. 3.6-3.7): $K_{Td}=G_d(0)/B_{0d}(0)$; $K_{Tm}=G_{d,m}(0)/B_{0d,m}(0)$.
- Correlación de Page (mensual, ec. 3.9): $FD_m = 1-1{,}13\cdot K_{Tm}$. Ejemplo numérico resuelto ($G_{d,m}(0)=3150$ Wh/m², $B_{0d,m}(0)=4320$ Wh/m² → $K_{Tm}=0{,}73$, $FD_m=0{,}175$, difusa 551,6 Wh/m², directa 2598,4 Wh/m²).
- Correlación de Collares-Pereira y Rabl (diaria, ec. 3.10): $FD_d=0{,}99$ si $K_{Td}\le0{,}17$; $FD_d=1{,}188-2{,}272K_{Td}+9{,}473K_{Td}^2-21{,}856K_{Td}^3+14{,}648K_{Td}^4$ si $K_{Td}>0{,}17$.
- Discrepancia entre bases de datos de radiación: **hasta el 30%** — cualquier estimación de energía debe referenciar la base de datos empleada.
- **3.3 Radiación en superficies inclinadas** — procedimiento de cálculo completo (figura 3.3, diagrama de flujo): irradiación diaria horizontal → irradiancia horizontal (perfiles $r_D$, $r_G$) → irradiancia en plano del generador (directa/difusa/albedo) → irradiación diaria/mensual/anual efectiva.
  - $r_D=D(0)/D_d(0)=B_0(0)/B_{0d}(0)$ (ec. 3.11), con $B_0(0)/B_{0d}(0)$ calculable con ec. 3.12.
  - $r_G=G(0)/G_d(0)=r_D\cdot(a+b\cos\omega)$ (ec. 3.13), con $a=0{,}409-0{,}5016\sin(\omega_s+\pi/3)$ (ec. 3.14), $b=0{,}6609+0{,}4767\sin(\omega_s+\pi/3)$ (ec. 3.15).
  - Directa en plano inclinado (ecs. 3.16-3.17): $B(\beta,\alpha)=B(0)\cdot\max(0,\cos\theta_s)/\cos\theta_{zs}$.
  - Difusa isotrópica (ec. 3.19): $D(\beta,\alpha)=D(0)\cdot(1+\cos\beta)/2$.
  - Modelo anisotrópico de Hay-McKay (ecs. 3.20-3.23): separa difusa isotrópica $D_I$ (ec. 3.21) y circunsolar $D_C$ (ec. 3.22), ponderadas por el índice de anisotropía $k_1=B(0)/B_0(0)$ (ec. 3.23).
  - Albedo (ec. 3.24): $R(\beta,\alpha)=\rho\cdot G(0)\cdot(1-\cos\beta)/2$, con $\rho=0{,}2$ recomendado si no hay datos del terreno.
- **3.4 Incertidumbre** — variabilidad interanual $\delta_X=\sigma_X/\bar X$: diaria 0,1-0,6 (según época), mensual 0,1-0,35, **anual ≈ 2,5%** (datos Carmona-Tomejil, Andalucía, 2001-2008, fig. 3.6). Desviación de la media para predicción a N años: $\sigma_{\bar X}=\sigma_X/\sqrt N$ (relevante para predicciones a 25 años de vida útil).
- **3.5 Ángulo de Incidencia y Suciedad** — pérdidas angulares por reflexión (Martin-Ruiz, ec. 3.27): $FT_B(\theta_s)=\dfrac{\exp(-\cos\theta_s/a_r)-\exp(-1/a_r)}{1-\exp(-1/a_r)}$, apreciables solo a partir de ~60-70° de desviación.
  - **Tabla 3.2** — Coeficiente de pérdidas angulares $a_r$ y transmitancia relativa según suciedad: Limpio $T=1$, $a_r=0{,}17$; Bajo $T=0{,}98$, $a_r=0{,}20$; Medio $T=0{,}97$, $a_r=0{,}21$; Alto $T=0{,}92$, $a_r=0{,}27$.
  - Ecuaciones análogas para difusa isotrópica (3.28) y albedo (3.29), con coeficientes $c_1=4/3\pi$ y $c_2$ dependiente de $a_r$ (tabla 3.2, tercera columna: -0,069/-0,054/-0,049/-0,023).
  - Pérdidas por suciedad+incidencia integradas anualmente en Madrid, suciedad media: **7-10%** según inclinación/orientación (fig. 3.8).
- **3.6 Aplicación práctica: sistemas estáticos**:
  - Inclinación óptima (ec. 3.33, Lorenzo [60]): $\beta_{opt}=3{,}7+0{,}69\lvert\phi\rvert$ (grados). Desviarse ~10° del óptimo produce solo ~1% de pérdidas (baja sensibilidad de módulos planos).
  - Relación irradiación óptima/horizontal (ec. 3.34): $G_a(0)/G_a(\beta_{opt})=1-4{,}46\times10^{-4}\beta_{opt}-1{,}19\times10^{-4}\beta_{opt}^2$.
  - Irradiación anual efectiva vs. incidente (ecs. 3.35-3.36): $G_{efa}(\beta,\alpha)/G_a(\beta_{opt})=g_1(\beta-\beta_{opt})^2+g_2(\beta-\beta_{opt})+g_3$, con $g_i=g_{i1}\lvert\alpha\rvert^2+g_{i2}\lvert\alpha\rvert+g_{i3}$.
  - **Tabla 3.3** — coeficientes $g_{ij}$ para suciedad media (usados en los ejercicios D.1): $g_{11}=8\times10^{-9}$, $g_{21}=-4{,}27\times10^{-7}$, $g_{31}=-2{,}5\times10^{-5}$; $g_{12}=3{,}8\times10^{-7}$, $g_{22}=8{,}2\times10^{-6}$, $g_{32}=-1{,}034\times10^{-4}$; $g_{13}=-1{,}218\times10^{-4}$, $g_{23}=2{,}892\times10^{-4}$, $g_{33}=0{,}9314$.

### Capítulo 4. La célula solar (pp. 39-52)

**4.1 Teoría de semiconductores**: bandas de valencia/conducción/prohibida; $E_g$ define conductor/aislante/semiconductor ($E_g<5$ eV); silicio $E_g=1{,}12$ eV. Dopaje tipo n (donadoras, p. ej. fósforo) y tipo p (aceptoras, p. ej. boro). Unión p-n: ecuación de Shockley del diodo (ec. 4.1): $I_D=I_0[\exp(V/mV_T)-1]$, con $V_T=kT/e=25{,}85$ mV a 300 K (potencial térmico).

**4.1.4 Unión p-n iluminada**: energía del fotón (ec. 4.2): $E_f=hc/\lambda$. Corriente total célula (ec. 4.3): $I=I_L-I_0[\exp(V/mV_T)-1]$. Rango aprovechable para silicio: visible (400-700 nm) y UV cercano (300-400 nm); infrarrojo (>1100 nm) no rompe enlaces.

**4.2 Funcionamiento de la célula**:
- $I_{sc}=I_L$ (ec. 4.5); $V_{oc}=\dfrac{mkT_c}{e}\ln(I_L/I_0+1)$ (ec. 4.6); forma combinada (ec. 4.7).
- **Punto de máxima potencia (MPP)**: condición $dP/dV=0$ (ec. 4.8-4.9): $dI/dV=-I_{mpp}/V_{mpp}$.
- **Factor de forma** (ec. 4.10): $FF=\dfrac{I_{mpp}V_{mpp}}{I_{sc}V_{oc}}$, típicamente **0,7-0,8**.
- **Eficiencia** (ec. 4.11): $\eta=I_{mpp}V_{mpp}/P_L$. Células industriales de silicio: **13-17%** (fig. 4.7, NREL).
- **Circuito equivalente** (fig. 4.10, modelo de un diodo con $R_s$ y $R_p$): ec. 4.12: $I=I_L-I_0[\exp((V+IR_s)/mV_T)-1]-(V+IR_s)/R_p$. $R_s$ alta reduce el FF (fig. 4.8); $R_p$ baja reduce FF y $V_{oc}$ (fig. 4.9).
- Simplificación práctica (ec. 4.13-4.16) despreciando $R_p$: $I=I_{sc}[1-\exp((V-V_{oc}+IR_s)/mV_t)]$.
- **Influencia de temperatura**: $dV_{oc}/dT_c=-2{,}3$ mV/°C (ec. 4.17, valor por defecto si no hay datos de fabricante para silicio cristalino); $d\eta/dT_c=-0{,}4\%/°$C.
- **Influencia de irradiancia**: $I_{sc}(X)=X\cdot I_{sc}(1)$ (ec. 4.18), proporcional al factor de "soles" $X$.
- **Condiciones STC** (Standard Test Conditions): $G_{stc}=1000\ \text{W/m}^2$ incidencia normal, $T_c^*=25°C$, $AM=1{,}5$.
- **Cálculo del MPP fuera de STC** — método de J.M. Ruiz (ecs. 4.20-4.32): normaliza tensión/corriente, define $r_s=R_s/(V_{oc}/I_{sc})$ y $k_{oc}=V_{oc}/V_t$; resuelve $i_{mpp}$ (ec. 4.28) y $v_{mpp}$ (ec. 4.29) vía $D_{M0}$ (ec. 4.31) y $D_M$ (ec. 4.30). $R_s^*$ se calcula con ec. 4.32 a partir de datos de ficha técnica. Método simplificado alternativo (FF constante, ecs. 4.33-4.34): $I_{mpp}/I_{sc}=I^*_{mpp}/I^*_{sc}$; $V_{mpp}/V_{oc}=V^*_{mpp}/V^*_{oc}$.
- **4.3 Fabricación**: silicio grado metalúrgico → triclorosilano → silicio grado solar; policristalino (Siemens) vs. monocristalino (Czochralski); obleas 200-500 µm; dopaje P/B; contactos Ag/Al; capa antirreflectante (TiO₂, color azulado); texturado.

### Capítulo 5. Asociación de dispositivos fotovoltaicos (pp. 53-60)

**5.1 Módulo fotovoltaico**: encapsulado EVA entre vidrio y tedlar/vidrio, marco aluminio anodizado. Norma **IEC 61215** para módulos de silicio cristalino. Configuración histórica de 36 células en serie (~15 V MPP, compatible con baterías 12 V); actual >200 Wp, 30-50 V.

- Modelo de módulo ($N_{cs}$ células serie, $N_{cp}$ ramas paralelo): $V_m=N_{cs}V_c$, $I_m=N_{cp}I_c$ (ec. 5.1). $I_{sc}=G_{ef}I^*_{sc}/G_{stc}$ (ec. 5.2); $V_{oc}(T_c)=V^*_{oc}+(T_c-T^*_c)dV_{oc}/dT_c$ (ec. 5.3), con $dV_{oc}/dT_c=-2{,}3$ mV/(célula·°C) por defecto (ec. 5.4).
- **Comportamiento térmico**: balance de potencias (ec. 5.5): $A_cG_{ef}=P_c+P_Q$; $T_c=T_a+\xi P_Q$ (ec. 5.6), $\xi=C_T/A_c$.
- **NOCT** (Temperatura de Operación Nominal de Célula), condiciones de referencia: $G=800$ W/m², $AM=1{,}5$, incidencia normal, $T_a=20°C$, $v_v=1$ m/s. Ecuación de temperatura de célula (ec. 5.7): $T_c=T_a+G_{ef}\cdot(NOCT-20)/800$.
- **5.1.3 Punto caliente**: cuando una célula sombreada/averiada en una serie recibe menos fotocorriente, puede pasar a disipar potencia (cuadrante negativo), sobrecalentándose. Diferencia de temperatura con diodo de paso protegiendo $N_D$ células (ec. 5.12): $T_{cs}-T_c=C_T\cdot N_D\cdot\eta\cdot G_{ef}$. **Ejemplo numérico**: $N_D=18$, $C_T=0{,}036\ °C\cdot m^2/W$, $\eta=0{,}14$, $G_{ef}=1000$ W/m² → $\Delta T\approx91°C$ con diodo de paso. Sin diodos, 36 células en serie (ec. 5.13): $\Delta T$ **supera los 180°C**. Práctica común: 18-20 células por diodo de paso, conexión solapada (fig. 5.9).
- **5.2.1 Pérdidas por dispersión**: corriente MPP de un conjunto de módulos modelada con distribución Weibull (ec. 5.14). Eficiencia de conexión serie (ecs. 5.15-5.16): $\eta_{cs}=N_s^{-1/\alpha}$ — decrece con $N_s$ (series más cortas = menos pérdidas, pero mayor sección de cable). Clasificación de módulos por "flash-list" puede reducir pérdidas un 2-3% teóricamente, pero cuestionada por el error de medida del propio flash-test.

### Capítulo 6. Sistemas Fotovoltaicos de Conexión a Red (pp. 61-91)

**6.1 Conceptos básicos**: dos mecanismos de retribución — prima (feed-in tariff, habitual en Europa) y balance neto (net-metering, habitual en EEUU). Normativa española citada (**desactualizada**, contexto histórico): RD 1578/2008, RD 1699/2011, RD 436/2004, REBT, HE5-CTE.

- **Ecuación de potencia mínima HE5-CTE** (ec. 6.1): $P_{min}=C\cdot(A\cdot S+B)$, $S$ superficie construida, $C$ según zona climática (1 a 1,4; zona I <3,8 kWh/m², zona V >5 kWh/m²), mínimo 6,25 kWp.
- Sistemas de concentración: requieren doble eje (ciegos a difusa).

**6.2 Inversor DC/AC**:
- Tipos: central, orientado a rama (string), módulo-AC (descartado salvo demostrativos). Monofásico ≤5 kW (límite normativo español histórico).
- Bloques: filtro entrada, convertidor DC/DC, puente inversor, filtro salida, transformador, control.
- **THD** onda cuadrada monofásica (ec. 6.2): $THD_v=0{,}4829$; trifásica (ec. 6.3): $THD_v=0{,}3103$.
- **SPWM** (modulación de ancho de pulso sinusoidal) reduce armónicos según índice de modulación de frecuencia.
- **6.2.5 Búsqueda del MPP**: algoritmo P&O ("perturb and observe", ec. 6.4-6.5) y de "conductancia incremental" ($dI/dV=-I/V$ en el MPP).
- **Curva de eficiencia del inversor** (ec. 6.19, modelo de 3 coeficientes, Jantsch et al. [55]): $\eta_{inv}=\dfrac{p_o}{p_o+k_0^o+k_1^op_o+k_2^op_o^2}$, $p_o=P_{ac}/P_{inv}$.
- **6.2.7 Funcionamiento en isla**: probabilidad de coincidencia balance carga/generación + desconexión de red ≈ **$10^{-9}$**, no incrementa el riesgo eléctrico de base ($10^{-6}$) (estudio IEA [37,99]).

**6.3 Configuración de un SFCR**:
- $\beta_{opt}=3{,}7+0{,}69\lvert\phi\rvert$ (ec. 6.10, idéntica a 3.33). Mínimo 15° por autolimpieza.
- **Tabla 6.1** — Pérdidas límite HE5-CTE (%): General: orient./incl. 10, sombras 10, total 15. Superposición: 20/15/30. Integración arquitectónica: 40/20/50.
- Fórmula de pérdidas por orientación/inclinación HE5-CTE (ec. 6.11): $Pérdidas=100[1{,}2\times10^{-4}(\beta-\phi+10)^2+3{,}5\times10^{-5}\alpha^2]$ si $15°<\beta<90°$.
- **Número máximo de módulos en serie** (ec. 6.13): $N_{sMAX}=V_{max,inv}/V_{ocM}(G=200\ \text{W/m}^2,T_a=-10°C)$.
- **Ventana MPP** (ecs. 6.14-6.16): $N^{min}_{sMPP}=V_{mppMIN}/V_{mppM}(G_{stc},25°C)$; $N^{max}_{sMPP}=V_{mppMAX}/V_{mppM}(G_{stc},25°C)$.
- **Número máximo de ramas** (ec. 6.18): $N_{pMAX}=I_{max,INV}/I^*_{scM}$.
- Relación de sobredimensionamiento $P^*_g/P_{inv}$: **1 a 1,4** en sistemas estáticos (más frecuentemente en integración arquitectónica); **cercana a 1** (máx. +20%) en sistemas de seguimiento. CTE-HE5 español (histórico): inversor mínimo 80% de la potencia pico del generador.

**6.4 Sombras en generadores**: pérdidas por sombreado parcial en Alemania: **4% a 30%** [39,54] (dato ya presente en el resumen previo, ahora contextualizado).
- Factor de sombras HE5-CTE (procedimiento paso a paso, diagrama de trayectorias solares, tablas de pérdida porcentual por celda) — ejemplo numérico resuelto: $FS\approx6{,}3\%$.
- **GCR** (Ground Coverage Ratio) y **ROT** (Ratio de Ocupación de Terreno, inverso de GCR). Valores típicos de ROT: estático **2**, eje horizontal N-S **4**, doble eje **6**.
- Sombras mutuas doble eje: factores $FS_{eo}$, $FS_{ns}$, $FS_d$ (ecs. 6.24-6.32), en función de acimut solar $\psi_s$, altura $\gamma_s$, factor de forma del seguidor $b=L/W$ (ec. 6.22) y distancias normalizadas $l_{eo}=L_{eo}/W$, $l_{ns}=L_{ns}/W$.
- **Retroseguimiento** (backtracking, ec. 6.34-6.35): ángulo corregido $\beta=\beta_0-\arccos(l_{eo}\cos\beta_0)$ cuando $l_{eo}\cos\beta_0\le1$.
- Comparativa de productividad (figs. 6.19-6.20, mapas España/Portugal 30-50°N, base SODA-ESRA): doble eje vs. estático **+30% a +50%**; doble eje vs. eje horizontal **+25% a +30%**; eje horizontal vs. estático **+5% a +20%**.

**6.5 Cálculo de la productividad**:
- Ecuación aproximada de energía anual (ec. 6.36): $E_{ac}=P^*_g\cdot\dfrac{G_{ef,a}}{G_{stc}}\cdot PR\cdot(1-FS)$.
- **Productividad** (ec. 6.37): $Y_f=E_{ac}/P^*_g$ [kWh/kWp].
- **Tabla 6.2** — Factores de pérdidas incluidos en el Performance Ratio anual: dispersión de parámetros 2-4%, tolerancia de potencia 3%, temperatura 5-8%, conversión DC/AC (inversor) 8-12%, efecto Joule cableado 2-3%, transformador BT/MT 2-3%, disponibilidad 0,5-1%.
- **PR anual típico**: rango **0,4 a 0,85**, promedio europeo **0,74** (base de datos IEA para sistemas desde 1996 [28]).

### Capítulo 7. Sistemas Fotovoltaicos Autónomos (pp. 93-112) — **capítulo de mayor relevancia para el TFM**

**7.1 Conceptos generales**: cuatro configuraciones típicas (fig. 7.1): SHS (solo DC), AC (con inversor), AC-DC (mixto), híbrido (con grupo electrógeno).

**7.2.1 Acumulador electroquímico** — íntegramente sobre plomo-ácido:
- **Definiciones clave**: capacidad nominal $C_b$; régimen de carga/descarga (p. ej. $C_{10}$); relación **$C_{100}\approx1{,}35\cdot C_{10}$** (importante: no implica $I_{100}=0{,}1\cdot I_{10}$; ejemplo: $C_{10}=300$ Ah, $I_{10}=30$ A, $C_{100}\approx405$ Ah, $I_{100}=4{,}05$ A); estado de carga (SoC); profundidad de descarga (PD); tensión de corte; capacidad útil (ec. 7.1): $C_U=PD_{max}\cdot C_b$.
- **Reacciones electroquímicas** (ecs. 7.2-7.4): ánodo $PbO_2+SO_4^{2-}+H^++2e^-\rightleftharpoons PbSO_4+2H_2O$; cátodo $Pb+SO_4^{2-}\rightleftharpoons PbSO_4+2e^-$; global $Pb+PbO_2+2H_2SO_4\rightleftharpoons2PbSO_4+2H_2O$.
- Mecanismos de degradación: sulfatación (cristalización irreversible en descarga prolongada), estratificación (gradiente de densidad de electrolito), gaseo (electrólisis del agua al final de la carga), corrosión de rejillas.
- Baterías VRLA (gel, AGM) para evitar reposición de agua.
- **Modelo eléctrico** (fig. 7.2): $V_B=V_{BI}+I_CR_{BI}$ (carga, ec. 7.5); $V_B=V_{BI}-I_DR_{BI}$ (descarga, ec. 7.6). Relación densidad-tensión (ec. 7.7): $V_{BI}=\rho_e+0{,}84$, con $\rho_e$ entre 1,2 y 1,28 g/cm³ (batería cargada) → $V_{BI}$ entre **2,04 V y 2,12 V** por vaso.
- Umbral de fin de carga recomendado: **2,3-2,4 V/vaso a 25°C**; umbral de descarga: **~2 V/vaso** (dependiente del tipo de batería).
- Efecto temperatura: capacidad decrece ~**1%/°C** al bajar la temperatura [57].
- Factores que reducen la vida por ciclado: profundidad de descarga, régimen de carga excesivo, temperatura alta.
- Tipos de acumulador para SFA: SLI (arranque automóvil, mal comportamiento en ciclado), tracción (buen ciclado, mucho mantenimiento), **estacionarias** (recomendadas: buena fiabilidad, resistentes a corrosión, régimen de flotación), "fotovoltaicas" (SLI o estacionarias modificadas). Recomendación general [41]: estacionarias aireadas de placa positiva tubular, aleación Pb-Sb.

**7.2.2 Regulador de carga**: tipos serie (fig. 7.7a) y shunt/paralelo (7.7b, requiere diodo de bloqueo). Histéresis de protección (fig. 7.8): $U_{sc}$ (fin de carga) / $U_{rc}$ (reposición); $U_{sd}$ (fin de descarga) / $U_{rd}$ (reposición). Controladores "on-off" vs. PWM. Corrección por temperatura: **4-5 mV/°C por vaso**.

**7.3 Dimensionado de un SFA — método LLP**:
- **LLP** (Loss of Load Probability, ec. 7.8): $LLP=E_{def}/L$.
- **Capacidad normalizada del generador** (ec. 7.9): $C_A=\eta_G A_G G_d(\beta,\alpha)/L$; variante con radiación horizontal (ec. 7.10): $C'_A=\eta_G A_G G_d(0)/L$; relación entre ambas (ec. 7.11): $C'_A=C_A\cdot G_d(0)/G_d(\beta,\alpha)$.
- **Capacidad normalizada del acumulador** (ec. 7.12): $C_S=C_U/L=C_B\cdot PD_{max}/L$.
- Estado de carga diario simulado (ec. 7.13): $SOC_j=\min[SOC_{j-1}+C_AG_{d,j}/(C_S\bar G_d)-1/C_S;\ 1]$. Déficit diario (ec. 7.14): $E_{def}=\max\{1/C_S-SOC_j;0\}$. LLP acumulado (ec. 7.15): $LLP=\sum E_{def}/(N\cdot L)$.
- **Curvas isofiables** (ecs. 7.16-7.18): $C'_A=f\cdot C_S^{-u}$, $f=f_1+f_2\log(LLP)$, $u=\exp(u_1+u_2\cdot LLP)$. **Parámetros para Madrid**: $f_1=-0{,}2169$, $f_2=-0{,}7865$, $u_1=-1{,}2138$, $u_2=-15{,}280$. Cálculos con probabilidad $LLP<10^{-2}$ **carecen de utilidad práctica** [74] (incertidumbre intrínseca del proceso estocástico de radiación).
- **Método basado en experiencia** (Norma Técnica Universal [41]): doméstico $C_A=1{,}1$, $3\le C_S\le5$; profesional $1{,}2\le C_A\le1{,}3$, $5\le C_S\le8$.
- **Tabla 7.1** (ya en el resumen previo, confirmada): Norte España doméstico $C_A=1{,}2/C_S=5$, profesional $C_A=1{,}3/C_S=8$; Sur España doméstico $C_A=1{,}1/C_S=4$, profesional $C_A=1{,}2/C_S=6$.
- **Configuración eléctrica** (ecs. 7.19-7.22): $L=V_bQ_L$; $\eta_GA_GG_{stc}=I^*_gV_b$; $I^*_g=C_A\cdot Q_L\cdot G_{stc}/G_d(\beta,\alpha)$; $C_U=C_S\cdot Q_L$. Prohibido normativamente conectar en paralelo más de 2 baterías, y nunca una batería nueva con una vieja.
- **Orientación/inclinación según perfil de consumo** (sección 7.3.4): consumo constante → $\beta=\lvert\phi\rvert+10°$ (maximiza en el mes peor); consumo tipo equinoccio → $\beta=\lvert\phi\rvert$; consumo predominante en verano → $\beta=\lvert\phi\rvert-10°$.
- **Cálculo de consumo** (ecs. 7.23-7.24): $L_T=L_{dc}/\eta_r+L_{ac}/\eta_{inv}$; $L=L_T/(\eta_{bat}\eta_c)$. **Valores orientativos**: $\eta_{inv}=0{,}9$; $\eta_r=0{,}95$; $\eta_{bat}=0{,}85$; $\eta_c=0{,}98$ (ya en resumen previo, confirmados con contexto completo).
- Distribución de consumo eléctrico doméstico: sigue una **distribución Gamma**, no Normal ("mucha gente consume poco y poca gente consume mucho") — cita textual de investigadores brasileños [72] (fig. 7.11).
- **Tabla 7.2** — Escenarios de consumo SFA: SHS1 (120 Wh/día, sin frigorífico, $C_A=1{,}1$, $3\le C_S\le5$), SHS2 (250 Wh/día, TV color), SHS3 (1000 Wh/día, con frigorífico eficiente, $C_S=5$), Centrales (500 Wh/día por vivienda, todo AC, $C_S=5$).
- Sensibilidad de la fiabilidad al consumo real (fig. 7.12): variación del 60% en consumo respecto al de diseño reduce la fiabilidad **a la mitad**.

**7.2.3 Luminarias**: eficiencia recomendada de luminaria fluorescente **>50 lm/W** (mínimo 35 lm/W); resistencia mínima **10.000 ciclos** de encendido/apagado (mínimo 5.000).

### Capítulo 8. Sistemas Fotovoltaicos de Bombeo (pp. 113-123) — relevancia baja para el TFM (CPD), se resume de forma más compacta

- Motor DC (con/sin escobillas) vs. motor de inducción asíncrono (más común, requiere variador de frecuencia).
- Leyes de semejanza de bombas centrífugas (ecs. 8.3-8.6): $Q\propto n$, $H\propto n^2$, $P_{mec}\propto n^3$, $T\propto n^2$.
- Potencia hidráulica (ec. 8.11): $P_H=2{,}725\cdot Q\cdot H_V$ [W, m³/h, m]. Potencia eléctrica de entrada (ec. 8.14): $P_{el}=P^*_g\cdot(G/G_{stc})\cdot(\eta_g/\eta^*_g)\cdot\eta_{inv}$.
- **Altura Total Equivalente** $H_{TE}$ (ec. 8.17): combina altura estática/dinámica del pozo, caudal aparente y pérdidas de fricción, con $Q_{AP}=\alpha\cdot Q_d$, $\alpha=0{,}047\ h^{-1}$.
- Dimensionado aproximado del generador (ec. 8.18): $P^*_g=10\cdot H_{TE}\cdot Q_d/(G_d/G_{stc})$. El diseño fino se resuelve con nomogramas específicos por modelo de bomba (fig. 8.6).
- Referencias de consumo de agua: OMS 50 l/persona·día; mínimo emergencia 3-5 l; cooperación 30-35 l; SFB [75]: 25 l (fuente comunitaria) o 45 l (grifo domicilio).

### Capítulo 9. Seguridad Eléctrica en Sistemas Fotovoltaicos (pp. 125-140)

- Esquemas de puesta a tierra: **TT** (habitual en la salida del inversor hacia la red), **TN**, **IT** (habitual en el generador FV europeo — "configuración flotante").
- Umbrales de tensión/corriente de seguridad: emplazamientos secos 120 V DC / 50 V AC; mojados **60 V DC / 24 V AC**; corriente máxima 100 mA DC / 30 mA AC.
- Contacto directo esquema IT: corriente de fuga máxima (ec. 9.3): $I_f=V_{ocG}/(R_{iso}+R_h)$; resistencia mínima de aislamiento (ec. 9.4): $R_{iso}\ge10\cdot V_{ocG}-R_h$ para $I_f\le100$ mA.
- Corriente de descarga capacitiva transitoria (ec. 9.5, norma CEI479-2): $I_{desc}=V_{ocG}/(R_h\sqrt6)$, con $R_h=1000\ \Omega$, $C_{iso}=1\ \mu F$. Riesgo de fibrilación requiere $V_{ocG}>3000$ V.
- Tres niveles de protección (Gómez-Vidal [49]): Nivel 1 refuerzo de aislamiento (config. flotante, cableado clase II, aislamiento galvánico AC-DC); Nivel 2 detección de aislamiento (vigilante, señal 2-5 Hz); Nivel 3 puesta a tierra.
- Resistencia de puesta a tierra (ec. 9.8, $n_p$ picas): $R_t\approx\rho/(n_p\cdot L_p)$.
- **Tabla 9.1** — resistividad del terreno (ITC-BT-18): cultivables fértiles 50 Ω·m, poco fértiles 500 Ω·m, pedregosos 3000 Ω·m.
- Límite de resistencia de puesta a tierra esquema TT (ec. 9.9): $R_{tp}\le V_{max}/I_f$; ejemplo resuelto 60 V/100 mA → $R_{tp}\le600\ \Omega$.
- Protección frente a rayos: acoplamiento galvánico, capacitivo e inductivo. Sistemas de protección externa no necesarios para sistemas <500 Wp.
- **Sección de cableado por caída de tensión** (ecs. 9.13-9.15): $S_{dc}=2\cdot l_{dc}\cdot I_{dc}/(56\cdot\Delta V_{dc})$; $S_{1ac}$ análoga; $S_{3ac}=\sqrt3\cdot l_{3ac}\cdot I_{3ac}/(56\cdot\Delta V_{3ac})$. Límite normativo ITC-BT-40: caída máxima **1,5%** de la tensión nominal (aplicado por separado a tramos DC y AC).
- Criterio térmico: sección dimensionada para ≥125% de la intensidad máxima (ITC-BT-40); elección de fusibles (ecs. 9.11-9.12): $I_B<I_n<I_z$; $I_2<1{,}45\cdot I_z$; para instalaciones FV, $I_n\ge1{,}25\cdot I_{sc}$.

### Apéndices (uso como referencia metodológica, no como cifras a citar directamente)

- **Apéndice A**: algoritmo completo de simulación de un SFB (curvas H-Q por leyes de semejanza, perfil de irradiancia según norma IEC 61725, acoplamiento potencia FV-bomba paso a paso).
- **Apéndice B**: enlaces a bases de datos de radiación (SIAR, PVGIS, SODA-ESRA, NASA, HELIOS-IES Madrid) — enlaces revisados en 2013, verificar vigencia antes de usar.
- **Apéndices C y D**: colecciones de ejercicios resueltos con datos numéricos completos (geometría solar, SFCR, SFA, SFB, seguridad eléctrica), útiles como plantilla de procedimiento de cálculo pero con casos particulares (A Coruña, Coslada, León, Brasil, Bolivia) no directamente aplicables al CPD de Madrid del TFM sin recalcular con los datos propios. Destaca el ejercicio D.2.3: dimensionado de un SFA con grupo electrógeno de apoyo (metodología de reducción de LLP a costa de horas de funcionamiento del grupo, análogo conceptual a una estrategia híbrida FV+almacenamiento+red).

## Datos clave (con página)

- **p. 4** — Potencia FV mundial instalada a finales de 2011: >69 GW (Europa 75%). Dato histórico de 2013, no usar como cifra de mercado actual.
- **p. 16** — $\beta_{opt}=3{,}7+0{,}69\lvert\phi\rvert$ (grados), inclinación óptima para sistemas estáticos según latitud (Lorenzo [60]); coincide con la ec. 3.33 y 6.10.
- **p. 27** — Correlación de Page (mensual): $FD_m=1-1{,}13K_{Tm}$.
- **p. 34** — Discrepancia entre bases de datos de radiación: hasta **30%**. Incertidumbre anual de la irradiación: **~2,5%** (Carmona-Tomejil, 2001-2008).
- **p. 35** — Tabla 3.2, coeficiente de pérdidas angulares $a_r$ por grado de suciedad: limpio 0,17; bajo 0,20; medio 0,21; alto 0,27.
- **p. 45** — Factor de forma de una célula: $FF=I_{mpp}V_{mpp}/(I_{sc}V_{oc})$, valor típico **0,7-0,8**.
- **p. 46** — Células industriales de silicio: eficiencia **13-17%** (fig. 4.7, NREL).
- **p. 48** — STC: $G_{stc}=1000\ \text{W/m}^2$, $T_c^*=25°C$, $AM=1{,}5$. Coeficiente térmico habitual (si no hay dato de fabricante): $dV_{oc}/dT_c=-2{,}3$ mV/°C.
- **p. 58** — Punto caliente: con diodo de paso ($N_D=18$, $C_T=0{,}036\ °C\cdot m^2/W$, $\eta=0{,}14$, $G_{ef}=1000\ \text{W/m}^2$) $\Delta T\approx91°C$; sin diodos (36 células serie) $\Delta T$ **>180°C**.
- **p. 60** — Eficiencia de conexión serie $\eta_{cs}=N_s^{-1/\alpha}$ (distribución Weibull de dispersión de parámetros); reducción de pérdidas por clasificación de módulos: 2-3% teórico, cuestionado en la práctica.
- **p. 73** — HE5-CTE, potencia mínima FV obligatoria: $P_{min}=C(AS+B)$, mínimo **6,25 kWp**.
- **p. 74** — Tabla 6.1, pérdidas límite HE5-CTE (%): General 10/10/15; Superposición 20/15/30; Integración arquitectónica 40/20/50.
- **p. 76-77** — Relación de sobredimensionamiento generador/inversor: **1 a 1,4** (estáticos), **≈1, máx +20%** (seguimiento). CTE histórico: inversor ≥80% de potencia pico del generador.
- **p. 77** — Pérdidas por sombreado parcial (estudios Alemania): **4% a 30%**.
- **p. 80-90** — ROT (Ratio de Ocupación de Terreno) recomendado: estático **2**, eje horizontal N-S **4**, doble eje **6**.
- **p. 88** — Tabla 6.2, Performance Ratio, pérdidas típicas: dispersión 2-4%, tolerancia 3%, temperatura 5-8%, inversor 8-12%, cableado 2-3%, transformador 2-3%, disponibilidad 0,5-1%. PR anual **0,4-0,85** (promedio europeo **0,74**).
- **p. 90-91** — Mejora de productividad doble eje vs. estático **30-50%**; doble eje vs. eje horizontal **25-30%**; eje horizontal vs. estático **5-20%**.
- **p. 94-95** — Definiciones de acumulador: $C_b$, régimen carga/descarga, $C_{100}\approx1{,}35\cdot C_{10}$ (no equivale a $I_{100}=0{,}1I_{10}$).
- **p. 96** — $V_{BI}=\rho_e+0{,}84$; para batería cargada, $\rho_e\in[1{,}2,1{,}28]$ g/cm³ → $V_{BI}\in[2{,}04,2{,}12]$ V/vaso.
- **p. 97-98** — Umbral de fin de carga recomendado a 25°C: **2,3-2,4 V/vaso** (on-off) o **2,3-2,35 V/vaso** (PWM); corrección con temperatura **4-5 mV/°C por vaso**. Umbral de descarga ~2 V/vaso (depende del tipo).
- **p. 98** — Capacidad reducida por baja temperatura: aprox. **1%/°C**.
- **p. 104** — $LLP=E_{def}/L$; $C_A=\eta_GA_GG_d(\beta,\alpha)/L$; $C_S=C_U/L=C_B\cdot PD_{max}/L$.
- **p. 106** — Método LLP, parámetros de ajuste Madrid: $f_1=-0{,}2169$, $f_2=-0{,}7865$, $u_1=-1{,}2138$, $u_2=-15{,}280$.
- **p. 106** — Tabla 7.1, valores recomendados SFA España: Norte doméstico $C_A=1{,}2$/$C_S=5$, profesional $C_A=1{,}3$/$C_S=8$; Sur doméstico $C_A=1{,}1$/$C_S=4$, profesional $C_A=1{,}2$/$C_S=6$.
- **p. 108** — LLP<$10^{-2}$: cálculos carecen de utilidad práctica por la incertidumbre intrínseca del proceso estocástico de radiación.
- **p. 109** — Rendimientos orientativos SFA: $\eta_{inv}=0{,}9$, $\eta_r=0{,}95$, $\eta_{bat}=0{,}85$, $\eta_c=0{,}98$.
- **p. 111** — Sensibilidad del SFA al consumo real: variación del 60% en consumo reduce la fiabilidad a la mitad.
- **p. 121-122** — Fórmula aproximada de dimensionado SFB: $P^*_g=10\cdot H_{TE}\cdot Q_d/(G_d/G_{stc})$; ejemplo: 30 m³/día a 40 m con $G_d=5$ kWh/m² → 2400 Wp.
- **p. 126-127** — Umbrales de seguridad eléctrica: secos 120 V DC/50 V AC; mojados **60 V DC/24 V AC**; corriente máxima 100 mA DC/30 mA AC.
- **p. 132** — Tabla 9.1, resistividad del terreno: cultivable fértil 50 Ω·m, poco fértil 500 Ω·m, pedregoso 3000 Ω·m.
- **p. 133** — Riesgo de fibrilación por descarga atmosférica: requiere $V_{ocG}>3000$ V (duración de descarga 3 ms según CEI479-2).
- **p. 139-140** — Caída de tensión máxima admisible por cableado (ITC-BT-40): **1,5%** de la tensión nominal, aplicado por separado a DC y AC; criterio térmico: sección dimensionada para ≥125% de la corriente máxima del generador.

## Relevancia para el TFM

- **Capítulos del índice a los que aporta** (ver `Memoria/indice_propuesto.md`): dimensionado del campo FV (generador/inversor, orientación e inclinación, sombras, ROT), metodología de dimensionado de almacenamiento (LLP, capacidades normalizadas $C_A$/$C_S$), definición de nomenclatura estándar (STC, performance ratio, productividad $Y_f$), seguridad eléctrica del sistema FV.
- **Qué aporta exactamente**:
  1. Base física completa y trazable (geometría solar, radiación en plano inclinado, célula solar, generador) para justificar hipótesis de cálculo del dimensionado FV con fórmulas concretas, no "conocimiento general".
  2. El método LLP (ecuaciones 7.8-7.18) es la referencia metodológica más directa para justificar el criterio de fiabilidad del sistema de almacenamiento del CPD, aunque el TFM previsiblemente usará baterías de ion-litio y un modelo horario en Excel en vez del método estadístico diario aquí descrito — el marco conceptual (capacidad normalizada, ciclado diario vs. estacional, curvas isofiables) es igualmente aplicable.
  3. Valores orientativos de eficiencia de componentes (inversor, cableado, regulador, batería) citables cuando no se disponga de datos de fabricante concretos, siempre marcados como "valores orientativos" de esta fuente.
  4. Procedimientos completos de configuración eléctrica generador-inversor (número de módulos en serie/paralelo, ventana MPP, límites de tensión) directamente aplicables al dimensionado del campo FV del CPD.
  5. Marco normativo de seguridad eléctrica (esquemas de tierra IT/TT/TN, criterios de sección de cableado, protección contra sobretensiones) como referencia metodológica, con la salvedad de que la normativa específica citada está desactualizada.
- **No usar como fuente para**: normativa vigente de autoconsumo/conexión a red (desactualizada, ver advertencia arriba), datos técnicos de baterías de ion-litio (no tratadas en el documento — todo el capítulo 7 es plomo-ácido), ni cifras de mercado FV actuales (dato de 2011-2012).

## Notas de procesamiento
Documento de 192 páginas procesado de forma exhaustiva y completa: se ha leído la totalidad del texto extraído del PDF (índice, nomenclatura, los 9 capítulos completos y los 4 apéndices, incluida la bibliografía), sin muestreo. Los apéndices C y D (ejercicios resueltos) se han resumido de forma más compacta que el cuerpo teórico, indicando la estructura y metodología de cada ejercicio en vez de reproducir la aritmética completa de cada uno, dado que sus datos numéricos particulares (localidades, latitudes y consumos específicos de cada enunciado) no son directamente trasladables al caso del TFM sin recalcular. El capítulo 8 (bombeo) se ha resumido de forma más compacta que los capítulos 2, 4, 6, 7 y 9 por su baja relevancia directa para un TFM de autoconsumo con almacenamiento en un CPD. No se han detectado imágenes o gráficas que no pudieran describirse a partir del texto/leyendas extraídos vía `pypdf`; algunas figuras vectoriales (diagramas de circuitos, mapas de nivel) se han descrito por su contenido y ejes en vez de reproducirse gráficamente, como corresponde a un resumen en Markdown.
