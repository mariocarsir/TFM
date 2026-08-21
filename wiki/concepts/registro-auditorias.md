---
type: concept
title: "Registro de auditorías"
created: 2026-08-21
updated: 2026-08-21
status: evergreen
tags:
  - concept
  - tfm
  - auditoria
  - registro
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-skill-auditor]]"
  - "[[tfm-skills]]"
  - "[[aud-001-humanizer-no-invocable]]"
  - "[[aud-002-pipeline-sin-ejercitar]]"
  - "[[aud-003-repo-mezclado-con-vault]]"
  - "[[aud-004-zips-versionados]]"
  - "[[aud-005-skills-anidadas]]"
  - "[[aud-006-gitignore-ruta-fantasma]]"
  - "[[aud-007-claude-md-desactualizado]]"
  - "[[aud-008-optimizador-prompts-sin-usar]]"
  - "[[aud-009-fichero-con-nombre-recordatorio]]"
  - "[[aud-010-config-obsidian-versionada]]"
  - "[[aud-011-escritura-por-trozos]]"
  - "[[aud-012-densidad-contra-paginas]]"
  - "[[aud-013-pregunta-densidad-incondicional]]"
  - "[[aud-014-ingesta-obsidian-sin-documentar]]"
  - "[[aud-015-worktrees-residuales]]"
  - "[[aud-016-python3-ambiguo-windows]]"
  - "[[aud-017-locks-git-huerfanos]]"
  - "[[aud-018-pvsyst-sin-ejercitar]]"
---

# Registro de auditorías

Índice de todos los hallazgos producidos por la skill [[tfm-skill-auditor]] sobre el meta-flujo del TFM: las herramientas, la organización de los ficheros y lo que debería estar automatizado y no lo está. **Nunca sobre el contenido del TFM en sí** — esa frontera es deliberada, para no dar veredictos que contradigan a los agentes de dominio.

Cada fila enlaza a una ficha con el detalle completo. La fuente de verdad operativa sigue siendo `Auditorias/registro.md` en el repositorio; estas notas son su versión navegable y explicada.

## Qué significa cada estado

- **Cerrado** — o aceptaste el cambio y ya está aplicado, o el hallazgo dejó de aplicar porque el proyecto avanzó. No hay nada que hacer.
- **Pendiente** — se dejó para más adelante **a propósito**, no por olvido. Reaparece en la siguiente auditoría indicando su antigüedad.

Hay un tercer estado posible, **rechazado** (dijiste que no y no se vuelve a proponer nunca), que hasta hoy no ha usado ningún hallazgo: los tres que rechazaste en la primera vuelta del 20/08/2026 los reconsideraste y aprobaste al día siguiente.

Los identificadores son correlativos y **nunca se reutilizan**, ni siquiera cuando un hallazgo queda obsoleto.

## Todos los hallazgos

