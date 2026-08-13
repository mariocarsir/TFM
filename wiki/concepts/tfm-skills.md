---
type: concept
title: "Skills que usa Mario en el TFM"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - tfm
  - skill
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-subagentes]]"
  - "[[tfm-skill-auditor]]"
  - "[[tfm-skill-humanizer]]"
  - "[[tfm-skill-obsidian]]"
  - "[[tfm-skill-obsidian-vault-maintainer]]"
  - "[[claude-obsidian]]"
  - "[[superpowers]]"
---

# Skills que usa Mario en el TFM

Si cada [[tfm-subagentes|subagente]] es una persona que ejecuta una parte del trabajo del TFM, una skill es la herramienta que esa persona usa (o que Mario usa directamente sobre la conversación). Este catálogo reúne las skills presentes en `.claude/skills/` del propio proyecto más los dos plugins de Claude Code instalados en esta sesión (`claude-obsidian`, `superpowers`).

## Catálogo

- [[tfm-skill-auditor]] — audita el meta-flujo (herramientas, organización, automatización) del propio catálogo de agentes y skills. Invocación exclusiva de Mario, nunca autoinvocada.
- [[tfm-skill-humanizer]] — reescribe un capítulo para reducir su riesgo de detección por IA (Turnitin/GPTZero) antes de cerrarlo.
- [[tfm-skill-obsidian]] — wrapper del CLI oficial de Obsidian Desktop (leer/crear/mover notas, tareas, propiedades).
- [[tfm-skill-obsidian-vault-maintainer]] — mantenimiento de vault Obsidian vía un framework externo ("openclaw") no instalado en este proyecto.
- [[claude-obsidian]] (hub aparte, documentado el 2026-08-06) — plugin con 15 skills para gestionar este mismo vault (ingesta, consulta, lint, transacciones).
- [[superpowers]] (hub aparte) — plugin con 14 skills de metodología general de Claude Code (brainstorming, TDD, debugging sistemático, git worktrees...).

## Vinculación con los subagentes

De todas las skills del catálogo, **solo `humanizer` tiene una relación directa y explícita** con subagentes del TFM, documentada en sus propios ficheros de definición:

- **humanizer** ↔ [[tfm-subagente-redactor-humanizador]] (la aplica sobre cada borrador, en modo ADVANCED por defecto o STEALTH si el texto ya está muy detectado, antes de dar el capítulo por cerrado) y [[tfm-subagente-revisor-calidad]] (comprueba en su checklist que el capítulo pasó por `humanizer` y que el riesgo residual es BAJO; si es MEDIO/ALTO, lo devuelve para modo STEALTH).

El resto no está vinculado a ningún subagente concreto, y conviene decirlo explícitamente en vez de forzar una relación que no existe:

- **auditor** evalúa el uso del catálogo completo de agentes y skills desde fuera (su propia definición lista qué queda fuera de su alcance: calidad de texto es de [[tfm-subagente-revisor-calidad]], memoria de [[tfm-subagente-conservador-memoria]], ingeniería de [[tfm-subagente-ingeniero-dominio]], cifras de [[tfm-subagente-investigador-cientifico]]) pero nunca ejecuta ese trabajo — solo audita si las herramientas están bien usadas, con aprobación explícita de Mario hallazgo por hallazgo.
- **obsidian** y **obsidian-vault-maintainer** son herramientas de gestión del vault sin uso confirmado en este proyecto (redundantes con `claude-obsidian` la primera; la segunda depende de un framework ausente).
- Las 15 skills de **claude-obsidian** y las 14 de **superpowers** son infraestructura que Mario o Claude Code usan directamente sobre la conversación (gestionar este mismo grafo, aplicar disciplina de proceso) — ningún subagente del TFM las invoca.
