---
title: "Selección del módulo fotovoltaico — comparativa 3 + 3 (V1a semitransparente; V1b/V2/V3 opaco)"
tipo: analisis-tecnico
autor: ingeniero-dominio
fecha: 2026-09-22
estado: propuesta (pendiente de validación por Mario)
fase_erma: "Fase 3 — Selección del módulo"
encargo: "Prompts/Prompt_ComparacionModulos.md"
tags: [modulo-fv, seleccion, BIPV, lucernario, V1a, V1b, V2, V3, PVsyst, ranking]
---

# Selección del módulo fotovoltaico

> **SUPERADO el 27/09/2026 por `Memoria/analisis/seleccion-modulos-por-variante.md`.** La
> elección pasa a ser independiente por variante (V1a, V1b, V2, V3), cada una con sus criterios. La
> categoría A (V1a) se confirma sin cambios; la categoría B deja de tener módulo único. Este
> documento se conserva porque contiene las fichas, rankings y fuentes que el nuevo reutiliza.

> **Regla aplicada.** Toda cifra de ficha técnica lleva su fuente (URL o ruta local, al final
> en §7). Lo que no se ha podido verificar figura como **no verificado**. Ningún hueco se ha
> rellenado con memoria del modelo. Las puntuaciones son cálculo propio con el método de
> Arcas (§1.1) y se pueden rehacer si Mario cambia los criterios o sus pesos.

## 0. Resultado en una línea

| Categoría | Módulo elegido | Alternativa de reserva |
| --- | --- | --- |
| **A — V1a** (lucernario horizontal, BIPV) | **Onyx Solar, vidrio FV de silicio cristalino, grado de transparencia 35 %** (ref. 044A0-16500850-35-M, 182 Wp, 1650 × 850 mm) | Polysolar PS-MC-ST-60, **solo si** se acepta una transparencia del 10 % o Polysolar confirma por escrito una versión al 20-35 % |
| **B — V1b, V2, V3** (opaco, módulo único) | **AIKO Neostar 2P 475 W** (AIKO-A475-MAH54Mw, N-type ABC, 23,8 %) | LONGi Hi-MO X6 Max Explorer LR7-54HTH-465M (si pesa más la bancabilidad en V3 o el PAN de AIKO no está en PVsyst) |

El REC Alpha Pure-RX 470 del trabajo previo **no sale confirmado** (§4.4). Es una desviación
respecto a lo que corrigió el tutor en el Módulo 6 y hay que decirlo en la memoria con su motivo.

---

## 1. Criterios de comparación y de dónde salen

### 1.1 Capítulo 4.3 del TFM de Manuel Arcas (`TFM_M_A.pdf`, pp. 16-17 impresas)

Método literal del 4.3: *«se llevará a cabo la elección de los principales componentes del
sistema, otorgando un valor numérico a las categorías que se han estudiado […] si por ejemplo
se estudian 4 fabricantes de paneles, se dará un valor del 1 al 4 a cada uno»*. Arcas compara
4 módulos **de la misma potencia (605 W) y de fabricantes bien posicionados**, y justifica las
categorías así: *«precio, eficiencia, dimensiones (importantes para el manejo) y coeficiente de
temperatura (importante por instalarse en un clima cálido)»*. La decisión sale de un **gráfico
radar** con esos cuatro ejes (Ilustración 23).

Filas de su tabla (Ilustración 22): potencia pico STC · tecnología de célula · peso · dimensiones ·
año de fabricación · coeficiente de temperatura de la potencia · eficiencia · garantía de
potencia · garantía de producto · protección contra salinidad/amoniaco · características
estructurales · posición del fabricante, precio (€/Wp).

### 1.2 Diapositivas 15-17 de la guía ERMA (`GUIA_PLANTILLA Estudio Autoconsumo FV ERMA20.pptx`)

- **Diap. 15** — «Posición del fabricante o/y del módulo en estudios existentes», con 7 URL de
  ranking (§2).
- **Diap. 16** — «Justificar el módulo seleccionado», tabla Módulo 1/2/3 con: potencia pico STC ·
  tecnología de célula (PERC, HJT, TOPCon…) · coeficiente de temperatura de la potencia · **LID** ·
  **PID** · garantía de potencia · garantía de producto · características especiales (bifacial,
  glass-glass, tedlar transparente…) · posición del fabricante en ranking · precio (€/Wp).
- **Diap. 17** — imagen del módulo, curvas características, y «destacar las características más
  significativas del módulo seleccionado». → Pendiente de maquetar en LaTeX con las figuras de
  las fichas (§6).

