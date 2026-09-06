---
title: "Normativa autonómica/local (2.4) y normas técnicas de referencia (2.5) del capítulo Marco normativo"
fecha: 2026-09-06
estado: borrador — con pendientes de verificación marcados explícitamente
alcance: "Cubre únicamente los apartados 2.4 (autonómica/local) y 2.5 (técnica) del capítulo 2. No repite las 15 normas estatales/europeas ya verificadas en Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx."
fuentes_primarias_consultadas:
  - "BOE, texto consolidado, Ley 21/2013, de 9 de diciembre, de evaluación ambiental (leído directamente, Anexos I-III, páginas 66-80 del PDF consolidado)"
  - "BOE, Ley 9/2001, de 17 de julio, del Suelo de la Comunidad de Madrid — vía Bibliografia/Resumenes/ComunidadMadrid_2001.md (ya citable, generado por bibliotecario-pdf)"
  - "web.trescantos.es/tramite/planeamiento — página oficial del Ayuntamiento de Tres Cantos"
  - "Búsquedas web para localizar (no para citar sin verificación posterior): Decreto 86/2025 CM, PGOU Colmenar Viejo, Instrucción autoconsumo CM, normas UNE/IEC/EN"
tags: [normativa, marco-normativo, autonomica, local, tecnica, capitulo-2, comunidad-madrid, tres-cantos, colmenar-viejo, une, iec, en-50600]
---

# Normativa autonómica/local y normas técnicas de referencia — Capítulo 2 "Marco normativo"

> **Nota de método.** Este informe distingue tres niveles de confianza en cada norma:
> **[VERIFICADO]** — texto leído directamente de la fuente oficial (BOE consolidado o resumen ya
> generado por `bibliotecario-pdf` a partir del PDF original); **[LOCALIZADO, NO LEÍDO A FONDO]**
> — se ha identificado la norma y su referencia oficial mediante búsqueda web, pero no se ha leído
> el articulado completo ni se ha descargado el PDF, así que el detalle de aplicación al proyecto
> es preliminar; **[NO VERIFICABLE EN ESTA SESIÓN]** — no se ha podido confirmar con una fuente
> primaria y no debe darse por bueno sin más trabajo. Ninguna cifra o cita de este informe debe
> pasar a LaTeX sin que las de nivel 2 y 3 se conviertan primero en nivel 1 (PDF descargado +
> resumen de `bibliotecario-pdf`).

---

## ACTUALIZACIÓN 06/09/2026 (tarde) — pendiente crítico nº1 resuelto

Encargo del team lead: determinar el término municipal exacto de la subparcela candidata de V3
a partir de las coordenadas del polígono `Layout1` (centroide 40,62235 N/−3,74762 O; bounding box
40,61658–40,62677 N / −3,75346 a −3,74208 O).

**Resultado [VERIFICADO — fuente primaria oficial]:** consulté el centroide y las cuatro esquinas
del rectángulo envolvente contra el servicio público `Consulta_RCCOOR` de la Sede Electrónica del
Catastro (`ovc.catastro.meh.es`, SRS EPSG:4326). **Los cinco puntos devuelven código de municipio
28045 = COLMENAR VIEJO** (no Tres Cantos), con referencias catastrales rústicas de los polígonos
43 y 45 (parajes "Arroyo del Buitre", "El Olivo", "La Vencosilla", "Los Llanillos"). Como
contraste, consulté también la coordenada del CPD (40,59823 N/−3,71721 O) y esa sí devuelve TRES
CANTOS — confirma que el servicio funciona correctamente y que la diferencia es real, no un
artefacto de la consulta.

**Conclusión:** la subparcela de V3 cae íntegramente (o con altísima probabilidad — se
comprobaron 5 puntos repartidos por todo el rectángulo envolvente, no la totalidad del contorno
real del polígono) en **término municipal de Colmenar Viejo**. El hallazgo transversal original de
este informe sobre Tres Cantos (que allí no existe suelo urbanizable no sectorizado) **queda sin
efecto práctico para V3** — importa, en cambio, el régimen de Colmenar Viejo, que sí pude
localizar y leer parcialmente (ver 2.4.3 actualizado más abajo). Sigue aplicando a V1/V2 si se
analiza su clasificación en Tres Cantos (cubierta del CPD y aparcamiento).

**Nuevo hallazgo relevante de la lectura del planeamiento de Colmenar Viejo:** encontré un
mecanismo de autorización (art. 43.3 de la antigua Ley del Suelo estatal, vigente en el
planeamiento local de 1987) para instalaciones de "utilidad pública o interés social" en Suelo No
Urbanizable Común, distinto y potencialmente más abierto que la lista tasada del art. 29.3 de la
Ley 9/2001 actual. Ver el detalle y las reservas importantes en 2.4.3.

---

## Hallazgo transversal que condiciona todo el apartado 2.4 (leer antes de lo demás — contexto histórico, ya no aplica directamente a V3 tras la resolución del término municipal)

**Contradicción detectada entre dos fuentes, tal como pide el protocolo de este agente:** el
resumen ya citable `Bibliografia/Resumenes/ComunidadMadrid_2001.md` identifica el art. 26.1.c) y
el art. 27.1.d) de la Ley 9/2001 (generación de energía para autoconsumo y centros de proceso de
datos, respectivamente) como la vía habilitante más directa para la variante 3 — pero **ambos
artículos aplican solo a "suelo urbanizable no sectorizado"**, una clase de suelo intermedia entre
urbano y no urbanizable de protección.

La página oficial de planeamiento del Ayuntamiento de Tres Cantos (`web.trescantos.es/tramite/planeamiento/`,
consultada el 06/09/2026) declara textualmente: **"con el vigente Plan General aprobado el
07.05.2003 no existe suelo urbanizable no sectorizado"** en el término municipal de Tres Cantos.

