---
title: "Análisis comparativo de los tres TFM de referencia ERMA"
tipo: analisis-comparativo
autor: "Análisis derivado (Claude Code), sobre los resúmenes de Arcas 2024, Barrios 2023 y Fernandes 2025"
anio: 2026
densidad: exhaustivo
fecha_resumen: 2026-08-20
fuente_original: "conocimiento fotovoltaico/Referencia/{autoconsumo-industrial-san-martin-pyl, evaluacion-fv-autoconsumo-gran-industria, instalacion-fotovoltaica-centro-logistico-mad9}.md"
tags: [TFM-referencia, ERMA, estructura, metodologia, almacenamiento, autoconsumo, analisis-comparativo, indice]
related: [autoconsumo-industrial-san-martin-pyl, evaluacion-fv-autoconsumo-gran-industria, instalacion-fotovoltaica-centro-logistico-mad9, trabajo-previo-modulo6-cpd]
---

# Análisis comparativo de los tres TFM de referencia ERMA

> **Qué es este documento.** Análisis transversal de los tres TFM de años anteriores indexados en este vault, orientado a extraer patrones de estructura, metodología, presentación de resultados y estilo de redacción aplicables al TFM de Mario Carrión. **No sustituye a los resúmenes individuales**: los complementa con lo que solo se ve al cruzarlos.
>
> **Estatus de citabilidad:** ninguno de los tres TFM es fuente citable (trabajos académicos de otros autores, no publicados). Este análisis tampoco lo es. Su valor es de referencia de formato y de método, y como criterio de decisión sobre el índice.

Documentos analizados:

| Documento | Autor / año | Extensión | Nota de origen |
| --- | --- | --- | --- |
| San Martín PYL (fábrica de placa de yeso) | Manuel Arcas Navarro, 2024 (cotutor: Julio Amador Guerra) | 69 pp. (51 memoria + 18 anexos) | [[autoconsumo-industrial-san-martin-pyl]] |
| Gran industria (complejo anonimizado, CAM) | Andrea Barrios López, 2023 | 132 pp. (96 memoria + 36 anexos) | [[evaluacion-fv-autoconsumo-gran-industria]] |
| Centro logístico Amazon MAD9 | Diego Fernandes Alves, 2025 | 225 pp. (85 memoria + 140 anexos) | [[instalacion-fotovoltaica-centro-logistico-mad9]] |

Línea base propia contra la que se contrasta: [[trabajo-previo-modulo6-cpd]].

---

## 1. Hallazgo principal: cuándo sobrevive el almacenamiento

Es el resultado que solo aparece al cruzar los tres trabajos con la línea base del Módulo 6, y **condiciona directamente el capítulo 7 del TFM**.

| TFM | Generación / consumo | Autosuficiencia | Decisión sobre baterías |
| --- | --- | --- | --- |
| Arcas 2024 | 2.233 / 14.328 MWh = **16 %** | 15,05 % | ❌ Descartado — ninguna estrategia de carga/descarga supera al FV sin batería |
| Barrios 2023 | 2.714 / 8.728 MWh = **31 %** | 30 % | ❌ Descartado — energía excedentaria insuficiente |
| Fernandes (MAD9) 2025 | 4.151 / 4.722 MWh = **88 %** | 77 % | ✅ 2.000 kWh, viable (VAN 4.481.882 €, TIR 15,76 %) |
| **Línea base CPD (M6)** | **166,55 / 1.260 MWh = 13 %** | **13,22 %** | *Pendiente de justificar* |

**Lectura:** el almacenamiento solo supera el filtro económico cuando la generación se aproxima al consumo. La línea base del CPD está en el extremo opuesto, por debajo incluso de Arcas — y Arcas concluyó que la batería no era rentable con un coste de 120 €/kWh y un diferencial P1-P6 de solo el 38 %.

**Consecuencia para el TFM:** la justificación de la batería **no puede venir por excedentes**. Con A_PV = 100 % y *EUnused* ≈ 0, no sobra ni un kWh que almacenar. Las tres vías alternativas, ya identificadas en [[trabajo-previo-modulo6-cpd]], son:

1. **Arbitraje entre periodos de la tarifa 6.1TD** (6 periodos, diferencial P1/P6).
2. **Recorte de punta del término de potencia** (2.300 / 3.300 kW contratados: el término de potencia pesa mucho en la factura).
3. **Respaldo de la carga crítica** del CPD.

Hay que demostrarlo con el modelo horario en Excel, no darlo por supuesto. **Un resultado negativo es un resultado válido y publicable**: es exactamente lo que hicieron Arcas y Barrios, y ambos aprobaron.

---

## 2. Estructura y organización del documento

Ninguno de los tres reproduce literalmente el índice genérico de la guía ERMA: los tres organizan en capítulos temáticos propios y cubren las categorías genéricas de forma implícita. Dos escuelas:

- **Numeración plana** (Arcas, Fernandes): 8-9 capítulos correlativos + anexos. Es lo mayoritario y lo que sigue `Memoria/indice_propuesto.md`.
- **Bloques romanos** (Barrios): `I. Introducción` / `II. Análisis técnico-económico` / `III. Ingeniería básica y conclusiones`, con numeración que reinicia en cada bloque. Refleja un proyecto en dos fases (evaluación preliminar → ingeniería de detalle). **No recomendable** para este TFM: el índice de 13 capítulos ya reparte esa lógica.

Secuencia común a los tres:

```
Introducción (objetivo, alcance, antecedentes, normativa, metodología)
  → Datos de partida (emplazamiento, consumo, recurso solar, restricciones)
  → Tipología de autoconsumo y tramitación
  → Selección de componentes
  → Diseño y simulación PVsyst
  → [Almacenamiento — solo Fernandes lo desarrolla como capítulo propio]
  → Análisis energético (resultados)
  → Análisis económico
  → Conclusiones
  → Bibliografía → Anexos
```

**Extensión.** Los tres están muy por debajo del techo ERMA de 150 páginas: 51, 96 y 85 páginas de memoria. El volumen está en los anexos (18, 36 y 140 páginas). El tribunal no premia memoria larga, sino memoria compacta con anexos que soporten la trazabilidad. El índice propuesto de 13 capítulos apunta a algo más largo que los tres: conviene vigilarlo.

**Anexos.** Estructura idéntica en los tres y coincidente con los Anexos A-E previstos: planos · fichas técnicas · informe PVsyst completo · cálculos eléctricos / flujos de caja.

---

## 3. Metodología: cómo la declaran

Los tres la declaran **explícitamente en la introducción**, como lista numerada de pasos. Es un patrón fuerte del tribunal ERMA; la sección 1.6 del índice debe hacerlo.

| TFM | Formato | Nivel |
| --- | --- | --- |
| Barrios | 12 pasos numerados, muy operativos | El más detallado y transferible |
| Fernandes | 5 fases + **tabla de herramientas software** (PVsyst, AutoCAD, EPLAN, Caneco BT, Excel) | El más claro; declarar herramientas es buena práctica |
| Arcas | No la aísla en apartado propio; se deduce del alcance | El más flojo en este punto |

Criterio de diseño especialmente útil (Barrios, paso 9): *dimensionar hasta alcanzar un ratio de autoconsumo del ~95 %, mediante casación horaria de curvas de demanda y generación*. Es una regla de parada objetiva y defendible, no un "se eligió por criterio del proyectista".

---

## 4. Datos de partida y su tratamiento

- **Consumo:** curva horaria de un año natural completo, verificada contra las facturas mensuales por periodos. Arcas y Fernandes disponen de dato horario real; Barrios lo **reconstruye** (facturas + hábitos + curvas tipo de REE) y lo declara abiertamente. Esa honestidad metodológica es un patrón a imitar cuando el dato no existe.
- **Recurso solar:** los tres comparan bases de datos y **justifican la elección con una tabla**. Arcas y Fernandes eligen Meteonorm (Fernandes documenta ~7,6 % más de irradiación que NASA/PVGIS y lo razona por resolución espacial); Barrios usa PVGIS para el preanálisis y reserva PVsyst para la ingeniería. La elección propia de **PVGIS 5.3** por resolución horaria está mejor argumentada que las de ellos, porque el dato horario es lo que permite cruzar con el consumo.
- **Restricciones del emplazamiento:** aquí divergen. Arcas calcula **cargas de viento según CTE DB-SE-AE** (único de los tres). Barrios documenta Dominio Público Hidráulico del Jarama y zona de influencia AESA. Fernandes deja el **estudio estructural de cubierta como fase pendiente e indispensable** y lo reconoce en conclusiones.
- **Datos económicos de partida:** los tres sitúan el desglose de precio por periodo tarifario en "datos de partida", no en el capítulo económico.