### 1.3 Criterios propios añadidos (y por qué)

| Criterio | Categoría | Motivo |
| --- | --- | --- |
| Tensión máxima del sistema y Voc, Vmp, Isc, Imp, β_Voc | B | El inversor se elige **después**: son los datos que lo condicionan (ventana MPP, n.º en serie, corriente por MPPT) |
| Carga mecánica de ensayo (Pa) | B | Viento en marquesinas (V2) y en sheds de cubierta (V1b); la comprobación CTE es de la fase 6 |
| Disponibilidad del PAN en PVsyst o datos suficientes para crearlo | A y B | Sin PAN no hay simulación (bloqueante formal que ya tuvo V1a) |
| Transparencia / VLT (requisito de paso) | A | La justificación de V1a es arquitectónica: iluminación natural del hall y control solar |
| Wp/m², peso (kg/m²), U y factor solar g, seguridad del laminado | A | Encaje en la perfilería existente del lucernario y argumento térmico |
| Uc sin ventilación posterior | A | V1a trabaja más caliente que un módulo libre (§3.4) |

---

## 2. Rankings consultados (diap. 15) y cómo salen los candidatos

| URL de la diap. 15 | Estado de la consulta (22/09/2026) | Qué aporta |
| --- | --- | --- |
| cleanenergyreviews.info — *Best solar panels* | OK, ed. 2025 (act. 10/07) | 1.º **REC Alpha Pure-RX** (22,6 %, HJT); 3.º **AIKO Neostar 2P** (23,8 %, ABC); 5.º Trina Vertex S+; 6.º **LONGi Hi-MO 6**; 7.º Jinko Tiger Neo |
| energysage.com (redirige desde news.energysage.com) | OK, act. 01/07/2026 | 1.º **REC Alpha Pure-RX 460 W** (−0,24 %/°C); 2.º Hyundai; 3.º Qcells; 6.º Maxeon 6 |
| taiyangnews.info — *Top modules June 2024* | OK | Por eficiencia: 1.º **AIKO** Comet 2U (24,2 %, ABC); 2.º Maxeon 7; 3.º **LONGi Hi-MO 6** (23,2 %, HPBC) |
| blackridgeresearch.com | OK (act. 06/02/2026) | Por envíos Q1 2025: 1.º Jinko; **2.º LONGi**; 3.º JA; 4.º Trina |
| solarfeeds.com (PV-Tech bankability) | **Caído** (DNS no resuelve) | Sustituido por la fuente primaria, pv-tech.org: **LONGi, Trina y JA en AAA** (Q4 2025) |
| solaranalytica.com — *Tier 1* | **HTTP 404** | — |
| semprius.com | **Redirige** a otra web ajena (todayshomeowner.com); no se ha usado | — |

**Criterio para escoger los tres opacos:** que el **mismo formato** (54 células de media celda,
~2 m², ~21-23 kg, manejable a mano en cubierta) aparezca en al menos dos rankings, que haya ficha
técnica descargable, y que entre los tres haya una tecnología distinta cada uno (HJT, ABC, HPBC)
para que la comparación diga algo. Siguiendo a Arcas, se comparan en la **misma clase de
potencia** (465-475 W). Quedan:

1. **REC Alpha Pure-RX 470** — 1.º en dos rankings, y es el módulo del trabajo previo (referencia).
2. **AIKO Neostar 2P 475** — 3.º en CleanEnergyReviews; AIKO, 1.º en eficiencia en TaiyangNews.
3. **LONGi Hi-MO X6 Max Explorer 465** — LONGi aparece en cuatro de las fuentes (6.º CER, 3.º
   TaiyangNews, 2.º en envíos, AAA en bancabilidad). Además, **su ficha está en el material del
   propio Módulo 6** (`Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/…/Fichas tecnicas Longi/`).

Descartados de entrada: Maxeon (formato y precio de gama residencial premium, ficha no
consultada), Jinko/Trina/JA en formato grande de 2,3-2,8 m² (no comparables en la misma clase y
peor manejo en cubierta de chapa; Arcas ya usó Trina 605 W).

**Categoría A (semitransparentes):** ningún ranking de la diap. 15 los recoge, como anticipaba
el encargo. Se parte del trabajo previo verificado del 02/09/2026 (`Memoria/analisis/bipv-tragaluz-fichas-tecnicas.md`,
rama `worktree-bipv-tragaluz-fichas`), que documentó Onyx Solar (cristalino y capa fina) y AGC
SunEwat Vision. Para tener **tres fabricantes de silicio cristalino** comparables entre sí se
sustituye la capa fina de Onyx por **Polysolar PS-MC-ST** (ficha localizada hoy). La capa fina
queda descartada por aritmética (§3.3).