**Consecuencia para el TFM:** si la subparcela candidata de la variante 3 cae dentro del término
municipal de Tres Cantos, la vía del art. 26.1.c/27.1.d de la Ley 9/2001 **no está disponible**,
porque esa clase de suelo no existe allí — solo quedarían suelo urbano, suelo urbanizable
sectorizado o suelo no urbanizable de protección. En este último caso, el único camino sería el
art. 29.3 (lista tasada que, como ya documentó el resumen de la Ley 9/2001, **no incluye la
generación fotovoltaica**) o la vía excepcional del art. 29.1 (protección sectorial + legislación
sectorial habilitante, que la propia Ley 9/2001 no llega a nombrar). Esta contradicción **no se
resuelve** sin saber (a) en qué término municipal cae exactamente la subparcela elegida — Tres
Cantos o Colmenar Viejo — y (b) cómo clasifica esa parcela concreta el PGOU/planeamiento vigente
de ese municipio. Es el pendiente más crítico de este informe (ver tabla final).

No he podido verificar aún la clasificación de suelo no urbanizable del PGOU de Tres Cantos de
2003 más allá de la frase citada; y el PGOU de Colmenar Viejo no se ha podido identificar con
certeza (ver apartado 2.4.3).

---

## 2.4 Normativa autonómica y local

### 2.4.1 Comunidad de Madrid — suelo y urbanismo

#### Ley 9/2001, de 17 de julio, del Suelo, de la Comunidad de Madrid [VERIFICADO — ya citable]

- **Referencia oficial:** BOE-A-2001-18984 (publicada en BOE núm. 245, de 12 de octubre de 2001,
  como es preceptivo para las leyes autonómicas; texto consolidado actualizado a 15/06/2026).
- **Enlace permanente:** https://www.boe.es/buscar/act.php?id=BOE-A-2001-18984
- **Vigencia:** vigente, con modificaciones consolidadas.
- **Qué regula:** clasificación del suelo madrileño en urbano / urbanizable (sectorizado y no
  sectorizado) / no urbanizable de protección; régimen de usos y trámites (calificación
  urbanística, proyecto de actuación especial, licencias, declaración responsable) para cada
  clase.
- **Cómo aplica al proyecto:** es la norma que determina si la variante 3 puede instalarse en la
  parcela candidata según su clasificación urbanística real (no la etiqueta catastral de "uso
  agrario"). Ya resumida exhaustivamente en `Bibliografia/Resumenes/ComunidadMadrid_2001.md`
  (arts. 13, 16, 26-29, 29 bis, 147-148), con hallazgo de fricción documentado en la memoria de
  proyecto `project-suelo-agrario-fv-ley9-2001`. **No repetir el resumen aquí**; ver ese archivo
  para el detalle articulado.
- **Fuente citable ya disponible:** `Bibliografia/Fuentes/Normativa/BOE_Ley_9-2001_Suelo_Madrid_consolidado.pdf`
  → `Bibliografia/Resumenes/ComunidadMadrid_2001.md`.

#### Ley 2/2002, de 19 de junio, de Evaluación Ambiental de la Comunidad de Madrid [LOCALIZADO, NO LEÍDO A FONDO]

- **Referencia oficial:** BOE-A-2002-14841.
- **Enlace:** https://www.boe.es/buscar/act.php?id=BOE-A-2002-14841
- **Estado:** **mayoritariamente derogada**. Su Título II fue derogado por la Ley 4/2014, de 22 de
  diciembre, y el grueso del procedimiento de evaluación ambiental autonómico quedó desplazado por
  la Ley 21/2013 estatal (ver 2.4.2). Según las fuentes consultadas, de la Ley 2/2002 **solo
  permanece vigente el Anexo Quinto** (evaluación ambiental de actividades de competencia
  municipal — licencias de actividad ante el Ayuntamiento).
- **Cómo aplica al proyecto:** relevante solo si la tramitación municipal de la variante 3 exige
  licencia de actividad y esta cae dentro del listado del Anexo Quinto; no es la norma que rige la
  evaluación de impacto ambiental de la planta FV en sí (esa es la Ley 21/2013 estatal).
- **Pendiente:** no se ha leído el Anexo Quinto para confirmar si una planta FV de autoconsumo de
  2-2,5 MWp está en su listado de actividades. Verificar antes de citar.

#### Decreto 86/2025, de 29 de octubre, del Consejo de Gobierno [LOCALIZADO, NO LEÍDO A FONDO]

- **Título completo:** "Decreto 86/2025, de 29 de octubre, del Consejo de Gobierno, para la
  simplificación de los procedimientos de autorización, comunicación, verificación e inspección,
  responsabilidades y régimen sancionador en materia de instalaciones de energía eléctrica en alta
  tensión en la Comunidad de Madrid."
- **Publicación:** BOCM núm. 260, de 31 de octubre de 2025.
- **Deroga:** el Decreto 70/2010, que regulaba antes este mismo procedimiento.
- **Vigencia:** vigente y reciente (menos de un año).
- **Cómo aplica al proyecto:** si la conexión de la variante 3 se resuelve en alta tensión (dado
  que la evacuación pasa por Tres Cantos GIS 220, ver memoria `project-capacidad-acceso-tres-cantos`),
  este decreto autonómico es el que fija el procedimiento administrativo de autorización de las
  instalaciones eléctricas de alta tensión asociadas (línea de evacuación, subestación si la
  hubiera) ante la Comunidad de Madrid — distinto del procedimiento de acceso y conexión estatal
  (RD 1183/2020, ya en `NormativaLinks.xlsx`).
- **Pendiente:** descargar el texto del decreto (BOCM 31/10/2025) y confirmar el ámbito exacto de
  aplicación (umbral de tensión, qué tipo de instalaciones incluye) antes de citarlo con detalle.

#### Instrucción de la Dirección General de Industria, Energía y Minas sobre puesta en servicio de instalaciones generadoras de autoconsumo [LOCALIZADO, NO LEÍDO A FONDO]

- **Qué es:** instrucción administrativa (no ley ni decreto) que fija la documentación y el
  procedimiento para poner en servicio instalaciones de generación para autoconsumo en la
  Comunidad de Madrid, y para su inscripción en el Registro de Autoconsumo autonómico.
- **Vigencia localizada:** una versión fue obligatoria desde el 1 de junio de 2019; hay referencia
  a una versión posterior obligatoria desde el 1 de diciembre de 2022. **No he podido confirmar
  cuál es la versión vigente en septiembre de 2026** ni su fecha/número de instrucción exactos —
  las fuentes secundarias consultadas (agremia.com, APIEM) no bastan como fuente primaria.
- **Dónde consultarla de primera mano:** portal de instrucciones y circulares de la Comunidad de
  Madrid, https://www.comunidad.madrid/transparencia/exportar-instrucciones-circulares — y la
  sede electrónica, http://sede.comunidad.madrid/node/212646 (trámite "Autorización instalaciones
  eléctricas").
- **Cómo aplica al proyecto:** es el trámite administrativo autonómico que complementa (no
  sustituye) al RD 244/2019 estatal para poner en marcha cualquiera de las tres variantes de
  autoconsumo, incluida la conexión al registro autonómico de autoconsumo.
- **Pendiente — prioridad alta:** pedir a Mario el PDF de la instrucción vigente (descargable desde
  el enlace de sede electrónica) para que `bibliotecario-pdf` la procese; sin esto, no debe citarse
  ni la fecha ni el contenido exacto del trámite.

### 2.4.2 Evaluación ambiental — corrección de encuadre respecto al encargo

El encargo pedía "normativa de evaluación ambiental autonómica aplicable a una planta de
2-2,5 MWp". La verificación directa muestra que **la norma que realmente gobierna esto no es
autonómica, sino estatal**: la Ley 2/2002 de la Comunidad de Madrid está derogada en la parte que
importaría aquí, y el marco vigente es la **Ley 21/2013, de 9 de diciembre, de evaluación
ambiental** (estatal, de aplicación en toda España salvo Comunidades Autónomas con evaluación
ambiental propia y no derogada, que no es el caso de Madrid para proyectos energéticos).

#### Ley 21/2013, de 9 de diciembre, de evaluación ambiental [VERIFICADO — leído el texto consolidado del BOE]

- **Referencia oficial:** BOE-A-2013-12913. Enlace: https://www.boe.es/buscar/act.php?id=BOE-A-2013-12913
- **Vigencia:** vigente, texto consolidado (incorpora ya las modificaciones del RD 445/2023, que
  actualizó los Anexos I, II y III).
- **Texto literal verificado — umbral aplicable a una planta FV en suelo:**
  - **Anexo I, Grupo 3, letra j)** (evaluación ambiental **ordinaria**, obligatoria): *"Instalaciones
    para la producción de energía eléctrica a partir de la energía solar, que no se ubiquen en
    cubiertas y tejados y que ocupen más de 100 ha de superficie."*
  - **Anexo II, Grupo 4, letra j)** (evaluación ambiental **simplificada**): *"Instalaciones para
    la producción de energía eléctrica a partir de la energía solar no incluidas en el anexo I, ni
    instaladas sobre cubiertas o tejados de edificios, así como, las que ocupen una superficie
    inferior a 5 ha salvo que cumplan los criterios generales 1 o 2."*
  - **Anexo III, Apartado B, criterios generales 1 y 2** (los que activan la evaluación simplificada
    para proyectos por debajo del umbral de 5 ha): **criterio 1** — el proyecto se ubica en Red
    Natura 2000, espacio natural protegido, humedal Ramsar, sitio de Patrimonio Mundial, zona
    OSPAR/ZEPIM, o zona núcleo/tampón de Reserva de la Biosfera de la UNESCO; **criterio 2** — el
    proyecto se solapa con elementos de infraestructura verde formalmente declarados (corredores
    ecológicos, áreas críticas de planes de recuperación de especies amenazadas, hábitats de
    interés comunitario en estado de conservación desfavorable, o áreas de protección de especies
    de pesca/marisqueo).
