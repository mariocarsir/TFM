---
type: concept
title: "AUD-006 — El .gitignore excluía una ruta que ya no existía"
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
  - "[[aud-004-zips-versionados]]"
---

# AUD-006 — El .gitignore excluía una ruta que ya no existía

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Cosmético |
| **Commit** | `9b94c84` |

## El problema que trataba de resolver

Una línea del `.gitignore` apuntaba a una carpeta que ya no estaba en el disco. No rompía nada, pero ensuciaba un fichero que conviene mantener legible.

## La decisión que se planteó

Borrar la línea.

## La decisión que se adoptó

Aprobada tal cual. Se aplicó en el mismo commit que [[aud-004-zips-versionados]] por tocar las mismas líneas.

## Detalle

Cero consecuencias funcionales: git simplemente ignora una regla que no coincide con nada.

El motivo de arreglarlo es de higiene. Un `.gitignore` con reglas muertas envejece mal: al cabo de unos meses nadie sabe si una línea sigue siendo necesaria o es un resto, y acaba dando miedo tocarlo.

Coste de arreglo: un minuto. Es el tipo de hallazgo **cosmético** que la skill [[tfm-skill-auditor]] solo propone cuando ya está abriendo ese fichero por otro motivo — que fue exactamente el caso.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