---

## 3. Categoría A — V1a, lucernario horizontal (BIPV)

### 3.1 Tabla comparativa

| Característica | **Onyx Solar c-Si** (35 %) | **Polysolar PS-MC-ST-60** | **AGC SunEwat Vision** |
| --- | --- | --- | --- |
| Fabricante / fabricación | Onyx Solar Energy — Ávila (España) | Polysolar Ltd. — Reino Unido; «Manufactured in Europe» | AGC Glass (Japón / AGC Glass Europe, Bélgica) |
| Referencia | 044A0-16500850-35-M | PS-MC-ST-60 | SunEwat Vision (sin referencia) |
| Potencia pico STC (Wp) | 182 | 370 | no publicada por módulo |
| Tecnología de célula | Mono c-Si 6″ (158), células espaciadas | Mono c-Si **bifacial** 166 × 166 mm | Mono PERC |
| Dimensiones (mm) | 1650 × 850 (1,40 m²) | 1049 × 1770 × 7,1 (1,857 m²) | no publicadas |
| **Grado de transparencia / VLT** | **35 %** (gama publicada: 11 / 35 / 43 %) | **10 %** (única publicada; «variable transparencies» sin cifra) | no publicada |
| **Densidad (Wp/m²)** | **129,6** | **199,3** *(calc. 370 / 1,857)* | «máx. 180» |
| Composición | 4 templado extraclaro + 1,80 mm EVA + 4 templado (9,8 mm) | 3 mm templado + 3 mm templado, sin marco; intercalario **no publicado** | termotratado + intercalario + termotratado; espesores e intercalario **no publicados** |
| Peso (kg/m²) | ~20 *(calc. 28 kg / 1,40 m²)* | **16,2** *(calc. 30 kg / 1,857 m²)* | no publicado |
| U (W/m²·K) | 5,2 monolítico; 1,0-3,2 en UGU | no publicada | no publicada |
| Factor solar g | **no verificado** (Onyx no lo publica para c-Si) | no publicado | no publicado |
| Coef. temp. Pmpp / Voc / Isc (%/°C) | −0,32 / −0,28 / +0,07 | −0,362 / −0,265 / +0,036 | no publicados |
| Voc / Isc / Vmp / Imp | 24 V / 9,66 A / 19 V / 9,35 A | 40,50 V / 11,18 A / 34,86 V / 10,62 A | no publicados |
| Tensión máx. sistema | 1000 V | 1000 V / 20 A | no publicada |
| LID / PID | no declarados | no declarados («stabilized performance») | no declarados |
| Garantía de producto | **5 años** | **30 años** | 10 años (delaminación); condensación UGU 10 años **solo vertical** |
| Garantía de potencia | 80 % a 10 años | 87 % (horizonte no legible en la ficha) | 90 % años 1-10; 80 % años 11-20 |
| Seguridad / homologación de vidrio | Lista de normas «según configuración» (ISO 12543-4, EN 12150, EN 12600…) | **DIBt Z-70.3-288** (homologación alemana de construcción; alcance **no verificado**), IEC 61215/61730, clase A fuego | IEC 61215, IEC 61730, EN 13501 |
| Referencia en lucernario | Onyx sí (Bell Works, Alcalá 33) pero con capa fina; con c-Si no documentada | Fotos de marquesinas; lucernario no documentado | Dulwich College (Singapur), *skylight* |
| Datos para crear el PAN | **Completos** (Voc, Isc, Vmp, Imp, 36 células, coeficientes) — pero Voc/Vmp con 2 cifras | **Completos** | **Insuficientes** |
| Precio (€/Wp o €/m²) | **no publicado** | **no publicado** | **no publicado** |

### 3.2 Puntuación (método Arcas, 1 = peor, 3 = mejor; empates a media)

**Requisito de paso previo, no puntuable:** transparencia publicada ≥ 20 % (la hipótesis de
trabajo de V1a y la razón de ser del BIPV en un lucernario sobre un hall). **Polysolar no lo
pasa con dato publicado (10 %)**; AGC no publica transparencia. Se puntúa igualmente a los tres
para que la tabla sea completa y honesta:

| Criterio | Onyx c-Si | Polysolar | AGC |
| --- | --- | --- | --- |
| Densidad Wp/m² | 1 | 3 | 2 |
| Transparencia publicada | 3 | 2 | 1 |
| Peso (encaje en perfilería existente) | 2 | 3 | 1 |
| U y g publicados (argumento térmico) | 3 | 1,5 | 1,5 |
| Coeficiente de temperatura | 3 | 2 | 1 |
| Garantías | 1 | 3 | 2 |
| Homologación del laminado para cubierta | 2 | 3 | 1 |
| Datos para PAN | 2,5 | 2,5 | 1 |
| Referencias en lucernario | 2 | 1 | 3 |
| **Total** | **19,5** | **21,0** | **13,5** |