- **Cómo aplica al proyecto:** con una superficie ocupada estimada de la variante 3 del orden de
  3,5 a 5,1 ha (según el escenario de 95 % o 99 % de autosuficiencia real de la memoria
  `project-localizacion-cpd-parcela-v3`: 5,9 %–8,6 % de las 58,84 ha), la planta **queda por debajo
  del umbral de 5 ha del Anexo II** y, por tanto, **no estaría sometida ni siquiera a evaluación
  ambiental simplificada**, salvo que la subparcela elegida esté en un espacio protegido o solape
  infraestructura verde (criterios generales 1 o 2 del Anexo III). Esto es un hallazgo relevante
  para el TFM: reduce drásticamente la carga administrativa ambiental de la variante 3 frente a lo
  que Mario podría haber asumido por comparación con TFM de referencia de mayor tamaño (p. ej. el
  TFM_M_A, con planta de mayor superficie).
- **Pendiente:** verificar contra el mapa de espacios protegidos de la Comunidad de Madrid
  (Red Natura 2000, ZEC, ZEPA) si la subparcela finalmente elegida en `Datos/Catastro/.../afecciones`
  cae dentro de alguno — solo así se puede descartar con seguridad el criterio general 1. No se
  ha hecho esa comprobación geográfica en esta sesión.

### 2.4.3 Normativa municipal

#### Tres Cantos — Plan General de Ordenación Urbana [LOCALIZADO, PARCIALMENTE VERIFICADO]

- **Instrumento vigente:** Plan General de Ordenación Urbana aprobado el **7 de mayo de 2003**
  (según la propia página oficial de planeamiento del Ayuntamiento). No se ha podido confirmar el
  número/fecha de publicación en BOCM desde esta sesión.
- **Fuente:** https://web.trescantos.es/tramite/planeamiento/ ; texto completo de las normas
  urbanísticas en https://web.trescantos.es/contenido/urbanismo/pgou_normas.pdf (localizado, no
  descargado ni leído en esta sesión).
- **Dato clave verificado:** el propio Ayuntamiento declara que, con este PGOU, **"no existe suelo
  urbanizable no sectorizado"** en el término municipal — ver el hallazgo transversal al inicio de
  este informe.
