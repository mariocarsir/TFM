---
title: "Instalación fotovoltaica para autoconsumo en centro logístico de almacenaje (Amazon MAD9)"
tipo: tfm-referencia
autor: "Diego Fernandes Alves (tutor: Julio Amador Guerra)"
anio: 2025
densidad: exhaustivo
fecha_resumen: 2026-08-16
fuente_original: "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Documentacion de apoyo\Ejemplos TFM\TFM-MAD9_signed.pdf"
tags: [fotovoltaica, autoconsumo, almacenamiento, baterias, PVsyst, industrial, TFM-referencia, analisis-economico, LCOE, VAN, TIR, media-tension, Huawei, JA-Solar]
related: []
---

# Instalación fotovoltaica para autoconsumo en centro logístico de almacenaje (Diego Fernandes Alves, 2025)

> **Nota de no-citabilidad:** este documento es un TFM de otro autor (Máster ERMA, curso 2024/2025, UPM), tutorizado por el mismo tutor de Mario (Julio Amador Guerra). No es fuente académica citable en el TFM de Mario Carrión, pero sirve como referencia de estructura, nivel de detalle, metodología de cálculo, criterios de dimensionado de almacenamiento y formato esperado por el tribunal ERMA, por ser el trabajo más cercano en temática y tutor de entre los TFM de referencia disponibles (autoconsumo fotovoltaico industrial de gran escala con almacenamiento en baterías, sin excedentes, en media tensión).

## Resumen

El TFM desarrolla un estudio técnico-económico completo para una instalación fotovoltaica de autoconsumo sin excedentes en el centro logístico Amazon MAD9 (Alcalá de Henares, Madrid), con una potencia pico de 2,71 MWp (4.928 módulos JA Solar de 550 Wp), 8 inversores Huawei SUN2000-330KTL-H1 (330 kW) y un sistema de almacenamiento de 2.000 kWh (baterías Huawei LUNA2000), conectado en media tensión (20 kV) mediante una estación prefabricada Ingeteam. Se comparan 24 configuraciones (combinaciones de número de módulos/inversores × 3 capacidades de batería: 200, 2.000 y 4.500 kWh) simuladas en PVsyst v8.0.13, evaluando producción, autoconsumo, Performance Ratio y viabilidad económica (CAPEX, VAN, TIR, LCOE, payback). Se selecciona la batería de 2.000 kWh como óptimo técnico-económico frente a las de 200 kWh (retorno más rápido pero requiere reposición en el año 16 por desgaste de ciclos) y 4.500 kWh (sobredimensionada, penaliza el VAN). La propuesta final alcanza una producción anual de 4.150,8 MWh, un 87,5 % de autoconsumo, un PR del 70,61 %, una inversión de 2.372.000 €, un ahorro anual de 498.096 €, un payback de 5,75 años, un VAN de 4.481.881,96 € (TIR 15,76 %) y un LCOE de 0,0393 €/kWh. El documento incluye además esquema de medida y tramitación normativa (autoconsumo tipo 31-A CNMC), sistema antivertido, monitorización FusionSolar, plan de mantenimiento/garantías, y anexos con planos eléctricos, fichas técnicas, informe completo de PVsyst y cálculos eléctricos en BT (Caneco BT).

## Contenido técnico

### Estructura del documento (índice original, 85 páginas de memoria + 4 anexos hasta p. 225)

```
RESUMEN
LISTADO DE REFERENCIAS Y PARÁMETROS (ilustraciones, tablas, ecuaciones, definiciones)
1. INTRODUCCIÓN (objetivo, alcances, antecedentes, normativa aplicable, metodología)
2. DATOS INICIALES (titular, emplazamiento, superficie, instalación eléctrica, consumo, datos meteorológicos)
3. DESCRIPCIÓN DE INSTALACIÓN (características generales, sombreado/orientación,
   evaluación de 24 propuestas y selección final, potencia prevista, punto de conexión y
   medida, líneas y canalizaciones, esquema unifilar, puesta a tierra)
4. MONITORIZACIÓN (funciones, acceso, compatibilidad, beneficios, documentación técnica)
5. ANÁLISIS ENERGÉTICO (producción estimada, ahorro, % autoconsumo, simulación temporal)
6. ANÁLISIS ECONÓMICO (listado de materiales, presupuesto, conclusiones económicas)
7. MANTENIMIENTO Y GARANTÍAS
8. CONCLUSIONES
9. BIBLIOGRAFÍA
ANEXOS: I Planos eléctricos | II Fichas técnicas de equipos | III Simulación PVsyst | IV Cálculos eléctricos BT
```

**Nota de muestreo:** el PDF tiene 225 páginas en total. Las páginas 1-85 (memoria completa) se han leído íntegramente. El Anexo I (Planos eléctricos, pp. 87-123, formato EPLAN/CAD, contenido gráfico sin texto sustancial) y el Anexo IV (Cálculos eléctricos BT, pp. 155-225, salida de software Caneco BT: fichas de cálculo de cortocircuito/caída de tensión por circuito, listados de folios) se han verificado como existentes y se describe su contenido, pero no se ha extraído su detalle numérico exhaustivo por tratarse de salidas de software repetitivas por circuito, de bajo valor narrativo. El Anexo II (Fichas técnicas, pp. 124-141) y el Anexo III (Informe de simulación PVsyst, pp. 142-154) sí se han extraído con el detalle numérico relevante (ver más abajo).

### 1. Introducción

**1.1 Objetivo:** estudio técnico y económico completo de una instalación FV de autoconsumo sin excedentes para el centro logístico Amazon MAD9, con almacenamiento en baterías, buscando maximizar autoconsumo directo, reducir pérdidas y optimizar el aprovechamiento de la energía almacenada.

