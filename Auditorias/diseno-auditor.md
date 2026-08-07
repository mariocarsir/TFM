# Diseño — Skill `auditor`

**Fecha:** 2026-08-07
**Autor de la especificación:** sesión de brainstorming con Mario Carrión Sirvent
**Estado:** aprobado, pendiente de plan de implementación

---

## 1. Problema

El proyecto TFM tiene siete agentes, varias skills, un `CLAUDE.md` con diez reglas
operativas, memoria persistente y un vault Obsidian. Todo ese andamiaje se montó de
una vez, al principio, y desde entonces nadie lo ha revisado contra la realidad.

Los síntomas concretos que motivan esta skill:

- Reglas de `CLAUDE.md` que apuntan a carpetas vacías o a herramientas no cargadas.
- Desorden de ficheros y carpetas pese a una estructura pensada de forma lógica.
- Procesos que se repiten sesión tras sesión sin que nadie los automatice.
- Riesgo de proponer herramientas nuevas para tareas que un agente existente ya cubre.

Falta un mecanismo que Mario pueda invocar cuando **no está convencido del flujo de
trabajo que se está siguiendo**, y que produzca mejora acumulativa a lo largo del curso
del proyecto en lugar de diagnósticos que se repiten.

## 2. Objetivo

Una skill de proyecto, invocable manualmente, que audite el **meta-flujo** del TFM
—herramientas, organización y automatización— y aplique las mejoras que Mario apruebe,
recordando entre invocaciones qué se propuso, qué se aplicó y qué se rechazó.

## 3. No-objetivos

Delimitados explícitamente para que Mario no reciba dos veredictos contradictorios sobre
un mismo asunto. **El auditor juzga el uso de las herramientas, nunca el trabajo que
producen.**

| Fuera de alcance | Responsable |
| --- | --- |
| Calidad del texto, citas, cumplimiento tipográfico | `revisor-calidad` |
| Contenido de la memoria persistente | `conservador-memoria` |
| Decisiones y cálculos de ingeniería | `ingeniero-dominio` |
| Verificación de cifras y fuentes | `investigador-cientifico` |
| Seguimiento del calendario académico y avance por capítulos | nadie (decisión explícita de Mario) |

Matiz importante sobre `conservador-memoria`: el auditor **no** entra a valorar el
contenido de las memorias, pero **sí** señala si ese agente lleva hitos sin invocarse.
El contenido de la memoria no es asunto suyo; el desuso de un agente sí.

## 4. Decisión de forma: skill, no agente

Se implementa como **skill de proyecto**, no como subagente.

Razón determinante: el disparador declarado es *"cuando no estoy convencido del flujo que
se está siguiendo"*. Ese juicio necesita ver la conversación que generó la duda. Una skill
corre en la sesión activa y tiene ese contexto; un subagente arranca en frío y solo vería
el estado del disco. Añadido: el informe de un subagente no se muestra al usuario
directamente, y aplicar cambios exigiría devolverle el control.

El barrido ruidoso sí se delega a un subagente de solo lectura (ver Fase 1), que es donde
el aislamiento de contexto aporta y no cuesta nada.

Efecto secundario buscado: crear la skill en `.claude/skills/` deja sentado el directorio
correcto para skills de proyecto, que hoy no se está usando.

## 5. Invocación

- `/auditor` — barrido completo de los cuatro ejes.
- `/auditor <tema>` — foco acotado en texto libre. Ejemplos: `/auditor bibliografía`,
  `/auditor esto que acabamos de hacer`, `/auditor git`.

Con foco acotado se ejecutan las mismas cinco fases, pero las Fases 1 y 2 se restringen al
ámbito indicado. La Fase 0 se ejecuta siempre completa: el inventario de recursos es
barato y su omisión es precisamente lo que produce propuestas redundantes.

## 6. Arquitectura: cinco fases

### Fase 0 — Inventario de recursos (bloqueante)

Se ejecuta antes de cualquier análisis. Lee y tabula:

- `.claude/agents/*.md` — nombre y descripción de cada agente.
- Skills realmente cargadas en la sesión, más las presentes en disco pero no cargadas.
- `CLAUDE.md` — reglas operativas vigentes.
- El índice de la memoria persistente (`MEMORY.md`).
- `Auditorias/registro.md` — decisiones de auditorías anteriores.

Produce un mapa **capacidad → recurso que ya la cubre**.

Restricción que impone al resto del proceso: ninguna propuesta posterior puede sugerir
crear algo cuya capacidad ya figure en ese mapa. Si la capacidad existe pero no se usa, el
hallazgo cambia de naturaleza: pasa de *"falta herramienta"* a *"recurso infrautilizado"*,
que tiene otra solución.

La fase es bloqueante: si no se puede completar el inventario, la auditoría se detiene y lo
reporta, en lugar de analizar a ciegas.

### Fase 1 — Recogida de evidencia

Se delega a un subagente de solo lectura (tipo `Explore`) para no inundar el contexto de la
sesión con listados. Recoge:

