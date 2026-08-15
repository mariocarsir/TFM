---
type: concept
title: "Subagentes del TFM"
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
  - "[[tfm-subagente-bibliotecario-pdf]]"
  - "[[tfm-subagente-investigador-cientifico]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
  - "[[tfm-subagente-piloto-pvsyst]]"
  - "[[tfm-subagente-analista-economico]]"
  - "[[tfm-subagente-redactor-humanizador]]"
  - "[[tfm-subagente-revisor-calidad]]"
  - "[[tfm-subagente-conservador-memoria]]"
  - "[[tfm-skills]]"
---

# Subagentes del TFM

Ocho agentes especializados definidos en `.claude/agents/` del repositorio del TFM (autoconsumo fotovoltaico con almacenamiento en un CPD, Máster ERMA). Cada uno declara `memory: project` (memoria persistente propia) y se invoca delegando desde la conversación principal según la tabla de `CLAUDE.md`, nunca redactando directamente sin pasar por el agente adecuado.

Las herramientas (skills) que estos agentes usan, o que Mario usa junto a ellos, están catalogadas aparte en [[tfm-skills]].

## Catálogo

- [[tfm-subagente-bibliotecario-pdf]] (modelo sonnet) — procesa un PDF de bibliografía una sola vez y genera su resumen ultradenso trazable.
- [[tfm-subagente-investigador-cientifico]] (modelo sonnet) — fact-checking: evita que entren al TFM cifras o normas sin fuente verificada.
- [[tfm-subagente-ingeniero-dominio]] (modelo opus) — núcleo técnico: dimensionado FV, PVsyst, almacenamiento, autoconsumo/autosuficiencia, tramitación.
- [[tfm-subagente-piloto-pvsyst]] (modelo opus) — manejo operativo de PVsyst: guía paso a paso de la interfaz, lectura de capturas de pantalla, validación de resultados de simulación.
- [[tfm-subagente-analista-economico]] (modelo sonnet) — arquitectura de las hojas Excel: modelo horario de almacenamiento y análisis económico (VAN, TIR, LCOE).
- [[tfm-subagente-redactor-humanizador]] (modelo sonnet) — redacta los capítulos en LaTeX con la voz propia de Mario y los prepara para el humanizador.
- [[tfm-subagente-revisor-calidad]] (modelo sonnet) — revisión post-redacción: formato, citas, terminología, riesgo Turnitin residual.
- [[tfm-subagente-conservador-memoria]] (modelo sonnet) — audita la memoria persistente del proyecto tras cada hito.

## Flujo entre agentes

El pipeline bibliográfico y de redacción, tal como lo fija `CLAUDE.md`, conecta a los agentes en una cadena de dependencias:

1. **Entrada de bibliografía**: [[tfm-subagente-bibliotecario-pdf]] convierte cada PDF nuevo en un resumen citable en `Bibliografia/Resumenes/`. Es la única puerta de entrada — nadie cita un PDF directamente.
2. **Verificación previa**: [[tfm-subagente-investigador-cientifico]] contrasta cualquier cifra, norma o dato de mercado contra esos resúmenes (o la normativa oficial) antes de que lleguen a redacción.
3. **Cifras canónicas de ingeniería y economía**: [[tfm-subagente-ingeniero-dominio]] (dimensionado, PVsyst, almacenamiento) y [[tfm-subagente-analista-economico]] (Excel, VAN/TIR/LCOE) comparten el capítulo 7 (estrategia de carga/descarga): el primero decide la estrategia técnica, el segundo la modela hora a hora. Ambos alimentan de cifras trazables al redactor.
4. **Redacción**: [[tfm-subagente-redactor-humanizador]] solo puede citar a partir de lo que producen los cuatro agentes anteriores — nunca de memoria del modelo. Genera el borrador, Mario añade su voz, y pasa por la skill [[tfm-skill-humanizer]] antes de considerarse cerrado.
5. **Cierre de capítulo**: [[tfm-subagente-revisor-calidad]] revisa el capítulo redactado contra formato, citas, terminología y riesgo Turnitin residual; puede devolverlo a redacción si falla algún punto.
6. **Mantenimiento de memoria**: tras la aprobación de un capítulo grande o una corrección de rumbo importante, [[tfm-subagente-conservador-memoria]] audita `MEMORY.md` y las memorias de proyecto de todos los agentes anteriores para mantenerlas correctas y sin contradicciones.

Regla transversal a los siete: ninguna cifra que termine en la memoria del TFM puede salir de un PDF, una hoja Excel o un informe PVsyst sin pasar antes por el agente responsable de esa fuente — nunca del conocimiento general del modelo.
