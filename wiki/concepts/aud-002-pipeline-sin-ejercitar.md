---
type: concept
title: "AUD-002 — El pipeline bibliográfico y PVsyst nunca se habían usado"
created: 2026-08-21
updated: 2026-08-21
status: evergreen
tags:
  - concept
  - tfm
  - auditoria
  - hallazgo
  - cerrado
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skill-auditor]]"
  - "[[tfm-subagente-bibliotecario-pdf]]"
  - "[[tfm-subagente-piloto-pvsyst]]"
  - "[[aud-018-pvsyst-sin-ejercitar]]"
  - "[[resumenes]]"
---

# AUD-002 — El pipeline bibliográfico y PVsyst nunca se habían usado

| | |
| --- | --- |
| **Estado** | Cerrado — Dejó de aplicar porque el proyecto avanzó. |
| **Fecha** | 2026-08-08 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Bloqueante |
| **Commit** | sin commit |

## El problema que trataba de resolver

Todo el flujo de bibliografía y toda la parte de simulación fotovoltaica estaban descritos sobre el papel, pero nunca se habían ejecutado ni una vez. Las carpetas `Bibliografia/Resumenes/` y `Datos/PVsyst/` estaban vacías.

## La decisión que se planteó

Ninguna acción inmediata: no es un fallo que se arregle editando un fichero, es una alerta de proceso sin probar. Se dejó anotado para reevaluarlo en el primer uso real.

## La decisión que se adoptó

Se aceptó dejarlo en observación. El 21/08/2026 se cerró la mitad bibliográfica y la mitad de PVsyst se reabrió por separado como [[aud-018-pvsyst-sin-ejercitar]].

## Detalle

El riesgo de un proceso descrito pero no probado es que los fallos aparecen en el peor momento posible: la primera cita real, o la primera simulación, justo cuando ya hay prisa.

**Qué pasó después.** La mitad bibliográfica se ejercitó cuatro veces con éxito entre agosto de 2026: Perpiñán (2013), Arcas (2024), Fernandes Alves (2025) y Barrios López (2023). Y no solo funcionó — de ese uso real salieron **seis de los siete hallazgos** de la auditoría del 21/08/2026. Un proceso solo enseña sus costuras cuando se usa de verdad.

**Por qué se cerró como obsoleto y no como aplicado.** Porque no hubo ningún arreglo: el hallazgo dejó de aplicar por sí solo al cumplirse su condición. Y se cerró **solo a medias**: dar por buena la parte de PVsyst de rebote, sin haberla probado nunca, habría sido justamente el error que este hallazgo denunciaba. De ahí que naciera [[aud-018-pvsyst-sin-ejercitar]].

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