- **Cómo aplica al proyecto:** condiciona si la vía de los arts. 26.1.c/27.1.d de la Ley 9/2001 está
  disponible para la variante 3 dentro de Tres Cantos (probablemente no, según el dato anterior).
  También rige la clasificación real de la cubierta del CPD y del aparcamiento de las marquesinas
  (variantes 1 y 2), que si están en suelo urbano industrial no tienen esta fricción.
- **Pendiente — prioridad alta:** descargar `pgou_normas.pdf` y (si corresponde) procesarlo con
  `bibliotecario-pdf` para extraer exhaustivamente el régimen de suelo no urbanizable de protección
  del término, y cruzarlo con la subparcela candidata de V3 si cae en Tres Cantos.

#### Colmenar Viejo — instrumento de planeamiento [PARCIALMENTE VERIFICADO — leído directamente el texto del plano/norma, con reservas importantes]

**Término municipal confirmado (06/09/2026):** la subparcela candidata de V3 cae en Colmenar
Viejo, no en Tres Cantos — ver la actualización al inicio de este informe (verificación directa
contra el servicio de coordenadas del Catastro, 5/5 puntos consultados).

- **Documento localizado y leído parcialmente:** *"Modificación del Plan General de Colmenar
  Viejo — Normas Urbanísticas, Volumen 3"*, **Título 5: "Regulación del Suelo No Urbanizable"**.
  PDF alojado, algo inesperadamente, en el servidor del Ayuntamiento de **Tres Cantos**
  (`https://web.trescantos.es/contenido/urbanismo/colmenarviejo_no_urba.pdf`) — explicable porque
  Tres Cantos se segregó del término histórico de Colmenar Viejo en 1991 y conserva documentación
  de referencia del municipio matriz. Es un escaneado de 60 páginas, con sello húmedo de la
  **Comunidad de Madrid, Consejería de Ordenación del Territorio, Medio Ambiente y Vivienda**
  ("DOCUMENTO INFORMADO") en casi todas las páginas, y una diligencia repetida: *"Aprobado
  [provisionalmente] (ratificación) por el Pleno de este Ayuntamiento en sesión celebrada el día
  **13 FEB 1987**. El Secretario."*
- **Reserva importante sobre vigencia — no dar por cerrado:** lo que he leído es una diligencia de
  **aprobación provisional/ratificación municipal** de 1987, con informe favorable de la
  Comunidad de Madrid. **No he encontrado en este documento la aprobación definitiva** (que en el
  régimen urbanístico español suele corresponder a un órgano autonómico para el planeamiento
  general, y se publica en el BOCM) ni su fecha/número de BOCM. Es razonable — pero no está
  verificado — que esta modificación de 1987 sea la que sigue rigiendo el suelo no urbanizable de
  Colmenar Viejo en 2026, dado que (a) el Ayuntamiento solo ha llegado a la fase de "Documento de
  Avance" de un PGOU nuevo en enero de 2025 (es decir, todavía no hay un instrumento que la
  sustituya), y (b) el articulado citado usa numeración de la antigua Ley del Suelo estatal
  (art. 85, 86, 43.3, 94 LS; art. 42, 44 RG — Reglamento de Gestión Urbanística de 1978), coherente
  con un plan de los años 80 nunca sustituido de fondo. **No debe darse por definitiva la fecha de
  1987 sin que el Ayuntamiento o la Comunidad de Madrid lo confirmen expresamente.**
- **Clasificación del suelo no urbanizable en este plan (distinta de las categorías a/b de la
  Ley 9/2001 actual, por ser anterior a ella):**
  - **N. Suelo No Urbanizable Común**: N.1 (orientación ganadera) y N.2 (orientación ganadera
    compatible con explotación agrícola limitada).
  - **P. Suelo No Urbanizable de Protección Especial**, con 15 subáreas: P.1 Reserva Natural
    Integral; P'.1 Alto Valor Ecológico; P.2 Parque Comarcal Agropecuario; P.3 Protección
    Ecológica; P.4 Dehesas; P.5 Interés Paisajístico; P.6 Agrícola de posible regadío; P.7 Interés
    histórico-cultural; P.8 Ríos/cauces/arroyos; P.9 Carreteras; P.10 Instalaciones ferroviarias;
    P.11 Infraestructuras hidráulico-sanitarias; P.12 Infraestructuras eléctricas; P.13 Caminos y
    vías pecuarias; P.14 Instalaciones militares; P.15 Instalaciones especiales en Suelo No
    Urbanizable.
- **Hallazgo relevante — mecanismo distinto del art. 29.3 de la Ley 9/2001, texto literal
  verificado:** el Capítulo 3 ("Régimen Jurídico") del Título 5 dice textualmente: *"No se podrán
  realizar otras construcciones que las destinadas a explotaciones agrícolas [...] Sin embargo,
  podrán autorizarse, siguiendo el procedimiento previsto en el artículo 43.3 LS, edificaciones e
  instalaciones de utilidad pública o interés social [...]. Lo anterior es relativo al suelo no
  urbanizable común. En el suelo no urbanizable de Especial Protección no podrán ser permitidos
  usos ni edificaciones que impliquen transformación de su destino o naturaleza."* Y, más
  específico, el capítulo P.12 "Infraestructuras eléctricas" añade: *"Cuando las instalaciones
  eléctricas discurran por el suelo no urbanizable común se podrán autorizar instalaciones de
  utilidad pública, que no hayan sido explícitamente consideradas en el presente Plan según los
  arts. 85 y 86 LS y siguiendo el procedimiento previsto en art. 43.3 LS [...]. La infraestructura
  de energía eléctrica tiene atribuida esta utilidad pública por aplicación de su legislación
  específica (art. 8º Ley 10/1966)."*
