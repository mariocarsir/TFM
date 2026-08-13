---
type: concept
title: "Skill: obsidian-vault-maintainer"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - tfm
  - skill
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-skills]]"
  - "[[claude-obsidian]]"
---

# obsidian-vault-maintainer

Definida en `.claude/skills/obsidian-vault-maintainer/SKILL.md`. Pensada para mantener un vault de memoria compatible con Obsidian (wikilinks, frontmatter, consciencia del CLI oficial) cuando el modo de renderizado del wiki es `obsidian`.

Depende por completo de comandos de un framework externo, `openclaw` (`openclaw wiki status`, `openclaw wiki obsidian search`, `openclaw wiki obsidian open`...), que **no está instalado en este proyecto** y no aparece en ningún otro sitio del repositorio.

## Estado en este proyecto

Inerte. No hay binario `openclaw` disponible, así que ningún comando que propone esta skill puede ejecutarse. No confundir con las skills incluidas dentro de `claude-obsidian` (que sí están operativas y cubren el mismo objetivo — mantener el vault legible por Obsidian — sin depender de `openclaw`).

## Relación con los subagentes

Ninguna. No la usa ningún subagente del TFM; de hecho no puede usarse en absoluto mientras falte la dependencia externa. Ver catálogo completo en [[tfm-skills]].
