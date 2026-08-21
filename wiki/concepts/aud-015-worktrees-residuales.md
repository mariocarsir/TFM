---
type: concept
title: "AUD-015 — Copias residuales del repositorio inutilizaban el verificador del vault"
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
  - "[[git-worktrees]]"
  - "[[claude-obsidian-wiki-lint]]"
  - "[[aud-011-escritura-por-trozos]]"
  - "[[aud-017-locks-git-huerfanos]]"
---

# AUD-015 — Copias residuales del repositorio inutilizaban el verificador del vault

| | |
| --- | --- |
| **Estado** | Cerrado — Aceptaste el cambio y ya está aplicado. |
| **Fecha** | 2026-08-21 |
| **Eje** | Orden |
| **Severidad** | Fricción |
| **Commit** | `1b5221c` |

## El problema que trataba de resolver

Cuando Claude trabaja en segundo plano crea copias aisladas del repositorio (*worktrees*) para no pisar tu carpeta. Habían quedado seis abandonadas, y cinco contenían una copia completa del vault de Obsidian. El verificador de salud del vault las recorría y devolvía **182 problemas, ninguno real**, tapando por completo cualquier problema verdadero.

## La decisión que se planteó

Eliminar las copias residuales.

## La decisión que se adoptó

Aprobada, y ampliada al descubrir un problema añadido durante la limpieza.

## Detalle

**Comprobación previa.** Antes de borrar nada se verificó una por una que las seis copias estaban íntegramente fusionadas en la rama principal, sin cambios sin guardar y sin actividad en las seis horas anteriores. Nada de lo que había allí se perdió: todo estaba ya en `master`.

**El problema añadido que apareció.** Al investigarlo salió algo que no estaba en el diagnóstico: git había registrado seis de esos directorios en el índice como si fueran **submódulos** (entradas de tipo `gitlink`), y dos de ellas apuntaban a carpetas ya borradas del disco. Eran las entradas fantasma que aparecían marcadas como borradas en cada `git status`.

**Qué se hizo, en tres pasos.** Se eliminaron las seis copias y sus ramas locales; se retiraron del índice las seis entradas fantasma; y se añadió `.claude/worktrees/` al `.gitignore` para que ninguna copia futura vuelva a versionarse ni a contaminar el verificador.

**Resultado verificado.** El verificador pasa de **182 problemas a 0**, sobre 56 páginas y 168 enlaces. Vuelve a servir para lo que existe: detectar enlaces rotos y errores de procedencia.

Se conservaron a propósito dos ramas antiguas que no tenían copia asociada, por quedar fuera del alcance del hallazgo.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
