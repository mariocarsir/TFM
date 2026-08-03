# Guía tipográfica del TFM — Mario Carrión Sirvent

Combina dos fuentes:

1. La plantilla LaTeX del TFG (`Documentacion de apoyo/TFG_Linea_Aerea/MUXLaTeX.cls`,
   MUXLaTeX v1.0.1) — maquetación, tipografía y paquetes (secciones 1-8). Se hereda tal cual
   salvo en la **portada**, que debe seguir la plantilla oficial del máster (ver sección 14).
2. La normativa oficial **`Documentacion de apoyo/GUIA Elaboracion TFM ERMA20.pdf`, páginas
   21-28** — criterios de estilo de redacción y aspectos formales exigidos/recomendados por
   el máster ERMA (secciones 9-13). Esta es la fuente que faltaba y que Mario señaló que
   debía incorporarse: no hay una guía tipográfica propia del máster más allá de estas
   páginas; el resto de la maquetación se apoya en el TFG y en los informes académicos.

## 1. Clase base y página

| Parámetro | Valor |
|---|---|
| Clase | `book`, opciones `a4paper, 12pt, oneside` |
| Tamaño de papel | A4 |
| Cuerpo de texto | 12 pt |
| Impresión | A una cara (`oneside`) |

## 2. Márgenes (paquete `geometry`)

Márgenes generales del documento:

| Margen | Valor |
|---|---|
| Interior (`inner`) | 2,5 cm |
| Exterior (`outer`) | 2,5 cm |
| Superior (`top`) | 2,5 cm |
| Inferior (`bottom`) | 2,0 cm |
| Encuadernación (`bindingoffset`) | 0,5 cm |
| Altura de cabecera (`headheight`) | 10 ex |

Tras la portada, el comando `\cambio` reduce los márgenes laterales a **2 cm** (interior y
exterior) manteniendo superior 2,5 cm e inferior 2 cm. Con `\digital{no}` el cuerpo pasa a
`twoside`; con `\digital{si}` permanece a una cara.

La **portada** usa márgenes propios de 2,5 cm en los cuatro lados y restaura la geometría
general en la página siguiente.

## 3. Tipografía

| Elemento | Especificación |
|---|---|
| Fuente principal | **Palatino** vía `mathpazo` (texto y matemáticas) |
| Idioma | `babel` con opción `spanish` |
| Sangría de párrafo (`parindent`) | **0 pt** (sin sangría) |
| Separación entre párrafos (`parskip`) | **0,7 em** |
| Interlineado | Simple (el de la clase `book`; no se redefine) |
| División de palabras | **Desactivada** (`\usepackage[none]{hyphenat}` + `\sloppy`) |

Penalizaciones tipográficas activas: sin guiones en líneas consecutivas
(`doublehyphendemerits=10000`), sin palabras partidas entre páginas (`brokenpenalty=10000`),
viudas y huérfanas casi prohibidas (`widowpenalty` y `clubpenalty` = 9999).

## 4. Títulos (paquete `titlesec`)

Color común de títulos: **`lechuga` = RGB(39, 30, 32)** — un negro cálido, no negro puro.
Las subsubsecciones usan `grissection` = HTML `#6D6E71` (gris medio).

| Nivel | Formato | Prefijo |
|---|---|---|
| Capítulo | `\Huge\bfseries`, color RGB(39,30,32) | `Capítulo N.` |
| Sección | `\Large\bfseries`, color RGB(39,30,32) | `N.M.` |
| Subsección | `\Large\bfseries`, color RGB(39,30,32) | `N.M.K.` |
| Subsubsección | `\Large\bfseries`, color #6D6E71 | sin numeración |

Espaciado de todos los títulos: `\titlespacing` a **0 pt** antes y después (el aire lo aporta
el `parskip`).

## 5. Índices y numeración

- `tocdepth = 2` → el índice general muestra capítulos, secciones y subsecciones.
- Entradas de capítulo en el índice: `\sffamily\bfseries` (sans-serif negrita), con relleno
  de puntos gris y número de página en negro.
