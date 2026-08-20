---
title: "Trabajo previo del Módulo 6 — Autoconsumo fotovoltaico para el sistema HVAC de un CPD"
tipo: trabajo-propio
autor: "Mario Carrión Sirvent (Módulo 6, Autoconsumo Fotovoltaico — Julio Amador Guerra)"
anio: 2026
densidad: exhaustivo
fecha_resumen: 2026-08-20
fuente_original: "Documentacion de apoyo/Trabajo Autoconsumo CPD/ (AUTOCONSUMO FOTOVOLTAICO PARA SISTEMA HVAC DE UN CPD.pptx + Trabajo_DataCenter_Project.VC0-Report1.pdf)"
tags: [fotovoltaica, autoconsumo, CPD, data-center, HVAC, PVsyst, Tres-Cantos, sin-excedentes, trabajo-previo, baseline, ERMA-modulo6]
related: [autoconsumo-industrial-san-martin-pyl, instalacion-fotovoltaica-centro-logistico-mad9]
---

# Trabajo previo del Módulo 6 — Autoconsumo FV para el sistema HVAC de un CPD

> **Qué es este documento.** El TFM de Mario Carrión amplía un trabajo que él mismo entregó en el Módulo 6 del Máster ERMA el 08/01/2026, sobre **el mismo CPD**. Aquel trabajo resolvió **una sola variante** (cubierta central del edificio, sin almacenamiento). Este resumen fija las **cifras canónicas** de esa variante para que sirvan de línea base contra la que comparar las variantes nuevas del TFM (marquesinas del aparcamiento, entre otras) y para no recalcular desde cero lo que ya está simulado y corregido por el tutor.
>
> **Estatus de citabilidad:** trabajo académico propio, no publicado. No es fuente citable, pero sus resultados sí son datos de partida legítimos del TFM siempre que se re-simulen o se declaren como procedentes del trabajo previo.

---

## 1. Datos de partida

### 1.1 Emplazamiento

| Campo | Valor |
| --- | --- |
| Localidad | Tres Cantos (Madrid) |
| Dirección | RD Europa, 3 |
| Latitud | 40° 35′ 53″ N (40,60 °N en PVsyst) |
| Longitud | −3° 43′ 2″ O (−3,72 °O en PVsyst) |
| Altitud | 741 m |
| Huso horario | UTC+1 |
| Albedo | 0,20 |

### 1.2 Normativa aplicada

| Ámbito | Normas |
| --- | --- |
| Edificación | Ley 38/1999 (LOE) · RD 314/2006 (CTE) |
| Seguridad | Ley 31/1995 (PRL) · RD 513/2017 (RIPCI) · RD 2267/2004 (RSCIEI) · RD 145/2023 (mod. RSCIEI) |
| Ambiental | Ley 7/2021 (cambio climático y transición energética) · RD 105/2008 (RCD) |
| Eléctrica | RD 842/2002 (REBT + ITC) · UNE-EN IEC 62446-1 · UNE-EN IEC 62116 (anti-isla) · UNE-EN IEC 61730-1 y 62109-1 |
| Comunidad | Ley de Propiedad Horizontal (emplazamiento de uso común a varias empresas) |
| Renovables | Ley 24/2013 (sector eléctrico) · RD 1183/2020 (acceso y conexión) |
| Autoconsumo | **RD 244/2019** |

### 1.3 Radiación solar y clima

Comparativa que justificó la elección de base de datos:

| Característica | METEONORM 8.2 | **PVGIS 5.3** (elegida) | NASA-SSE |
| --- | --- | --- | --- |
| Nº años con medidas | 20 | TMY: 1990 | 13 |
| Resolución temporal | Mensual | **Horaria** | Mensual |
| Resolución espacial | Puntual (interpolación) | **~5 km** | ~111 km |
| Fuente de datos | Estaciones + satélite (~28 %) | PVGIS (API) – TMY | Satélite |
| Precisión | MBE ≈ 0 % · RMS ≈ 6,8 % | **MBE ≈ 0,07 % · RMS ≈ −0,45 %** | MBE ≈ −1 % · RMS ≈ 14,5 % |

