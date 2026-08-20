---
title: "Evaluación inicial de un proyecto real de implantación de instalación fotovoltaica para autoconsumo en gran industria"
tipo: tfm-referencia
autor: "Andrea Barrios López (tutores: Patricia Aláez, Pablo Corredoira, Julio Amador Guerra)"
anio: 2023
densidad: exhaustivo
fecha_resumen: 2026-08-20
fuente_original: "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Documentacion de apoyo\Ejemplos TFM\TFM_ANDREA_BARRIOS_L.pdf"
tags: [fotovoltaica, autoconsumo, TFM-referencia, gran-industria, analisis-economico, tramitacion, dimensionado-electrico, TIR, VAN, cableado, subvenciones]
related: []
---

# Evaluación inicial de un proyecto real de implantación de instalación fotovoltaica para autoconsumo en gran industria (Andrea Barrios López, 2023)

> **Nota de no-citabilidad:** este documento es un TFM de otra autora (Máster ERMA, curso 2022/2023, UPM), tutorizado en parte por el mismo tutor de Mario (Julio Amador Guerra), junto a Patricia Aláez y Pablo Corredoira. No es fuente académica citable en el TFM de Mario Carrión, pero sirve como referencia de estructura, metodología de cálculo, criterios de tramitación administrativa y nivel de detalle esperado por el tribunal ERMA. El complejo industrial del estudio aparece anonimizado en el propio documento original (ubicación, nudo de conexión y varias imágenes marcadas como "CONFIDENCIAL"), así que ciertos datos de localización concreta no están disponibles ni en la fuente ni en este resumen.

## Resumen

El TFM evalúa la viabilidad técnico-económica de una instalación fotovoltaica de autoconsumo sin excedentes para un complejo industrial de gran consumo (8,73 GWh/año en 2021) situado en un municipio de la Comunidad de Madrid, colindante con el Río Jarama (lo que introduce restricciones de Dominio Público Hidráulico) y cercano al Aeropuerto de Madrid-Barajas (zona de influencia de AESA). Se identifican 8 zonas disponibles (suelo, marquesinas y cubiertas) y se comparan 3 propuestas de ejecución (A: 1.657 kWp sobre suelo; B: 800 kWp mixta suelo+cubiertas; C: 1.504 kWp suelo+marquesinas), evaluadas bajo 3 escenarios de evolución de precios de mercado eléctrico (decreciente, base, incremental) y con/sin subvención del RD 477/2021. La Propuesta A resulta la más viable técnica y económicamente (ratio de autoconsumo 96%, autosuficiencia 30%, TIR entre 13,4% y 40,8% según escenario, payback entre 2,5 y 6 años) y se desarrolla como ingeniería básica: instalación final sobre suelo de 3.024 módulos JinkoSolar JKM530M-7TL4-V (530 Wp, 1,603 MWp) con 14 inversores Fronius TAURO ECO 100 (1,4 MWn), con cálculos completos de dimensionado del generador FV, cableado CC/CA según UNE, y presupuesto de ejecución material de 983.250 € (sin IVA), 1.252.350 € con IVA. El documento descarta explícitamente la hibridación con baterías por ser la energía excedentaria demasiado baja para rentabilizar el almacenamiento, y detalla de forma extensa el procedimiento administrativo de legalización (ayuntamiento, Comunidad de Madrid, CHT, AESA, CAU) con plazos orientativos.

## Contenido técnico

### Estructura del documento (índice original, 96 páginas numeradas + 28 páginas de anexos, 132 páginas de PDF en total)

```
AGRADECIMIENTOS
RESUMEN
I. INTRODUCCIÓN
  1. Introducción (antecedentes, objeto y alcance, normativa de aplicación)
II. ANÁLISIS TÉCNICO-ECONÓMICO
  1. Metodología
  2. Análisis de los consumos energéticos
  3. Análisis del emplazamiento
  4. Evaluación de la generación
  5. Selección de tecnologías y parámetros esenciales
  6. Procedimiento de legalización
  7. Solución de autoconsumo
  8. Propuestas de ejecución (A, B, C)
  9. Evaluación económica
III. INGENIERÍA BÁSICA Y CONCLUSIONES DEL PROYECTO
  1. Descripción de la instalación
  2. Cálculos eléctricos (generador FV, cableado, distribución de inversores)
  3. Mediciones y presupuestos
  4. Planos
  5. Conclusiones y líneas futuras
  6. Planificación temporal
  7. Bibliografía
ÍNDICE DE TABLAS / ÍNDICE DE FIGURAS / ABREVIATURAS, UNIDADES Y DEFINICIONES
IV. ANEXOS
  Anexo I: Cálculo de la subvención
  Anexo II: Flujos de caja
  Anexo III: Fichas técnicas
  Anexo IV: Informe de generación
```

**Nota de muestreo:** documento de 132 páginas de PDF (96 numeradas de memoria + índices + 36 de anexos). Se ha extraído y leído el **100% del texto nativo del PDF** (sin OCR adicional necesario, texto no escaneado en el cuerpo principal) en tramos completos. Los **Anexo III (Fichas técnicas, pp. 103-110) y Anexo IV (Informe de generación, pp. 111-124) son páginas puramente gráficas** (imágenes de fichas de fabricante e informe de simulación, probablemente PVsyst o similar): la extracción de texto de estas páginas devolvió contenido vacío o solo encabezados de página, por lo que su contenido numérico detallado **no ha podido extraerse** y no se reproduce en este resumen — se documenta su existencia y su temática, pero cualquier dato específico de esas fichas/informe debe verificarse directamente en el PDF original. Asimismo, algunas figuras del cuerpo (vistas aéreas, referencia catastral, planos) están marcadas explícitamente como **"CONFIDENCIAL"** en el propio documento original y no incluyen datos de localización.

### I.1 Introducción

**1.1 Antecedentes:** se busca dotar a una nave industrial (ubicación anonimizada, "un municipio de la Comunidad de Madrid") de una instalación fotovoltaica de autoconsumo para cubrir parte de las necesidades eléctricas del punto de suministro. La instalación es del tipo ITC-BT-40 (instalaciones generadoras en baja tensión).

**1.2 Objeto y alcance:** definir las características principales de una instalación de autoconsumo FV conectada a la red de baja tensión. Fase 1: análisis técnico-económico de las diferentes zonas disponibles, evaluación económica y tiempos de puesta en marcha, más el procedimiento de legalización. Fase 2 (tras elegir propuesta): ingeniería de detalle — cálculos eléctricos de cableado CC y CA, presupuesto final de ejecución material, planos, conclusiones, evaluación de impactos y planificación temporal.

**1.3 Normativa de aplicación (listado íntegro, orden cronológico descendente del original):**
RD 377/2022 (ampliación beneficiarios RD 477/2021) · RD-ley 20/2022 (medidas Guerra de Ucrania) · Resolución 15/12/2022 CNMC (peajes de acceso 2023) · RD 477/2021 (ayudas autoconsumo y almacenamiento, PRTR) · RD 1183/2020 (acceso y conexión a redes) · RD-ley 23/2020 (reactivación económica) · RD 244/2019 (condiciones administrativas, técnicas y económicas del autoconsumo) · RD-ley 15/2018 (transición energética) · RD 186/2016 y RD 187/2016 (compatibilidad electromagnética / seguridad material eléctrico) · RD 337/2014 e ITC-RAT 01-23 (alta tensión) · Ley 24/2013 (Sector Eléctrico) · Ley 21/2013 (evaluación ambiental) · RD 1699/2011 (conexión a red de pequeña potencia) · Decreto 70/2010 CAM (simplificación autorizaciones AT) · RD 223/2008 e ITC-LAT 01-09 (líneas AT) · RD 314/2006 (CTE) · RD 842/2002 (REBT) · RD 1955/2000 (transporte/distribución/comercialización) · RD 614/2001 (riesgo eléctrico) · RD 1627/1997 y RD 486/1997 (seguridad y salud en obras/lugares de trabajo) · Ley 31/1995 (Prevención de Riesgos Laborales).

### II.1 Metodología (12 pasos, íntegros)

