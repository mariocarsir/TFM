---
type: concept
title: "Skill: wiki-query (claude-obsidian)"
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

# wiki-query

Responde preguntas usando exclusivamente el vault seleccionado como fuente de evidencia, sin modificar ningún archivo. Tres profundidades: `quick` (solo `hot.md`/`index.md`), `standard` (búsqueda selectiva con seguimiento de enlaces relevantes) y `deep` (cobertura amplia, sigue siendo de solo lectura).

Persistir el resultado de una consulta requiere una operación [[claude-obsidian-save]] separada y explícita.

Se invoca con `/claude-obsidian:wiki-query`.
