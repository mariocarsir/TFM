---
type: concept
title: "Skill: wiki-cli (claude-obsidian)"
created: 2026-08-06
updated: 2026-08-06
status: developing
tags:
  - concept
  - claude-obsidian
  - skill
domain: "Claude Code plugins"
complexity: intermediate
related:
  - "[[claude-obsidian]]"
---

# wiki-cli

Detecta y usa el CLI oficial de Obsidian (`obsidian`) como transporte de solo lectura: búsquedas, backlinks, tags. Requiere que la app Obsidian esté abierta y el CLI habilitado en Settings→General; la mera presencia del ejecutable no garantiza que esté operativo. Todas las mutaciones del vault pasan siempre por el núcleo transaccional de `claude-obsidian`, nunca por este transporte.

Se invoca con `/claude-obsidian:wiki-cli`.
