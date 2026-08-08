---
type: decision
title: Shim python3 para hooks de claude-obsidian en Windows
status: active
created: 2026-08-06
updated: 2026-08-06
tags:
  - decision
  - claude-code
  - claude-obsidian
  - windows
  - troubleshooting
---

# Shim python3 para hooks de claude-obsidian en Windows

## Contexto

Los hooks `SessionStart` (matcher `startup|resume|clear|compact`) y `Stop` de [[claude-obsidian]] invocan el comando literal `python3` para ejecutar `scripts/claude-obsidian.py`. En Windows, el instalador oficial de python.org solo registra `python.exe` en el PATH del sistema — no crea un alias `python3.exe`, a diferencia de macOS/Linux. Un alias `python3` definido en el perfil de Git Bash no resuelve el problema: Claude Code invoca los comandos de hook contra el PATH real de Windows, no contra el shell de Bash.

## Sintoma

Ambos hooks fallaban con `Executable not found in $PATH: "python3"` en cada arranque de sesion (`SessionStart`) y al cerrarla (`Stop`), visible en la interfaz de Claude Code como error no bloqueante.

## Decision

Crear un shim `python3.bat` en el mismo directorio que `python.exe` (`C:\Users\Usuario\AppData\Local\Programs\Python\Python312\`, ya presente en el PATH de Windows), que reenvia todos los argumentos:

```bat
@echo off
"%~dp0python.exe" %*
```

Alternativas descartadas: editar `hooks.json` dentro de la cache del plugin (se sobrescribiria en cada actualizacion de `claude-obsidian`) y reinstalar Python via Microsoft Store (innecesariamente invasivo).

## Verificacion

- `python3 --version` -> `Python 3.12.10`
- `(Get-Command python3).Source` -> resuelve al shim, confirmando que el PATH real de Windows (no un alias de Bash) lo encuentra
- Invocacion directa de `claude-obsidian.py hook session-start` a traves del shim -> sin error de PATH

## Riesgo residual

Ninguno identificado: el shim no toca el plugin ni la instalacion de Python, y sobrevive a actualizaciones de `claude-obsidian`.