**1.2 Alcances:** caracterización del edificio; diseño técnico (módulos, inversores, antivertido, protecciones, esquema unifilar, puesta a tierra); simulación energética; estudio económico; sistema de monitorización; plan de mantenimiento y garantías; documentación técnica (planos, memoria de cálculos, fichas técnicas). No incluye ejecución física.

**1.3 Antecedentes:** contextualiza el interés creciente del sector logístico en autoconsumo FV por su alta demanda continua (24/7) y disponibilidad de cubierta. Menciona explícitamente el apagón eléctrico nacional de abril de 2025 como factor que "reavivó el debate en torno a la estabilidad de la red" y aceleró el interés por generación + almacenamiento integrados — dato de contexto sectorial potencialmente citable como antecedente (verificar en fuente primaria antes de usar en el TFM de Mario, esta mención es de un TFM no citable).

**1.4 Normativa aplicable:** RD 244/2019 (autoconsumo); REBT (RD 842/2002) e ITC-BT; RAT (RD 337/2014) e ITC-RAT (conexión en MT 20 kV); RSCIEI (RD 2267/2004, seguridad contra incendios industrial); CTE DB-HE; normativa autonómica/municipal (Alcalá de Henares); Orden ITC/3860/2007 (RUPM, puntos de medida).

**1.5 Metodología:** 5 fases — (1) recopilación de datos iniciales, (2) diseño técnico, (3) simulación energética con PVSyst, (4) análisis económico, (5) documentación técnica y normativa. Herramientas: **PVSyst** (simulación/modelado), **AutoCAD** (planos dimensionales), **EPLAN** (planos eléctricos), **CANECO BT** (cálculos eléctricos en BT), **Microsoft Excel** (análisis económico).

### 2. Datos iniciales

- **Emplazamiento:** Camino de los Afligidos, 28805 Alcalá de Henares (Corredor del Henares, acceso A-2). Cubierta plana >70.000 m², con lucernarios y unidades técnicas que condicionan el aprovechamiento.
- **Superficie disponible para FV:** 46.550 m² (tras descontar retranqueos y pasillos técnicos; excluye aún lucernarios/escotillas, contemplados en la simulación).
- **Suministro eléctrico:** distribuidora UFD (Unión Fenosa Distribución, grupo Naturgy); comercializadora Naturgy Energy Group. Anillo interior en MT a 20 kV con varios centros de transformación internos.
- **Consumo eléctrico:**
  - Consumo anual total: **4.721,8 MWh**
  - Potencia pico registrada: **1.318 kW**
  - Patrón: operativa 24/7, estable en días laborables, con caída en fines de semana. Perfil horario por estaciones (Ilustración 4) muestra picos coincidentes con franjas de mayor actividad logística.
- **Coordenadas geográficas:** Latitud 40,506° N, Longitud -3,320° O, Altitud 594 m.

**Comparación de bases de datos meteorológicas** (tablas 1-3, valores mensuales de irradiación global GLOBH, difusa DIFFH, temperatura y viento):

| Mes | Meteonorm GLOBH (kWh/m²) | NASA SSE GLOBH (kWh/m²) | PVGIS GLOBH (kWh/m²) |
|---|---|---|---|
| Enero | 64,7 | 62,9 | 53,5 |
| Junio | 227,0 | 212,7 | 202,1 |
| Julio | 242,4 | 223,2 | 245,5 |
| Diciembre | 58,1 | 52,7 | 55,3 |
| **Anual (suma)** | ~1734,6 | ~1608,7 | ~1595,7 (aprox.) |

Meteonorm 8.2 ofrece un valor de irradiación global ~7,6 % superior al resto (mayor resolución espacial 2-3 km, actualización más reciente, enfoque mixto medición+modelado). **Se selecciona Meteonorm 8.2** como base de datos principal por su precisión en entornos europeos y compatibilidad directa con PVsyst.

### 3. Descripción de la instalación

**3.1-3.2 Características generales y sombreado/orientación:**
- Azimut de módulos: **33° respecto al sur (orientación sureste)**, siguiendo la alineación estructural del edificio (no óptimo pero pérdidas mínimas según PVSyst).
- Separación entre filas: **3,5 m** (evita sombreado y sirve de pasillo técnico).
- Inclinación: **15°** (compatible con cubierta plana, favorece autolimpieza y evacuación de agua).
- Bloques de módulos <400 m² de superficie continua, separados por pasillos de 3,5 m, por exigencia del RSCIEI (compartimentación frente a incendio).

**3.3 Evaluación de propuestas y solución final**

Metodología comparativa: **24 variantes** combinando número de módulos/inversores (desde 616 hasta 4.928 módulos, 1 a 8 inversores) × 3 capacidades de batería (200 / 2.000 / 4.500 kWh), organizadas en 3 bloques (A/B/C). Equipos: módulos JA Solar JAM72D30-550-MB (550 Wp), inversores Huawei SUN2000-330KTL-H1, baterías Huawei LUNA2000. Cadenas de 22 módulos en serie (923,12 V en MPP, dentro del rango 500-1.500 V del inversor). Ratio DC/AC = 1,13 (28 cadenas × 22 módulos = 616 módulos/inversor).

Parámetros técnicos evaluados: potencia pico, energía anual generada, fracción solar autoconsumida, PR, pérdidas energéticas, participación de la batería en el autoconsumo, autosuficiencia, cobertura de demanda.

Indicadores económicos evaluados: CAPEX, ahorro anual, payback simple, TIR, VAN (tasa de descuento 4 %, vida útil 20-25 años según apartado), LCOE.

**Hipótesis de pérdidas del sistema (aplicadas en PVsyst para todas las propuestas):**
- Pérdidas ópticas (suciedad): 3 %
- Desajuste entre módulos: 2 %
- Pérdidas por cableado CC / CA: 1,5 % / 1 %
- Degradación media de módulos: 0,4 %/año
- Disponibilidad del sistema: 2 % (7,3 días/año)

