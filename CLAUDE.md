# CLAUDE.md — TFM de Mario Carrión Sirvent

> Generado a partir de la plantilla de entrevista de Gonzalo Aguirre (Máster ERMA, UPM).
> Este archivo orquesta el proyecto: el conocimiento vive en los agentes de `.claude/agents/`
> y en la memoria persistente, no aquí.

## Contexto maestro

- **Autor:** Mario Carrión Sirvent.
- **Titulación:** Máster ERMA (Energías Renovables y Medio Ambiente), UPM.
- **Tema:** Autoconsumo fotovoltaico con almacenamiento en un centro de proceso de datos (CPD), Madrid.
- **Tutor:** Julio Amador Guerra.
- **Fecha de entrega estimada:** 15 de septiembre de 2026.
- **Idioma:** español (tildes y eñes siempre, nunca sustitutos ASCII).
- **Documento:** LaTeX, heredando `MUXLaTeX.cls` del TFG de Mario. Guía tipográfica completa ya extraída en `Normativa TFM/guia_tipografica.md` — no releer el `.cls`, esa guía es la fuente de verdad.
- **Portada:** NO hereda la del TFG. Sigue `Plantillas/Portada TFM.docx` (logos UPM + Máster ERMA en `Plantillas/`).
- **Bibliografía:** estilo IEEEtran, fichero `biblio.bib`.
- **Normativa ERMA:** máx. 150 páginas, entrega en PDF firmado digitalmente, estructura índice → memoria → anexos.
- **Universidad usa Turnitin:** el flujo de humanización con voz propia (skill `humanizer`) es OBLIGATORIO en cada capítulo, no opcional.
- **Índice de trabajo:** `Memoria/indice_propuesto.md` — 13 capítulos + anexos, validado como **provisional** (revisable con el tutor). El pliego de condiciones se eliminó el 05/09/2026 y su función la asume, en versión ligera, el cap. 8 «Explotación: mantenimiento y garantías». El estudio de seguridad y salud (cap. 11) queda pendiente de confirmar con Julio: es opcional por normativa ERMA y ninguno de los tres TFM de referencia lo incluye. Sin portada de firmas y sin abstract en inglés (06/09/2026). Comparación estructural completa en `Memoria/analisis/comparacion-estructura-tfm.md`.
- **La rúbrica del tribunal manda tanto como la guía:** `Normativa TFM/Rúbrica Tribunal TFM ERMA_v1.pdf` reparte 20 % formato, 55 % contenidos y 25 % defensa. Ojo al criterio del 10 % «Marco socio-económico y medioambiental / Marco Normativo»: se satisface con el presupuesto **y/o** el impacto ambiental, así que el capítulo medioambiental refuerza la nota pero no la sostiene — de ahí que vaya acotado.
- **La normativa NO es citable:** ninguna ley, real decreto, real decreto-ley, circular o resolución entra en `biblio.bib` ni aparece en el capítulo de Referencias. Toda la normativa aplicable se relaciona en el apartado 2.5, con título completo, qué regula y cómo aplica al proyecto (modelo: apartado 1.4 de `TFM-MAD9_signed.pdf`). En el texto, forma larga la primera mención y forma corta después. Si una norma no merece figurar en 2.5, se consulta a Mario antes de mencionarla suelta.
- **Cálculo:** PVsyst para la simulación fotovoltaica (núcleo del TFM); Excel para todo lo que PVsyst no cubre (modelo horario de almacenamiento, análisis económico: VAN, TIR, LCOE, sensibilidad).
- **TFM de referencia** (los tres indexados en `conocimiento fotovoltaico/Referencia/`; comparativa transversal en `analisis-comparativo-tfm-referencia-erma.md`):
  - **Primario — `TFM-MAD9_signed.pdf`** (Diego Fernandes Alves, 2025, centro logístico Amazon MAD9): arquitectura y resultados esperables. El más reciente, el único con almacenamiento realmente dimensionado, escala comparable y perfil de consumo 24/7.
  - **`TFM_M_A.pdf`** (Manuel Arcas, 2024, San Martín PYL; cotutor Julio Amador): método de cálculo — cargas de viento CTE, strings, P50/P90, modelo Excel de gestión de batería.
  - **`TFM_ANDREA_BARRIOS_L.pdf`** (Andrea Barrios López, 2023): tramitación y economía — procedimiento administrativo con plazos, escenarios de precio, subvenciones, dimensionado eléctrico con ecuaciones.
- **Reuniones con el tutor:** sin frecuencia fija, puntuales por hitos — no asumir cadencia regular al planificar seguimiento.
- **Git:** Mario no tenía experiencia previa; explicar lo mínimo imprescindible (qué es un commit, cómo revisar el historial) según haga falta.

## Mapa de carpetas

La estructura es la que Mario ya tenía montada, sin renombrar a convención numérica:

| Carpeta | Contenido |
| --- | --- |
| `Memoria/` | Fuente LaTeX de la memoria + PDF compilado. Incluye `indice_propuesto.md`. |
| `Bibliografia/Fuentes/` | PDFs originales de bibliografía. Incluye la subcarpeta `Normativa/` con la normativa sectorial aplicable al proyecto (leyes, reales decretos, circulares) y `NormativaLinks.xlsx` como ficha de seguimiento (título, vigencia, resumen, URL) — no confundir con `Normativa TFM/`, que es la normativa ERMA del propio máster. |
| `Bibliografia/Resumenes/` | Resúmenes densos generados por `bibliotecario-pdf` vía skill `resumen-tecnico` (PDFs de papers/normas/manuales citables), únicas fuentes citables. |
| `Datos/` | `PVsyst/` (informes de simulación) y `Consumo CPD/` (perfil horario de consumo). |
| `Normativa TFM/` | Normativa ERMA oficial y `guia_tipografica.md`. |
| `Plantillas/` | Portada oficial, plantilla de presentación/defensa, resumen TFM. |
| `Imagenes/` | Logos y figuras del documento. |
| `Documentacion de apoyo/` | TFM de referencia, apuntes de las asignaturas, TFG propio de Mario. |
| `conocimiento fotovoltaico/` | Base de conocimiento de `piloto-pvsyst`: `Manuales PVsyst/` (14 manuales oficiales v6/v7/v8), `Referencia/` (datasheets, notas técnicas, guía de diseño generada, resúmenes de apuntes/presentaciones/vídeos/TFMs no-citables generados por `bibliotecario-pdf` vía skill `resumen-tecnico`) y `Capturas/` (pantallazos de trabajo, formato `AAAA-MM-DD_HHMM.png`). |
| `Auditorias/` | Informes de auditoría del meta-flujo y `registro.md` con el estado de cada hallazgo. |
| `.claude/agents/` | Agentes especializados (tabla abajo). |

**Memoria persistente:** este proyecto usa el sistema de memoria automática de Claude Code (fuera de esta carpeta, vinculado al directorio de trabajo). No crear una carpeta `memory/` local: sería redundante.

## Catálogo de agentes

| Agente | Cuándo delegar |
| --- | --- |
| `bibliotecario-pdf` | Mario aporta un PDF/DOCX/PPTX/TXT o vídeo YouTube nuevo de bibliografía a resumir (paper, norma, apuntes, presentación, TFM de referencia). Invoca la skill `resumen-tecnico` automáticamente. |
| `redactor-humanizador` | Redactar o desarrollar cualquier sección/capítulo de la memoria. |
| `analista-economico` | Estructurar o revisar cálculos en Excel: modelo horario de almacenamiento, VAN, TIR, LCOE, sensibilidad. |
| `ingeniero-dominio` | Cualquier decisión o cálculo de ingeniería: dimensionado FV, PVsyst, almacenamiento, autoconsumo, tramitación. |
| `piloto-pvsyst` | Manejo operativo de PVsyst: guía paso a paso de la interfaz, dudas sobre capturas de pantalla del programa, validación de resultados de simulación. |
| `investigador-cientifico` | Verificar una cifra, norma o dato de mercado antes de que entre en el documento. |
| `revisor-calidad` | Cerrar una sección o capítulo grande: formato, citas, terminología, compilación, riesgo Turnitin residual. |
| `conservador-memoria` | Tras un hito importante o corrección de rumbo: auditar memorias obsoletas o contradictorias. |
| `/auditor` (skill) | Mario duda del flujo de trabajo y quiere diagnóstico de herramientas, orden y automatización. |

## Reglas operativas

1. **Delegar siempre**: al recibir una petición, identificar el agente ideal e invocarlo con un resumen telegráfico del encargo.
2. **Verificar siempre**: ninguna edición al documento se cierra sin compilar (`pdflatex → bibtex → pdflatex ×2`, 0 referencias/citas indefinidas). `MUXLaTeX.cls` usa `\bibliographystyle{IEEEtran}` + BibTeX clásico, no biblatex: el backend es `bibtex`, no `biber`, y la cita correcta es `\cite{}` (nunca `\parencite`/`\textcite`, que son de biblatex).
3. **Flujo de redacción fijo**: `redactor-humanizador` genera el borrador → Mario corrige y añade voz propia → skill `humanizer` (modo ADVANCED por defecto, STEALTH si ya está muy detectado) → verificación LaTeX. Nunca saltarse un paso.
4. **Memoria antes que repetición**: si algo se explicó dos veces, va a memoria persistente.
5. **Cifras canónicas**: cada número del documento sale de una fuente única (informe PVsyst, hoja Excel, resumen de `Bibliografia/Resumenes/`), nunca de la memoria del modelo. Ante la duda, recalcular desde la fuente.
6. **Correcciones de estilo = ley**: lo que Mario rechace una vez no se vuelve a proponer; se registra en la memoria de estilo (`feedback_estilo_mario`) y en la tabla de vocabulario prohibido de `Skills/humanizer/humanizer/SKILL.md`.
7. **Auditar por hitos**: al cerrar cada capítulo grande, pasar `revisor-calidad` y `conservador-memoria`.
8. **Ortografía completa del español** en todo lo generado: tildes y eñes siempre, nunca sustitutos ASCII.
9. **Commit proactivo** tras cada cambio relevante y verificado, sin preguntar. El título sigue obligatoriamente la «Convención de títulos de commit» de abajo; el cuerpo del mensaje explica el detalle. El push sí se consulta. El PDF compilado también se versiona: es el entregable.
10. **Prohibido citar de memoria del modelo**: toda afirmación con cita debe ser trazable a un PDF que Mario tenga y haya aprobado, vía `bibliotecario-pdf` + skill `resumen-tecnico`.

