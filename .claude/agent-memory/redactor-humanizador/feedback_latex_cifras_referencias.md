---
name: feedback-latex-cifras-referencias
description: En el TFM las cifras van en texto plano (no siunitx) y no se usa \ref a capítulos aún no escritos
metadata:
  type: feedback
---

Dos reglas de formato LaTeX para los borradores de la memoria del TFM:

1. **Cifras y unidades en texto plano**: escribir «2,00 MWp», «216 m», «2,93 km», «3.832 MWh». No usar `\num{}`, `\SI{}` ni `\qty{}`.
2. **Nada de `\ref{}` a capítulos o secciones que todavía no existen**: mencionar «el capítulo 3» en texto llano y dejar un `% TODO Mario` para convertirlo en `\ref{}` cuando ese capítulo se escriba.

**Why:** aunque `siunitx` está cargado en `MUXLaTeX.cls`, el documento va con `babel` en español y una entrada tipo `\num{2.00}` sale con punto decimal anglosajón, contra la guía tipográfica (sección 13: coma decimal, punto de millar, máx. dos decimales). Y un `\ref` a una etiqueta inexistente produce referencia indefinida, que es justo lo que la regla de verificación del `CLAUDE.md` exige que salga a cero antes de cerrar una sección.

**How to apply:** en todo bloque LaTeX que se entregue para la memoria, desde el primer borrador. La guía tipográfica sigue mandando en lo demás (`\cite{}` y nunca `\parencite`/`\textcite`, comandos `\figura`/`\figuras`, IEEEtran con bibtex clásico).

Relacionado: [[feedback-estilo-mario]].
