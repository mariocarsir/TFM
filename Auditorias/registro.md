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
| AUD-002 | Pipeline bibliográfico y PVsyst nunca ejercitados (carpetas vacías) | Doctrina/realidad | Bloqueante | pendiente | 2026-08-08 | No es un fix de fichero, es una alerta de proceso no probado. Reevaluar cuando se use `bibliotecario-pdf` o PVsyst por primera vez |
| AUD-003 | El repo mezcla el TFM con artefactos de un vault de Obsidian (`wiki/`, `inbox/`, `.obsidian/`, `.claude-obsidian.json`, `.raw/`) | Orden | Fricción | pendiente | 2026-08-08 | Origen: Mario eligió este workspace como bóveda de Obsidian. La parte `Skills/obsidian*` se resolvió (ver AUD-005, commit `c2ede82`). Queda abierto si el resto debe separarse a otro repo |
| AUD-004 | 3 zips versionados duplicando contenido ya extraído (~19 MB) | Orden | Fricción | aplicado | 2026-08-08 | Destrackeados con `git rm --cached`, quedan en disco. Commit `9b94c84` |
| AUD-005 | Anidamiento `carpeta/carpeta/` en `obsidian` y `obsidian-vault-maintainer` | Orden | Fricción | aplicado | 2026-08-08 | Desanidadas y trasladadas a `.claude/skills/`. Commit `c2ede82` |
| AUD-006 | Entrada de `.gitignore` apuntando a una ruta que ya no existe en disco | Orden | Cosmético | aplicado | 2026-08-08 | Retirada en el mismo commit que AUD-004: `9b94c84` |
| AUD-007 | `CLAUDE.md` declara `Presentaciones/` (no existe) y `Skills/` con contenido desactualizado | Doctrina/realidad | Cosmético | aplicado | 2026-08-08 | Ambas filas retiradas del mapa de carpetas. Commit `6f00dd7` |
| AUD-008 | `Skills/optimizador-prompts.skill` sin desempaquetar, sin ninguna dependencia que lo referencie | Orden | Cosmético | pendiente | 2026-08-08 | Detectado al aplicar AUD-007. Mario lo gestiona manualmente, fuera de esta pasada |
| AUD-009 | Nombre de fichero con una nota-recordatorio sin resolver como nombre (`Datos/Consumo CPD/datos/miraaverfalta...zip`) | Orden | Cosmético | pendiente | 2026-08-08 | Detectado, no priorizado |
| AUD-010 | Configuración de `.obsidian/` (salvo `workspace.json`) versionada sin necesidad aparente | Orden | Cosmético | pendiente | 2026-08-08 | Detectado, no priorizado. Relacionado con AUD-003 |

## Historial de auditorías

Permite calcular la antigüedad de los hallazgos `pendiente`.

| Fecha | Ámbito | Informe | Hallazgos | Aplicados |
| --- | --- | --- | --- | --- |
| 2026-08-08 | completo | `Auditorias/2026-08-08-auditoria.md` | 10 (7 priorizados + 3 no priorizados) | 5 (AUD-001, AUD-004, AUD-005, AUD-006, AUD-007) |
