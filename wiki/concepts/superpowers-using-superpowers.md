---
type: concept
title: "Skill: using-superpowers (superpowers)"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - superpowers
  - skill
domain: "Claude Code plugins"
complexity: intermediate
related:
  - "[[superpowers]]"
---

# using-superpowers

"Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions."

Punto de entrada del plugin: obliga a comprobar si alguna skill (de este plugin o de cualquier otro instalado) aplica antes de responder, explorar el repositorio o hacer preguntas aclaratorias. Se carga automáticamente al inicio de cada conversación.

Ninguna relación con los subagentes del TFM — opera sobre la conversación principal, no dentro de un subagente. Ver [[tfm-skills]].
