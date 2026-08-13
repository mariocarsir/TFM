---
type: concept
title: "Subagente: revisor-calidad"
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
  - "[[tfm-subagente-redactor-humanizador]]"
  - "[[tfm-subagente-conservador-memoria]]"
  - "[[tfm-skill-humanizer]]"
---

# revisor-calidad

Modelo: sonnet. Definido en `.claude/agents/revisor-calidad.md`.

Revisión post-redacción de un capítulo cerrado contra tres ejes: coherencia interna, cumplimiento de la guía tipográfica y trazabilidad de citas.

## Cuándo se delega

Al cerrar cualquier sección o capítulo grande, antes de darlo por definitivo.

## Checklist de revisión

1. Formato (`Normativa TFM/guia_tipografica.md`): clase `book`, Palatino/mathpazo, sin sangría, parskip, color `lechuga`, siunitx, IEEEtran.
2. Estilo y aspectos formales ERMA (secciones 9-13): impersonal, párrafos de 6-8 líneas, figuras/tablas numeradas sin repetirse, ecuaciones editadas y numeradas.
3. Estructura genérica ERMA: cada categoría (introducción, requisitos, metodología, resultados) cubierta en algún capítulo.
4. Límite de extensión: máximo 150 páginas (normativa ERMA) — vigila el cómputo acumulado.
5. Citas: cada cifra trazable a un resumen de `Bibliografia/Resumenes/`; señala cifras "sueltas" sin fuente.
6. Terminología consistente a lo largo del documento.
7. Compilación: exige `pdflatex → biber → pdflatex ×2` con 0 referencias/citas indefinidas.
8. Riesgo Turnitin residual: confirma paso por la skill [[tfm-skill-humanizer]] y puntuación BAJA; si es MEDIO/ALTO, devuelve a modo STEALTH.
9. Conclusiones (capítulo 11): correspondencia 1:1 con cada alcance/resultado, sin elementos nuevos.

Nunca aprueba un capítulo que falle alguno de estos puntos; enumera exactamente qué falla y dónde.

## Relación con otros agentes y skills

Recibe el borrador de [[tfm-subagente-redactor-humanizador]] — ya pasado por [[tfm-skill-humanizer]] — y, tras aprobar un capítulo grande, dispara la auditoría de [[tfm-subagente-conservador-memoria]] sobre la memoria persistente del proyecto.
