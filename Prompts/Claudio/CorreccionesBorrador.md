# CorreccionesBorrador

- **Fecha de la petición:** 11/10/2026 (hora no registrada)
- **Contexto (cuándo):** después de que Claude depurase `Prompts/Prompt_CorreccionesBorradorCap6.md` contrastándolo con el borrador real del capítulo 6 y detectase 10 problemas (9 fichas en uso y no 12, decimales del radar que no vienen de pesos, referencias internas en las líneas 99 y 101, efectos en cadena de borrar «Tecnologías de generación fotovoltaica», etc.). Versión 2: reescrita para ejecutarse DENTRO del worktree `Capitulo6ModulosBorrador`, con las decisiones A–F ya incorporadas.
- **Objetivo (por qué):** que Mario abra la sesión del worktree del borrador del capítulo 6 y le diga «lee y ejecuta este prompt», sin más contexto.

---

## Prompt

```markdown
# Correcciones del borrador del capítulo 6 (v2)

Trabajas en el worktree `Capitulo6ModulosBorrador` (rama `worktree-Capitulo6ModulosBorrador`). No crees otro
worktree. Fichero a corregir: `Memoria/Capitulos/capitulo06.tex`. Delega la redacción en
`redactor-humanizador` y el alta de fichas en `bibliotecario-pdf` (densidad Ejecutivo, una sola pregunta).
Antes de editar, lee el .tex entero. Los números de línea de este prompt son los del borrador del 10/10/2026.

## 1. Reglas de oro (guárdalas en memoria PRIMERO, antes de tocar el texto)
- Tablas: dato no encontrado → «N/D»; dato que no aplica conceptualmente → «N/A». Sin variantes
  («No figura», «No declarado», «No aplica»…). Ampliar `feedback_formato_tablas_y_notas_editor`.
- Prohibido referirse a documentación interna no publicable (guías de asignatura, TFM ajenos) como
  fuente u origen del método. Ejemplos vetados: «las que pide la guía de la asignatura», «según el TFM
  de M.A.». Un TFM solo se cita si Mario lo pide expresamente. Norma global para todos los capítulos
  restantes. Memoria feedback nueva + incorporarla a las instrucciones de `redactor-humanizador`.
- Aplícalas ya al cap. 6: líneas 99, 101 (y la nota pendiente sobre citar a Arcas: NO se cita) y las notas
  al pie de las tablas de V1b/V2 y V3 («rankings de la guía de la asignatura»). Marca con `\nota{}` como
  caso dudoso «recálculo de superficies» (líneas 273 y 372). Haz también un grep de esta regla en los
  capítulos 1 y 2 y avisa de lo que encuentres sin corregirlo.

## 2. Fichas técnicas (`Datos/Fichas Técnicas/Módulos/`)
- Crea `Módulos/OLD/` y mueve allí las fichas sin uso: las 3 de `V1b/` (AIKO Neostar 2P 475,
  LONGi Hi-MO X6, REC Alpha Pure RX 470).
- Con `git mv`, renombra `V2/` → `V1b-V2/` y elimina la carpeta `V1b/` vacía.
- Actualiza la ruta en la cabecera del .tex y en la memoria `feedback_fichas_tecnicas_fuente_unica`.
- Quedan 9 fichas en uso (3 por comparativa), no 12.

## 3. Apartado 6.1.1
### 3.1 «Tecnologías de generación fotovoltaica»: eliminar por completo
- Fuera el subapartado, su tabla y el párrafo introductorio de la línea 39. Revisa la numeración de tablas.
- `Perpinan2013` solo se cita ahí: comprueba si queda citada en otro sitio; si no, avísalo a Mario.
- Lleva a V1a el descarte de la capa fina (34,0 Wp/m²), que remitía al apartado borrado («como se ha indicado»).
  En V1b-V2, define el vidrio-vidrio en una frase.
- Actualiza CLAUDE.md (línea del índice de trabajo: el estado del arte de las tecnologías FV ya no vive en el 6.1)
  y la memoria `project_estructura_indice_erma`.

### 3.2 «Método de selección» → renómbralo «Criterios de selección»
- Fuentes citables: da de alta con `bibliotecario-pdf` las 9 fichas en uso (con `\cite`, entradas en
  `biblio.bib`). Los rankings (Black Ridge, CleanEnergyReviews 2025) y las fuentes de precios pvXchange y de
  bancabilidad las facilitará Mario: déjalos como `\nota{}` pendiente y NO inventes ni cites de memoria.
- Dato ausente en una ficha: NUNCA se asigna la peor nota. Se marca «N/D» en la tabla.
  Radar: ese aspecto se saca de la media del candidato; si falta el criterio entero, el eje no se pinta
  para ese candidato y se marca con `\nota{}`.
- AGC SunEwat Vision Square: es un vidrio a medida sin datos eléctricos. Descártalo del radar y de la
  valoración como «no dimensionable», mantenlo en la tabla con N/D/N/A según proceda, y no pidas datos
  que no existen. Revisa el texto de V1a en consecuencia.
- Contradicción de los decimales (1,8 y 2,2 de la Figura 6.1): NO hay pesos entre criterios; los decimales
  salen de (a) empates repartidos a la media y (b) criterios compuestos promediados («Pérdidas en
  operación», «Integración arquitectónica»). Corrige así: en los empates, todos reciben el mismo entero
  (p. ej. 3-3-2); en los criterios compuestos, media simple de los aspectos con dato, y dilo de forma
  explícita en una frase del apartado. Los decimales solo pueden aparecer en ejes compuestos.
- Redacta los 8 criterios SIN paréntesis valorativos («menor es mejor»), con la forma:
  «[Criterio]: [explicación del criterio]. [Conclusión sobre qué valor es preferible].»
- Tabla 6.3 actual («Criterio limitante y requisito de paso de cada variante»): sustitúyela por un
  listado de bullets, UNO POR VARIANTE (no por variable).

### 3.3 Apartados por variante (V1a, V1b-V2, V3)
- Estructura objetivo: introducción breve → tabla comparativa → diagrama radar → conclusión breve que
  justifique con claridad la elección.
- Elimina los bullets «Los criterios que no figuran en la tabla se valoran con…» (los que desglosan los
  ejes del radar) y los bullets de conclusión. Los datos que sostienen el radar (degradación anual,
  espesor de vidrio, clase de fuego, carga trasera, bifacialidad, módulos por string) pasan como FILAS a la
  tabla comparativa de cada variante. Esto rompe la regla de filas de Mario del 04/10: señálalo con
  `\nota{}` en la primera tabla para que él lo valide.
- No repitas datos ya presentes en tablas o fichas («el GL.04», no «el GL.04 de 1.641 × 989 mm»). Los
  cálculos propios que sostienen la elección (377,1 kWp, 12,3 kg/m², etc.) NO son redundantes: se mantienen.
- V3: el borrador avisa de que la elección depende de la bifacialidad del LONGi (dato ausente). Con la
  nueva regla de N/D, rehaz esa conclusión y déjala marcada con `\nota{}`.

### 3.4 PARADA OBLIGATORIA
Antes de rehacer valoraciones, radares y conclusiones: entrega a Mario el inventario de datos ausentes
(candidato × criterio) y espera su respuesta. Puedes avanzar mientras tanto con las partes que no dependen
de esos datos (secciones 1, 2, 3.1, el renombrado, la redacción de criterios y la tabla de bullets).

## 4. Cierre
- Compila (pdflatex → bibtex → pdflatex ×2): 0 referencias/citas indefinidas. Entrega el PDF del borrador.
- Commit en este worktree con título según la convención de CLAUDE.md. Sin push.
- Humanizer NO en esta ronda: va después de la revisión de Mario.
- Informe final: qué cambió, qué quedó en `\nota{}`, y la lista de datos ausentes pendientes.
```
