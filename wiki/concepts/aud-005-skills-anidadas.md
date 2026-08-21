---
type: concept
title: "AUD-005 — Skills anidadas dentro de sí mismas tras extraer los zips"
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
  - "[[tfm-skill-obsidian]]"
  - "[[tfm-skill-obsidian-vault-maintainer]]"
  - "[[aud-001-humanizer-no-invocable]]"
  - "[[aud-008-optimizador-prompts-sin-usar]]"
---

# AUD-005 — Skills anidadas dentro de sí mismas tras extraer los zips

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Fricción |
| **Commit** | `c2ede82` |

## El problema que trataba de resolver

Al descomprimir dos zips habían quedado carpetas dentro de carpetas con el mismo nombre (`obsidian/obsidian/...`), lo que hacía confusas todas las rutas al referenciar esas skills.

## La decisión que se planteó

Aplanar el anidamiento.

## La decisión que se adoptó

Aprobada y **ampliada por ti**: además de aplanarlas, pediste trasladarlas a `.claude/skills/` y borrar la carpeta `Skills/` entera.

## Detalle

Es un artefacto típico de descomprimir un `.zip` que ya contiene una carpeta raíz: acabas con `Skills/obsidian/obsidian/SKILL.md` en vez de `Skills/obsidian/SKILL.md`.

Tu ampliación fue lo que más valor aportó: al mover las skills a `.claude/skills/` no solo dejaron de estar anidadas, sino que pasaron a estar **en la ruta desde la que Claude realmente las carga** — el mismo problema de fondo que [[aud-001-humanizer-no-invocable]]. Y al vaciar `Skills/` se eliminó de golpe una fuente permanente de ambigüedad sobre dónde vive cada herramienta.

Efecto secundario útil: al borrar `Skills/` apareció un paquete olvidado que nadie usaba, lo que dio origen a [[aud-008-optimizador-prompts-sin-usar]].

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
