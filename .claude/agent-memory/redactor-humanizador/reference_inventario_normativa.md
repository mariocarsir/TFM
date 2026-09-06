---
name: reference-inventario-normativa
description: Dónde leer las 15 normas del Excel de normativa sin necesitar openpyxl, para redactar el capítulo 2
metadata:
  type: reference
---

`Memoria/analisis/normativa-inventario.md` es el volcado literal en Markdown de la hoja `Normativa` de `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`, con las 15 filas completas: tipo, jerarquía, fecha, título básico, título completo, resumen articulado, «¿Para qué se ha consultado?», URL ELI, vigencia y notas de derogación o modificación.

Es la **fuente canónica de títulos y fechas del capítulo 2** y la que hay que consultar antes de escribir cualquier norma. Se lee con `Read` sin necesidad de Bash ni de openpyxl, cosa que el `.xlsx` sí exige.

La columna «¿Para qué se ha consultado?» contiene ya la frase de aplicación al proyecto que cada norma debe llevar en el capítulo; conviene partir de ella en vez de redactar la aplicación desde cero.

Cuando el Excel cambie, el volcado hay que regenerarlo: no se edita a mano.

Para los apartados 2.4 (autonómica y local) y 2.5 (normas técnicas), que el Excel no cubre, la fuente es `Memoria/analisis/normativa-autonomica-y-tecnica.md`. Marca cada norma con un nivel de confianza explícito —VERIFICADO, LOCALIZADO NO LEÍDO A FONDO, NO VERIFICABLE—: **solo lo marcado como VERIFICADO puede pasar a LaTeX sin `[pendiente]`**.

Relacionado: [[feedback-latex-cifras-referencias]].
