---
type: concept
title: "AUD-013 — La skill preguntaba la densidad aunque ya se la hubieran dicho"
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
  - "[[aud-012-densidad-contra-paginas]]"
  - "[[tfm-subagente-bibliotecario-pdf]]"
---

# AUD-013 — La skill preguntaba la densidad aunque ya se la hubieran dicho

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Fricción |
| **Commit** | `5ce1b49` |

## El problema que trataba de resolver

La skill estaba obligada a preguntar el nivel de densidad siempre, incluso cuando el encargo ya lo traía escrito. Y un agente trabajando en segundo plano no tiene a quién preguntar: o se quedaba bloqueado, o se saltaba su propia regla.

## La decisión que se planteó

Hacer la pregunta condicional: preguntar solo si el nivel no viene ya especificado.

## La decisión que se adoptó

Aprobada, y **absorbida dentro de [[aud-012-densidad-contra-paginas]]**: es la otra cara de la misma moneda, así que se aplicó en el mismo commit.

## Detalle

Los dos hallazgos parecían independientes pero comparten el mismo principio, que formulaste tú: **el nivel de densidad lo eliges siempre tú, nunca la skill**.

De ahí salen las dos reglas, que ahora conviven sin contradecirse:

- Si el encargo trae el nivel, se usa tal cual y no se pregunta.
- Si no lo trae, se pregunta **antes** de leer nada.

Y una prohibición explícita: la skill no puede deducir el nivel del tamaño del documento. Deducirlo era justamente la puerta trasera por la que se colaba el problema de [[aud-012-densidad-contra-paginas]].

Efecto colateral bueno: los subagentes en segundo plano dejan de estar en un callejón sin salida, porque el encargo que reciben ya lleva el nivel decidido.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
