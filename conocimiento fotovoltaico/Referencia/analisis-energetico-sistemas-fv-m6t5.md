---
title: "Análisis energético de sistemas fotovoltaicos"
tipo: presentacion
autor: "Jorge López Galera"
anio: "Sin fecha exacta (discrepancia entre portadas, ver Notas de procesamiento)"
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Documentacion de apoyo\Presentaciones Master\M6 Autoconsumo\Presentaciones\M6_T5_AnalisisEnergeticoSistemasFV.pdf"
tags: [fotovoltaica, analisis-energetico, perdidas-fv, performance-ratio, produccion-especifica, sankey, iam, mismatch, degradacion, modulo6-erma]
related: []
---

# Análisis energético de sistemas fotovoltaicos (Jorge López Galera, Máster ERMA — Módulo 6)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA (UPM) que desarrolla, paso a paso, el flujo completo de pérdidas de energía en un sistema fotovoltaico desde el recurso solar hasta la energía inyectada en red, siguiendo la estructura de un diagrama de Sankey de PVsyst. Cubre: pérdidas respecto al recurso solar (disposición, sombras, suciedad, albedo), pérdidas por desviación respecto a condiciones STC (ángulo de incidencia/IAM, espectrales, temperatura, baja irradiancia), diferencias entre potencia nominal y real de los módulos (tolerancia, dispersión/mismatch, LID, PID, UV-ID, degradación anual), comportamiento energético del inversor (eficiencia estática/dinámica, clipping, curtailment, derrating térmico), pérdidas eléctricas de la instalación (cableado, transformador) y, finalmente, los indicadores de rendimiento energético de sistemas FV. **Importante:** los indicadores de rendimiento que desarrolla el documento son Producción Específica (SY), Performance Ratio (PR), Capacity Factor (CF) y un método de "Coeficientes" (regresión cuadrática); el documento **no emplea la notación Y_R/Y_A/Y_F/A_PV/C_D/D_G** solicitada en el encargo — ver nota en "Datos clave" y en "Notas de procesamiento". Cada apartado incluye valores típicos de mercado, tablas de ensayos de laboratorio reales (DEKRA, ENERTIS, fabricantes chinos bajo norma IEC 61215-2) y fuentes explícitas (PVsyst, FRV, artículos técnicos).

## Contenido técnico

### 0. Portada e índice (pp. 1-3)

1. Título: "Análisis energético de sistemas fotovoltaicos". Autor: Jorge López Galera (jorge.lopez@frv.com). Máster en Energías Renovables y Medio Ambiente (ERMA), UPM — Módulo 6: Autoconsumo Fotovoltaico.
2. Índice de la presentación (7 apartados):
   1. Introducción
   2. Pérdidas de energía respecto al recurso solar
   3. Pérdidas de energía por desviación respecto a STC
   4. Diferencia entre potencia real y nominal
   5. Comportamiento energético del inversor solar
   6. Pérdidas de energía en la instalación eléctrica
   7. Indicadores de rendimiento energético de sistemas fotovoltaicos

### 1. Introducción al análisis energético de sistemas FV (pp. 4-8)

1. **Objetivos del análisis energético:**
   - Control y definición de calidad: identificar eficiencias, pérdidas de energía y disponibilidad.
   - Predecir la energía a generar por un sistema FV en un periodo determinado.
   - Ayudar al diseño de planta y comparación de producciones/eficiencias → AM (Asset Management) y O&M (Operación y Mantenimiento).
   - Informes energéticos: información a inversores y gestores de la producción, apoyo al cálculo de ingresos.

2. **Factores determinantes** (tres bloques):
   - **Emplazamiento**: localización y recurso solar (GHI, DHI, ALB, contaminación); climatología (velocidad y dirección del viento, T_amb, lluvia, nieve, granizo); parcela y superficie.
   - **Componentes del sistema fotovoltaico**: tecnología de componentes (f(Inversor, MPPTs, seguimiento, BESS)); ratio DC/AC y diseño POI (f(clipping, curtailments, PQ, Layout, BESS)); punto de conexión (POI).
   - **Instalación**: orientación (α), inclinación (β), seguimiento, BESS (f(Tarifa, PPA, LCOE...), estacionalidad, uso, contrato/PPA); espacio (Ground Cover Ratio, GCR); sombras; topografía/orografía; disipación de calor (en edificios); estructura y anclajes (cargas, cubierta, viento, sombras).

