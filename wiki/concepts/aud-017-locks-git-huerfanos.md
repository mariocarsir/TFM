---
type: concept
title: "AUD-017 — Bloqueos de git abandonados por trabajos simultáneos"
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
  - "[[git-worktrees]]"
  - "[[aud-015-worktrees-residuales]]"
  - "[[aud-011-escritura-por-trozos]]"
---

# AUD-017 — Bloqueos de git abandonados por trabajos simultáneos

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Fricción |
| **Commit** | sin commit |

## El problema que trataba de resolver

Al guardar cambios, git falló porque existía un fichero de bloqueo (`.git/index.lock`). Git cuelga ese fichero como un cartel de *ocupado* mientras trabaja y lo quita al terminar; si el proceso muere de golpe, el cartel se queda puesto con nadie dentro y a partir de ahí todos los git de esa carpeta fallan.

## La decisión que se planteó

Escribir un protocolo obligatorio para tratar esos bloqueos, en lugar de improvisar cada vez.

## La decisión que se adoptó

Aprobada en su **versión barata**: el protocolo vive en la memoria persistente, no en `CLAUDE.md`.

## Detalle

**El peligro no es el fallo, es la reacción.** Lo fácil es borrar el bloqueo y seguir. Pero si resulta que sí hay un git vivo escribiendo en ese momento, al quitar el cartel entra un segundo proceso en el índice y lo corrompe: en el mejor caso hay que reconstruir lo que estaba preparado para guardar, en el peor se pierde.

**El protocolo, en tres pasos.** Primero esperar unos dos minutos, porque la mayoría de bloqueos legítimos se liberan solos. Segundo, mirar el fichero: si tiene 0 bytes y la fecha lleva minutos congelada, huele a abandonado. Tercero y decisivo, confirmar que **no existe ningún proceso de git en toda la máquina**. Solo entonces se borra.

**Por qué en memoria y no en `CLAUDE.md`.** `CLAUDE.md` se carga entero en cada sesión, así que meterlo ahí habría cobrado un peaje permanente por un incidente ocasional. Como memoria persistente, se recupera solo cuando es relevante — y sirve para **cualquier** tarea de git del proyecto, no solo las de Obsidian, que es donde estaba enterrado antes.

**La causa raíz** es la misma que la de [[aud-011-escritura-por-trozos]] y [[aud-015-worktrees-residuales]]: varios trabajos de Claude operando a la vez sobre el mismo repositorio.

Es el único hallazgo de la pasada **sin commit**: vive fuera del repositorio, en la memoria persistente.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
