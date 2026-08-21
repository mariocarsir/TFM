# Auditoría del meta-flujo — 2026-08-21

**Ámbito:** con foco. Errores recurrentes de las skills `resumen-tecnico` (invocada vía
`bibliotecario-pdf`) y del flujo de ingesta a `claude-obsidian`, ambas ejercitadas de verdad
por primera vez con carga real durante los días previos.

**Resumen en tres líneas:** `resumen-tecnico` contenía dos reglas contradictorias sobre cuánto
del documento hay que leer, de modo que un resumen pedido como exhaustivo podía devolverse
muestreado sin que se notara; el guard de aislamiento de los jobs en segundo plano empujaba a
escribir el `.md` por trozos, con riesgo de corromper tildes y ecuaciones; y el patrón completo
de ingesta al vault de Obsidian se re-deducía desde cero en cada invocación, sin estar escrito
en ninguna parte.

**Dato ancla medido:** una invocación de `resumen-tecnico` sobre un PDF de 132 páginas en
densidad Exhaustivo consumió **359.784 tokens y 48 llamadas a herramienta en unos 25 minutos**.
Todos los costes estimados de este informe están calculados contra esa referencia real, no
contra una suposición.

## Mapa de recursos (Fase 0)

| Capacidad | Recurso que ya la cubre | Estado al iniciar esta pasada |
| --- | --- | --- |
| Procesar bibliografía nueva | `bibliotecario-pdf` + skill `resumen-tecnico` | Ejercitada 4 veces con éxito |
| Resumir con densidad graduable | skill `resumen-tecnico` | Con reglas internas contradictorias |
| Indexar al grafo de Obsidian | plugin `claude-obsidian` (transacciones) | Funcional, pero sin procedimiento escrito |
| Verificar la salud del vault | linter de `claude-obsidian` | Inutilizable: 182 hallazgos, 0 reales |
| Aislar trabajo concurrente | worktrees de git | 6 worktrees residuales, 5 con copia del vault |
| Auditar el meta-flujo | skill `auditor` | Operativa |

Registro previo: 10 hallazgos de la pasada del 2026-08-08, de los cuales 5 aplicados y 5
pendientes. AUD-002 se cierra en esta pasada (ver más abajo).

## Hallazgos (7 de 7 máximo)

### AUD-011 — El `.md` del resumen se escribía por trozos

**Eje:** doctrina/realidad. **Severidad:** fricción alta.

En un job en segundo plano, el guard de aislamiento bloquea `Write` y `Edit` sobre el checkout
compartido. `bibliotecario-pdf` descubrió el bloqueo a base de intentarlo, y acabó volcando un
fichero de 60 KB con varios `>>` sucesivos. Trocear el volcado expone el contenido a la
terminal varias veces: tildes, eñes y los `$` de las ecuaciones LaTeX pueden corromperse en
silencio, y si un trozo falla el fichero queda a medias sin que nada lo señale.

**Coste sin corregir:** 5-10k tokens por invocación en reintentos y troceado, más el riesgo no
acotado de un resumen corrupto que se detecta tarde. **Coste de corregir:** ~2k tokens, una vez.

**Solución aplicada:** una sección obligatoria en `SKILL.md` que declara el bloqueo como hecho
conocido de antemano (nada de reintentar `Write` "a ver si cuela"), fija el heredoc único con
delimitador entrecomillado como vía obligatoria, y añade una verificación posterior de tamaño
y de caracteres acentuados.

**Riesgos:** ninguno sobre el contenido. Se descartaron dos alternativas: desactivar el guard
con `bgIsolation: none` en `.claude/settings.json` (habría abierto la puerta a colisiones entre
los jobs paralelos que este mismo repositorio sufre a diario) y forzar `EnterWorktree` (se
muerde la cola con AUD-015, que precisamente elimina worktrees).

### AUD-012 — Dos reglas contradictorias sobre cuánto leer

**Eje:** doctrina/realidad. **Severidad:** bloqueante para la calidad del resultado.

`SKILL.md` definía el nivel Exhaustivo como "nada omitido" y, cuarenta líneas más abajo,
ordenaba muestrear todo documento de más de 80 páginas "por presupuesto de tokens". Dos reglas
distintas gobernando exactamente lo mismo, con respuestas opuestas para el caso más frecuente:
un TFM de referencia largo pedido en exhaustivo.

Que cada densidad cueste distinto no es el defecto: eso es el diseño. El defecto es pedir "nada
omitido" y poder recibir un muestreo etiquetado como exhaustivo sin que la etiqueta mienta
formalmente. La prueba de que la contradicción era real: en la ingesta de Barrios (2023) el
agente leyó las 132 páginas completas, incumpliendo la regla de presupuesto, y solo lo hizo
porque el encargo insistía en "EXHAUSTIVO".

**Coste sin corregir:** no es de tokens, es de fiabilidad — un resumen incompleto que se cita
en la memoria del TFM como si fuera completo. **Coste de corregir:** ~3k tokens, una vez.

