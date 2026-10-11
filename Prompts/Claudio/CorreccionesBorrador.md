# CorreccionesBorrador

- **Fecha de la petición:** 11/10/2026 (hora no registrada)
- **Contexto (cuándo):** después de que Claude depurase `Prompts/Prompt_CorreccionesBorradorCap6.md` contrastándolo con el borrador real del capítulo 6 (rama `worktree-Capitulo6ModulosBorrador`) y detectase 10 problemas: 9 fichas en uso y no 12, decimales del radar que no vienen de pesos, referencias internas en las líneas 99 y 101, efectos en cadena de borrar «Tecnologías de generación fotovoltaica», etc.
- **Objetivo (por qué):** ejecutar las correcciones del capítulo 6 en una sesión aparte a partir de una versión sin ambigüedades. Las decisiones A–F están marcadas con su recomendación y se dan por aceptadas salvo que Mario diga lo contrario antes de ejecutar.

---

## Prompt

```markdown
# Correcciones del borrador del capítulo 6 (v2)

Base: rama `worktree-Capitulo6ModulosBorrador` (NO origin/master). Worktree nuevo desde esa rama.
Delegar: redacción → redactor-humanizador; fichas → bibliotecario-pdf (densidad Ejecutivo, una sola pregunta).

## 1. Reglas de oro (guardar en memoria antes de tocar el texto)
- Tablas: dato no encontrado → «N/D»; no aplica → «N/A». Sin variantes («No figura», «No declarado»…).
  → ampliar `feedback_formato_tablas_y_notas_editor`.
- Prohibido referir documentación interna no publicable (guías de asignatura, TFM ajenos) como fuente
  o como origen del método. Un TFM solo se cita si Mario lo pide expresamente. Global para los capítulos restantes.
  → memoria feedback nueva + agente redactor-humanizador. Corregir en cap. 6: líneas 99, 101 y notas
  de las tablas V1b/V2 y V3. Avisar de «recálculo de superficies» como caso dudoso.

## 2. Fichas técnicas (`Datos/Fichas Técnicas/Módulos/`)
- Crear `OLD/` y mover allí las fichas sin uso: las 3 de `V1b/` (AIKO 2P 475, LONGi Hi-MO X6, REC Alpha).
- Renombrar `V2/` → `V1b-V2/` y borrar `V1b/` vacía (git mv).
- Actualizar la ruta en la cabecera de capitulo06.tex y en `feedback_fichas_tecnicas_fuente_unica`.

## 3. Apartado 6.1.1
### 3.1 «Tecnologías de generación fotovoltaica»: eliminar
- Fuera el subapartado, su Tabla de tecnologías y la frase introductoria de la línea 39.
- Llevar a V1a el descarte de la capa fina (34,0 Wp/m²); en V2, definir en una frase el vidrio-vidrio.
- Actualizar CLAUDE.md y `project_estructura_indice_erma` (el estado del arte de las tecnologías FV ya no vive en el 6.1).

### 3.2 «Método de selección» → «Criterios de selección»
- Fuentes citables: las 9 fichas en uso, vía bibliotecario-pdf. Los rankings, solo si Mario aporta
  PDF/URL de Black Ridge y CleanEnergyReviews 2025. pvXchange y bancabilidad: pendientes (las da Mario).
- Dato ausente: nunca la peor nota. Hacer inventario de todos los N/D por candidato y criterio, ENTREGARLO
  a Mario y PARAR antes de rehacer valoraciones y conclusiones. Mientras tanto, [decisión B].
- Decimales del radar: [decisión A]. Explicar en una frase que no hay pesos entre criterios.
- Definición de los 8 criterios, sin paréntesis valorativos, con la forma:
  «[Criterio]: [explicación]. [Qué valor es preferible].»
- Tabla 6.3 actual (criterio limitante y requisito de paso, que será la 6.2): pasarla a bullets, uno por variante.

### 3.3 Apartados por variante (V1a, V1b-V2, V3)
- Estructura: introducción breve → tabla comparativa → radar → conclusión breve que justifique la elección.
- Eliminar los bullets «Los criterios que no figuran en la tabla se valoran con…» y los bullets de
  conclusión. Destino de esos datos: [decisión D].
- No repetir datos ya presentes en tablas o fichas («el GL.04», no «el GL.04 de 1.641 × 989 mm»).
  Sí se mantienen los cálculos propios que sostienen la elección.
- AGC: [decisión C]. V3: si cambia la nota de bifacialidad del LONGi, revisar la elección.

## 4. Cierre
- Compilar (pdflatex → bibtex → pdflatex ×2, 0 indefinidas) y entregar el PDF del borrador.
- Commit en el worktree con título según la convención. Sin push.
- Humanizer NO en esta ronda: va después de la revisión de Mario.
```

## Decisiones A–F (recomendación por defecto)

| # | Decisión | Recomendación |
|---|---|---|
| A | Decimales del radar | Explicarlo en el texto, sin cambiar el método. En los empates, todos reciben el mismo entero (3-3-2). En los criterios compuestos se usa una media simple, dicho de forma explícita. Los decimales solo aparecen en los ejes compuestos. |
| B | Radar mientras falta un dato | Sacar ese aspecto de la media de ese candidato. Si le falta el criterio entero, no se pinta y se marca con `\nota{}`. |
| C | AGC | Descartarlo del radar como «no dimensionable»; no pedir datos que no existen (vidrio a medida). |
| D | Datos de los bullets eliminados | Añadirlos como filas a las tablas comparativas. Rompe la regla de filas del 04/10, por eso es decisión de Mario. |
| E | Carpetas | Fusionada: `Módulos/V1b-V2/`. OLD: `Módulos/OLD/`. |
| F | Capítulos 1 y 2 | Pasarles también un grep de la regla 2 (referencias internas), aunque el prompt original dice «capítulos restantes». |