### 3.3 Justificación de la elección — Onyx Solar c-Si al 35 %

**Por puntos gana Polysolar, pero no cumple la función del elemento.** Su ventaja sale de la
densidad (199 Wp/m²) y la garantía (30 años), y ambas son consecuencia directa de tapar el 90 %
del vidrio con célula. Un lucernario de 579 m² sobre un hall con un 10 % de transparencia deja
de ser un lucernario: la justificación de V1a, fijada desde el 31/08/2026, **no es energética
sino arquitectónica** (luz natural + control solar), y el BIPV aporta en cualquier caso en torno
al 2-3 % del consumo. Optimizar V1a por Wp/m² contra su propia función sería un error de
planteamiento que el tribunal vería.

Onyx c-Si al 35 % es, por tanto, la elección, por cuatro razones:

1. **Es el único que publica una gama de transparencias** (11-43 %) y una fila exacta al 35 %
   con 129,6 Wp/m², sin interpolar. Cumple la hipótesis de trabajo (125 Wp/m²) **con más
   transparencia de la supuesta** (35 % frente a 20 %).
2. **Publica U** (5,2 W/m²·K monolítico; hasta 1,0 en UGU), que es la mitad del argumento térmico.
3. **Mejor coeficiente de temperatura** de los tres (−0,32 %/°C frente a −0,362), relevante en un
   vidrio horizontal sin ventilación posterior.
4. **Fabricante español con planta en Ávila**, con proyectos de lucernario ejecutados; facilita
   pedir oferta real para el capítulo económico.

**Lo que hay que declarar como debilidad:** garantía corta (5 años producto, 80 % a 10 años), EVA
como intercalario (el trabajo previo, §9, verificó que en España **no hay norma que lo impida**:
DITEX 692EX/24 del IETcc evaluó un vidrio FV con EVA para lucernarios) y **g no publicado** para
la gama cristalina.

**Por qué no AGC:** sin transparencia, g, U, peso ni datos eléctricos, no se puede ni crear el
PAN ni sostener el argumento térmico. Queda como contraste.

**Capa fina (Onyx a-Si + PVB), descartada:** 34,0 Wp/m² a transparencia 20 % (verificado por dos
fuentes en el trabajo previo). Sobre 463 m² darían ~15,7 kWp: no es una alternativa de
dimensionado, es otra variante.

**Cuándo cambiar a Polysolar:** si Mario y el tutor aceptan una transparencia del 10 % (hall con
iluminación artificial permanente, por ejemplo), o si Polysolar confirma por escrito una versión
al 20-35 % manteniendo la homologación DIBt. Su **homologación alemana de construcción** es la
mejor credencial de seguridad del laminado de las tres fichas, y merece citarse aunque no se elija.

### 3.4 Parámetros de simulación que se derivan

- **Uc sin ventilación posterior:** la guía de proyecto (`guia-diseno-pvsyst.md`, §7.2) fija
  **Uc ≈ 15 W/m²·K** para BIPV integrado frente a los 20 del resto; el cálculo preliminar con 20 es
  cota superior (−1,5 a −2,5 % de energía). Hipótesis a mantener y declarar; ningún fabricante de
  la tabla publica un Uc.
- **PAN:** no está en la base de datos de PVsyst; se crea en `Databases → PV modules → New` con
  Pnom 182 W, 36 células, Voc 24 V, Isc 9,66 A, Vmp 19 V, Imp 9,35 A, μPmp −0,32 %/°C, μVoc −0,28 %/°C,
  μIsc +0,07 %/°C, 1650 × 850 mm. **Ojo:** Voc y Vmp vienen con dos cifras significativas; hay que
  pedir a Onyx la ficha del modelo concreto con tres decimales, o PVsyst ajustará el modelo de un
  diodo con un error apreciable.

---

## 4. Categoría B — V1b, V2 y V3 (módulo opaco único)

### 4.1 Tabla comparativa

