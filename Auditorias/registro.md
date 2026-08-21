# Registro de hallazgos de auditoría

Tabla viva del meta-flujo del proyecto. La mantiene la skill `/auditor`: la lee en la Fase 0
antes de analizar nada y la actualiza en la Fase 4.

Los ID son correlativos y **nunca se reutilizan**, ni siquiera si el hallazgo queda obsoleto.

## Estados

| Estado | Significado | Efecto en la siguiente auditoría |
| --- | --- | --- |
| `pendiente` | Propuesto, todavía sin resolver | **Reaparece**, indicando su antigüedad en número de auditorías |
| `aplicado` | Ejecutado, con hash de commit en la Nota | No reaparece. Si el síntoma vuelve, se abre un hallazgo nuevo etiquetado "regresión de AUD-NNN" |
| `rechazado` | Mario dijo que no. El motivo va siempre en la Nota | **No se vuelve a proponer nunca** |
| `obsoleto` | Dejó de aplicar porque el proyecto cambió | No reaparece |

## Hallazgos

| ID | Hallazgo | Eje | Severidad | Estado | Fecha | Nota |
| --- | --- | --- | --- | --- | --- | --- |
| AUD-001 | `humanizer` en `Skills/`, no invocable | Doctrina/realidad | Bloqueante | aplicado | 2026-08-08 | Movida a `.claude/skills/humanizer/`. Commit `a18a228` |
| AUD-002 | Pipeline bibliográfico y PVsyst nunca ejercitados (carpetas vacías) | Doctrina/realidad | Bloqueante | obsoleto | 2026-08-08 | Cerrado el 2026-08-21: `bibliotecario-pdf` se ha ejercitado con éxito 4 veces y de ahí salieron 6 de los 7 hallazgos de esa pasada. La mitad de PVsyst sigue sin probarse y se reabre por separado como AUD-018 para no darla por buena de rebote |
| AUD-003 | El repo mezcla el TFM con artefactos de un vault de Obsidian (`wiki/`, `inbox/`, `.obsidian/`, `.claude-obsidian.json`, `.raw/`) | Orden | Fricción | pendiente | 2026-08-08 | Origen: Mario eligió este workspace como bóveda de Obsidian. La parte `Skills/obsidian*` se resolvió (ver AUD-005, commit `c2ede82`). Decisión de Mario (2026-08-08): no se separa a otro repositorio con control de versiones propio. Se deja como está por ahora; si el volumen de artefactos de Obsidian crece mucho, valorar agruparlos en una carpeta `Obsidian/` dedicada dentro de este mismo repo |
| AUD-004 | 3 zips versionados duplicando contenido ya extraído (~19 MB) | Orden | Fricción | aplicado | 2026-08-08 | Destrackeados con `git rm --cached`, quedan en disco. Commit `9b94c84` |
| AUD-005 | Anidamiento `carpeta/carpeta/` en `obsidian` y `obsidian-vault-maintainer` | Orden | Fricción | aplicado | 2026-08-08 | Desanidadas y trasladadas a `.claude/skills/`. Commit `c2ede82` |
| AUD-006 | Entrada de `.gitignore` apuntando a una ruta que ya no existe en disco | Orden | Cosmético | aplicado | 2026-08-08 | Retirada en el mismo commit que AUD-004: `9b94c84` |
| AUD-007 | `CLAUDE.md` declara `Presentaciones/` (no existe) y `Skills/` con contenido desactualizado | Doctrina/realidad | Cosmético | aplicado | 2026-08-08 | Ambas filas retiradas del mapa de carpetas. Commit `6f00dd7` |
| AUD-008 | `Skills/optimizador-prompts.skill` sin desempaquetar, sin ninguna dependencia que lo referencie | Orden | Cosmético | pendiente | 2026-08-08 | Detectado al aplicar AUD-007. Mario lo gestiona manualmente, fuera de esta pasada |
| AUD-009 | Nombre de fichero con una nota-recordatorio sin resolver como nombre (`Datos/Consumo CPD/datos/miraaverfalta...zip`) | Orden | Cosmético | pendiente | 2026-08-08 | Detectado, no priorizado |
| AUD-010 | Configuración de `.obsidian/` (salvo `workspace.json`) versionada sin necesidad aparente | Orden | Cosmético | pendiente | 2026-08-08 | Detectado, no priorizado. Relacionado con AUD-003 |
| AUD-011 | El guard de aislamiento de jobs en segundo plano empujaba a escribir el `.md` del resumen por trozos, con riesgo de corromper tildes y ecuaciones LaTeX | Doctrina/realidad | Fricción | aplicado | 2026-08-21 | Volcado único con heredoc entrecomillado + verificación posterior; el bloqueo de `Write` se declara conocido de antemano para no reintentarlo. Descartadas las vías `bgIsolation: none` (abre colisiones entre jobs) y `EnterWorktree` (contradice AUD-015). Commit `10d367b` |
| AUD-012 | `resumen-tecnico/SKILL.md` se contradecía: Exhaustivo prometía "nada omitido" y otra regla ordenaba muestrear todo documento de más de 80 pp. | Doctrina/realidad | Bloqueante | aplicado | 2026-08-21 | Reformulado tras objeción acertada de Mario (que cada densidad cueste distinto es el diseño, no el fallo). Solución elegida por él: eliminar los umbrales por páginas, el alcance lo fija solo la densidad. Commit `5ce1b49` |
| AUD-013 | La pregunta de densidad con `AskUserQuestion` era incondicional; un subagente en segundo plano no tiene a quién preguntar | Doctrina/realidad | Fricción | aplicado | 2026-08-21 | Absorbido por AUD-012: la densidad la elige siempre Mario, se pregunta solo si el encargo no la trae. Mismo commit `5ce1b49` |
| AUD-014 | El patrón de ingesta al vault de Obsidian se re-deducía desde cero en cada invocación (~30-45k tokens) | Repetición/automatización | Fricción | aplicado | 2026-08-21 | Consolidado en `.claude/skills/resumen-tecnico/references/ingesta-obsidian.md`, verificado contra el ledger real. La skill sigue sin ingestar sola: solo documenta el cómo. Commit `af74d67` |
| AUD-015 | Los worktrees residuales de `.claude/worktrees/**` inutilizaban el linter del vault: 182 hallazgos, 0 reales | Orden | Fricción | aplicado | 2026-08-21 | Eliminados los 6 worktrees y sus ramas (todos fusionados, limpios y sin actividad), destrackeadas 6 entradas `gitlink` espurias del índice y añadido `.claude/worktrees/` al `.gitignore`. Linter verificado: de 182 hallazgos a 0. Commit `1b5221c` |
| AUD-016 | `python3` es un nombre ambiguo en Windows: el alias de la Microsoft Store va por delante en el PATH de Git Bash | Doctrina/realidad | Cosmético | aplicado | 2026-08-21 | Al re-verificar, `python3` sí resolvía al Python 3.12.10 real, así que se documenta como ambigüedad (con comprobación previa de 3 candidatos) y no como ausencia. Commit `5ce8066` |
| AUD-017 | Locks de git huérfanos por jobs concurrentes sobre el mismo checkout | Doctrina/realidad | Fricción | aplicado | 2026-08-21 | Protocolo de 3 pasos (esperar → inspeccionar `mtime` → confirmar con `Get-Process`) sacado a su propia memoria persistente `feedback_git_index_lock.md`. Descartado meterlo en `CLAUDE.md`: se carga en cada sesión y cobraría peaje permanente. Sin commit, vive fuera del repositorio |
| AUD-018 | El flujo de PVsyst sigue sin ejercitarse (`Datos/PVsyst/` sin informes, `piloto-pvsyst` sin usar) | Doctrina/realidad | Bloqueante | pendiente | 2026-08-21 | Mitad superviviente de AUD-002. No es un fix de fichero: es el núcleo técnico del TFM sin probar. Reevaluar en cuanto exista la primera simulación |

## Historial de auditorías

Permite calcular la antigüedad de los hallazgos `pendiente`.

| Fecha | Ámbito | Informe | Hallazgos | Aplicados |
| --- | --- | --- | --- | --- |
| 2026-08-08 | completo | `Auditorias/2026-08-08-auditoria.md` | 10 (7 priorizados + 3 no priorizados) | 5 (AUD-001, AUD-004, AUD-005, AUD-006, AUD-007) |
| 2026-08-21 | con foco: skills `resumen-tecnico` e ingesta a Obsidian | `Auditorias/2026-08-21-auditoria.md` | 8 (AUD-011 a AUD-018) | 7 (AUD-011 a AUD-017). AUD-018 queda abierto; AUD-002 se cierra como obsoleto |
