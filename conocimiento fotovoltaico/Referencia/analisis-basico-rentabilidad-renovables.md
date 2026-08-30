---
title: "Análisis básico de rentabilidad de instalaciones renovables"
tipo: presentacion
autor: "Miguel Duvison Santiago (Repsol Renovables)"
anio: 2025
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T12_AnalisisRentabilidadI.pdf"
tags: [fotovoltaica, autoconsumo, rentabilidad, VAN, TIR, WACC, fiscalidad, tarifas-acceso, PPA, capex, opex]
related: []
---

# Análisis básico de rentabilidad de instalaciones renovables (Miguel Duvison Santiago, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA (20ª edición, 2025-2026), impartida por Miguel Duvison Santiago (Repsol Renovables) el 16/12/2025. Desarrolla el modelo básico de evaluación económica de proyectos de energías renovables: estructura de inversión (CAPEX) y gastos (OPEX) con valores de referencia €/kWp, modalidades de ingresos (venta a mercado, PPA en sus variantes onsite/offsite, subastas, autoconsumo), fiscalidad específica del sector (peaje de colocación, impuesto sobre el valor de la producción, impuesto eléctrico al consumo), metodología de cálculo del coste de capital (WACC vía CAPM) y los indicadores clásicos de rentabilidad (PRI, VAN, TIR). Dedica un bloque a los términos económicos específicos del autoconsumo bajo RD 244/2019 (compensación de excedentes, autoconsumo con excedentes sin compensación) y a la estructura vigente de tarifas de acceso (2.0TD, 3.0TD, 6.XTD). Cierra con dos casos prácticos remitidos a hoja de cálculo externa (no incluida en el PDF): instalación de 239 kWp en industria agroalimentaria y de 7,63 MWp en industria automovilística.

## Contenido técnico

### 1. Índice de contenidos (p. 2)

- Modelo básico de evaluación económica de proyectos renovables: Inversión, Ingresos, Gastos, Fiscalidad, Coste de capital, Flujos de caja libre, Payback/VAN/TIR.
- Términos económicos específicos autoconsumo PV (RD 244/2019).
- Casos prácticos: instalación PV de 239 kWp (industria agroalimentaria) e instalación PV de 7,63 MWp (industria automovilística).

### 2. Inversión — CAPEX (p. 3-4)

Partidas de inversión (€/kWp):
- Central solar fotovoltaica: módulos, inversores, seguidores, estructura soporte, interconexión.
- Sistemas eléctricos de interconexión.
- Sistemas de almacenamiento.
- Refuerzo estructural de cubierta.
- Instalación y PEM (Puesta en Marcha).
- Ingeniería.
- Dirección de obra.
- Coordinación de Seguridad y Salud (SyS).

**Referencia CAPEX planta autoconsumo FV pequeña escala: 800-1200 €/kWp.** Puede situarse en **600-700 €/kWp** para mayor escala.

**Desglose de inversión en plantas PV de mayor escala** (gráfico circular, p. 4):

| Partida | % del CAPEX |
|---|---|
| Módulos | 28% |
| Seguidor | 16% |
| Auxiliares de planta | 14% |
| SET + LAT | 11% |
| Otros equipos (cables BT, MT, cajas de conexión, etc.) | 11% |
| Inversores | 8% |
| Conexión | 5% |
| Tasas | 3% |
| Ingeniería y Dirección de Obra | 2% |
| Otros CAPEX | 1% |
| DEVEX | 1% |

### 3. Ingresos (p. 5-10)

- **Producción de planta**: fundamental una buena estimación; el dimensionamiento debe adaptarse al perfil de demanda de la instalación consumidora en el caso de autoconsumo FV.

**Modalidad de explotación — Venta a mercado** (p. 5): clave la previsión de precio de venta. Ejemplo con OMIP y previsión de dos consultores para España, horizonte 2025-2031:

| Concepto | Unidad | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---|---|---|---|---|---|---|---|
| Futuros OMIP (Ref. 16/12/25) | €/MWh | 56,73 | 54,95 | 55,45 | 55,30 | 55,30 | 55,30 | 55,30 |
| Apuntamiento tecnológico solar FV a considerar (elaboración propia) | % | 49,5 | 48,4 | 51 | 51,1 | 53,9 | 56 | 52,3 |
| Capturado Solar OMIP | €/MWh | 28,08 | 26,60 | 28,28 | 28,26 | 29,81 | 30,97 | 28,92 |
| Capturado Solar Consultor 1 CENTRAL | €/MWh | 33,21 | 33,33 | 35,85 | 40,31 | 46,29 | 49,78 | 45,43 |
| Capturado Solar Consultor 1 LOW | €/MWh | 28,07 | 24,94 | 25,00 | 27,16 | 30,65 | 32,98 | 34,11 |

