---
type: concept
title: "AUD-010 — La configuración de Obsidian se versiona sin necesidad clara"
created: 2026-08-21
updated: 2026-08-21
status: developing
tags:
  - concept
  - tfm
  - auditoria
  - hallazgo
  - pendiente
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skill-auditor]]"
  - "[[aud-003-repo-mezclado-con-vault]]"
  - "[[claude-obsidian]]"
---

# AUD-010 — La configuración de Obsidian se versiona sin necesidad clara

| | |
| --- | --- |
| **Estado** | Pendiente — Se dejó para más adelante, a propósito. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Cosmético |
| **Commit** | sin commit |

## El problema que trataba de resolver

Casi todo el contenido de la carpeta `.obsidian/` (la configuración de la aplicación) está bajo control de versiones. Es estado de una herramienta, no contenido del TFM.

## La decisión que se planteó

Valorar si se excluye del control de versiones.

## La decisión que se adoptó

Detectado y **no priorizado**. Sigue pendiente, ligado a la decisión mayor de [[aud-003-repo-mezclado-con-vault]].

## Detalle

Ya se excluyeron en su día los ficheros claramente volátiles (`workspace.json` y `workspace-mobile.json`, que guardan qué paneles tienes abiertos). Lo que queda versionado es la configuración estable: temas, ajustes del grafo, plugins.

Hay un argumento legítimo **a favor** de versionarla: si algún día reinstalas Obsidian, recuperas tu configuración exacta. Por eso no es un fallo evidente, sino una decisión sin tomar.

Depende de [[aud-003-repo-mezclado-con-vault]]: si algún día el vault se separa o se agrupa en su propia carpeta, esta cuestión se resuelve sola.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