Se eligió **PVGIS 5.3 (API TMY)**: mejor resolución temporal (horaria, imprescindible para cruzar con el consumo), mejor resolución espacial y menor error.

Datos de clima:

| Dato | Valor | Fuente |
| --- | --- | --- |
| Temperatura ambiente mínima diurna | −10 °C (20/01/1978) | AEMET, efemérides extremas |
| Temperatura ambiente máxima diurna | 40,0 °C (12/04/1987) | AEMET, efemérides extremas |
| **Inclinación óptima** | **37–38°** | PVGIS |
| Temperatura ambiente media anual | 14,23 °C | PVsyst (TMY) |

> **Decisión clave y contraintuitiva:** la inclinación óptima es 37–38°, pero **se instaló a 10°**. El motivo es la altísima densidad de ocupación en sheds (GCR 86,3 %): a mayor inclinación, mayor separación entre filas y menos potencia total en 450 m². La guía lo permite porque la pérdida por inclinación (8,62 %) se compensa con creces con la potencia adicional instalada. Es el ejemplo perfecto de que en cubierta limitada **manda la superficie, no el óptimo angular** — argumento reutilizable en el TFM para las marquesinas.

### 1.4 Superficie disponible (variante única del trabajo previo)

| Campo | Superficie 1 — cubierta central |
| --- | --- |
| Área total | 550 m² |
| Orientación | −30° |
| Inclinación | 10° |
| Características | Cubierta plana de chapa |
| Pérdidas por orientación | 1,22 % |
| Pérdidas por inclinación | 8,62 % |
| **Pérdidas globales** | **11,4 %** |
| **Superficie neta disponible** | **450 m²** (factor de aprovechamiento 0,82) |

### 1.5 Consumo eléctrico y tarifa

| Campo | Valor |
| --- | --- |
| Propiedad | SIEMENS, S.A. |
| Uso | Parque tecnológico |
| Red | Trifásica en BT |
| Distribuidora | i-DE Redes Eléctricas Inteligentes, S.A.U. |
| Comercializadora | Acciona Green Energy Developments, S.L.U. |
| Potencia contratada | 2.300 kW (P1–P5) y 3.300 kW (P6) |
| Tarifa | **6.1TD** |
| Periodos | 6 (P1–P6) |

Consumo mensual introducido en PVsyst (necesidades del usuario, valores mensuales, MWh):

| Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic | **Año** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 96,6 | 92,4 | 101 | 98,0 | 109 | 116 | 121 | 119 | 109 | 107 | 97,1 | 95,3 | **1.260** |

> Perfil casi plano con repunte estival — la firma típica del HVAC de un CPD (carga 24/7, refrigeración modulada por temperatura exterior). Máximo julio 121 MWh, mínimo febrero 92,4 MWh: sólo un **31 % de oscilación** entre mes punta y mes valle.

---

## 2. Determinación de la potencia (criterio más restrictivo)

| Criterio | ¿Limita? | Razón |
| --- | --- | --- |
| Normativa | **No** | Edificio existente + reforma no integral |
| Punto de conexión | **No** | Potencia nominal > 100 kW admisible |
| % de autoconsumo | **No** | HVAC de CPD = gran consumo plano 24/7, absorbe todo |
| **Superficie disponible** | **SÍ** | 450 m² netos |
| **Capacidad de inversión** | **SÍ** | La propiedad saca los proyectos a subasta |

Resultado: la potencia la fija la **superficie**, no la demanda. Es el hecho estructural del caso.

---

## 3. Selección del módulo