Fuente citada en diapositiva: https://www.omip.pt/es

**Modalidad de explotación — PPA (Power Purchase Agreement)** (p. 6-9): se definen por duración (5, 10, 15 años), ubicación de la instalación (*offsite*/*onsite*), forma de entrega de la energía y estabilidad de precio como cobertura ante la volatilidad; predictibilidad al colocar P50.

- **Onsite**: instalación conectada al cliente. Autoconsumo con o sin excedentes.
- **Offsite**: instalación alejada del cliente; la energía se vende a mercado y se liquida por diferencias. Dos tipos:
  - **Físico**: el desarrollador vende la energía generada a un cliente final a través de una comercializadora. Cualquier desviación en la producción renovable y el resto de energía demandada por el cliente es cubierta por la cartera de la comercializadora. El consumidor recibe una única factura (instalación renovable con PPA + spot que hubiera necesitado).
  - **Virtual**: el consumidor negocia directamente con el desarrollador el precio del PPA, y contrata su suministro eléctrico con una comercializadora distinta. Recibe dos facturas: una de la comercializadora (consumo físico) y otra del desarrollador (ajuste por diferencias entre precio spot y precio del PPA acordado). Las Garantías de Origen (GdO) se transfieren al cliente final.

Formas de entrega de energía en modalidad offsite:
- **As generated / Pay as Produced (PAP)** (p. 7): el cliente final consume la generación total de la planta. Modalidad más competitiva en precio pero más arriesgada por la impredecibilidad de la producción renovable. Se muestran dos gráficas "Curva PAP" (eje X: horas 1-24, eje Y: potencia sin unidad explícita en el eje pero del orden de miles): en la primera, consumo cliente estable ~11.000-11.700 (línea plana), producción solar FV con forma de campana centrada en horas 10-16 (pico ~6.000); en la segunda, consumo cliente ~30.000-35.000 con leve caída a media mañana, producción eólica no mostrada, solar FV con pico moderado ~8.000-10.000 entre horas 18-22 (perfil distinto, posiblemente error de leyenda o mezcla de fuentes).
- **Base load** (p. 8): el productor convierte la generación del parque en una carga base combinando diferentes instalaciones de su porfolio. Es la modalidad más común por el equilibrio entre precio y riesgo. Gráfica "Cobertura BL": consumo cliente constante en barras (~13.000, horas 1-24); curva eólica (roja) con valle en horas 9-15 (~18.000) y máximos en extremos (~24.500); curva solar FV (naranja) con pico en horas 10-16 (~30.000-31.500) y mínimo en extremos (~24.000).
- **As consumed** (p. 9): el productor convierte la generación del parque en una curva que sigue fielmente el consumo del cliente. Es el producto más común entre consumidores no expertos y donde el productor aporta mayor valor añadido; es la opción más cara para el cliente final. Gráfica: consumo cliente en área azul con forma de campana (mínimo ~4.000-5.000 en horas nocturnas, máximo ~14.000 en horas 10-19); curva eólica (roja) en forma de "U" invertida al consumo (máximo ~21.000 en horas nocturnas, mínimo ~17.500 en horas centrales); curva solar FV (naranja) con pico ~28.000-29.000 en horas 10-16. Referencia normativa citada en la diapositiva: RDL 24/2020 como marco legal de referencia.

**Modalidad de explotación — Subastas** (p. 10): orientadas al cumplimiento del PNIEC y a la eficiencia en costes. Mecanismos: convocatorias por tecnología, contratos por diferencias. Fuente: https://energia.gob.es/renovables/regimen-economico/Paginas/index-subastas-regimen-economico.aspx

**Modalidad de explotación — Autoconsumo** (p. 10): evaluación mediante coste evitado y adaptación de la producción a la demanda. Fuentes/hitos de mercado citados en la diapositiva:
- 2021: se instalan 1.151 MW de autoconsumo en España, casi el doble que el año anterior (El Periódico de la Energía).
- 2022: España duplica el autoconsumo solar, instala más de 2.500 MW (El Periódico de la Energía).
- 2023: se instalaron en España 1.706 MW de autoconsumo fotovoltaico (UNEF).
- UNEF propone medidas urgentes para impulsar el autoconsumo, que sigue cayendo (UNEF, sin fecha específica indicada en la diapositiva).
- 2025: Red Eléctrica incorpora información de autoconsumo fotovoltaico en todas sus plataformas de datos → **8,7 GW instalados** (REE).

### 4. Gastos — OPEX (p. 11-12)

Costes de O&M de la instalación:
- Mantenimiento correctivo (planificado y no planificado).
- Mantenimiento preventivo.
- Mantenimiento predictivo → maximización de la disponibilidad.
- Limpieza: reduce producción por ensuciamiento; su ausencia aumenta la degradación por generación de puntos calientes.
- Mantenimiento legal.

**Referencia OPEX planta autoconsumo PV de pequeña escala: 8-10 €/kWp**, que puede situarse en **15-17 €/kWp** para mayor escala.

**Desglose de gastos operativos en plantas PV de mayor escala** (gráfico circular, p. 12):

| Partida | % del OPEX |
|---|---|
| O&M Planta | 40% |
| Impuestos locales | 26% |
| Terrenos | 15% |
| Personal y gestión del parque | 8% |
| Otros (seguros, servicios, suministros) | 7% |
| O&M Evacuación | 3% |
| SCADA, Sistemas y comunicaciones | 1% |

### 5. Fiscalidad (p. 13-14)

**Peaje de colocación de la energía eléctrica en la red por parte de los generadores** (p. 13): vigente desde 2011 mediante el Real Decreto 1544/2011, que fijaba el peaje de acceso a redes de transporte y distribución para instalaciones de generación, conforme a la Ley del Sector Eléctrico (Ley 54/1997) y en el contexto del Real Decreto-ley 14/2010 (medidas de corrección del déficit tarifario), aplicable a toda instalación de generación desde el 1 de enero de 2011, con un valor de **0,5 €/MWh** (valor máximo aplicable según normativa europea). Desde el 24 de enero de 2020, en aplicación del artículo 2 de la Circular 3/2020, de 15 de enero, de la CNMC (metodología de cálculo de peajes de transporte y distribución), **los productores de energía quedaron exceptuados del pago de peajes por la energía inyectada a las redes**. Debe considerarse no obstante el coste asociado al pago del peaje al Operador del Sistema (OS) y al Representante de mercado, como referencia: **0,28 €/MWh**.

**Impuesto sobre el valor de la producción de energía eléctrica (IPVEE)** (p. 14): establecido en la Ley 15/2012, de 27 de diciembre, con tipo de gravamen del **7%** sobre el importe que corresponda percibir al sujeto pasivo por la producción e incorporación al sistema eléctrico de energía eléctrica. Suspendido temporalmente desde el tercer trimestre de 2021 hasta el 31 de diciembre de 2023 (última actualización: RDL 20/2022, de 27 de diciembre). Con el RDL 8/2023, durante el primer trimestre de 2024 el tipo se situó en el 3,5%, durante el segundo trimestre en el 5,25%, y **desde el tercer trimestre de 2024 se recupera el tipo impositivo anterior a las medidas, estabilizándose en un 7%**.

> **Nota de vigencia (verificada contra `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`, 2026-08-30):** el tipo del 7% del IPVEE sigue vigente a la fecha de este resumen.

**Impuesto eléctrico al consumo** (p. 14): procedente de la Ley 38/1992, de Impuestos Especiales, modificada en 2015 (Ley 28/2014, de 27 de noviembre), con un tipo del **5,11269632%**. Reducido temporalmente al 0,5% hasta el 31 de diciembre de 2023 (RDL 20/2022). Con el RDL 8/2023, durante 2024 el impuesto ascendió de forma progresiva: del 1 de enero al 31 de marzo de 2024, tipo del 2,5%; del 1 de abril al 30 de junio de 2024, tipo del 3,8%; **el 1 de julio de 2024 volvió a subir, recuperando su valor original del 5,11%**.

> **Nota de vigencia (verificada contra `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`, 2026-08-30):** el tipo del 5,11269632% del impuesto eléctrico al consumo sigue vigente a la fecha de este resumen.

**Nota al pie 1 de la diapositiva 14** (sobre distancia del autoconsumo a través de red): "En este mismo RD también se promulga el impulso al autoconsumo a través de la red, incrementando la distancia entre las instalaciones de autoconsumo y las plantas generadoras hasta los 2.000 metros (anteriormente 1.000 m desde el RDL 18/2022 del 18 de octubre, que amplió los 500 m originales del RD 244/2019) en casos de plantas generadoras fotovoltaicas ubicadas no sólo en cubiertas, sino también en suelo industrial y estructuras artificiales destinadas a otros usos (ej. aparcamiento)."

> **Nota de actualización de vigencia (2026-08-30) — no es un error de la diapositiva, es correcta para su fecha (RDL 20/2022):** la progresión histórica del umbral de distancia del autoconsumo a través de red descrita en la p. 14 es: 500 m originales (RD 244/2019) → 1.000 m con el RDL 18/2022, de 18 de octubre → 2.000 m con el RDL 20/2022, de 27 de diciembre. Posteriormente, el **RDL 7/2026** sustituyó de nuevo este umbral, ampliándolo a **5.000 m para instalaciones fotovoltaicas y eólicas de potencia ≤5 MW, sin restricción de ubicación**. Este dato de vigencia 2026 no figura en la fuente original (presentación de diciembre de 2025) y se añade aquí como contexto normativo actualizado para su uso en el TFM — verificar el articulado del RDL 7/2026 antes de citarlo en la memoria (regla de fuente primaria del proyecto).

### 6. Evaluación del coste de capital (p. 15-18)

**Tasa libre de riesgo ($T_{LR}$)** (p. 15): se basa en el concepto económico teórico de una alternativa de inversión sin riesgo para el inversionista, que ofrece un rendimiento seguro en un plazo determinado, sin riesgo crediticio ni riesgo de reinversión, ya que pasado el plazo se dispondrá del efectivo con la tasa de generación de valor comprometida.

**Prima de riesgo de mercado ($P_{RM}$)**: diferencia en la tasa de interés que un inversor paga al asumir una determinada inversión, con una fiabilidad económica menor que aquella cuya prima es cero (por asumir cierto riesgo). Dichas primas suelen oscilar **entre el 3% y el 10%**.

**Beta (apalancada y desapalancada)** (p. 16): el coeficiente beta mide la volatilidad de un activo en relación a la variabilidad del mercado; constituye una medida de la evolución del activo respecto a los movimientos del mercado. Valores elevados de beta denotan más volatilidad; beta = 1 supone equivalencia con el mercado. La beta mide un riesgo sistémico (no eliminable, inherente a la naturaleza del activo).

En proyectos con financiación asociada (deuda), es necesario incorporar el riesgo financiero mediante la **beta apalancada** $\beta_L$:

$$\beta_L = \beta_U \cdot \left(1 + \left(A \cdot (1 - T_f)\right)\right)$$

**Beta desapalancada** (p. 17): el valor de $\beta_U$ del activo se obtiene de referencias disponibles, citando explícitamente **[Damodaran]** como fuente. La tasa fiscal $T_f$ es del **25%** para España (valor "actualmente", según la diapositiva). El apalancamiento $A$ se define como el nivel de endeudamiento $E$:

$$A = \frac{E}{1-E}$$

Conocidos estos valores, el **coste de capital propio o rentabilidad exigida a las acciones** $K_e$:

$$K_e = T_{LR} + \beta_L \cdot P_{RM}$$

**Coste de la deuda** (p. 18): se calcula a partir del coste de la deuda en los mercados $C_{dm}$:

$$K_d = C_{dm} \cdot (1 - T_f)$$

**WACC (Weighted Average Cost of Capital)**:

$$WACC = K_e \cdot (1-E) + K_d \cdot E$$

### 7. Flujos de caja libre (p. 19)

Obtención de los FCF: remitida explícitamente a "hoja de cálculo" externa no incluida en el PDF de la presentación (no especificado en la fuente).

### 8. Indicadores de evaluación de la rentabilidad (p. 20)

- **Período de Retorno de la Inversión (PRI)**: mide en cuánto tiempo se recuperará el total de la inversión a valor presente.
- **Valor Actual Neto (VAN)**: actualiza los cobros y pagos de un proyecto o inversión ($I_0$) para conocer cuánto se va a ganar o perder con la misma, trayendo todos los flujos de caja ($F_t$) durante el tiempo de evaluación ($t$) al momento presente, descontados a un tipo de interés determinado (tasa de descuento $k$). Expresa una medida de rentabilidad del proyecto en términos absolutos netos (nº de unidades monetarias):

$$VAN = -I_0 + \sum_{t=1}^{n} \frac{F_t}{(1+k)^t} = -I_0 + \frac{F_1}{(1+k)} + \frac{F_2}{(1+k)^2} + \cdots + \frac{F_n}{(1+k)^n}$$

- **Tasa Interna de Rentabilidad (TIR)**: corresponde con la tasa $k$ que hace VAN = 0. Constituye un indicador importante de la rentabilidad intrínseca de la inversión, independientemente de la exigencia marcada por el WACC.

### 9. Términos económicos específicos de instalaciones de autoconsumo — RD 244/2019 (p. 21-22)

**Sistemas con compensación de excedentes** (p. 21):
- La compensación de pagos se hace **mensualmente**, sobre el término de energía, y este **nunca podrá ser negativo**.
- Los excedentes que no se compensen en el período mensual **se perderán**.
- Precio pagado por la energía excedentaria:
  - Con comercializadora libre: **precio pactado**.
  - Con comercializadora de referencia: **precio medio horario menos coste del sistema**.
- Los excedentes compensados **no pagan peajes de generación** (cuando aplicaba) **ni el impuesto sobre el valor de la producción de la energía eléctrica del 7%** (en el caso de estar vigente).

**Autoconsumo con excedentes sin compensación** (p. 22):
- Los ingresos corresponden con el precio del mercado, descontando los gastos de la comercializadora, peajes e impuestos.
- La energía horaria excedentaria opera como una instalación de venta a red.
- Se valora el excedente al precio horario del mercado.
- Es necesario darse de alta como productor y operar mediante un representante.
- La energía excedentaria debe satisfacer el peaje de generación (cuando aplicaba) y el impuesto de generación del 7% (en el caso de estar vigente).
- En todos los casos las cantidades a facturar se realizan **antes de impuestos**, esto es, antes del impuesto eléctrico al consumo y antes del IVA.

### 10. Tarifas de acceso (p. 23-25)

**Uso doméstico (baja tensión, P<15 kW): tarifas 2.X** (p. 23):
- 2.0 — hasta 10 kW.
- 2.1 — entre 10 y 15 kW.
- Históricamente, en función del peaje de acceso:
  - 2.0A y 2.1A — único peaje de acceso durante todo el día (sin discriminación horaria).
  - 2.0DHA y 2.1DHA — discriminación horaria en dos períodos (dos peajes de acceso).
  - 2.0DHS y 2.1DHS — discriminación horaria en tres períodos (tres peajes de acceso).
- Desde el **01/06/2021**, las seis opciones anteriores se condensan en una única tarifa, la **2.0TD**, con tres términos de energía y dos de potencia.

Franjas horarias tarifa de acceso 2.0TD (Península, Baleares y Canarias):

| Punta | Llano | Valle |
|---|---|---|
| 10:00-14:00 | 08:00-10:00 | 00:00-08:00 |
| 18:00-22:00 | 14:00-18:00 | — |
| — | 22:00-00:00 | — |

Fines de semana y festivos → Valle. Periodificación de potencia 2.0TD: dos períodos, Punta y Valle (lunes a viernes laborables → Punta/Valle según hora; sábados, domingos y festivos → Valle todo el día, según diagramas circulares de la diapositiva).

**Uso comercial e industrial** (p. 24-25): **3.0TD** (baja tensión, P>15 kW) y **6.XTD** (alta tensión, P>15 kW; "X" según nivel de tensión de conexión). 4 temporadas eléctricas, 6 peajes para el término de energía, 6 peajes para el término de potencia.

Peajes y tensiones 6.XTD:

| Tarifa | Tensión |
|---|---|
| 6.1TD | 1-30 kV |
| 6.2TD | 30-72,5 kV |
| 6.3TD | 72,5-145 kV |
| 6.4TD | Superior a 145 kV |

Temporadas eléctricas por mes y zona (p. 24; niveles: BAJA, MEDIA, MEDIA-ALTA, ALTA):

| Mes | Península | Canarias | Baleares |
|---|---|---|---|
| Enero | ALTA | MEDIA | MEDIA |
| Febrero | ALTA | MEDIA | MEDIA |
| Marzo | MEDIA-ALTA | MEDIA | BAJA |
| Abril | BAJA | BAJA | BAJA |
| Mayo | BAJA | BAJA | MEDIA-ALTA |
| Junio | MEDIA | BAJA | ALTA |
| Julio | ALTA | ALTA | ALTA |
| Agosto | MEDIA | ALTA | ALTA |
| Septiembre | MEDIA | ALTA | ALTA |
| Octubre | BAJA | ALTA | MEDIA-ALTA |
| Noviembre | MEDIA-ALTA | MEDIA-ALTA | BAJA |
| Diciembre | ALTA | MEDIA-ALTA | MEDIA |

Diagramas circulares "Península — Horarios según la temporada" (p. 24) muestran 5 periodos de energía P1-P6 (de más cara a más barata) distribuidos por hora del día para cada temporada (ALTA, MEDIA-ALTA, MEDIA, BAJA, y SÁBADO/DOMINGO/FESTIVO), sin valores numéricos legibles adicionales a los ya recogidos en la tabla horaria de la p. 25.

**Tabla completa de periodos horarios por mes (año de referencia 2022, tarifa 6.XTD)** (p. 25) — periodos P1 (más caro) a P6 (más barato), aplicables hora a hora; transcripción íntegra de la tabla (columnas = horas 1 a 24, agrupadas en franjas horarias de la cabecera 0-1, 1-2, ..., 23-24):

| Mes | Inicio | Fin | 0-1 | 1-2 | 2-3 | 3-4 | 4-5 | 5-6 | 6-7 | 7-8 | 8-9 | 9-10 | 10-11 | 11-12 | 12-13 | 13-14 | 14-15 | 15-16 | 16-17 | 17-18 | 18-19 | 19-20 | 20-21 | 21-22 | 22-23 | 23-24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Enero | 01/01/2022 | 31/01/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 |
| Febrero | 01/02/2022 | 28/02/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 |
| Marzo | 01/03/2022 | 31/03/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 3 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 3 | 3 |
| Abril | 01/04/2022 | 30/04/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 |
| Mayo | 01/05/2022 | 31/05/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 |
| Junio | 01/06/2022 | 30/06/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 |
| Julio | 01/07/2022 | 31/07/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 |
| Agosto | 01/08/2022 | 31/08/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 |
| Septiembre | 01/09/2022 | 30/09/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 |
| Octubre | 01/10/2022 | 31/10/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 |
| Noviembre | 01/11/2022 | 30/11/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 3 | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 3 | 3 |
| Diciembre | 01/12/2022 | 31/12/2022 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 2 |

*(Nota de fidelidad: la tabla de la p. 25 se transcribe a partir de una imagen de resolución limitada; los dígitos 1-6 se han podido distinguir con claridad razonable, pero se recomienda contrastar contra el original en PDF antes de usar estos valores para un cálculo del TFM que dependa de la periodificación horaria exacta.)*

### 11. Casos prácticos (p. 26-27)

- **Caso 1**: instalación PV de **239 kWp** en industria agroalimentaria — remitido a "hoja de cálculo" externa, no incluida en el PDF (no especificado en la fuente).
- **Caso 2**: instalación PV de **7,63 MWp** en industria automovilística — remitido a "hoja de cálculo" externa, no incluida en el PDF (no especificado en la fuente).

### 12. Cierre (p. 28)

Diapositiva de agradecimiento con contactos del autor: miguel.duvison@repsol.com / mduvison@gmail.com.

## Datos clave (con página de origen)

- CAPEX referencia pequeña escala (p. 3): 800-1.200 €/kWp; a mayor escala: 600-700 €/kWp.
- OPEX referencia pequeña escala (p. 11): 8-10 €/kWp; a mayor escala: 15-17 €/kWp.
- Desglose CAPEX mayor escala (p. 4): módulos 28%, seguidor 16%, auxiliares planta 14%, SET+LAT 11%, otros equipos 11%, inversores 8%, conexión 5%, tasas 3%, ingeniería+DO 2%, otros CAPEX 1%, DEVEX 1%.
- Desglose OPEX mayor escala (p. 12): O&M planta 40%, impuestos locales 26%, terrenos 15%, personal/gestión 8%, otros (seguros/servicios/suministros) 7%, O&M evacuación 3%, SCADA 1%.
- Futuros OMIP 2026 (p. 5): 56,73 €/MWh; capturado solar OMIP 2026: 28,08 €/MWh (apuntamiento tecnológico 49,5%).
- Peaje de colocación histórico (p. 13): 0,5 €/MWh (RD 1544/2011), exonerado para generadores desde 24/01/2020 (Circular 3/2020 CNMC); coste de referencia OS+Representante: 0,28 €/MWh.
- IPVEE (p. 14): 7% (Ley 15/2012), suspendido Q3-2021 a Q4-2023, recuperado al 7% desde Q3-2024 — vigente en 2026 según NormativaLinks.xlsx.
- Impuesto eléctrico al consumo (p. 14): 5,11269632% (Ley 38/1992 mod. Ley 28/2014), reducido a 0,5% hasta 31/12/2023, recuperado a 5,11% desde 01/07/2024 — vigente en 2026 según NormativaLinks.xlsx.
- Progresión umbral distancia autoconsumo a través de red (p. 14, nota al pie): 500 m (RD 244/2019) → 1.000 m (RDL 18/2022) → 2.000 m (RDL 20/2022) → **5.000 m sin restricción de ubicación para FV/eólica ≤5MW (RDL 7/2026, dato añadido en este resumen, no en la fuente original)**.
- Tasa fiscal España para cálculo de WACC (p. 17): 25%.
- Prima de riesgo de mercado (p. 15): rango habitual 3%-10%.
- Tarifa 2.0TD vigente desde 01/06/2021 (p. 23), sustituye a las 6 tarifas 2.X anteriores.
- Umbral doméstico 2.0/2.1 (p. 23): hasta 10 kW / entre 10 y 15 kW.
- Umbral 3.0TD/6.XTD (p. 24): P>15 kW, baja tensión / alta tensión.
- 8,7 GW de autoconsumo instalados en España según REE (p. 10, dato de 2025).
- 1.706 MW de autoconsumo instalados en España en 2023 según UNEF (p. 10).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo de análisis económico (VAN, TIR, LCOE, sensibilidad — ver `analista-economico`); capítulo de marco regulatorio/fiscalidad del autoconsumo; capítulo de tarifas de acceso aplicables al modelo horario de consumo del CPD.
- **Qué aporta exactamente**: fórmulas canónicas de WACC/CAPM (beta apalancada, coste de capital propio, coste de la deuda) para justificar la tasa de descuento del VAN del TFM; valores de referencia de CAPEX/OPEX por kWp útiles como banda de contraste frente al presupuesto real del proyecto; reglas exactas de compensación de excedentes bajo RD 244/2019 (mensual, nunca negativa, no acumulable) relevantes para el dimensionado de la variante de autoconsumo con excedentes; tipos impositivos vigentes (IPVEE 7%, impuesto eléctrico al consumo 5,11269632%) para el modelo Excel de flujos de caja; tabla completa de periodificación horaria 6.XTD (p. 25) potencialmente útil para modelar el coste de energía del CPD si su tarifa de acceso es 6.1TD (ver memoria `project_peaje_61tda_2026`).
- **Confianza en los datos**: todas las cifras están tomadas literalmente de la diapositiva y su página se referencia arriba. La nota de vigencia sobre el umbral de distancia (RDL 7/2026) y la confirmación de vigencia de los dos impuestos fueron aportadas por el encargo del equipo (contrastadas contra `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`) y no están en el PDF original — están señaladas explícitamente como tal, no mezcladas con el contenido original de la fuente. Los valores de la tabla de periodificación horaria (p. 25) se transcriben con una advertencia de fidelidad por la resolución de la imagen fuente.

## Notas de procesamiento

Documento leído íntegro (28 pp., densidad exhaustiva, dos tandas de lectura: pp. 1-14 y pp. 15-28). No hay anexos ni apéndices adicionales al final del documento. Las dos diapositivas de "caso práctico" (pp. 26-27) remiten a una hoja de cálculo externa no incluida en el PDF; no se dispone de su contenido y no se ha inventado ningún dato al respecto. Las gráficas de las pp. 7-9 (curvas PAP, Base Load, As Consumed) se han descrito por ejes y tendencia visual; no llevan unidades explícitas en el eje Y de la fuente. La tabla horaria de la p. 25 se transcribió por lectura visual de una tabla con separación de color por periodo tarifario; se advierte fidelidad limitada por resolución de imagen.
