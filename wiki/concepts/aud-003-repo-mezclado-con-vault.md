---
type: concept
title: "AUD-003 — El repositorio mezcla el TFM con los artefactos de Obsidian"
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
  - "[[claude-obsidian]]"
  - "[[aud-010-config-obsidian-versionada]]"
  - "[[aud-005-skills-anidadas]]"
---

# AUD-003 — El repositorio mezcla el TFM con los artefactos de Obsidian

| | |
| --- | --- |
| **Estado** | Pendiente — Se dejó para más adelante, a propósito. |
| **Fecha** | 2026-08-08 |
| **Eje** | Orden |
| **Severidad** | Fricción |
| **Commit** | sin commit |

## El problema que trataba de resolver

En la misma carpeta y bajo el mismo control de versiones conviven dos cosas distintas: el TFM (memoria, datos, bibliografía) y toda la maquinaria del vault de Obsidian (`wiki/`, `inbox/`, `.obsidian/`, `.raw/`). Confunde cuál es realmente el alcance del repositorio.

## La decisión que se planteó

Aclarar el origen de la mezcla y decidir si el vault se separa a un repositorio propio.

## La decisión que se adoptó

Decidiste **no separarlo**. Se queda como está. Si algún día el volumen de ficheros de Obsidian crece mucho, se valorará agruparlos en una carpeta `Obsidian/` dentro de este mismo repositorio.

## Detalle

El origen no fue un accidente: elegiste esta misma carpeta del TFM como bóveda de Obsidian, así que la herramienta creó su estructura aquí dentro. No hay nada roto — es una consecuencia lógica de esa elección.

La fricción es de legibilidad: quien mire el repositorio ve mezclados los ficheros del trabajo académico con los de una herramienta de notas, y el `CLAUDE.md` no lo declaraba.

**Por qué sigue pendiente y no rechazado.** Separar repositorios tiene un coste real (dos historiales, dos sitios donde commitear) que hoy no compensa. Queda anotado como decisión consciente, no como olvido. La sub-parte de las skills sueltas de Obsidian sí se resolvió, dentro de [[aud-005-skills-anidadas]].

Está emparentado con [[aud-010-config-obsidian-versionada]], que es la misma raíz vista a menor escala.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
