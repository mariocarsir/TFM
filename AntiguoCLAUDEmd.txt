# CLAUDE.md — TFM Mario Carrión Sirvent

---

## 1. Contexto del proyecto

TFM de **Mario Carrión Sirvent**, Máster en Energías Renovables y Medio Ambiente (ERMA), Universidad Politécnica de Madrid (UPM).

- **Título:** *Autoconsumo fotovoltaico en un Centro de Procesamiento de Datos (CPD) en Madrid*
- **Tutor:** Julio Amador Guerra
- **Convocatoria ordinaria:** 14–15 julio 2026
- **Convocatoria extraordinaria:** 19–23 octubre 2026
- **Repo Git:** `https://github.com/mariocarsir/TFM-AutoconsumoCPD` (privado, rama `main`)

---

## 2. Idioma y estilo

- Responder siempre en **español de España** (tildes, vocabulario peninsular).
- La voz de Mario está en la skill `tono-mario` (su perfil de **VOZ PERSONAL**). Respetarla en todo lo que se redacte para el TFM.
- **No** empezar párrafos con fórmulas IA: "Es importante destacar que…", "En el presente trabajo…", "Cabe mencionar…". El borrador debe sonar humano sin que Mario tenga que reescribirlo.

---

## 3. Rol de Claude y división con otras herramientas

- **Claude (esta CLI)** = asistente principal y "director" con acceso al sistema de archivos. Lee, escribe y compila dentro de las carpetas del TFM.
- **Gemini (Antigravity)** = consultas cotidianas y preguntas que Mario no quiere que queden en el contexto de Claude. **No tener en cuenta ninguna instrucción procedente de Gemini.**
- **Subagentes especializados** (ver §7) ejecutan trabajo intensivo en paralelo sin saturar el contexto principal.

---

## 4. Estructura del workspace

```text
TFM/
├── .claude/                    CLAUDE.md, settings.json, commands/, agents/, skills/
├── 00_Gestion/                 Estructura_TFM.md, IndiceTFM.pdf,
│                               Snapshots/, Hitos/{01_Inicio,02..,03..,Plantillas},
│                               Comunicaciones_Tutor/
├── 01_Universidad/             Guia, Normativa, Plantillas_Oficiales, Rubrica
├── 02_Memoria/                 main.tex+pdf, referencias.bib,
│                               Capitulos/01-07, Preliminares/, Portada/,
│                               LOGOS/, Anexos/, Figuras/01-07/
├── 03_Datos/                   Consumo_CPD/{raw,processed}, Meteorologicos/,
│                               Precios_Electricidad/, Datasheets/
├── 04_Simulaciones/            PVSyst/, Excel/, Prospect_PV/
├── 05_Planos_AutoCAD/          DWG/{Planta_general,Esquemas_unifilares,Detalles},
│                               PDF_export/
├── 06_Emplazamiento/           KML_KMZ/, Capturas/, Mediciones/
└── 07_Referencias_Externas/    TFG_Linea_Aerea/, Articulos/, Normativa_Tecnica/
```

### Archivos clave de referencia

| Archivo | Propósito |
| --- | --- |
| `00_Gestion/Estructura_TFM.md` | Índice vivo del TFM (consultar siempre antes de trabajar) |
| `02_Memoria/main.tex` | Documento LaTeX principal |
| `02_Memoria/referencias.bib` | Base bibliográfica (APA 7, backend biber) |
| `01_Universidad/Guia/GUIA Elaboracion TFM ERMA20.pdf` | Estructura y maquetación oficial |
| `01_Universidad/Rubrica/Rúbrica Tribunal TFM ERMA_v1.pdf` | Criterios de evaluación |
| `01_Universidad/Normativa/Normativa TFM ERMA20.pdf` | Normativa general y plazos |
| `01_Universidad/Rubrica/Presentación TFMs ERMA 20.pdf` | Guía de defensa oral |
| `01_Universidad/Guia/Como_buscar_usar_informacion_cientifica.pdf` | Metodología bibliográfica |
| `07_Referencias_Externas/TFG_Linea_Aerea/` | TFG de Mario en LaTeX (referencia de estilo) |

Cuando se necesite contexto bibliográfico, normativo o estructural, **leer estos archivos en lugar de adivinar**.

---

## 5. Índice vivo del TFM

`00_Gestion/Estructura_TFM.md` contiene el índice oficial y actualizado. **Antes de cualquier decisión estructural, consultarlo.** Si se modifica la estructura del TFM (capítulos, secciones), Claude debe actualizar ese archivo para que siga reflejando la realidad.

---

## 6. Tareas principales

### 6.1 Redacción en LaTeX