- **Por qué esto es relevante pero no debe darse por bueno todavía:** a diferencia del art. 29.3
  de la Ley 9/2001 actual (lista tasada de usos que **no incluye** generación FV, ver 2.4.1), este
  plan de 1987 tiene, para el Suelo No Urbanizable **Común**, una vía de declaración de "utilidad
  pública o interés social" que no es una lista cerrada. Sin embargo, quedan **tres huecos que
  impiden concluir nada todavía**:
  1. No sé si las subparcelas concretas ("Arroyo del Buitre", "El Olivo", "La Vencosilla", "Los
     Llanillos") están clasificadas como **N (Común)** o como **P (Protección Especial)** — eso
     solo lo dicen los planos de zonificación a escala 1:10.000, que no forman parte de este
     volumen de texto y no se han localizado ni consultado en esta sesión. Si son P, esta vía se
     cierra por completo (mismo régimen restrictivo que el 29.3 de la Ley 9/2001, sin excepción).
  2. El capítulo P.12 concreto habla de "instalaciones eléctricas" en el sentido de tendidos/
     infraestructura de transporte-distribución (coherente con el resto de la serie P.9-P.11,
     todas sobre infraestructuras lineales existentes), no necesariamente de una planta de
     generación fotovoltaica — la cita general del Capítulo 3 (cualquier "utilidad pública o
     interés social") es la que realmente abriría la puerta a una planta FV, y esa calificación
     requeriría de todos modos una declaración expresa caso por caso, no es automática.
  3. **No he verificado cómo se relaciona jurídicamente esta clasificación de 1987 (bajo la
     antigua Ley del Suelo estatal) con la clasificación de tres clases de la Ley 9/2001 de 2001
     (urbano/urbanizable/no urbanizable de protección) que rige hoy a nivel autonómico.** Es una
     cuestión de derecho transitorio que no he resuelto: si la Ley 9/2001 obliga a reinterpretar
     "Suelo No Urbanizable Común" de un plan de 1987 como "no urbanizable de protección del
     art. 16.1.b" (el caso restrictivo sin FV, según ya se documentó en
     `ComunidadMadrid_2001.md`), la vía del art. 43.3 LS podría no ser invocable sin más en 2026.
     **No dar por buena la vía del 43.3 LS/utilidad pública sin que esto se aclare.**
- **Pendiente — prioridad crítica (reformulada):**
  1. Localizar los planos de zonificación 1:10.000 de este mismo plan (o del PGOU vigente si hay
     uno más reciente que sustituya a esta modificación de 1987) para saber si las subparcelas
     candidatas son N o P.
  2. Confirmar con el Ayuntamiento de Colmenar Viejo o la Comunidad de Madrid si esta modificación
     de 1987 sigue siendo el instrumento vigente en 2026, o si hay una aprobación definitiva
     posterior que la sustituye — el propio Ayuntamiento sería la fuente más fiable.
  3. Aclarar la relación entre la clasificación N/P de 1987 y las tres clases de la Ley 9/2001 de
     2001 (consultar, si existen, las disposiciones transitorias de la Ley 9/2001 sobre
     adaptación de planeamiento preexistente — no revisadas en esta sesión).

### Tabla resumen 2.4 (para volcar a `NormativaLinks.xlsx`)

| Título | Fecha/Ref. oficial | Nivel | Vigente | Enlace | Qué regula | Aplica a | Confianza |
|---|---|---|---|---|---|---|---|
| Ley 9/2001, de 17 de julio, del Suelo de la Comunidad de Madrid | BOE-A-2001-18984, consolidado 15/06/2026 | Autonómica | Sí | boe.es/buscar/act.php?id=BOE-A-2001-18984 | Clasificación de suelo y régimen de usos/trámites | V3 (clasificación urbanística de la parcela) | Verificado, ya citable |
| Ley 2/2002, de 19 de junio, de Evaluación Ambiental de la CM | BOE-A-2002-14841 | Autonómica | Parcialmente (solo Anexo Quinto) | boe.es/buscar/act.php?id=BOE-A-2002-14841 | Evaluación ambiental de actividades municipales | Posible licencia de actividad municipal de V3 | Localizado, no leído a fondo |
| Ley 21/2013, de 9 de diciembre, de evaluación ambiental | BOE-A-2013-12913, consolidado (incorpora RD 445/2023) | Estatal (sustituye de facto a la autonómica en este punto) | Sí | boe.es/buscar/act.php?id=BOE-A-2013-12913 | Umbrales de EIA ordinaria/simplificada para plantas FV en suelo | V3: por debajo del umbral de 5 ha (Anexo II), salvo espacio protegido | Verificado, texto leído directamente |
| Decreto 86/2025, de 29 de octubre, del Consejo de Gobierno (CM) | BOCM núm. 260, 31/10/2025 | Autonómica | Sí | (pendiente enlace BOCM oficial) | Procedimientos de autorización de instalaciones de alta tensión | Evacuación de V3 si requiere AT | Localizado, no leído a fondo |
| Instrucción DG Industria, Energía y Minas (CM) sobre autoconsumo | Sin fecha/número confirmado (¿vigente desde 01/12/2022?) | Autonómica (instrucción administrativa) | Probable, sin confirmar versión | sede.comunidad.madrid/node/212646 | Documentación y trámite de puesta en servicio de autoconsumo | Las tres variantes | Localizado, no verificado |
| PGOU de Tres Cantos | Aprobado 07/05/2003 | Municipal | Sí | web.trescantos.es/contenido/urbanismo/pgou_normas.pdf | Clasificación de suelo del término; NO existe suelo urbanizable no sectorizado | V1, V2 (CPD y aparcamiento están en Tres Cantos, confirmado por Catastro) | Parcialmente verificado |
| Modificación del Plan General de Colmenar Viejo — Título 5, Suelo No Urbanizable | Diligencia de aprobación provisional/ratificación por el Pleno: 13/02/1987; informado favorablemente por la CM. Aprobación definitiva y BOCM NO localizados | Municipal | Probable (sin confirmar formalmente), no hay PGOU nuevo aprobado (solo Avance, ene. 2025) | web.trescantos.es/contenido/urbanismo/colmenarviejo_no_urba.pdf | Clasifica el suelo no urbanizable en N (Común) y P (Protección Especial, 15 subáreas); en Común admite "utilidad pública o interés social" vía art. 43.3 LS | V3 — confirmado que la subparcela cae en este término (Catastro, 5/5 puntos) | Parcialmente verificado, con reservas críticas explícitas |

---

## 2.5 Normas técnicas de referencia

### 2.5.1 Baja tensión

#### Reglamento Electrotécnico para Baja Tensión (REBT) — RD 842/2002, de 2 de agosto [ya en NormativaLinks.xlsx, no repetir aquí salvo la ITC específica]

- **ITC-BT-40 — Instalaciones generadoras de baja tensión** [LOCALIZADO, NO LEÍDO A FONDO]: es la
  instrucción técnica del REBT que regula específicamente las instalaciones generadoras conectadas
  en baja tensión, incluido el autoconsumo fotovoltaico — requisitos de protección (diferencial
  tipo A si aplica, protección anti-isla), circuito independiente y dedicado desde cuadro de
  protección, límites de potencia. Guía técnica oficial de desarrollo (no vinculante pero de
  referencia): "Guía-BT-40", Ministerio de Industria — `industria.gob.es`.
  **Aplica a:** V1 y V2 (conexión en baja tensión de la cubierta del CPD y las marquesinas del
  aparcamiento). **Pendiente:** descargar el texto de la ITC-BT-40 y la Guía-BT-40 vigentes para
  contrastar cifras de diseño eléctrico (sección de conductores, protecciones) del cap. 6.

### 2.5.2 Alta/media tensión (si la V3 lo exige)

#### Real Decreto 337/2014, de 9 de mayo — Reglamento sobre condiciones técnicas y garantías de seguridad en instalaciones eléctricas de alta tensión (RAT) e ITC-RAT 01 a 23 [LOCALIZADO, NO LEÍDO A FONDO]

- **Referencia:** BOE-A-2014-6084. Deroga el RD 3275/1982.
- **Qué exige:** condiciones técnicas y de seguridad de las instalaciones de alta tensión (líneas,
  subestaciones, centros de transformación) — las ITC-RAT cubren desde terminología y normas
  técnicas hasta aparamenta de maniobra y transformadores de potencia.
- **Cómo aplica al proyecto:** si la evacuación de la variante 3 hacia Tres Cantos GIS 220 requiere
  instalaciones propias de alta tensión (línea de evacuación, posición en el GIS), este reglamento
  —y no solo el REBT— es el marco técnico aplicable. Pendiente de confirmar con el diseño eléctrico
  final del cap. 6/7 si la interconexión queda en MT o AT.
- **Pendiente:** identificar qué ITC-RAT concretas aplican (probablemente ITC-RAT-04 líneas
  subterráneas/aéreas y ITC-RAT-14 instalaciones de exterior, sin verificar aún el número exacto)
  una vez se sepa el nivel de tensión real de interconexión.

### 2.5.3 Código Técnico de la Edificación — estructuras

#### CTE, Documento Básico SE-AE (Seguridad Estructural — Acciones en la Edificación) [LOCALIZADO, NO LEÍDO A FONDO]

- **Qué exige:** las acciones de viento (mapa de zonas eólicas, coeficientes de presión/succión)
  que dimensionan la estructura soporte de los módulos y su sistema de lastre o anclaje, tanto en
  cubierta (V1) como en marquesina de aparcamiento (V2). No existe en el DB-SE-AE una
  configuración normalizada idéntica a una instalación FV inclinada sobre cubierta plana; la
  práctica habitual (no normativa cerrada) es asimilarla a una marquesina a un agua y aplicar la
  hipótesis de succión/presión más desfavorable.
- **Cómo aplica al proyecto:** dimensionado estructural de las marquesinas de V2 (estructura nueva,
  CTE aplica en su totalidad) y verificación de la capacidad portante de la cubierta existente del
  CPD para V1 (aquí el CTE aplica como referencia de cálculo de la sobrecarga adicional, no como
  proyecto de obra nueva).
- **Pendiente:** no se ha descargado el DB-SE-AE vigente (revisión de junio de 2022 según
  conocimiento general, **sin verificar en esta sesión**) ni se ha identificado la zona eólica
  exacta de Tres Cantos en el mapa del Anejo D. Necesario para el cap. 6 (dimensionado mecánico),
  no solo para el marco normativo.

### 2.5.4 Normas UNE-EN/IEC de equipos fotovoltaicos

Todas las normas de este bloque se han localizado por título mediante búsqueda web (catálogo
público de AENOR/UNE); **no se ha verificado el número de edición/año vigente exacto de cada una**
consultando directamente la ficha de AENOR, así que el año entre paréntesis es orientativo.

| Norma | Título | Qué exige | Uso en el TFM |
|---|---|---|---|
| UNE-EN IEC 61215 (serie -1, -1-1, -2) | Módulos fotovoltaicos (FV) para uso terrestre — Cualificación del diseño y homologación | Ensayos de cualificación de diseño de los módulos (térmicos, mecánicos, eléctricos) | Justificar la elección del módulo FV en cap. 6, criterio de selección de datasheet |
| UNE-EN IEC 61730 (serie -1, -2) | Cualificación de la seguridad de módulos fotovoltaicos (FV) | Seguridad frente a descarga eléctrica, incendio y riesgos mecánicos/estructurales | Idem, junto con 61215 |
| UNE-EN 62109-1 / -2 | Seguridad de los convertidores de potencia utilizados en sistemas de potencia fotovoltaicos — Parte 1: Requisitos generales / Parte 2: Requisitos particulares para inversores | Requisitos de seguridad eléctrica de inversores (protección frente a choque eléctrico, cortocircuito, sobrecarga) | Selección de inversores en cap. 6 |
| UNE-EN 50549-1 / -2 / -10 | Requisitos para centrales eléctricas destinadas a ser conectadas en paralelo con redes de distribución — Parte 1: BT (hasta tipo B) / Parte 2: MT / Parte 10: Ensayos de conformidad | Requisitos de protecciones y capacidades operativas para conexión en paralelo a la red de distribución | Conexión a red de V1/V2 (BT, Parte 1) y de V3 si es MT (Parte 2) |

**Pendiente de prioridad media:** confirmar en la ficha oficial de AENOR (tienda.aenor.com o
une.org) el año de edición vigente exacto de cada norma antes de citarla con fecha en el TFM;
en esta sesión solo se ha verificado el título y la estructura por partes, no la ficha completa.

### 2.5.5 Normas de almacenamiento electroquímico

#### UNE-EN IEC 62619 [LOCALIZADO, NO LEÍDO A FONDO]

- **Título:** "Pilas y baterías secundarias que contienen electrolitos alcalinos u otros no
  ácidos — Requisitos de seguridad para pilas y baterías de litio secundarias, para uso en
  aplicaciones industriales."
- **Qué exige:** requisitos de seguridad y ensayos para celdas/baterías de litio en aplicaciones
  industriales estacionarias (incluye expresamente sistemas de almacenamiento de energía) y
  móviles.
- **Cómo aplica al proyecto:** norma de referencia para la especificación de seguridad del BESS de
  4-6 MWh de cualquiera de las variantes (cap. 7).
- **Pendiente:** localizar también, si existe y es distinta, una norma de nivel de sistema completo
  (más allá de la celda/batería) — candidata razonable: serie **IEC 62933** (sistemas de
  almacenamiento de energía eléctrica) — **no verificada en esta sesión**, solo mencionada como
  candidata a investigar, no debe citarse sin confirmar número de parte y título exactos.
- También pendiente: **UNE-EN 50272-2** (instalación y funcionamiento de baterías estacionarias) —
  localizada por nombre en conocimiento general, **sin verificar en esta sesión mediante fuente
  primaria**; no citar sin confirmación.

### 2.5.6 Infraestructura de centro de datos — series EN 50600 (relevantes por el PUE)

[LOCALIZADO, NO LEÍDO A FONDO — títulos verificados por coincidencia de varias fuentes secundarias
independientes, pero no se ha leído el texto normativo]

- **EN 50600 (serie general):** "Tecnología de la información — Instalaciones e infraestructuras de
  centros de datos." Primera norma transnacional europea con especificaciones completas de
  planificación, construcción y operación de un CPD.
- **EN 50600-1:** requisitos generales.
- **EN 50600-2-1 a 2-5:** subsistemas — construcción del edificio (2-1), distribución de energía
  (2-2), control ambiental (2-3), sistemas de cableado (2-4), sistemas de seguridad (2-5).
- **EN 50600-3-1:** gestión y operación.
- **EN 50600-4-x (serie de indicadores/KPI):** incluye **EN 50600-4-2, "Power Usage
  Effectiveness"** — define el PUE como indicador clave, su fórmula (energía total del CPD /
  energía consumida por el equipo de TI), las categorías de medición (PUE1, PUE2...) y el método
  de cálculo y reporte.
