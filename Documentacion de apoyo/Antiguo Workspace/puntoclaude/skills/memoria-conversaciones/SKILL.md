---
name: memoria-conversaciones
description: Motor de búsqueda y resumen sobre el historial de conversaciones del TFM (snapshots de sesión + transcripciones .jsonl de Claude Code). Úsalo para localizar en qué sesión se trató un tema, recuperar decisiones o vistos buenos antiguos, o resumir qué se hizo en sesiones pasadas. Reutilizable por el hilo principal y por subagentes (p. ej. el redactor que necesita recuperar un capítulo aprobado). Triggers "¿en qué sesión…", "busca en conversaciones antiguas", "qué decidimos sobre…", "recupera el/la… de hace…", "cuándo hablamos de…".
---

# memoria-conversaciones — Búsqueda en el historial del TFM

Localizas y resumes información tratada en conversaciones pasadas del TFM. **No inventas**: si algo no está en los registros, lo dices.

## Fuentes (de más limpia a más cruda)

1. **Índice de conversaciones:** `00_Gestion/Snapshots/INDICE.md` — tabla por sesión (nº, fecha, temas, archivos afectados, decisiones/vistos buenos). Punto de entrada rápido.
2. **Snapshots:** `00_Gestion/Snapshots/YYYY-MM-DD_HHmm_sesion_N.txt` — resúmenes estructurados de cada sesión.
3. **Transcripciones crudas (`.jsonl`):** `C:\Users\Usuario\.claude\projects\C--Users-Usuario-OneDrive---Universidad-Polit-cnica-de-Madrid-Escritorio-MASTER-TFM\*.jsonl` (y `*\subagents\*.jsonl`). Historial literal de cada sesión; úsalo cuando el índice y los snapshots no basten. Son grandes: **filtra con Grep** por términos antes de leer ningún fragmento.

## Procedimiento

1. **Empieza por el índice** (`INDICE.md`). Si responde a la consulta, para ahí.
2. Si no, **busca (Grep) en los snapshots** por los términos clave.
3. Solo si hace falta literalidad (qué se dijo o se aprobó exactamente), **busca (Grep) en los `.jsonl`** y lee únicamente los fragmentos relevantes. No vuelques transcripciones enteras al contexto.
4. **Cruza fechas:** relaciona cada hallazgo con su sesión (nº y fecha) y el archivo afectado.

## Formato de salida

```
CONSULTA: <lo que se busca>
─────────────────────────────────
HALLAZGOS
- Sesión N (YYYY-MM-DD): <qué se trató / decidió>. Fuente: <snapshot o .jsonl>.
- ...
RECUPERADO (si aplica):
  <texto, decisión o visto bueno literal o parafraseado, con su sesión de origen>
NO ENCONTRADO:
  <lo que la consulta pedía y no aparece en los registros>
```

## Mantenimiento del índice

El índice `INDICE.md` se actualiza al **guardar sesión** (lo hace el hilo principal, no esta skill). Si detectas que el índice está desfasado respecto a los snapshots existentes, indícalo y ofrece regenerarlo a partir de los `.txt` de `Snapshots/`.

## Reglas

- **No inventes** contenido de conversaciones. Si no está en los registros, va en `NO ENCONTRADO`.
- **Solo lectura:** no edites las transcripciones ni los snapshots.
- **Trazabilidad:** cita siempre la sesión y la fecha de cada hallazgo para que Mario pueda verificarlo.
