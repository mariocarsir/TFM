---
type: concept
title: "AUD-007 — El mapa de carpetas de CLAUDE.md describía cosas que no existían"
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
  - "[[aud-008-optimizador-prompts-sin-usar]]"
  - "[[aud-005-skills-anidadas]]"
---

# AUD-007 — El mapa de carpetas de CLAUDE.md describía cosas que no existían

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-08 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Cosmético |
| **Commit** | `6f00dd7` |

## El problema que trataba de resolver

`CLAUDE.md` declaraba una carpeta `Presentaciones/` que no existía en el disco, y describía `Skills/` con un contenido que ya no era el real.

## La decisión que se planteó

Retirar ambas filas del mapa de carpetas.

## La decisión que se adoptó

Aprobada, con el diff mostrado antes de escribir por tratarse de `CLAUDE.md`.

## Detalle

`CLAUDE.md` es el fichero que Claude lee al empezar cada sesión para saber cómo está montado el proyecto. Si describe carpetas que no existen, deja de ser fiable como mapa — y un mapa en el que no confías no sirve para nada.

**Sobre la puerta dura.** La skill [[tfm-skill-auditor]] obliga a enseñarte el diff exacto antes de escribir en `CLAUDE.md`, `.claude/agents/**` o `Datos/**`. Son los tres sitios donde un cambio silencioso podría cambiar el comportamiento de todo el proyecto sin que te enteres, así que ahí nunca se escribe a ciegas.

Al aplicarlo apareció, de rebote, el paquete huérfano que originó [[aud-008-optimizador-prompts-sin-usar]].

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