## Convención de títulos de commit

Aplica **solo a la primera línea** del mensaje (el título). El cuerpo se escribe en español normal, con tildes y eñes, y conserva los trailers de coautoría.

**Forma:**

1. **Máximo 4 palabras, prioriza 3.** Solo se sube a 4 cuando con 3 el título no queda claro o se parecería demasiado a otro ya existente.
2. **Solo letras y números.** Nada de espacios, guiones, dos puntos, tildes, eñes ni emojis. `Diseño` → `Diseno`.
3. **Palabras pegadas, inicial de cada una en mayúscula** (PascalCase): `VariantesV3Parcela`.
4. **Siglas enteras en mayúsculas**: CPD, FV, PPA, SIG, BIPV, PVsyst → `DocumentacionAutoconsumoCPD`, `ResumenM6T13SIG`.
5. **Orden de general a concreto**: la primera palabra da el contexto y cada siguiente concreta a la anterior. `Variantes` → `V3` → `Parcela`.
6. **El título refleja el cambio de fondo, no un detalle secundario.** Si un commit corrige una superficie *y* desbloquea una variante entera por normativa, el título habla del desbloqueo: `VariantesV3DesbloqueoNormativa`, no `VariantesV2Marquesinas`.
7. **Unicidad**: ningún título repetido ni casi idéntico a otro del historial. Si dos commits tocan lo mismo, se separan por la palabra final (`NormativaFichaExcel` vs `NormativaFichaVerificacion`).

**Prefijos obligatorios por tipo:**

| Tipo de commit | Forma | Ejemplo |
| --- | --- | --- |
| Vault de Obsidian (`wiki/`, `.obsidian/`) | `Obsidian` + acción del plugin (`Fix`, `Save`…) + 2 palabras. **Aquí se permiten 4 palabras siempre.** | `ObsidianSaveContrastePresentaciones` |
| Merge | `Merge` + qué se integra | `MergeVariantesAutoconsumo` |
| Resumen de presentación del máster | `Resumen` + código `M<módulo>T<tema>` + tema | `ResumenM6T4Inversores` |
| Resto | contexto + concreción | `BibliografiaFuentesReorganizacion` |

**Reescritura de historial:** los títulos antiguos solo se corrigen en commits **no publicados** (`origin/master..master`). Lo ya empujado a `origin` se queda como está: renombrarlo exigiría `push --force`, que está prohibido. Antes de cualquier reescritura, rama de respaldo (`git branch backup-<motivo>`) y verificación posterior de que `git diff <backup> <rama>` sale vacío.

## Pipeline bibliográfico

```text
PDF/DOCX/PPTX/TXT/YouTube nuevo
         ↓
    bibliotecario-pdf (invoca skill resumen-tecnico)
         ↓
    Detecta tipo: paper/manual/normativa/apuntes/presentacion/tfm-referencia/video
         ↓
    Pregunta nivel de densidad: Ejecutivo / Estándar / Exhaustivo
         ↓
    Extrae preservando ecuaciones LaTeX, tablas, gráficas, procedimientos
         ↓
    Resume en dos pasos: extracción exhaustiva → limpieza/organización
         ↓
    Genera .md con frontmatter compatible Obsidian
         ↓
    Si es normativa → Bibliografia/Fuentes/Normativa/Resumenes/<slug-norma>.md
                      (NO genera entrada en biblio.bib: alimenta el apartado 2.5)
    Si es citable → Bibliografia/Resumenes/<Autor>_<Año>.md
    Si es no-citable → conocimiento fotovoltaico/Referencia/<slug-titulo>.md
         ↓
    redactor-humanizador SOLO cita a partir de estos resúmenes
         ↓
    revisor-calidad contrasta cada cifra citada contra el resumen
```

## Consejos heredados (de la experiencia de Gonzalo)

- Resume cada PDF una sola vez y bien: reprocesar bibliografía quema tiempo y dinero.
- Verifica cada cifra contra su fuente ANTES de que se propague por el documento.
- La memoria persistente es lo que convierte a Claude en compañero de proyecto en vez de un chat que empieza de cero cada día.
- Empieza la defensa (guion y slides en `Presentaciones/`) semanas antes de la entrega, no después — con el 15 de septiembre como fecha límite, no dejarlo para el final.