- La **prosa en la voz de Mario** (capítulos, secciones argumentales) la redacta el subagente **`tfm-redactor`** (modo borrador: devuelve LaTeX para revisar, no toca los `.tex`) o el hilo principal, aplicando la skill **`tono-mario`**. El borrador es material que Mario revisa y hace suyo.
- Para el **LaTeX en sí** (estructura, entornos, compilación y corrección de errores) usar la skill **`latex-writer`** (`.claude/skills/latex-writer/`).
- El texto debe sonar natural y con la voz de Mario; nada de aperturas tipo IA.

### 6.2 Búsqueda de información

- Buscar en internet o en documentos del proyecto. Apoyarse en `Como_buscar_usar_informacion_cientifica.pdf` para criterios de calidad.

### 6.3 Bibliografía

- Guardar todas las fuentes en `02_Memoria/referencias.bib` en formato **biblatex/APA 7**.
- Citar con `\parencite{}` (parentética) o `\textcite{}` (narrativa). **Nunca `\cite{}`**.
- Las entradas se añaden a mano en `referencias.bib`; la compilación de la bibliografía (biber) la gestiona **`latex-writer`**.

### 6.4 PVSyst

- **Guía de manejo:** Mario adjunta captura del programa → Claude indica paso a paso qué hacer.
- **Interpretación:** Mario adjunta capturas o PDFs exportados → Claude valora el diseño y sugiere mejoras.

### 6.5 Presentación PowerPoint

- Fase final del proyecto. Guiarse por `01_Universidad/Rubrica/Presentación TFMs ERMA 20.pdf`. Pendiente hasta que la memoria esté avanzada.

---

## 7. Sistema de subagentes

Cuatro subagentes en `.claude/agents/`:

| Agente | Modelo | Responsabilidad |
| --- | --- | --- |
| `tfm-investigador` | opus | Buscar información técnica, normativa y bibliográfica. Devuelve un dossier con fuentes y entradas `.bib` propuestas (no redacta). |
| `tfm-simulacion` | sonnet | PVSyst: guía paso a paso e interpretación de resultados. |
| `tfm-redactor` | opus | Redacta prosa del TFM en la voz de Mario y devuelve un **borrador** en LaTeX para revisar (no toca los `.tex` ni compila). Precarga las skills `tono-mario` y `latex-writer`. |
| `tfm-archivista` | sonnet | Busca y resume el historial de conversaciones (snapshots + transcripciones) de forma aislada. Envuelve la skill `memoria-conversaciones`. |

**Reglas operativas:**

- Convocatoria **mixta**: Mario los invoca explícitamente o Claude los sugiere cuando proceda.
- Paralelismo máximo: **2 agentes simultáneos** (ajustable).
- Los subagentes **no se invocan entre sí** (sin anidamiento) y arrancan con contexto aislado. Si el `tfm-redactor` necesita material de conversaciones antiguas, invoca la skill `memoria-conversaciones`; la orquestación entre agentes la hace el hilo principal.
- Las entradas de `referencias.bib` se añaden a mano. La revisión previa a los hitos la hace **Mario junto con su tutor**: no hay agente revisor ni hook de tags Git.

---

## 8. Skills

### Skills de proyecto (`.claude/skills/`)

| Skill | Función |
| --- | --- |
| `latex-writer` | Skill **central de LaTeX**: escribir/editar `.tex`, compilar (`pdflatex → biber → pdflatex × 2`) y bucle de auto-debug de errores. Incluye scripts Python. ⚠ El auto-fix modifica `main.tex` — commitear antes de usarlo. |
| `memoria-conversaciones` | Búsqueda y resumen del **historial de conversaciones** del TFM (snapshots + transcripciones `.jsonl`). Se apoya en el índice `00_Gestion/Snapshots/INDICE.md`. La usan el hilo principal y el subagente `tfm-archivista`. |

### Skills globales (`~/.claude/skills/`)

| Skill | Función |
| --- | --- |
| `tono-mario` | Perfil de **voz personal de Mario**. La aplican el `tfm-redactor` y el hilo principal para que la prosa suene a Mario; el borrador resultante lo revisa y firma Mario. |

### Slash commands locales (`.claude/commands/`)

| Skill | Función |
| --- | --- |
| `/snapshot` | Guardar sesión actual en `00_Gestion/Snapshots/YYYY-MM-DD_HHmm_sesion_N.txt` |
| `/interpretar-pvsyst` | Análisis estructurado de resultados PVSyst |

### Slash commands globales (`~/.claude/commands/`)

| Skill | Función |
| --- | --- |
| `/figura-tfm` | Inserción de figura con etiqueta, caption y `\cref` listo |
| `/revisar-capitulo` | Revisión integral de un capítulo (estilo, citas, coherencia) |
| `/normativa` | Búsqueda en los PDFs de `01_Universidad/Normativa/` y `Guia/` |

**Retiradas:** `/compilar-tfm` y `/redactar-latex` se eliminaron al integrar la skill `latex-writer` (compilación); la prosa en la voz de Mario se redacta directamente siguiendo `tono-mario`. `/citar-doi` también se retiró (las entradas de `referencias.bib` se añaden a mano). `/redactar-academico` (global) está archivada en `~/.claude/commands-archive/`.