3. **Diagrama de Sankey (flujo de pérdidas), fuente PVsyst** — cadena completa de valores (ejemplo real de una planta bifacial):
   | Etapa | Valor | Pérdida asociada |
   |---|---|---|
   | Global horizontal irradiation | 1152 kWh/m² | — |
   | Global incident in coll. plane | +18,0% | — |
   | Near Shadings: irradiance loss | -4,50% | |
   | IAM factor on global | -0,70% | |
   | Soiling loss factor | -1,60% | |
   | Ground reflection on front side | +0,09% | |
   | Global incident on ground (bifacial) | 375 kWh/m² sobre 82.426 m² | |
   | Ground reflection loss (0,17 Gnd. albedo) | -82,54% | |
   | View Factor for rear side | -63,82% | |
   | Sky diffuse on the rear side | +47,35% | |
   | Beam effective on the rear side | +1,91% | |
   | Shadings loss on rear side | -3,00% | |
   | Global Irradiance on rear side | 4,54% (58 kWh/m²) | |
   | Effective irradiation on collectors | 1269 kWh/m² × 109.182 m² coll. | — |
   | PV conversion (Bifaciality factor = 0,80; efficiency at STC = 22,23%) | — | — |
   | Array nominal energy (at STC effic.) | 31.924.651 kWh | — |
   | Module Degradation Loss (year #10) | -3,80% | |
   | PV loss due to irradiance level | -0,40% | |
   | PV loss due to temperature | -1,32% | |
   | Shadings: Electrical Loss acc. to strings | -0,52% | |
   | Module quality loss | +0,40% | |
   | LID - Light induced degradation | -0,10% | |
   | Mismatch loss, modules and strings (incl. 2% dispersión) | -2,38% | |
   | Mismatch for back irradiance | -0,26% | |
   | Ohmic wiring loss | -0,28% | |
   | Array virtual energy at MPP | 29.242.970 kWh | — |
   | Inverter Loss during operation (efficiency) | -1,45% | |
   | Inverter Loss over/under nominal power/current/voltage/threshold | 0,00% (cada una) | |
   | Night consumption | -0,01% | |
   | Available Energy at Inverter Output | 28.817.098 kWh | — |
   | Auxiliaries (fans, other) | -0,20% | |
   | AC ohmic loss | -0,40% | |
   | Medium voltage transfo loss | -0,86% | |
   | MV line ohmic loss | -0,25% | |
   | High voltage transfo loss | -0,68% | |
   | Energy injected into grid | 28.135.565 kWh | — |

4. **Tipos de pérdidas energéticas en sistemas FV** (esquema del flujo Pdc/Idc → DC/AC → Pac/Iac → red):
   - **Disposición**: orientación, inclinación, layout.
   - **Recurso solar**: horizonte y sombras (objetos y estructura), albedo, suciedad, nieve/hielo.
   - **Desviación de STC**: pérdidas angulares (IAM), espectrales, temperatura, eficiencia a baja irradiancia.
   - **Diferencia entre potencia FV nominal y real**: calidad, LID, degradación, dispersión de parámetros, PID.
   - **No trabajar en punto de máxima potencia**; adecuación generador FV al inversor; fallos en array/inversor/instalación/red.
   - **Pérdidas inversor**: eficiencia (estática, dinámica), mismatch (I,V,P), clipping/saturación, curtailment (PPC).
   - **Pérdidas cableado AC, transformador, red AT** (plantas FV).

### 2. Pérdidas de energía respecto al recurso solar (pp. 8-23)

1. **Disposición y Layout**: el array FV no tiene la orientación/inclinación "óptimas"; dependen de perfil de generación/consumo, precios de venta/consumo, LCOE (equipos y producción), BESS, condiciones locales y físicas (disposición de cubierta/suelo, condiciones atmosféricas -viento-, tipo de suelo, soporte de cargas de cubierta).

2. **Altura del horizonte (sombras lejanas)**: el array no recibe radiación solar directa en ningún punto de su superficie. Depende del perfil del horizonte (medido o archivo *.HOR) y de la superficie/"color" delante de los módulos. Gráfica de "Trazado de la línea del perfil de obstáculos - Hora Legal" (altura del sol [°] vs acimut [°], plano inclinación 30°, acimut 0°, líneas horarias 6h-18h). Limitaciones de PVsyst: 1 solo perfil (grandes plantas), necesita optimizar tratamiento de topografía, no realiza backtracking 3D, limitaciones con trackers estacionales (E/W).

3. **Sombras cercanas/parciales**: el array recibe radiación directa sobre parte de la superficie. Requiere evaluar la deformación de la curva I(V) mediante modelos de funcionamiento de módulos y array (modelo de un diodo, modelo de dos diodos, otros), modelado de curvas I(V), y tipología de panel/disposición (full cell/half-cut/shingled, portrait/landscape).

4. **Modelo de un diodo — ecuación fundamental de la celda FV:**
   $$I = I_L - I_D - \frac{V + I \cdot R_s}{R_{Sh}}$$
   donde: $I$ = corriente suministrada por el módulo/célula; $V_{cel}$ = tensión en bornes; $I_L$ = corriente fotogenerada ($I_{PH}$); $I_D$ = corriente de oscuridad; $R_S$ = resistencia serie; $R_{Sh}$ = resistencia paralelo.
   - Curva teórica de diodo: $I_D = I_0\left[e^{\left(\frac{e \cdot V}{m \cdot k \cdot T}\right)} - 1\right]$
   - Curva I(V) del módulo: $I = I_L - I_0\left[e^{\left(\frac{e \cdot V}{m \cdot k \cdot T}\right)} - 1\right]$
   - Fill Factor: $FF = \dfrac{V_{mp} \cdot I_{mp}}{V_{co} \cdot I_{sc}} = \dfrac{\text{área A}}{\text{área B}}$. Valores requeridos: FF > 70÷80%.
   - Resistencia paralelo $R_{Sh}$: representa fugas de corriente en bordes de células e impurezas en uniones PN. Valores típicos: células 2500-4500 Ω; módulos 300-900 Ω.
   - Resistencia serie $R_s$: resistencia interna de conectores. Valores típicos 0,05-0,3 Ω.
   - Fuente citada: Mermoud A., "PV module one-diode model as implemented in PVSYST", 1st European Workshop on PV performance modelling, INES, 22-23 febrero 2013.
   - Tabla de ensayo de módulos (front/back side, bifaciales), 620 W nominal: ejemplo fila 1: Front P_max=623,83 W, Voc=55,81 V, Isc=13,70 A, Vmpp=47,64 V, Impp=13,09 A, FF=81,57%; Back P_max=491,34 W, Voc=56,28 V, Isc=10,60 A, Vmpp=48,50 V, Impp=10,13 A, FF=82,38%, φPmax=78,78%. (4 filas de ejemplo con serial numbers, fecha 14/05/2023, modelo 620, workshop 5B).
   - Práctica de fabricación: dado que existe dispersión de parámetros, en fábrica se mide con trazador y se ajustan los parámetros para crear el archivo *.PAN (proceso inverso a la teoría, que sale de Isc/Voc/Rsh/Rs).

5. **Disposición del panel — nuevas tecnologías:** full cell (60 células) vs 120 Half-Cut Cell (con bypass diodes agrupando 1 de 3 strings o 1 de 6 strings, 3 arriba/3 abajo). Reducción de pérdidas eléctricas: "electrical losses = current² × resistance" — al dividir la célula a la mitad, la corriente se reduce a la mitad y las pérdidas caen a 1/4 (esquema con triángulos de corriente eléctrica). Configuraciones: Landscape (Maxeon), Landscape (Half-cut), Portrait (Maxeon), Portrait (Half-cut) — con diagramas de recorrido de corriente. Dimensiones de ejemplo de módulo: 2066×1160 mm (exterior), 2022×1118 mm (activo), marco 274 mm, con 4 agujeros de toma de tierra (Ø4,2 mm) y 8 agujeros de montaje.

6. **Pérdidas por suciedad ("Soiling"):**
   - Curva I-V/potencia limpia vs sucia (gráfica corriente [A] / potencia [W] vs tensión [V], hasta 1300 V).
   - Dependen de: condiciones climáticas y régimen de lluvias, velocidad del viento, contaminación atmosférica (natural y humana), tamaño y composición de partículas, deposiciones de aves/hojas, inclinación y disposición de módulos, tecnología (half-cut), superficie exterior del vidrio.
   - **Suciedad uniforme**: disminuye la corriente generada (polvo, arena, contaminación).
   - **Suciedad localizada**: incrementa pérdidas por dispersión de parámetros y puede producir puntos calientes (efecto playa —acumulación en zona próxima al marco—, excrementos de aves/hojas/barro → hot-spots).
   - Ejemplo real documentado: "Lluvia de barro de la borrasca Celia" (14-15 marzo 2022) — fotografías de módulos antes/después de limpieza en cubierta urbana.
   - **Estudio de suciedad en instalación en Jordania** (sept. 2019 - dic. 2020):
     - Ratio anual de suciedad (1 limpieza/mes): **2,10%**.
     - Ratio anual (sin limpiezas): **48%**.
     - Tabla de ratio diario de suciedad (GHI>300 W/m²) por temporada (invierno/verano) y método (IV Curve vs WS data): invierno IV Curve diario 0,106% / mensual 3,18%; verano IV Curve diario 0,157% / mensual 4,71%; verano WS data diario 0,145% / mensual 4,35%.
     - Tabla mensual "AVG Soiling" 2020: ene 1,62%, feb 1,66%, mar 2,05%, abr 2,35%, may 2,36%, jun 2,36%, jul 2,36%, ago 2,36%, sep 2,11%, oct 1,97%, nov 2,11%, dic 1,91%.
     - Fórmula de pérdida por suciedad: $\text{Soiling loss}(\%) = 1 - \dfrac{Cell_{dirty}}{Cell_{clean}}$
     - Gráfica "Dirty vs Clean cell reference by WS" (sept-2019 a nov-2020), tres sensores (PS03.WS, PS08.WS, PS13.WS) con media móvil de 10 periodos, mostrando periodos válidos de análisis y periodos de lluvia señalados. Fuente: FRV.
   - **Medición del soiling**: análisis por curvas IV, torres meteorológicas; medición del soiling [%] mediante células calibradas (limpia vs sucia), sensor óptico, módulos calibrados Isc/Voc (clean vs dirty). Foto de sensor de suciedad "SSERC LAB" con etiqueta de calibración (Factory: CSI Dafeng, Test: Visual IV EL Calibration).

7. **Pérdidas de Albedo y Reflejada:**
   - **Albedo (ALB) (horizontal)**: ratio de reflexión en suelo [%]. Sobre cubierta: campaña puntual. Sobre suelo: 1 o 2 años de medición (por variaciones), correlación con BBDD satelitales.
   - **Reflejada (RTI) (inclinada) → Bifacialidad**: algoritmos de seguimiento, altura al suelo.
   - Gráfica "Albedo Measured on Site": GHI, RTI (reflejada) y Albedo (%) medidos en campo a lo largo de un día (11:24-16:38), con albedo estable en torno a 2-3%.

### 3. Pérdidas de energía por desviación respecto a STC (pp. 24-38)

1. **Tabla de condiciones estándar (STC) vs pérdidas por condiciones reales de operación:**
   | Parámetro | Condiciones estándar de medida | Pérdidas por condiciones reales |
   |---|---|---|
   | Ángulo de incidencia | Normal a la superficie del módulo | Pérdidas angulares |
   | Masa de aire | AM 1,5 G | Pérdidas espectrales |
   | Temperatura de la célula | 25 °C | Pérdidas por temperatura |
   | Irradiancia incidente | 1000 vs 200 W/m² | Pérdidas por baja irradiancia |
   | Irradiancia incidente | Homogénea sobre la superficie del módulo | Pérdidas por sombras |

2. **Pérdidas por ángulo de incidencia (IAM):**
   - Mecanismo físico: pérdidas por reflexión, transmitancia y absorción de las capas superiores a la célula FV (Air → Glass → EVA → PV cell) y de la propia célula cuando los rayos no inciden según la normal. Primera reflexión = contribución principal a la pérdida IAM; segunda reflexión < 1% de la primera.
   - Tabla comparativa de Bill of Materials (BOM1 vs BOM2) de un módulo real: célula (Jinko), cell connectors (Jinko), string connectors (Jinko), front/rear cover (Flat), front/rear encapsulation (First TF4/F406P vs Sinopont PO8110), frame (Jinko), adhesive junction box/frame (Zhijiang JS-606 vs Minghao MH-3668), potting material (Zhijiang JS-1184), junction box (JK09ES Jinko), connector (JK03M2 Jinko), cable (Jinko).
   - Las pérdidas angulares dependen de: componentes del módulo solar (cristal, encapsulante), latitud (AOI), climatología (DHI), disposición del módulo (inclinación, orientación, seguimiento), y se incrementan con la suciedad.
   - **Definición de IAM (Incidence Angle Modifier)**: ratio entre la transmitancia $\tau(\theta)$ para el ángulo $\theta$ y la transmitancia cuando es normal al Sol $\tau(0)$ (AOI=0):
     $$IAM_B = \frac{\tau(\theta)}{\tau(0)}$$
   - Ecuación completa del coseno del ángulo de incidencia (fuente: Óscar Perpiñán):
     $$\cos(\theta_s) = \vec{\mu}_{ns\lambda} \cdot \vec{\mu}_s = \text{signo}(\phi) \cdot \sin(\lambda) \cdot (\cos(\delta)\cos(\omega)\sin(\phi) - \cos(\phi)\sin(\delta)) + \cos(\lambda)\sin(\psi_{ns})\cos(\delta)\sin(\omega) + \cos(\lambda)\cos(\psi_{ns}) \cdot (\cos(\delta)\cos(\omega)\cos(\phi) + \sin(\delta)\sin(\phi))$$
     $$= \cos(\delta) \cdot \{\text{signo}(\phi) \cdot \sin(\lambda) \cdot (\cos(\omega)\sin(\phi) - \cos(\phi)\tan(\delta)) + \cos(\lambda) \cdot [\sin(\psi_{ns})\sin(\omega) + \cos(\psi_{ns}) \cdot (\cos(\omega)\cos(\phi) + \tan(\delta)\sin(\phi))]\}$$
   - Diagrama geométrico: Sol, cenit (Zenith), normal a la superficie, ángulos β (inclinación), θ (incidencia), ψ/ψ' (acimut), puntos cardinales N/S/E.
   - Comportamiento: los efectos angulares son despreciables para ángulos de incidencia pequeños; las pérdidas angulares son mayores a ángulos elevados y con radiación principalmente difusa, debido al incremento de pérdidas por reflexión. Gráfica "Incidence Angle Modifier" (perfil efectivo vs modelo Fresnel con AR coating) — IAM cae bruscamente por encima de ~60-70°, llegando a 0 en 90°. Segunda gráfica: factor de transmitancia bifacial $FT_B$ vs $\theta_S$, comparando módulo limpio (clean) vs sucio (dirty) — la suciedad incrementa las pérdidas angulares para ángulos superiores a 30°. Fuente: Handbook of Photovoltaic Science and Engineering (Chapter 20).
   - **Comparativa de modelos IAM usados por PVsyst**: gráfica "IAM correction, Fresnel and Ashrae" comparando 3 modelos (Fresnel AR coating, Fresnel normal glass, Ashrae b0=0,05) en función del ángulo de incidencia [0-90°] — divergen notablemente por encima de 60°, con IAM cayendo a ~60-65% a 80°.
   - **Modelo definido por usuario (*.PAN)**, obtenido al caracterizar el módulo: mismo BOM que los módulos instalados, 3 módulos testeados, seguimiento de producción, semi-templado vs endurecido, diferencias frontal/trasero, cambio de espesores de cristal.
     | θ (°) | IAM |
     |---|---|
     | 0 | 1,000 |
     | 10 | 1,004 |
     | 20 | 1,003 |
     | 30 | 1,002 |
     | 40 | 1,002 |
     | 50 | 1,001 |
     | 60 | 0,999 |
     | 65 | 0,992 |
     | 70 | 0,964 |
     | 75 | 0,921 |
     | 80 | 0,842 |
     | 85 | 0,719 |
   - Tabla "Yearly IAM losses" comparando funciones IAM (factor a 60°/70°/80°, pérdida IAM anual total, y desglose beam/diffuse/albedo):
     | IAM function | IAM factor 60° | 70° | 80° | IAM loss | Beam | Diffuse | Albedo |
     |---|---|---|---|---|---|---|---|
     | User defined profile | 100,0% | 96,0% | 84,0% | 0,82% | 0,43% | 0,36% | 0,04% |
     | ASHRAE bo=0,050 | 95,0% | 90,4% | 76,2% | 3,27% | 1,99% | 1,20% | 0,07% |
     | ASHRAE bo=0,040 | 96,0% | 92,3% | 81,0% | 2,62% | 1,60% | 0,97% | 0,06% |
     | Fresnel smooth glass, n=1,526 | 94,8% | 86,2% | 63,6% | 3,56% | 2,09% | 1,37% | 0,10% |
     | Fresnel AR coating n(glass)=1,526, n(AR)=1,290 | 96,2% | 89,2% | 68,1% | 2,78% | 1,61% | 1,09% | 0,09% |
     | Sandia model, acc. to database | 95,6% | 85,6% | 59,7% | 3,27% | 1,86% | 1,30% | 0,11% |

3. **Pérdidas espectrales:**
   - La distribución espectral de la atmósfera se expresa por el parámetro AM (Air Mass), que depende de: longitud de atmósfera atravesada (AM), contenido de vapor de agua, aerosoles.
   - $$AM = \frac{1}{\cos(\theta)}$$
   - Modelo de Kasten y Young (más preciso, corrige curvatura terrestre):
     $$AM = \frac{1}{\cos(\theta) + 0,50572 \cdot (96,07995 - \theta)^{-1,6364}}$$
   - Gráfica de distribución espectral: intensidad solar [kW/m²/µm] vs longitud de onda [µm] para cuerpo negro a 6000K, AM0, AM1,5, y sensibilidad del ojo humano. Distribución espectral AM 1,5 de referencia: Norma UNE EN 60904-3.
   - **Segundo orden — respuesta espectral de un módulo FV** depende de: distribución espectral de la irradiancia incidente, tecnología de la célula (eficiencia cuántica η), ángulo de incidencia.
     $$I_{sc} \propto \int_0^\infty E(\lambda) \, SR(\lambda) \, d\lambda$$
   - Gráfica de respuesta espectral normalizada (SR) por tecnología: a-Si/a-Ge (pico 602nm), CdTe (648nm), mono c-Si (708nm), multi c-Si (717nm), µ-Si (638nm), a-Si/µ-Si (655nm), acidic multi c-Si (710nm), CIGS (731nm), rango 300-1300 nm. Fuente: "The real challenges for photovoltaic modules", Krauter S. et al., Photovoltaik Institut University of Technology Berlín. Gráfica adicional: "Total Solar Irradiance Composite" 1975-2010 con número de manchas solares.

4. **Pérdidas por temperatura:**
   - Potencia de un módulo FV en función de la temperatura (STC: irradiancia 1000 W/m², temperatura de célula 25 °C, AM=1,5). La eficiencia normalizada η/η_STC incluye la influencia de distintos factores; considerando solo el efecto de la temperatura:
     $$P = P_{STC} \cdot \frac{G}{G_{STC}} \cdot [1 - \gamma \cdot (T_{CEL} - T_{CEL\_STC})]$$
     donde: G = irradiancia en condiciones estándar de prueba [W/m²]; P = potencia pico del módulo (a T y G) [W]; A = área del módulo [m²]; $T_{CEL}$ = temperatura de operación de célula; $T_{CEL\_STC}$ = temperatura de célula en condiciones estándar; γ = coeficiente de temperatura de la potencia (~0,35 %/°C para Si-monocristalino y ~0,25 %/°C para Si-amorfo, valores considerados constantes en el rango típico de operación).
   - Gráfica de eficiencia [%] vs irradiancia incidente [0-1000 W/m²] para distintas temperaturas de célula (10, 25, 40, 55, 70 °C) — módulo Canadian Solar CS7N-650MB-AG 1500V RFP ESP21, eficiencia STC 21,01%. Tabla de eficiencia relativa respecto a STC (1000 W/m², 25°C): 800 W/m² +0,4%; 600 W/m² +0,5%; 400 W/m² +0,1%; 200 W/m² -1,7%. Imagen de mapa térmico de módulo (irradiancia trasera "Backside Irradiance W/m²" en matriz de valores).
   - Coeficiente de temperatura de la potencia: gráfica de barras "TC for Power [%/K]" por tecnología (A1/A2/A3 c-Si, B1/B2 CdTe, C1/C2 CIGS, D a-Si), rango -0,20 a -0,42 %/K. Fuente: "Uncertainties in PV System Yield Predictions and Assessments", IEA PVPS 2018.
   - Evolución de parámetros del módulo FV con la temperatura (gráfica): Isc, Voc, Pm normalizados [%] vs temperatura de célula [-50 a 100°C] — Voc y Pm decrecen linealmente con la temperatura, Isc aumenta ligeramente. Tabla de coeficientes de temperatura normalizados: Pmax -0,29%/°C; Voc -0,25%/°C; Isc 0,045%/°C; NOCT (Nominal Operating Cell Temperature) 45±2°C.
   - **Medida de la temperatura**: monitorización mediante T_amb (termómetro protegido de irradiación y viento) y T_mod/T_back (PT100 o PT1000, calibrados Clase A). Existen pérdidas por temperatura también en transformadores, cables e inversores.
   - **Tabla de modelos de temperatura de célula** (con parámetros IEC-Sandia a/b/dT para Glass/Cell/Glass: a=-3,47, b=-0,0594 s/m, dT=3°C; Glass/Cell/Polymer Sheet: a=-3,56, b=-0,075, dT=3°C; Polymer/Thin Film/Steel: a=-3,58, b=-0,113, dT=3°C):
     | Modelo | Fórmula |
     |---|---|
     | Faiman | $T_{cell} = T_a + \dfrac{GHI}{U_0 + U_1 \cdot WS}$ |
     | Schott (1985) | $T_{cell} = T_a + 0{,}028 \cdot GHI - 1$ |
     | Servant (1985) | $T_{cell} = T_a + \alpha \cdot GHI \cdot (1+\beta \cdot T_a) \cdot (1-\gamma \cdot WS) \cdot (1-1{,}053 \cdot \eta_m)$ |
     | Ross & Smokler (1986) | $T_{cell} = T_a + \dfrac{(T_{NOCT}-20)}{800} \cdot GHI$ |
     | IEC-Sandia | $T_{back} = T_a + GHI \cdot e^{(a+b \cdot WS)}$; $T_{cell} = T_{back} + \dfrac{GHI}{1000} \cdot dT_{cond}$ |
     | PVsyst | $T_{cell} = T_a + \dfrac{\alpha \cdot GTI \cdot (1-eta_m)}{U_0 + U_1 \cdot WS}$ |
     | Homer | $T_{cell} = \dfrac{T_a + (T_{NOCT}-20)\cdot\left(\dfrac{GHI}{800}\right)\cdot\left(1-\dfrac{\eta_{mp\text{-}STC}\cdot(1-(\alpha_P\cdot25))}{\tau\cdot\alpha}\right)}{1+(T_{NOCT}-20)\cdot\left(\dfrac{GHI}{800}\right)\cdot\left(\dfrac{\alpha_P\cdot\eta_{mp}}{\tau\cdot\alpha}\right)}$ |

5. **Pérdidas por baja irradiancia:**
   - Para irradiancias bajas, la eficiencia disminuye por la influencia negativa de la baja irradiancia en la tensión generada.
   - Ejemplo de fórmula de relación de potencias: $\dfrac{Pot_{200}}{Pot_{1000} \cdot \frac{200}{1000}} = 0{,}962$
   - Gráfica de curvas I-V a distintas irradiancias (1000, 800, 600, 400, 200 W/m²) a 45°C — módulo CSI Solar CS7N-690TB-AG 1500V, con potencias marcadas (649,0 / 521,0 / 390,9 / 259,1 / 126,9 W).
   - Tabla de eficiencia relativa respecto a STC (G ref./T ref./Pmp/Rel. effic.): 1000 W/m²·25°C → 700,7 W, 0,00%; 800 W/m² → 564,4 W, +0,62%; 600 W/m² → 424,6 W, +0,92%; 400 W/m² → 282,2 W, +0,62%; 200 W/m² → 139,2 W, -0,72%. Fuente: PVsyst.
   - Referencias a informes de ensayo reales: DEKRA (pag. 16, informe "6192997A.50-Panfile report_RSM132-8-695BHDG.pdf"); ENERTIS (pag. 20, "LAB-UK2023-2699Q02-4 Ed.1 Batch4_Enertis Lab Test Report_FRV_BEON-Lauriston-Risen.pdf") — test según IEC 61215-2, criterio "relative efficiency loss < 5%" a 200 W/m². Ejemplo de resultados: módulo E2FX7A23E13190121 (SN 2115660): 1000 W/m² → Pmax 636,80 W; 200 W/m² → Pmax 123,05 W → relative efficiency 96,62%. Módulo SN 2115905: relative efficiency 97,26%.

### 4. Diferencia entre potencia real y nominal (pp. 37-49)

1. **Diferencias entre potencia FV nominal y real**: tolerancia de la potencia, dispersión de parámetros, LID, UV-ID, degradación.

2. **Tolerancia de potencia y dispersión (Module Quality):**
   - Datasheet vs flash test data (caracterización). Tolerancia en potencia [0/+5W] & [0/+1%]. Tolerancia en corriente [±4%] (Imp o Isc). Tolerancia en tensión [±3,5%] (Vmp o Voc).
   - Tabla "Pmax Average test Results": Nominal Maximum Power 620W → Re-Flash Average 622,97W → Pass; 625W → 628,15W → Pass.
   - Tabla "Mismatched modules parameter distribution" (RMSvalue): Isc = 18,03 A (0,90 A / 5,0%); Voc = 47,4 V (2,4 V / 5,0%).
   - Bill of Material (BOM), procesos de fabricación, binning/sorting (clasificación) de potencia y corriente. Module Quality (PVsyst): ~-0,35% (module efficiency loss, valor por defecto -0,30% en PVsyst).
   - Tabla "Current sorting": Nominal Power 620W → L: 12,56≤Imp<13,01 A; M: 13,01≤Imp<13,11 A; H: 13,11≤Imp<13,56 A. 625W → L: 12,59≤Imp<13,04; M: 13,04≤Imp<13,14; H: 13,14≤Imp<13,59.
   - La dispersión (Pmp e Imp) se acentúa con el paso del tiempo.

3. **Dispersión de parámetros: Mismatch.**
   - Caso ideal: todos los módulos FV con la misma curva I-V. Fórmula de potencia de array: $P^*(A) = N_P \cdot N_S \cdot P^*(M)$ (con $N_P$ = módulos en paralelo, $N_S$ = módulos en serie).
   - Formas de modelar la distribución aleatoria de curvas (PVsyst): distribución normal (Gaussiana), distribución cuadrática. Modelado por Isc/Imp y Voc/Vmp.
   - Valores típicos: Module mismatch loss 0,35÷0,60% (corriente del string); String mismatch loss ~0,15% (tensión del string).
   - **Pérdidas en sistema bifacial:**
     - Irradiance reflected on ground: shed transparency factor ~5% (factor de transparencia del panel: backsheet/Tedlar, encapsulante, reflective layer).
     - Structure shading factor ~10÷20% (postes, railes, clamps, torque-tube, cableado; incluye IAM trasero, altura del panel). Gráfica de "Shading factor $f_s$ (%)" por componente: Posts only 1,0%; Rails only 4,9%; Torque tube only 5,6%; Frames only 2,8%; Sum 14,3%. Tabla PVsyst: Structure Shading Factor 12,3%; Mismatch Loss Factor 3,5%.
     - Bifacial Mismatch ~3%: P-type 70%±5%; N-type 80%±5%; HJT 85%±5%. Panel PVsyst "PV Array behavior": Mismatch loss factor 3,0%; Module bifaciality factor 80,0%.

4. **Degradación de la potencia con la luz y el tiempo**: LID (Light Induced Degradation), PID (Potential Induced Degradation), UV-ID (Ultraviolet Induced Degradation), degradación anual. Gráfica de degradación lineal a 30 años: 99,00% inicial → n-type's DG warranty 87,40%; p-type's DG warranty 84,95% (Astronergy's linear degradation ≤0,4%/año).

5. **LID (Degradación inducida por luz):**
   - Se produce con las primeras horas de exposición para células de silicio tipo p [25 kWh/m²]. Afecta más al Si-monocristalino (más átomos de oxígeno) que al Si-policristalino. Asociada a la reacción entre átomos de oxígeno y átomos de boro (¿Ga?). No afecta (casi) al silicio tipo n. Para CIS se produce una ganancia inicial.
   - Valores de reducción por LID: p-type 0,1÷1,4% (típico -0,45%, fabricante indica <1,55%); n-type +0,5÷-0,5% (típico -0,3%, fabricante indica <0,6%).
   - Tabla de test LID n-type (IEC 61215-2:2021, MQT 01/02/06.1/08/15, LID 25kWh/m², requisito atenuación ≤0,8%, condiciones AM1,5·1000W/m²·25°C): 4 módulos de ejemplo con degradación resultante de 0,43%, 0,56%, 0,30%, 0,40%.

6. **UV-ID (Degradación inducida por luz ultravioleta):**
   - Rango UV [10-400nm]: UVA [315-400nm] no se absorbe por la capa de ozono; UVB [280-315nm] bastante absorbido; UVC [100-280nm] absorbido completamente (uso en desinfección).
   - Tabla test IEC 61215-2:2016 (Performance at STC, MQT 06.1, T=25±1°C, G=1000 W/m²): secuencia Initial(front) Pmax 708,3W Pass → After UV1(front) -2,1% → After HF1(front) -2,2% → After UV2(front) -0,7% → After HF2(front) -0,2%. **Total degradation of UV Sequence test: -5,2% → Result: Fail** (supera el límite admisible).

7. **PID (Degradación inducida por potencial):**
   - Existen 3 tipos de PID: a nivel de célula, de panel y de sistema. Debido a fluctuaciones de tensión entre módulos y tierra; fuga de electrones entre células y resto de componentes (marco, Tedlar, encapsulante EVA/POE/EPE/PVB, vidrio).
   - Origen: materiales utilizados (BOM), función de temperatura y humedad ambiente, configuración FV (PAT, tensión del string).
   - Valores estabilizados a 96h (mejor 288h): P-type -0,4÷1,5%; N-type -0,2÷1,3%; HJT -0,1÷1,2%.
   - Algunos fabricantes requieren para mantener garantía la puesta a tierra del negativo ⇒ inversor con transformador.
   - Tabla de test PID96h (IEC 61215-2:2021, ±1500V, criterio ≤5%): ejemplos con degradación de potencia entre -1,14% y +1,07%, y tasa bifacial (bifacial rate attenuation) entre -0,64% y +1,00%.

8. **Degradación anual del módulo**, causada por: degradación producida por la luz (VI, IR, UV); incremento de Rs por pérdida de adherencia de conectores o corrosión (vapor de agua); decremento de Rsh por migración de material a través de la unión PN; deterioro de componentes (encapsulante EVA/POE/EPE/PVB, capa antirreflectante, cristal); altas irradiancias y elevadas temperaturas (LeTID); microfisuras (snail trails); fallos en la PAT y tensiones en sistema (PID). Imagen de electroluminiscencia mostrando "PID severo" (patrón de degradación en tablero de ajedrez).
   - Garantía de fabricante (lineal): P-type <0,45 a 0,60%/año; N-type <0,40%/año; HJT <0,30%/año. Gráfica "Additional Value from Linear Warranty" mostrando degradación acumulada de 100% a 84,95% en 30 años con incrementos anuales marcados.

### 5. Comportamiento energético del inversor solar (pp. 49-53)

1. **Pérdidas de energía en un inversor solar**: eficiencia (estática, dinámica), mismatch (I,V), clipping/saturación, curtailment.

2. **Eficiencia de conversión DC/AC (estáticas):**
   - Curva de rendimiento en función de la potencia y tensión de entrada; curva de eficiencia en conversión DC/AC vs DC/DC/AC (IGBTs).
   - Gráfica: Efficiency [%] vs P Out (AC) [kW], para tres tensiones de entrada (U=1300V, U=1189V, U=930V) — eficiencia sube rápidamente de ~85% a >98% en los primeros ~50kW y luego se estabiliza en torno a 98-99% hasta 300kW; la tensión de 1189V presenta la mejor eficiencia en todo el rango.

3. **Pérdidas dinámicas MPPT / IGBTs:**
   - Eficiencia en el seguimiento del punto de máxima potencia (dinámicas): relación entre la potencia extraída por el MPPT del inversor ante perturbaciones (p.ej. nubes). Variación de rango MPPT en función de la potencia/tensión de red (inversor DC/DC/AC vs inversor DC/AC).
   - Gráfica de curva P-V con puntos P1/P2 en torno al MPP mostrando el algoritmo de búsqueda ("dP>0"/"dP<0"). Segunda gráfica: Potencia fotovoltaica [kW] vs Tensión fotovoltaica [V] con GMPP (Global MPP) y LMPP (Local MPP, mínimo local por sombreado parcial) y "Rango del MPP normal". Fuente: www.sma.de y TFG 2012, Álvaro Palomino, Univ. Carlos III, "Análisis datos técnicos de los inversores FV de conexión a red".

4. **Clipping — adecuación array FV-inversor:**
   - Hay que tener en cuenta temperaturas e irradiancias extremas del emplazamiento (P99 TMY vs P90 LP). Ejemplo "Operating conditions": Vmpp(60°C)=1013V; Vmpp(20°C)=1157V; Voc(-5°C)=1479V.
   - Pérdidas al arranque por tener Voc fuera de rango de tensión de funcionamiento (considerar longitud de string, temperatura mínima al arranque, tolerancia de tensión en fabricación).
   - Pérdidas por estar el PMP fuera de rango del MPPT; pérdidas de clipping por exceder la potencia DC máxima del inversor; pérdidas por curtailment de la red (requisitos de reactiva, limitaciones).
   - Gráfica "Array Voltage Sizing" (PVsyst): Current [A] vs Voltage [V], con curvas a distintas temperaturas de célula (T=20°C, T=60°C) mostrando Vmpp Min, Vmpp Nom, Vmpp Max, Voc(-5°C), e Inv. Imax DC como límite horizontal.

5. **Derrating — reducción por temperatura del inversor:**
   - Gráfica Power [kVA] vs Temperature [°C, 20-80]: potencia constante en Pmax=330kVA hasta ~40°C, luego reducción escalonada (Pnom=300kVA) hasta ~230kVA a 60°C. Fuente: PVsyst.
   - Causas del derrating: temperaturas externas muy elevadas, dificultad en la disipación de calor del inversor (filtros), inversor excesivamente subdimensionado (ratio DC/AC), altitud superior a la máxima de funcionamiento.

### 6. Pérdidas de energía en la instalación eléctrica (pp. 54-56)

1. **Pérdidas eléctricas y en conexiones**: esquema PV Generator → Inverter → LV/MV Transformer → Electricity Grid, con P_DC, P_AC, P_OUT y variables G (irradiancia) y T_A (temperatura ambiente) como entradas.
   - Cálculo de pérdidas de potencia eléctricas: secciones de cables en función de corriente máxima, temperatura, longitud de tramo, caídas de tensión, corriente de cortocircuito, material del cable, cos(φ) y flujos de carga. Cálculo de pérdidas (media y máximas) en función de longitud de tramo, material y parámetros eléctricos.
   - La temperatura se estima en función de la temperatura ambiente y la intensidad por el cable; hay que considerar si va bajo tubo, enterrado, por canaleta; se calcula a la temperatura máxima del aislamiento (p.ej. XLPE 90°C).

2. **Modelado energético de los componentes eléctricos — tabla comparativa de pérdidas por fabricante de transformador** (Huawei / Sungrow / Genérico):
   | Parámetro | Huawei | Sungrow | Genérico |
   |---|---|---|---|
   | Potencia nominal inversor (MW) | 48,75 | 8,96 | 8,96 |
   | Pérdidas hierro (MW) | 0,0337 | 0,00504 | 0,00504 |
   | Pérdidas cobre (MW) | 0,324 | 0,062586 | 0,062586 |
   | Pérdidas hierro (%) | 0,07% | 0,06% | 0,10% |
   | Pérdidas cobre (%) | 0,66% | 0,70% | 0,90% |

3. **Valores típicos de pérdidas eléctricas por etapa:**
   - DC (string inverter): ~0,5%
   - DC (central inverter + CB): ~1,5%
   - AC-LV (Inv string): ~1,0÷1,5%
   - AC-LV (Inv Central): despreciable
   - AC-MV: ~0,5%
   - Transformador: pérdidas en hierro ~0,07÷0,12%
   - Transformador: pérdidas en cobre (resistivas) ~0,67÷0,90%
   - AC-HV: muchos factores (no cuantificado en la fuente)
   - **Pérdidas en el hierro** (en vacío, en el núcleo): debidas a la magnetización de los núcleos del transformador, suelen ser constantes mientras la tensión de trabajo se mantenga constante.
   - **Pérdidas en el cobre**: pérdidas por efecto Joule en los devanados del transformador, dependen del factor de carga.

### 7. Indicadores de rendimiento energético de sistemas fotovoltaicos (pp. 57-67)

1. **Contexto**: se repite el diagrama de Sankey completo (idéntico al de la sección 1) junto con los "Datos del año de estudio" derivados de él:
   - Energía incidente: 1152 kWh/m²
   - Energía array: 1269 kWh/m²
   - Energía producida: 28.136 MWh/y
   - Producción específica: 1160 kWh/kWp/yr
   - **PR: 0,854**
   - Producción normalizada: 3,18 kWh/kWp/día
   - Pérdidas array: 0,42 kWh/kWp/día
   - Pérdidas sistema: 0,13 kWh/kWp/día
   - Se incluye también una imagen del layout de planta (distribución de mesas/strings en parcela).

2. **Definiciones de los KPIs (Key Performance Indicators):**
   - **Producción específica (SY, Specific Yield) [kWh/kWp/año]**:
     $$SY = \frac{\text{plant output (kWh)}}{\text{installed capacity (kWp)}}$$
     También llamado "Rendimiento específico". Indica el potencial de producción (kWh) de un emplazamiento para una potencia (kWp) dada durante un año tipo o real.
   - **Performance Ratio (PR) [%]**:
     $$PR = \frac{\text{actual plant output (kWh)}}{\text{nominal plant output (kWh)}}$$
     También llamado "Coeficiente de Rendimiento". Es una magnitud que, independientemente de la ubicación, indica la calidad de una instalación FV.
   - **Capacity Factor (CF) [%]**:
     $$CF = \frac{\text{plant output (kWh)}}{8760 \text{ horas} \times \text{installed capacity}}$$
     Ratio entre la generación (kWh) y la generación teórica operando a capacidad nominal durante un año completo (incluyendo la noche). Esquema con $P_A$ (potencia array) y $P_{TUN}$ (potencia hacia red) sobre el bloque generador-inversor-red.

3. **Producción Específica [kWh/kWp] — desarrollo:**
   - Factores que impactan: localización y datos meteorológicos (BBDD), disposición y orientación, selección de equipo BOS (módulos, estructura, inversores — los módulos bifaciales tienen otra escala y no se pueden comparar directamente), y si se toma a la entrada de los paneles da un KPI del recurso solar en vez de de la planta.
   - Balance de la eficiencia de planta (BOS efficiency): toma la energía a la salida del sistema; incluye eficiencia de inversores, clipping y eficiencia MPPT; incluye pérdidas eléctricas y mismatch.
   - **Valores típicos de mercado citados:**
     - Seguimiento 1 eje, Extremadura: **2200 kWh/kWp**
     - Estructura fija 25° (Sur), Sur de España: **~1600 kWh/kWp** (1800 kWh/kWp bifacial)
     - Estructura fija 25° (Sur), Alemania: **~850 kWh/kWp** (1150 kWh/kWp bifacial)
     - Estructura fija 25° (Este-Oeste), Alemania: **~1000 kWh/kWp**
   - **Pros**: KPI muy versátil para medir rendimiento (capacidad del emplazamiento); puede usarse con GHI y GTI; muy útil para comparativa de localizaciones (mismas condiciones) y para comparar diferentes diseños en un mismo emplazamiento.
   - **Contras**: no es un KPI universal, requiere especificar mucho las acotaciones (tiempo de medida, punto de medida, tecnología usada); no tiene en cuenta la bifacialidad, al no computar la potencia extra en el denominador.

4. **Performance Ratio [%] — desarrollo:**
   - Introducción: expresa la relación entre el rendimiento real y el nominal de una planta; permite el seguimiento del rendimiento actual y comparar con el diseño inicial; rango [0÷100%].
   - Factores que impactan: datos ambientales (irradiación, temperatura, suciedad, sombreado), periodo de registro, ratio DC/AC, rendimiento de módulos e inversor, pérdidas de cableado/transformadores, O&M (limpieza, fallos en trackers).
   - **Valores típicos de mercado citados:**
     - Seguimiento 1 eje, Extremadura: **~0,858** (0,887 bifacial)
     - Estructura fija 25° (Sur), Sur de España: **~0,859** (0,890 bifacial)
     - Estructura fija 25° (Sur), Alemania: **~(0,854 bifacial)** (valor no bifacial no especificado en la fuente)
     - Estructura fija 25° (Este-Oeste), Alemania: **~0,899**
   - **Pros**: aceptado a nivel mundial (especialmente por bancos) como KPI; da una idea bastante acertada del rendimiento de la planta durante su operación; muy útil para comparar sistemas iguales a lo largo del tiempo (actual contra fase de diseño).
   - **Contras**: no tiene en cuenta la bifacialidad; los valores se desvirtúan cuando se modifica la tecnología (tracker, backtracking, bifacial, topografía); es válido para valorar una planta ya seleccionada pero no para diseño (no valora la optimización de la planta).

5. **"Coeficientes" — método de regresión (no es Y_R/Y_A/Y_F ni ningún acrónimo estándar; la fuente lo llama simplemente "Coeficientes"):**
   - Introducción: expresa la relación entre el rendimiento real y el nominal de una planta; permite el seguimiento del rendimiento actual y comparar con el diseño en cualquier año; su rango compara energía producida.
   - Factores que impactan: datos ambientales (irradiación, temperatura, suciedad), curtailments (outages).
   - **Fórmula de energía esperada** (modelo de regresión cuadrática en irradiancia G y logarítmico en el periodo T, con coeficientes de temperatura A_T/B_T/C_T y de irradiancia A_G/B_G/C_G ajustados empíricamente por planta):
     $$E_{expected} = (A_T \cdot G^2 + B_T \cdot G + C_T) \cdot \ln T + (A_G \cdot G^2 + B_G \cdot G + C_G)$$
     (No se detalla en la fuente el método de ajuste de los coeficientes $A_T, B_T, C_T, A_G, B_G, C_G$ ni las unidades exactas de $G$ y $T$ — no especificado en la fuente.)
   - Gráfica "Monthly Error" (%) de este método a lo largo de un año: valores entre -0,028% (septiembre) y +0,554% (diciembre), la mayoría por debajo de 0,4%.
   - **Pros**: aceptado a nivel mundial (especialmente por bancos) como KPI; da una idea muy acertada del rendimiento durante la operación; tiene en consideración todos los problemas dentro del sistema FV (caja negra) y los independiza; presenta un error inferior frente al cálculo de PR (PVsyst).
   - **Contras**: no desglosa las pérdidas y dificulta averiguar el origen de los fallos; no considera el soiling, curtailment ni degradación; el sombreado incrementa el error (requiere uso de matriz de sombras).
   - **Comparativa gráfica final** (dos gráficas "Ten days period PR error Vs ENERGY error", usando coeficientes de un TMY): error de PR (rojo) vs error de energía (verde) en periodos de 10 días a lo largo de 2015 — el error de PR alcanza picos de hasta -6% en algunos periodos, mientras el error de energía se mantiene mucho más acotado (entre -1% y +1% aprox.), evidenciando que el método de coeficientes produce un error inferior al de PR. Segunda gráfica en valor absoluto: error absoluto de PR (rojo, hasta ~2,5%) vs error absoluto de energía (verde, siempre <1%).

## Datos clave (con página de origen)

- (p. 6) Diagrama de Sankey completo con cadena de pérdidas desde 1152 kWh/m² de irradiación horizontal global hasta 28.135.565 kWh inyectados en red (planta bifacial ejemplo, fuente PVsyst).
- (p. 12, 14) Ecuación del modelo de un diodo: $I = I_L - I_D - \frac{V+I \cdot R_s}{R_{Sh}}$; Fill Factor $FF = \frac{Vmp \cdot Imp}{Vco \cdot Isc}$, valor requerido >70-80%.
- (p. 15) Valores típicos $R_{Sh}$: 300-900 Ω (módulos), 2500-4500 Ω (células); $R_s$: 0,05-0,3 Ω.
- (p. 21) Estudio de suciedad Jordania: ratio anual con 1 limpieza/mes = 2,10%; sin limpiezas = 48%.
- (p. 27) Definición IAM: $IAM_B = \tau(\theta)/\tau(0)$.
- (p. 30) Tabla IAM usuario 0°→1,000 hasta 85°→0,719; pérdida IAM anual "user defined profile" = 0,82% frente a 2,62-3,56% de modelos genéricos (ASHRAE/Fresnel/Sandia).
- (p. 31) $AM = 1/\cos(\theta)$ y fórmula de Kasten-Young con corrección de curvatura terrestre.
- (p. 33) Ecuación de potencia por temperatura: $P = P_{STC} \cdot (G/G_{STC}) \cdot [1-\gamma(T_{CEL}-T_{CEL\_STC})]$; γ ≈ 0,35%/°C (Si-m), 0,25%/°C (Si-a).
- (p. 34) Coeficientes de temperatura normalizados de referencia: Pmax -0,29%/°C, Voc -0,25%/°C, Isc 0,045%/°C, NOCT 45±2°C.
- (p. 35) Siete modelos distintos de temperatura de célula (Faiman, Schott, Servant, Ross&Smokler, IEC-Sandia, PVsyst, Homer) con sus fórmulas completas.
- (p. 36) Pérdida por baja irradiancia ejemplo: $Pot_{200}/(Pot_{1000} \cdot 200/1000) = 0,962$; ensayos DEKRA y ENERTIS con criterio IEC 61215-2 de pérdida relativa <5% a 200 W/m².
- (p. 38) Tolerancia de potencia [0/+5W]&[0/+1%]; tolerancia en corriente ±4%; tolerancia en tensión ±3,5%.
- (p. 39-40) $P^*(A) = N_P \cdot N_S \cdot P^*(M)$; module mismatch loss 0,35-0,60%; string mismatch loss ~0,15%.
- (p. 41) Bifacial: structure shading factor ~10-20%; bifacial mismatch ~3% (P-type 70±5%, N-type 80±5%, HJT 85±5%).
- (p. 42) Degradación lineal a 30 años: 99,00% inicial → n-type 87,40%, p-type 84,95% (Astronergy ≤0,4%/año).
- (p. 43) LID: p-type -0,45% típico (fabricante <1,55%); n-type -0,3% típico (fabricante <0,6%).
- (p. 45) UV-ID: caso de ensayo con degradación total -5,2%, resultado **Fail** frente al criterio IEC 61215-2.
- (p. 46) PID (96h estabilizado, mejor 288h): P-type -0,4 a 1,5%; N-type -0,2 a 1,3%; HJT -0,1 a 1,2%.
- (p. 48) Degradación anual garantizada: P-type <0,45-0,60%/año; N-type <0,40%/año; HJT <0,30%/año.
- (p. 56) Pérdidas transformador ejemplo (Huawei): hierro 0,07%, cobre 0,66%; (Genérico): hierro 0,10%, cobre 0,90%.
- (p. 58) Ejemplo completo de resultados anuales de planta: SY=1160 kWh/kWp/yr, PR=0,854, producción normalizada 3,18 kWh/kWp/día.
- (p. 59) **Fórmulas de los tres KPIs principales**: $SY = \text{plant output (kWh)} / \text{installed capacity (kWp)}$; $PR = \text{actual output (kWh)} / \text{nominal output (kWh)}$; $CF = \text{plant output (kWh)} / (8760\text{h} \times \text{installed capacity})$.
- (p. 61) SY valores de mercado: seguimiento 1 eje Extremadura 2200 kWh/kWp; fija Sur España ~1600 (1800 bifacial); fija Sur Alemania ~850 (1150 bifacial); fija E-O Alemania ~1000 kWh/kWp.
- (p. 63) PR valores de mercado: seguimiento 1 eje Extremadura ~0,858 (0,887 bifacial); fija Sur España ~0,859 (0,890 bifacial); fija Sur Alemania ~(0,854 bifacial); fija E-O Alemania ~0,899.
- (p. 65) Fórmula del método de "Coeficientes": $E_{expected} = (A_T G^2+B_T G+C_T)\ln T + (A_G G^2+B_G G+C_G)$; error mensual entre -0,028% y +0,554%.
- (p. 67) Comparativa gráfica: error de PR alcanza picos de hasta -6% en periodos de 10 días, frente a un error de energía (método de coeficientes) acotado en ±1%.
- **NOTA IMPORTANTE**: el documento **no contiene** los acrónimos ni fórmulas Y_R (Reference Yield), Y_A (Array Yield), Y_F (Final Yield), A_PV, C_D o D_G solicitados en el encargo original. Los indicadores realmente desarrollados en esta presentación son SY (Specific Yield / Producción Específica), PR (Performance Ratio), CF (Capacity Factor) y el método de "Coeficientes" de regresión. Si el tutor Julio Amador usa la notación Y_R/Y_A/Y_F/A_PV/C_D/D_G en otra presentación del Módulo 6 (posiblemente M6_T2, ya indexada, o M6_T6/T7), esa es la fuente correcta a citar para esas fórmulas — no esta.

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo de análisis energético/resultados de simulación PVsyst del TFM (fase 8 de la metodología ERMA según memoria del proyecto). También aporta directamente al capítulo de dimensionado del campo FV (pérdidas de disposición, sombras, mismatch) y al de selección de inversor (clipping, curtailment, derrating).
- **Qué aporta exactamente**: (1) el desglose completo y ordenado de todas las pérdidas de un sistema FV siguiendo la estructura exacta del diagrama de Sankey de PVsyst, útil para justificar y verificar cada línea de pérdidas del informe de simulación del TFM; (2) las definiciones canónicas y fórmulas exactas de SY, PR y CF (con sus pros/contras de uso), que deberán emplearse literalmente al reportar los resultados de la simulación PVsyst del CPD en el capítulo de análisis energético; (3) valores de mercado de referencia (SY y PR típicos por tecnología/ubicación en España y Alemania) útiles para contrastar la plausibilidad de los resultados propios; (4) valores técnicos concretos (coeficientes de temperatura, tolerancias de fabricación, degradación LID/PID/UV-ID, pérdidas eléctricas por etapa) aplicables si el TFM necesita justificar hipótesis de pérdidas del sistema en la parametrización de PVsyst.
- **Confianza en los datos**: todas las cifras citadas en este resumen provienen literalmente de las diapositivas del documento (tablas de ensayos de laboratorio DEKRA/ENERTIS/fabricantes chinos, valores de PVsyst, estudios de campo de FRV); no se ha completado ningún dato con conocimiento general del modelo. Las fórmulas de Y_R/Y_A/Y_F/A_PV/C_D/D_G solicitadas en el encargo **no aparecen en esta fuente** y no deben atribuirse a este documento en el TFM.

## Notas de procesamiento

- **Documento leído íntegro: 68 páginas** (portada + 67 diapositivas de contenido), en 7 lecturas por rangos de 10 páginas (1-10, 11-20, 21-30, 31-40, 41-50, 51-60, 61-68). No se ha omitido ninguna diapositiva.
- **Discrepancia de portadas detectada y no resuelta**: la primera diapositiva (p. 1) corresponde a la "20 Edición 2025-2026" del Máster ERMA, mientras que la última diapositiva (p. 68, portada de cierre repetida) indica "XVIII Edición 2023-24". Esto sugiere que el material fue reutilizado/actualizado de una edición anterior del máster con una portada nueva pero sin actualizar la contraportada. No se ha podido determinar con certeza el año exacto de creación original del contenido técnico; por eso el campo `anio` del frontmatter queda marcado como indeterminado en vez de asumir uno de los dos años.
- Varias imágenes contienen texto en chino (tablas de ensayo de fabricantes de módulos, pp. 15, 26, 44-47) correspondientes a informes de certificación IEC 61215-2 de un fabricante chino no identificado por nombre en el documento; se ha preservado la traducción al español/inglés de los campos relevantes tal como aparece en la propia tabla bilingüe de la fuente.
- Algunas preguntas retóricas del propio documento quedan sin resolver explícitamente en el contenido (marcadas con "??" en las diapositivas 4, 5 y 18 sobre "factores determinantes" y "pérdidas por suciedad") — se han transcrito tal cual, sin completarlas con conocimiento externo, siguiendo la regla de no rellenar huecos.
- La fórmula del método de "Coeficientes" (p. 65) se presenta en la fuente sin especificar el procedimiento de ajuste de sus 6 coeficientes ($A_T, B_T, C_T, A_G, B_G, C_G$) ni las unidades exactas de las variables $G$ (irradiancia, probablemente en W/m² o kWh/m²) y $T$ (posiblemente el periodo temporal en algún tipo de unidad, dado que aparece como $\ln T$); esto se ha marcado explícitamente como "no especificado en la fuente" en el cuerpo del resumen.
- Se han omitido del texto (no aportan contenido técnico adicional) las repeticiones del índice de la presentación que aparecen al inicio de cada sección (diapositivas separadoras 8, 24, 37, 49, 54, 57) — su única función es de navegación y ya están reflejadas en el índice general de la sección "0. Portada e índice".