| Característica | **REC Alpha Pure-RX 470** | **AIKO Neostar 2P 475** | **LONGi Hi-MO X6 Max Explorer 465** |
| --- | --- | --- | --- |
| Referencia | REC470AA Pure-RX | AIKO-A475-MAH54Mw | LR7-54HTH-465M |
| Revisión de ficha | IEC EN 8.2026 V8 | DS_EN_2405_V1.1 (05/2024) | 20240511 V2 |
| Potencia pico STC (Wp) | 470 | 475 | 465 |
| Tecnología de célula | N-type **HJT**, 88 medias células bifaciales | N-type **ABC** (contacto posterior), 108 medias | **HPBC** (contacto posterior; «HTH»), 108 medias |
| Dimensiones (mm) | 1728 × 1205 × 30 (2,08 m²) | 1757 × 1134 × 30 (1,99 m²) | 1800 × 1134 × 30 (2,04 m²) |
| Peso (kg) | 22,7 | 21,5 ± 3 % | 21,6 |
| **Eficiencia (%)** | 22,6 | **23,8** | 22,8 |
| **Coef. temp. Pmax (%/°C)** | **−0,24** | −0,26 | −0,28 |
| Coef. temp. Voc / Isc (%/°C) | −0,24 / +0,04 | −0,22 / +0,05 | −0,23 / +0,050 |
| LID (1.er año) | 2 % (98 % año 1) | ≤ 1 % | < 1 % |
| PID | no declarado | no declarado | no declarado |
| Degradación anual | 0,25 %/año | ≤ 0,35 %/año (años 2-30) | 0,40 %/año (años 2-25) |
| Garantía de potencia | **92 % a 25 años** | 90,6 % a 25 / 88,85 % a 30 años | 89,4 % a 25 años |
| Garantía de producto | 20 años (25 con instalador certificado REC ProTrust) | 15 años en la web del fabricante (ampliable a 25); la ficha muestra 25 — **ambigüedad a aclarar** | 15 años |
| Carga mecánica frontal / trasera | **+7000 / −4000 Pa** | +5400 / −2400 Pa | +5400 / −2400 Pa |
| Salinidad / amoniaco | IEC 61701 SM6 / IEC 62716 | no declarado | no declarado |
| Características especiales | Vidrio AR 3,2 mm; backsheet negro; granizo 55 mm (PVEL) | Monovidrio 3,2 mm; optimización frente a sombreado parcial (fabricante); marco negro | Monovidrio 3,2 mm con recubrimiento |
| **Tensión máx. sistema** | **1000 V** | 1500 V | 1500 V |
| Voc / Isc (STC) | 65,7 V / 8,95 A | 41,24 V / 14,35 A | 39,55 V / 14,93 A |
| Vmp / Imp (STC) | 55,4 V / 8,49 A | 34,80 V / 13,66 A | 33,39 V / 13,93 A |
| NMOT / NOCT (°C) | 44 ± 2 | no declarado (ensayo NOCT 800 W/m², 20 °C) | 45 ± 2 |
| Fusible serie máx. | 25 A | 25 A | 25 A |
| Posición en ranking | 1.º CER 2025; 1.º EnergySage 2026 | 3.º CER 2025; AIKO 1.º en eficiencia TaiyangNews 06/2024 | LONGi: 6.º CER; 3.º TaiyangNews; 2.º en envíos; **AAA** PV-Tech Q4 2025 |
| Bancabilidad PV-Tech | CC+ (Q2 2024, **no verificado**: resumen de distribuidor) | B (Q2 2024, **no verificado**) | **AAA** (Q4 2025, nota de prensa del fabricante + pv-tech.org) |
| Precio (€/Wp) — categoría pvXchange feb. 2026 | 0,145 («Full black») | 0,130-0,145 («High efficiency» > 23 % / «Full black») | 0,115 («Mainstream» ≤ 23 %) |
| PAN en PVsyst | **Sí** (usado en el informe del trabajo previo, PVsyst V8.0.19) | **no verificado** | **no verificado** |

> **Precio:** pvXchange publica precio **por categoría tecnológica**, no por modelo, y desde
> febrero ha seguido subiendo (+5,5 % entre marzo y abril de 2026). Sirve para ordenar, no como
> partida de CAPEX. Para el capítulo 9 hay que pedir oferta o usar la fuente de costes que elija
> `analista-economico`.

### 4.2 Puntuación (método Arcas, 1 = peor, 3 = mejor)

| Criterio (origen) | REC | AIKO | LONGi |
| --- | --- | --- | --- |
| Coeficiente de temperatura (Arcas, diap. 16) | 3 | 2 | 1 |
| Eficiencia (Arcas) | 1 | 3 | 2 |
| Precio (Arcas, diap. 16) | 1 | 2 | 3 |
| Tamaño y peso para el manejo (Arcas) | 1 | 3 | 2 |
| Garantías (Arcas, diap. 16) | 3 | 2 | 1 |
| LID del primer año (diap. 16) | 1 | 2,5 | 2,5 |
| Posición en ranking (diap. 15-16) | 2 | 2 | 3 |
| Tensión máx. del sistema (propio) | 1 | 2,5 | 2,5 |
| **Total** | **13** | **19** | **17** |

