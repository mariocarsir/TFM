---
type: concept
title: Git worktrees en Claude Code
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags:
  - git
  - workflow
  - claude-code
---

# Git worktrees en Claude Code

Un **worktree de Git** es una característica que permite tener múltiples "árboles de trabajo" del mismo repositorio de forma simultánea. Cada worktree puede estar en una rama diferente y con un estado de trabajo independiente.

## Analogía: mesa de trabajo auxiliar

Un worktree es como una **mesa auxiliar** junto a la mesa de trabajo principal. Permite probar, cortar y pegar cosas sin ensuciar ni desordenar la mesa principal (el checkout donde Mario trabaja en vivo, por ejemplo con Obsidian abierto). Si algo sale mal en la mesa auxiliar, la principal sigue intacta. Solo cuando el resultado de la mesa auxiliar gusta, se traslada a la mesa principal.

## Por qué se usa en este proyecto

Claude Code usa worktrees en contextos de **background jobs** para aislar cambios del checkout principal:

### Aislamiento de seguridad
- Si estoy editando archivos en un background job, el working directory principal (`~/Escritorio/Claudio/TFM`) permanece intacto
- Mario puede seguir trabajando localmente (en Obsidian, VS Code, etc.) sin que mis cambios interfieran

### Evita conflictos en trabajos paralelos
- Si hay múltiples background jobs corriendo simultáneamente, cada uno usa su propio worktree
- Impide que un job sobrescriba los cambios de otro

### Seguridad ante fallos
- Si algo sale mal (merge conflict, error no capturado, edición destructiva), solo afecta al worktree aislado
- El checkout principal queda protegido

## Cuándo se crea un worktree

### Bajo demanda
Un worktree se crea cuando:
1. Se invoca manualmente `EnterWorktree(name: "...")`
2. Un background job necesita editar código — se crea automáticamente **al abrir la sesión**, antes de la primera edición

### Durante la lectura
No se crea worktree si solo se lee, busca o se responden preguntas. El trabajo ocurre directamente sobre el checkout principal.

## Dónde vive y qué ocupa en disco

El worktree vive en **disco local**, no en la nube: `.claude/worktrees/<nombre>/` dentro del propio repositorio.

No duplica todo el proyecto. Hay dos partes con comportamiento distinto:

| Parte | ¿Se duplica? | Ubicación |
|---|---|---|
| Base de datos Git (`.git/objects`, historial de commits) | No — se comparte entre todos los worktrees | Una sola copia en `.git/` |
| Archivos de trabajo (`wiki/`, `Memoria/`, etc.) | Sí — cada worktree tiene su propia copia completa | Una copia por worktree |

Por eso cada worktree activo añade espacio en disco proporcional al tamaño de los archivos de trabajo del proyecto, pero no vuelve a copiar todo el historial de Git.

### Cuándo se eliminan los archivos duplicados

La carpeta del worktree se limpia **automáticamente al terminar el background job**, independientemente de si sus cambios se fusionaron a `master` o no. Los commits hechos dentro del worktree, en cambio, permanecen en Git (en su propia rama) aunque la carpeta desaparezca — fusionarlos a `master` es un paso aparte, no una condición para que se limpien.

## Secuencia de trabajo

```
1. Se abre una sesión nueva
        ↓
2. Se crea el worktree (EnterWorktree)
        ↓
3. Trabajo sobre el worktree (editar archivos, capítulos, notas...)
        ↓
4. Commit — guarda los cambios SOLO en la rama del worktree,
   no en master ni en el checkout principal
        ↓
5. Fusión con master — traslada a la mesa de trabajo principal
   solo los cambios que se quieren conservar
        ↓
[fin de la sesión] → la carpeta del worktree se limpia automáticamente;
                      lo fusionado a master ya está a salvo ahí
```

Puedo editar múltiples archivos o capítulos dentro del **mismo worktree** antes de fusionar — no hace falta fusionar tras cada commit. Por ejemplo: commit del capítulo 1 → commit del capítulo 2 → una sola fusión al final con todo junto.

## Relación con GitHub

GitHub es la fuente de verdad del repositorio. El worktree es solo infraestructura local temporal:
- Los commits dentro del worktree se pueden pushear a su propia rama en GitHub (nunca directamente a `master`)
- Fusionar o pushear a `master` requiere confirmación explícita de Mario — no es una acción automática
- La única restricción operativa es: si voy a editar algo, primero necesito estar dentro de un worktree
