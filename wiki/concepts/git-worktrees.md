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

## Por qué se usa en este proyecto

Claude Code usa worktrees en contextos de **background jobs** para aislar cambios del checkout principal (donde trabaja Mario localmente):

### Aislamiento de seguridad
- Si estoy editando archivos en un background job, el working directory principal (`~/Escritorio/Claudio/TFM`) permanece intacto
- Mario puede seguir trabajando localmente sin que mis cambios interfieran

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
2. Un background job necesita editar código

### Durante la lectura
No se crea worktree si solo se lee, busca o se responden preguntas. El trabajo ocurre en el checkout principal.

## Ciclo de vida

```
EnterWorktree → trabajo aislado → git commit → push (si hay remoto) → fin del job
                                                                    ↓
                                    worktree se limpia automáticamente
```

### Dentro de un worktree
- Puedo editar múltiples capítulos/archivos en el **mismo worktree**
- Hago commits separados para cada sección si quiero (ej: "Cap 1: redacción inicial" → "Cap 2: redacción inicial")
- Al final del job, todos los commits se pushean a GitHub
- El worktree se limpia automáticamente

## Relación con GitHub

GitHub es la fuente de verdad del repositorio. El worktree es solo infraestructura local de aislamiento:
- Los commits dentro del worktree se pushean normalmente a GitHub
- No hay barrera entre capítulos o secciones dentro del mismo worktree
- La única restricción es: si voy a editar algo, primero necesito estar dentro de un worktree
