---
type: concept
title: "Skill: wiki-retrieve (claude-obsidian)"
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

# wiki-retrieve

Construye y consulta un índice de recuperación BM25 local sobre el vault, con reranking multilingüe opcional (Nomic) por similitud coseno. Los cachés derivados se guardan en `.vault-meta/`, nunca modifica las notas canónicas. El egreso de red para el reranker requiere consentimiento explícito; si no está disponible, cae de forma determinista al ranking BM25 puro.

Se invoca con `/claude-obsidian:wiki-retrieve`. Actualmente disponible pero sin configurar en este vault (pendiente de `bin/setup-retrieve.sh` si se quiere activar).
