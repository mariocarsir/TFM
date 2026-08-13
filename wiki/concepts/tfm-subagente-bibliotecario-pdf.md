---
type: concept
title: "Subagente: bibliotecario-pdf"
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
  - "[[tfm-subagente-investigador-cientifico]]"
  - "[[tfm-subagente-redactor-humanizador]]"
---

# bibliotecario-pdf

Modelo: sonnet. Definido en `.claude/agents/bibliotecario-pdf.md`.

Procesa un PDF nuevo de bibliografía y lo convierte en un resumen denso y verificable en `Bibliografia/Resumenes/<autor>_<año>.md`. Es su única función: no redacta, no calcula, no cita en el documento final.

## Cuándo se delega

Cuando Mario aporta un paper, norma o libro nuevo que quiere citar en el TFM. El PDF original debe estar (o copiarse) en `Bibliografia/PDFs/`.

## Reglas clave

- Procesa cada PDF una sola vez; si ya existe resumen, no lo reprocesa salvo petición explícita de ampliarlo.
- El resumen incluye: referencia IEEE lista para `biblio.bib`, 5-10 cifras clave con página exacta de origen, y 3-5 frases de relevancia por capítulo del índice.
- Nunca resume de memoria ni rellena huecos con conocimiento general: si un dato no está en el PDF, lo dice explícitamente en vez de inventarlo.

## Relación con otros agentes

Es la fuente de entrada del pipeline bibliográfico: [[tfm-subagente-investigador-cientifico]] contrasta cifras contra sus resúmenes, y [[tfm-subagente-redactor-humanizador]] solo puede citar a partir de ellos — nunca directamente del PDF.
