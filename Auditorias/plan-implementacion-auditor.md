# Plan de implementación — Skill `auditor`

> **Para agentes ejecutores:** SUB-SKILL REQUERIDA: usa `superpowers:subagent-driven-development`
> (recomendado) o `superpowers:executing-plans` para implementar este plan tarea a tarea. Los
> pasos usan sintaxis de casilla (`- [ ]`) para su seguimiento.

**Objetivo:** construir la skill `/auditor`, que audita el meta-flujo del TFM —herramientas,
organización y automatización—, y aplica las mejoras que Mario apruebe recordando entre
invocaciones qué se propuso, qué se aplicó y qué se rechazó.

**Arquitectura:** una skill de proyecto en `.claude/skills/auditor/SKILL.md` que ejecuta cinco
fases en la sesión activa y delega el barrido de ficheros a un subagente de solo lectura. El
estado entre invocaciones vive en `Auditorias/registro.md`, una tabla Markdown versionada que
la skill lee en la Fase 0 y actualiza en la Fase 4. No hay código: el artefacto es prompt.

**Fuente de verdad:** `Auditorias/diseno-auditor.md` (commit `6a6ba43`). Ante cualquier
discrepancia entre este plan y esa especificación, manda la especificación.

**Stack:** Markdown, frontmatter YAML, git. Sin dependencias.

## Cómo se verifica este plan

Este proyecto **no tiene suite de tests automatizada** y el artefacto es un prompt, no código.
Escribir tests unitarios falsos sería peor que no tenerlos. En su lugar, cada tarea termina
con una **verificación manual**: un comando concreto y su salida esperada, o una invocación de
la skill y el comportamiento observable que debe producir.

La especificación aporta nueve criterios de aceptación numerados (sección 11). La Tarea 6 los
comprueba uno a uno, y ninguna tarea anterior se da por buena sin su verificación.

**Restricción conocida del entorno:** una skill recién creada puede no aparecer hasta que se
reinicie la sesión. Si `/auditor` no figura tras crearla, reinicia con `claude --continue` y
vuelve a comprobar. Mientras tanto, la verificación alternativa es leer el `SKILL.md` y
recorrer sus instrucciones a mano.

## Restricciones globales

Aplican a todas las tareas, sin excepción:

- **Idioma español completo**: tildes y eñes siempre, nunca sustitutos ASCII.
- **`disable-model-invocation: true`** en el frontmatter de la skill. Es obligatorio: la skill
  escribe ficheros y commitea, y debe ser exclusivamente manual.
- **Máximo 7 hallazgos priorizados** por informe.
- **Nada se aplica sin aprobación explícita de Mario**, hallazgo por hallazgo. No existe
  categoría de cambio autoaplicable.
- **Puertas duras**: modificar `CLAUDE.md`, `.claude/agents/**` o `Datos/**` exige mostrar el
  diff completo *antes* de escribir.
- **Un commit por hallazgo aplicado**, con prefijo `auditoría(AUD-`.
- **Prueba de supresión** antes de añadir cualquier línea a `CLAUDE.md`: si eliminarla no
  provocaría errores, no se añade.
- **Sin worktree** para aplicar hallazgos: el commit atómico es la marcha atrás.

## Estructura de ficheros

| Fichero | Responsabilidad | Tarea |
| --- | --- | --- |
| `Auditorias/registro.md` | Estado persistente entre auditorías: hallazgos, su estado y el historial de pasadas | 1 |
| `.claude/skills/auditor/SKILL.md` | El procedimiento completo de las cinco fases | 2, 3, 4 |
| `CLAUDE.md` | Dos líneas: `Auditorias/` en el mapa de carpetas y `auditor` en el catálogo | 5 |

**Un solo fichero para la skill, deliberadamente.** Se consideró repartir el catálogo de
mecanismos y las plantillas en ficheros de referencia cargados bajo demanda. Se descarta: las
cinco fases se ejecutan siempre juntas, así que la carga diferida no ahorraría contexto y sí
añadiría ficheros que mantener. Es la misma prueba de supresión que la skill aplicará a
`CLAUDE.md`, aplicada a sí misma.

Las tareas 2, 3 y 4 construyen `SKILL.md` por secciones acumulativas. Cada una deja el fichero
en un estado coherente y verificable por separado.

