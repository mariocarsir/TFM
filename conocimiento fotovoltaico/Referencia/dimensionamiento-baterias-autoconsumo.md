---
title: "Dimensionamiento de baterías para autoconsumo"
tipo: presentacion
autor: "Úrsula Pérez Ramírez"
anio: 2025
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T9_BateriasAutoconsumo.pdf"
tags: [fotovoltaica, almacenamiento, autoconsumo, bateria, optimizacion, peajes]
related: []
---

# Dimensionamiento de baterías para autoconsumo (Úrsula Pérez Ramírez, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición 2025-2026, que distingue dos estrategias de gestión de batería en autoconsumo: la "brainless" (reglas simples PV-demanda, sin optimización económica) y la "smart" (optimización con arbitraje, inyección a red y peak shaving). Introduce el término de exceso de potencia del peaje de acceso como justificación económica del peak shaving, presenta un simulador basado en 84 combinaciones mes-día de la semana y un JSON de configuración, y esboza el uso de programación lineal/entera mixta (Pyomo, Python-MIP) para optimizar el despacho de un inversor híbrido PV-batería. Cierra con una lista de comprobación de indicadores financieros (VAN, TIR, ROI) y criterios prácticos de dimensionamiento. Es un documento breve (10 diapositivas) y de contenido mayormente cualitativo/introductorio, con poco desarrollo cuantitativo propio.

## Contenido técnico

### 1. Batería brainless (diapositiva 3)
1. No tiene en cuenta los precios de red.
2. Regla de control: PV > demanda → carga la batería; demanda > PV → descarga la batería.
3. Algunos modelos permiten programar cargas de batería desde red.
4. Gráfica descrita: eje X horas del día, ejes Y potencia (W), SOC (%) y precio (€/kWh); muestra curvas de tarifa, previsión PV, previsión de carga, consumo comprado a red antes/después de instalación y estado de carga a lo largo de un día tipo de marzo (lunes a viernes).

### 2. Batería smart (diapositivas 4-5)
1. Estrategia con cuatro fases diarias observadas en el gráfico del 19/02/2025: carga de red en horario barato (00:00-06:00), descarga en horario caro (06:00-12:00), carga con excedentes solares (12:00-18:00), descarga en horario caro (18:00-24:00). Ejes: precio (€/kWh) 0,05-0,3 a la izquierda, SOC (%) 0-100 a la derecha.
2. Fuentes de ahorro: arbitraje, energía solar almacenada, inyección a red, peak shaving.
3. **Justificación normativa del peak shaving — término de exceso de potencia**, fórmula literal de la diapositiva 5:

$$F_{PD} = \sum_{p=1}^{P=i} tep_p^{1-3} \times \sqrt{\sum_{j=1}^{n} (Pd_j - Pc_p)^2}$$

   Donde:
   - $F_{PD}$: facturación por potencia demandada (€).
   - $tep_p^{1-3}$: término de exceso de potencia (€/kW) del peaje correspondiente, período horario $p$, aplicable a puntos de suministro con tipo de punto de medida 1, 2 y 3.
   - $Pd_j$: potencia demandada en cada cuarto de hora $j$ del período $p$ en que se supera $Pc_p$ (kW); si el equipo de medida no tiene registro cuartohorario, se toma la misma potencia en todos los cuartos de hora.
   - $Pc_p$: potencia contratada en el período horario (kW).
   - $i$: número de periodos horarios del término de facturación de potencia del peaje correspondiente.
   - Fórmula atribuida a: BOE-A-2020-1066, Circular 3/2020, de 15 de enero, de la CNMC, metodología de cálculo de peajes de transporte y distribución.
   - Valores citados en la diapositiva: **BOE-A-2025-5341, Resolución de 6 de marzo de 2025 de la CNMC, que modifica el anexo II de la Resolución de 4 de diciembre de 2024**, valores de peajes de acceso aplicables desde el 1 de enero de 2025.

   **Aviso de vigencia (verificado contra `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`):** la resolución de valores de peajes citada en la diapositiva (BOE-A-2025-5341, de 06/03/2025, sobre la de 04/12/2024) **ya no está vigente**. La resolución de peajes 6.1TDA aplicable en 2026 es la **Resolución de 18 de diciembre de 2025 de la CNMC (BOE-A-2025-26348)**, con valores aplicables desde el 01/01/2026. La fórmula estructural del término de exceso de potencia ($F_{PD}$), que proviene de la Circular 3/2020, no cambia; lo que hay que actualizar antes de usar esta diapositiva en el TFM son los valores numéricos de $tep_p$ y $Pc_p$, tomándolos de la resolución vigente, no de esta presentación.

### 3. Simulador de escenarios (diapositivas 6-7)
1. El simulador combina tarifa, energía fotovoltaica y consumo en 7 días de la semana × 12 meses = 84 situaciones (combinaciones mes-día de la semana), cada una representada por una curva de producción fotovoltaica, demanda energética y tarifa a lo largo del día.
2. Estructura del JSON de entrada descrita (campos relevantes, sin unidades explícitas salvo indicado):
   - `configuration`: `simulationYears` (5 elementos), `studyName` (ej. "demo_bodega1_pv_c_f"), `brainless` (booleano).
   - `externalPvInstallations`: `panelModel`, `inclination` (25, se entiende en grados), `azimuth` ("S"), `installedPower` (20, se entiende kWp), `inverterNominalPower` (20).
   - `currentEnergyContractDetails`: `absorptionTariffType`, `injectionTariffType`, arrays `absorption` (2016 elementos) e `injection` (1 elemento).
   - `consumptionMonthWeekdayComb`: 84 elementos, cada uno con `months`, `weekdays` y `data` (24 valores horarios; ejemplo enero-lunes con valores entre 5,0 y 9,0, unidad no especificada en la fuente, probablemente kWh).
   - `energyDevicesPossibilities`: `modelId` (ej. "Buffer120"), `batteryCapacity`, `inverterNominalPower` (100), `chargeMaxPower` (60), `deviceCost`, `inverterCost`, `batteryCost`, `totalCost`, `weight` (1550).
   - `subsidies` (1 elemento), `prices.installationCost` (18400, se entiende €).