Los cuatro ejes del radar de Arcas (coef. temperatura, eficiencia, precio, tamaño) dan **REC 6,
AIKO 10, LONGi 8**: el mismo orden.

### 4.3 Justificación de la elección — AIKO Neostar 2P 475 W

1. **Es el más eficiente (23,8 %) y V1b y V2 están limitadas por superficie.** A igualdad de
   metros cuadrados de módulo mete un **~6 % más de potencia que REC** y un ~5 % más que LONGi
   (§5). En la variante que mejor rinde del TFM (V2), eso son ~40 kWp más sobre la misma huella.
2. **Coeficiente de temperatura de −0,26 %/°C**, a 0,02 puntos del mejor (REC) y mejor que LONGi.
   En Madrid la diferencia con REC en energía anual es marginal.
3. **1500 V de tensión máxima**: el mismo módulo sirve para la planta en suelo (V3), donde el
   estándar son inversores y strings de 1500 V. Con REC (1000 V) la V3 quedaría atada a strings
   cortos y más cajas de conexión.
4. **Degradación inicial ≤ 1 %** frente al 2 % de REC.
5. La tecnología de contacto posterior sin rejilla frontal con **optimización frente a sombreado
   parcial** declarada por el fabricante encaja con sheds (sombra mutua de filas) y marquesinas.
   Es afirmación del fabricante, no dato cuantificado: no se usa como argumento principal.

**Frente a LONGi, que queda de reserva:** LONGi gana en bancabilidad (AAA) y precio. Si en V3
—varios MWp, previsiblemente financiados— el tribunal o el tutor valoran más la bancabilidad del
fabricante que la densidad, LONGi es la elección defendible, y su ficha está además en el
material del Módulo 6. La diferencia de puntuación (19 frente a 17) es corta y hay que decirlo así.

### 4.4 Por qué REC no sale confirmado (desviación respecto al trabajo previo)

REC tiene el mejor coeficiente de temperatura, la mejor garantía de potencia y la mayor robustez
mecánica, y es el 1.º en dos rankings de producto. Pierde por: (a) **1000 V** de tensión de
sistema, que penaliza V3; (b) la menor eficiencia de los tres en la clase de 470 W; (c) **2 % de
degradación el primer año**; (d) precio de categoría más alto; (e) bancabilidad baja (dato no
verificado). Fue una buena elección para una cubierta de 102 kWp con un inversor de 1100 V; deja
de serlo cuando el mismo módulo tiene que servir a una planta en suelo de MW. **Hay que escribirlo
así en la memoria**, porque el tutor corrigió el trabajo previo con REC.

Matiz: REC fabrica la misma serie hasta 485 W (23,3 %, 233 W/m²). Aun con la potencia máxima,
sigue por debajo de AIKO en eficiencia y conserva la limitación de 1000 V.

---

## 5. Implicaciones inmediatas

### 5.1 Potencia y n.º de módulos aproximados

Superficies de partida de `recalculo-superficies-3d-pvsyst.md` (geometría cerrada el 19/09/2026).
Cálculo propio: superficie neta de módulo / área del módulo, redondeo a la baja; **sin** ajustar
todavía a strings completos ni a entradas de inversor.

| Variante | Superficie neta de módulo | Módulo | Área unitaria | N.º | **kWp** | Antes (REC o hipótesis) |
| --- | --- | --- | --- | --- | --- | --- |
| **V1a** | 578,91 × 0,80 = **463,1 m²** de vidrio activo | Onyx 182 Wp | 1,4025 m² | **330** | **≈ 60,1** | 57,89 (125 Wp/m², VLT 20 %) |
| **V1b** | 2.756,88 × 0,70 × 0,82 = **1.582,5 m²** | AIKO 475 | 1,9924 m² | **794** | **≈ 377** | 358,7 techo por superficie; 338,40 adoptado |
| **V2** | 3.536 × 0,90 = **3.182,4 m²** | AIKO 475 | 1,9924 m² | **1.597** | **≈ 758** | 716,28 (1.524 REC) |
| **V3** | por decidir (subparcela en Colmenar Viejo) | AIKO 475 | — | — | — | 2,0-2,5 MWp de hipótesis |

