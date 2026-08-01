# Guía tipográfica del TFM — Mario Carrión Sirvent

Extraída de la plantilla LaTeX del TFG (`Documentacion de apoyo/TFG_Linea_Aerea/MUXLaTeX.cls`,
MUXLaTeX v1.0.1). Se hereda tal cual salvo en la **portada**, que debe seguir la plantilla
oficial del máster (ver sección final).

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

## 9. Portada — NO se hereda del TFG

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

## 10. Verificación

Toda edición del documento se cierra compilando `pdflatex → biber/bibtex → pdflatex ×2` y
comprobando 0 referencias y 0 citas indefinidas, según la regla de verificación del CLAUDE.md.