**Hipótesis del sistema de almacenamiento (AC-coupling):**
- Profundidad máxima de descarga: 90 %
- Eficiencia de carga-descarga: 95 %
- Estrategia: autoconsumo optimizado sin vertido, prioriza carga en horas solares y descarga cuando demanda > generación.

**Tabla 5 — Resultados de simulación de las 24 propuestas (selección de filas relevantes):**

| Nº propuesta | Módulos | Batería (kWh) | Consumo desde red (MWh) | Autoconsumo (MWh) | PR | Energía perdida | Red/autoconsumo (%) | Batería directo (%) |
|---|---|---|---|---|---|---|---|---|
| 1 | 4.928 (8 inv, 200 kWh) | 200 | 1.386,0 | 3.335,8 | 53,80 % | 46,20 % | 64,8 % | 10,00 % |
| 9 | 4.928 (8 inv, 2000 kWh) | 2.000 | 1.088,0 | 3.633,8 | 60,70 % | 39,30 % | 70,6 % | 2,60 % |
| 17 | 4.928 (8 inv, 4500 kWh) | 4.500 | 951,7 | 3.770,1 | 63,10 % | 36,90 % | 73,3 % | 0,00 % |
| 8 | 616 (1 inv, 200 kWh) | 200 | 4.248,1 | 473,7 | 33,40 % | 66,60 % | 73,6 % | 0,00 % |
| 24 | 616 (1 inv, 4500 kWh) | 4.500 | 4.150,6 | 571,2 | 33,40 % | 66,60 % | 88,8 % | 0,00 % |

(Tabla completa de las 24 propuestas disponible en la fuente original, tabla 5, p. 37.)

**Costes unitarios usados en el análisis preliminar (Tabla 6, p. 39):**

| Elemento | Referencia | Coste estimado |
|---|---|---|
| Módulo FV | JAM72D30-550-MB | 121 €/unidad (0,22 €/Wp) |
| Inversor | Huawei SUN2000-330KTL-H1 | 25.000 €/unidad |
| Batería | Huawei LUNA2000 | 250 €/kWh instalado |
| Estructura soporte | Variable | 20 €/panel |
| Centro de transformación | 800V/20kV con celdas MT | 120.000 € |
| Protecciones/cableado/auxiliares | Variable | 4 €/kWp instalado |
| Mano de obra | Variable | 100 €/kWp instalado |

**Tabla 9 — Comparación económica de las 3 propuestas finalistas (mismo campo FV 2.710 kWp, 4.928 módulos, 8 inversores; solo cambia batería):**

| Propuesta | Batería (kWh) | Inversión (€) | Ahorro anual (€) | VAN (€) | Payback (años) | LCOE (€/kWh) |
|---|---|---|---|---|---|---|
| 1 | 200 | 1.588.528 | 397.502 | >8.300.000¹ | 4,10 | 0,0370 |
| 9 | 2.000 | 2.398.528 | 435.542 | 3.702.453 | 5,51 | 0,0514 |
| 17 | 4.500 | 3.523.528 | 453.134 | 2.663.264 | 7,78 | 0,0726 |

¹ VAN estimado sobre 30 años según hoja de cálculo del proyecto (nota original).

**3.3.6 Estudio de degradación del sistema de almacenamiento** (aportación diferencial de este TFM — método propio de estimación de ciclos):

Vida útil garantizada: 6.000 ciclos (a profundidad de descarga 80%) para los 3 modelos de batería. Se aplica la ecuación de degradación por ciclos:

$$\text{Ciclos}_t = \text{Ciclos}_{t-1} \cdot (1+\delta)^{t-1}$$

Donde $\delta$ = incremento relativo anual del ciclado por degradación anterior, estimado en **3 %/año**.

Estado de uso tras el primer año (extraído de PVsyst):

| Capacidad batería | Estado de uso tras 1er año | Ciclos equivalentes perdidos (año 1) |
|---|---|---|
| 200 kWh | 0,9532 | 280,8 ciclos |
| 2.000 kWh | 0,9937 | 37,80 ciclos |
| 4.500 kWh | 0,9975 | 0,60 ciclos |

Proyección de degradación acumulada (tablas 12-14):

- **Batería 200 kWh**: alcanza el 100,15 % de degradación (fin de vida útil, ≈6.000 ciclos) en el **año 16**. Requiere reposición: +90.000 € de inversión adicional, elevando el CAPEX ajustado a 1.678.528 €.
- **Batería 2.000 kWh**: en el año 30 solo alcanza 30,59 % de degradación acumulada — no requiere reposición en la vida útil del proyecto.
- **Batería 4.500 kWh**: en el año 30 solo 11,70 % de degradación — muy infrautilizada, sobredimensionada.

**3.3.7 Selección de propuesta final:** batería de **2.000 kWh** por ofrecer rentabilidad elevada y bien distribuida, equilibrio inversión/ahorro, durabilidad completa sin reemplazos, y uso eficiente del almacenamiento sin sobredimensionar.

**3.4 Potencia prevista:** 2.710 kWp DC (4.928 módulos JA Solar 550 Wp), 2.640 kWp AC nominal (8 inversores Huawei 330 kW), ratio DC:AC ≈ 1,03 (nota: el texto usa dos valores de ratio DC/AC en distintos puntos, 1,13 en el diseño de strings del apartado 3.3.2 y ≈1,03 aquí — probablemente por distinta base de cálculo, dato a verificar si se usa como referencia). Producción anual estimada >3.600 MWh, autoconsumo >75 %.