- **Cómo aplica al proyecto:** el PUE es una magnitud citada en varios puntos del índice (cap. 1.2
  y 3.2, según `project-estructura-indice-erma`) y es también el criterio numérico central del
  proyecto de RD de CPD en tramitación (PUE ≤ 1,15, memoria `project-marco-regulatorio-2026`). La
  EN 50600-4-2 es la norma técnica que formaliza qué significa "PUE" y cómo se mide — es la
  referencia adecuada para citar la definición del indicador en el cap. 1.2/3.2, distinta de la
  norma/proyecto regulatorio que le pone un umbral obligatorio.
- **Pendiente de prioridad media-alta:** ninguna de las partes de la serie EN 50600 se ha leído en
  esta sesión; antes de citar la definición exacta de PUE con número de norma en LaTeX, descargar
  al menos la EN 50600-4-2 y procesarla con `bibliotecario-pdf`.

### Tabla resumen 2.5 (para volcar a `NormativaLinks.xlsx`)

| Código | Título | Qué exige | Apartado del TFM que la usa | Confianza |
|---|---|---|---|---|
| ITC-BT-40 (REBT, RD 842/2002) | Instalaciones generadoras de baja tensión | Protecciones y conexión de generación en BT (autoconsumo) | Cap. 6 (V1/V2, diseño eléctrico BT) | Localizado, no leído a fondo |
| RD 337/2014 + ITC-RAT 01-23 | Reglamento sobre condiciones técnicas y garantías de seguridad en instalaciones eléctricas de alta tensión | Seguridad técnica de instalaciones de AT | Cap. 6/7 (V3, evacuación si es AT) | Localizado, no leído a fondo |
| CTE DB-SE-AE | Seguridad estructural — Acciones en la edificación | Cargas de viento sobre estructura soporte FV | Cap. 6 (dimensionado mecánico V1/V2) | Localizado, no leído a fondo |
| UNE-EN IEC 61215 (-1, -1-1, -2) | Módulos FV para uso terrestre — cualificación del diseño | Ensayos de cualificación de módulos | Cap. 6 (selección de módulo) | Localizado, no leído a fondo |
| UNE-EN IEC 61730 (-1, -2) | Cualificación de la seguridad de módulos FV | Seguridad eléctrica/mecánica de módulos | Cap. 6 (selección de módulo) | Localizado, no leído a fondo |
| UNE-EN 62109-1/-2 | Seguridad de convertidores de potencia en sistemas FV | Seguridad de inversores | Cap. 6 (selección de inversor) | Localizado, no leído a fondo |
| UNE-EN 50549-1/-2/-10 | Requisitos para centrales conectadas en paralelo a redes de distribución (BT/MT/ensayos) | Protecciones y capacidades para conexión a red | Cap. 6/7 (conexión a red de las 3 variantes) | Localizado, no leído a fondo |
| UNE-EN IEC 62619 | Seguridad de pilas y baterías de litio secundarias en aplicaciones industriales | Seguridad de celdas/baterías del BESS | Cap. 7 (especificación de seguridad del BESS) | Localizado, no leído a fondo |
| EN 50600-4-2 | Data centre facilities and infrastructures — Power Usage Effectiveness | Definición, categorías y cálculo del PUE | Cap. 1.2 / 3.2 (definición de PUE) | Localizado, no leído a fondo |
| EN 50600 (serie 1, 2-x, 3-1) | Infraestructura de centros de datos | Requisitos generales de diseño/operación del CPD | Contexto de cap. 1/3 (mención, no núcleo del TFM) | Localizado, no leído a fondo |