- Índice de figuras (`\listoffigures`) y de tablas (`\listoftables`): **activados**.
- Preliminares en numeración **romana**; el cuerpo arranca en `\pagenumbering{arabic}`.
- Número de página: **pie de página centrado** (`fancyhdr`, `\fancyfoot[C]{\thepage}`),
  sin líneas de cabecera ni de pie (`headrulewidth` y `footrulewidth` = 0 pt).
- Páginas pares en blanco sin numerar (`emptypage`).

## 6. Orden de los preliminares (macro `\maquetacion`)

1. Portada
2. Portada de firmas
3. Página en blanco
4. Agradecimientos
5. Página en blanco
6. Resumen (español)
7. Abstract (inglés, opcional vía `\abstract{si}`)
8. Índice general
9. Índice de figuras
10. Índice de tablas
11. Lista de acrónimos

Palabras clave al final del resumen (`\clave{...}`) y *keywords* al final del abstract
(`\keywords{...}`), ambas en `\large\textsf\bfseries`.

## 7. Bibliografía

- Estilo: **IEEEtran** (`\bibliographystyle{IEEEtran}`), fichero `biblio.bib`.
- Se añade al índice como capítulo sin numerar.

## 8. Paquetes de apoyo relevantes

`acronym`, `siunitx` (con **coma decimal**, `per-mode=symbol`, `detect-all`), `amsmath`,
`amssymb`, `multirow`, `xcolor`/`colortbl` (`[table,xcdraw]`), `enumitem`, `float`,
`pdflscape`, `pdfpages`, `hyperref`+`xurl`, `tcolorbox`, `todonotes`, `watermark`,
`multicol`.

Enlaces (`hyperref`): citas en magenta, referencias internas en azul, URLs en rojo oscuro;
marcadores del PDF abiertos.

Comandos propios de figuras: `\figura{ruta}{ancho}{caption}` (una figura) y
`\figuras{ruta1}{ruta2}{caption}` (dos figuras al 45 % cada una). Ambos con `[H]` (posición
fija).

## 9. Estilo de redacción (normativa ERMA, pp. 21-22)

- **Estilo científico**: información presentada de forma clara y rigurosa.
- **Forma verbal**: impersonal en tiempo presente — coincide con la voz "se" ya identificada
  en la memoria de estilo `feedback_estilo_mario` a partir de sus informes académicos reales.
- **Brevedad**: frases cortas; decir lo mismo con el mínimo número de palabras.
- **Claridad**: párrafos de 6-8 líneas, separados entre sí (no bloques compactos).
- **Enumeraciones**: listas en vertical, ordenadas o con viñetas.
- **Ortografía**: pasar corrector ortográfico siempre antes de dar por cerrado un apartado.
- **Términos técnicos**: usar según definición normalizada, sin inventar sinónimos a mitad de
  documento.
- **Paginación**: el documento debe estar paginado incluso en fase de borrador.

Evitar explícitamente (la guía lo marca con un ejemplo real de mala redacción sobre inversores
fotovoltaicos, útil como referencia de qué NO hacer):

- Lenguaje coloquial.
- Estilo novelístico.
- Repetición de la misma palabra dentro de una frase.
- Palabras "comodín" reutilizadas sin variación a lo largo de todo el texto.

## 10. Aspectos formales — recomendados vs. obligatorios (pp. 23-24)

**Recomendados** (la guía los llama así explícitamente, no son de cumplimiento estricto):

| Aspecto | Recomendación ERMA | Estado frente a `MUXLaTeX.cls` |
|---|---|---|
| Tamaño de letra | 10-11 pt | **Resuelto**: ahora usa 11 pt, alineado con la recomendación ERMA (decisión de Mario, 3 de agosto de 2026). |
| Interlineado | Máximo 1,5 (o mínimo 15 pt) | Compatible: la clase usa interlineado simple, dentro del máximo. |
| Márgenes superiores y laterales | 2-3 cm | Compatible: la plantilla usa 2,5 cm. |
| Capítulos | Cada uno empieza en página nueva | Ya cumplido (comportamiento estándar de la clase `book`). |
| Apartados | Evitar más de tres subniveles | Respetar el límite capítulo > sección > subsección > subsubsección; no crear un cuarto nivel. |
| Siglas/abreviaturas/símbolos | Uso moderado y coherente; debe incluirse listado de siglas | Ya contemplado (ver sección 6, "Lista de acrónimos" en los preliminares). |