**3.5 Punto de conexión y medida:**
- Modalidad: **autoconsumo individual sin excedentes**, tipología CNMC **31 (subtipo 31-A)**, mismo titular generación/consumo, sin figura de productor independiente.
- Esquema de medida **tipo A**: contador bidireccional único en el punto frontera (acometida MT), sin segundo contador de generación.
- Dispositivo antivertido certificado (exigencia ITC-BT-40), mide en cuadro general y recorta producción FV si se detecta exceso sobre demanda instantánea, garantizando exportación ≤ 0.
- Caja de Protección y Medida: PNZ-CPM-TDT-CES (ref. 313168, Industrias Eléctricas Pinazo), interruptor de corte en carga 4×80 A, bornas 16 mm², bases BUC-00 hasta 160 A.
- **Arquitectura AC-coupling**: la planta FV y el sistema de baterías tienen **centros de transformación independientes** (800 V/20 kV cada uno), ambos conectados al mismo anillo de MT. Ventajas: modularidad, compatibilidad con inversores estándar (no híbridos), seguridad eléctrica (circuitos separados), facilidad de control/medida independiente, robustez ante fallos (redundancia entre subsistemas).
- Batería Huawei LUNA2000-2.0MWh-2H1 (DC) conectada a **10 inversores PCS Huawei LUNA2000-213KTL-H0** que convierten a AC trifásica 800 V.
- Equipamiento de medida en MT: transformadores de intensidad (TI) y tensión (TU), contador bidireccional fiscal clase 0,5s o mejor (tipo 3-4 según RUPM).
- Compatibilidad con SAIs y grupos electrógenos de emergencia existentes sin alterar el esquema de medida (operan aislados de red).

**3.6 Líneas distribuidoras:** canaletas estancas pisables serie WT (BASOR), IP66, libres de halógenos, sin perforar la impermeabilización de cubierta. Distribución BT (AC) con conductores RZ1-K(AS+) 240 mm².

**3.8 Puesta a tierra:** sistema tipo **TT**. Conductores de protección de 150 mm² (RZ1-K AS+), red mallada de picas de cobre. Resistencia de tierra objetivo: **<10 Ω** en condiciones normales de humedad.

### 4. Monitorización

Sistema **Huawei FusionSolar Smart PV Management**: visualización en tiempo real (producción, inversores, batería SOC, consumo), registro histórico en nube, gestión de alarmas, control del antivertido, informes automáticos, acceso multiusuario web/app. Compatibilidad Modbus TCP/RTU con SCADA externo. Herramienta **Smart I-V Curve Diagnosis**: escaneo de cadenas en <1s por string, 128 puntos de muestreo por curva I-V, certificación TUV; permite diagnosticar 5 MW de planta en 15 min.

### 5. Análisis energético (resultados de la propuesta final seleccionada — batería 2.000 kWh)

- **Energía anual generada:** 4.150,8 MWh/año
- **Energía autoconsumida:** 3.633,8 MWh/año
- **Producción específica:** 1.341 kWh/kWp/año
- **Performance Ratio (PR):** 70,61 %
- **Fracción solar (SF):** 76,96 %
- **Energía almacenada en batería (acumulado anual):** ≈93.955 kWh (capacidad útil operada)
- **Energía solar no utilizada** (batería llena, sin inyección posible): 98,5 MWh/año

**Justificación del PR relativamente bajo (70,61 %)** — análisis cualitativo del propio TFM, útil como referencia de factores a considerar en el TFM de Mario para un sistema con alta penetración de almacenamiento:
- Pérdidas de proceso de almacenamiento >9 % (más del 60 % de la energía generada pasa por batería: carga, descarga, conversión, gestión térmica).
- Conversiones adicionales por arquitectura AC-coupling con PCS dedicados.
- Pérdidas térmicas/irradiancia (orientación no óptima, sombreados de lucernarios, separación entre filas).
- Consumo auxiliar permanente (monitorización, ventilación, protección) ≈2 %.
- Recortes de potencia por control antivertido (<3 %).

- **Autosuficiencia:** 3.633,8 / 4.721,8 = **77 %** de la demanda anual cubierta por FV (directo + batería).
- **Porcentaje de autoconsumo** (sobre generación, no sobre demanda): 3.633,8 / 4.150,8 = **87,5 %**.

**Tabla 17 — Simulación temporal de degradación de producción** (degradación inicial 2 % año 1, luego lineal 0,4 %/año según ficha JA Solar):

| Año | Producción estimada (MWh) | Reducción acumulada |
|---|---|---|
| 1 | 4.150,8 | 0,00 % |
| 5 | 3.993,1 | -3,80 % |
| 10 | 3.898,6 | -6,05 % |
| 15 | 3.804,2 | -8,30 % |
| 20 | 3.709,8 | -10,55 % |
| 25 | 3.615,4 | -12,80 % |

Se recomienda plan de repotenciación o sustitución parcial en torno al año 25.

### 6. Análisis económico

**Listado de materiales** (Tabla 18, extraído de planos EPLAN, 8 estaciones de inversores): incluye fusibles/portafusibles ABB, cajas moldeadas, interruptores magnetotérmicos y diferenciales (ABB, Siemens), seccionadores en carga, descargadores de sobretensión CC 1000 V, envolventes Schneider (NSYSF2016602DP), bornas Weidmuller, cable de potencia AC RZ1-K(AS+) 240 mm² (20.000 m), cable de tierra 150 mm² (3.200 m), 4.928 módulos JA Solar, estación prefabricada MT INGETEAM 2550 FSK B (sin inversores).

**Presupuesto detallado (Tablas 19-21):**

| Categoría | Importe (€) |
|---|---|
| Módulos fotovoltaicos JA Solar | 407.000 |
| Inversores Huawei (8×300 kW) | 160.000 |
| Batería Huawei LUNA2000 – 2.000 kWh | 800.000 |
| Estación MT (Ingeteam FSK B, sin inversores) | 120.000 |
| Cableado de potencia y tierra | 100.000 |
| Materiales eléctricos (según planos) | 160.000 |
| Sistema de monitorización y protección | 45.000 |
| Estructura y soporte | 270.000 |
| **Subtotal materiales** | **2.062.000** |
| Ingeniería, simulaciones, memoria técnica | 60.000 |
| Tramitaciones y legalización | 30.000 |
| Supervisión técnica y gestión de proyecto | 40.000 |
| **Subtotal ingeniería** | **130.000** |
| Instalación eléctrica y montaje | 180.000 |
| **Subtotal mano de obra** | **180.000** |
| **TOTAL PRESUPUESTO** | **2.372.000** |

