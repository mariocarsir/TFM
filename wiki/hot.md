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

2026-08-06 — primera operacion save completada.

## Key Recent Facts

- Los hooks SessionStart/Stop de claude-obsidian invocan el comando literal
  `python3`; en Windows nativo solo existe `python.exe` en el PATH. Fix: shim
  `python3.bat` en el directorio de la instalacion de Python.

## Recent Changes

- Creada la primera nota del vault: [[Shim python3 para hooks de claude-obsidian en Windows]].

## Active Threads

- Anadir una fuente a `inbox/` y correr la ingesta cuando haya bibliografia lista.