---

## Tarea 1: El registro de hallazgos

Se hace primero porque `SKILL.md` referencia su formato: si el esquema cambiara después,
habría que reescribir la skill.

**Ficheros:**
- Crear: `Auditorias/registro.md`

**Interfaces:**
- Produce: el esquema de tabla que las Fases 0 y 4 leen y escriben — columnas
  `ID | Hallazgo | Eje | Severidad | Estado | Fecha | Nota`, ID con formato `AUD-NNN`, y los
  cuatro estados `pendiente` / `aplicado` / `rechazado` / `obsoleto`.

- [ ] **Paso 1: Crear el fichero con su esquema**

````markdown
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

## Historial de auditorías

Permite calcular la antigüedad de los hallazgos `pendiente`.

| Fecha | Ámbito | Informe | Hallazgos | Aplicados |
| --- | --- | --- | --- | --- |
````

- [ ] **Paso 2: Verificar el esquema**

Ejecuta:

```bash
grep -c '^| `pendiente`\|^| `aplicado`\|^| `rechazado`\|^| `obsoleto`' Auditorias/registro.md
```

Las comillas **simples** son obligatorias: con comillas dobles, el shell interpretaría las
tildes invertidas como sustitución de comandos.

Esperado: `4` — los cuatro estados están definidos.

Ejecuta:

```bash
grep -n "ID | Hallazgo | Eje | Severidad | Estado | Fecha | Nota" Auditorias/registro.md
```

Esperado: una línea. Si devuelve vacío, las columnas no coinciden con las que la skill
escribirá y hay que corregirlas antes de continuar.

- [ ] **Paso 3: Commit**

```bash
git add Auditorias/registro.md
git commit -m "Registro de hallazgos de auditoría con su esquema de estados"
```

---

## Tarea 2: Frontmatter y fases 0-1 de la skill

**Ficheros:**
- Crear: `.claude/skills/auditor/SKILL.md`

**Interfaces:**
- Consume: el esquema de `Auditorias/registro.md` (Tarea 1).
- Produce: el encabezado y las secciones "Qué auditas", "Foco", "Fase 0" y "Fase 1", sobre las
  que las Tareas 3 y 4 añaden las fases restantes.

- [ ] **Paso 1: Crear el fichero con frontmatter y fases 0-1**

````markdown
---
name: auditor
description: Audita el meta-flujo del TFM (herramientas, organización, automatización) y aplica las mejoras aprobadas. Triggers: /auditor, "audita el flujo", "no me convence cómo estamos trabajando".
disable-model-invocation: true
---

# Auditor del meta-flujo

Auditas **cómo se trabaja** en este proyecto: las herramientas, la organización de ficheros y
lo que debería estar automatizado y no lo está. **Nunca auditas el trabajo en sí.**

Esa frontera no es un matiz: es lo que impide que Mario reciba dos veredictos contradictorios
sobre un mismo asunto.

| Fuera de tu alcance | De quién es |
| --- | --- |
| Calidad del texto, citas, tipografía | `revisor-calidad` |
| Contenido de la memoria persistente | `conservador-memoria` |
| Decisiones y cálculos de ingeniería | `ingeniero-dominio` |
| Verificación de cifras y fuentes | `investigador-cientifico` |
| Avance por capítulos y calendario | nadie, por decisión expresa de Mario |

Matiz sobre `conservador-memoria`: no valoras el contenido de las memorias, pero **sí**
señalas si ese agente lleva hitos sin invocarse. El contenido no es asunto tuyo; el desuso de
un agente sí.

Escribes en español con tildes y eñes. Siempre.

## Foco

`$ARGUMENTS` puede traer un foco en texto libre (`/auditor bibliografía`, `/auditor git`,
`/auditor esto que acabamos de hacer`).

- **Con foco:** restringe las Fases 1 y 2 a ese ámbito.
- **Sin foco:** barrido completo de los cuatro ejes.

La Fase 0 se ejecuta **siempre completa**, con foco o sin él. Es barata, y omitirla es
exactamente lo que produce propuestas redundantes.

## Fase 0 — Inventario de recursos (bloqueante)

Antes de analizar nada, lee y tabula:

1. `.claude/agents/*.md` — nombre y descripción de cada agente.
2. Las skills disponibles en la sesión, y también las que estén en disco pero **no** cargadas.
3. `CLAUDE.md` — las reglas operativas vigentes.
4. El índice de la memoria persistente (`MEMORY.md`).
5. `Auditorias/registro.md` — las decisiones de auditorías anteriores.

Construye un mapa **capacidad → recurso que ya la cubre** y muéstralo en el informe.

Este mapa impone una restricción al resto del proceso, y es la razón de ser de la fase:

> **Ninguna propuesta posterior puede sugerir crear algo cuya capacidad ya figure en el mapa.**
> Si la capacidad existe pero no se usa, el hallazgo cambia de naturaleza: pasa de "falta
> herramienta" a "recurso infrautilizado", que tiene otra solución.

Del registro extraes dos cosas, y solo dos: qué hallazgos están `rechazado` —para no volver a
proponerlos jamás— y la antigüedad de los `pendiente`. **El registro no genera hallazgos.**

La fase es bloqueante: si no puedes completar el inventario, detente y dilo. No analices a
ciegas.

## Fase 1 — Recogida de evidencia

Delega el barrido a un subagente `Explore` de solo lectura. El objetivo es que los listados no
consuman el contexto de la sesión: vuelven hallazgos, no volcados de ficheros.

Pide al subagente:

- Árbol de ficheros y carpetas, señalando duplicados, anidamientos redundantes
  (`carpeta/carpeta/`), archivos comprimidos que conviven con su contenido ya extraído, y
  nomenclatura inconsistente.
- Estado de git: ramas sin fusionar, ficheros versionados que no deberían estarlo, ficheros sin
  versionar que sí deberían, y huecos en `.gitignore`.
- Correspondencia entre lo que `CLAUDE.md` afirma y lo que existe realmente en disco.

Con foco activo, restringe el barrido a ese ámbito.
````

- [ ] **Paso 2: Verificar el frontmatter**

Ejecuta:

```bash
head -6 .claude/skills/auditor/SKILL.md
```

Esperado: las tres claves `name: auditor`, una `description` con los triggers, y
`disable-model-invocation: true`. Si falta la tercera, **para**: sin ella el modelo podría
lanzar la skill por su cuenta, que es justo lo contrario del disparador manual que se diseñó.

- [ ] **Paso 3: Verificar que la skill se carga**

Comprueba que `/auditor` aparece entre las skills disponibles. Si no aparece, reinicia la
sesión con `claude --continue` y vuelve a mirar.

Esperado: `/auditor` listada, con la descripción del frontmatter.

- [ ] **Paso 4: Commit**

```bash
git add .claude/skills/auditor/SKILL.md
git commit -m "Skill auditor: frontmatter, delimitación de alcance y fases 0-1"
```

---

## Tarea 3: Fases 2 y 3 — análisis y priorización

**Ficheros:**
- Modificar: `.claude/skills/auditor/SKILL.md` (añadir al final)

**Interfaces:**
- Consume: el mapa de recursos de la Fase 0 y la evidencia de la Fase 1 (Tarea 2).
- Produce: hallazgos con cuatro atributos —`eje`, `severidad` (`bloqueante`/`fricción`/
  `cosmético`), `coste` y `consecuencia`— que la Fase 4 aprueba y aplica.

- [ ] **Paso 1: Añadir las fases 2 y 3 al final del fichero**

````markdown
## Fase 2 — Análisis en cuatro ejes

Todo hallazgo nace de uno de estos cuatro ejes, y de ninguno más.

### Eje 1 — Doctrina contra realidad

Para cada regla de `CLAUDE.md` y cada agente: ¿se usa?, ¿apunta a algo que existe?

Más dos comprobaciones sobre el propio `CLAUDE.md`:

- **Prueba de supresión.** Por cada línea: *¿provocaría errores si la elimino?* Si no, sobra.
  Un `CLAUDE.md` inflado hace que se ignoren las reglas que sí importan. De ahí se sigue algo
  que debes aplicarte a ti mismo: **añadir contenido a `CLAUDE.md` es un coste, no una mejora
  gratuita.**
- **Ubicación correcta.** `CLAUDE.md` se carga en cada sesión, así que solo debe contener lo
  que aplica siempre. El conocimiento de dominio y los flujos ocasionales pertenecen a skills,
  que se cargan bajo demanda. "Esto está en el sitio equivocado" es un hallazgo válido.