Nota: el presupuesto detallado (2.372.000 €) resulta muy próximo al preliminar estimado con costes unitarios de la tabla 6 (2.398.528 € para la propuesta 9) — el propio TFM señala esta coherencia como validación cruzada del método.

**6.3 Conclusiones económicas — hipótesis y resultados finales:**

Hipótesis:
- Inversión total: 2.372.000 €
- Producción eléctrica anual: 4.150.800 kWh
- Ahorro económico anual: 498.096 € (energía autoconsumida × 0,12 €/kWh precio medio electricidad)
- Vida útil del sistema: 25 años, con repotenciación de módulos prevista en el año 25
- Tasa de descuento: 4 %
- O&M: constante, incluido en el ahorro neto estimado
- Financiación: 100 % fondos propios (simplificación; el TFM señala que un esquema mixto con financiación bancaria o PPA alteraría VAN/TIR)

**Ecuaciones utilizadas** (definiciones y expresiones matemáticas, pp. 8-12 del original, todas preservadas):

Fracción solar autoconsumida:
$$F_{autoconsumo} = \frac{E_{directo}}{E_{gen}} \cdot 100$$

Potencia pico instalada:
$$P_{pico} = N_{modulos} \cdot P_{pico/modulo}$$

Performance Ratio:
$$PR = \frac{E_{AC}}{G_{REF} \cdot P_{pico}}$$

Coste Nivelado de la Energía (LCOE):
$$LCOE = \frac{\sum_{t=1}^{N} \frac{C_t}{(1+r)^t}}{\sum_{t=1}^{N} \frac{E_t}{(1+r)^t}}$$

Valor Actual Neto (VAN):
$$VAN = \sum_{t=1}^{N} \frac{(Ahorro_t - OPEX_t)}{(1+r)^t} - CAPEX$$

Tasa Interna de Retorno (TIR): valor de $r$ que anula el VAN:
$$\sum_{t=1}^{N} \frac{(Ahorro_t - OPEX_t)}{(1+r)^t} = CAPEX$$

Ahorro económico anual:
$$AHORRO_{anual} = E_{autoconsumida} \cdot P_{compra}$$

ROI / payback simple:
$$ROI = \frac{1}{\frac{AHORRO_{anual} - OPEX}{CAPEX}}$$

Participación de la batería en el autoconsumo:
$$\%bateria = \frac{E_{bateria}}{E_{AC}} \cdot 100$$

Autosuficiencia:
$$Autosuficiencia = \frac{E_{AC}}{E_{demanda}} \cdot 100$$

Porcentaje de autoconsumo (sobre generación):
$$Autoconsumo(\%) = \frac{E_{AC} + E_{bateria}}{E_{generada}} \cdot 100$$

Degradación de almacenamiento por ciclos (aportación propia del autor):
$$Ciclos_t = Ciclos_{t-1} \cdot (1+\delta)^{t-1}$$

**Resultados económicos finales (Tabla 22):**

| Parámetro | Valor |
|---|---|
| VAN | 4.481.881,96 € |
| Payback | 5,75 años |
| LCOE | 0,0393 €/kWh |
| TIR (mencionado en conclusiones, no en tabla 22) | 15,76 % |

### 7. Mantenimiento y garantías

**Modalidad:** contrato de O&M externalizado con empresa especializada.

**Mantenimiento preventivo:** inspección visual periódica, limpieza de módulos, verificación de protecciones, comprobación de puesta a tierra, revisión de conexiones, pruebas funcionales de inversores/baterías/monitorización.

**Periodicidad recomendada (Tabla 23):**

| Tarea | Frecuencia |
|---|---|
| Inspección visual general | Trimestral |
| Limpieza de módulos | 2-3 veces/año |
| Revisión de protecciones | Semestral |
| Medición de tierra y continuidad | Anual |
| Termografía e informe completo | Anual |
| Mantenimiento batería Huawei | Según fabricante |

**Garantías (Tabla 24):**

| Elemento | Fabricante | Garantía estándar |
|---|---|---|
| Módulos JA Solar JAM72D30-550 | JA Solar | 12 años producto / 25 años rendimiento (≥84,8 %) |
| Inversores Huawei SUN2000-330KTL | Huawei | 5 años (ampliable a 10-20) |
| Batería Huawei LUNA2000-2.0MWh | Huawei | 10 años o 6.000 ciclos |
| Estación MT (FSK B) | Ingeteam | 2 años estándar, ampliable |
| Sistema de monitorización | Huawei | Incluido con inversores |

Garantía de instalación/montaje: mínimo 1 año del instalador. Se recomienda seguro de responsabilidad civil y seguro de montaje.

### 8. Conclusiones (del TFM original)

Confirma viabilidad técnica y económica de la instalación de 2,71 MWp + 2.000 kWh batería. Propone como líneas futuras: estudio de configuración con excedentes, modelos de explotación PPA/leasing operativo, nuevas tecnologías de almacenamiento, y estudio mecánico/estructural de la cubierta (señalado explícitamente como **fase pendiente e indispensable** para ejecución real, no resuelta en este TFM).

### Anexo II — Fichas técnicas (extracto de valores numéricos relevantes)

**Batería Huawei LUNA2000-2.0MWH (container):**

