---
type: concept
title: "Skill: using-git-worktrees (superpowers)"
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
  - "[[git-worktrees]]"
---

# using-git-worktrees

"Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback."

Aísla trabajo de una feature en un worktree (nativo de la herramienta o vía `git worktree` si no hay soporte nativo) antes de ejecutar un plan de implementación, para no mezclar cambios con el checkout principal. Ver [[git-worktrees]] para el concepto general ya documentado en este vault.

Ninguna relación con los subagentes del TFM. Ver [[tfm-skills]].
