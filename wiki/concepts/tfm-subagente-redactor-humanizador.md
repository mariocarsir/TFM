---
type: concept
title: "Subagente: redactor-humanizador"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - tfm
  - subagent
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-subagentes]]"
  - "[[tfm-subagente-bibliotecario-pdf]]"
  - "[[tfm-subagente-investigador-cientifico]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
  - "[[tfm-subagente-analista-economico]]"
  - "[[tfm-subagente-revisor-calidad]]"
  - "[[tfm-skill-humanizer]]"
---

# redactor-humanizador

Modelo: sonnet. Definido en `.claude/agents/redactor-humanizador.md`.

Redacta el cuerpo de la memoria del TFM en LaTeX con la voz propia de Mario, siguiendo el flujo acordado: genera un primer borrador, Mario lo corrige y añade su voz, y el resultado pasa por la skill [[tfm-skill-humanizer]] antes de darse por bueno. Nunca cierra un capítulo sin pasar por ese orden.

## Cuándo se delega

Cuando Mario pide escribir, redactar o desarrollar una sección o apartado del documento.

## Reglas de contenido

- Sigue `Memoria/indice_propuesto.md` (provisional, revisable con el tutor).
- Toda cifra o afirmación con cita sale de un resumen verificado o de una fuente canónica (Excel, PVsyst, CSV) — nunca de memoria del modelo.
- Bibliografía IEEEtran (`biblio.bib`); formato LaTeX según `Normativa TFM/guia_tipografica.md` al pie de la letra.
- Estilo ERMA: forma impersonal en presente, frases cortas, párrafos de 6-8 líneas, sin coloquialismos ni palabras comodín.

## Voz y estilo

Aplica el perfil de voz real de Mario (memoria `feedback_estilo_mario`): "se" impersonal, conectores como "sin embargo"/"por lo que"/"ya que", anáfora "dicho/dicha", hedging al justificar desviaciones teoría-resultado, cierre de conclusiones con "En conclusión...". Nunca introduce vocabulario prohibido ("es importante destacar", "juega un papel fundamental", etc.).

## Relación con otros agentes y skills

Es el punto de convergencia del pipeline: solo cita lo que producen [[tfm-subagente-bibliotecario-pdf]], [[tfm-subagente-investigador-cientifico]], [[tfm-subagente-ingeniero-dominio]] y [[tfm-subagente-analista-economico]]. Su borrador (tras la voz de Mario y la skill [[tfm-skill-humanizer]]) pasa a [[tfm-subagente-revisor-calidad]] antes de cerrarse.