| Parámetro | 1H0 | 1H1 | 2H1 |
|---|---|---|---|
| Tensión DC nominal | 1.200 V | 1.250 V | 1.250 V |
| Tensión DC máx. | 1.500 V | 1.500 V | 1.500 V |
| Capacidad de energía nominal | 2.064 kWh | 2.032 kWh | 2.032 kWh |
| Tasa de carga/descarga | ≤1 C | ≤1 C | ≤0,5 C |
| Potencia nominal | 2.064 kW | 2.032 kW | 1.016 kW |
| Dimensiones (An×Al×P) | 6.058×2.896×2.438 mm (los 3 modelos) | | |
| Peso del contenedor | ≤30 t | | |
| Rango temperatura operación | -30°C ~ 55°C | | |
| Agente extinción | FM-200 | FM-200/Novec 1230 | FM-200/Novec 1230 |
| Grado de protección | IP55 | | |
| Comunicación | Ethernet/SFP, Modbus TCP/IEC 104 | | |

**Inversor Huawei SUN2000-330KTL-H1:**

| Parámetro | Valor |
|---|---|
| Eficiencia máxima | ≥99,0 % |
| Eficiencia europea | ≥98,8 % |
| Tensión DC máx. entrada | 1.500 V |
| Número de MPPT | 6 |
| Corriente máx. por MPPT | 65 A |
| Corriente cortocircuito máx. por MPPT | 115 A |
| Entradas PV por MPPT | 4/5/5/4/5/5 |
| Tensión de arranque | 550 V |
| Rango tensión MPPT | 500-1.500 V |
| Tensión nominal de entrada | 1.080 V |
| Potencia activa nominal AC | 300.000 W |
| Potencia aparente máx. AC | 330.000 VA |
| Tensión de salida nominal | 800 V, 3W+PE |
| Corriente nominal de salida | 216,6 A |
| Corriente máx. de salida | 238,2 A |
| THDi | <1 % (nominal) |
| Dimensiones | 1.048×732×395 mm |
| Peso (con placa de montaje) | ≤112 kg |
| Rango temperatura operación | -25°C ~ 60°C |
| Grado de protección | IP66 |
| Topología | Sin transformador (transformerless) |

**PCS de batería Huawei LUNA2000-213KTL-H0 (10 unidades para el sistema de 2.000 kWh):**

| Parámetro | Valor |
|---|---|
| Eficiencia máxima | 99,01 % |
| Tensión DC nominal | 1.331 V |
| Tensión DC máx. | 1.500 V |
| Rango tensión DC operación | 800-1.500 V |
| Corriente DC máx. | 218,5 A |
| Potencia activa nominal AC | 213.000 W @40°C / 192.000 W @50°C |
| Potencia aparente máx. | 236.400 VA |
| Tensión AC nominal | 800 V |
| Corriente AC máx. | 170,6 A |
| THDi máx. | ≤1,5 % (nominal) |
| Dimensiones | 875×865×365 mm |
| Peso | ≤110 kg |

**Módulo JA Solar JAM72D30-550-MB:** Vmp = 41,96 V, Imp = 13,11 A por módulo (a partir de las fichas de cálculo eléctrico del Anexo IV; no se localizó en el material extraído la tabla completa de datasheet con Voc/Isc/coeficientes de temperatura — **dato no especificado en la fuente extraída**, verificar directamente si se necesita).

**Estación Ingeteam InverterStation FSK B Series:** solución de MT hasta 5,1 MVA, transformador MT integrado (hasta 36 kV), densidad de potencia 317 kW/m³, sin necesidad de envolvente (outdoor), preensamblada en skid.

### Anexo III — Informe de simulación PVsyst (propuesta final: 4.928 módulos / 2.000 kWh / 8 inversores)

**Parámetros generales de simulación:**
- Sitio: El Encín, España (lat. 40,51°N, long. -3,32°O, alt. 597 m, UTC+1)
- Albedo: 0,20
- Datos meteo: Meteonorm 8.2 (2005-2019), Sat=28%, sintético
- Orientación: plano fijo, inclinación 15°/azimut -33°
- Configuración cobertizos: 187 unidades, espaciado 2,75 m, ancho de sensor 1,13 m
- Transposición: Perez; difuso: Perez, Meteonorm; horizonte: altura promedio 2,6°
- Estrategia de almacenamiento: autoconsumo, sin reinyección de red; carga cuando hay exceso de potencia solar, descarga tan pronto como se necesite potencia
- Paquete de baterías: 56 unidades, 1.267 V, 92.680 Ah
- Simulación para el año nº 10 (incluye degradación acumulada)

**Balances y resultados mensuales principales** (Tabla del informe PVsyst, p. 9/12):

| Mes | GlobHor (kWh/m²) | GlobInc (kWh/m²) | EArray (MWh) | E_User consumo (MWh) | E_Solar autoconsumo (MWh) | EUnused (MWh) | EFrGrid desde red (MWh) |
|---|---|---|---|---|---|---|---|
| Enero | 63,8 | 84,2 | 191,0 | 335,2 | 211,7 | 0,00 | 123,6 |
| Febrero | 84,4 | 102,4 | 235,5 | 321,3 | 206,8 | 0,00 | 114,6 |
| Marzo | 135,7 | 153,5 | 345,2 | 405,3 | 313,6 | 0,00 | 91,7 |
| Abril | 168,6 | 180,6 | 400,9 | 405,7 | 330,4 | 0,00 | 75,3 |
| Mayo | 207,9 | 212,5 | 464,0 | 440,9 | 423,4 | 0,00 | 17,5 |
| Junio | 226,1 | 226,4 | 482,5 | 412,0 | 396,6 | 0,00 | 15,3 |
| Julio | 242,0 | 243,6 | 511,8 | 366,6 | 366,6 | 62,74 | 0,0 |
| Agosto | 212,8 | 224,2 | 474,6 | 366,8 | 366,8 | 33,28 | 0,0 |
| Septiembre | 158,5 | 176,0 | 380,7 | 407,1 | 407,1 | 2,50 | 0,0 |
| Octubre | 109,8 | 130,1 | 289,8 | 457,7 | 285,2 | 0,00 | 172,4 |
| Noviembre | 68,8 | 87,3 | 198,1 | 405,3 | 170,0 | 0,00 | 235,3 |
| Diciembre | 57,3 | 77,7 | 176,7 | 397,9 | 155,6 | 0,00 | 242,3 |
| **Año** | **1.735,9** | **1.898,6** | **4.150,8** | **4.721,8** | **3.633,8** | **98,52** | **1.088,0** |

