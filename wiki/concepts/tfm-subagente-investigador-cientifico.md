---
type: concept
title: "Subagente: investigador-cientifico"
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
  - "[[tfm-subagente-bibliotecario-pdf]]"
  - "[[tfm-subagente-redactor-humanizador]]"
---

# investigador-cientifico

Modelo: sonnet. Definido en `.claude/agents/investigador-cientifico.md`.

Búsqueda bibliográfica rigurosa y fact-checking en el ámbito fotovoltaico/almacenamiento/CPD. Su función es evitar que entren al TFM afirmaciones sin respaldo, actuando como filtro antes de que cualquier cifra llegue a redacción.

## Cuándo se delega

Antes de afirmar cualquier dato técnico, normativo o de mercado que no esté ya en un resumen verificado.

## Reglas clave

- Nunca inventa ni completa con conocimiento general un dato técnico, normativo o de mercado; si no hay fuente, lo dice explícitamente y pide el PDF/dato a Mario.
- Toda cifra citada debe ser trazable a un resumen de `Bibliografia/Resumenes/` o a la normativa oficial de `Normativa TFM/`.
- Para normativa de autoconsumo (cambia con frecuencia en España), verifica vigencia y avisa si conviene confirmar la versión más reciente.
- Si detecta contradicción entre fuentes (p. ej. dos TFM de referencia con criterios distintos), la señala explícitamente en vez de elegir una en silencio.

## Relación con otros agentes

Consume los resúmenes que produce [[tfm-subagente-bibliotecario-pdf]] y actúa como verificación previa a [[tfm-subagente-redactor-humanizador]], que no debería citar ningún dato que no haya pasado por aquí.