- Árbol de ficheros y carpetas, con detección de duplicados, anidamientos redundantes
  (`carpeta/carpeta/`), archivos comprimidos que conviven con su contenido ya extraído, y
  nomenclatura inconsistente.
- Estado de git: ramas sin fusionar, ficheros versionados que no deberían estarlo, ficheros
  sin versionar que deberían estarlo, cobertura de `.gitignore`.
- Correspondencia entre lo que `CLAUDE.md` afirma y lo que existe en disco.

Devuelve hallazgos, no volcados de ficheros.

### Fase 2 — Análisis en cuatro ejes

Todo hallazgo debe nacer de uno de estos cuatro ejes, y de ninguno más:

1. **Doctrina vs. realidad.** Para cada regla de `CLAUDE.md` y cada agente: ¿se usa?,
   ¿apunta a algo que existe?
2. **Orden del repositorio.** Duplicados, anidamientos, nomenclatura, qué se versiona y qué
   no, ficheros sueltos en la raíz.
3. **Repetición → automatización.** Patrones que se repiten entre sesiones y el mecanismo
   que los elimina: hook, skill o script.
4. **Solape y huecos.** Agentes redundantes entre sí, agentes nunca invocados, y capacidades
   que ningún recurso cubre.

Evidencia admisible para **generar** hallazgos, en orden de prioridad: la conversación en
curso, el estado del disco y el historial de git. No se admiten impresiones sin respaldo
verificable.

El registro de auditorías previas queda expresamente fuera de esta lista: no genera
hallazgos, solo filtra los rechazados y anota la antigüedad de los reincidentes (ver
sección 12).

### Fase 3 — Priorización

Cada hallazgo se emite con cuatro atributos:

- **Severidad:** `bloqueante` (impide trabajar o corrompe el resultado) / `fricción`
  (cuesta tiempo cada vez) / `cosmético`.
- **Coste de arreglo:** estimación en minutos u operaciones.
- **Consecuencia de no arreglarlo:** enunciado concreto, no genérico.
- **Eje** del que procede.

Se ordenan por severidad descendente (`bloqueante` → `fricción` → `cosmético`) y, a igualdad
de severidad, por menor coste de arreglo. **Se presentan como máximo siete.** El resto se
escribe en el registro con estado `pendiente` y nota "detectado, no priorizado". Un informe
de treinta puntos no se lee, y un auditor que no se lee no sirve.

### Fase 4 — Aprobación y aplicación

Ver secciones 8 y 9.

## 7. Formato del informe

Se escribe en `Auditorias/AAAA-MM-DD-auditoria.md`. Es inmutable una vez escrito: constituye
el historial. Contiene:

- Fecha, ámbito (`completo` o el foco indicado) y resumen en tres líneas.
- Mapa de recursos de la Fase 0.
- Los hallazgos priorizados, con sus cuatro atributos y la acción propuesta.
- Hallazgos reincidentes, con su antigüedad.
- Hallazgos no priorizados, en lista breve.
- Decisiones tomadas por Mario en esta pasada.

Si en una fecha ya existe un informe, el nuevo fichero añade sufijo `-2`, `-3`, etc.

## 8. Registro de decisiones

`Auditorias/registro.md` es la tabla viva del proyecto. Una fila por hallazgo:

| ID | Hallazgo | Eje | Severidad | Estado | Fecha | Nota |
| --- | --- | --- | --- | --- | --- | --- |
| AUD-001 | `Skills/` fuera de `.claude/skills/`: humanizer no cargable | Doctrina | Bloqueante | aplicado | 2026-08-07 | commit `a1b2c3d` |

Los ID son estables y correlativos (`AUD-001`, `AUD-002`, ...) y nunca se reutilizan.

### Estados y sus consecuencias mecánicas

| Estado | Significado | Efecto en la siguiente auditoría |
| --- | --- | --- |
| `pendiente` | Propuesto, sin resolver | **Reaparece**, marcado con su antigüedad: "propuesto hace N auditorías" |
| `aplicado` | Ejecutado, con hash de commit | No reaparece. Si el síntoma vuelve, se levanta hallazgo nuevo etiquetado "regresión de AUD-00X" |
| `rechazado` | Mario dijo que no, con motivo escrito | **No se vuelve a proponer nunca** |
| `obsoleto` | Dejó de aplicar por cambios del proyecto | No reaparece |

La regla de `rechazado` es la aplicación al propio auditor de la regla 6 de `CLAUDE.md`
("lo que Mario rechace una vez no se vuelve a proponer"). El motivo del rechazo se escribe
siempre en la columna Nota.

La detección de regresiones es deliberada: que un arreglo no aguante es una señal más
valiosa que el hallazgo original, porque indica que la causa raíz seguía viva.

### Regla de cierre

El registro se actualiza y se commitea **aunque Mario rechace todos los hallazgos**. Un "no"
es información, y no guardarla garantiza repetir la conversación.

## 9. Aplicación de cambios

- **Nada se aplica sin aprobación explícita de Mario, hallazgo por hallazgo.** No hay
  categoría de cambio autoaplicable.
