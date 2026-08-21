---
type: concept
title: "AUD-004 — Tres zips versionados duplicaban 19 MB ya extraídos"
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
  - "[[aud-006-gitignore-ruta-fantasma]]"
---

# AUD-004 — Tres zips versionados duplicaban 19 MB ya extraídos

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Fricción |
| **Commit** | `9b94c84` |

## El problema que trataba de resolver

El repositorio guardaba tres ficheros `.zip` cuyo contenido ya estaba también descomprimido al lado. Unos 19 MB duplicados que git tenía que arrastrar en cada clonación.

## La decisión que se planteó

Sacarlos del control de versiones con `git rm --cached` (siguen en el disco, no se borran) y añadir `*.zip` y `*.rar` al `.gitignore`.

## La decisión que se adoptó

Aprobada tal cual y aplicada.

## Detalle

Un fichero comprimido versionado es especialmente malo para git: al ser binario, cada versión se guarda entera en vez de guardarse solo la diferencia. Y aquí ni siquiera aportaban nada, porque su contenido ya estaba descomprimido en el propio repositorio.

La consecuencia práctica de no arreglarlo era acumulativa: clonaciones y `git pull` cada vez más lentos, para siempre, ya que el historial de git no olvida.

**Detalle importante:** `git rm --cached` deja de versionar el fichero pero **no lo borra del disco**. Los zips siguen ahí; git simplemente deja de seguirles la pista.

Se aplicó en el mismo commit que [[aud-006-gitignore-ruta-fantasma]], porque tocaban las mismas líneas del mismo fichero.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
