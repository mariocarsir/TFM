---
type: concept
title: "AUD-016 — El nombre python3 es ambiguo en Windows"
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
  - "[[Shim python3 para hooks de claude-obsidian en Windows]]"
  - "[[claude-obsidian]]"
---

# AUD-016 — El nombre python3 es ambiguo en Windows

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Cosmético |
| **Commit** | `5ce8066` |

## El problema que trataba de resolver

Los scripts auxiliares de la skill se invocan con `python3`. En Windows ese nombre es ambiguo: lo primero que encuentra el sistema es un atajo de la Microsoft Store que, en lugar de ejecutar nada, imprime un anuncio invitando a instalar Python desde la tienda. El error resultante no apunta a la causa real.

## La decisión que se planteó

Documentar que `python3` no existe en este entorno y usar otro nombre.

## La decisión que se adoptó

Aprobada, pero **reformulada al re-verificarla**: `python3` sí funciona ahora, así que se documenta como ambigüedad, no como ausencia.

## Detalle

**El matiz honesto.** Al ir a aplicar el arreglo se comprobó de nuevo el entorno y resultó que `python3` **sí** funcionaba: resolvía correctamente a Python 3.12.10. Escribir en la skill que *no existe* habría sido documentar algo falso, y una regla falsa es peor que ninguna regla.

Lo que sí sigue siendo cierto, y se verificó: el atajo de la Microsoft Store **sigue estando primero** en el orden de búsqueda del sistema. Es decir, el comportamiento no es estable — funciona hoy y puede no funcionar mañana, según cómo esté configurado el entorno de esa sesión.

**Qué se escribió.** Una comprobación previa de tres candidatos en orden (`python3`, `python`, `py -3`), quedándose con el primero que responda con un número de versión de verdad; la descripción del síntoma exacto que hay que reconocer (el anuncio de la tienda en vez de una versión); y la nota de que dentro de WSL `python3` es siempre el correcto y la comprobación no hace falta.

Hay un precedente del mismo problema en otra parte del proyecto, recogido en [[Shim python3 para hooks de claude-obsidian en Windows]].

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
