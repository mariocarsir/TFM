---
type: concept
title: "Skill: humanizer"
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
  - "[[tfm-skills]]"
  - "[[tfm-subagente-redactor-humanizador]]"
  - "[[tfm-subagente-revisor-calidad]]"
---

# humanizer

Definida en `.claude/skills/humanizer/SKILL.md`. Triggers: "humaniza esto", "pásalo por el humanizador", "está muy detectado", "reescribe como humano". Combina técnicas de humanización de IA (estilo StealthWriter/Undetectable.ai) con conocimiento de cómo funcionan estadísticamente los detectores (Turnitin, GPTZero), aplicando por defecto la voz personal de Mario.

Paso obligatorio del flujo de redacción (regla 3 de `CLAUDE.md`): ningún capítulo se cierra sin pasar por aquí.

## Modos

- **LIGHT** — texto mayormente humano con trazas menores de IA: sustitución sutil de sinónimos, ritmo, conectores IA obvios.
- **ADVANCED (por defecto)** — texto académico IA estándar: reestructuración sintáctica completa, activa↔pasiva, clustering de vocabulario, conectores propios de Mario, un detalle numérico/técnico por párrafo donde falte.
- **STEALTH (máxima humanización)** — texto muy detectado o ya parafraseado una vez: reestructuración cognitiva completa, cambio de ángulo argumentativo, imperfecciones naturales controladas, dos versiones alternativas del párrafo de mayor riesgo.

## Cómo evalúa el riesgo

Perplexity (evita la palabra más probable), burstiness (varía longitud de frase agresivamente), distribución de vocabulario no uniforme, uniformidad estructural (entierra la tesis, transiciones abruptas), firma de paráfrasis Turnitin AIR-1 (reconstruir, no parafrasear). Autoevalúa el resultado como riesgo BAJO/MEDIO/ALTO y, si no es BAJO, indica qué párrafo sigue en riesgo.

## Reglas clave

- Mantiene tabla de vocabulario prohibido para Mario ("es importante destacar", "resulta fundamental/crucial", "juega un papel fundamental", "sin lugar a dudas") — se amplía cada vez que Mario rechaza una redacción concreta.
- Aplica por defecto la voz personal de Mario extraída de sus memorias de laboratorio reales (voz "se" impersonal, conectores característicos, anáfora "dicho/dicha", hedging al justificar desviaciones, cierre "En conclusión...").
- Preserva datos técnicos (valores, DOIs, citas, nombres de modelos); tras modo STEALTH recomienda una lectura manual final.

## Relación con los subagentes

Es la única skill del catálogo con vínculo directo y explícito a subagentes del TFM: [[tfm-subagente-redactor-humanizador]] la invoca sobre cada borrador antes de darlo por cerrado, y [[tfm-subagente-revisor-calidad]] comprueba en su checklist que se aplicó y que el riesgo residual es BAJO antes de aprobar el capítulo. Ver catálogo completo en [[tfm-skills]].
