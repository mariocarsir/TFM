---
type: concept
title: "AUD-008 — Un paquete de skill sin desempaquetar que nadie usa"
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
  - "[[aud-007-claude-md-desactualizado]]"
  - "[[tfm-skills]]"
---

# AUD-008 — Un paquete de skill sin desempaquetar que nadie usa

| | |
| --- | --- |
| **Estado** | Pendiente — Se dejó para más adelante, a propósito. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Cosmético |
| **Commit** | sin commit |

## El problema que trataba de resolver

Apareció `Skills/optimizador-prompts.skill`, un paquete comprimido sin instalar y sin que ningún agente, skill ni documento lo referenciase. Estaba ahí sin función.

## La decisión que se planteó

Decidir si se instala o se retira.

## La decisión que se adoptó

Dijiste que lo gestionas **tú manualmente**, fuera del alcance de esa pasada. Queda anotado como pendiente, no como rechazado.

## Detalle

Se comprobó antes de proponerlo que no tenía ninguna referencia operativa: solo aparecía en la fila de `CLAUDE.md` que se retiró en [[aud-007-claude-md-desactualizado]] y en la documentación de diseño de la propia skill auditora. Es decir, retirarlo no rompería nada.

No es urgente ni tiene consecuencia técnica. Está anotado para que no se pierda: la diferencia entre "pendiente" y "olvidado" es precisamente que exista esta ficha.

Salió a la luz al aplicar [[aud-007-claude-md-desactualizado]] — un patrón habitual en auditorías: arreglar algo destapa lo que había debajo.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