| Característica | SunPower Maxeon 6 | **REC Alpha Pure-RX** (elegido) | Jinko Tiger Neo 72HL4 |
| --- | --- | --- | --- |
| Potencia pico STC | 440 Wp | **470 Wp** | 585 Wp |
| Tecnología de célula | IBC (back-contact) | **HJT (heterounión)** | TOPCon (tipo N) |
| Coef. temperatura potencia | −0,29 %/°C | **−0,24 %/°C** | −0,29 %/°C |
| Degradación LID | 2 % | **0 %** | 1 % |
| Degradación PID | Solicitar | **0 % (anti-PID)** | 0 % (anti-PID) |
| Garantía de potencia | 40 años (0,25 %/año) | 25 años (0,25 %/año) | 30 años (0,30 %/año) |
| Garantía de producto | 40 años | 25 años | 12 años |
| Características especiales | *shade resilience*, larga garantía | **Coef. térmico muy bajo, alta densidad de potencia, sin LID** | Mejor captación, bifacial |
| Posición en ranking | 1 (EnergySage) | **1 (CleanEnergyReviews)** | 7 (CleanEnergyReviews) |
| Precio | 0,85–1,10 €/Wp | **0,45–0,60 €/Wp** | 0,15–0,25 €/Wp |

Elegido **REC Alpha Pure-RX 470 Wp**: coeficiente térmico el mejor del trío (−0,24 %/°C, relevante en Madrid con 40 °C de máxima), LID y PID nulos, y **alta densidad de potencia** — decisivo cuando el limitante es la superficie. En PVsyst se modeló como `REC470AA Pure-RX` (base de datos original).

## 4. Selección del inversor

| Característica | **Huawei SUN2000-100KTL-M2** (elegido) | Sungrow SG110CX | SMA Sunny Tripower CORE2 STP110-60 |
| --- | --- | --- | --- |
| Tipo | String 3F | String 3F | String 3F |
| Tecnología | Estándar | Estándar | Estándar |
| Potencia nominal AC | **100 kW** | 110 kW | 110 kW |
| Eficiencia máxima | **98,8 %** | 98,7 % | 98,6 % |
| Nº MPPT | 10 | 9 | 12 |
| Intervalo DC de MPP | 200–1000 V | 200–1000 V | 500–800 V |
| Intensidad máxima DC | **30 A** | 26 A | 26 A |
| Índice de protección | IP66 | IP66 | IP66 |
| Precio | 0,0489 €/W | 0,0426 €/W | 0,0402 €/W |

Elegido **Huawei SUN2000-100KTL-M2**: mayor eficiencia, mayor intensidad máxima DC y ventana MPP amplia (200–1000 V). Es el más caro de los tres, así que la justificación es técnica, no económica.

> **Ojo con la nomenclatura:** la presentación del trabajo previo escribe «SUN2000-100**TKL**-M2»; la denominación correcta de Huawei y la que usa PVsyst es «SUN2000-100**KTL**-M2-400Vac». Corregirlo al trasladarlo al TFM.

---

## 5. Configuración del sistema (fuente: informe PVsyst)

| Parámetro | Valor |
| --- | --- |
| Proyecto / variante | `Trabajo_DataCenter` / «Real» (VC0) |
| Versión y fecha | PVsyst **V8.0.19**, simulación 09/01/2026 19:29 |
| Disposición | *Sheds*, single array |
| Inclinación / azimut | **10° / −30°** |
| Nº de sheds | 27 |
| Separación entre sheds | 1,42 m |
| Anchura sensible | 1,21 m |
| **GCR shading** | **86,3 %** |
| Ángulo límite de perfil | 44,9° |
| Bandas inactivas | 0,02 m superior / 0,02 m inferior |
| Modelo de transposición | Perez · difusa importada · circumsolar separada |
| Sombras cercanas | Lineales (*slow*, simuladas) |
| Horizonte | Altura media 1,5° (PVGIS API) · factor difuso 1,00 · factor albedo 0,91 |
| **Módulos** | 216 unidades · **18 strings × 12 en serie** |
| **Potencia nominal STC** | **102 kWp** |
| En condiciones de operación (50 °C) | Pmpp 95,5 kWp · Umpp 619 V · Impp 154 A |
| Área de módulos / de célula | 450 m² / 419 m² |
| **Inversores** | 1 unidad (0,9 utilizada) · **90,0 kWac** totales |
| Tensión de operación | 200–1000 V · P máx. (≥40 °C) 110 kWac |
| **Ratio DC/AC** | **1,13** |
| Reparto entre MPPT | Sin *power sharing* (9 MPPT al 10 %) |

