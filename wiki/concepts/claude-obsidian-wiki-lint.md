---
type: concept
title: "Skill: wiki-lint (claude-obsidian)"
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

# wiki-lint

Auditoría determinista y de solo lectura de la salud del vault: enlaces rotos o ambiguos, páginas huérfanas, frontmatter incompleto, secciones vacías, índices desactualizados y violaciones del contrato de los ledgers de procedencia/afirmaciones. No repara nada ni realiza análisis semántico o de estilo — solo reporta los hallazgos deterministas del motor de lint.

Se invoca con `/claude-obsidian:wiki-lint`.
