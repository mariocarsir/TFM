---
type: meta
title: Hot Cache
status: developing
created: 2026-08-05
updated: 2026-08-06
tags:
  - meta
  - hot-cache
---

# Recent Context

## Last Updated

2026-08-06 — save: [[git-worktrees]] completada.

## Key Recent Facts

- Los hooks SessionStart/Stop de claude-obsidian invocan el comando literal
  `python3`; en Windows nativo solo existe `python.exe` en el PATH. Fix: shim
  `python3.bat` en el directorio de la instalacion de Python.
- Los worktrees se crean bajo demanda en background jobs para aislar el checkout
  principal. No hay barrera entre capítulos dentro del mismo job/worktree.

## Recent Changes

- Creada nota conceptual: [[git-worktrees]].

## Active Threads

- Anadir una fuente a `inbox/` y correr la ingesta cuando haya bibliografia lista.
- Empezar a redactar el capítulo 2 del TFM.