**Definición constructiva:**

| Campo | Valor |
| --- | --- |
| Tipo de autoconsumo | **Sin excedentes** (*no grid reinjection*) |
| Punto de conexión | CGBT con **sistema antivertido** |
| Ubicación del inversor | Cubierta |
| Área ocupada | 450 m² |
| Estructura soporte | **Renusol FS Pro 10-S IFP** |
| — superficie de empleo | Cubierta plana de chapa perforable |
| — fijación | Fijación mecánica al tejado + sellado de estanqueidad |
| — soporte de cumbrera | F (1190–1230 mm) |
| — criterio de dimensionado | Comprobación de cargas de viento y nieve según **CTE** |

---

## 6. Hipótesis de pérdidas

| Tipo de pérdida | Hipótesis (presentación) | Parámetro PVsyst | Diagrama de pérdidas |
| --- | --- | --- | --- |
| Térmicas | Modelo térmico PVsyst (4,50 %) | Uc = 20,0 W/m²·K · Uv = 0,0 W/m²·K·m/s | **−4,4 %** (temperatura) |
| Eléctricas — cableado DC | 1,00 % | Resistencia global 64 mΩ → **1,50 % en STC** | **−1,0 %** (óhmicas) |
| Eléctricas — inversor | 1,50 % | — | **−1,5 %** (operación) |
| Tolerancia de potencia | 0,53 % | *Module Quality Loss* = **−0,53 %** | **+0,5 % (GANANCIA)** |
| Degradación LID | 0,0 % | — | 0,0 % |
| Degradación PID | 0,0 % | — | 0,0 % |
| Dispersión de parámetros | Módulos 2,00 % · strings 0,05 % | 2,00 % en MPP / 0,05 % | **−2,1 %** (conjunta) |
| Suciedad | 1 % | *Soiling* 1,0 % | **−1,0 %** |
| Ángulo de incidencia (IAM) | 1,9 % | Perfil definido por el usuario | **−1,9 %** |
| Indisponibilidad | 0,5 % · consumo nocturno 0,0 % | 0,5 % del tiempo (1,8 días, 3 periodos) | **−0,2 %** |

Perfil IAM introducido (definido por el usuario):

| 0° | 30° | 45° | 60° | 70° | 75° | 80° | 85° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,000 | 1,000 | 1,000 | 0,974 | 0,907 | 0,832 | 0,688 | 0,445 | 0,000 |

> **Dos avisos para el TFM.** (1) El *module quality loss* de −0,53 % es una **ganancia** de +0,5 %, no una pérdida: la presentación lo lista en la columna de pérdidas y hay que redactarlo con cuidado. (2) El cableado DC aparece como 1,50 % en el cuadro de parámetros («at STC») y como 1,0 % en el diagrama de pérdidas (real anual); son dos cosas distintas y hay que decir cuál se cita.

### Diagrama de pérdidas completo (cascada anual)

```
1786 kWh/m²   Irradiación global horizontal
   +8,5 %     → Global incidente en el plano del captador
   −0,1 %     Sombras lejanas / horizonte
   −3,9 %     Sombras cercanas: pérdida de irradiancia
   −1,0 %     Factor de suciedad
   −1,9 %     Factor IAM sobre la global
1806 kWh/m² × 450 m²   Irradiación efectiva sobre captadores
              [conversión FV — eficiencia en STC = 22,59 %]
183,55 MWh    Energía nominal del generador (a eficiencia STC)
   −0,9 %     Pérdida por nivel de irradiancia
   −4,4 %     Pérdida por temperatura
   +0,5 %     Module quality loss (ganancia)
   −2,1 %     Mismatch de módulos y strings
   −1,0 %     Pérdidas óhmicas de cableado
169,43 MWh    Energía virtual del generador en el MPP
   −1,5 %     Pérdida del inversor en operación (eficiencia)
    0,0 %     Sobre potencia nominal / corriente máx. / tensión / umbrales
    0,0 %     Consumo nocturno
166,83 MWh    Energía disponible a la salida del inversor
   −0,2 %     Indisponibilidad del sistema
166,55 MWh    → al usuario desde solar   (+ 1093,44 MWh desde red)
```

