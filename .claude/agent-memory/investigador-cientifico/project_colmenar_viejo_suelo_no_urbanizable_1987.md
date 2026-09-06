---
name: project-colmenar-viejo-suelo-no-urbanizable-1987
description: "V3 confirmada en Colmenar Viejo; su plan de 1987 clasifica en N/P, y la Disposicion Transitoria 1a de la Ley 9/2001 (verificada en BOE) reinterpreta N como urbanizable no sectorizado -> abre el art 26.1.c si la subparcela es N; parque regional y Red Natura descartados geograficamente; falta saber si es N o P"
metadata:
  type: project
---

## Confirmación del término municipal (06/09/2026)

Consulté el centroide y las 4 esquinas del rectángulo envolvente del polígono `Layout1` (V3)
contra `Consulta_RCCOOR` del Catastro (EPSG:4326). Los 5 puntos devuelven **municipio 28045 =
COLMENAR VIEJO**. Ver [[project-tres-cantos-sin-urbanizable-no-sectorizado]] para el contraste con
el CPD (que sí está en Tres Cantos).

## Documento localizado y parcialmente leído

*"Modificación del Plan General de Colmenar Viejo — Normas Urbanísticas, Volumen 3, Título 5:
Regulación del Suelo No Urbanizable"*. PDF en
`https://web.trescantos.es/contenido/urbanismo/colmenarviejo_no_urba.pdf` (60 páginas, escaneado;
alojado en el servidor de Tres Cantos por herencia histórica — Tres Cantos se segregó de Colmenar
Viejo en 1991). Diligencia repetida en casi cada página: *"Aprobado [provisionalmente]
(ratificación) por el Pleno de este Ayuntamiento en sesión celebrada el día 13 FEB 1987"*, con
sello de informe favorable de la Comunidad de Madrid (Consejería de Ordenación del Territorio,
Medio Ambiente y Vivienda).

## Clasificación del suelo no urbanizable (numeración de la antigua Ley del Suelo estatal, arts.
85/86/43.3 LS y 42/44 RG — anterior a la Ley 9/2001 de la Comunidad de Madrid)

- **N. Suelo No Urbanizable Común**: N.1 orientación ganadera; N.2 orientación ganadera
  compatible con explotación agrícola.
- **P. Suelo No Urbanizable de Protección Especial** (15 subáreas: reserva natural integral, alto
  valor ecológico, parque comarcal agropecuario, protección ecológica, dehesas, interés
  paisajístico, agrícola de posible regadío, interés histórico-cultural, ríos/cauces/arroyos,
  carreteras, ferroviarias, hidráulico-sanitarias, eléctricas, caminos/vías pecuarias,
  instalaciones militares, instalaciones especiales).

## Hallazgo clave — mecanismo distinto del art. 29.3 de la Ley 9/2001

Texto literal (Capítulo 3, Régimen Jurídico): *"No se podrán realizar otras construcciones que
las destinadas a explotaciones agrícolas [...]. Sin embargo, podrán autorizarse, siguiendo el
procedimiento previsto en el artículo 43.3 LS, edificaciones e instalaciones de utilidad pública o
interés social [...]. Lo anterior es relativo al suelo no urbanizable común. En el suelo no
urbanizable de Especial Protección no podrán ser permitidos usos ni edificaciones que impliquen
transformación de su destino."*

El capítulo P.12 (Infraestructuras Eléctricas) añade: *"Cuando las instalaciones eléctricas
discurran por el suelo no urbanizable común se podrán autorizar instalaciones de utilidad pública
[...] siguiendo el procedimiento previsto en art. 43.3 LS [...]. La infraestructura de energía
eléctrica tiene atribuida esta utilidad pública por aplicación de su legislación específica
(art. 8º Ley 10/1966)."*

A diferencia de la lista tasada del art. 29.3 de la Ley 9/2001 actual (sin FV, ver
[[project-suelo-agrario-fv-ley9-2001]] en la memoria de proyecto), esta vía de "utilidad pública o
interés social" en Suelo No Urbanizable Común **no es una lista cerrada**.

## ACTUALIZACIÓN 06/09/2026 (noche) — dos de las cuatro reservas resueltas