3. (no especificado en la fuente): unidades exactas de varios campos numéricos del JSON no se aclaran en la diapositiva.

### 4. Optimización matemática (diapositiva 8)
1. Esquema de flujos de potencia de un inversor híbrido PV-batería con seis variables: $P_{pv-inv}$, $P_{pv-bat}$, $P_{inv-bat}$, $P_{bat-inv}$, $P_{grid}$, $P_{injection}$, $P_{load}$, conectando los nodos PV, batería, inversor, red (grid) y carga (load).
2. Se menciona que existe una función objetivo y unas restricciones (no desarrolladas ni formuladas explícitamente en la diapositiva).
3. Técnicas citadas: Linear Programming / Mixed Integer Linear Programming / Nonlinear Programming.
4. Ventajas señaladas: modelos matemáticos comprensibles y modulares, flexibilidad, existencia de motores de optimización.
5. Herramientas citadas: Pyomo, Python-MIP (motores de optimización en Python); aplicaciones "en la nube": simuladores, comunidades energéticas, Virtual Power Plants (VPPs); mención de Git como herramienta de control de versiones (sin desarrollo).

### 5. Indicadores financieros y criterios de dimensionamiento (diapositiva 9)
1. **VAN (Valor Actual Neto)**: trae a la actualidad flujos de gastos e ingresos futuros del proyecto, estima ganancias brutas menos la inversión inicial. VAN positivo = proyecto viable; representa la ganancia de la empresa en la actualidad si invierte.
2. **TIR (Tasa Interna de Retorno)**: porcentaje de beneficio o pérdida de una inversión.
3. **ROI**: retorno de la inversión, expresado en años.
4. **Independencia energética (%)**: indicador adicional citado sin fórmula.
5. Criterios prácticos de dimensionamiento de batería:
   - Almacenar el excedente fotovoltaico más ciertos kWh de arbitraje; la capacidad concreta depende del fabricante.
   - No infra ni sobredimensionar; centrarse en ciertas estaciones.
   - Puede recomendarse cambiar de tarifa energética o bajar la potencia contratada.
   - Considerar eficiencias de carga y descarga (en la ponencia se simplifican a 1, es decir, sin pérdidas).
   - Establecer un % de SOC mínimo y un % de SOC máximo para evitar degradación excesiva de la batería.

## Datos clave (con página de origen)

- (p. 5) Fórmula del término de exceso de potencia $F_{PD}$ de la Circular 3/2020 de la CNMC, base normativa del peak shaving.
- (p. 5) Resolución de valores de peajes citada en la diapositiva (06/03/2025 sobre la de 04/12/2024, BOE-A-2025-5341) **desactualizada**: sustituir por Resolución de 18/12/2025 (BOE-A-2025-26348), vigente desde 01/01/2026.
- (p. 6) El simulador cubre 84 combinaciones (7 días × 12 meses) de tarifa, producción fotovoltaica y demanda.
- (p. 7) Ejemplo de instalación FV modelada: 20 kWp instalados, inversor de 20 kW nominal, inclinación 25°, azimut sur; coste de instalación de ejemplo 18.400 (unidad no especificada, se entiende €).
- (p. 9) Eficiencias de carga/descarga simplificadas a 1 en esta ponencia por simplicidad, no como recomendación general.
- (p. 9) Indicadores financieros propuestos para evaluar el dimensionamiento: VAN, TIR, ROI, independencia energética (%).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo 7 (estrategia de carga/descarga del almacenamiento) y, de forma tangencial, capítulo 8 (análisis económico) — solo como referencia conceptual de indicadores (VAN/TIR/ROI ya cubiertos con más detalle en otras fuentes del proyecto).
- **Qué aporta exactamente**: la fórmula del término de exceso de potencia ($F_{PD}$) es el único elemento con valor de cita técnica potencial, pero sus valores numéricos de referencia están caducados y deben tomarse de la Resolución CNMC vigente (18/12/2025, BOE-A-2025-26348) antes de usarla en el TFM. El resto del contenido (batería brainless/smart, simulador JSON, optimización matemática) es introductorio y cualitativo, sin desarrollo suficiente para citar cifras o procedimientos propios del TFM.
- **Confianza en los datos**: contenido extraído literalmente de las 10 diapositivas del PDF; ningún dato completado desde memoria del modelo. Como estableció Mario, este documento contiene poco contenido de valor pese a su título — la revisión ejecutiva confirma esa valoración: la aportación real se limita a la fórmula normativa de la p. 5, y esta requiere actualización de valores antes de cualquier uso.

## Notas de procesamiento

Densidad Ejecutiva según el encargo: se leyó el documento completo (10 diapositivas, incluida la portada repetida al final) porque su extensión total es reducida — no fue necesario omitir secciones. El recorte propio del nivel Ejecutivo se aplicó en la profundidad de desarrollo (se resumen los puntos sin expandir cada gráfica más allá de ejes/tendencias descritas) y no en la cobertura de páginas. No se detectaron imágenes con contenido textual adicional no extraíble; los gráficos y capturas de pantalla (diapositivas 3, 4, 6, 7, 8) se describen por ejes y tendencias según lo visible en el PDF.