---

## 5. Cómo presentan y documentan los resultados

**Métricas que reportan los tres sin excepción:** potencia pico (kWp) y nominal (kWn) · producción anual (MWh) · producción específica (kWh/kWp) · Performance Ratio · ratio de autoconsumo · ratio de autosuficiencia · CAPEX · ahorro anual · payback · VAN · TIR · LCOE.

Convenciones de presentación:

- **Diagrama de pérdidas de PVsyst reproducido íntegro**, en cascada desde la irradiación horizontal hasta la energía al usuario, con cada pérdida en porcentaje. Los tres lo hacen. Es la prueba de que la simulación se entiende, no solo se ejecuta.
- **P50 / P90** — solo Arcas, con tabla de incertidumbres desglosada (modelado del módulo 1,0 %; eficiencia del inversor 0,5 %; suciedad/mismatch 1,0 %; degradación 1,0 %) y variabilidad global del 4,4 %. Es un plus de rigor diferencial.
- **Comparación explícita de alternativas antes de elegir**, con una fila de tabla por variante: Arcas 3 configuraciones; Barrios 3 propuestas × 3 escenarios de precio; Fernandes **24 configuraciones** (módulos/inversores × 3 capacidades de batería). En los tres casos **la elegida no es la de mejor resultado bruto sino la de mejor compromiso**, y se argumenta: Arcas descarta el terreno mejor orientado por no comprar suelo; Fernandes descarta la batería de 200 kWh — de payback más rápido — porque exige reposición en el año 16.
- **Trazabilidad numérica:** tabla de datos de partida → tabla de resultados intermedios → tabla de resultados finales, más el anexo con el informe PVsyst crudo que permite auditar cada cifra.
- **Flujos de caja a 25 años en anexo**, con la fila de reinversión de equipos visible (Barrios: reposición en el año 15 al 70 % del coste actual).

---

## 6. Redacción académica, nivel de detalle y citación

- **Estilo de citación:** numérico entre corchetes `[1]`, `[2]`…, compatible con **IEEEtran** (ya configurado en este TFM). Nada de autor-año.
- **Volumen bibliográfico bajo:** Barrios cierra con **19 referencias**, Arcas con 15. El tribunal ERMA no espera decenas de referencias.
- **Perfil de las fuentes:** mucha norma (RD, UNE, ITC-BT), mucha fuente institucional (REE, OMIE, IDAE, MITECO, PVGIS, CNMC) y bastante **fuente comercial** (fabricantes, portales sectoriales tipo Selectra o SolarPlack). Este último grupo es el punto débil de los tres: **no imitarlo**; sustituir fuente comercial por norma o fuente institucional siempre que sea posible.
- **Normativa como sección propia** de la introducción, listada íntegra en orden cronológico descendente (Barrios lista ~22 disposiciones).
- **Glosario de abreviaturas y definiciones** al final de la memoria, con definiciones operativas de las métricas clave (ratio de autoconsumo, ratio de autosuficiencia, potencia pico frente a nominal, horas equivalentes). Barrios lo hace especialmente bien: define los términos que después usa cuantitativamente, lo que evita la confusión habitual entre autoconsumo y autosuficiencia.
- **Conclusiones:** viñetas cortas, una por alcance declarado, correspondencia 1:1 con los objetivos. Sin tablas, sin gráficas, sin elementos nuevos. Los tres cierran con **líneas futuras** explícitas, como exige la guía ERMA.
- **Tono:** impersonal y descriptivo ("se elige", "se comparan", "se concluye"). Nivel de detalle: se explica el *porqué* de cada decisión de diseño, no solo el *qué*.

