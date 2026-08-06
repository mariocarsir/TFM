---
type: concept
title: "Skill: wiki (claude-obsidian)"
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

# wiki

Skill orquestadora de [[claude-obsidian]]. Inicializa o adopta un vault de Obsidian y enruta la petición del usuario hacia la sub-skill correcta (ingest, query, save, autoresearch, lint, fold, canvas...) según la intención detectada, sin ampliar el alcance por su cuenta.

Comandos base: `init` (vault nuevo) y `adopt` (vault existente), ambos en modo dry-run por defecto; requieren aprobación explícita (`--approved-plan-sha256`) antes de `--apply`.

Se invoca con `/claude-obsidian:wiki`.