**Solución aplicada:** se retiran los umbrales por páginas. El alcance de lectura lo fija
exclusivamente el nivel de densidad, y Exhaustivo obliga a leer el documento entero encadenando
rangos. Si el nivel pedido resulta inviable, la skill lo dice **antes** de empezar en lugar de
recortar por su cuenta. La sección "Límites de presupuesto de tokens" se sustituye por
"Alcance de lectura", que además deja escrito el coste real medido de un Exhaustivo largo para
que nadie lo confunda con un desvío.

**Riesgos:** un Exhaustivo sobre un documento muy largo será caro por diseño. Es la decisión
consciente de Mario: prefiere pagar el coste a recibir un resumen incompleto sin saberlo.

### AUD-013 — La pregunta de densidad era incondicional

**Eje:** doctrina/realidad. **Severidad:** fricción.

La Fase 1 obligaba a preguntar el nivel de densidad con `AskUserQuestion` aunque el encargo ya
lo trajera. Un subagente ejecutando en segundo plano no tiene a quién preguntar, así que o se
bloqueaba o se saltaba la regla.

**Solución aplicada:** en el mismo commit que AUD-012. La densidad la elige **siempre** Mario;
si el encargo ya la trae, se usa tal cual y no se pregunta; si no la trae, se pregunta antes de
extraer nada y nunca se deduce del tamaño del documento.

**Riesgos:** ninguno.

### AUD-014 — El procedimiento de ingesta al vault no estaba escrito

**Eje:** repetición no automatizada. **Severidad:** fricción alta.

Cada vez que Mario pide "indexa esto en Obsidian" había que volver a deducir: rutas del plugin
bajo WSL, esquema del bundle transaccional, forma de los dos ledgers, enums admitidos, cálculo
determinista del `source_id`, y cuáles de los siete ficheros del vault hay que tocar. Nada de
eso vivía en el repositorio; sobrevivía solo en memoria persistente en prosa y se reconstruía a
mano en cada pasada.

**Coste sin corregir:** 30-45k tokens por ingesta, y creciendo, más el riesgo real de inventarse
un `source_id` a mano y romper la unión entre el ledger y la página.
**Coste de corregir:** ~8k tokens, una vez.

**Solución aplicada:** `.claude/skills/resumen-tecnico/references/ingesta-obsidian.md`, escrito
y verificado contra el ledger real del vault, con los diez apartados del procedimiento. Se
apunta a él desde la Fase 6 y desde la regla 4 de la skill.

**Riesgos:** el documento puede quedar desactualizado si el plugin cambia de versión (hoy la
2.1.0). Se mitiga porque el fichero declara la versión exacta en las rutas, así que un cambio
de versión salta a la vista.

**Importante:** la skill **sigue sin ingestar por su cuenta**. La referencia documenta el cómo
para cuando Mario lo pida; no convierte la ingesta en automática. La regla de mecanismos *pull*
y no *push* queda intacta.

### AUD-015 — Worktrees residuales inutilizando el linter

**Eje:** orden del repositorio. **Severidad:** fricción alta.

Los seis worktrees de `.claude/worktrees/` estaban fusionados en master, sin commits propios y
sin cambios sin guardar, pero cinco contenían una copia completa del vault de Obsidian. El
linter los recorría y devolvía **182 hallazgos, ninguno real**, tapando por completo cualquier
problema verdadero. Al investigarlo apareció un problema añadido: git había registrado seis de
esos directorios en el índice de master como entradas `gitlink` (modo 160000), como si fueran
submódulos, y dos de ellas apuntaban a directorios ya borrados del disco.

**Coste sin corregir:** el linter deja de servir para lo que existe, que es detectar enlaces
rotos y errores de procedencia. **Coste de corregir:** ~4k tokens, una vez.

**Solución aplicada:** eliminados los seis worktrees y sus ramas locales (todo su contenido ya
estaba en master, comprobado uno a uno: cero commits divergentes, cero cambios sin guardar,
cero actividad en las últimas seis horas); destrackeadas las seis entradas `gitlink`; y añadido
`.claude/worktrees/` al `.gitignore` para que ningún worktree futuro vuelva a versionarse ni a
contaminar el linter.

**Verificación:** el linter pasa de 182 hallazgos a **0**, sobre 56 páginas y 168 enlaces.

**Riesgos:** ninguno de pérdida de trabajo. Se conservan intencionadamente las ramas
`worktree-agent-a378a456372409571` y `worktree-qa-git-doc`, que no tenían worktree asociado y
quedan fuera del alcance de este hallazgo.

### AUD-016 — Ambigüedad del intérprete de Python en Windows

**Eje:** doctrina/realidad. **Severidad:** cosmético.

Una invocación de los scripts de la skill falló contra el alias de ejecución de la Microsoft
Store, que va por delante en el PATH de Git Bash y, en lugar de ejecutar nada, imprime un
mensaje invitando a instalar Python desde la tienda y devuelve el código 9009 sin traza útil.

