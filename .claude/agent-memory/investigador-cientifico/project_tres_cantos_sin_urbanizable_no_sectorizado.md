---
name: project-tres-cantos-sin-urbanizable-no-sectorizado
description: "El PGOU vigente de Tres Cantos (2003) no tiene la categoria de suelo urbanizable no sectorizado, lo que puede cerrar la via de la Ley 9/2001 (arts. 26.1.c/27.1.d) para la variante 3 si la subparcela cae en ese termino municipal"
metadata:
  type: project
---

## Contradicción detectada (06/09/2026)

`Bibliografia/Resumenes/ComunidadMadrid_2001.md` identifica los arts. 26.1.c) y 27.1.d) de la
Ley 9/2001 del Suelo de Madrid (generación de energía para autoconsumo / centros de proceso de
datos) como la vía más directa para legitimar la variante 3 — pero **ambos artículos solo aplican
a "suelo urbanizable no sectorizado"**.

La página oficial de planeamiento del Ayuntamiento de Tres Cantos
(`https://web.trescantos.es/tramite/planeamiento/`, consultada 06/09/2026) declara textualmente:
**"con el vigente Plan General aprobado el 07.05.2003 no existe suelo urbanizable no
sectorizado"** en el término municipal.

## Consecuencia

Si la subparcela candidata de V3 (de `Datos/Catastro/V3 Terreno amplio/` → `afecciones`, ver
[[project-seleccion-parcela-v3-catastro]]) cae en término de **Tres Cantos**, la vía del 26.1.c/
27.1.d **no está disponible**. Solo quedarían: suelo urbano, suelo urbanizable sectorizado, o
suelo no urbanizable de protección — y en este último caso, solo el art. 29.3 (lista tasada SIN
FV, ver [[project-suelo-agrario-fv-ley9-2001]] en la memoria de proyecto) o la vía excepcional del
29.1 (sin legislación sectorial habilitante identificada).

## Cómo aplicar

1. **No dar por buena la vía del art. 26.1.c/27.1.d para V3 sin antes confirmar el término
   municipal exacto de la subparcela elegida.** Es un pendiente crítico, no un detalle menor.
2. Si la subparcela cae en **Colmenar Viejo**, este hallazgo no aplica automáticamente — hay que
   verificar el régimen de suelo de ESE municipio por separado (su planeamiento vigente no se pudo
   identificar con fuente fiable en la sesión del 06/09/2026; solo se sabe que aprobaron el
   Documento de Avance de un PGOU nuevo en enero de 2025, fase muy temprana).
3. Fuente citable pendiente: descargar `https://web.trescantos.es/contenido/urbanismo/pgou_normas.pdf`
   (normas urbanísticas completas de Tres Cantos) y procesarlo con `bibliotecario-pdf` antes de
   escribir el apartado 2.4/análisis de viabilidad de V3 en LaTeX.
4. Informe completo con más detalle en `Memoria/analisis/normativa-autonomica-y-tecnica.md`.