Comparación en la misma superficie: con LONGi 465 (2,0412 m²) serían 775 módulos / 360 kWp en
V1b y 1.559 / 725 kWp en V2; con REC 470 (2,0822 m²), 759 / 357 kWp y 1.528 / 718 kWp.

**Cautelas:**
- El factor 0,82 de empaquetado en sheds se validó con la geometría del REC (1728 × 1205 mm).
  El AIKO es más largo y estrecho (1757 × 1134 mm): hay que **rehacer la disposición en la escena
  3D de PVsyst** antes de dar por buenos los 794 módulos.
- En V2, con ~758 kWp el pico de producción supera aún más la carga plana de ~437 kW: aumentan
  los excedentes recortados por el antivertido respecto a los 16,5 MWh calculados con REC. Hay que
  recalcularlo; puede reabrir la discusión de la batería en V2.
- En V1a el nuevo valor sube un 3,8 % frente a la hipótesis con **más transparencia** (35 % frente
  a 20 %). No cambia la conclusión: sigue siendo marginal en energía.

### 5.2 Datos que condicionan el inversor (a elegir después)

| Dato | AIKO 475 | Onyx 182 (V1a) |
| --- | --- | --- |
| Voc STC / β_Voc | 41,24 V / −0,22 %/°C | 24 V / −0,28 %/°C |
| Vmp STC | 34,80 V | 19 V |
| Isc / Imp STC | **14,35 A** / 13,66 A | 9,66 A / 9,35 A |
| Tensión máx. sistema | 1500 V | 1000 V |

Orientación (cálculo propio, **temperatura mínima pendiente de AEMET**, fase 1.3): con −10 °C,
Voc del AIKO = 41,24 × (1 + 0,0022 × 35) ≈ **44,4 V** → máx. **24 módulos** en serie con un
inversor de 1100 V y **33** con uno de 1500 V.

**Alerta para la fase 4:** los 14,35 A de Isc son un 60 % más que los 8,95 A del REC. Con dos
strings en paralelo por MPPT la corriente llega a ~28,7 A (antes del factor de seguridad). Hay
que comprobar la **intensidad máxima DC por MPPT** de cada inversor candidato; el reparto de
strings de V1b calculado para el Huawei SUN2000-100KTL-M2 con REC (20 entradas × 8,6 A) **no se
puede reutilizar tal cual**.

### 5.3 Pendientes

| # | Pendiente | Quién | Bloquea |
| --- | --- | --- | --- |
| 1 | Comprobar si el **PAN del AIKO-A475-MAH54Mw** (y del LONGi LR7-54HTH-465M) está en la BD de PVsyst 8.1.5; si no, descargarlo del fabricante | Mario → `piloto-pvsyst` | Simulación de V1b/V2/V3 |
| 2 | Crear el PAN del Onyx 182 Wp y **pedir a Onyx la ficha con Voc/Vmp de tres cifras**, el g de la gama cristalina y una oferta | Mario (consulta a Onyx) | Simulación de V1a y argumento térmico |
| 3 | Aclarar la **garantía de producto del AIKO** (15 o 25 años) y su **disponibilidad en España** (la ficha consultada es de un distribuidor australiano) | Consulta a AIKO Europa | Cap. 9 (OPEX / reposición) |
| 4 | Verificar la **bancabilidad** de AIKO y REC en el informe PV ModuleTech vigente | `investigador-cientifico` | Solo si se reabre la elección con LONGi |
| 5 | Rehacer la disposición de sheds (V1b) y marquesinas (V2) con las dimensiones del AIKO | Mario en PVsyst 3D | Cifras de §5.1 |
| 6 | Comprobar la carga de viento (succión) del CTE en marquesinas frente a los −2400 Pa del AIKO | Fase 6 | Estructura soporte |
| 7 | Tmín/Tmáx diurnas de AEMET para cerrar el n.º de módulos en serie | Fase 1.3 | Fase 5 |
| 8 | Preparar la diap. 17: imagen del módulo, curva I-V y los puntos fuertes destacados | `redactor-humanizador` | Redacción del apartado |

---

## 6. Qué llevar al documento

- Dos tablas comparativas (§3.1 y §4.1, formato Arcas + diap. 16), cada una seguida de la tabla
  de puntuación y, si se quiere seguir a Arcas al pie de la letra, un **gráfico radar** con los
  cuatro ejes de su 4.3.1.
- La frase de método de Arcas se puede parafrasear, pero la cita va a su TFM solo si Mario lo da
  de alta como fuente citable (hoy está en `conocimiento fotovoltaico/Referencia/`, no citable).
- Las fichas técnicas son fuente citable si se procesan con `bibliotecario-pdf` (regla 10): hay
  que dar de alta al menos las de AIKO, Onyx (Technical Guide) y las dos de reserva.

