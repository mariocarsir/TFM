---
type: concept
title: "Skill: auditor"
created: 2026-08-13
updated: 2026-08-21
status: developing
tags:
  - concept
  - tfm
  - skill
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skills]]"
  - "[[tfm-subagente-revisor-calidad]]"
  - "[[tfm-subagente-conservador-memoria]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
  - "[[tfm-subagente-investigador-cientifico]]"
---

# auditor

Definida en `.claude/skills/auditor/SKILL.md`. Invocación exclusiva de Mario (`disable-model-invocation: true` — no se autoinvoca desde ningún agente); triggers: `/auditor`, "audita el flujo", "no me convence cómo estamos trabajando".

Audita **cómo se trabaja** en el proyecto — herramientas, organización de ficheros, qué debería estar automatizado y no lo está — nunca el trabajo en sí (esa frontera es explícita en su propia definición, para no dar veredictos contradictorios con los agentes de dominio).

## Fases

0. **Inventario de recursos** (bloqueante, siempre completo): tabula `.claude/agents/*.md`, skills cargadas y en disco, `CLAUDE.md`, `MEMORY.md`, `Auditorias/registro.md`. Construye un mapa capacidad → recurso que ya la cubre; ninguna propuesta posterior puede sugerir crear algo que ya figure ahí.
1. **Recogida de evidencia**, delegada a un subagente `Explore` de solo lectura (árbol de ficheros, estado de git, correspondencia `CLAUDE.md` vs. disco).
2. **Análisis en cuatro ejes**: doctrina contra realidad, orden del repositorio, repetición hacia automatización (elige entre hook/skill/subagente/script/regla), solape y huecos.
3. **Priorización**: cada hallazgo lleva eje, severidad, coste de arreglo y consecuencia de no arreglarlo; máximo siete hallazgos presentados.
4. **Aprobación y aplicación**: nada se aplica sin un sí explícito de Mario, hallazgo por hallazgo; puertas duras (diff obligatorio antes de escribir) sobre `CLAUDE.md`, `.claude/agents/**` y `Datos/**`.

## Reglas clave

- No propone crear algo cuya capacidad ya figure en el mapa de la Fase 0, ni repite un hallazgo marcado `rechazado`.
- Un informe sin hallazgos es un resultado válido — ante la duda, calla en vez de inflar el informe.
- Cada cambio aplicado es un commit atómico (`auditoría(AUD-NNN): <resumen>`), sin worktree, con evidencia legible de que quedó hecho.

## Hallazgos producidos

Todo lo que esta skill ha encontrado está catalogado en [[registro-auditorias]], con una ficha por hallazgo explicando qué problema trataba de resolver, qué se propuso y qué se decidió finalmente. A 2026-08-21 son 18 hallazgos repartidos en dos pasadas: la auditoría completa del 2026-08-08 ([[aud-001-humanizer-no-invocable]] a [[aud-010-config-obsidian-versionada]]) y la auditoría con foco del 2026-08-21 sobre las skills de resumen e ingesta ([[aud-011-escritura-por-trozos]] a [[aud-018-pvsyst-sin-ejercitar]]).

## Relación con los subagentes

No la usa ningún subagente — la invoca Mario directamente sobre el sistema completo. Su propia definición delimita el terreno de cada agente de dominio para no invadirlo: calidad de texto es de [[tfm-subagente-revisor-calidad]], memoria persistente de [[tfm-subagente-conservador-memoria]], ingeniería de [[tfm-subagente-ingeniero-dominio]], verificación de cifras de [[tfm-subagente-investigador-cientifico]]. Ver catálogo completo en [[tfm-skills]].