**Derecho transitorio [RESUELTO]:** leí directamente el texto consolidado del BOE de la Ley
9/2001 (descargado completo, 139 páginas) y encontré la **Disposición Transitoria Primera**
(p. 135): *"[...] c) Al suelo urbanizable no programado y al suelo no urbanizable común se les
aplicará el régimen establecido en la presente Ley para el suelo urbanizable no sectorizado. [...]
d) Al suelo no urbanizable especialmente protegido se le aplicará el régimen [...] para el suelo
no urbanizable de protección."* Esto significa que el antiguo **Suelo No Urbanizable Común (N) se
reinterpreta como "urbanizable no sectorizado"**, NO como "no urbanizable de protección". Si la
subparcela de V3 es N, el **art. 26.1.c de la Ley 9/2001 sí le aplica** (generación FV para
autoconsumo, habilitable por calificación urbanística) — ya no depende solo de la vía, más débil,
del art. 43.3 LS. También verifiqué la Disposición Transitoria Tercera (p. 135): los planes ya
aprobados definitivamente mantienen su vigencia.

**Afección de espacios protegidos [RESUELTO, con matiz]:** consulté los 5 puntos (centroide + 4
esquinas del rectángulo envolvente) contra los servicios WMS oficiales del IEPNB — capa `enp_2024`
(`https://geoserver-des.iepnb.es/geoserver/ENP/wms`) y capa `rn2000`
(`https://geoserver.iepnb.es/geoserver/RN2000/wms`) — con control de sanidad positivo en La
Pedriza (que sí devolvió el Parque Regional y la ZEC "Cuenca del río Manzanares"). **Los 5 puntos
de la parcela V3 dan resultado negativo en las dos capas: no está en el Parque Regional de la
Cuenca Alta del Manzanares ni en Red Natura 2000.** Matiz: solo 5 puntos del rectángulo envolvente,
no el contorno completo del polígono; no comprobé vías pecuarias (no localicé el servicio WMS
correspondiente de la CM) ni el criterio general 2 del Anexo III de la Ley 21/2013
(infraestructura verde).

## Conclusión reformulada tras esta actualización

El pendiente crítico nº1 de este hallazgo (clasificación N/P real de la subparcela, ver planos de
zonificación 1:10.000 no localizados) es ahora, con diferencia, **el dato más importante de todo
el análisis de V3**: con el derecho transitorio ya resuelto a favor de N→art.26.1.c, y con la
protección especial por espacio protegido descartada geográficamente, solo falta saber si la
subparcela concreta es N o P para determinar si la vía FV está abierta o cerrada.

## Tres reservas críticas originales (dos ya resueltas arriba) — NO dar el hallazgo por concluyente

1. **No sé si las subparcelas concretas** ("Arroyo del Buitre" polígono 45 parcelas 47 y 18 en
   polígono 43 parcela 188, "El Olivo" parcela 213, "La Vencosilla" parcela 74) son **N (Común)**
   o **P (Protección Especial)** — solo lo dicen los planos de zonificación 1:10.000, no
   localizados en esta sesión (el documento leído es solo texto normativo, sin planos). Si son P,
   la vía se cierra.
2. El capítulo P.12 concreto parece referirse a tendidos/infraestructura de transporte-
   distribución (como el resto de la serie P.9-P.11), no necesariamente a una planta de
   generación FV — la cita general del Capítulo 3 (cualquier "utilidad pública o interés social")
   es la que realmente podría abrir la puerta, y requeriría declaración expresa caso por caso.
3. **No he verificado la relación jurídica transitoria** entre esta clasificación de 1987 (Ley del
   Suelo estatal antigua) y las tres clases de la Ley 9/2001 de 2001 (urbano/urbanizable/no
   urbanizable de protección) que rige hoy a nivel autonómico. Si la Ley 9/2001 obliga a
   reinterpretar "Suelo No Urbanizable Común" de 1987 como "no urbanizable de protección del
   art. 16.1.b" de 2001, la vía del 43.3 LS podría no ser invocable sin más en 2026.
4. Tampoco he confirmado si esta modificación de 1987 (solo vista con aprobación provisional/
   ratificación municipal) sigue vigente en 2026 o si hubo una aprobación definitiva posterior con
   otra fecha/BOCM — no localizada.

## Cómo aplicar

- **No afirmar en el TFM que la vía del art. 43.3 LS está disponible para V3** sin resolver las
  cuatro reservas de arriba. Presentarlo como pista a investigar, no como conclusión.
- Próximos pasos, en orden: (1) pedir al Ayuntamiento de Colmenar Viejo los planos de zonificación
  1:10.000 y confirmar qué instrumento está vigente en 2026; (2) si se confirma Suelo No
  Urbanizable Común, consultar si existen disposiciones transitorias en la Ley 9/2001 sobre
  adaptación de planeamiento preexistente.
- Informe completo en `Memoria/analisis/normativa-autonomica-y-tecnica.md`.
