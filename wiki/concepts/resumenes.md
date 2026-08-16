---
type: concept
title: "Resúmenes"
created: 2026-08-17
updated: 2026-08-17
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
---

# Resúmenes

Nodo de agrupación temática para los tres resúmenes técnicos de bibliografía/referencia indexados en el vault del TFM: [[perpinan-2013-energia-solar-fotovoltaica]], [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] y [[fernandes-alves-2025-autoconsumo-mad9]]. Relaciona las tres fuentes según los temas técnicos que comparten (autoconsumo fotovoltaico industrial, almacenamiento en baterías, simulación con PVsyst, análisis económico), separando lo que es fuente académica citable (Perpiñán) de lo que es solo referencia de metodología y formato (los dos TFM de otros autores).

## Comparativa por fuente

| | [[perpinan-2013-energia-solar-fotovoltaica\|Perpiñán (2013)]] | [[arcas-2024-autoconsumo-industrial-san-martin-pyl\|Arcas (2024) — San Martín PYL]] | [[fernandes-alves-2025-autoconsumo-mad9\|Fernandes Alves (2025) — MAD9]] |
|---|---|---|---|
| Tipo | Libro/manual docente | TFM Máster ERMA UPM | TFM Máster ERMA UPM |
| Citable en el TFM de Mario | Sí (fuente primaria) | No | No |
| Caso de estudio | Teórico/genérico | Fábrica PYL, San Martín de la Vega | Centro logístico Amazon MAD9 |
| Herramienta de simulación | No usa PVsyst (base teórica) | PVsyst | PVsyst v8.0.13 |
| Química de batería tratada | Solo plomo-ácido | No especificada (genérica) | Ion-litio (Huawei LUNA2000) |
| Conclusión sobre almacenamiento | Método de dimensionado por fiabilidad (LLP), sin evaluar rentabilidad | NO rentable en el caso estudiado | SÍ rentable (2.000 kWh óptimo) |
| Análisis económico VAN/TIR/LCOE | No | Sí | Sí |
| Performance Ratio citado | 0,4-0,85 (rango, media UE 0,74) | 0,784 | 0,7061 |

## Temas compartidos

### 1. Autoconsumo fotovoltaico industrial/genérico

Los tres tratan, en distinto grado de concreción, el dimensionado de un sistema fotovoltaico para autoconsumo: Perpiñán aporta el marco teórico general (SFCR, geometría solar, célula solar); Arcas y Fernandes Alves lo aplican a un caso industrial real simulado en PVsyst.

### 2. Almacenamiento en baterías — el hilo más relevante para el TFM

Es el tema donde las tres fuentes divergen de forma más útil para el TFM de Mario (autoconsumo con almacenamiento en un CPD):

- Perpiñán aporta el marco metodológico de fiabilidad (método LLP) pero solo para plomo-ácido, sin evaluar rentabilidad económica.
- Arcas concluye que el almacenamiento NO es rentable en su caso (bajo diferencial tarifario P1-P6, batería a 120 €/kWh).
- Fernandes Alves sí encuentra un tamaño de batería rentable (2.000 kWh, ion-litio) y aporta un método propio de degradación por ciclos equivalentes, más cercano en tecnología (ion-litio) a lo previsto para el CPD.

Contrastar estas tres conclusiones (marco teórico sin evaluación económica → no rentable → sí rentable) es un punto de partida útil para justificar por qué el resultado del TFM de Mario puede diferir de ambos casos de referencia, en función del perfil de consumo y el diferencial tarifario propios del CPD.

### 3. Simulación con PVsyst

Arcas y Fernandes Alves usan PVsyst para comparar configuraciones (orientaciones de tejado en Arcas; combinaciones de módulos/inversores/batería en Fernandes Alves). Perpiñán no usa PVsyst, pero su capítulo 6 (SFCR) describe la física que PVsyst modela internamente — útil para entender e interpretar los resultados de simulación de las otras dos fuentes, no para reemplazarlos.

### 4. Análisis económico (VAN, TIR, LCOE, payback)

Arcas y Fernandes Alves calculan VAN/TIR/LCOE/payback con estructuras de cálculo comparables, útiles como referencia de formato para el capítulo 8 de Mario. Perpiñán no incluye análisis económico de ningún caso — su aportación es exclusivamente física y de dimensionado.

### 5. Performance Ratio

Los tres dan una cifra de PR que sirve de contraste de plausibilidad: el rango general de Perpiñán (0,4-0,85, media UE 0,74) enmarca los valores puntuales de Arcas (0,784) y Fernandes Alves (0,7061, penalizado por pérdidas de proceso de almacenamiento AC-coupling) — ambos dentro de rango, lo que valida su plausibilidad sin necesidad de recalcularlos.

## Uso en el TFM

- Perpiñán es la única fuente citable de las tres: usar para justificar hipótesis físicas y el marco metodológico LLP (regla 10 de `CLAUDE.md`).
- Arcas y Fernandes Alves NO son citables: solo sirven como referencia de estructura, metodología de cálculo y orden de magnitud — contrastando explícitamente sus conclusiones distintas sobre la rentabilidad del almacenamiento antes de fijar la metodología propia del capítulo 7.

## Relacionado

- [[perpinan-2013-energia-solar-fotovoltaica]] — fuente citable primaria
- [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] — TFM de referencia, no citable
- [[fernandes-alves-2025-autoconsumo-mad9]] — TFM de referencia, no citable