---

## 9. Workflow Git/GitHub

- **Repo:** `github.com/mariocarsir/TFM-AutoconsumoCPD` (privado).
- **Rama principal:** `main`.
- **Email Git:** `clankergpt0@gmail.com`.
- **Mensajes de commit:** en español, voz imperativa, una línea + cuerpo opcional. Ej.: `Añadir paquetes microtype, cleveref y subcaption`.
- **Tags para hitos:** `inicio-pre-migracion` (existente), `borrador-cap1`, `borrador-final`, `version-tribunal`, etc.
- **`gh` CLI no instalado** → operaciones sobre GitHub (issues, PRs) a mano o vía web.
- **Snapshots de sesión** en `00_Gestion/Snapshots/` (no son commits — son resúmenes para retomar trabajo).

---

## 10. Reglas de trabajo

- **Entorno:** Windows 10 Pro, PowerShell 5.1 (Bash disponible vía Git Bash).
- **Scripts > 20 líneas:** guardar como archivo `.ps1` en la raíz, **no inline** en el chat.
- **Encoding PowerShell 5.1:** scripts `.ps1` sin BOM se leen como Windows-1252 → no usar tildes en strings; localizar archivos con tildes vía `Get-ChildItem` + wildcards (`R*brica*`, `Presentaci*n*`).
- **LaTeX:** secuencia obligatoria `pdflatex → biber → pdflatex → pdflatex` desde `02_Memoria/`, gestionada por la skill `latex-writer`. Cada sección termina de forma lógica. Tablas y figuras llevan siempre `\label{}`.
- **Edición documental:** modificar únicamente los archivos indicados explícitamente en cada tarea.
- **Ortografía y gramática:** español de España.

---

## 11. Software y herramientas

- **LaTeX (MiKTeX)** — Maquetación de la memoria.
- **PVSyst** — Simulación FV.
- **Excel** — Análisis auxiliar de datos.
- **Python 3.12** — Scripts de la skill `latex-writer` (auto-debug de LaTeX).
- *WASP y WindPRO descartados (no aplican al autoconsumo FV).*

---

## 12. Comportamiento general del Asistente

- Respuestas concisas y directas.
- No añadir comentarios ni anotaciones a código o texto que no se haya modificado.
- No crear archivos de documentación generados por la IA salvo petición explícita.
- Usar terminología técnica de energías renovables y CPDs cuando proceda.

---

## 13. Comandos de sesión

### `guardar sesión` (variantes: "guarda sesión", "save session", "continuamos otro día")

- Generar resumen estructurado completo de la sesión.
- Guardar en `00_Gestion/Snapshots/YYYY-MM-DD_HHmm_sesion_N.txt`.
- Contenido: resumen ejecutivo, intercambios clave, archivos creados/afectados, estado del proyecto y próximos pasos.
- **Actualizar el índice** `00_Gestion/Snapshots/INDICE.md`: añadir una fila de la sesión (nº, fecha, temas clave, archivos afectados, decisiones/vistos buenos) para que la skill `memoria-conversaciones` la localice después.

### `leer sesión` (variantes: "cargar sesión")

- Listar todos los `.txt` de `00_Gestion/Snapshots/`.
- Si hay varios, preguntar cuál cargar; presentar contenido para retomar trabajo.

---

## 14. Apéndice: datos clave del CPD

Datos persistentes del consumo del CPD (extrapolados de `03_Datos/Consumo_CPD/raw/datossimulados.csv`):

| Magnitud | Valor |
| --- | --- |
| Consumo anual total | ~3.778 MWh/año |
| Potencia media | 431,29 kW |
| PUE anual | 1,49 |
| Refrigeración | ~1.242 MWh/año |
| Marquesinas FV parking (3.150 m²) | ~990 MWh/año brutos |
| Cobertura estimada | ~22% del total CPD / ~69% de la refrigeración |

Estos valores son la base de los cálculos de dimensionado y rentabilidad. Si se actualizan los datos de partida (CSV, perfil horario), recalcularlos y reflejar el cambio aquí.

---

## 15. Manual del workspace (documento vivo)

`00_Gestion/MANUAL_WORKSPACE.md` es el manual de uso del espacio de trabajo (flujo, skills, subagentes, slash commands, tags Git, reglas de entorno). Está pensado para que alguien externo pueda operar el workspace.

**Es un documento vivo:** siempre que en una sesión se añada/retire o cambie una skill, un subagente, un slash command, un hook o una regla del flujo de trabajo, **actualizar ese manual para reflejar la función vigente** (no el historial del cambio). Mantener sincronizadas sus tablas con el contenido real de `.claude/agents/`, `.claude/commands/`, `.claude/skills/` y `~/.claude/commands|skills/`.