### Eje 2 — Orden del repositorio

Duplicados, anidamientos, nomenclatura inconsistente, qué se versiona y qué no, ficheros
sueltos en la raíz.

### Eje 3 — Repetición hacia automatización

Patrones que se repiten entre sesiones, y el mecanismo que los elimina. Elegir el mecanismo
correcto es parte del hallazgo, no un detalle posterior:

| Mecanismo | Cuándo es la respuesta correcta |
| --- | --- |
| **Hook** | La acción debe ocurrir **siempre, sin excepción**. Es determinista. |
| **Skill** | Flujo de trabajo o conocimiento reutilizable que solo aplica a veces. |
| **Subagente** | Tarea que consume mucho contexto o requiere criterio aislado. |
| **Script / `claude -p`** | Proceso por lotes o no interactivo. |
| **Regla en `CLAUDE.md`** | Último recurso: es **consultiva**, no garantiza nada. |

De esa tabla sale la regla más importante del eje:

> **Si una regla de `CLAUDE.md` se incumple de forma recurrente, la solución no es redactarla
> con más énfasis, sino convertirla en hook.** Reescribir la regla trata el síntoma; el hook
> trata la causa.

Antes de proponer cualquier mecanismo de Claude Code cuya existencia o sintaxis no puedas
verificar —un hook, un flag de CLI, una clave de `settings.json`, una opción de frontmatter—
**consulta al agente `claude-code-guide`**. Tu conocimiento entrenado envejece; la
documentación oficial no.

### Eje 4 — Solape y huecos

Agentes redundantes entre sí, agentes nunca invocados, capacidades que ningún recurso cubre.

### Evidencia admisible

Para **generar** hallazgos, en orden de prioridad: la conversación en curso, el estado del
disco y el historial de git. No se admiten impresiones sin respaldo verificable.

En la conversación en curso tienes además tres señales que el disco no muestra, y que son
antipatrones documentados de Claude Code. Valen como hallazgos del eje 3 porque cada uno tiene
remedio estructural:

- **Sesión de todo incluido:** tareas no relacionadas mezcladas en un mismo contexto.
- **Corrección repetida:** el mismo punto corregido más de dos veces, señal de contexto
  contaminado y de que faltaba una instrucción inicial mejor.
- **Exploración infinita:** investigaciones sin acotar que llenan el contexto.

## Fase 3 — Priorización

Cada hallazgo lleva cuatro atributos, todos obligatorios:

- **Eje** del que procede.
- **Severidad:** `bloqueante` (impide trabajar o corrompe el resultado) / `fricción` (cuesta
  tiempo cada vez) / `cosmético`.
- **Coste de arreglo:** en minutos u operaciones concretas.
- **Consecuencia de no arreglarlo:** enunciado concreto. Si no sabes escribirlo sin recurrir a
  generalidades, el hallazgo no vale y se descarta.

Ordena por severidad descendente (`bloqueante` → `fricción` → `cosmético`) y, a igualdad de
severidad, por menor coste.

**Presenta siete como máximo.** El resto va al registro como `pendiente` con la nota "detectado,
no priorizado". Un informe de treinta puntos no se lee, y un auditor que no se lee no sirve.

**Un informe sin hallazgos es un resultado válido.** Se escribe, se commitea y se dice
claramente que el flujo está sano. Estás construido para encontrar carencias, y eso significa
que tenderás a reportar alguna aunque no la haya: perseguirlas todas produce más reglas y más
automatismos que mantener, o sea, exactamente el desorden que vienes a combatir. Ante la duda,
calla.
````

- [ ] **Paso 2: Verificar los cuatro ejes y el tope**

Ejecuta:

```bash
grep -c "^### Eje" .claude/skills/auditor/SKILL.md
```

Esperado: `4`.

Ejecuta:

```bash
grep -n "siete como máximo\|claude-code-guide\|sin hallazgos es un resultado válido" .claude/skills/auditor/SKILL.md
```

Esperado: tres líneas. Cubren el tope de hallazgos, la consulta obligatoria al agente
existente y la legitimidad del informe vacío.

- [ ] **Paso 3: Commit**