**Obligatorio**:

- **Justificación completa del texto** (alineado a ambos márgenes), salvo párrafos especiales.
  Comprobar que no se desactive la justificación por defecto de la clase `book`.

## 11. Figuras y tablas (p. 25)

- Toda figura y tabla debe llevar: **numeración** que permita referenciarla, **nombre o
  denominación** que describa el contenido, y **referencia de fuente** si procede de una
  modificación de una figura/tabla existente (fórmula tipo "elaboración propia a partir de...").
- **No repetir** una figura o tabla ya usada en otro punto del documento.
- Lista de figuras y lista de tablas al inicio o final del documento — ya contemplado en el
  orden de preliminares (sección 6, `\listoffigures` y `\listoftables`).

## 12. Ecuaciones (pp. 26-27)

- Las ecuaciones deben **editarse en LaTeX**, nunca copiarse como imagen o captura de otro
  documento.
- Deben ir **numeradas** para poder referenciarse.
- No es ortodoxo repetir una misma ecuación más de una vez en el documento.
- Las **variables se definen en lista vertical** justo después de la ecuación, nunca en una
  frase corrida (p. ej. "donde $G_i$ es..., $T_m$ es..., ...$" seguido, tal como aparece en el
  ejemplo de mala práctica de la propia guía).
- Evitar, según el ejemplo de "lo que NO debe hacerse" de la guía: ecuaciones "pegadas" al
  texto sin espacio, referencias de fuente incompletas o informales, y nomenclatura de
  variables que no coincide entre ecuaciones relacionadas del mismo capítulo.

## 13. Unidades y valores numéricos (p. 28)

- Las unidades del Sistema Internacional que derivan de nombres propios van en **mayúscula**
  (A de Ampere, K de Kelvin, W de Watt, etc.).
- La energía eléctrica se expresa habitualmente en **kWh** (prefijo "k" minúscula = 10³, W de
  vatios, h de horas).
- Valores numéricos: la **coma** "," separa decimales, el **punto** "." separa millares, y
  **no se usan más de dos cifras decimales**. Coherente con `siunitx` en coma decimal (sección
  8), pero ahora con el límite explícito de dos decimales que no estaba recogido antes.

## 14. Portada — NO se hereda del TFG

La portada del TFG **queda descartada**. Debe seguir `Plantillas/Portada TFM.docx`, cuya
estructura es:

- Logo **UPM (POLITÉCNICA)** arriba a la izquierda y logo **Máster ERMA** arriba a la derecha.
- `Máster en Energías Renovables y Medio Ambiente` (azul oscuro, negrita, centrado).
- `Curso 20../..` (azul oscuro, negrita, centrado).
- `Trabajo Fin de Máster` (azul, cuerpo mayor, centrado).
- **Título del trabajo** (negro, cuerpo grande, centrado).
- `Tutor:` a la izquierda y `Autor:` a la derecha (etiquetas en naranja/rojo, contenido en negro).
- `Fecha: Mes, año` abajo a la derecha (etiqueta en naranja/rojo).

Los logos originales están en `Plantillas/` (extraíbles del .docx: `word/media/image1.jpeg`
y `image2.jpeg`). Habrá que reconstruir esta portada en LaTeX respetando posiciones y colores.

## 15. Verificación

Toda edición del documento se cierra compilando `pdflatex → biber/bibtex → pdflatex ×2` y
comprobando 0 referencias y 0 citas indefinidas, según la regla de verificación del CLAUDE.md.
El `revisor-calidad` debe además comprobar el cumplimiento de las secciones 9-13 (estilo de
redacción, formato de figuras/tablas/ecuaciones, unidades) antes de cerrar cualquier capítulo.