1. **Análisis de la normativa vigente.**
2. **Recogida de datos de partida**: facturas eléctricas (≥12 meses, tarifa/consumo/potencia contratada/precio desglosado); curva de consumo horaria de 12 meses (o alternativamente periodos tarifarios de mayor consumo); localización y zonas disponibles.
3. **Análisis de los consumos energéticos**: curva horaria construida a partir de facturas más estimaciones de hábitos de consumo más corrección con curvas de demanda tipo de REE. Los consumos aportados son de 2021, actualizados a periodos tarifarios de la tarifa 6.1TD (vigente desde 2023).
4. **Análisis de los precios de la energía actuales**: precio de mercado diario medio de abril 2023 = 74 €/MWh.
5. **Análisis del emplazamiento**: visitas técnicas o herramientas online (Google Maps/Earth); factores: materiales de cubierta, inclinación/orientación, relieve, distancia al cuadro eléctrico, accesibilidad.
6. **Análisis del recurso solar**: base de datos PVGIS para el preanálisis (rápida, diferencia de un 8 por ciento aprox. frente a otras bases, considerada residual para el impacto económico); PVSyst reservado para el proyecto de ingeniería.
7. **Análisis del proceso de tramitación**: variable según ubicación de los equipos.
8. **Definición de la tipología de autoconsumo**: dado un consumo anual mayor de 8.000 MWh, se elige autoconsumo sin vertido de excedentes, por: tiempos de ejecución (permisos de acceso y conexión lentos, aval de 40 euros por kWn si hay vertido); costes asociados (adecuación de infraestructuras de evacuación, unos 0,15 euros por Wp); y análisis coste-beneficio (con autosuficiencia mayor al 10 por ciento casi toda la generación se autoconsume instantáneamente).
9. **Definición de áreas de instalación y dimensionamiento**: criterio de diseño = alcanzar ratio de autoconsumo de alrededor del 95 por ciento, mediante casación horaria de curvas de demanda y generación.
10. **Estimación de ahorros**: 3 escenarios de evolución del mercado eléctrico a 25 años.
11. **Estimación de costes de ejecución**: presupuesto llave en mano, sin tasas ni impuestos.
12. **Ventajas e inconvenientes** de cada propuesta.

Ecuación del término de energía:

$$\text{Término de energía} = \text{Peajes y cargos} + \text{Precio de la energía} \quad [1]$$

### II.2 Análisis de los consumos energéticos

Un único CUPS. Consumo horario de un año natural completo (2021), verificado contra consumos mensuales por periodos del propio CUPS.

**Tabla 3 — Consumos eléctricos mensuales por periodos tarifarios (kWh), 2021:**

| Mes | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|---|---|---|---|---|---|---|
| Ene | 179.080 | 139.142 | 0 | 0 | 0 | 382.919 | 701.141 |
| Feb | 163.380 | 129.475 | 0 | 0 | 0 | 326.662 | 619.517 |
| Mar | 0 | 194.403 | 156.136 | 0 | 0 | 349.150 | 699.689 |
| Abr | 0 | 0 | 0 | 166.634 | 132.081 | 337.134 | 635.849 |
| May | 0 | 0 | 0 | 204.552 | 160.216 | 377.551 | 742.319 |
| Jun | 0 | 0 | 232.392 | 180.760 | 0 | 382.206 | 795.358 |
| Jul | 262.223 | 203.937 | 0 | 0 | 0 | 489.812 | 955.972 |
| Ago | 0 | 0 | 232.759 | 181.012 | 0 | 363.649 | 777.420 |
| Sep | 0 | 0 | 212.840 | 171.777 | 0 | 374.852 | 759.469 |
| Oct | 0 | 0 | 0 | 192.329 | 154.438 | 388.405 | 735.172 |
| Nov | 0 | 182.493 | 140.987 | 0 | 0 | 338.111 | 661.591 |
| Dic | 172.775 | 132.698 | 0 | 0 | 0 | 338.930 | 644.403 |
| **Total** | **777.458** | **982.148** | **975.114** | **1.097.064** | **446.735** | **4.449.381** | **8.727.900** |

**Figura 2** (descrita): gráfico de barras apiladas por periodo (P1-P6), eje X meses, eje Y consumo en kWh. Se observa alto porcentaje de consumo en P6 (fines de semana y horas nocturnas), coherente con operación de la planta 24h/365 días.

**Tabla 2 — Resumen de precios utilizados:**

| Concepto | P1 | P2 | P3 | P4 | P5 | P6 |
|---|---|---|---|---|---|---|
| Peajes y cargos (€/kWh) | 0,018036 | 0,014354 | 0,005965 | 0,004393 | 0,000362 | 0,000362 |
| Precio de la energía (€/kWh) | 0,074 | 0,074 | 0,074 | 0,074 | 0,074 | 0,074 |
| Término de energía (€/kWh) | 0,0920 | 0,0884 | 0,0800 | 0,0784 | 0,0744 | 0,0744 |
| Término de potencia (€/kW día) | 0,052352 | 0,049072 | 0,024453 | 0,019612 | 0,001387 | 0,001387 |
| Potencia contratada (kW) | 1.203 | 1.203 | 1.203 | 1.203 | 1.203 | 1.850 |

**Tabla 4 — Costes eléctricos anuales:**

| Concepto | Importe (€) |
|---|---|
| Término de potencia | 134.479 |
| Término de energía | 715.688 |
| Impuesto eléctrico | 43.466 |
| **Total coste** | **893.633** |

El término de energía representa el 80% del coste total. Adicionalmente, en 2021 se pagaron 27.000 € en excesos de potencia (mayormente en P1 y P2), reducibles con la instalación FV.

### II.3 Análisis del emplazamiento

**3.1 Análisis general e incidencias:** complejo industrial de unas 14,2 ha. Incidencias detectadas:
- Linda al este y sur con el **Río Jarama**: parte del complejo bajo **Dominio Público Hidráulico (DPH)**. Zonificación DPH: álveo/cauce natural, ribera, margen, **zona de policía** (100 m desde la linde, requiere autorización para alteraciones de relieve, extracciones de áridos, construcciones), **zona de servidumbre** (5 m, uso de vigilancia/pesca/salvamento, construcción muy restringida), lecho de lagos, zonas inundables (retorno de 500 años). El río Jarama es afluente del Tajo, competencia de la **Confederación Hidrográfica del Tajo (CHT)**.
- Linda al norte con carretera de paso.
- A 4,5 km de la Terminal T4 de Madrid-Barajas, zona de influencia de la **AESA** (Agencia Estatal de Seguridad Aérea).
- Obras en curso: construcción de edificio anexo al laboratorio y carretera de camiones que cruza el aparcamiento, condicionan el diseño.

**3.2 Análisis de emplazamientos disponibles, Tabla 5 (21 espacios evaluados, aptitud SI o NO):** de 21 espacios catalogados por orientación (óptima=sur, buena=sureste/suroeste), tipo de instalación (cubierta plana, a 2 aguas, marquesina, suelo), obstáculos y sombras (bajo/medio/alto), **8 resultan aptos**: espacios 2, 8, 14, 15, 16, 17, 18, 19 (los descartados lo son por sombras altas, tipo de chapa no adecuado, baja potencia instalable, previsible desuso, cercanía menor de 50 m al río o futura construcción).

**3.3 Zonas seleccionadas, Tabla 6 (superficies, m2):**

| Zona | 1 | 1.1 | 1.2 | 1.3 | 2 | 2.1 | 3 | 4 |
|---|---|---|---|---|---|---|---|---|
| Superficie (m2) | 4.000 | 9.500 | 1.250 | 1.300 | 1.920 | 1.050 | 1.200 | 610 |

- **Zona 1**: suelo, respetando 100 m desde la linde del río; no está bajo DPH.
- **Zona 1.1**: suelo a 50 m de la linde, bajo DPH, requiere informe favorable de la CHT.
- **Zona 1.2 / 1.3**: suelo, respetando 100 m; no bajo DPH.
- **Zona 2**: marquesina de aparcamiento; requiere estudio estructural (acero S-275 JR o similar); correas existentes demasiado delgadas para las cargas FV, necesita refuerzo u obra civil de cimentación, con sobrecoste; se recomienda cambiar estructuras completas.
- **Zona 2.1**: marquesina de nueva construcción.
- **Zona 3**: cubierta plana transitable del edificio principal.
- **Zona 4**: edificio a 2 aguas de chapa, orientación óptima en la vertiente sur.

### II.4 Evaluación de la generación

Base de datos **PVGIS** (rápida, fiabilidad suficiente para preanálisis). **Figura 10** (descrita): radiación normal directa mensual, eje X meses, eje Y kWh/m2; pico en julio (274,38 kWh/m2), valor promedio anual 184,42 kWh/m2.

**Tabla 7 — Pérdidas utilizadas para la simulación:**

