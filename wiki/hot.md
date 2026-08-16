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

2026-08-16 — ingest: [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] y
[[fernandes-alves-2025-autoconsumo-mad9]] completadas.

## Key Recent Facts

- Los hooks SessionStart/Stop de claude-obsidian invocan el comando literal
  `python3`; en Windows nativo solo existe `python.exe` en el PATH. Fix: shim
  `python3.bat` en el directorio de la instalacion de Python.
- Los worktrees se crean bajo demanda en background jobs para aislar el checkout
  principal. No hay barrera entre capítulos dentro del mismo job/worktree.
- Toda mutación del vault en Windows nativo está bloqueada por diseño
  (`UNSUPPORTED_PLATFORM`); las transacciones se aplican vía WSL2/Ubuntu
  apuntando al script core en la ruta `/mnt/c/...` del lado Windows.
- El `source_id` del ledger NUNCA se inventa: es
  `stable_source_id(kind, locator, sha256)` de `claude_obsidian/ledgers.py`
  (paquete del plugin, no vive en este repo). `review_status` solo admite
  `unreviewed/active/superseded/rejected` (no existe un estado
  "no-citable" propio: la no-citabilidad de un TFM de referencia se impone
  con `authority: secondary`/`community` + notas en cada claim + aviso en el
  cuerpo de la página, nunca con un enum inventado). `risk` de un claim solo
  admite `normal/high`; `high` exige dos fuentes independientes para poder
  aceptarse, así que una única fuente no revisada por pares sigue siendo
  `normal`, con la reserva puesta en `notes`, no en `risk`.

## Recent Changes

- Creada nota conceptual: [[git-worktrees]].
- Registrada la primera fuente bibliográfica citable del TFM:
  [[perpinan-2013-energia-solar-fotovoltaica]] (Perpiñán Lamigueiro, 2013).
- Registradas dos fuentes de referencia NO citables (TFM de otros autores del
  Máster ERMA, usados solo como referencia de estructura/metodología, nunca
  citables en el TFM de Mario):
  [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] (Manuel Arcas Navarro,
  2024, autoconsumo industrial San Martín PYL — concluye que el
  almacenamiento NO es rentable en ese caso) y
  [[fernandes-alves-2025-autoconsumo-mad9]] (Diego Fernandes Alves, 2025,
  autoconsumo sin excedentes Amazon MAD9 con almacenamiento en media
  tensión — aporta el método de degradación de batería por ciclos
  equivalentes más útil metodológicamente para el capítulo 7 de Mario).

## Active Threads

- Empezar a redactar el capítulo 2 del TFM.
- Ingestar el resto de resúmenes de `Bibliografia/Resumenes/` y
  `conocimiento fotovoltaico/Referencia/` a medida que `bibliotecario-pdf`
  los vaya generando.