---

## 7. Resultados energéticos (CIFRAS CANÓNICAS)

### 7.1 Balance energético

| Símbolo | Magnitud | Valor |
| --- | --- | --- |
| E_PV / *Produced Energy* | Energía generada por el sistema FV | **166,55 MWh** |
| E_A / *E_Solar* | Energía fotovoltaica autoconsumida | **166,5 MWh** |
| E_TUN | Energía inyectada en la red de distribución | **0 MWh** |
| E_FUN / *EFrGrid* | Energía consumida de la red de distribución | **1.093,4 MWh** |
| E_L / *Used Energy* | Energía consumida por el usuario | **1.259,99 MWh** |
| E_NUN | Energía neta aportada por la red | **1.093,4 MWh** |

> ⚠️ **Errata detectada en el trabajo previo.** La diapositiva 23 de la presentación da E_PV = **165,55** MWh, mientras que el informe PVsyst (páginas 2, 7 y 8) da **166,55** MWh de forma consistente. Es un error tipográfico de la presentación. **La cifra correcta es 166,55 MWh** — corregirla al trasladarla al TFM.

### 7.2 Tabla resumen de resultados (los 9 parámetros ERMA)

| Parámetro | Símbolo | Valor | Unidades |
| --- | --- | --- | --- |
| Irradiación global sobre el generador | Y_R | **1.937,60** | kWh/m² |
| Índice de productividad del generador | Y_A | **1.668,72** | kWh/kWp |
| Índice de productividad final del sistema | Y_F | **1.640,98** | kWh/kWp |
| Rendimiento (Performance Ratio) | PR | **84,67** | % |
| Energía total producida | E_PV | **166,55** | MWh |
| Autoconsumo | A_PV | **100** | % |
| Autosuficiencia sin balance neto | C_D | **13,22** | % |
| Autosuficiencia con balance neto | C_D,NM | **13,22** | % |
| Dependencia de la red | D_G | **86,78** | % |

Producción específica: **1.641 kWh/kWp/año**. *Solar Fraction* PVsyst: **13,22 %** (= C_D).

### 7.3 Balance mensual (informe PVsyst, página 7)

| Mes | GlobHor kWh/m² | DiffHor kWh/m² | T_Amb °C | GlobInc kWh/m² | GlobEff kWh/m² | EArray MWh | E_User MWh | E_Solar MWh | EFrGrid MWh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Enero | 79,2 | 22,95 | 3,48 | 100,7 | 84,1 | 8,3 | 96,6 | 8,2 | 88,4 |
| Febrero | 95,3 | 27,77 | 6,15 | 112,7 | 101,1 | 9,8 | 92,4 | 9,7 | 82,7 |
| Marzo | 149,8 | 45,66 | 10,02 | 166,1 | 155,0 | 14,8 | 101,0 | 14,6 | 86,5 |
| Abril | 151,5 | 68,96 | 9,79 | 158,1 | 149,7 | 14,3 | 98,0 | 14,1 | 83,9 |
| Mayo | 207,5 | 76,51 | 17,21 | 213,8 | 204,9 | 19,1 | 108,8 | 18,9 | 89,9 |
| Junio | 232,2 | 72,53 | 23,55 | 235,0 | 226,2 | 20,7 | 115,5 | 20,4 | 95,1 |
| Julio | 240,9 | 60,21 | 27,55 | 245,8 | 236,8 | 21,4 | 121,4 | 21,1 | 100,3 |
| Agosto | 207,4 | 49,78 | 25,85 | 217,4 | 208,5 | 19,0 | 118,8 | 18,7 | 100,1 |
| Septiembre | 167,1 | 46,02 | 21,91 | 182,5 | 172,9 | 16,0 | 108,5 | 15,7 | 92,8 |
| Octubre | 116,6 | 37,82 | 12,80 | 134,2 | 122,5 | 11,7 | 106,5 | 11,5 | 95,0 |
| Noviembre | 72,4 | 28,28 | 7,02 | 87,0 | 75,7 | 7,4 | 97,1 | 7,1 | 90,0 |
| Diciembre | 65,9 | 21,96 | 4,82 | 84,2 | 69,0 | 6,8 | 95,3 | 6,6 | 88,7 |
| **Año** | **1.785,8** | **558,44** | **14,23** | **1.937,6** | **1.806,3** | **169,4** | **1.260,0** | **166,5** | **1.093,4** |

