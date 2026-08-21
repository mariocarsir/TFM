---
type: concept
title: "AUD-011 — El resumen se escribía por trozos y podía corromperse"
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
  - "[[aud-015-worktrees-residuales]]"
  - "[[aud-017-locks-git-huerfanos]]"
---

# AUD-011 — El resumen se escribía por trozos y podía corromperse

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Fricción |
| **Commit** | `10d367b` |

## El problema que trataba de resolver

Cuando Claude trabaja en segundo plano, tiene bloqueada la escritura directa de ficheros como medida de seguridad. El agente lo descubría a base de intentarlo y fallar, y acababa escribiendo el resumen a trozos, en varios envíos. Cada envío pasa por la terminal, y ahí las tildes, las eñes y los símbolos `$` de las ecuaciones LaTeX pueden estropearse sin avisar.

## La decisión que se planteó

Se plantearon tres vías: (a) desactivar el bloqueo de seguridad, (b) obligar al agente a aislarse en una copia del repositorio, o (c) dejar el bloqueo como está y prohibir por norma escribir a trozos.

## La decisión que se adoptó

La **opción (c)**, con un matiz que añadiste tú: que la skill sepa de antemano que la escritura directa va a fallar, para que no se quede reintentándolo en bucle.

## Detalle

**Por qué se descartaron las otras dos.** La (a) desactivaba una protección que existe por un motivo real: en este repositorio suele haber varios trabajos de Claude en marcha a la vez, y quitar el aislamiento abre la puerta a que se pisen entre ellos (justo lo que provocó [[aud-017-locks-git-huerfanos]]). La (b) se muerde la cola con [[aud-015-worktrees-residuales]], que precisamente eliminaba esas copias por los problemas que causaban.

**Qué se escribió en la skill.** Tres reglas: el fichero se vuelca de una sola vez; el bloqueo se da por conocido y no se reintenta; y después de escribir se comprueba el tamaño del fichero y que sigue habiendo caracteres acentuados dentro. Si un resumen en español tiene cero tildes, la escritura se corrompió y hay que repetirla, no parchearla.

**El detalle técnico que importa.** Al volcar el fichero hay que usar un delimitador entrecomillado. Sin las comillas, la terminal interpreta los `$` como variables suyas y se come las ecuaciones LaTeX enteras.

**Coste evitado:** entre 5.000 y 10.000 tokens por resumen en reintentos y troceado, más el riesgo no acotado de un resumen corrupto que se descubre tarde.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
