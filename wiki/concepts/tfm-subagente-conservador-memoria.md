---
type: concept
title: "Subagente: conservador-memoria"
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
  - "[[tfm-subagente-revisor-calidad]]"
---

# conservador-memoria

Modelo: sonnet. Definido en `.claude/agents/conservador-memoria.md`.

Audita `MEMORY.md` y los archivos de memoria persistente del proyecto para mantenerlos correctos, sin contradicciones y sin redundancia con lo que ya vive en el código o el documento.

## Cuándo se delega

Al cerrar un capítulo grande, tras una corrección de rumbo importante, o cuando Mario lo pide explícitamente.

## Qué busca

- Obsolescencia: memorias `project` que describían un estado ya cambiado (ej. un índice que pasó de "provisional" a "validado", una fecha de entrega movida).
- Contradicciones: dos memorias `feedback` de estilo que se pisan — gana la más reciente, pero anota el cambio en vez de dejar ambas.
- Redundancia: información que ya vive en el código/documento y no debería guardarse en memoria (convenciones LaTeX ya en la guía tipográfica, contenido del índice ya en `Memoria/indice_propuesto.md`).
- Huecos: decisiones tomadas en conversación pero no guardadas.

## Reglas clave

- Nunca borra una memoria `feedback` de estilo sin confirmar con Mario que ya no aplica.
- Mantiene cada línea de `MEMORY.md` por debajo de ~150 caracteres.
- Si encuentra una corrección de Mario repetida dos veces y no guardada como `feedback`, la crea siguiendo el formato con `**Why:**` y `**How to apply:**`.

## Relación con otros agentes

Cierra el ciclo del pipeline: audita las memorias que generan y consumen todos los demás agentes, con especial atención a lo que aprueba [[tfm-subagente-revisor-calidad]] al cerrar un capítulo.
