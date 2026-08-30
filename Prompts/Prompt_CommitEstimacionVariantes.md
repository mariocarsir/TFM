# Merge de estimación de variantes FV

Estoy en la rama master. Quiero mergear la rama worktree-estimacion-variantes-fv, que contiene el análisis de variantes de autoconsumo FV del CPD (9 commits) ya preparado para mergear sin conflictos de contenido, salvo un archivo.

  Haz esto:

  1. Comprueba que el working tree está limpio (git status) antes de nada.
  2. Ejecuta git merge worktree-estimacion-variantes-fv.
  3. Debería fallar solo por conflicto en Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx. Si hay más archivos en conflicto, párate y dime
     cuáles antes de resolver nada.
  4. Para ese archivo, quédate con la versión de master (la nuestra, --ours), porque es más reciente y más completa que la de la rama que se
     mergea — ya está verificado que es un superconjunto:
  git checkout --ours "Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx"
  git add "Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx"
  5. Comprueba que no queda ningún otro archivo sin resolver (git status) y completa el merge con git commit (usa el mensaje de merge por defecto     que propone Git, no hace falta editarlo).
  6. Enséñame el git log --oneline -12 final y el git status para confirmar que quedó limpio.

  No hagas push todavía, eso lo reviso yo.
