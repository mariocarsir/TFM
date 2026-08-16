---
type: meta
title: Wiki Log
status: evergreen
created: 2026-08-05
updated: 2026-08-16
tags:
  - meta
  - log
---

# Wiki Log

Newest completed operations appear first.

## 2026-08-16 — ingest: Energía Solar Fotovoltaica (Perpiñán Lamigueiro, 2013)

Registrada la primera fuente bibliográfica citable del TFM en el ledger de
fuentes (`wiki/meta/ledgers/source-ledger.json`), con 4 afirmaciones
verificables extraídas al ledger de afirmaciones
(`wiki/meta/ledgers/claim-ledger.json`). Creada la página fuente
`wiki/sources/perpinan-2013-energia-solar-fotovoltaica.md`, enlazada al
resumen técnico ya generado por `bibliotecario-pdf` en
`Bibliografia/Resumenes/Perpiñán_2013.md` (fuente ya presente dentro del
vault, producida por el pipeline bibliográfico propio del proyecto — no se
capturó ningún payload crudo adicional en `.raw/`).

## 2026-08-06 — save: Git worktrees en Claude Code

Conversación sobre funcionamiento de git worktrees en Claude Code: cuándo se crean,
porque se usan en background jobs para aislar el checkout principal, y ciclo de vida.
Nota conceptual creada en `wiki/concepts/`.

## 2026-08-06 — save: Shim python3 para hooks de claude-obsidian en Windows

Diagnostico y fix de los hooks SessionStart/Stop de claude-obsidian, que fallaban
en Windows por ausencia de python3 en el PATH. Nota de decision creada en
`wiki/decisions/`.