| ID | Fecha | Estado | Qué problema trataba de resolver | Decisión planteada | Decisión adoptada |
| --- | --- | --- | --- | --- | --- |
| [[aud-001-humanizer-no-invocable\|AUD-001]] | 2026-08-08 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | `CLAUDE.md` declara obligatorio pasar cada capítulo por el humanizador anti-Turnitin, pero la skill vivía en una carpeta suelta (`Skills/`) desde la que Claude no puede cargarla. Es decir: una regla obligatoria que era imposible de cumplir. | Mover la skill a `.claude/skills/humanizer/`, que es la única ruta desde la que Claude carga skills. | Aprobada tal cual y aplicada el mismo día. |
| [[aud-002-pipeline-sin-ejercitar\|AUD-002]] | 2026-08-08 | **Cerrado** — Dejó de aplicar porque el proyecto avanzó. | Todo el flujo de bibliografía y toda la parte de simulación fotovoltaica estaban descritos sobre el papel, pero nunca se habían ejecutado ni una vez. Las carpetas `Bibliografia/Resumenes/` y `Datos/PVsyst/` estaban vacías. | Ninguna acción inmediata: no es un fallo que se arregle editando un fichero, es una alerta de proceso sin probar. Se dejó anotado para reevaluarlo en el primer uso real. | Se aceptó dejarlo en observación. El 21/08/2026 se cerró la mitad bibliográfica y la mitad de PVsyst se reabrió por separado como [[aud-018-pvsyst-sin-ejercitar]]. |
| [[aud-003-repo-mezclado-con-vault\|AUD-003]] | 2026-08-08 | **Pendiente** — Se dejó para más adelante, a propósito. | En la misma carpeta y bajo el mismo control de versiones conviven dos cosas distintas: el TFM (memoria, datos, bibliografía) y toda la maquinaria del vault de Obsidian (`wiki/`, `inbox/`, `.obsidian/`, `.raw/`). Confunde cuál es realmente el alcance del repositorio. | Aclarar el origen de la mezcla y decidir si el vault se separa a un repositorio propio. | Decidiste **no separarlo**. Se queda como está. Si algún día el volumen de ficheros de Obsidian crece mucho, se valorará agruparlos en una carpeta `Obsidian/` dentro de este mismo repositorio. |
| [[aud-004-zips-versionados\|AUD-004]] | 2026-08-08 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | El repositorio guardaba tres ficheros `.zip` cuyo contenido ya estaba también descomprimido al lado. Unos 19 MB duplicados que git tenía que arrastrar en cada clonación. | Sacarlos del control de versiones con `git rm --cached` (siguen en el disco, no se borran) y añadir `*.zip` y `*.rar` al `.gitignore`. | Aprobada tal cual y aplicada. |
| [[aud-005-skills-anidadas\|AUD-005]] | 2026-08-08 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Al descomprimir dos zips habían quedado carpetas dentro de carpetas con el mismo nombre (`obsidian/obsidian/...`), lo que hacía confusas todas las rutas al referenciar esas skills. | Aplanar el anidamiento. | Aprobada y **ampliada por ti**: además de aplanarlas, pediste trasladarlas a `.claude/skills/` y borrar la carpeta `Skills/` entera. |
| [[aud-006-gitignore-ruta-fantasma\|AUD-006]] | 2026-08-08 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Una línea del `.gitignore` apuntaba a una carpeta que ya no estaba en el disco. No rompía nada, pero ensuciaba un fichero que conviene mantener legible. | Borrar la línea. | Aprobada tal cual. Se aplicó en el mismo commit que [[aud-004-zips-versionados]] por tocar las mismas líneas. |
| [[aud-007-claude-md-desactualizado\|AUD-007]] | 2026-08-08 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | `CLAUDE.md` declaraba una carpeta `Presentaciones/` que no existía en el disco, y describía `Skills/` con un contenido que ya no era el real. | Retirar ambas filas del mapa de carpetas. | Aprobada, con el diff mostrado antes de escribir por tratarse de `CLAUDE.md`. |
| [[aud-008-optimizador-prompts-sin-usar\|AUD-008]] | 2026-08-08 | **Pendiente** — Se dejó para más adelante, a propósito. | Apareció `Skills/optimizador-prompts.skill`, un paquete comprimido sin instalar y sin que ningún agente, skill ni documento lo referenciase. Estaba ahí sin función. | Decidir si se instala o se retira. | Dijiste que lo gestionas **tú manualmente**, fuera del alcance de esa pasada. Queda anotado como pendiente, no como rechazado. |
| [[aud-009-fichero-con-nombre-recordatorio\|AUD-009]] | 2026-08-08 | **Pendiente** — Se dejó para más adelante, a propósito. | En `Datos/Consumo CPD/datos/` hay un fichero cuyo nombre es en realidad un recordatorio escrito a vuelapluma (`miraaverfalta...zip`), no un nombre descriptivo. Dentro de la carpeta de datos del TFM. | Renombrarlo, o resolver lo que el recordatorio pedía y eliminarlo. | Detectado y **no priorizado**. Sigue pendiente. |
| [[aud-010-config-obsidian-versionada\|AUD-010]] | 2026-08-08 | **Pendiente** — Se dejó para más adelante, a propósito. | Casi todo el contenido de la carpeta `.obsidian/` (la configuración de la aplicación) está bajo control de versiones. Es estado de una herramienta, no contenido del TFM. | Valorar si se excluye del control de versiones. | Detectado y **no priorizado**. Sigue pendiente, ligado a la decisión mayor de [[aud-003-repo-mezclado-con-vault]]. |
| [[aud-011-escritura-por-trozos\|AUD-011]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Cuando Claude trabaja en segundo plano, tiene bloqueada la escritura directa de ficheros como medida de seguridad. El agente lo descubría a base de intentarlo y fallar, y acababa escribiendo el resumen a trozos, en varios envíos. Cada envío pasa por la terminal, y ahí las tildes, las eñes y los símbolos `$` de las ecuaciones LaTeX pueden estropearse sin avisar. | Se plantearon tres vías: (a) desactivar el bloqueo de seguridad, (b) obligar al agente a aislarse en una copia del repositorio, o (c) dejar el bloqueo como está y prohibir por norma escribir a trozos. | La **opción (c)**, con un matiz que añadiste tú: que la skill sepa de antemano que la escritura directa va a fallar, para que no se quede reintentándolo en bucle. |
| [[aud-012-densidad-contra-paginas\|AUD-012]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | La skill de resúmenes decía dos cosas incompatibles. Por un lado definía el nivel Exhaustivo como *nada omitido*. Por otro, cuarenta líneas más abajo, ordenaba leer solo una muestra de cualquier documento de más de 80 páginas para ahorrar tokens. Con un TFM de referencia largo pedido en exhaustivo, las dos reglas daban respuestas opuestas. | Inicialmente, una regla de jerarquía: que Exhaustivo anulase los límites por páginas. | Tu solución, más simple: **eliminar los límites por páginas del todo**. El nivel lo eliges siempre tú y, si alguna vez se te olvida decirlo, que la skill pregunte antes de ponerse a trabajar. |
| [[aud-013-pregunta-densidad-incondicional\|AUD-013]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | La skill estaba obligada a preguntar el nivel de densidad siempre, incluso cuando el encargo ya lo traía escrito. Y un agente trabajando en segundo plano no tiene a quién preguntar: o se quedaba bloqueado, o se saltaba su propia regla. | Hacer la pregunta condicional: preguntar solo si el nivel no viene ya especificado. | Aprobada, y **absorbida dentro de [[aud-012-densidad-contra-paginas]]**: es la otra cara de la misma moneda, así que se aplicó en el mismo commit. |
| [[aud-014-ingesta-obsidian-sin-documentar\|AUD-014]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Cada vez que pedías *indexa esto en Obsidian*, había que volver a deducir desde cero todo el procedimiento: rutas del plugin, formato de la transacción, estructura de los dos registros internos, valores admitidos, cómo se calcula el identificador de cada fuente y qué siete ficheros hay que tocar. Nada de eso estaba escrito. | Consolidar el procedimiento completo en un documento de referencia dentro de la propia skill. | Aprobada. Inicialmente la habías rechazado; al reformularla como *meter dentro de la skill cómo usar claude-obsidian*, la aprobaste. |
| [[aud-015-worktrees-residuales\|AUD-015]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Cuando Claude trabaja en segundo plano crea copias aisladas del repositorio (*worktrees*) para no pisar tu carpeta. Habían quedado seis abandonadas, y cinco contenían una copia completa del vault de Obsidian. El verificador de salud del vault las recorría y devolvía **182 problemas, ninguno real**, tapando por completo cualquier problema verdadero. | Eliminar las copias residuales. | Aprobada, y ampliada al descubrir un problema añadido durante la limpieza. |
| [[aud-016-python3-ambiguo-windows\|AUD-016]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Los scripts auxiliares de la skill se invocan con `python3`. En Windows ese nombre es ambiguo: lo primero que encuentra el sistema es un atajo de la Microsoft Store que, en lugar de ejecutar nada, imprime un anuncio invitando a instalar Python desde la tienda. El error resultante no apunta a la causa real. | Documentar que `python3` no existe en este entorno y usar otro nombre. | Aprobada, pero **reformulada al re-verificarla**: `python3` sí funciona ahora, así que se documenta como ambigüedad, no como ausencia. |
| [[aud-017-locks-git-huerfanos\|AUD-017]] | 2026-08-21 | **Cerrado** — Aceptaste el cambio y ya está aplicado. | Al guardar cambios, git falló porque existía un fichero de bloqueo (`.git/index.lock`). Git cuelga ese fichero como un cartel de *ocupado* mientras trabaja y lo quita al terminar; si el proceso muere de golpe, el cartel se queda puesto con nadie dentro y a partir de ahí todos los git de esa carpeta fallan. | Escribir un protocolo obligatorio para tratar esos bloqueos, en lugar de improvisar cada vez. | Aprobada en su **versión barata**: el protocolo vive en la memoria persistente, no en `CLAUDE.md`. |
| [[aud-018-pvsyst-sin-ejercitar\|AUD-018]] | 2026-08-21 | **Pendiente** — Se dejó para más adelante, a propósito. | PVsyst es el núcleo técnico del TFM: de ahí salen las cifras de la simulación fotovoltaica. Pero nunca se ha usado. `Datos/PVsyst/` sigue sin informes y el subagente [[tfm-subagente-piloto-pvsyst]] no se ha invocado ni una vez. | Ninguna acción inmediata. Queda anotado para reevaluarlo en cuanto exista la primera simulación. | Abierto como hallazgo propio el 21/08/2026, al cerrar la mitad bibliográfica de [[aud-002-pipeline-sin-ejercitar]]. |

## Las dos pasadas

### 2026-08-08 — auditoría completa

Primera auditoría real del proyecto, de alcance completo. Diez hallazgos ([[aud-001-humanizer-no-invocable]] a [[aud-010-config-obsidian-versionada]]), cinco aplicados el mismo día. El más grave fue [[aud-001-humanizer-no-invocable]]: una regla declarada obligatoria en `CLAUDE.md` que era **imposible de cumplir**, porque la herramienta estaba en una carpeta desde la que Claude no puede cargarla.

Informe: `Auditorias/2026-08-08-auditoria.md`.

### 2026-08-21 — auditoría con foco

Auditoría dirigida a los errores recurrentes de la skill de resúmenes y del flujo de indexación en Obsidian, ambos ejercitados de verdad por primera vez en los días previos. Ocho hallazgos ([[aud-011-escritura-por-trozos]] a [[aud-018-pvsyst-sin-ejercitar]]), siete aplicados.

El más grave fue [[aud-012-densidad-contra-paginas]], porque su daño era invisible: pedir un resumen exhaustivo y recibir un muestreo etiquetado como exhaustivo, que luego se cita en la memoria del TFM como si fuera completo.

Esta pasada tuvo dos vueltas. En la primera (20/08) se aprobaron dos hallazgos, se rechazaron tres y quedaron dos pendientes de explicación. En la segunda (21/08), ya con las explicaciones sobre la mesa, se revirtieron los tres rechazos y se aprobaron los dos pendientes — con dos precisiones tuyas que mejoraron las propuestas originales, en [[aud-011-escritura-por-trozos]] y [[aud-012-densidad-contra-paginas]].

Informe: `Auditorias/2026-08-21-auditoria.md`.

## Estado actual

- **13 cerrados**, **5 pendientes** de 18 hallazgos.
- El pendiente que más pesa es [[aud-018-pvsyst-sin-ejercitar]]: el núcleo técnico del TFM sin probar todavía.
- Los otros tres ([[aud-003-repo-mezclado-con-vault]], [[aud-008-optimizador-prompts-sin-usar]], [[aud-009-fichero-con-nombre-recordatorio]]) son decisiones conscientes de no actuar, no olvidos.

## Relacionado

- [[tfm-skill-auditor]] — la skill que produce estos hallazgos
- [[tfm-skills]] — catálogo completo de skills del proyecto
