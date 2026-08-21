---
type: concept
title: "AUD-014 — El procedimiento para indexar en Obsidian no estaba escrito en ninguna parte"
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
  - "[[claude-obsidian-wiki-ingest]]"
  - "[[claude-obsidian]]"
  - "[[tfm-subagente-bibliotecario-pdf]]"
---

# AUD-014 — El procedimiento para indexar en Obsidian no estaba escrito en ninguna parte

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Repetición/automatización |
| **Severidad** | Fricción |
| **Commit** | `af74d67` |

## El problema que trataba de resolver

Cada vez que pedías *indexa esto en Obsidian*, había que volver a deducir desde cero todo el procedimiento: rutas del plugin, formato de la transacción, estructura de los dos registros internos, valores admitidos, cómo se calcula el identificador de cada fuente y qué siete ficheros hay que tocar. Nada de eso estaba escrito.

## La decisión que se planteó

Consolidar el procedimiento completo en un documento de referencia dentro de la propia skill.

## La decisión que se adoptó

Aprobada. Inicialmente la habías rechazado; al reformularla como *meter dentro de la skill cómo usar claude-obsidian*, la aprobaste.

## Detalle

**El coste que se estaba pagando.** Entre 30.000 y 45.000 unidades de texto por cada indexación, solo en reconstruir lo que ya se sabía la vez anterior. Y creciendo, porque los registros internos se reescriben enteros cada vez.

**El riesgo que se estaba corriendo.** El identificador de cada fuente se calcula con una fórmula determinista a partir de su contenido. Inventárselo a mano —que es lo que pasa cuando no está documentado— rompe la unión entre el registro y la página, y el fallo no se ve hasta mucho después.

**Qué se escribió.** El documento `references/ingesta-obsidian.md`, con diez apartados: requisitos, flujo completo, los siete ficheros obligatorios, cálculo del identificador, formato de la transacción, estructura de los dos registros, valores admitidos, convención de enlaces, verificación y cierre. Todo **verificado contra el registro real del vault**, no escrito de memoria.

**Lo que NO cambió, y es importante.** La skill sigue sin indexar por su cuenta. Solo documenta el cómo, para cuando tú lo pidas. La regla de que Claude nunca toca el vault por iniciativa propia sigue intacta.

**Riesgo conocido:** el documento puede quedar desfasado si el plugin cambia de versión. Se mitiga porque las rutas incluyen el número de versión, así que un cambio salta a la vista.

Esta misma nota que estás leyendo se creó siguiendo ese documento.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