Nota: EUnused (energía no utilizada por batería llena) se concentra en verano (jul-sep), cuando la generación supera ampliamente el consumo (menor demanda relativa) — patrón relevante para dimensionar la relación batería/campo FV en instalaciones de perfil de consumo estable.

**Diagrama completo de pérdidas PVsyst (cascada, de irradiación horizontal a energía útil al usuario):**

```
Irradiación horizontal global                              1.736 kWh/m²
  +9,4%  Global incidente plano receptor
  -0,5%  Sombreados lejanos / Horizonte
  -1,0%  Sombreados cercanos: pérdida de irradiancia
  -3,0%  Factor de pérdida de suciedad
  -2,0%  Factor IAM en global
Irradiancia efectiva en colectores                          1.779 kWh/m²  (* 12.730 m² colectores)
  eficiencia en STC = 21,31%                                Conversión FV
Conjunto de energía nominal (con efic. STC)                 4.825,8 MWh
  -3,8%  Pérdida de degradación módulos (por año #10)
  -1,1%  Pérdida FV debido al nivel de irradiancia
  -3,8%  Pérdida FV debido a la temperatura
  -0,3%  Corrección espectral
  +0,8%  Pérdida calidad de módulo
  -2,0%  LID - Degradación inducida por luz
  -3,6%  Pérdidas de desajuste, módulos y cadenas (incl. 1,5% dispersión por degradación)
  -1,0%  Pérdida óhmica del cableado
Energía virtual del conjunto en MPP                          4.150,8 MWh
  -1,6%  Pérdida del inversor durante la operación (eficiencia)
   0,0%  Pérdida del inversor sobre potencia nominal / corriente máx. / voltaje nominal / umbral potencia / umbral voltaje
Energía disponible en la salida del inversor                 4.083,2 MWh
   0,0%  Auxiliares (ventiladores, otros)
  -2,2%  Indisponibilidad del sistema
  -2,7%  Batería IN, pérdida de cargador
  +1,2%  Balance de energía almacenada en la batería
    Almacenamiento de batería: Almacenado 60,7% / Uso directo 39,3%
  -2,9%  Pérdida global de la batería (4,9% de la contribución de la batería)
  -2,3%  Batería OUT, pérdida del inversor
  -2,6%  Energía no utilizada (batería llena, sin inyección de red)
Usuario: desde solar y desde red                              3.633,8 MWh
```

Este diagrama es directamente equiparable en formato al que Mario deberá generar en PVsyst para el CPD (capítulo 6.4 del índice propuesto), y sirve de referencia de la magnitud típica de pérdidas por almacenamiento en arquitectura AC-coupling (aquí, la cadena completa de pérdidas de batería —cargador IN, pérdida global batería, inversor OUT— suma en torno a 8 puntos porcentuales sobre la energía que pasa por el sistema de almacenamiento).

**Ficha de generador FV (Conjunto/Subconjunto):**
- Módulo: Generic JAM72-D30-550-MB (BD PVsyst), 550 Wp nominal
- Inversor: Generic SUN2000-330KTL-H1 (BD PVsyst), 300 kWca nominal
- Cada subconjunto: 704 módulos (32 cadenas × 22 en serie), 387 kWp nominal, 8 inversores a MPPT 14% con proporción 1,1
- En condiciones de funcionamiento (50°C): Pmpp 355 kWp, Umpp 837 V, Impp 425 A
- Rango de voltaje de funcionamiento: 550-1.500 V

### Anexo I y Anexo IV (contenido verificado, no extraído en detalle)

- **Anexo I (Planos eléctricos, EPLAN):** portada con datos de proyecto — cliente **Amazon Spain Services S.L.**, ingeniería **Diferal Engineering**, dirección Carr. Nacional II km 20, Comunidad de Madrid, esquema de puesta a tierra TT/(3F+PE), cubierta plana, 4.928 módulos, 8×300 kW inversores, 2.000 kWh batería. Contiene esquemas unifilares de FV y almacenamiento, cuadros de protección por inversor, balance de potencia y nomenclatura de cables — formato gráfico CAD, sin extraer en detalle.
- **Anexo IV (Cálculos eléctricos BT, software Caneco BT 5.14):** fichas de cálculo de cortocircuito y caída de tensión por circuito (centro de maniobra MT, INV1-INV8), unifilares de cuadros de protección por inversor, listado de folios y nomenclatura de cables — salida de software repetitiva por circuito, sin extraer en detalle numérico.

## Datos clave (con página de origen)