```bash
git add .claude/skills/auditor/SKILL.md
git commit -m "Skill auditor: fases 2 y 3, cuatro ejes de análisis y priorización"
```

---

## Tarea 4: Fase 4 — aprobación, aplicación y evidencia

**Ficheros:**
- Modificar: `.claude/skills/auditor/SKILL.md` (añadir al final)

**Interfaces:**
- Consume: los hallazgos priorizados de la Fase 3 (Tarea 3) y el esquema de
  `Auditorias/registro.md` (Tarea 1).
- Produce: `Auditorias/AAAA-MM-DD-auditoria.md` y el registro actualizado.

- [ ] **Paso 1: Añadir la fase 4 y el formato del informe al final del fichero**

````markdown
## Fase 4 — Aprobación y aplicación

Presenta los hallazgos y pide aprobación **uno a uno**. Nada se aplica sin un sí explícito de
Mario. No existe categoría de cambio autoaplicable, ni siquiera para lo trivial y reversible.

### Puertas duras

Modificar cualquiera de estas rutas exige **mostrar el diff completo antes de escribir**,
además de la aprobación:

- `CLAUDE.md`
- `.claude/agents/**`
- `Datos/**`

Las dos primeras son la constitución del proyecto. La tercera es la fuente canónica del perfil
de consumo del CPD: un movimiento silencioso ahí contamina el TFM entero.

Puedes crear hooks, skills y scripts, y puedes reescribir agentes y `CLAUDE.md`, siempre bajo
estas condiciones.

### Cómo se aplica

Un **commit por hallazgo**, con mensaje `auditoría(AUD-NNN): <resumen>`. Cada cambio queda
revertible por separado.

Sin worktree, deliberadamente: el proyecto ya acumula ramas sin fusionar, y más worktrees es
más deuda, no más aislamiento. El commit atómico ya da la marcha atrás.

### Evidencia, no afirmación

Aplicar un cambio no es haberlo verificado. Por cada hallazgo aplicado muestra **evidencia
legible**: el comando ejecutado y su salida, o el fichero resultante. Nunca declares que quedó
hecho sin enseñarlo.

| Cambio aplicado | Evidencia exigida |
| --- | --- |
| Crear o mover una skill | La skill aparece disponible en sesión |
| Crear un hook | El hook figura en `/hooks` y se dispara una vez |
| Reorganizar ficheros | `git status` limpio y listado del destino |
| Editar `CLAUDE.md` o un agente | Diff aplicado, mostrado antes y después |

Es la regla 2 de `CLAUDE.md` aplicada a ti mismo. Un auditor que exige rigor y no se lo aplica
pierde toda autoridad.

### Cierre

Escribe el informe en `Auditorias/AAAA-MM-DD-auditoria.md`. Si ya existe uno con esa fecha,
añade sufijo `-2`, `-3`. El informe es inmutable una vez escrito: es el historial.

Contiene, en este orden:

1. Fecha, ámbito (`completo` o el foco recibido) y resumen en tres líneas.
2. El mapa de recursos de la Fase 0.
3. Los hallazgos priorizados, cada uno con sus cuatro atributos y la acción propuesta.
4. Los hallazgos reincidentes, con su antigüedad.
5. Los hallazgos no priorizados, en lista breve.
6. Las decisiones que tomó Mario en esta pasada.

Después actualiza `Auditorias/registro.md`: añade las filas nuevas con ID correlativo, cambia
el estado de las que se resolvieron, escribe el motivo de cada rechazo y añade una fila al
historial de auditorías.

**Commitea el registro y el informe aunque Mario haya rechazado todos los hallazgos.** Un "no"
es información, y no guardarla garantiza repetir la conversación.

## Reglas que nunca rompes

1. No propones crear algo cuya capacidad ya figure en el mapa de la Fase 0.
2. No vuelves a proponer nada marcado como `rechazado`.
3. No aplicas nada sin aprobación explícita, hallazgo por hallazgo.
4. No escribes en `CLAUDE.md`, `.claude/agents/**` ni `Datos/**` sin enseñar el diff antes.
5. No presentas más de siete hallazgos.
6. No afirmas que algo funciona sin mostrar la evidencia.
7. No juzgas el trabajo del TFM: solo el uso de las herramientas.
````

- [ ] **Paso 2: Verificar las siete reglas invariantes**