---

## Pendientes de verificación, por orden de criticidad

1. **[RESUELTO 06/09/2026]** Término municipal exacto de la subparcela V3: **Colmenar Viejo**,
   confirmado con el servicio de coordenadas del Catastro (5/5 puntos, centroide + 4 esquinas del
   rectángulo envolvente). Ya no es un pendiente abierto.
2. **[CRÍTICO] Clasificación exacta (N-Común o P-Protección Especial) de las subparcelas
   candidatas dentro del planeamiento de Colmenar Viejo** — solo la dan los planos de zonificación
   a escala 1:10.000 del propio plan, no localizados en esta sesión (el documento leído es solo el
   texto normativo). Sin esto no se puede saber si la vía del art. 43.3 LS (utilidad pública/
   interés social) está disponible para la subparcela real o si aplica el régimen restrictivo de
   Protección Especial.
3. **[CRÍTICO] Confirmar vigencia real en 2026 de la Modificación del Plan General de Colmenar
   Viejo de 1987** — solo se ha visto una diligencia de aprobación provisional/ratificación
   municipal (13/02/1987) e informe favorable de la CM; no se ha localizado la aprobación
   definitiva ni su publicación en BOCM. Acción: preguntar directamente al Ayuntamiento de
   Colmenar Viejo (Concejalía de Urbanismo) cuál es el instrumento vigente citable, ya que el
   visor web no permite descarga directa por nombre de municipio.
