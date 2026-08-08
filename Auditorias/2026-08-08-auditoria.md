# Auditoría del meta-flujo — 2026-08-08

**Ámbito:** completo.

**Resumen en tres líneas:** la skill `humanizer`, marcada obligatoria en `CLAUDE.md`, no era
invocable porque vivía fuera de `.claude/skills/`; el pipeline bibliográfico y PVsyst nunca se
han ejercitado (carpetas vacías); y el repositorio arrastraba ~19 MB de duplicados versionados
(zip + extraído) más una mezcla de dos proyectos distintos bajo el mismo `.git`.

## Mapa de recursos (Fase 0)

| Capacidad | Recurso que ya la cubre |
| --- | --- |
| Redactar capítulos con voz propia | `redactor-humanizador` |
| Procesar bibliografía nueva | `bibliotecario-pdf` |
| Cálculos económicos (VAN/TIR/LCOE) | `analista-economico` |
| Dimensionado FV / PVsyst / almacenamiento | `ingeniero-dominio` |
| Verificar cifras y normativa | `investigador-cientifico` |
| Cierre de capítulo (formato, citas) | `revisor-calidad` |
| Auditar memoria persistente | `conservador-memoria` |
| Auditar meta-flujo | skill `auditor` (`.claude/skills/auditor/`) |
| Humanización anti-Turnitin | skill `humanizer` — al inicio de esta auditoría, en `Skills/`, sin cargar |
| Gestión de vault Obsidian | skills `obsidian`, `obsidian-vault-maintainer` — al inicio, en `Skills/`, sin relación declarada con el TFM |

Registro previo: vacío. Primera auditoría real del proyecto.

## Hallazgos priorizados (7 de 7 máximo)

| # | Eje | Severidad | Hallazgo | Coste | Consecuencia si no se arregla | Acción propuesta |
| --- | --- | --- | --- | --- | --- | --- |
| AUD-001 | Doctrina/realidad | Bloqueante | `humanizer` en `Skills/humanizer/humanizer/SKILL.md`, no en `.claude/skills/`: no invocable | Minutos | Cada capítulo se cierra sin pasar por Turnitin-humanizer pese a ser obligatorio | Mover a `.claude/skills/humanizer/` |
| AUD-002 | Doctrina/realidad | Bloqueante | `Bibliografia/PDFs/`, `Bibliografia/Resumenes/` y `Datos/PVsyst/` no existen; `Memoria/Capitulos/` tiene 1 de 11 capítulos | No aplicable — es una alerta, no un fix | La primera cita real o la primera simulación PVsyst descubre errores del pipeline en el peor momento | Ninguna hoy; reevaluar en el primer uso real |
| AUD-003 | Orden | Fricción | El repo mezcla el TFM con artefactos de un vault de Obsidian (`wiki/`, `inbox/`, `.obsidian/`, `.claude-obsidian.json`, `.raw/`, `Skills/obsidian*`), no declarados en `CLAUDE.md` | Decisión de Mario | Confusión sobre el alcance real del repositorio | Aclarar origen y decidir si se separa |
| AUD-004 | Orden | Fricción | 3 zips versionados duplican contenido ya extraído (~19 MB): `Skills/obsidian.zip`, `Skills/obsidian-vault-maintainer.zip`, `Documentacion de apoyo/TFG_Linea_Aerea.zip` | 10 min | Clones y `git pull` cada vez más lentos | `git rm --cached` + `*.zip`/`*.rar` en `.gitignore` |
| AUD-005 | Orden | Fricción | Anidamiento `carpeta/carpeta/` en `obsidian` y `obsidian-vault-maintainer`, resultado de extraer zips | 5 min | Rutas confusas al referenciar las skills | Aplanar y trasladar a `.claude/skills/` |
| AUD-006 | Orden | Cosmético | `.gitignore` excluye una ruta que ya no existe en disco | 1 min | Ninguna funcional; solo ruido | Borrar la línea |
| AUD-007 | Doctrina/realidad | Cosmético | `CLAUDE.md` declara `Presentaciones/` (no existe) y describe `Skills/` con contenido desactualizado | Trivial | El mapa de carpetas deja de ser fiable | Retirar ambas filas |

**No priorizados** (quedan en `Auditorias/registro.md` como `pendiente`):
- Nombre de fichero con una nota-recordatorio sin resolver como nombre (`Datos/Consumo CPD/datos/miraaverfalta...zip`).
- Configuración de `.obsidian/` (salvo `workspace.json`) versionada sin necesidad aparente.
- `Skills/optimizador-prompts.skill`, un `.zip` sin desempaquetar y sin ninguna dependencia que lo referencie (surgió al aplicar AUD-007).

**Reincidentes:** ninguno — primera auditoría.

## Decisiones de Mario en esta pasada

- **AUD-001** — aprobado. Aplicado: `humanizer` movida a `.claude/skills/humanizer/` (commit `a18a228`).
- **AUD-002** — aclarado, sin acción aplicable hoy. Queda `pendiente` para reevaluar en el primer uso real del pipeline.
- **AUD-003** — explicado el origen (bóveda de Obsidian sobre este mismo workspace), pero sin decisión sobre separar el repo. Queda `pendiente`. La sub-parte `Skills/obsidian*` sí se resolvió, al aprobar AUD-005 extendido (ver abajo).
- **AUD-004** — aprobado. Aplicado junto con AUD-006 (commit `9b94c84`).
- **AUD-005** — aprobado, y ampliado: Mario pidió además trasladar `obsidian` y `obsidian-vault-maintainer` a `.claude/skills/` (no solo desanidarlas) y borrar `Skills/`. Aplicado (commit `c2ede82`).
- **AUD-006** — aprobado. Aplicado junto con AUD-004 (commit `9b94c84`), mismas líneas del mismo fichero.
- **AUD-007** — aprobado, con diff mostrado antes de escribir por ser puerta dura sobre `CLAUDE.md`. Aplicado (commit `6f00dd7`).
- **Decisión adicional, fuera de los 7 hallazgos**: al borrar `Skills/`, apareció `optimizador-prompts.skill` sin desempaquetar. Se comprobó que no tiene ninguna referencia operativa (solo aparecía en la fila de `CLAUDE.md` ya retirada y en la documentación de diseño del propio auditor). Mario decidió moverlo manualmente fuera de esta pasada; queda registrado como AUD-008 `pendiente`.

## Commits de esta auditoría

```
a18a228 auditoría(AUD-001): mueve humanizer a .claude/skills/ para que sea invocable
c2ede82 auditoría(AUD-005): desanida obsidian y obsidian-vault-maintainer, y las traslada a .claude/skills/
9b94c84 auditoría(AUD-004,AUD-006): destrackea zips duplicados y limpia entrada obsoleta de .gitignore
6f00dd7 auditoría(AUD-007): retira Presentaciones/ y Skills/ del mapa de carpetas
```