**Matiz honesto, detectado al re-verificar hoy:** `python3` **sí** funciona ahora en este shell
y resuelve a Python 3.12.10 real, aunque el alias de la Store sigue por delante en el PATH. Por
eso el hallazgo no se documenta como una ausencia absoluta —lo habría sido escribir algo falso—
sino como lo que realmente es: un nombre ambiguo cuyo comportamiento no es estable entre
sesiones.

**Solución aplicada:** una comprobación previa de tres candidatos (`python3`, `python`, `py -3`)
y la descripción del síntoma concreto que hay que reconocer, más la nota de que dentro de WSL
`python3` es siempre el correcto.

**Riesgos:** ninguno.

### AUD-017 — Locks de git huérfanos por trabajo concurrente

**Eje:** doctrina/realidad. **Severidad:** fricción, con cola de riesgo alta.

Al comitear la ingesta de Barrios, `git add` falló porque `.git/index.lock` ya existía. Causa
raíz: varios jobs de Claude Code operando en paralelo sobre el mismo checkout. El peligro no es
el fallo, es la reacción: borrar el lock sin comprobar nada. Si hay un `git` vivo escribiendo,
eliminar el lock deja entrar a un segundo proceso al índice y lo corrompe.

**Coste sin corregir:** 3-8k tokens de improvisación por incidente, más el riesgo de un borrado
a ciegas que corrompa el índice. **Coste de corregir:** ~2k tokens, una vez.

**Solución aplicada:** el protocolo de tres pasos (esperar en bucle → inspeccionar tamaño y
`mtime` → confirmar con `Get-Process` que no existe ningún proceso `git`, y solo entonces
borrar) se saca a su propia memoria persistente, `feedback_git_index_lock.md`, en lugar de
quedar enterrado dentro de la memoria de Obsidian, que solo aflora al hablar del vault. Un lock
puede aparecer en cualquier commit del TFM.

**Riesgos:** ninguno. Se descartó expresamente meterlo en `CLAUDE.md`, que se carga entero en
cada sesión: habría cobrado un peaje permanente por un incidente ocasional. Como memoria, se
recupera solo cuando es relevante.

## Cierre de un hallazgo antiguo

**AUD-002** (pipeline bibliográfico y PVsyst nunca ejercitados) llevaba desde el 2026-08-08 con
la nota "reevaluar cuando se use `bibliotecario-pdf` por primera vez". La condición se ha
cumplido: se ha usado con éxito cuatro veces y de ahí salieron seis de los siete hallazgos de
esta pasada. Se cierra la mitad bibliográfica. **La mitad de PVsyst sigue sin ejercitarse** y se
reabre como hallazgo propio, AUD-018, para no darla por buena de rebote.

## Decisiones de Mario en esta pasada

Los siete hallazgos se presentaron uno a uno. En la primera vuelta (2026-08-20) Mario aprobó
AUD-013 y AUD-015, rechazó AUD-014, AUD-016 y AUD-017, y pidió explicación detallada de AUD-011
y AUD-012 antes de decidir. En la segunda vuelta (2026-08-21), ya con las explicaciones, revirtió
los tres rechazos y aprobó los dos pendientes, con dos precisiones propias que mejoraron las
propuestas:

- **Sobre AUD-011:** además de prohibir el troceado, exigió que la skill sepa de antemano que
  `Write` va a fallar en un job en segundo plano, para que no se embucle reintentándolo. Ese
  matiz está incorporado en el texto aplicado.
- **Sobre AUD-012:** en lugar de una regla de jerarquía entre umbrales y densidad, pidió
  eliminar los umbrales por páginas directamente, porque el nivel lo elige siempre él y, si
  alguna vez se le olvida decirlo, prefiere que la skill le pregunte antes de ponerse a
  trabajar. Es una solución más simple que la propuesta inicial y es la que se ha aplicado.

Mario objetó también, con razón, la formulación inicial de AUD-012: que cada densidad cueste
distinto es el diseño, no un fallo. El hallazgo se reformuló para acotarlo a la contradicción
real antes de aplicarlo.

## Commits de esta auditoría

| Hallazgo | Commit | Qué cambió |
| --- | --- | --- |
| AUD-011 | `10d367b` | Escritura del resumen en un único volcado |
| AUD-012 + AUD-013 | `5ce1b49` | La densidad manda sobre el número de páginas |
| AUD-014 | `af74d67` | Procedimiento de ingesta al vault documentado |
| AUD-016 | `5ce8066` | Ambigüedad del intérprete de Python |
| AUD-015 | `1b5221c` | Poda de worktrees, destrackeo de gitlinks y `.gitignore` |
| AUD-017 | sin commit | Memoria persistente, fuera del repositorio |

## Estado tras la pasada

- `resumen-tecnico/SKILL.md`: sin contradicciones internas conocidas.
- Linter del vault: 0 hallazgos, operativo de nuevo como herramienta de diagnóstico.
- Repositorio: un solo worktree (el principal), sin gitlinks espurios.
- Pendiente principal: ejercitar el flujo de PVsyst (AUD-018).
