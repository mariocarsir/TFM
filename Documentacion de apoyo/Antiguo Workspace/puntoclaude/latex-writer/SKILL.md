---
name: latex-writer
description: Skill central de LaTeX del TFM. Úsala para escribir y editar archivos .tex, compilar la memoria y corregir errores de compilación con bucle de auto-debug. Triggers: el usuario menciona LaTeX, .tex, pdflatex, biber, compilar, PDF, o pide arreglar un error de compilación.
version: 2.0.0
author: OpenClaw + Gonzalo Aguirre (adaptada al TFM de Mario Carrión Sirvent)
---

# LaTeX Writer — con Auto-Debug (TFM Mario)

Generador y depurador de documentos LaTeX con bucle de compilación y corrección
automática de errores hasta obtener un PDF limpio. Es la skill central de LaTeX
del TFM: cubre redacción técnica en `.tex`, compilación y auto-debug.

> Esta skill se ocupa del **LaTeX en sí** (estructura, entornos, compilación y
> errores), no de la prosa en la voz de Mario: esa la redacta el `tfm-redactor`
> (modo borrador) o el hilo principal, aplicando la skill `tono-mario`.

## Flujo de trabajo obligatorio

```
ESCRIBIR / EDITAR LaTeX
     ↓
COMPILAR (pdflatex + biber)
     ↓
¿Errores?
  NO → Entregar PDF ✓
  SÍ → Leer log → Corregir .tex → volver a COMPILAR
         (máximo MAX_ATTEMPTS = 5 iteraciones)
     ↓
Si persisten errores tras 5 intentos → Reportar y pedir ayuda
```

**Regla crítica:** nunca entregar código LaTeX sin haberlo compilado y verificado.
Si el PDF no compila limpiamente, el trabajo no está terminado.

## Comandos de compilación (entorno Mario: Windows 10 + MiKTeX)

Secuencia oficial del TFM, desde `02_Memoria/`:

```bash
pdflatex -interaction=nonstopmode -file-line-error main.tex
biber main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

`biber` (no `bibtex`): la bibliografía es **biblatex con estilo APA 7**.

## Uso del script automatizado (bucle de auto-debug)

Python disponible como `python` (3.12). Desde `02_Memoria/`:

```bash
python "../.claude/skills/latex-writer/scripts/latex_writer.py" --file "main.tex" --biber
```

- `--file main.tex` activa el bucle de auto-corrección sobre el archivo.
- `--biber` ejecuta biber para la bibliografía biblatex (imprescindible aquí).
- `--max-attempts N` ajusta el número de iteraciones (defecto 5).

Devuelve `SUCCESS`, `FIXED(N)` (con la lista de correcciones) o `FAILED` (con el
log de errores sin resolver).

## ⚠ SEGURIDAD — el auto-fix MODIFICA main.tex

El bucle reescribe el `.tex` directamente cuando encuentra errores fatales:

| Error en log | Auto-fix que aplica | Riesgo |
|---|---|---|
| `Undefined control sequence` | **Comenta** la línea con `% [AUTO-FIX]` | Puede silenciar contenido legítimo |
| `Label multiply defined` | Renombra el 2º `\label` a `<label>-b` | **Rompe los `\cref` que apuntaban a él** |
| `Missing $ inserted` | Envuelve la expresión en `$...$` | Puede mal-delimitar texto |
| `Overfull \hbox` | Inserta `\sloppy` tras `\begin{document}` | Benigno |
| `File '*.sty' not found` | (sin auto-fix) | Instalar el paquete en MiKTeX |

Reglas obligatorias antes de lanzar el bucle sobre `main.tex`:

1. **Commitear o guardar `main.tex` en Git antes** de ejecutar con `--file`
   (red de seguridad: las correcciones son reversibles vía `git`).
2. Tras la corrección, **revisar** las líneas `% [AUTO-FIX]` y cualquier label
   renombrado a `-b` antes de dar el trabajo por bueno.
3. Para `Undefined control sequence` y `Label multiply defined`, **preferir
   corrección manual**: el auto-fix comenta o renombra y puede romper contenido
   o referencias cruzadas del TFM.

## Leer y parsear el log

Tras cada compilación, leer el `.log` o la salida stdout. Buscar:
- `!` → **error fatal** (detiene compilación)
- `LaTeX Warning:` → advertencia (no detiene, pero puede importar)
- `Overfull \hbox` / `Underfull \hbox` → desbordamiento (cosmético)

Formato de error fatal:
```
./main.tex:42: Undefined control sequence.
l.42 \comandoInexistente
```
→ Línea 42, comando `\comandoInexistente` no definido.

## Correcciones comunes (referencia)

| Error en log | Causa probable | Corrección |
|---|---|---|
| `Undefined control sequence \foo` | Comando inexistente o paquete sin cargar | Cargar el paquete o corregir `\foo` |
| `Missing $ inserted` | Matemáticas fuera de entorno `$` | Envolver en `$...$` |
| `File 'paquete.sty' not found` | Paquete no instalado | Instalar en MiKTeX o usar alternativa |
| `Paragraph ended before \cmd` | Línea vacía dentro de comando | Eliminar la línea vacía |
| `Citation 'key' undefined` | Clave no existe en `referencias.bib` | Corregir la clave o añadir la entrada a mano en `referencias.bib` |
| `Label 'X' multiply defined` | Label duplicado | Renombrar uno de los `\label{}` y sus `\cref` |
| `Unicode char not set up` | Carácter sin soporte | Revisar `inputenc`/`fontenc` del preámbulo |
| `Overfull \hbox` | Texto desborda la línea | Reescribir el párrafo o `\sloppy` |
| `Package babel Error` | Opción de idioma | Verificar `\usepackage[spanish]{babel}` |

## Reglas para main.tex (TFM Mario)

- Compilador: **pdflatex** (NO xelatex/lualatex).
- Bibliografía: **biber** con biblatex **estilo APA 7**. Citar con `\parencite{}`
  o `\textcite{}`, **nunca `\cite{}`**.
- **No modificar el preámbulo** salvo instrucción explícita.
- **No editar auxiliares** (`.aux`, `.bbl`, `.bcf`, `.log`, `.toc`, `.run.xml`...).
- Cada sección termina **de forma lógica** (no forzar `\newpage`).
- Tablas y figuras llevan **siempre** `\label{}`.
- Las nuevas entradas de `referencias.bib` se añaden a mano (formato biblatex
  APA 7); esta skill solo procesa la bibliografía existente vía biber.

## Trigger conditions

Invocar esta skill cuando:
1. Se pide escribir, editar o corregir un archivo `.tex`.
2. Se menciona "LaTeX", "pdflatex", "biber", "compilar", "PDF".
3. Se pide corregir errores de compilación LaTeX.
4. Se detecta un `.tex` en el directorio de trabajo y hay que compilarlo.