---

## 7. Fuentes

**Criterios y formato**
1. M. Arcas, TFM (2024), cap. 4.3, pp. 16-17 impresas — `Documentacion de apoyo/Ejemplos TFM/TFM_M_A.pdf`
2. J. Amador, *GUIA_PLANTILLA Estudio Autoconsumo FV ERMA20.pptx*, diap. 15-17 — `Documentacion de apoyo/Trabajo Autoconsumo CPD/`

**Rankings (diap. 15)**
3. CleanEnergyReviews, *Best solar panels 2025* — <https://www.cleanenergyreviews.info/blog/best-solar-panels-review>
4. EnergySage, *Best solar panels complete ranking* (act. 01/07/2026) — <https://www.energysage.com/solar/best-solar-panels-complete-ranking/>
5. TaiyangNews, *Top solar modules listing June 2024* — <https://taiyangnews.info/top-modules/top-solar-modules-listing-june-2024/>
6. Black Ridge Research, *Top solar PV module manufacturers* — <https://www.blackridgeresearch.com/blog/top-solar-pv-module-panel-manufacturers-companies-suppliers-producers>
7. PV Tech, *JA Solar moves to AAA-Rating in latest PV ModuleTech Bankability Ratings report* — <https://www.pv-tech.org/ja-solar-moves-to-aaa-rating-in-latest-pv-moduletech-bankability-ratings-report/> · LONGi, *AAA Rating* — <https://www.longi.com/us/news/longi-earns-24th-aaa-rating/>
8. 7SUN, *PV ModuleTech Bankability Ratings Q2 2024* (resumen de distribuidor; **no verificado** contra el informe) — <https://7sun.eu/pv-moduletech-bankability-ratings-q2-2024/>
9. Sin acceso: solaranalytica.com (404), solarfeeds.com (DNS), semprius.com (redirige a web ajena).

**Fichas técnicas — categoría B**
10. REC, *REC Alpha Pure-RX Datasheet 460-485 W*, IEC EN 8.2026 V8 — <https://www.recgroup.com/sites/default/files/2025-01/Web_DS_REC%20Alpha%20Pure-RX_EN.pdf>
11. AIKO, *Neostar 2P Mono-Glass 450-475 W*, DS_EN_2405_V1.1 — <https://www.solargain.com.au/sites/default/files/2024-09/Aiko-Neostar-475w.pdf> · página de producto (garantías, degradación) — <https://aikosolar.com/en/products/neostar-2pplus54-dual-glass/>
12. LONGi, *Hi-MO X6 Max Explorer LR7-54HTH 455-465M*, 20240511 V2 (ES) — `Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Ejercicios y Ejemplos/Configuraciones/Configuraciones/Fichas tecnicas Longi/ES_Datasheet_LR7_54HTH_X6_MAX_Explorer.pdf`
13. Precios: pvXchange vía Rinnovabili (feb. 2026) — <https://www.rinnovabili.net/business/energy/photovoltaic-module-prices-2025-updated-data/> · tendencia abril 2026 — <https://www.pvxchange.com/Market-Analysis-April-2026-Solar-module-price-increase-continues-for-now>

**Fichas técnicas — categoría A**
14. Onyx Solar, *Technical Guide* rev. 260630 — <https://onyxsolar.com/images/3.resources/Technical_guide_EN-ES_300626.pdf> (datos verificados el 02/09/2026 en `Memoria/analisis/bipv-tragaluz-fichas-tecnicas.md`, rama `worktree-bipv-tragaluz-fichas`)
15. Polysolar, *PS-MC-ST Series panels* — <https://files.uk-siteglide.com/instances/42/assets/Datasheets/PS-MC-ST-datasheet.pdf> · página de especificaciones — <https://www.polysolar.co.uk/technology/specifications>
16. AGC, *SunEwat* EN-08/2023 — <https://agc-glassasia.com/wp-content/uploads/2023/09/SunEwat_Brochure_0923_EN-Asia.pdf> (vía el mismo informe del 02/09/2026)

**Documentos internos del proyecto**
17. `Memoria/analisis/recalculo-superficies-3d-pvsyst.md` y `estimacion-preliminar-variantes.md` — superficies y factores de reducción
18. `conocimiento fotovoltaico/Referencia/guia-diseno-pvsyst.md`, §6-7 — Uc del BIPV y alta del PAN
19. `conocimiento fotovoltaico/Referencia/trabajo-previo-modulo6-cpd.md` — REC 470 en el informe PVsyst del Módulo 6
