---
name: project-tres-cantos-sin-urbanizable-no-sectorizado
description: "El PGOU vigente de Tres Cantos (2003) no tiene la categoria de suelo urbanizable no sectorizado; relevante solo para V1/V2 (CPD y aparcamiento, confirmados en Tres Cantos) - la subparcela de V3 se confirmo en Colmenar Viejo, no aqui"
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

## RESUELTO 06/09/2026: la subparcela V3 cae en Colmenar Viejo, no Tres Cantos

Consulté el centroide y las cuatro esquinas del rectángulo envolvente del polígono `Layout1`
(coordenadas dadas por el team lead) contra el servicio oficial `Consulta_RCCOOR` del Catastro
(`ovc.catastro.meh.es`, SRS EPSG:4326). **Los 5 puntos devuelven código de municipio 28045 =
COLMENAR VIEJO.** Contraste: la coordenada del CPD (40,59823 N/−3,71721 O) sí devuelve Tres
Cantos, confirmando que el servicio funciona correctamente.

**Consecuencia:** este hallazgo (que en Tres Cantos no existe "suelo urbanizable no sectorizado")
queda como contexto histórico sin efecto práctico directo sobre V3 — importa solo si se analiza
la clasificación de V1/V2 (CPD y aparcamiento, confirmados en término de Tres Cantos). Para V3
aplica en su lugar el planeamiento de Colmenar Viejo — ver [[project-colmenar-viejo-suelo-no-urbanizable-1987]].

## Cómo aplicar (parte todavía vigente de esta memoria)

1. Para **V1/V2**, sigue aplicando: el PGOU de Tres Cantos de 2003 no tiene "suelo urbanizable no
   sectorizado" — relevante si se analiza la clasificación urbanística de la cubierta del CPD o el
   aparcamiento (aunque previsiblemente ambos están ya en suelo urbano industrial, sin la fricción
   de la V3).
2. Para **V3**, no usar esta memoria — ir a [[project-colmenar-viejo-suelo-no-urbanizable-1987]].
3. Fuente citable pendiente: descargar `https://web.trescantos.es/contenido/urbanismo/pgou_normas.pdf`
   (normas urbanísticas completas de Tres Cantos) y procesarlo con `bibliotecario-pdf` si se
   necesita detalle de V1/V2.
4. Informe completo con más detalle en `Memoria/analisis/normativa-autonomica-y-tecnica.md`.