| Concepto | Valor |
|---|---|
| Sombras (%) | 2,5 |
| Eficacia módulos (%) | 21,0 |
| Rendimiento inversores (%) | 97,0 |
| Suciedad (%) | 1,0 |
| Degradación año 0 (%) | 0,8 |
| Degradación resto de los años (%) | 0,4 |
| Temperatura (W/m2K) | 20 |

### II.5 Selección de tecnologías y parámetros esenciales

**5.1 Módulos fotovoltaicos:** cerca del 90% del mercado usa silicio; tipologías mono/poli/amorfo y dopaje tipo p/n. Se eligen módulos monocristalinos tipo p (desde 2018 desplazan a la policristalina, cerca del 80% del mercado). Tecnologías del módulo elegido: Multi Busbar (10 busbar por célula, reduce pérdidas resistivas) y célula partida (Half-cell, reduce corriente manteniendo voltaje, reduce efectos de sombreado).

**Tabla 8 — Módulo fotovoltaico (fase de análisis técnico-económico):**

| Marca | Modelo | Potencia (W) | Tecnología | Eficiencia STC (%) |
|---|---|---|---|---|
| JinkoSolar | Tiger Pro JKM540M-72HL4-V0 | 540 | Si-Mono Half Cell | 20,94 |

Elegido por: stock asegurado desde el tercer trimestre de 2023, primera posición TIER 1 en 2023 (ensayos DNVGL), poco incremento de dimensiones respecto a módulos de menor potencia. Otras ventajas: Anti-PID, alto rendimiento con baja luz, alta resistencia mecánica, 12 años garantía de producto, 25 años garantía de producción.

**5.2 Inversores:** tipos según conexión (centrales, de cadena, multicadena); se eligen **multicadena** por las distintas orientaciones e inclinaciones y ubicaciones. Marca Huawei (fabricación en España, buen servicio técnico).

**Tabla 9 — Inversores (fase de análisis técnico-económico):**

| Marca | Modelo | Potencia (kW) | Nº MPPT | Rendimiento (%) |
|---|---|---|---|---|
| Huawei | SUN2000-100KTL-H1 | 100 | 10 | 98,6 |
| Huawei | SUN2000 60KTL M0 | 60 | 2 | 98,7 |

Relación Potencia pico sobre Potencia nominal mantenida entre **1,10 y 1,25** en todas las propuestas.

**5.3 Orientaciones e inclinaciones:** orientación óptima = azimut 0° sur. Orientaciones usadas: azimut -27° (sureste) y azimut 117°/-63° (este-oeste). Inclinación óptima en suelo/cubierta plana en esta ubicación: **37°**. Inclinaciones usadas: 5° (marquesinas, por defecto de fabricante), 10° (coplanar en cubierta), 20° (inclinada en cubierta). Se exige inclinación mínima mayor de 3° sobre la horizontal para favorecer autolimpieza por lluvia.

**5.4 Estructuras:** distinción coplanar/autoportante y fija/móvil (se usa fija en todo el proyecto). Tipos: suelo, estructura fija anclada, disposición 4H (4 módulos en horizontal por fila); cubierta plana, perfiles triangulares de aluminio con lastres de hormigón; cubierta inclinada, perfiles de aluminio anclados; marquesinas, perfiles de aluminio anclados, de nueva construcción.

**5.5 Monitorización:** inversores con protocolo abierto Modbus RTU. Mediciones adicionales recomendadas: radiación incidente, temperatura ambiente, velocidad del viento, temperatura de célula.

**Tabla 10 — Resumen de tecnologías por zonas** (módulo Jinko Mono Tiger PRO JKM540M-72HL4-V en todas las zonas):

| Zona | Nº módulos | Inversor(es) | Nº inversores | Orientación | Inclinación | Estructura |
|---|---|---|---|---|---|---|
| 1 | 707 | Huawei SUN2000 100KTL (x3) más 60KTL (x1) | 4 | SSE | 20° | Anclada |
| 1.1 | 1.931 | Huawei SUN2000-100KTL | 10 | SSE | 20° | Anclada |
| 1.2 | 211 | Huawei SUN2000-100KTL | 1 | SSE | 20° | Anclada |
| 1.3 | 216 | Huawei SUN2000-100KTL | 1 | SSE | 20° | Anclada |
| 2 | 1.080 | Huawei SUN2000 100KTL | 5 | NEE-SOO | +5°/-5° | Marquesina |
| 2.1 | 570 | Huawei SUN2000-100KTL | 2 | NEE-SOO | +5°/-5° | Marquesina |
| 3 | 194 | Huawei SUN2000 60KTL | 1 | SSE | 20° | Lastres |
| 4 | 152 | Huawei SUN2000 100KTL | 1 | SSE | 10° | Coplanar |

### II.6 Procedimiento de legalización

Esquema general para instalación sin excedentes (evita punto de acceso/conexión): tramitación municipal, tramitación en la Comunidad, ejecución material (CFO, certificado OCA, certificado de no vertido), autorización administrativa de explotación, obtención del CAU, inscripción en Registro de Autoconsumo (la solicitud de punto de acceso y conexión NO aplica en este caso).

**6.1 Tramitación municipal:** terreno catastrado como industrial agrario (suelo rústico). Requiere **licencia de obra menor**. Documentación general: proyecto de ingeniería, escrituras de constitución, CIF, escritura de apoderamiento, DNI del apoderado, recibo IBI, IAE de la sociedad y de la instaladora, fichas técnicas, coordinador de Seguridad y Salud, asume de dirección técnica, declaración responsable, justificante de tasas. Documentación específica potestativa: informe CHT (si a menos de 100 m del río), estudio estructural de marquesinas, certificado de solidez estructural en cubiertas, estudio de viabilidad geométrica, certificado de medios de elevación. Plazo del ayuntamiento: **4 meses**. Plazo CHT: **3 meses, ampliable a 6**. AESA: no requerido si la instalación no supera la altura del edificio y ocupa 100 m2 o menos (criterio RD 244/2019); si se requiere, plazo de **6 meses**.

**6.2 Tramitación en la Comunidad de Madrid (DGIEM):** permisos ambientales no aplican (Ley 21/2013, solo para venta a red en más de 100 ha, no aplica a autoconsumo sin excedentes). Autorización administrativa previa y de construcción obligatoria para potencia superior a 500 kW. Autorización de puesta en servicio: plazo **3 meses** (Decreto 70/2010 CAM). Documentación: certificado dirección de obra, certificado instalación eléctrica (empresa habilitada en AT), declaración responsable, declaraciones UE de conformidad de inversores (RD 1699/2011, RD 413/2014, protección anti-isla), documentación de conformidad del sistema anti-vertido (ITC-BT-40 Anexo I.4), certificado de inspección OCA en AT y BT.

**6.3 CAU:** identificador único = CUPS (22 caracteres) más A000. Se solicita a la distribuidora vía empresa instaladora.

**6.4 Inscripción en registro de producción:** obligatoria para potencia superior a 100 kW; trámite telemático a DGIEM, sin plazo formal (según experiencia, no suele demorarse mucho).

**6.5 Solicitud del punto de acceso y conexión:** NO necesaria por tratarse de autoconsumo sin vertido (simplificación del RD 244/2019). Si en el futuro se cambiara a modalidad con excedentes: aval de 40 euros por kW (más de 100 kW), riesgo de pérdida del 100% del aval por incumplir hitos del RD-ley 23/2020, o 20% por inadmisión en nudo sin capacidad. Distribuidora: **Iberdrola Distribución**. Plazos del trámite completo: evaluación y propuesta previa (40 días si más de 36 kV), aceptación o discordancia (30 días), documentación adicional (10 días), respuesta a revisión (15 días), propuesta revisada aceptada (30 días), remisión de permisos (20 días); **mínimo 70 días** en total (potencialmente mayor por incumplimientos habituales de las distribuidoras).

**Tabla 11:** cronograma Gantt de 9 meses con hitos: licencia de obras, informe CHT, informe AESA (no requerido), autorización de impacto ambiental (no requerido), autorización de explotación, autorización previa y de construcción, obtención del CAU, inscripción en registro de autoconsumo, solicitud de punto de acceso (no requerido).

### II.7 Solución de autoconsumo

Capacidad de acceso disponible en el nudo de conexión (anonimizado en el original): **1,17 MW** según mapa de capacidad de Iberdrola Distribución (actualizado a 28 de abril de 2023), lo que en principio permitiría vertido de excedentes. Sin embargo, **se decide autoconsumo sin excedentes** por: evitar el trámite de acceso y conexión y el aval de 40 euros por kWn; evitar la contratación de representante en mercado eléctrico y la inscripción en RAIPRE (necesaria para venta de excedentes); el valor de la energía vertida es muy bajo dado el elevado consumo del punto de suministro; una modalidad con excedentes podría requerir sobrecostes de conexión (transformador o subestación) estimados en unos **200.000 €**; este proyecto es la Fase 1 de un plan de instalación de más potencia FV en fases posteriores, y cambiar de modalidad limitaría la capacidad de red disponible para esas fases. La modalidad de autoconsumo puede cambiarse tras 4 meses desde la puesta en marcha.