- **Un commit por hallazgo**, con mensaje `auditoría(AUD-00X): <resumen>`. Cada cambio queda
  revertible por separado.
- **Sin worktree, deliberadamente.** El proyecto acumula ramas `worktree-*` sin fusionar; más
  worktrees es más deuda, no más aislamiento. El commit atómico ya proporciona la marcha
  atrás.
- **Puertas duras.** Modificar cualquiera de estas rutas exige mostrar el diff completo
  **antes** de escribir, además de la aprobación:
  - `CLAUDE.md`
  - `.claude/agents/**`
  - `Datos/**`

  Las dos primeras son la constitución del proyecto. La tercera es la fuente canónica del
  perfil de consumo del CPD: un movimiento silencioso ahí contamina el TFM entero.
- El auditor puede crear hooks, skills y scripts, y puede reescribir agentes y `CLAUDE.md`,
  siempre bajo las condiciones anteriores.

## 10. Ficheros que crea esta implementación

| Ruta | Contenido |
| --- | --- |
| `.claude/skills/auditor/SKILL.md` | La skill: frontmatter con `name` y `description`, y las cinco fases como instrucciones ejecutables |
| `Auditorias/registro.md` | Tabla vacía con cabecera y leyenda de estados |
| `Auditorias/diseno-auditor.md` | Este documento |

`Auditorias/` se añade al mapa de carpetas de `CLAUDE.md`, y el auditor se añade a la tabla
de recursos con su criterio de invocación.

## 11. Criterios de aceptación

La implementación se considera correcta cuando:

1. `/auditor` aparece entre las skills disponibles al iniciar sesión en el proyecto.
2. Una invocación de `/auditor` produce un informe en `Auditorias/` y deja el registro
   actualizado, aunque no se apruebe ningún cambio.
3. Ejecutada dos veces seguidas, la segunda pasada **no repite** ningún hallazgo marcado como
   `rechazado` y **sí** repite los `pendiente`, indicando su antigüedad.
4. Ningún hallazgo propone crear un recurso cuya capacidad ya figure en el mapa de la Fase 0.
5. Ningún informe presenta más de siete hallazgos priorizados.
6. Ninguna escritura sobre `CLAUDE.md`, `.claude/agents/**` o `Datos/**` ocurre sin diff previo
   mostrado.
7. Cada cambio aplicado corresponde a exactamente un commit con el prefijo `auditoría(AUD-`.

## 12. Riesgos conocidos

- **Coste de contexto.** Un barrido completo es caro. Mitigado por la delegación de la Fase 1
  a un subagente y por el tope de siete hallazgos. Si aun así resulta gravoso, la mitigación
  siguiente es usar `/auditor <tema>` como modo habitual y reservar el completo para hitos.
- **Autoridad amplia.** El auditor puede reescribir `CLAUDE.md` y los agentes. La mitigación
  es procedimental: aprobación caso por caso, diff previo obligatorio y un commit por cambio.
- **Sesgo de confirmación entre pasadas.** Al leer el registro antes de analizar, el auditor
  podría anclarse en hallazgos previos y dejar de mirar con ojos nuevos. Mitigación: la Fase 2
  recoge evidencia antes de contrastar con el registro; el registro solo se usa para filtrar
  rechazados y marcar antigüedad, nunca como fuente de hallazgos.

## Anexo A — Hallazgos de la exploración preliminar

Detectados durante el brainstorming del 2026-08-07, sin auditoría formal. Sirven como banco
de pruebas de la primera ejecución real: el auditor debería reencontrarlos por sí solo.

1. `Skills/humanizer/`, `Skills/obsidian/` y `Skills/obsidian-vault-maintainer/` están en la
   raíz del repositorio, pero Claude Code solo carga skills de proyecto desde
   `.claude/skills/`. El paso que `CLAUDE.md` marca como obligatorio por Turnitin no es
   invocable. `optimizador-prompts.skill` es un ZIP sin descomprimir.
2. `humanizer.rar`, `obsidian.zip` y `obsidian-vault-maintainer.zip` están versionados junto a
   sus carpetas ya extraídas.
3. `Bibliografia/PDFs/`, `Bibliografia/Resumenes/` y `Datos/PVsyst/` están vacías, y `Memoria/`
   no contiene ningún `.tex`: el pipeline bibliográfico y la regla de compilación no se han
   ejercitado nunca.
4. `Datos/Consumo CPD/` presenta anidamiento `datos/datos/h/`, mezcla de `.xlsx` y `.csv`,
   ZIPs junto a sus carpetas extraídas y un fichero llamado
   `miraaverfaltaagostoperocreoqueesunproblemadelnom.zip`.
5. Coexisten dos sistemas de conocimiento —memoria persistente y vault Obsidian (`wiki/`)—
   cuyos dieciséis conceptos documentan el propio claude-obsidian, no el TFM. Nadie audita el
   solape.
6. Higiene de git: tres ramas `worktree-*` sin fusionar ni borrar, `.claude/worktrees/` sin
   ignorar, `Sin título.canvas` vacío en la raíz y `Listado de TFMs ERMA XX.pdf` suelto en la
   raíz.
