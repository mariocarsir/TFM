---
type: concept
title: "Subagente: analista-economico"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - tfm
  - subagent
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-subagentes]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
  - "[[tfm-subagente-redactor-humanizador]]"
---

# analista-economico

Modelo: sonnet. Definido en `.claude/agents/analista-economico.md`.

Estructura y revisa los cálculos económicos y el modelo horario de gestión del almacenamiento en Excel: todo lo que PVsyst no cubre.

## Cuándo se delega

Para el capítulo 8 (análisis económico) y el capítulo 7 (estrategia de carga/descarga).

## Alcance

- Modelo horario anual de gestión del almacenamiento (carga/descarga por periodos tarifarios).
- Análisis económico completo: mediciones y presupuesto, VAN, TIR, payback, LCOE, análisis de sensibilidad, escenarios de precio de electricidad.

## Reglas clave

- No escribe código: da arquitectura de hoja (pestañas, fórmulas, inputs/outputs) y estructura de tablas y gráficos.
- Cada cifra que acabe en la memoria debe ser trazable a una celda concreta de un Excel real (regla de "cifras canónicas" de `CLAUDE.md`).
- Para LCOE, VAN y TIR: explicita las hipótesis (tasa de descuento, vida útil, degradación de baterías y módulos, inflación) y pide a Mario que las confirme — no asume valores de industria sin aprobación.
- Los gráficos de sensibilidad y evolución de precio quedan en Excel con datos referenciables sin que el redactor recalcule nada.

## Relación con otros agentes

Comparte el capítulo 7 con [[tfm-subagente-ingeniero-dominio]] (que fija la estrategia técnica de carga/descarga que aquí se modela hora a hora) y entrega cifras canónicas a [[tfm-subagente-redactor-humanizador]] para el capítulo 8.