### II.8 Propuestas de ejecución

**8.1 Propuesta A**, usa zonas 1, 1.1, 1.2, 1.3 (suelo, respetando 50 m de la linde del río):

**Tabla 12 — Características Propuesta A:**

| Zonas | 1 | 1.1 | 1.2 | 1.3 | Total |
|---|---|---|---|---|---|
| Nº módulos | 707 | 1.931 | 211 | 216 | 3.065 |
| Potencia pico (kWp) | 382 | 1.043 | 114 | 117 | 1.657 |
| Potencia nominal (kWn) | 360 | 1.000 | 100 | 100 | 1.560 |
| Orientación / Inclinación | SSE / 20° en las 4 zonas | | | | |

**Tabla 13 — Generación mensual por zonas (kWh), total anual 2.714.388 kWh; 1.638 horas equivalentes.**

**Tabla 14 — Flujos energéticos mensuales:** total anual: energía autoconsumida 2.600.914 kWh, energía de red 6.126.986 kWh, energía vertida a red 113.474 kWh, ratio autoconsumo **96%**, ratio autosuficiencia **30%**.

Ventajas: alta radiación (orientación sur óptima), ratios elevadas, costes marginales bajos, un solo tipo de emplazamiento (mano de obra y mantenimiento simple), sin necesidad de grúas, ejecución por fases. Inconvenientes: más trámites CHT (zona a 50 m del río), caseta necesaria para inversores, obra civil para soterrar cableado (interrumpida por la nueva carretera), evacuación centralizada en un único cuadro. **Plazo total de unos 16 meses** (Tabla 15, Gantt).

**8.2 Propuesta B**, zonas 1, 1.2, 1.3, 3, 4 (suelo a 100 m más cubiertas):

**Tabla 16:** Nº módulos 1.480 total; potencia pico **800 kWp**; potencia nominal 732 kWn.

**Tabla 17:** generación mensual, total anual **1.305.175 kWh**; 1.630 horas equivalentes.

**Tabla 18:** energía autoconsumida 1.305.175 kWh, energía de red 7.422.725 kWh, energía vertida **0 kWh** (ninguna), ratio autoconsumo **100%**, autosuficiencia **15%**.

Ventajas: no depende de la CHT (plazo de ejecución corto), autoconsumo cercano al 100%, varias vías de evacuación, ejecución por fases, coste reducido por estructura coplanar. Inconvenientes: autosuficiencia moderada, caseta de inversores, obra civil, dos tipos de estructura (mayor coste de mantenimiento). **Plazo total de unos 8 meses**, el más corto de las 3 propuestas (Tabla 19).

**8.3 Propuesta C**, zonas 1, 1.2, 1.3, 2, 2.1 (suelo a más de 100 m más marquesinas):

**Tabla 20:** Nº módulos 2.784 total; potencia pico **1.504 kWp**; potencia nominal 1.320 kWn.

**Tabla 21:** generación mensual, total anual **2.301.390 kWh**; 1.529 horas equivalentes.

**Tabla 22:** energía autoconsumida 2.272.701 kWh, energía de red 6.455.199 kWh, energía vertida 28.689 kWh, ratio autoconsumo **99%**, autosuficiencia **26%**.

Ventajas: sin trámite CHT, autoconsumo elevado (99%), autosuficiencia elevada (26%), ejecución por fases, posibilidad futura de puntos de recarga de VE en marquesinas. Inconvenientes: cambio de estructura de marquesinas (sobrecoste más informe de cumplimiento CTE), peores ratios que A por orientación de marquesinas, caseta de inversores, obra civil, evacuación centralizada. **Plazo total de unos 15 meses** (Tabla 23).

**8.4 Resumen de las propuestas:**

**Tabla 24 — Resumen técnico:**

| Ppta | Generación (kWh) | Potencia (kWp) | Plazo (meses) | Autocons. | Autosuf. | Heq | Evacuación | Recarga VE |
|---|---|---|---|---|---|---|---|---|
| A | 2.714.388 | 1.657 | 16 | Óptimo | Medio-alto | 1.638 | Centralizada | Media |
| B | 1.305.175 | 800 | 8 | Óptimo | Medio-bajo | 1.630 | Diversificada | Media |
| C | 2.301.390 | 1.504 | 15 | Óptimo | Medio-alto | 1.529 | Centralizada | Óptima |

**Tabla 25 — Resumen de flujos energéticos anuales:**

| Ppta | Autoconsumida (kWh) | Red (kWh) | A red (kWh) | Autoconsumo (%) | Autosuficiencia (%) |
|---|---|---|---|---|---|
| A | 2.600.914 | 6.126.986 | 113.474 | 96% | 30% |
| B | 1.305.175 | 7.422.725 | - | 100% | 15% |
| C | 2.272.701 | 6.455.199 | 28.689 | 99% | 26% |

**Sobre la hibridación con baterías:** se planteó inicialmente cubrir los periodos de menor generación, pero se **descartó explícitamente** al observar que la energía excedentaria (energía a red) es demasiado baja en las 3 propuestas, nula en la Propuesta B, por lo que el coste de instalación de baterías no se rentabilizaría.

**Conclusión de la comparación técnica:** la **Propuesta A** es la más adecuada por sus altas horas equivalentes y ratio de autosuficiencia, pese a su plazo de ejecución más largo; la Propuesta C queda en segundo lugar (autosuficiencia alta pero penalizada por el coste y plazo de las marquesinas).

### II.9 Evaluación económica

**9.1.1 Costes de ejecución**, estimados a partir de 3 grandes distribuidores nacionales (módulos e inversores) y del fabricante Praxiaenergy (estructuras); incluye ingeniería, tramitación y legalización, maquinaria, cableado, protecciones y margen industrial; **excluye obra civil (casetas), tasas e impuestos**.

**Tabla 26 — Costes de ejecución estimados:**

| Propuesta | Potencia (kW) | Precio total (€) | Precio unitario (€/Wp) |
|---|---|---|---|
| A | 1.657 | 1.035.426 | 0,62 |
| B | 800 | 536.385 | 0,67 |
| C | 1.504 | 1.148.265 | 0,76 |

**9.1.2 Ahorros energéticos**, precio medio de energía 74 €/MWh (abril 2023) más peajes y cargos.

**Tabla 27 — Tarifa eléctrica resumen** (idéntica a Tabla 2).

Costes de mantenimiento y reposición NO incluidos en el estudio económico (mantenimiento, IBI y seguro variables, no cuantificados); se supone reposición de equipos en el **año 15** al **70% del coste de compra actual** (típicamente inversores). Degradación: 0,8% año 0, 0,4% anual a partir del año 1.

**Tabla 28 — Ahorros energéticos sin autoconsumo (€), año base, con impuesto eléctrico del 5,11%** (nota: en 2023 se aplicó exención puntual de este impuesto por el RD-ley 20/2022): total 715.676 €.

**9.1.3 Incentivos fiscales:**
- **Subvención nacional RD 477/2021** (modificado por RD 377/2022), Programa de incentivos 1 (instalaciones de autoconsumo, sector servicios, con o sin almacenamiento).

**Tabla 29 — Cantidad subvencionable por propuesta:**

| Propuesta | Coste total subvencionado (€) | Coste unitario subvencionado (€/Wp) | % subvención s/coste total |
|---|---|---|---|
| A | 114.202 | 0,07 | 11 |
| B | 80.458 | 0,10 | 15 |
| C | 145.179 | 0,10 | 11 |

Estos valores NO se incluyen en los flujos de caja base (dependen de la disponibilidad presupuestaria de la Administración); se calculan también escenarios con subvención.

- **Bonificaciones fiscales municipales**: IBI, 25% de bonificación de la cuota íntegra sobre inmuebles con sistemas de aprovechamiento solar térmico o eléctrico, máximo **200 €/año**, durante los **5 primeros periodos impositivos**; sí se incluye en el cálculo de ahorros. ICIO, 95% sobre la base imponible de la construcción o instalación; NO se incluye en la evaluación económica (que no contempla tasas ni impuestos).

**9.1.4 Escenarios de evolución del mercado eléctrico (25 años, año base 2022):**

