---
type: concept
title: "Resúmenes"
created: 2026-08-17
updated: 2026-08-20
status: developing
tags:
  - concept
  - fotovoltaica
  - bibliografia-tfm
  - almacenamiento
  - tfm-referencia
domain: "Fotovoltaica / TFM"
complexity: intermediate
related:
  - "[[perpinan-2013-energia-solar-fotovoltaica]]"
  - "[[arcas-2024-autoconsumo-industrial-san-martin-pyl]]"
  - "[[fernandes-alves-2025-autoconsumo-mad9]]"
  - "[[barrios-2023-evaluacion-fv-autoconsumo-gran-industria]]"
---

# Resúmenes

Nodo de agrupación temática para los cuatro resúmenes técnicos de bibliografía/referencia indexados en el vault del TFM: [[perpinan-2013-energia-solar-fotovoltaica]], [[arcas-2024-autoconsumo-industrial-san-martin-pyl]], [[fernandes-alves-2025-autoconsumo-mad9]] y [[barrios-2023-evaluacion-fv-autoconsumo-gran-industria]]. Relaciona las cuatro fuentes según los temas técnicos que comparten (autoconsumo fotovoltaico industrial, almacenamiento en baterías, simulación con PVsyst, análisis económico, tramitación administrativa), separando lo que es fuente académica citable (Perpiñán) de lo que es solo referencia de metodología y formato (los tres TFM de otros autores).

## Comparativa por fuente

| | [[perpinan-2013-energia-solar-fotovoltaica\|Perpiñán (2013)]] | [[arcas-2024-autoconsumo-industrial-san-martin-pyl\|Arcas (2024) — San Martín PYL]] | [[fernandes-alves-2025-autoconsumo-mad9\|Fernandes Alves (2025) — MAD9]] | [[barrios-2023-evaluacion-fv-autoconsumo-gran-industria\|Barrios (2023) — Gran industria]] |
|---|---|---|---|---|
| Tipo | Libro/manual docente | TFM Máster ERMA UPM | TFM Máster ERMA UPM | TFM Máster ERMA UPM |
| Citable en el TFM de Mario | Sí (fuente primaria) | No | No | No |
| Caso de estudio | Teórico/genérico | Fábrica PYL, San Martín de la Vega | Centro logístico Amazon MAD9 | Complejo industrial anonimizado (CAM) |
| Herramienta de simulación | No usa PVsyst (base teórica) | PVsyst | PVsyst v8.0.13 | PVGIS (preanálisis) / PVsyst previsto |
| Química de batería tratada | Solo plomo-ácido | No especificada (genérica) | Ion-litio (Huawei LUNA2000) | No aplica (almacenamiento descartado) |
| Conclusión sobre almacenamiento | Método de dimensionado por fiabilidad (LLP), sin evaluar rentabilidad | NO rentable en el caso estudiado | SÍ rentable (2.000 kWh óptimo) | Descartado explícitamente (excedente insuficiente) |
| Análisis económico VAN/TIR/LCOE | No | Sí | Sí | Sí (TIR/payback, sin LCOE explícito) |
| Performance Ratio citado | 0,4-0,85 (rango, media UE 0,74) | 0,784 | 0,7061 | No reportado explícitamente |
| Detalle de tramitación administrativa | No aplica | Básico | Básico | Muy detallado (ayuntamiento, CAM, CHT, AESA, CAU, plazos) |

## Temas compartidos

### 1. Autoconsumo fotovoltaico industrial/genérico

Los cuatro tratan, en distinto grado de concreción, el dimensionado de un sistema fotovoltaico para autoconsumo: Perpiñán aporta el marco teórico general (SFCR, geometría solar, célula solar); Arcas, Fernandes Alves y Barrios lo aplican a un caso industrial real (los dos primeros simulados en PVsyst, Barrios con preanálisis en PVGIS).

### 2. Almacenamiento en baterías — el hilo más relevante para el TFM

Es el tema donde las cuatro fuentes divergen de forma más útil para el TFM de Mario (autoconsumo con almacenamiento en un CPD):

