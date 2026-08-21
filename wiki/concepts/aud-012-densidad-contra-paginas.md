---
type: concept
title: "AUD-012 — Dos reglas contradictorias sobre cuánto del documento leer"
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
  - "[[aud-013-pregunta-densidad-incondicional]]"
  - "[[resumenes]]"
---

# AUD-012 — Dos reglas contradictorias sobre cuánto del documento leer

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Bloqueante |
| **Commit** | `5ce1b49` |

## El problema que trataba de resolver

La skill de resúmenes decía dos cosas incompatibles. Por un lado definía el nivel Exhaustivo como *nada omitido*. Por otro, cuarenta líneas más abajo, ordenaba leer solo una muestra de cualquier documento de más de 80 páginas para ahorrar tokens. Con un TFM de referencia largo pedido en exhaustivo, las dos reglas daban respuestas opuestas.

## La decisión que se planteó

Inicialmente, una regla de jerarquía: que Exhaustivo anulase los límites por páginas.

## La decisión que se adoptó

Tu solución, más simple: **eliminar los límites por páginas del todo**. El nivel lo eliges siempre tú y, si alguna vez se te olvida decirlo, que la skill pregunte antes de ponerse a trabajar.

## Detalle

**Tu objeción, que era correcta.** Cuando se te presentó el hallazgo señalaste que el hecho de que cada nivel de densidad cueste distinto no es un fallo, es el diseño. Tenías razón, y el hallazgo se reformuló para acotarlo a la contradicción real: no el coste, sino que hubiera **dos reglas distintas gobernando exactamente lo mismo** — cuánto del PDF se lee.

**Por qué era bloqueante y no cosmético.** El daño no se ve. Pides un resumen exhaustivo, recibes un resumen que dice ser exhaustivo, y en realidad es un muestreo. Luego citas ese resumen en la memoria del TFM como si fuera completo. Nada falla, nada avisa.

**La prueba de que era real.** En el resumen del TFM de Barrios López (132 páginas) el agente leyó el documento entero, **incumpliendo** la regla de las 80 páginas, y solo lo hizo porque el encargo insistía en mayúsculas en que fuera EXHAUSTIVO. La contradicción existía y se resolvía por casualidad.

**Cómo quedó.** El alcance de lectura lo fija ahora solo el nivel de densidad. Exhaustivo obliga a leer el documento entero, encadenando lecturas por rangos si hace falta. Y si el nivel pedido resulta inviable, la skill lo dice **antes** de empezar en lugar de recortar por su cuenta.

**Riesgo asumido conscientemente:** un exhaustivo sobre un documento largo es caro. La referencia real medida: 132 páginas costaron unas 360.000 unidades de texto y 25 minutos. Prefieres pagarlo a recibir un resumen incompleto sin saberlo.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
