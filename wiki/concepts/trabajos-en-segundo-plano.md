---
type: concept
title: Trabajos en segundo plano (background jobs) en Claude Code
created: 2026-08-22
updated: 2026-08-22
status: accepted
tags:
  - concept
  - claude-code
  - workflow
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[git-worktrees]]"
  - "[[aud-015-worktrees-residuales]]"
  - "[[aud-017-locks-git-huerfanos]]"
---

# Trabajos en segundo plano (background jobs) en Claude Code

Un **background job** es una sesión de Claude Code que se lanza para trabajar de forma autónoma mientras Mario no está necesariamente delante — a diferencia de una sesión en primer plano, donde Mario está presente en la conversación en tiempo real y puede autorizar cada paso al momento.

## Aislamiento automático: el worktree

Antes de tocar ningún archivo, un background job crea automáticamente su propio [[git-worktrees|worktree]] — sin que nadie lo pida explícitamente, a diferencia de una sesión en primer plano donde el worktree es opt-in (`EnterWorktree` bajo demanda). Esto evita que un job que corre sin supervisión directa pise el checkout principal donde Mario pueda tener trabajo sin guardar, o el de otro job corriendo en paralelo.

## La restricción que no es del worktree, sino del job

Es fácil confundir esta regla con una propiedad del worktree en sí, pero no lo es: **un background job nunca fusiona ni pushea directamente a `master`/`main`, ni fuerza un push, aunque el trabajo esté terminado, comiteado y verificado.** Esta restricción viene de que nadie está mirando en tiempo real para confirmar esa acción concreta — el propio diseño del background job asume que cualquier cambio en la rama compartida de verdad necesita un humano revisando en el momento.

En cambio, en una **sesión en primer plano** que también usa un worktree (por ejemplo porque `CLAUDE.md` o la memoria lo piden para una tarea concreta), esta restricción no aplica igual: si Mario está presente en esa misma conversación y autoriza fusionar o pushear a `master` ahí mismo, es una acción normal más, sujeta a las mismas reglas de confirmación que cualquier otra operación de riesgo (regla general de "medir dos veces, cortar una"), no a una prohibición categórica.

| | Background job | Sesión en primer plano con worktree |
| --- | --- | --- |
| ¿Quién crea el worktree? | Automático, al abrir la sesión | Bajo demanda (`EnterWorktree`) |
| ¿Puede fusionar/pushear a `master`? | **Nunca**, aunque esté verificado | Sí, si Mario lo autoriza ahí mismo |
| ¿Por qué la diferencia? | Nadie supervisa en tiempo real esa acción concreta | Mario está presente y puede confirmar al momento |

## Qué sí hace un background job sin preguntar

Dentro de esos límites, el flujo normal de un background job es proactivo:

1. Comitea los cambios verificados con mensaje descriptivo — no hace falta preguntar.
2. Pushea a su propia rama en GitHub si el repositorio tiene remoto (nunca a `master`/`main`).
3. Abre un PR en borrador si la tarea lo pide.
4. Al terminar, informa dónde vive el trabajo (ruta del worktree, rama, PR o la respuesta en sí) y el siguiente comando si hace falta uno.

## Limpieza al terminar

Igual que cualquier worktree, la carpeta se limpia automáticamente al terminar la sesión del job — independientemente de si algo se llegó a fusionar a `master`. Los commits sobreviven en su propia rama aunque la carpeta desaparezca. Ver [[aud-015-worktrees-residuales]] para un incidente real en el que worktrees de background jobs quedaron abandonados sin limpiarse y contaminaron el verificador de salud del vault, y [[aud-017-locks-git-huerfanos]] para un incidente relacionado de trabajo concurrente de varios jobs sobre el mismo repositorio.