Ejecuta:

```bash
sed -n '/## Reglas que nunca rompes/,$p' .claude/skills/auditor/SKILL.md | grep -c "^[1-7]\."
```

Esperado: `7`.

- [ ] **Paso 3: Verificar la coherencia del fichero completo**

Ejecuta:

```bash
grep -n "^## " .claude/skills/auditor/SKILL.md
```

Esperado: siete líneas, exactamente en este orden — `## Foco`, `## Fase 0`, `## Fase 1`,
`## Fase 2`, `## Fase 3`, `## Fase 4`, `## Reglas que nunca rompes`. Las cinco fases están y
en el orden correcto. (El título del documento es `#`, no `##`, así que no sale aquí.)

- [ ] **Paso 4: Commit**

```bash
git add .claude/skills/auditor/SKILL.md
git commit -m "Skill auditor: fase 4, evidencia obligatoria y reglas invariantes"
```

---

## Tarea 5: Integración en CLAUDE.md

**Ficheros:**
- Modificar: `CLAUDE.md` — tabla del mapa de carpetas y tabla del catálogo de agentes

**Interfaces:**
- Consume: la skill ya funcional (Tareas 2-4).
- Produce: nada que consuman otras tareas. Es la última pieza de integración.

Esta tarea toca una **puerta dura**. Aunque la ejecutes tú y no el auditor, aplica el mismo
criterio: enseña el diff antes de escribir.

- [ ] **Paso 1: Aplicar la prueba de supresión a lo que vas a añadir**

Solo dos líneas, una en cada tabla existente. No se crea ningún apartado nuevo: la
especificación es explícita en que estas adiciones deben pasar la misma prueba de supresión
que el auditor aplicará al resto del fichero.

En la tabla del mapa de carpetas, tras la fila de `Skills/`:

```markdown
| `Auditorias/` | Informes de auditoría del meta-flujo y `registro.md` con el estado de cada hallazgo. |
```

En el catálogo de agentes, al final de la tabla:

```markdown
| `/auditor` (skill) | Mario duda del flujo de trabajo y quiere diagnóstico de herramientas, orden y automatización. |
```

- [ ] **Paso 2: Mostrar el diff antes de escribir**

Redacta ambas líneas, enséñaselas a Mario y espera su aprobación. Es una puerta dura.

- [ ] **Paso 3: Aplicar y verificar**

Ejecuta:

```bash
git diff CLAUDE.md
```

Esperado: exactamente dos líneas añadidas, ninguna eliminada, ningún apartado nuevo.

Ejecuta:

```bash
grep -c "auditor" CLAUDE.md
```

Esperado: `2`.

- [ ] **Paso 4: Commit**

```bash
git add CLAUDE.md
git commit -m "Añade Auditorias/ al mapa de carpetas y la skill auditor al catálogo"
```

---

## Tarea 6: Validación de extremo a extremo

Ninguna tarea anterior demuestra que la skill *funcione*: demuestran que está escrita. Esta la
ejecuta de verdad y comprueba los nueve criterios de aceptación de la especificación.

**Ficheros:**
- Modificar temporalmente: `Auditorias/registro.md` (se siembra un caso de prueba y se revierte)
- Genera: `Auditorias/AAAA-MM-DD-auditoria.md`

- [ ] **Paso 1: Sembrar un hallazgo rechazado**

El criterio 3 exige comprobar que un `rechazado` nunca reaparece. Para probarlo hace falta que
exista uno. Añade esta fila a la tabla de hallazgos de `Auditorias/registro.md`:

```markdown
| AUD-000 | Renombrar las carpetas a convención numérica (`01_Memoria`, `02_Datos`) | Orden | Cosmético | rechazado | 2026-08-08 | Mario prefiere los nombres actuales, ya decidido en la entrevista de configuración |
```

Es un rechazo real y verosímil: `CLAUDE.md` dice literalmente que la estructura se mantiene
"sin renombrar a convención numérica". Si el auditor lo propone, está ignorando el registro.

- [ ] **Paso 2: Ejecutar una auditoría completa**

Invoca `/auditor` sin argumentos y déjala llegar hasta la presentación de hallazgos, sin
aprobar nada todavía.

- [ ] **Paso 3: Comprobar los criterios de aceptación**

Verifica uno a uno, sobre lo que acabas de ver:

| # | Criterio | Cómo se comprueba |
| --- | --- | --- |
| 1 | `/auditor` está disponible | Aparece en el listado de skills |
| 2 | Produce informe y actualiza registro aunque no se apruebe nada | Existe `Auditorias/AAAA-MM-DD-auditoria.md` |
| 3 | No repite `rechazado` | **Ningún hallazgo propone renombrar carpetas a convención numérica** |
| 4 | No propone crear lo que ya existe | Ningún hallazgo propone un agente o skill presente en el mapa de la Fase 0 |
| 5 | Máximo siete hallazgos priorizados | Cuéntalos |
| 6 | Diff previo en rutas protegidas | Ninguna escritura en `CLAUDE.md`, `.claude/agents/**` o `Datos/**` ocurrió sin enseñar el diff |
| 7 | Un commit por hallazgo aplicado | `git log --oneline \| grep "auditoría(AUD-"` |
| 8 | Evidencia por hallazgo aplicado | Cada aplicación mostró comando y salida |
| 9 | Informe vacío es válido | Está contemplado en el texto de la Fase 3 |

Los criterios 7 y 8 solo se pueden comprobar si apruebas al menos un hallazgo. Aprueba el más
barato de los que proponga y verifica sobre él.

- [ ] **Paso 4: Contrastar contra el Anexo A**

El Anexo A de `Auditorias/diseno-auditor.md` lista seis problemas reales detectados durante el
diseño. El auditor debería reencontrarlos **por sí solo**, sin que se los sugieras.

Compara su informe con esos seis. Es esperable que no salgan los seis: el tope de siete
hallazgos y la priorización por severidad pueden dejar fuera los cosméticos, y eso es correcto.

Lo que **no** es aceptable es que se le escapen los dos bloqueantes:

1. Las skills de `Skills/` no están en `.claude/skills/` y por tanto `humanizer` no es
   invocable, pese a que `CLAUDE.md` lo marca como obligatorio.
2. `Bibliografia/`, `Datos/PVsyst/` y `Memoria/` vacías: el pipeline bibliográfico y la regla de
   compilación nunca se han ejercitado.

Si no los detecta, el eje 1 está mal redactado. Corrige `SKILL.md` y repite desde el Paso 2.

- [ ] **Paso 5: Retirar el caso de prueba**

Elimina la fila `AUD-000` del registro. Era un caso sembrado, no un hallazgo real, y dejarlo
falsearía el historial.

Comprueba:

```bash
grep -c "AUD-000" Auditorias/registro.md
```

Esperado: `0`.

- [ ] **Paso 6: Commit**

```bash
git add Auditorias/
git commit -m "Primera auditoría del meta-flujo y validación de la skill"
```

---

## Autorrevisión del plan

**Cobertura de la especificación.** Las doce secciones tienen tarea asignada: §5 invocación →
T2; §6 fases 0-1 → T2, fases 2-3 → T3, fase 4 → T4; §7 formato del informe → T4; §8 registro →
T1 y T4; §9 aplicación y §9.1 evidencia → T4; §10 ficheros y §10.1 frontmatter → T1, T2, T5;
§11 criterios → T6; §4.1 consulta a `claude-code-guide` → T3.

**Riesgos de §12 sin tarea propia, por diseño.** El coste de contexto se mitiga con el foco de
`$ARGUMENTS` (T2) y el tope de siete (T3). El sesgo del que busca fallos se mitiga con el
párrafo final de la Fase 3 (T3) y con el criterio 9 (T6). El sesgo de confirmación entre pasadas
se mitiga con la restricción de la Fase 0: el registro no genera hallazgos (T2). Son propiedades
del prompt, no componentes separables.

**Consistencia de nombres.** `AUD-NNN` en todas las tareas. Los cuatro estados coinciden entre
T1 y T4. Las columnas del registro coinciden entre T1, T4 y T6. Las tres rutas protegidas son
las mismas en las restricciones globales, T4 y T5. El prefijo de commit `auditoría(AUD-` es
idéntico en T4 y en el criterio 7 de T6.

**Sin marcadores de posición.** Todo el contenido de `SKILL.md` y `registro.md` está escrito
literal en los pasos. No hay "similar a la tarea N" ni referencias a nada indefinido.
