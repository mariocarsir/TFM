---
type: concept
title: "Skill: obsidian (CLI oficial)"
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

# obsidian (CLI oficial)

Definida en `.claude/skills/obsidian/SKILL.md`. Wrapper fino del CLI oficial de Obsidian Desktop (`obsidian <comando>`, disponible desde Obsidian 1.12.7+): leer/buscar/crear/editar notas, tareas, enlaces y propiedades del vault vía comandos como `obsidian read`, `obsidian search`, `obsidian create`, `obsidian property:set`, `obsidian backlinks`.

## Requisitos

- Obsidian Desktop instalado (1.12.7+).
- CLI activado en Settings → General → Command line interface.
- `obsidian` registrado en el PATH.
- La app abierta — el CLI se conecta a la instancia en ejecución.

## Estado en este proyecto

Sin uso confirmado. Redundante con `claude-obsidian` (que ya trae su propio transporte de lectura al mismo CLI en su skill `wiki-cli`) para el vault de este TFM; no hay evidencia de que el CLI de Obsidian esté activado ni de que la app esté abierta durante las sesiones de Claude Code.

## Relación con los subagentes

Ninguna. No la usa ningún subagente del TFM ni está integrada en el pipeline de redacción — es una herramienta de acceso directo al vault que, de usarse, la invocaría Mario o Claude Code fuera del flujo de los 7 agentes de dominio. Ver catálogo completo en [[tfm-skills]].
