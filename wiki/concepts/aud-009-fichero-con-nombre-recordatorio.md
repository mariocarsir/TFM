---
type: concept
title: "AUD-009 — Un fichero de datos con una nota-recordatorio como nombre"
created: 2026-08-21
updated: 2026-08-21
status: developing
tags:
  - concept
  - tfm
  - auditoria
  - hallazgo
  - pendiente
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skill-auditor]]"
  - "[[tfm-skill-auditor]]"
---

# AUD-009 — Un fichero de datos con una nota-recordatorio como nombre

| | |
| --- | --- |
| **Estado** | Pendiente — Se dejó para más adelante, a propósito. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Cosmético |
| **Commit** | sin commit |

## El problema que trataba de resolver

En `Datos/Consumo CPD/datos/` hay un fichero cuyo nombre es en realidad un recordatorio escrito a vuelapluma (`miraaverfalta...zip`), no un nombre descriptivo. Dentro de la carpeta de datos del TFM.

## La decisión que se planteó

Renombrarlo, o resolver lo que el recordatorio pedía y eliminarlo.

## La decisión que se adoptó

Detectado y **no priorizado**. Sigue pendiente.

## Detalle

Es cosmético hoy, pero está en el sitio más delicado del repositorio: `Datos/`, de donde salen las cifras canónicas del TFM (regla 5 de `CLAUDE.md`).

El riesgo real no es el nombre feo, es el recordatorio en sí: alguien anotó que faltaba algo y esa nota nunca se resolvió. Dentro de unos meses nadie recordará qué era lo que faltaba.

**Por qué no se tocó.** `Datos/**` es una de las tres puertas duras de la skill [[tfm-skill-auditor]]: no se toca nada ahí sin tu visto bueno explícito y con el cambio a la vista. Renombrar un fichero de datos por iniciativa propia sería exactamente el tipo de acción que esa regla prohíbe.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
