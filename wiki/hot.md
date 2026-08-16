---
type: meta
title: Hot Cache
status: developing
created: 2026-08-05
updated: 2026-08-16
tags:
  - meta
  - hot-cache
---

# Recent Context

## Last Updated

2026-08-16 — ingest: [[perpinan-2013-energia-solar-fotovoltaica]] completada.

## Key Recent Facts

- Los hooks SessionStart/Stop de claude-obsidian invocan el comando literal
  `python3`; en Windows nativo solo existe `python.exe` en el PATH. Fix: shim
  `python3.bat` en el directorio de la instalacion de Python.
- Los worktrees se crean bajo demanda en background jobs para aislar el checkout
  principal. No hay barrera entre capítulos dentro del mismo job/worktree.
- Toda mutación del vault en Windows nativo está bloqueada por diseño
  (`UNSUPPORTED_PLATFORM`); las transacciones se aplican vía WSL2/Ubuntu
  apuntando al script core en la ruta `/mnt/c/...` del lado Windows.

## Recent Changes

- Creada nota conceptual: [[git-worktrees]].
- Registrada la primera fuente bibliográfica del TFM en el ledger de fuentes:
  [[perpinan-2013-energia-solar-fotovoltaica]] (Perpiñán Lamigueiro, 2013,
  *Energía Solar Fotovoltaica*), enlazada al resumen ya generado por
  `bibliotecario-pdf` en `Bibliografia/Resumenes/Perpiñán_2013.md`.

## Active Threads

- Empezar a redactar el capítulo 2 del TFM.
- Ingestar el resto de resúmenes de `Bibliografia/Resumenes/` y
  `conocimiento fotovoltaico/Referencia/` a medida que `bibliotecario-pdf`
  los vaya generando.