- Potencia pico instalada: **2.710 kWp** / 4.928 módulos JA Solar 550 Wp (p. 51, p. 5 resumen)
- Inversores: **8× Huawei SUN2000-330KTL-H1** (330 kW), potencia AC total 2.400-2.640 kW según sección, ratio DC/AC 1,03-1,13 (p. 51-52, verificar discrepancia)
- Batería seleccionada: **2.000 kWh Huawei LUNA2000** (p. 50-51)
- Superficie disponible de cubierta: **46.550 m²** (p. 19)
- Consumo anual del centro: **4.721,8 MWh/año**, pico 1.318 kW (p. 22)
- Producción anual estimada (propuesta final): **4.150,8 MWh/año** (p. 68)
- Autoconsumo (sobre generación): **87,5 %** (p. 70)
- Autosuficiencia (sobre demanda): **77 %** (p. 69)
- Performance Ratio: **70,61 %** (p. 68)
- CAPEX final: **2.372.000 €** (p. 74-75)
- Ahorro anual: **498.096 €** (p. 75)
- Payback: **5,75 años**; VAN: **4.481.881,96 €**; TIR: **15,76 %**; LCOE: **0,0393 €/kWh** (p. 76, p. 82)
- Batería 200 kWh alcanza fin de vida útil (6.000 ciclos) en el **año 16**, requiere reposición de +90.000 € (p. 46-50)
- Batería 2.000 kWh: solo 30,59 % de degradación acumulada en 30 años, sin necesidad de reposición (p. 48)
- Degradación de módulos: 2 % pérdida inicial año 1 + 0,4 %/año lineal después (ficha JA Solar) (p. 70)
- Delta de degradación de ciclos de batería aplicado: 3 %/año (p. 46-47, ecuación propia del autor)
- Precio de electricidad asumido para el ahorro: 0,12 €/kWh (p. 39, p. 75)
- Resistencia de puesta a tierra objetivo: <10 Ω (p. 62)
- Autoconsumo tipología CNMC: **31-A** (individual, sin excedentes, mismo titular) (p. 52)
- Diagrama de pérdidas PVsyst completo (irradiación 1.736 kWh/m² → 3.633,8 MWh al usuario), con desglose de pérdidas de batería ≈8 puntos porcentuales acumulados (Anexo III, p. 9/12 del informe PVsyst)

## Relevancia para el TFM

- **Capítulos del índice a los que aporta** (ver `Memoria/indice_propuesto.md`):
  - Cap. 3 (emplazamiento y consumo): metodología de comparación de bases de datos meteorológicas (Meteonorm/NASA/PVGIS) directamente replicable.
  - Cap. 4 (tipología de autoconsumo y tramitación): ejemplo completo de codificación CNMC 31-A, esquema de medida tipo A, y justificación normativa para instalación sin excedentes en media tensión — muy alineado con lo que necesitará el CPD de Mario si opta por MT.
  - Cap. 6 (diseño e ingeniería FV): metodología de comparación de 24 variantes (módulos/inversores × capacidad batería), diagrama de pérdidas PVsyst completo con desglose de pérdidas por almacenamiento AC-coupling, cálculo de ratio DC/AC y configuración de strings/MPPT.
  - Cap. 7 (diseño del sistema de almacenamiento — núcleo del TFM de Mario): **aportación más valiosa de este documento**. Metodología original de estimación de degradación de baterías por ciclos equivalentes con tasa de incremento anual (ecuación propia del autor), y criterio de selección de capacidad de batería basado en durabilidad/reposición, no solo en rentabilidad estática. Directamente aplicable al capítulo 7.4 (modelo horario y degradación) del índice de Mario.
  - Cap. 8 (análisis económico): estructura completa de presupuesto (materiales/ingeniería/mano de obra), hipótesis de VAN/TIR/LCOE con sus ecuaciones, y validación cruzada entre presupuesto preliminar (costes unitarios) y detallado (a partir de planos).
  - Anexos A-C: modelo de organización de anexos (planos, fichas técnicas, informe PVsyst) equivalente al esquema previsto por Mario.

- **Qué aporta exactamente:** referencia de la magnitud esperable de resultados (PR, LCOE, payback, VAN) para una instalación industrial de gran escala con almacenamiento significativo en AC-coupling, con el mismo tutor y bajo la misma normativa ERMA. Es el TFM de referencia más reciente y más cercano en escala/arquitectura al de Mario (aunque el consumo del CPD será previsiblemente más plano y crítico 24/7 que el de un centro logístico, y la escala de potencia puede diferir). Su capítulo de degradación de almacenamiento por ciclos es un modelo de cálculo transferible casi directamente.
- **Confianza en los datos:** todas las cifras citadas arriba están verificadas contra el texto extraído de las páginas 1-85 (memoria completa) y del informe PVsyst del Anexo III (páginas 142-154). Los Anexos I y IV se han verificado como existentes pero no se ha extraído su detalle numérico exhaustivo (ver nota de muestreo). Una discrepancia menor detectada: el ratio DC/AC se cita como 1,13 en el apartado 3.3.2 (diseño de strings) y como ≈1,03 en el apartado 3.4 (potencia prevista) — no se ha podido resolver esta discrepancia con el texto disponible; si se usa como dato comparativo, verificar directamente en la fuente original antes de citar.

## Notas de procesamiento

- Documento de 225 páginas en total. Memoria principal (pp. 1-85) leída y extraída íntegramente mediante extracción de texto de PDF (pypdf), sin OCR adicional necesario (el texto era nativo, no escaneado).
- Anexo II (fichas técnicas, pp. 124-141) y Anexo III (informe PVsyst, pp. 142-154) extraídos con el detalle numérico relevante para el análisis técnico.
- Anexo I (planos eléctricos EPLAN, pp. 87-123) y Anexo IV (cálculos eléctricos BT, salida Caneco BT, pp. 155-225) verificados como presentes y descrito su contenido general, pero **no extraídos en detalle numérico exhaustivo** por ser salidas de software repetitivas por circuito de bajo valor narrativo para un resumen — si se necesita algún dato específico de estos anexos (p. ej. una sección de cable concreta o cálculo de cortocircuito de un circuito determinado), debe consultarse directamente el PDF original.
- Varias ilustraciones/gráficas del documento original (vistas aéreas, esquemas unifilares, gráficos de flujo de caja, curvas de estado de batería) son imágenes; se han descrito sus datos numéricos subyacentes cuando estaban disponibles en tablas asociadas, pero no se ha "leído" el contenido visual de los gráficos en sí.
- No se ha localizado en el texto extraído la ficha técnica completa (Voc, Isc, coeficientes de temperatura) del módulo JA Solar JAM72D30-550-MB; solo se dispone de Vmp/Imp derivados de las fichas de cálculo eléctrico del Anexo IV.
