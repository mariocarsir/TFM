---
description: Guarda un snapshot estructurado de la sesión actual en 00_Gestion/Snapshots/YYYY-MM-DD_HHmm_sesion_N.txt. Numera la sesión automáticamente leyendo los snapshots existentes. Uso: /snapshot [tema-breve]
argument-hint: [tema-breve-de-la-sesion]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# Guardar snapshot de sesión

El usuario ha invocado este comando con: $ARGUMENTS

## Tu rol

Generas un snapshot del estado actual de la sesión de trabajo con Mario para que mañana (u otro día) se pueda retomar sin perder contexto. **No es un commit Git**, es un resumen narrativo guardado como `.txt`.

Estructura idéntica a snapshots previos del proyecto: ver `00_Gestion/Snapshots/2026-05-10_1831_sesion_2.txt` como referencia.

---

## Paso 1 — Determinar nombre de archivo

1. Listar todos los snapshots existentes:
   ```bash
   ls 00_Gestion/Snapshots/
   ```
   o usar `Glob 00_Gestion/Snapshots/*.txt`.
2. Identificar el número de sesión más alto presente en los nombres (`sesion_N.txt`) y sumar 1.
3. Obtener fecha y hora actuales:
   ```bash
   date +"%Y-%m-%d_%H%M"
   ```
   (en Windows PowerShell: `Get-Date -Format "yyyy-MM-dd_HHmm"`).
4. Tema breve: si `$ARGUMENTS` contiene texto, usarlo como tema. Si no, derivar del trabajo realizado en la sesión.
5. Nombre final: `YYYY-MM-DD_HHmm_sesion_N.txt`

---

## Paso 2 — Recolectar contexto

Antes de redactar, comprobar el estado actual del proyecto:
- `git status` y `git log --oneline -10` para identificar commits de la sesión.
- `git diff --stat HEAD~N` si hubo varios commits, para resumir cambios.
- Listar archivos nuevos o modificados que aún no estén commiteados.

---

## Paso 3 — Redactar el snapshot

Estructura fija (en `.txt` plano, encoding UTF-8, sin BOM):

```
================================================================================
SNAPSHOT DE SESIÓN — TFM Mario Carrión Sirvent
Fecha: YYYY-MM-DD  |  Hora: ~HH:MM  |  Sesión: N
Tema: <tema breve>
================================================================================


RESUMEN EJECUTIVO
--------------------------------------------------------------------------------
[3-6 líneas: qué se ha hecho en esta sesión, qué decisiones se han tomado,
en qué estado queda el proyecto. Sin floreo.]


INTERCAMBIOS CLAVE (cronológico)
--------------------------------------------------------------------------------
1. "<frase literal del usuario>" → [qué hice]
2. "<…>"                        → [qué hice]
[…]


ARCHIVOS CREADOS / AFECTADOS EN ESTA SESIÓN
--------------------------------------------------------------------------------
[CREADOS]
  ruta/al/archivo                  (descripción breve)

[MODIFICADOS]
  ruta/al/archivo                  (qué se cambió)

[RENOMBRADOS]
  ruta/origen -> ruta/destino

[DES-TRACKEADOS / ELIMINADOS]
  ruta/al/archivo                  (motivo)


COMMITS GIT REALIZADOS (N esta sesión)
--------------------------------------------------------------------------------
<hash>  <mensaje>


ESTADO DEL PROYECTO TRAS LA SESIÓN
--------------------------------------------------------------------------------
GIT / GITHUB:
  - [estado de la rama, último commit, sincronización con origin]

LATEX (02_Memoria/main.pdf):
  - [si se compiló: páginas, tamaño, warnings notables]

CLAUDE.md / config:
  - [cambios relevantes]

MEMORIA PERSISTENTE:
  - [nuevas memorias creadas o actualizadas]


PRÓXIMOS PASOS (en orden, para próxima sesión)
--------------------------------------------------------------------------------
  #N  ⌛ PENDING    [descripción]


PENDIENTES MENORES APUNTADOS
--------------------------------------------------------------------------------
- [pendiente concreto, no bloqueante]


CONTEXTO TÉCNICO PARA NO RE-DERIVAR
--------------------------------------------------------------------------------
- [decisión técnica o gotcha que importa recordar]

================================================================================
FIN DEL SNAPSHOT — Sesión N
================================================================================
```

---

## Paso 4 — Reglas de redacción

- **Frases literales del usuario**: copiar entrecomilladas; preservan el tono real del intercambio.
- **No floreo IA**: nada de "es importante destacar", "en la presente sesión". Frases secas y operativas.
- **Marcas de estado**: `✓ COMPLETED`, `⌛ PENDING`, `⚠ BLOCKED` para próximos pasos.
- **Codificación**: UTF-8 sin BOM. Tildes y caracteres especiales en plano.
- **Longitud**: lo necesario; típicamente 100-250 líneas. Si es más corto, mejor — un snapshot inflado no se relee.

---

## Paso 5 — Escritura del archivo

Usar `Write` directamente al path completo:
```
00_Gestion/Snapshots/YYYY-MM-DD_HHmm_sesion_N.txt
```

Tras escribir, hacer un `Read` rápido del archivo para confirmar que se guardó.

---

## Paso 6 — Reporte a Mario

Mostrar:
1. Ruta del archivo creado.
2. Número de sesión asignado.
3. Resumen ejecutivo en 2 líneas.
4. Preguntar si quiere commitear y pushear el snapshot al repo (política actual: sí se commitean).

---

## Ejemplos de uso

```
/snapshot
/snapshot Creación de skills locales
/snapshot Outline capítulo 3 + recopilación datasheets
```
