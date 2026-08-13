---
type: concept
title: "superpowers (plugin)"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - superpowers
domain: "Claude Code plugins"
complexity: intermediate
related:
  - "[[tfm-skills]]"
  - "[[superpowers-using-superpowers]]"
  - "[[superpowers-brainstorming]]"
  - "[[superpowers-dispatching-parallel-agents]]"
  - "[[superpowers-executing-plans]]"
  - "[[superpowers-finishing-a-development-branch]]"
  - "[[superpowers-receiving-code-review]]"
  - "[[superpowers-requesting-code-review]]"
  - "[[superpowers-subagent-driven-development]]"
  - "[[superpowers-systematic-debugging]]"
  - "[[superpowers-test-driven-development]]"
  - "[[superpowers-using-git-worktrees]]"
  - "[[superpowers-verification-before-completion]]"
  - "[[superpowers-writing-plans]]"
  - "[[superpowers-writing-skills]]"
---

# superpowers

Plugin de Claude Code (marketplace `claude-plugins-official`) que aporta disciplina de proceso genérica: cuándo explorar intención antes de construir, cómo depurar de forma sistemática, cómo pedir y recibir revisión de código, cómo aislar trabajo en un worktree, cómo verificar antes de dar algo por completado. No es específico del dominio del TFM (fotovoltaica/CPD) — es una capa de metodología que se aplica a cualquier tarea de la conversación con Claude Code, incluida la gestión de este mismo vault.

**Instalación:** caché de plugin en `C:\Users\Usuario\.claude\plugins\cache\claude-plugins-official\superpowers\` (varias versiones conviven en caché; la sesión que documentó este catálogo usaba 6.3.0).
**Activación:** la skill [[superpowers-using-superpowers]] se carga al inicio de la conversación vía hook de sesión y exige comprobar, antes de cualquier respuesta, si alguna otra skill del plugin aplica a la tarea en curso.

## Skills incluidas

- [[superpowers-using-superpowers]] — establece la regla de invocar skills antes de responder; punto de entrada del plugin.
- [[superpowers-brainstorming]] — explora intención, requisitos y diseño antes de cualquier trabajo creativo.
- [[superpowers-dispatching-parallel-agents]] — reparte tareas independientes entre varios subagentes en paralelo.
- [[superpowers-executing-plans]] — ejecuta un plan de implementación ya escrito, con puntos de revisión.
- [[superpowers-finishing-a-development-branch]] — decide cómo integrar una rama de desarrollo ya completa y con tests en verde.
- [[superpowers-receiving-code-review]] — cómo procesar feedback de revisión de código con rigor, sin aceptación performativa.
- [[superpowers-requesting-code-review]] — verifica que un trabajo cumple los requisitos antes de darlo por terminado o fusionarlo.
- [[superpowers-subagent-driven-development]] — ejecuta un plan con tareas independientes dentro de la sesión actual, vía subagentes.
- [[superpowers-systematic-debugging]] — metodología ante cualquier bug o fallo de test, antes de proponer una solución.
- [[superpowers-test-driven-development]] — escribir el test antes que el código de implementación.
- [[superpowers-using-git-worktrees]] — aísla trabajo de features en un worktree nativo o vía git.
- [[superpowers-verification-before-completion]] — exige evidencia (comandos ejecutados y su salida) antes de afirmar que algo funciona o está listo.
- [[superpowers-writing-plans]] — redacta un plan a partir de una especificación, antes de tocar código.
- [[superpowers-writing-skills]] — crea, edita y verifica skills nuevas antes de desplegarlas.