4. **[ALTO] Relación jurídica entre la clasificación N/P de este plan de 1987 (antigua Ley del
   Suelo estatal) y las tres clases de la Ley 9/2001 de 2001 (urbano/urbanizable/no urbanizable de
   protección) que rige hoy a nivel autonómico** — no revisado; sin esto, no está claro si la vía
   del art. 43.3 LS de 1987 sigue siendo invocable en 2026 o si ha quedado subsumida en el régimen
   más restrictivo del art. 29 de la Ley 9/2001.
5. **[ALTO] Normas urbanísticas completas de Tres Cantos** (`pgou_normas.pdf`) — descargar y pasar
   por `bibliotecario-pdf`; relevante ahora sobre todo para V1/V2 (CPD y aparcamiento, confirmados
   en término de Tres Cantos por Catastro), no ya para V3.
6. **[ALTO] Comprobación geográfica de espacios protegidos** (Red Natura 2000, ZEC/ZEPA) sobre la
   subparcela V3 elegida, para descartar el criterio general 1 del Anexo III de la Ley 21/2013 y
   confirmar que la evaluación ambiental simplificada no aplica.
7. **[ALTO] Instrucción vigente de la Comunidad de Madrid sobre puesta en servicio de autoconsumo**
   — confirmar versión y fecha exactas (indicios de 01/06/2019 y 01/12/2022, ninguna confirmada
   como la vigente en 2026) antes de citarla.
8. **[MEDIO] Decreto 86/2025 (alta tensión CM)** — leer el texto completo (BOCM 31/10/2025) para
   confirmar el ámbito de aplicación exacto y si cubre la instalación de evacuación de V3.
9. **[MEDIO] EN 50600-4-2 y resto de la serie EN 50600** — descargar y procesar con
   `bibliotecario-pdf` antes de citar la definición formal de PUE con número de norma.
10. **[MEDIO] Ediciones/años vigentes exactos de las normas UNE-EN/IEC** del apartado 2.5.4 y 2.5.5
    — verificar ficha oficial en AENOR/UNE antes de citar con año.
11. **[BAJO] Ley 2/2002 CM, Anexo Quinto** — confirmar si una planta FV de autoconsumo de
    2-2,5 MWp figura en su listado de actividades sujetas a licencia municipal.
12. **[BAJO] ITC-RAT concretas aplicables a la V3** — depende de que el diseño eléctrico del cap. 6/7
    fije el nivel de tensión de interconexión real.

## PDFs a priorizar para descarga y procesamiento por `bibliotecario-pdf`

En este orden:

1. **Planos de zonificación (escala 1:10.000) del Plan General de Colmenar Viejo** — es el
   documento que falta para saber si la subparcela de V3 es Suelo No Urbanizable Común o de
   Protección Especial. No localizados en esta sesión; probablemente solo disponibles pidiéndolos
   al Ayuntamiento de Colmenar Viejo (Concejalía de Urbanismo, Plaza del Pueblo 1, tel.
   91 845 00 53) o en su visor de "Documentos Vigentes de Planeamiento".
2. **Confirmación municipal de qué instrumento está vigente en 2026** para Colmenar Viejo (¿sigue
   siendo la Modificación de 1987, Título 5? ¿hay una aprobación definitiva posterior con otra
   fecha/BOCM?) — pedir directamente al Ayuntamiento, es más fiable que seguir buscando en la web.
3. El texto normativo ya localizado y parcialmente leído de Colmenar Viejo (`Modificación del
   Plan General — Normas Urbanísticas Volumen 3, Título 5`) está descargado en esta sesión desde
   `https://web.trescantos.es/contenido/urbanismo/colmenarviejo_no_urba.pdf` (60 páginas,
   escaneado). **Recomendación:** que `bibliotecario-pdf` lo procese igual que la Ley 9/2001, para
   dejarlo citable con exhaustividad en los capítulos 1-16 (especialmente el Capítulo 3 de
   régimen jurídico y el P.12 de infraestructuras eléctricas, ya identificados como relevantes).
4. Normas urbanísticas completas de Tres Cantos (`pgou_normas.pdf`, ya localizado el enlace) —
   ahora relevante sobre todo para V1/V2, no para V3.
5. Instrucción vigente de autoconsumo de la Comunidad de Madrid (sede electrónica).
6. Ley 21/2013 de evaluación ambiental — **ya verificado el fragmento relevante en esta sesión
   directamente del BOE**; si se quiere una versión citable completa con resumen estructurado,
   descargar el PDF consolidado y procesarlo igual que se hizo con la Ley 9/2001.
7. Decreto 86/2025 (alta tensión CM), BOCM 31/10/2025.
8. EN 50600-4-2 (si Mario tiene acceso a AENOR/CENELEC; es de pago, a diferencia del resto).