**Tabla 30 — Escenario decreciente** (basado en mercados de futuros OMIP, precio medio mercado diario 2022 = 167,3 €/MWh):

| Año | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 y sig. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| €/MWh | 167,3 | 91,6 | 103,5 | 91,0 | 65,0 | 59,6 | 53,1 | 47,4 | 45,9 | 44,7 | 43,5 | 43,5 |
| % vs. año base | - | -38 | -46 | -61 | -64 | -68 | -72 | -73 | -73 | -74 | -74 | -74 |

- **Escenario base:** precio constante en **91,59 €/MWh**.
- **Escenario incremental:** incremento anual del **0,8%** (justificado por mayor electrificación de la economía y penetración de renovables, con menor diferencia entre periodos tarifarios).

**9.2 Evaluación económica Propuesta A**

**Tabla 31 — Costes del término de energía con autoconsumo, año 1:** total con autoconsumo 498.848 €, ahorro **216.827 €** respecto a la factura sin FV (**30,3%** del coste actual del término de energía).

**Tabla 32 — Resumen agregado de escenarios (25 años):**

| Escenario | Subvención | Ahorros (€) | TIR (%) | Payback (años) |
|---|---|---|---|---|
| Decreciente | Sin | 1.398.314 | 13,36 | 6,0 |
| Decreciente | Con | 1.512.516 | 16,77 | 4,8 |
| Base | Sin | 5.522.848 | 33,76 | 2,9 |
| Base | Con | 5.637.050 | 39,71 | 2,5 |
| Incremental | Sin | 6.179.449 | 34,77 | 2,9 |
| Incremental | Con | 6.293.651 | 40,77 | 2,5 |

**9.3 Evaluación económica Propuesta B**

**Tabla 33:** ahorro año 1 = **108.644 €** (15,20% del coste actual del término de energía).

**Tabla 34 — Resumen agregado (25 años):**

| Escenario | Subvención | Ahorros (€) | TIR (%) | Payback (años) |
|---|---|---|---|---|
| Decreciente | Sin | 882.262 | 31,50 | 2,6 |
| Decreciente | Con | 801.804 | 20,51 | 3,9 |
| Base | Sin | 2.952.010 | 64,76 | 1,5 |
| Base | Con | 2.871.552 | 46,24 | 2,2 |
| Incremental | Sin | 3.281.501 | 66,00 | 1,5 |
| Incremental | Con | 3.201.043 | 47,35 | 2,1 |

(Nota: en la Tabla 34 del original, las filas Sin/Con subvención del escenario decreciente aparecen invertidas en TIR y Payback respecto a los datos numéricos de las Tablas 10A y detalle; se transcribe literalmente tal como figura en la fuente, sin corregir.)

**9.4 Evaluación económica Propuesta C**

**Tabla 35:** ahorro año 1 = **189.102 €** según el texto; total mostrado en tabla 231.122 € (nota: hay una pequeña discrepancia entre el ahorro anual citado en el texto, 189.102 €, y el total de la Tabla 35 del documento original, 231.122 €, no resuelta por la fuente; se reporta tal cual, el 26,4% citado corresponde al primer valor).

**Tabla 36 — Resumen agregado (25 años):**

| Escenario | Subvención | Ahorros (€) | TIR (%) | Payback (años) |
|---|---|---|---|---|
| Decreciente | Sin | 970.240 | 8,09 | 9,5 |
| Decreciente | Con | 1.115.419 | 10,80 | 7,4 |
| Base | Sin | 4.574.293 | 24,56 | 4,0 |
| Base | Con | 4.719.472 | 29,32 | 3,4 |
| Incremental | Sin | 5.148.037 | 25,51 | 3,9 |
| Incremental | Con | 5.293.216 | 30,31 | 3,3 |

**9.5 Resumen evaluación económica (Tabla 37, consolidado de 32/34/36).** Conclusión: la **Propuesta A** es la más adecuada, payback similar a B y menor que C, con ahorros absolutos mayores que ambas. La Propuesta C tiene paybacks muy altos por el sobrecoste de las marquesinas. La Propuesta B, aunque con TIR porcentualmente mayor, tiene coste marginal alto (menor potencia) y ahorros absolutos bajos.

### III.1 Descripción de la instalación (ingeniería básica final)

Tras visita técnica y análisis más exhaustivo, la decisión final es una instalación **sobre suelo de 3.024 módulos de silicio monocristalino de 530 Wp** (aprox. 1,6 MWp), correspondiente en gran medida a la Propuesta A. Energía en CC inyectada mediante **14 inversores de 100 kW** (1,4 MWn) a un centro de transformación que eleva la tensión de 400 V a 20 kV. Estructuras de altura de 4 m o menos (no sobrepasan la rasante de edificios colindantes). Previsión de generación anual: **2,7 GWh**.

**Tabla 38 — Características principales de la instalación fotovoltaica (diseño final):**

| Parámetro | Valor |
|---|---|
| Tipo de instalación | Planta FV de generación de 1,603 MWp |
| Superficie del proyecto | 1,5 ha |
| Potencia pico | 3.024 módulos x 0,53 kW = 1,603 MWp |
| Potencia nominal | 14 inversores x 100 kW = 1,4 MWn |
| Sistema de instalación | Sobre suelo |
| Módulo, Fabricante/Modelo | Jinko Solar / JKM530M-7TL4-V |
| Módulo, Potencia unitaria | 530 Wp |
| Inversor, Fabricante/Modelo | Fronius / TAURO ECO 100 |
| Inversor, Potencia unitaria | 100 kWn |
| Estructura, Tipo/Fabricante | Mesas fijas / Nclave (o similar) |
| Estructura, Nº de mesas | 168 |
| Distancia entre filas | 8,5 m |
| Configuración | 2Vx9 (18 módulos) |
| Tipo de poste | Biposte |
| Inclinación | 20° |

**Nota de discrepancia (explícita en el propio TFM):** el módulo y el inversor del diseño final (JinkoSolar 530 Wp más Fronius) **difieren** de los usados en el análisis técnico-económico preliminar de la Propuesta A (JinkoSolar Tiger Pro 540 Wp más Huawei). El propio documento lo explica en las conclusiones: se tuvo que modificar el modelo de módulo e inversor por problemas de stock, y se eliminaron las zonas 1.2 y 1.3 por baja potencia instalable (no compensaban las pérdidas por extensión de cable).

### III.2 Cálculos eléctricos

**2.1 Dimensionado del generador fotovoltaico**

Número total de módulos (objetivo de unos 1.400 kWn multiplicado por un factor de sobredimensionado de 1,15 = 1.600.000 W pico):

$$N_T = \frac{P_{pico}}{P_{unitaria}} \quad [2]$$

Con $P_{pico}=1.600.000\ W$, $P_{unitaria}=530\ W$, resulta $N_T = 3.018$ módulos, redondeado al múltiplo de 18 más próximo (18 = máximo de módulos por MPPT del inversor): **3.024 módulos**.

**Número máximo de módulos en serie** (limitado por tensión máxima de entrada del inversor):

$$N_{serie\_max} \leq \frac{V_{CC\_max}}{V_{mod\_OC}} \quad [3]$$

$$V_{modOC}(G_{STC}, T_{min}) = V_{mod\_OC,STC} + \beta_V \cdot (T_{min} - 25°C) \quad [4]$$

Con $V_{mod\_OC,STC}=48,8\ V$, $\beta_V=-0,26\%/°C$, $T_{min}=-10°C$, resulta $V_{mod\_OC}(G_{STC},T_{min}) = 53,2\ V$. Con $V_{CC\_max}=1.000\ V$, resulta **$N_{serie\_max}=18$ módulos**.

**Número mínimo de módulos en serie** (limitado por tensión mínima del PMP del inversor):

$$N_{serie\_min} \geq \frac{V_{CC\_min}}{V_{mod\_min}} \quad [5]$$

$$V_{mod\_min}(G_{STC}, T_{max}) = V_{mod\_PMP} + \beta_V \cdot (T_{max} - 25°C) \quad [6]$$

Con $V_{mod\_PMP}=48,8\ V$, $\beta_V=-0,26\%/°C$, $T_{max}=55°C$, resulta $V_{mod\_min}=37,7\ V$. Con $V_{CC\_min}=580\ V$, resulta **$N_{serie\_min}=16$ módulos**.

**Número de módulos en paralelo** (limitado por corriente máxima de entrada del inversor):

$$N_p \leq \frac{I_{CC\_max}}{I_{mod\_SC}} \quad [7]$$