- Perpiñán aporta el marco metodológico de fiabilidad (método LLP) pero solo para plomo-ácido, sin evaluar rentabilidad económica.
- Arcas concluye que el almacenamiento NO es rentable en su caso (bajo diferencial tarifario P1-P6, batería a 120 €/kWh).
- Fernandes Alves sí encuentra un tamaño de batería rentable (2.000 kWh, ion-litio) y aporta un método propio de degradación por ciclos equivalentes, más cercano en tecnología (ion-litio) a lo previsto para el CPD.
- Barrios descarta la hibridación con baterías en sus tres propuestas, pero por un motivo distinto al de Arcas: no por diferencial tarifario, sino porque el diseño se ajusta deliberadamente a un ratio de autoconsumo del 95%, dejando muy poco excedente que rentabilizar.

Contrastar estas cuatro conclusiones (marco teórico sin evaluación económica → no rentable → sí rentable → descartado por diseño) es un punto de partida útil para justificar por qué el resultado del TFM de Mario puede diferir de los tres casos de referencia, en función del perfil de consumo, el diferencial tarifario y el criterio de dimensionado propios del CPD.

### 3. Simulación con PVsyst

Arcas y Fernandes Alves usan PVsyst para comparar configuraciones (orientaciones de tejado en Arcas; combinaciones de módulos/inversores/batería en Fernandes Alves). Barrios usa PVGIS para el preanálisis de las tres propuestas y reserva PVsyst para la fase de ingeniería de detalle (no incluida en el documento). Perpiñán no usa PVsyst, pero su capítulo 6 (SFCR) describe la física que PVsyst modela internamente — útil para entender e interpretar los resultados de simulación de las otras fuentes, no para reemplazarlos.

### 4. Análisis económico (VAN, TIR, LCOE, payback)

Arcas y Fernandes Alves calculan VAN/TIR/LCOE/payback con estructuras de cálculo comparables. Barrios calcula TIR y payback bajo tres escenarios de evolución de precios de mercado eléctrico a 25 años (decreciente/base/incremental) combinados con la subvención RD 477/2021 como línea de sensibilidad adicional — la estructura de análisis de sensibilidad más desarrollada de las tres fuentes, útil como plantilla para el capítulo 8 de Mario. Perpiñán no incluye análisis económico de ningún caso — su aportación es exclusivamente física y de dimensionado.

### 5. Performance Ratio

Perpiñán, Arcas y Fernandes Alves dan una cifra de PR que sirve de contraste de plausibilidad: el rango general de Perpiñán (0,4-0,85, media UE 0,74) enmarca los valores puntuales de Arcas (0,784) y Fernandes Alves (0,7061, penalizado por pérdidas de proceso de almacenamiento AC-coupling) — ambos dentro de rango, lo que valida su plausibilidad sin necesidad de recalcularlos. Barrios no reporta un PR explícito en el resumen (documento centrado en energía anual y ratios de autoconsumo/autosuficiencia, no en PR como métrica destacada).

### 6. Tramitación administrativa

Barrios es, con diferencia, la fuente más exhaustiva en este punto: detalla el procedimiento completo de legalización (ayuntamiento, Comunidad de Madrid, Confederación Hidrográfica del Tajo por proximidad al Dominio Público Hidráulico del río Jarama, AESA por zona de influencia aeroportuaria, CAU, Registro de Autoconsumo) con plazos orientativos por trámite. Arcas y Fernandes Alves tratan la tramitación de forma más básica. Útil como referencia principal para el capítulo de tipología de autoconsumo y tramitación del índice de Mario, aunque las restricciones administrativas atípicas de Barrios (Dominio Público Hidráulico, zona aeroportuaria) solo aplican si el CPD tiene restricciones similares.

## Uso en el TFM

- Perpiñán es la única fuente citable de las cuatro: usar para justificar hipótesis físicas y el marco metodológico LLP (regla 10 de `CLAUDE.md`).
- Arcas, Fernandes Alves y Barrios NO son citables: solo sirven como referencia de estructura, metodología de cálculo y orden de magnitud — contrastando explícitamente sus conclusiones distintas sobre la rentabilidad del almacenamiento antes de fijar la metodología propia del capítulo 7, y usando Barrios como referencia principal de tramitación y dimensionado eléctrico.

## Relacionado

- [[perpinan-2013-energia-solar-fotovoltaica]] — fuente citable primaria
- [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] — TFM de referencia, no citable
- [[fernandes-alves-2025-autoconsumo-mad9]] — TFM de referencia, no citable
- [[barrios-2023-evaluacion-fv-autoconsumo-gran-industria]] — TFM de referencia, no citable
