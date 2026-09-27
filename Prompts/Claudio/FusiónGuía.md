# FusiónGuía

- **Fecha de la petición:** 27/09/2026 ~13:15 (hora aproximada: la petición se hizo justo antes de que se estableciera esta norma de guardado, registrada a las 13:22)
- **Contexto (cuándo):** al retomar la sesión «PVsyst» el 27/09, después de que Claude recordara que seguía sin fusionar la rama `worktree-guia-pvsyst-sin-vc0`, donde `ingeniero-dominio` había reescrito la guía de PVsyst el 26/09 para quitar la calibración VC0.
- **Objetivo (por qué):** hacer la fusión y la limpieza del worktree en una sesión aparte, para que la sesión de PVsyst quede centrada solo en montar las variantes en el programa.

---

## Prompt

Fusiona en `master` la rama `worktree-guia-pvsyst-sin-vc0` (commit `84c539f GuiaPVsystSinCalibracion`), que reescribe `conocimiento fotovoltaico/Referencia/guia-diseno-pvsyst.md` para quitar el paso de calibración VC0 del flujo de PVsyst (decisión de Mario, 26/09/2026 — ver memoria `feedback_vc0_eliminada_calibracion`). El cambio ya fue revisado: solo toca ese fichero, 120 líneas añadidas / 83 borradas.

Pasos:
1. `git status` primero, por si hay cambios sin commitear en el checkout — si los hay, para y pregunta a Mario, no los toques.
2. `git diff master worktree-guia-pvsyst-sin-vc0` para confirmar que sigue siendo solo ese fichero antes de fusionar.
3. `git merge worktree-guia-pvsyst-sin-vc0` sobre `master`. Título del commit de merge según la convención del proyecto: `MergeGuiaPVsystVC0`.
4. Verificado el merge, borra la rama y el worktree que ya no hacen falta: `git branch -d worktree-guia-pvsyst-sin-vc0` y `git worktree remove` del directorio en `.claude/worktrees/` correspondiente (comprobar con `git worktree list`).
5. No hace falta tocar nada más ni recompilar LaTeX — es un fichero de referencia interno, no la memoria del TFM.