Con $I_{CC\_max}=175\ A$, $I_{mod\_SC}=14,01\ A$, resulta **$N_p=12$ módulos**.

**Resumen del generador:** 3.024 módulos = 12 ramas de 18 módulos cada una, conectadas a cada uno de los 14 inversores.

**2.2 Dimensionado del cableado**

**Cableado CC** (módulos hacia cuadro CC hacia inversor). Criterio de caída de tensión:

$$S_{string} = \frac{2 \cdot L_{string} \cdot I_{string}}{\Delta V_{string} \cdot \sigma \cdot V_{string}} \quad [8]$$

Con $L_{string}=80\ m$, $I_{string}=12,96\ A$, $\Delta V_{string}=1,5\%$, $\sigma=44\ \Omega^{-1}\cdot m/mm^2$, $V_{string}=736,2\ V$, resulta **$S_{string}=4,27\ mm^2$**, sección comercial elegida: **6 mm2**.

Criterio de intensidad máxima (UNE 60364-7-712):

$$I_0 \geq 1,25 \cdot I_{string\_max} \quad [9]$$

Con $I_{string\_max}=13,8\ A$ (corriente de cortocircuito del módulo), resulta **$I_0=17,25\ A$**.

**Tabla 39 — Intensidad máxima admisible según método de instalación (extracto UNE-EN 50618:2015):**

| Sección (mm2) | Un cable al aire libre (A) | Un cable sobre superficie (A) | Dos cables en contacto sobre superficie (A) |
|---|---|---|---|
| 1,5 | 30 | 29 | 24 |
| 2,5 | 41 | 39 | 33 |
| 4 | 55 | 52 | 44 |
| 6 | 70 | 67 | 57 |
| 10 | 98 | 93 | 79 |

Corrección por condiciones de instalación:

$$I_z = K_1 \cdot K_2 \cdot I_{adm} \quad [10]$$

**Tabla 40 — Factor K1** (agrupación de cables, extracto UNE HD 60364-5-52): para 2 circuitos agrupados, K1 = 0,80 (de una escala 1,00/0,80/0,70/0,65/0,60/0,57 para 1 a 6 circuitos).

**Tabla 41 — Factor K2** (temperatura de operación, extracto UNE-EN 50618): 60°C da 1,00; 70°C da 0,92; 80°C da 0,84; 90°C da 0,75. Temperatura de operación tomada: 90°C, K2=0,75.

Con $I_o=57\ A$ (sección 6 mm2, un cable sobre superficie), $K_1=0,8$, $K_2=0,75$, resulta $I_z=34,2\ A$, mayor que los $17,25\ A$ requeridos. **Se utilizan cables de 6 mm2 unipolares de cobre con aislamiento de polietileno reticulado.**

**Cableado CA** (inversor hacia cuadro de protección y medida). Criterio de caída de tensión trifásica:

$$S_{CA\_trif} = \frac{\sqrt{3} \cdot L_{CA} \cdot I_{inv\_CA} \cdot \cos(\varphi)}{\Delta V_{CA} \cdot \sigma \cdot V_{linea}} \quad [11]$$

Con $L_{CA}=150\ m$, $I_{inv\_CA}=152\ A$, $\cos(\varphi)=1$, $\Delta V_{CA}=1,5\%$, $\sigma=44\ \Omega^{-1}\cdot m/mm^2$, $V_{linea}=400\ V$, resulta **$S_{CA\_trif}=149,59\ mm^2$**, sección comercial elegida provisionalmente: **150 mm2**.

Criterio de corriente máxima:

$$I_o \geq 1,25 \cdot I_{inv\_CA} \quad [12]$$

Con $I_{inv\_CA}=152\ A$, resulta $I_o \geq 190\ A$. Según Tabla 5 ITC-BT-07 (cables soterrados directamente), cable de 150 mm2 admite $I_z=415\ A$ en condiciones de referencia. Sin embargo, al canalizar cada terna de cables por un mismo conducto (factor 0,8) y agrupar los conductos en hasta 3 capas de 4 conductos (factor 0,48): $I_z = 415 \times 0,8 \times 0,48 = 159\ A$, insuficiente por ser menor a 190 A. **Se aumenta la sección a 240 mm2**: $I_z = 540 \times 0,8 \times 0,48 = 207\ A > 190\ A$, válido.

**2.3 Distribución de los inversores:** layout preliminar (Figura 15/16, no reproducible en texto) con ubicación de los 14 inversores y el centro de transformación, y distribución de las 12 ramas de módulos por inversor (código de colores por inversor).

### III.3 Mediciones y presupuestos

**Tabla 42 — Presupuesto de ejecución material (extracto):**

| ID | Concepto | Ud. | Importe (€) |
|---|---|---|---|
| 01.01 | Paneles FV Jinko Solar JKM530-7TL4-V, 1.602,72 kWp | 3.024 | 434.700,00 |
| 01.02 | Inversor trifásico Fronius TAURO Eco 100-3-P/D | 14 | 124.200,00 |
| 01.03 | Estructura de aluminio inclinada | 3.024 | 113.850,00 |
| 01.04 | Equipo de medida Huawei DTSU666-H | 1 | 152.145,00 |
| 01.05 | Cableado y protecciones (Cu 6 mm2: 26.880 m; CA 4x(1x240) mm2: 30 m) | 1 | 43.200,00 |
| 02.01 | Montaje de material | 1 | 103.500,00 |
| 02.02 | Puesta en marcha | 1 | 10.350,00 |
| 02.03 | Medios de elevación | 1 | 1.035,00 |
| 02.04 | Gestión de residuos | 1 | 270,00 |

**Tabla 43 — Importe por capítulos:**

| ID | Capítulo | Importe (€) |
|---|---|---|
| 01 | Estructura y equipos | 866.295,00 |
| 02 | Mano de obra, instalación y puesta en marcha | 116.955,00 |
| — | **Total (sin IVA)** | **983.250,00** |

**Tabla 44 — Importe total de la inversión:**

| Concepto | Importe (€) |
|---|---|
| Presupuesto de ejecución material | 983.250,00 |
| Tramitación administración municipal y autonómica | 15.525,00 |
| Ingeniería | 25.875,00 |
| Trámites con la empresa distribuidora | 5.175,00 |
| Tramitación y realización de la PRL | 5.175,00 |
| **Total (sin IVA)** | **1.035.000,00** |
| IVA (21%) | 217.350,00 |
| **Importe total de la inversión (con IVA)** | **1.252.350,00** |

### III.4 Planos

Índice de planos (contenido gráfico, no extraído en texto): plano de situación, plano del emplazamiento, referencia catastral del inmueble (marcado CONFIDENCIAL en el original), plano de implantación general (marcado CONFIDENCIAL), implantación de paneles FV, plano de cableado CC, plano de cableado CA, plano de zonas del DPH, diagrama unifilar.

### III.5 Conclusiones y líneas futuras (texto original)

- La **Propuesta A** es la más adecuada por factores técnicos (ratio de autosuficiencia y horas equivalentes) y económicos (altos ahorros, bajos tiempos de retorno), pese a ser la de mayor plazo de ejecución. En la ingeniería de detalle se tuvo que **cambiar módulo e inversor por problemas de stock**, y se eliminaron las zonas 1.2 y 1.3 (baja potencia instalable, pérdidas de cable no compensadas económicamente).
- Dados los precios de la energía recientes y la dependencia energética, la instalación es **económicamente rentable**: ahorros cercanos al 30,3% del coste actual del término de energía.
- La instalación ahorraría **unos 2,6 MWh** de consumo de red (reducción de uso de combustibles fósiles asociados; consumo de proximidad, menores pérdidas de red).
- Los tiempos de ejecución se alargan principalmente por la **tramitación** (diseño y construcción están maduros); hasta **16 meses** en la Propuesta A. En la Propuesta C, la instalación de marquesinas es un factor determinante de retraso.

**Líneas futuras:** (1) nueva fase de instalación en el complejo (alto consumo, generación actual se autoconsume casi en su totalidad); explorar Propuestas B y C para fases posteriores. (2) Marquesinas FV más puntos de recarga de vehículos eléctricos para empleados. (3) **Hibridación con baterías** una vez ampliada la instalación (para cubrir consumo nocturno o días de baja radiación) u otra renovable térmica para procesos con demanda de calor; complementar con medidas de eficiencia energética.

### III.6 Planificación temporal

Figura 17: diagrama de Gantt del proyecto realizado con MS Project (contenido gráfico, no extraído en texto).

### III.7 Bibliografía (19 referencias, listado completo)