*EUnused* anual: −0,01 MWh (≈ 0, confirma que el antivertido no está recortando producción).

---

## 8. Conclusiones del trabajo previo y qué abre el TFM

**Lo que quedó demostrado:**

1. El diseño está **limitado por superficie**, no por demanda. El HVAC del CPD absorbe cuanto se produzca.
2. Con 450 m² de cubierta central caben **102 kWp** que cubren sólo el **13,22 %** del consumo anual. El CPD consume **7,6 veces** lo que esa cubierta puede generar.
3. El autoconsumo es del **100 %** por construcción (sin excedentes, con antivertido) y las pérdidas por vertido no realizado son nulas (EUnused ≈ 0). No se está desaprovechando nada.
4. El PR de **84,67 %** es alto y sano; el diseño no tiene margen de mejora relevante por la vía de reducir pérdidas.

**Qué se deduce para el TFM:**

- La única palanca real para subir C_D es **más superficie**: de ahí las marquesinas del aparcamiento y las demás variantes. Cualquier variante nueva debe reportar su C_D y compararlo con el 13,22 % de base.
- **El almacenamiento no se justifica por el mismo argumento que en el TFM de Manuel Arcas.** Allí había excedentes que guardar; aquí A_PV ya es 100 % y no sobra ni un kWh. La justificación de la batería tiene que venir por otra vía: arbitraje entre periodos de la tarifa **6.1TD** (6 periodos, gran diferencial P1/P6), recorte de punta de potencia contratada (2.300/3.300 kW son cifras muy altas: el término de potencia pesa), o respaldo de la carga crítica. **Hay que demostrarlo con el modelo horario en Excel, no darlo por supuesto.**
- Con potencia FV mayor (varias variantes sumadas) puede que sí aparezcan excedentes en horas centrales de fin de semana o de meses valle, y entonces el caso de la batería cambia. Es una hipótesis a verificar, no una conclusión.
- Falta por completo el **análisis económico** (fase 9 de la guía): el trabajo previo llegó sólo hasta el análisis energético. Es aportación neta del TFM.

**Erratas del trabajo previo a corregir al reutilizarlo:**

| Dónde | Dice | Debe decir |
| --- | --- | --- |
| Presentación, diapositiva 23 | E_PV = 165,55 MWh | **166,55 MWh** |
| Presentación, diapositiva 11 | Huawei SUN2000-100**TKL**-M2 | Huawei SUN2000-100**KTL**-M2 |
| Presentación, diapositiva 18 | Tolerancia de potencia «0,53 %» como pérdida | Es **ganancia** de +0,5 % (loss fraction −0,53 %) |

---

## 9. Ficheros fuente

| Fichero | Contenido |
| --- | --- |
| `Documentacion de apoyo/Trabajo Autoconsumo CPD/GUIA_PLANTILLA Estudio Autoconsumo FV ERMA20.pptx` | Guía metodológica oficial del Módulo 6 (38 diapositivas). Metodología volcada en el agente `ingeniero-dominio`. |
| `Documentacion de apoyo/Trabajo Autoconsumo CPD/AUTOCONSUMO FOTOVOLTAICO PARA SISTEMA HVAC DE UN CPD.pptx` | Presentación entregada por Mario (26 diapositivas, 08/01/2026). |
| `Documentacion de apoyo/Trabajo Autoconsumo CPD/Trabajo_DataCenter_Project.VC0-Report1.pdf` | **Informe PVsyst V8.0.19, 9 páginas — fuente canónica de toda cifra energética.** |
