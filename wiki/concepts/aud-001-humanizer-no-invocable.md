---
type: concept
title: "AUD-001 — La skill humanizer estaba donde nadie podía invocarla"
created: 2026-08-21
updated: 2026-08-21
status: evergreen
tags:
  - concept
  - tfm
  - auditoria
  - hallazgo
  - cerrado
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skill-auditor]]"
  - "[[tfm-skill-humanizer]]"
  - "[[tfm-subagente-redactor-humanizador]]"
  - "[[tfm-subagente-revisor-calidad]]"
---

# AUD-001 — La skill humanizer estaba donde nadie podía invocarla

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-08 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Bloqueante |
| **Commit** | `a18a228` |

## El problema que trataba de resolver

`CLAUDE.md` declara obligatorio pasar cada capítulo por el humanizador anti-Turnitin, pero la skill vivía en una carpeta suelta (`Skills/`) desde la que Claude no puede cargarla. Es decir: una regla obligatoria que era imposible de cumplir.

## La decisión que se planteó

Mover la skill a `.claude/skills/humanizer/`, que es la única ruta desde la que Claude carga skills.

## La decisión que se adoptó

Aprobada tal cual y aplicada el mismo día.

## Detalle

El daño potencial era silencioso y grave: cada capítulo se habría cerrado *creyendo* que había pasado por el humanizador, cuando en realidad la herramienta ni siquiera estaba disponible. Nadie habría visto un error; simplemente el paso se habría saltado.

La causa fue de organización, no de contenido: la skill estaba correctamente escrita, solo estaba en el sitio equivocado. Claude Code únicamente carga las skills que encuentra bajo `.claude/skills/`; cualquier otra ubicación es, a efectos prácticos, invisible.

Este hallazgo es el ejemplo canónico del eje **doctrina contra realidad** que audita la skill [[tfm-skill-auditor]]: el documento decía una cosa y el disco decía otra.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