1. Perfiles de consumo REE. 2. Precio de casación del mercado diario, OMIE (2023). 3. Peajes de acceso a redes de transporte y distribución, MITECO. 4. PVGIS (re.jrc.ec.europa.eu/pvg_tools/en/). 5. Derivatives, OMIP (mayo 2023). 6-7. Referencias sin descripción textual visible, asociadas a imágenes confidenciales de vista aérea y referencia catastral. 8. SNCZI, Inventario de Presas y Embalses, MITECO. 9. Delimitación del DPH, Proyecto LINDE, MITECO. 10. Tecnologías y tipologías de paneles fotovoltaicos, Solar FM (2020). 11. La rápida evolución de los módulos fotovoltaicos, Grupotec. 12. Tier 1 de placas solares, Selectra. 13. Mejores inversores solares, Atersa Solar. 14. Sistema de monitorización para autoconsumo FV, Selectra (2022). 15. Guía profesional de tramitación del autoconsumo, IDAE/ENERAGEN (2023, pp. 122-123). 16. Mapa de capacidad de acceso, Iberdrola Distribución. 17. El efecto PID en paneles solares, Techno Sun. 18. Es necesaria una licencia de obras para una instalación solar, SolarPlack. 19. Permiso de Obra Menor, GRN.

### Abreviaturas, unidades y definiciones (glosario íntegro del documento)

**Abreviaturas:** BOE, CTE (Código Técnico de la Edificación), PRTR, IBI, ICIO, IAE, REE, CNMC, CAPEX, PVGIS, OMIE, CAU, CUPS, DPH, AESA, CHT, Si, STC, PID, CC, CA, MPPT, CFO, CIF, DNI, DGIEM, CT, RAIPRE, TIR, PMP, CdT.

**Definiciones destacadas:**
- **Ratio de autoconsumo**: relación entre la energía consumida de la instalación FV y la generación FV total.
- **Ratio de autosuficiencia**: relación entre la energía consumida de la instalación FV y el consumo total.
- **Potencia pico**: potencia total de los módulos (potencia unitaria multiplicada por número de módulos), en kWp.
- **Potencia nominal**: potencia total de los inversores (suma de potencias unitarias), en kWn.
- **Horas equivalentes de funcionamiento**: periodo en el que la radiación solar equivale a 1 kW/m2.
- **Efecto PID** (Potential Induced Degradation): degradación por corrientes de fuga entre células y otros componentes del módulo (marco de aluminio, vidrio, tédlar, EVA), reduce el rendimiento.
- **DPH cartografiado**: superficie del álveo o cauce natural delimitada mediante el Proyecto LINDE Fase II.
- **Licencia de obra menor**: trámite municipal para construcciones o instalaciones que no superen 100 m2 o no modifiquen estructura o fachada.

### Anexo I: Cálculo de la subvención (RD 477/2021, Programa P1)

Metodología de cálculo: coste elegible de generación (CEUG), coste unitario de referencia (CUF), coste subvencionable unitario de generación (CSUG), más coste subvencionable de otras actuaciones (amianto/marquesinas), coste subvencionable unitario máximo total (CSUMTG, tope normativo), coste subvencionable unitario final de generación (CUSFG, el menor entre CSUG y CSUMTG), multiplicado por el porcentaje de ayuda por tipo de empresa (15% en los 3 casos, gran empresa en municipio de más de 5.000 habitantes), coste unitario subvencionable multiplicado por potencia instalada, igual a coste total subvencionado.

**Tabla 1A/2A — Propuesta A:** CEUG 694 €/kWp; CUF 120 €/kWp; CSUG 574 €/kWp; CSUMTG 460 €/kWp; CUSFG 460 €/kWp; coste unitario subvencionable 69 €/kWp; potencia 1.655 kWp; **coste total subvencionado 114.202 €** (10% del coste total, 0,07 €/Wp).

**Tabla 3A/4A — Propuesta B:** CEUG 671 €/kWp; sin CUF de referencia; CSUG 671 €/kWp; CSUMTG 749 €/kWp; CUSFG 671 €/kWp; coste unitario subvencionable 101 €/kWp; potencia 799 kWp; **coste total subvencionado 80.458 €** (15% del coste total, 0,10 €/Wp).

**Tabla 5A/6A — Propuesta C:** CEUG 764 €/kWp; CUF 120 €/kWp; CSUG 644 €/kWp; coste subvencionable otras actuaciones (marquesinas) 127 €/kW; total coste subvencionable 771 €/kWp; CSUMTG 960 €/kWp; CUSFG 644 €/kWp; coste unitario subvencionable 97 €/kWp; potencia 1.503 kWp; **coste total subvencionado 145.179 €** (11% del coste total, 0,10 €/Wp). Coste total del sistema con marquesinas: 1.339.385 € (0,89 €/Wp), 891 kWp en marquesina a 191.120 € (fabricante Praxia).

### Anexo II: Flujos de caja (25 años, 3 propuestas por 3 escenarios, 9 tablas completas en la fuente)

**Ejemplo íntegro, Tabla 7A, Propuesta A, escenario decreciente, sin subvención** (estructura: Año, Ahorro €, Bonificaciones €, Inversión €, Ahorros netos €, Flujos de caja agregados €):

| Año | Ahorro (€) | Bonif. (€) | Inversión (€) | Ahorros netos (€) | Flujo agregado (€) |
|---|---|---|---|---|---|
| 0 | 264.916 | - | (1.035.426) | (770.509) | (770.509) |
| 1 | 150.356 | 200 | - | 150.356 | (620.153) |
| 5 | 101.613 | 200 | - | 101.613 | (92.532) |
| 6 | 91.848 | - | - | 91.848 | (685) |
| 7 | 83.219 | - | - | 83.219 | 82.534 |
| 15 | 75.649 | - | (45.401) | 30.248 | 654.196 |
| 20 | 74.521 | - | - | 74.521 | 1.029.050 |
| 25 | 73.410 | - | - | 73.410 | 1.398.314 |
| **Total** | **2.479.141** | **1.000** | **(1.080.827)** | **1.398.314** | **1.398.314** |

(Nota: tabla condensada a años representativos por repetitividad estructural; el payback se cruza entre el año 6 y 7, coherente con el 6,0 años reportado en Tabla 32.) Se observa reinversión (reposición de equipos) en el **año 15** en las 9 combinaciones, coincidiendo con la hipótesis del apartado 9.1.2 (coste de reposición igual al 70% del coste actual): Propuesta A -45.401 €; Propuesta B -22.514 €; Propuesta C -38.723 €.

Las **8 tablas restantes** (Propuesta A base e incremental; Propuesta B decreciente, base e incremental; Propuesta C decreciente, base e incremental) siguen idéntica estructura fila a fila (26 años, mismo esquema de columnas) y sus resultados agregados a 25 años ya están íntegramente recogidos en las Tablas 32, 34 y 36 de este resumen (ahorros totales, TIR, payback, con y sin subvención); no se han transcrito año a año en este documento por ser altamente repetitivas y no aportar información no capturada ya por los totales, siguiendo el mismo criterio de síntesis aplicado en los resúmenes de referencia previos de este vault.

### Anexo III: Fichas técnicas (contenido gráfico, no extraído)

Páginas 103-110 del PDF. Por la referencia del cuerpo del documento (apartados 5.1 y 5.2), corresponden a las fichas técnicas de: módulo **JinkoSolar Tiger Pro JKM540M-72HL4-V0** (540 Wp), inversores **Huawei SUN2000-100KTL-H1** y **SUN2000 60KTL M0**, y, dado que la Tabla 38 del capítulo de ingeniería básica referencia también fichas del diseño final, posiblemente **JinkoSolar JKM530M-7TL4-V** y **Fronius TAURO ECO 100**, aunque esto último no se ha podido confirmar por no haber texto extraíble en estas páginas.

### Anexo IV: Informe de generación (contenido gráfico, no extraído)

Páginas 111-124 del PDF. Referenciado en el cuerpo (apartado III.1: la información detallada del resultado está en el Anexo IV, Informe de generación) como el informe de simulación de la generación anual estimada (2,7 GWh/año) de la instalación final de 1,603 MWp. El formato y software de origen (PVsyst u otro) no se ha podido determinar por no haber texto extraíble en estas páginas.

## Datos clave (con página de origen)