---

## 7. Transferibilidad al TFM, por prioridad

### Alto valor, aplicación directa

| # | Elemento | Origen | Destino en el índice |
| --- | --- | --- | --- |
| 1 | Metodología de **degradación de baterías por ciclos equivalentes** (ecuación propia del autor, delta 3 %/año) y criterio de selección por durabilidad/reposición en vez de rentabilidad estática | Fernandes, cap. 5-6 | **7.4** |
| 2 | **Modelo horario en Excel de estrategias de carga/descarga** (carga desde red en P6, carga con excedentes FV, carga desde generación), cada una con su diagrama lógico | Arcas, cap. 6 | **7.3** y **Anexo E** |
| 3 | **Escenarios de evolución del precio eléctrico a 25 años** (decreciente / base / incremental, sobre curvas de futuros OMIP) + subvención RD 477/2021 como línea de sensibilidad separada | Barrios, cap. II.9 y Anexo I | **8.3** y **8.5** |
| 4 | **Dimensionado eléctrico con ecuaciones explícitas**: módulos máximo/mínimo en serie, ramas en paralelo, sección de cable CC y CA por caída de tensión e intensidad (UNE-EN 50618, UNE HD 60364-5-52) | Barrios, cap. III.2 | **6.3** |
| 5 | **Comparación de bases de datos meteorológicas** en tabla justificativa | Fernandes, cap. 2 | **3.3** (ya resuelto y mejor argumentado) |
| 6 | **Tramitación administrativa con plazos por trámite** + codificación CNMC 31-A y esquema de medida | Barrios cap. II.6 + Fernandes cap. 3 | **Capítulo 4** completo |

### Útil, adaptar con criterio

| # | Elemento | Origen | Destino | Advertencia |
| --- | --- | --- | --- | --- |
| 7 | **Cargas de viento según CTE DB-SE-AE** | Arcas, cap. 3.6 | **3.6** | Fernandes dejó el estudio estructural de cubierta como fase pendiente indispensable. En un CPD la capacidad portante es más crítica que en una nave: decisión de alcance a tomar con el tutor |
| 8 | **Estructura de presupuesto en tres bloques** (materiales / ingeniería y tramitación / mano de obra) con validación cruzada entre presupuesto preliminar por costes unitarios y detallado desde planos | Fernandes, cap. 6 | **8.1** | — |
| 9 | **Capítulo de mantenimiento y garantías**: tabla de periodicidad de tareas + tabla de garantías por equipo | Fernandes, cap. 7 | **Capítulo 10** | Precedente de 2025 que sugiere que el pliego de condiciones sí encaja, al menos como capítulo ligero. Sigue pendiente de confirmar con el tutor |

### No transferible

- La numeración en bloques romanos de Barrios.
- Sus fuentes comerciales como referencia académica.
- Restricciones de emplazamiento atípicas (DPH, AESA) si Tres Cantos no las tiene.

---

## 8. Dos observaciones de alcance

**Ninguno de los tres trata una carga crítica 24/7 con redundancia y SAIs.** Fernandes se acerca (logística 24/7), pero un centro logístico admite interrupción y un CPD no. La sección **3.2 (criticidad y restricciones de operación del CPD)** es la aportación diferencial real del trabajo y no tiene precedente que copiar: hay que construirla desde normativa y bibliografía citable propia.

**El TFM de referencia primario es Fernandes (MAD9), no Arcas.** Arcas fue la referencia más cercana hasta que se indexó MAD9. Hoy el reparto es:

- **Fernandes (MAD9), 2025** — referencia de **arquitectura y resultados esperables**: es el más reciente, el único con almacenamiento realmente dimensionado e implementado, escala comparable y perfil de consumo más parecido (24/7).
- **Arcas, 2024** — referencia de **método de cálculo**: cargas de viento, cálculo de strings, P50/P90, modelo Excel de gestión de batería. Además comparte cotutor (Julio Amador Guerra).
- **Barrios, 2023** — referencia de **tramitación y economía**: procedimiento administrativo con plazos, escenarios de precio, subvenciones, dimensionado eléctrico con ecuaciones.
