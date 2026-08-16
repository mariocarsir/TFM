name: book-intelligence
description: >
Produce un informe completo de Inteligencia de Libros para cualquier PDF de libro subido —
ficción, no ficción, académico, autoayuda, negocios, filosofía, biografía,
memorias, historia, o género híbrido. Se activa cuando un usuario sube un PDF de libro y
pide análisis, desglose, resumen, informe, reseña, puntos clave, temas,
argumentos, o cualquier cosa que requiera un profundo compromiso con el contenido
y estructura del libro. También se activa cuando los usuarios dicen cosas como "analiza este libro",
"de qué trata este libro", "dame las ideas clave", "desglósalo para mí",
"qué argumenta el autor", o "qué debo llevarme de esto" — incluso
si no usan la palabra "informe" o "análisis". Usa esta habilidad de manera proactiva
siempre que un PDF de libro esté presente y el usuario quiera más que una descripción de una línea.
---
# Skill de Inteligencia de Libros
## Propósito
Produce un informe de Inteligencia de Libros estructurado y profundamente analítico a partir de un PDF de libro. El informe debe ser específico al texto real — no un resumen genérico que podría haber sido escrito desde una entrada de Wikipedia. Cada sección debe contener información derivable solo de la lectura del libro en sí.
La salida predeterminada es markdown en línea en el chat. Crea un archivo `.md` descargable solo si el usuario lo solicita explícitamente.
---
## Paso 1: Extraer el Contenido del Libro
Sigue la habilidad de lectura de PDF en `/mnt/skills/public/pdf-reading/SKILL.md` para
las mecánicas de extracción. Para libros específicamente:
Ejecuta `pdfinfo` para obtener el conteo de páginas y confirmar que es un PDF de texto (no escaneado).
Extrae el texto completo usando `pdftotext -layout` para extracción consciente del diseño, o
`pdfplumber` si necesitas granularidad a nivel de página. Para libros de más de 400 páginas,
extrae en partes (por ejemplo, las primeras 80 páginas, muestra del medio, últimas 30 páginas) más
cualquier índice o tabla de contenidos, en lugar de procesar el archivo completo.
Si `pdftotext` devuelve texto confuso o salida casi vacía, es probable que el PDF esté
escaneado; retrocede a rasterizar páginas representativas con `pdftoppm` y
léelas visualmente.
Para libros con figuras, gráficos o diagramas significativos (por ejemplo, un libro
de negocios con marcos, o un texto académico con datos), rasteriza esas
páginas específicas y léelas como imágenes además de la extracción de texto.
Anota cualquier falla de extracción, secciones faltantes o problemas de calidad explícitamente
en el informe.
**Conciencia del presupuesto de tokens:** La extracción de texto completo de un libro de 300 páginas es
aproximadamente 60,000–120,000 tokens. Prioriza extraer la introducción,
conclusión, aperturas de capítulos y cualquier tesis o secciones de resumen declaradas primero.
Luego muestrea capítulos medios. No rasterices todas las páginas — solo aquellas donde
el contenido visual importa.
---
## Paso 2: Identificar Género y Seleccionar Marco
Antes de escribir una sola palabra del informe, determina:
- **Género y subgénero** (por ejemplo, "no ficción narrativa / economía del comportamiento",
"ficción literaria / realismo mágico", "negocios / estrategia", "memorias /
biografía política")
- **Antecedentes del autor y contexto de publicación** — quién lo escribió, cuándo, para
qué audiencia, desde qué posición institucional o intelectual
- **Estado híbrido** — ¿abarca géneros? Un libro de Nassim Taleb no es
lo mismo que un libro de Malcolm Gladwell aunque ambos sean no ficción. Un
memoir ficcionalizado requiere mezclar marcos.
Luego selecciona el marco de análisis apropiado del Paso 3.
---
## Paso 3: Marcos de Análisis
Aplica el marco que coincida con el género del libro. Para híbridos, mezcla
inteligentemente — profundidad sobre la completitud.
---
### Marco A: No Ficción, Negocios, Autoayuda, Psicología, Filosofía, Académica
**Tesis Central**
La única reclamación central que hace el libro. Expresala en 1–2 oraciones como lo harías
para explicárselo a un amigo inteligente. Evita reexpresiones vagas ("el autor argumenta
que la mentalidad importa") — sé preciso sobre lo que exactamente se reclama.
**Argumentos Principales**
Los 3–6 pilares primarios que el autor usa para construir la tesis. No son
resúmenes de capítulos — son los movimientos lógicos que hace el argumento. Identifica
de qué depende cada argumento y cómo se conecta con la afirmación central.
**Evidencia y Ejemplos Clave**
Los datos, estudios de casos, experimentos o historias más convincentes citadas. Nota
la calidad de la evidencia — ¿es investigación revisada por pares, anécdota, datos
propietarios o estudio de caso histórico? Señala dónde la evidencia es escasa o exagerada.
**Modelos o Marcos Mentales Clave**
Cualquier modelo, matriz, taxonomía o concepto nombrado original que el autor
introduzca. Describe cada uno claramente: qué es, qué explica y dónde
se descompone.
**Perspectivas Accionables**
Conclusiones específicas y prácticas que un lector puede aplicar. Estas deben estar basadas en
el texto real — no generes consejos genéricos. Donde el autor brinda
instrucciones concretas o heurísticas, reproduce la lógica fielmente.
**Contraargumentos Reconocidos**
Objeciones, matices o matices que el autor aborda. Si el autor ignora
objeciones obvias, señala eso en Brechas Críticas.
**Brechas Críticas o Debilidades**
Lo que el autor exagera, pasa por alto o deja sin resolver. Esta sección
requiere juicio — identifica dónde el argumento es más débil, dónde la evidencia
es insuficiente o dónde los puntos ciegos del autor distorsionan las conclusiones.
No inflates esta sección con pequeñas objeciones; identifica problemas estructurales significativos.
**Mejores Citas**
3-5 citas cortas (cada una de menos de 20 palabras cuando sea posible) que mejor capturan las
ideas centrales del libro, su voz o formulaciones más memorables. Atribuir con
referencia de capítulo o página si está disponible.
---
### Marco B: Ficción, Ficción Literaria, Novela, Colección de Cuentos Cortos
**Tema(s) Central(es)**
Las ideas dominantes, preguntas o tensiones sobre las que se construye la narrativa.
Distingue entre temas superficiales (de qué trata la historia) y preocupaciones temáticas más profundas
(lo que el autor parece estar interrogando sobre la naturaleza humana, la sociedad o la existencia).
**Arquitectura de la Trama**
Un resumen conciso consciente de los spoilers: configuración, conflicto central, puntos de inflexión clave,
clímax, resolución. No vuelvas a contar cada evento — traza la lógica estructural de
la narrativa e identifica lo que la impulsa hacia adelante.
**Análisis de Personajes**
Personajes clave, sus arcos, motivaciones y roles simbólicos o temáticos. Para
cada personaje importante: ¿qué quieren, qué temen, y cómo cambian (o no cambian)?
**Técnica Narrativa**
Punto de vista, tiempo, estructura, ritmo, uso del tiempo (cronológico, fragmentado,
no lineal), narración poco fiable, narrativas enmarcadas u otras elecciones formales.
Explica cómo estas elecciones sirven a los propósitos de la historia en lugar de solo nombrarlas.
**Simbolismo y Motivos**
Imágenes, objetos, configuraciones o patrones recurrentes y en qué acumulan
significado a lo largo de la narrativa. No fabriques simbolismo que no esté claramente respaldado por el texto.
**Mensaje o Visión del Mundo del Autor**
Lo que el autor parece estar diciendo sobre la vida, la sociedad, la naturaleza humana o el
tema. Mantén este nivel de inferencia — anota dónde la interpretación es
especulativa frente a la claramente respaldada por el texto.
**Registro Emocional y Tonal**
El estado de ánimo y la atmósfera que el libro mantiene: su textura emocional dominante,
cambios tonales y el tipo de experiencia de lectura que crea. ¿Se gana sus
efectos emocionales, o se esfuerza por conseguirlos?
**Pasajes Memorables**
2-3 breves extractos (cada uno de menos de 40 palabras) que mejor ejemplifican el estilo de prosa
o cristalizan un tema. Atribuir con número de página o capítulo si está disponible.
---
### Marco C: Historia, Biografía, Memoria
**Narrativa o Argumento Central**
La historia central o la afirmación histórica que ancla el libro. Para biografía y
memoria: de qué trata esta vida, tal como se cuenta aquí, es en última instancia. Para la historia:
qué argumento sobre causa, consecuencia o interpretación está haciendo el libro.
**Arco Histórico o Biográfico**
Fases clave, períodos, eventos o puntos de inflexión cubiertos. Identifica la
lógica estructural — ¿es esto cronológico, temático o impulsado por argumentos?
**Figuras Principales y Sus Roles**
Quién importa y por qué. Para biografía y memoria, enfócate en cómo se caracteriza al sujeto
y cuál es la relación del autor con el sujeto.
Para la historia, identifica qué actores impulsan eventos y cómo el autor pondera
su agencia frente a fuerzas estructurales.
**Causas y Consecuencias**
Las fuerzas que el autor identifica como impulsoras de los eventos, y qué resultó. Nota
si la narrativa causal es individual (grandes hombres), estructural (sistemas,
economía, ideología) o contingente (accidente, tiempo).
**Perspectiva o Sesgo del Autor**
El lente interpretativo que el autor trae: político, ideológico, disciplinario,
personal. Ningún autor es neutral — identifica qué es lo que este autor ve claramente y
qué causa que su marco se pierda o minimice.
**Lecciones e Implicaciones**
Lo que esta historia o vida enseña, explícita o implícitamente. Sé específico:
"el autor argumenta que X conduce a Y en condiciones Z" es útil. La moralización vaga no.
**Revelaciones Destacadas**
Hechos, eventos, documentos o momentos que son sorprendentes, revisionistas,
o que dan un nuevo enfoque — cosas que el lector no sabría ni creería antes de leer
este libro.
---
## Paso 4: Formato de Salida
Comienza cada informe con un bloque de metadatos:
**Título:** [Título del Libro]
**Autor:** [Nombre del Autor]
**Género:** [Género y Subgénero Identificados]
**Año Publicado:** [Año, si es determinable a partir del texto o contexto]
**Propósito Central:** [Una frase — qué problema resuelve este libro o qué historia existe para contar]
Luego aplica las secciones adecuadas del marco como encabezados de markdown.
Cierra cada informe con una sección de **Veredicto del Lector**: 4-6 oraciones que
den una evaluación honesta del valor real del libro. Cubre: quién obtendrá más de
él, cuál es su mayor fortaleza, cuál es su limitación o fracaso más significativo, y si
cumple con su propósito declarado.
No te quedes en un hedor de significados. Un veredicto que podría aplicarse a cualquier libro
en el género es un veredicto fallido.
---
## Estándares de Calidad
- Cada oración debe contener información específica sobre este libro. Las observaciones
genéricas que podrían aplicarse a cualquier libro en el género son desperdicio.
- Distingue claramente entre lo que el autor reclama, lo que la evidencia
apoya y tu juicio analítico.
- No inventes citas ni parafrasees como citas. Si no puedes encontrar una cita directa,
describe el pasaje.
- Para PDFs escaneados o parcialmente ilegibles, indica explícitamente qué secciones
eran ilegibles y qué era analizable.
- La profundidad analítica supera la cobertura de secciones. Una sección de tesis bien argumentada
es más valiosa que completar superficialmente las ocho secciones del marco.
- El informe está redactado en prosa clara. Usa viñetas solo para las secciones de
Argumentos, Evidencia, Perspectivas y Citas donde el formato de lista
realmente ayude a la comprensión. Todas las secciones analíticas son prosa.