- Consumo eléctrico del complejo industrial (2021): **8.727.900 kWh/año**, coste eléctrico total 893.633 €/año, término de energía igual al 80% del coste (p. 9-10).
- Precio de energía usado para el estudio: **74 €/MWh** (precio medio de mercado diario, abril 2023) (p. 5-6).
- Restricciones de emplazamiento: Dominio Público Hidráulico del Río Jarama (zona de policía 100 m, zona de servidumbre 5 m), zona de influencia AESA por proximidad a Madrid-Barajas T4 (p. 11-14).
- 8 de 21 espacios evaluados resultan aptos para instalación FV (p. 15-17).
- Módulo del análisis técnico-económico: JinkoSolar Tiger Pro JKM540M-72HL4-V0, 540 Wp, eficiencia 20,94% (p. 21).
- Inversores del análisis técnico-económico: Huawei SUN2000-100KTL-H1 (100 kW) y SUN2000 60KTL M0 (60 kW) (p. 22).
- Tipología de autoconsumo elegida: **individual, sin excedentes**, por consumo anual mayor de 8.000 MWh (p. 7-8, 15, 31-32).
- Propuesta A (elegida): 1.657 kWp, 2.714.388 kWh/año, autoconsumo 96%, autosuficiencia 30%, coste ejecución 1.035.426 € (0,62 €/Wp), plazo 16 meses (p. 33-35, 43).
- Propuesta B: 800 kWp, 1.305.175 kWh/año, autoconsumo 100%, autosuficiencia 15%, coste 536.385 € (0,67 €/Wp), plazo 8 meses (p. 36-38, 43).
- Propuesta C: 1.504 kWp, 2.301.390 kWh/año, autoconsumo 99%, autosuficiencia 26%, coste 1.148.265 € (0,76 €/Wp), plazo 15 meses (p. 39-41, 43).
- Hibridación con baterías: **descartada explícitamente** en las 3 propuestas por baja energía excedentaria (p. 42).
- Resultados económicos Propuesta A (25 años, sin subvención): ahorros entre 1.398.314 € (decreciente) y 6.179.449 € (incremental); TIR entre 13,36% y 34,77%; payback entre 6,0 y 2,9 años (p. 47-48).
- Subvención RD 477/2021 (Programa P1): Propuesta A 114.202 € (10%); B 80.458 € (15%); C 145.179 € (11%) (p. 45, 89-91).
- Diseño final (ingeniería básica): 3.024 módulos JinkoSolar JKM530M-7TL4-V (530 Wp) igual a 1,603 MWp; 14 inversores Fronius TAURO ECO 100 igual a 1,4 MWn; estructura Nclave, 168 mesas, distancia entre filas 8,5 m, inclinación 20° (p. 54).
- Cálculo eléctrico del generador: 18 módulos máximo en serie, 16 módulos mínimo en serie, 12 ramas en paralelo, resultando 3.024 módulos igual a 12 ramas por 18 módulos por cada uno de los 14 inversores (p. 55-57).
- Cableado CC: sección 6 mm2 Cu (por criterio de caída de tensión 4,27 mm2 y criterio de intensidad 17,25 A); cableado CA: sección aumentada de 150 mm2 a 240 mm2 por factores de agrupación de conductos (p. 57-60).
- Presupuesto de ejecución material: **983.250 € sin IVA**; inversión total con tramitación e IVA: **1.252.350 €** (p. 63-64).
- Normativa clave citada: RD 244/2019 (autoconsumo), RD 477/2021 y RD 377/2022 (subvenciones), RD 1183/2020 (acceso y conexión), REBT (RD 842/2002), CTE (RD 314/2006), UNE-EN 50618:2015 y UNE HD 60364-5-52 (cableado FV), ITC-BT-07 (cables soterrados) (p. 1-3, 57-59).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta** (ver Memoria/indice_propuesto.md): capítulo de tipología de autoconsumo y tramitación (ejemplo muy detallado y trazable del procedimiento administrativo completo: ayuntamiento, Comunidad de Madrid, CAU, registro, con plazos concretos por trámite, más exhaustivo en este aspecto que los otros dos TFM de referencia ya indexados); capítulo de dimensionado eléctrico (metodología completa y con ecuaciones explícitas para el número de módulos en serie/paralelo y el dimensionado de cableado CC/CA según UNE, directamente aplicable al capítulo de ingeniería eléctrica del CPD de Mario); capítulo de análisis económico (estructura de escenarios de evolución de precios de mercado, decreciente, base e incremental, y tratamiento de subvenciones RD 477/2021 como línea de sensibilidad, algo que los otros dos TFM de referencia no desarrollan con este detalle).
- **Qué aporta exactamente:** primero, un ejemplo completo de comparación de escenarios de mercado eléctrico a 25 años basado en curvas de futuros OMIP, útil como plantilla para el análisis de sensibilidad de precios en el capítulo económico de Mario. Segundo, metodología explícita y con ecuaciones para el dimensionado eléctrico de un generador FV en baja tensión (número de módulos en serie/paralelo, secciones de cable CC y CA con normativa UNE), más detallada en este aspecto que los otros dos TFM de referencia. Tercero, un caso adicional (el tercero de los tres TFM de referencia disponibles) donde el almacenamiento en baterías se descarta explícitamente por baja energía excedentaria, refuerza el patrón observado en el TFM de San Martín PYL, aunque aquí el motivo (excedentes bajos por sobredimensionamiento ajustado al 95% de autoconsumo, no por diferencial tarifario) es distinto y complementario para contrastar con el caso del CPD de Mario. Cuarto, el tratamiento explícito de restricciones medioambientales y administrativas atípicas (Dominio Público Hidráulico, zona de influencia aeroportuaria) como ejemplo de análisis de emplazamiento condicionado, aunque de aplicabilidad limitada al caso concreto del CPD si este no tiene restricciones similares.
- **Confianza en los datos:** todas las cifras provienen literalmente del texto extraído del PDF original (extracción completa de las 96 páginas de memoria más anexos I y II con tablas completas), con página de origen indicada. Se han señalado explícitamente las discrepancias detectadas en la propia fuente (cambio de módulo e inversor entre el análisis preliminar y la ingeniería final, explicado por el propio documento como problema de stock; pequeña discrepancia entre el ahorro anual citado en texto y el total de la Tabla 35 para la Propuesta C; posible inversión de filas Sin/Con subvención en la Tabla 34) sin resolverlas ni completarlas con criterio propio. Los Anexos III y IV son contenido puramente gráfico sin texto extraíble: su existencia y temática se documentan, pero ningún dato numérico de esas páginas se ha incorporado a este resumen.

## Notas de procesamiento

- Documento de 132 páginas de PDF. Se extrajo el texto completo con pypdf (texto nativo, sin necesidad de OCR) y se leyó el **100% del contenido textual disponible**, en tramos sucesivos, dado el nivel de densidad EXHAUSTIVO solicitado explícitamente por Mario.
- Los **Anexo III (Fichas técnicas, pp. 103-110 de la memoria) y Anexo IV (Informe de generación, pp. 111-124 de la memoria)** son páginas puramente gráficas (imágenes escaneadas o incrustadas sin capa de texto): la extracción automática no devolvió contenido más allá de encabezados y pies de página repetidos. No se ha podido reproducir ningún dato numérico de estas páginas en el resumen; si se necesita algún valor concreto de las fichas técnicas o del informe de generación, debe consultarse directamente el PDF original (posiblemente requiere OCR manual).
- Varias figuras del cuerpo del documento (vista aérea del complejo, referencia catastral, plano de implantación general) están marcadas explícitamente como CONFIDENCIAL en el PDF original y no contienen datos de localización extraíbles; la ubicación exacta del complejo industrial permanece anonimizada en toda la fuente (un municipio de la Comunidad de Madrid).
- El Anexo II (Flujos de caja) contiene 9 tablas de 26 filas cada una (3 propuestas por 3 escenarios), todas con idéntica estructura de columnas. Se ha transcrito íntegra una tabla representativa (Tabla 7A) condensada a los años clave (0, 1, 5-7, 15, 20, 25, Total) y se ha verificado que los resultados agregados de las 8 tablas restantes coinciden con los totales ya recogidos en las Tablas 32/34/36 del cuerpo del documento; no se han transcrito año a año las 8 tablas restantes por ser repetitivas en estructura y no aportar información adicional no capturada por sus totales.
- Se detectaron varias inconsistencias numéricas menores dentro del propio documento original (módulo e inversor del diseño preliminar vs. final; discrepancia entre ahorro anual citado en texto y total de tabla para la Propuesta C) y se han señalado explícitamente en el resumen en cada caso, sin intentar resolverlas.
- Las referencias bibliográficas 1 a 19 del TFM original se han mencionado en el cuerpo del resumen donde son relevantes, pero no se han verificado ni se reproducen como bibliografía propia (este documento no es citable).
