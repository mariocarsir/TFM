---
title: "BIPV semitransparente para el lucernario del CPD — fichas técnicas y proyecto de referencia"
tipo: analisis-tecnico
autor: investigador-cientifico
fecha: 2026-09-02
estado: verificado-parcial
variante: V1a (BIPV en tragaluz)
tags:
  - BIPV
  - vidrio-fotovoltaico
  - lucernario
  - tragaluz
  - autoconsumo
  - CPD
  - TFM
relacionado:
  - "[[indice_propuesto]]"
---

# BIPV semitransparente para el lucernario del CPD (variante V1a)

> **Alcance.** Búsqueda de mercado verificada de vidrio fotovoltaico semitransparente
> apto para sustituir el lucernario del CPD de Tres Cantos (472 m² de proyección
> horizontal en catastro, ~378 m² estimados de vidrio activo tras descontar perfilería).
>
> **Regla aplicada.** Toda cifra de este documento lleva la URL de la que sale. Lo que no
> se ha podido verificar aparece marcado como **NO VERIFICADO** con indicación de qué falta.
> No se ha completado ningún hueco con conocimiento general del modelo.

## 0. Resumen de lo que cambia respecto a la hipótesis de partida

La hipótesis de diseño vigente es **VLT ≈ 20 %, 125 Wp/m², ~47 kWp, 76 MWh/año**. El
contraste con fichas técnicas reales obliga a matizarla en un punto y la confirma en otro:

| Hipótesis | Contraste con fuente verificada | Veredicto |
| --- | --- | --- |
| 125 Wp/m² a VLT 20 % | Alcanzable **solo con silicio cristalino** con separación entre células. La capa fina a-Si da **34,0 Wp/m² a VLT 20 %** (verificado por dos fuentes independientes) | Hipótesis **válida pero condicionada a c-Si** |
| ~47 kWp sobre 378 m² | c-Si Onyx a VLT 35 % da 129,6 Wp/m² → 378 × 129,6 = **49,0 kWp**. Casi exacto | **Confirmada** |
| VLT 20 % | Con c-Si a VLT 20 % la densidad sube a ~160 Wp/m² (interpolado) → 60,5 kWp. Con VLT 35 % se obtienen los 47 kWp buscados | El par (VLT 20 %, 125 Wp/m²) es **internamente conservador**: a VLT 20 % sobra potencia |
| Vidrio de seguridad laminado | Confirmado como necesario, pero **no por el motivo indicado en el encargo** (ver §4) | Matizado |

**El riesgo real no es el que se anticipaba.** No es la potencia: es el **encapsulante**. El
producto cristalino estándar de Onyx se lamina con **EVA**, y en la práctica europea de
acristalamiento en cubierta el EVA no tiene aprobación de base, solo autorización caso a
caso (§4.3). El producto de capa fina sí se lamina con **PVB** — pero da cuatro veces menos
potencia. Esa tensión, y no el dimensionado, es la decisión de proyecto de V1a.

---

## 1. Ficha 1 — Onyx Solar, vidrio FV de silicio cristalino

**Por qué encaja:** es la única de las tres que alcanza la densidad de potencia del objetivo
(47 kWp en 378 m²). Fabricante español (Ávila), con fábrica propia y guía técnica bilingüe
descargable. Vidrio-vidrio laminado, configurable como UGU.

**Fuente:** Onyx Solar, *Technical Guide* (rev. 260630), pp. 6-11, 26-31, 39-41 —
<https://onyxsolar.com/images/3.resources/Technical_guide_EN-ES_300626.pdf>

### 1.1 Datos generales (comunes a la gama cristalina)

| Parámetro | Valor | Fuente |
| --- | --- | --- |
| Fabricante / país | Onyx Solar Energy S.L. — Ávila, España | Guía técnica, p. 3 |
| Tecnología de célula | 6″ Mono 158 silicio cristalino | Guía técnica, pp. 6-11 |
| Composición del laminado | 4 mm vidrio templado bajo en hierro (frontal) + **1,80 mm EVA** + 4 mm vidrio templado (trasero) | Guía técnica, pp. 6-11 |
| Espesor total | 9,8 mm | Guía técnica, pp. 6-11 |
| Peso específico | ~20 kg/m² (calculado: 28 kg / 1,40 m²) | Calculado sobre guía técnica, p. 7 |
| Transmitancia térmica U | **5,2 W/m²·K** (monolítico, UNE-EN 673:1998) | Guía técnica, pp. 7-11 |
| Coef. temperatura Pmpp | **−0,32 %/°C** | Guía técnica, p. 7 (extracción `raw`) |
| Coef. temperatura Voc | −0,28 %/°C | Guía técnica, p. 7 |
| Coef. temperatura Isc | +0,07 %/°C | Guía técnica, p. 7 |
| Caja de conexiones | IP67, cableado 4,0 mm² | Guía técnica, pp. 6-11 |
| Tensión máx. sistema | 1000 V | Guía técnica, pp. 6-11 |
| Temperatura de operación | −40…+85 °C | Guía técnica, p. 7 |
| Tolerancia de potencia | ±10 % | Guía técnica, p. 6 |

### 1.2 Módulos estándar publicados

| Referencia | Dimensiones (mm) | Sup. (m²) | Nº células | VLT | Pmpp (Wp) | **Wp/m²** | Voc (V) | Isc (A) | Vmpp (V) | Impp (A) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 044A0-14750480-43-M | 1475 × 480 | 0,71 | 16 | 43 % | 81 | 114,4 *(calc.)* | 11 | 9,66 | 9 | 9,35 |
| 044A0-12450635-43-M | 1245 × 635 | 0,79 | 18 | 43 % | 91 | **115,0** | 12 | 9,66 | 10 | 9,35 |
| 044A0-16500850-35-M | 1650 × 850 | 1,40 | 36 | 35 % | 182 | **129,6** | 24 | 9,66 | 19 | 9,35 |
| 044A0-17001000-11-M | 1700 × 1000 | 1,70 | 60 | 11 % | 303 | **178,2** | 41 | 9,66 | 32 | 9,35 |

*Fuente: Onyx Solar Technical Guide pp. 6-9. Los valores en negrita son el campo
«Peak Power [Wp/sqm]» publicado en la propia ficha; el marcado (calc.) es Pmpp/superficie.*

Onyx publica el campo **«Light Transmission»** con el mismo valor que **«Transparency
degree»** para la gama cristalina (p. ej. p. 7: `Transparency degree 35%` /
`Light Transmission 35%`). Es decir, para el cristalino la transparencia declarada es
geométrica —la fracción libre entre células— y Onyx la usa directamente como transmisión
luminosa. **No he encontrado una medida VLT según UNE-EN 410 para la gama cristalina**:
la tabla de propiedades ópticas de la p. 26 corresponde solo a la gama de capa fina.
→ **NO VERIFICADO: el factor solar g y la VLT según EN 410 del cristalino.** Falta pedir
a Onyx la hoja de propiedades ópticas del cristalino en la configuración concreta.

### 1.3 Interpolación para el caso del CPD

Sobre los tres puntos publicados (11 % → 178,2; 35 % → 129,6; 43 % → 115,0 Wp/m²):

| Grado de transparencia | Wp/m² | Potencia sobre 378 m² |
| --- | --- | --- |
| 11 % | 178,2 (publicado) | 67,4 kWp |
| 20 % | ~160 (interpolado) | ~60,5 kWp |
| 35 % | 129,6 (publicado) | **49,0 kWp** |
| 43 % | 115,0 (publicado) | 43,5 kWp |

La interpolación a 20 % es **cálculo propio**, no cifra de fabricante. La fila de 35 % sí es
dato publicado y es la que reproduce el objetivo de ~47 kWp.

### 1.4 Certificaciones y garantía

- Normas declaradas (guía técnica, pp. 28-31): IEC 61215, IEC 61730-1, IEC 61646, UL 1703,
  ISO 12543-4:2011 (vidrio laminado de seguridad), EN 12150:2005 (templado), EN 12600:2003
  (ensayo pendular), EN 410:2011, EN 356:2001, EN 13501:2007.
- **Aviso de la propia guía:** «*Depending on the final BIPV glass configuration, it CAN
  comply with the following standards*». Es una lista de normas aplicables **según
  configuración**, no un certificado emitido para un producto concreto. Marketing, no
  certificado firmado. Habrá que exigir el certificado del laminado concreto.
- **Marcado CE como producto de construcción (EN 14449 / EN 1279): NO VERIFICADO.** La guía
  no menciona EN 14449 ni EN 1279. Es un hueco importante para justificar el vidrio en obra
  en España.
- **Garantía (pp. 39-40):** producto **5 años**; potencia **80 % a 10 años**.
  Es una garantía **notablemente más corta que la de un módulo FV convencional**
  (habitualmente 12-15 años de producto y 25-30 de potencia). Impacto económico directo
  sobre el VAN de V1a: hay que modelar reposición o degradación no cubierta más allá del año 10.

### 1.5 Configuración como UGU (doble acristalamiento)

Tabla de U publicada (guía técnica, p. 27), calculada **incluyendo un vidrio frontal 3+4**:

| Cámara | Vidrio interior | U (W/m²·K) |
| --- | --- | --- |
| 6 mm aire | 4+4 mm | 3,2 |
| 6 mm argón | 4+4 mm | 2,9 |
| 6 mm aire | 4+4 mm bajo emisivo | 2,4 |
| 6 mm argón | 4+4 mm bajo emisivo | 1,9 |
| 12 mm aire | 4+4 mm | 2,7 |
| 16 mm argón | 4+4 / 6T mm bajo emisivo | 1,1 |
| 20 mm argón | 4+4 mm bajo emisivo | 1,1 |
| 12/4/12 argón (doble cámara) | 4+4 mm bajo emisivo | **1,0** |

---

## 2. Ficha 2 — Onyx Solar, vidrio FV de silicio amorfo (capa fina) con PVB

**Por qué encaja:** es la configuración **realmente ejecutada en lucernario** en los dos
proyectos de referencia documentados (§3), se lamina con **PVB** —el encapsulante con
aprobación de base para acristalamiento en cubierta (§4.3)— y es la única de las tres para
la que dispongo de **fichas firmadas de proyecto** con óptica y térmica completas.

**Por qué no encaja del todo:** su densidad de potencia es **~4 veces menor**. Sobre 378 m²
no llega a 13 kWp. Es información útil precisamente por eso: descarta la capa fina como vía
para el objetivo de 47 kWp.

### 2.1 Configuración monolítica — ficha firmada Bell Works GL.01a/GL.01b

**Fuente:** Onyx Solar, ficha técnica de proyecto —
<https://onyxsolar.com/images/5.projects/108.bell_works_us/bell-works-skylight-onyx-solar-pv-glass-photovoltaics-bipv-specs.pdf>

| Parámetro | Valor |
| --- | --- |
| Dimensiones | 1930 × 865 mm |
| Superficie | 1,67 m² |
| Espesor total | 12,72 mm |
| Peso | 46,74 kg → **28,0 kg/m²** *(calc.)* |
| Tecnología | a-Si capa fina |
| Grado de transparencia | **M Clear-20 %** |
| Vidrio frontal | 4 mm templado |
| Vidrio activo FV | 3,2 mm float |
| Vidrio trasero | 4 mm templado |
| Encapsulante | **3,04 mm láminas PVB** (2 × 1,52 mm) |
| Pmpp | 57 Wp → **34,1 Wp/m²** *(calc.)* |
| Voc / Isc | 67 V / 1,50 A |
| Vmpp / Impp | 46 V / 1,22 A |
| Tolerancia | ±5 % |
| Caja de conexiones | IP65 |
| Coef. temp. Pmpp / Voc / Isc | −0,19 / −0,28 / +0,09 %/°C |

**Verificación cruzada:** 34,1 Wp/m² calculado sobre la ficha del proyecto coincide con los
**34,0 Wp/m²** que la guía técnica general publica para transparencia 20 % (p. 26). Dos
fuentes independientes del mismo fabricante concuerdan. Cifra sólida.

### 2.2 Propiedades ópticas y térmicas de la gama de capa fina

**Fuente:** Onyx Solar, *Technical Guide*, p. 26 «Other Properties».

| Propiedad (norma) | Config. 3+4 |  |  |  | Config. 6T+3+6T |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grado de transparencia** | 0 % | 10 % | 20 % | 30 % | 0 % | 10 % | 20 % | 30 % |
| Potencia pico (Wp/m²) | 57,6 | 40,0 | 34,0 | 28,0 | 57,6 | 40,0 | 34,0 | 28,0 |
| Peso (kg/m²) | 16,7 | 16,7 | 16,7 | 16,7 | 41 | 41 | 41 | 41 |
| **U (W/m²·K)** — UNE-EN 673:1998 | 5,7 | 5,7 | 5,7 | 5,7 | 5,2 | 5,2 | 5,2 | 5,2 |
| **Factor solar g** — UNE-EN 410:2011 | 22 % | 29 % | 34 % | 41 % | 23 % | 29 % | 32 % | 37 % |
| **Transmisión luminosa** — UNE-EN 410 | 0,2 % | 10,8 % | 17,3 % | 28,4 % | 0,0 % | 10,1 % | 16,3 % | 26,7 % |
| Transmisión solar — UNE-EN 410 | 0,2 % | 9,4 % | 15,0 % | 24,3 % | 0,0 % | 7,4 % | 11,5 % | 18,6 % |
| Transmisión UV — UNE-EN 410 | 0,0 % | 1,5 % | 1,5 % | 4,7 % | 0,0 % | 0,1 % | 0,3 % | 0,4 % |
| **EN 12600:2003** | 2(B)2 | 2(B)2 | 2(B)2 | 2(B)2 | **1(B)1** | 1(B)1 | 1(B)1 | 1(B)1 |
| Atenuación acústica (dB) | 32 (−1;−3) | | | | 34 (−1;−3) | | | |
| Reacción al fuego — EN 13501-1 | B-s1,d0 | | | | B-s1,d0 | | | |
| EN 356:2001 (efracción) | No aplicable | | | | **P3A** | | | |

> **Cautela metodológica.** Esta tabla se ha extraído de un PDF cuyo maquetado en dos
> columnas se solapa al convertirlo a texto. La lectura es internamente coherente (los pesos
> 16,7 vs 41 kg/m² y las U 5,7 vs 5,2 casan con cada composición), pero **conviene que Mario
> confirme visualmente la p. 26 de la guía** antes de llevar estos números al documento.

**Dato clave para el argumento térmico:** la transmisión luminosa medida según EN 410 es
**muy inferior** al grado de transparencia nominal (20 % nominal → 17,3 % real en 3+4;
16,3 % en 6T+3+6T). No son intercambiables. Un vidrio «al 20 %» transmite en torno al 16-17 %.

### 2.3 Configuración UGU — ficha firmada Alcalá 33 (Madrid)

**Fuente:** Onyx Solar, ficha técnica de proyecto —
<https://onyxsolar.com/images/5.projects/144.alcala-33/alcala-33-curtain-wall-onyx-solar-pv-glass-photovoltaics-bipv-data.pdf>

| Parámetro | Valor |
| --- | --- |
| Dimensiones | 1110 × 2140 mm — 2,38 m² |
| Espesor total | **35,76 mm** |
| Peso | 114 kg → **47,9 kg/m²** *(calc.)* |
| Tecnología / transparencia | a-Si capa fina — **XL Vision (30 %)** |
| Composición | 4 mm templado + **3,2 mm float FV** + 4 mm templado ⟨**1,52 mm PVB ×2**⟩ ‖ **12 mm cámara de aire** ‖ 4 mm float bajo emisivo + 4 mm float |
| **Factor solar / SHGC** | **17 %** |
| **Transmisión luminosa** | **26,70 %** |
| Transmisión UV | < 1 % |
| Reflexión luminosa | 8 % |
| **Valor Ug** | **1,5 W/m²·K** |
| **Potencia pico** | **28,0 Wp/m²** |
| Pmpp / Voc / Isc / Vmpp / Impp | 66 Wp / 167 V / 0,69 A / 115 V / 0,58 A |
| Coef. temp. Pmpp / Voc / Isc | −0,19 / −0,28 / +0,09 %/°C |
| Protección | IP65, 1000 Vsys, −40…+85 °C, protección máx. serie 3 A |

Esta es **la mejor ficha de las cinco que he podido descargar**: es una hoja firmada de
proyecto, en español, con las dos mitades del argumento (eléctrica y óptico-térmica) y con
una **UGU laminada por las dos hojas**, que es exactamente la tipología que pide un
lucernario sobre zona ocupada.

---

## 3. Ficha 3 — AGC SunEwat Vision

**Por qué encaja:** enfoque distinto a los dos anteriores. AGC no es un fabricante de módulos
que hace vidrio: es uno de los mayores **fabricantes de vidrio plano del mundo** que hace
módulos. El producto se entrega como vidrio arquitectónico, con la cadena de suministro y el
servicio técnico de un vidriero. Célula **PERC monocristalina**, ambas hojas de vidrio
**termotratado**, y densidad de potencia comparable a la ficha 1.

**Fuente:** AGC, *SunEwat — The Perfect Balance Between Efficiency And Aesthetics*, ref.
EN-08/2023 — <https://agc-glassasia.com/wp-content/uploads/2023/09/SunEwat_Brochure_0923_EN-Asia.pdf>

| Parámetro | Valor | Nota |
| --- | --- | --- |
| Fabricante / país | AGC Glass (grupo AGC, Japón; AGC Glass Europe, Bélgica) | |
| Gama | **SunEwat Vision** (semitransparente) | Las otras gamas —Origin, Colour, Design— son opacas |
| Tecnología | Células **PERC monocristalinas** | |
| Composición | Vidrio termotratado + intercalario + vidrio termotratado bajo en hierro | Composición de principio; espesores no publicados |
| **Potencia** | **máx. 180 Wp/m²** | «Typical Wp/m²: Max. 180» |
| Aplicaciones declaradas | Fachadas, marquesinas, parasoles, barandillas, lamas, spandrels, **cubiertas**, pantallas acústicas, carports | |
| Certificaciones | **IEC 61215, IEC 61730, EN 13501** | |
| Garantía de producto | Delaminación del vidrio **10 años**; condensación interna de la UGU **10 años\*** | |
| Garantía de potencia | **90 % años 1-10; 80 % años 11-20** | Mejor que la de Onyx |
| Referencia en lucernario | Dulwich College, Singapur — «Application: Skylight, Facade Fins», producto SunEwat Vision | |

> **⚠ Limitación que hay que poner encima de la mesa.** El asterisco de la garantía de
> condensación interna de la UGU remite a: **«\*Vertical application only.»** Es decir, **AGC
> excluye expresamente de esa garantía la aplicación no vertical**. Para un lucernario
> horizontal —que es exactamente nuestro caso— la garantía de estanqueidad de la cámara
> **no aplica tal cual**. Hay que negociarla por proyecto o renunciar a la UGU.

**Huecos de esta ficha (NO VERIFICADO):**
- Espesores concretos del laminado y tipo de intercalario (PVB vs EVA) — el folleto no lo dice.
- **Opciones de VLT y g/SHGC** — no publicadas. Es el hueco más grave: sin g no se puede
  sostener el argumento térmico con esta ficha.
- Transmitancia U, dimensiones máximas del vidrio, Voc/Isc/Vmpp/Impp, eficiencia,
  coeficiente de temperatura — ninguno publicado en el folleto.
- EN 12600, EN 14449, marcado CE como producto de construcción — no mencionados.
- El folleto descargado es el de **AGC Asia Pacific**. Para España habría que pedir la
  documentación de **AGC Glass Europe**, que puede diferir.

Esta ficha está, por tanto, **incompleta a propósito**: publico lo que AGC publica y no
relleno el resto. Para llevar AGC al TFM haría falta pedirles la ficha técnica firmada.

---

## 4. Verificación normativa: qué exige realmente el CTE

El encargo daba por sentado que «*el CTE DB-SE y DB-SUA exigen laminado en vidrio sobre
zonas ocupadas*». **He ido al articulado y la afirmación, tal como está formulada, no se
sostiene.** El resultado sigue siendo que hace falta laminado, pero por otra vía — y esto
importa porque cambia el artículo que hay que citar en la memoria.

### 4.1 Lo que dice el DB-SUA

**Fuente primaria:** CTE, *DB-SUA Seguridad de utilización y accesibilidad*, sección SUA 2,
apdo. 1.3 — <https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf>

El apdo. 1.3 «Impacto con elementos frágiles» exige la clasificación X(Y)Z de la
UNE-EN 12600:2003 **solo en las «áreas con riesgo de impacto»**, y define esas áreas de
forma tasada (punto 2 del mismo apartado):

> «*a) en puertas, el área comprendida entre el nivel del suelo, una altura de 1,50 m y una
> anchura igual a la de la puerta más 0,30 m a cada lado de esta;
> b) en paños fijos, el área comprendida entre el nivel del suelo y una altura de 0,90 m.*»

**Un lucernario horizontal no es ninguna de las dos.** El riesgo que regula SUA 2 §1.3 es el
de **una persona que impacta contra el vidrio**, no el de un vidrio que cae sobre las
personas. Lo confirma el documento de apoyo oficial:

**Fuente primaria:** *DA DB-SUA/1 — Clasificación de los vidrios según sus prestaciones frente
a impacto y su forma de rotura según la norma UNE-EN 12600:2003*, Ministerio de Fomento,
junio 2011 — <https://www.upv.es/contenidos/CADIVALT/info/CTEDADBSUA1.pdf>

> «*La prestación exigida en el apartado 1.3 de la sección SUA 2 pretende limitar tanto el
> riesgo de corte sobre el usuario como la posible caída de éste desde un desnivel mayor a
> 55 cm cuando se produzca la rotura de un vidrio.*»

Es decir: corte al usuario y **caída del usuario**. No contempla la caída de fragmentos.

La tabla 1.1 de SUA 2 §1.3, para desnivel entre 0,55 m y 12 m, exige Y = B o C y Z = 1 ó 2.
Y el DA DB-SUA/1 §5 lo ejemplifica: «*Los vidrios del tipo 2(B)2 ó 1(C)2 podrían utilizarse
en zonas con desnivel entre 0,55 y 12 m*». Ambas configuraciones de capa fina de Onyx
cumplirían ese umbral (2(B)2 la 3+4; 1(B)1 la 6T+3+6T).

### 4.2 De dónde viene entonces la exigencia de laminado en cubierta

- **DB-SE / DB-SE-AE** cubren la capacidad portante frente a acciones (viento, nieve,
  mantenimiento), no la retención de fragmentos.
  El DB-SE-AE §3.1.1 sí obliga a considerar, además de la sobrecarga uniforme, **una carga
  concentrada aplicada en cualquier punto** sobre una superficie cuadrada de 50 mm de lado
  para los usos distintos de tráfico y aparcamiento
  (<https://www.codigotecnico.org/pdf/Documentos/SE/DBSE-AE.pdf>). Es la carga que gobierna
  el vidrio del lucernario en mantenimiento.
- **La exigencia explícita de laminado en acristalamiento horizontal o inclinado sobre zona
  ocupada: NO VERIFICADO en el CTE.** No la he localizado en el articulado del DB-SUA ni del
  DB-SE-AE. En la práctica española se resuelve por norma UNE de producto y por prescripción
  facultativa, no por un artículo del CTE. **Recomiendo que Mario lo consulte con el tutor
  antes de redactar el capítulo**: escribir «lo exige el CTE DB-SUA» sin más sería una cita
  que un tribunal puede pedir que se localice, y no está donde parece.
- La norma **UNE 85247** («acristalamientos en posición horizontal o inclinada») aparece
  citada en literatura sectorial pero **no he podido verificar su vigencia ni su contenido**:
  no es de acceso libre. **NO VERIFICADO — pendiente de acceso a AENOR.**

### 4.3 El punto que sí es decisivo: PVB frente a EVA

**Fuente:** BauNetz Wissen, *PV in Überkopfverglasungen* —
<https://www.baunetzwissen.de/solar/fachwissen/pv-am-gebaeude/pv-in-ueberkopfverglasungen-165778>

En la práctica constructiva centroeuropea, para acristalamiento en cubierta (*Überkopf­verglasung*):

- Se exigen **módulos vidrio-vidrio** laminados.
- **Solo el laminado con PVB** (polivinilbutiral) tiene aprobación de base como
  acristalamiento en cubierta.
- Para los módulos que usan **EVA** como intercalario, «*las autoridades conceden por regla
  general una autorización individual*» (*Einzelgenehmigung*).

**Consecuencia directa sobre la ficha 1.** El cristalino estándar de Onyx se lamina con
**1,80 mm de EVA**. La gama de capa fina ofrece las dos opciones (ref. A: 0,90 mm EVA;
ref. B: 1,52 mm PVB) y **los dos lucernarios ejecutados que he documentado usan PVB**
(Bell Works 3,04 mm; Alcalá 33 1,52 mm ×2). No es casualidad.

→ **Acción concreta:** preguntar a Onyx si sirven la gama cristalina con **PVB en lugar de
EVA**. Si la respuesta es sí, V1a se cierra con c-Si y se conservan los ~49 kWp. Si es no,
hay que elegir entre potencia (EVA, autorización caso a caso) y tramitación limpia (PVB,
capa fina, ~13 kWp). Es **la pregunta que desbloquea la variante**.

*Nota de alcance:* este marco (*abZ* / autorización individual) es alemán-austríaco. Su
traslación literal a España **NO ESTÁ VERIFICADA**; lo traigo porque es el criterio técnico
que siguen los fabricantes europeos y porque explica la elección de encapsulante de los dos
proyectos reales. No debe citarse en el TFM como si fuera normativa española.

### 4.4 Un fabricante que directamente no encaja

**Megasol Energie AG** (Suiza) fabrica módulos vidrio-vidrio de alta calidad, pero su manual
de montaje de módulos enmarcados dice literalmente:

> «*Der Einsatz von Megasol Solarmodulen mit U-Rahmen als **Überkopfverglasung ist nicht
> zulässig**. Bei Dachmontage dürfen diese Solarmodule nur über einer feuerbeständigen
> Dachabdeckung montiert werden.*»
>
> — Megasol, *Installations- und Montageanleitung gerahmte Hochleistungsmodule*, p. 11,
> <https://megasol.ch/wp-content/uploads/2022/06/Megasol_Installation-und-Montagenleitung_Uxx_052022.pdf>

El uso como acristalamiento en cubierta **no está permitido** para sus módulos enmarcados, y
en cubierta solo pueden montarse sobre una cubierta resistente al fuego. El mismo manual
recomienda una **inclinación mínima de 15°** para la limpieza natural por lluvia (p. 12).
Descartado para V1a en esa configuración.

---

## 5. Proyecto de referencia — Bell Works (antiguo Bell Labs), Holmdel, Nueva Jersey

Elegido sobre las alternativas españolas porque es **el único caso documentado que replica la
operación exacta de V1a: sustituir el vidrio de un lucernario existente conservando su
estructura**. Además su escala permite extrapolar.

### 5.1 Datos del proyecto

| Dato | Valor | Fuente |
| --- | --- | --- |
| Edificio | Bell Labs Holmdel Complex, **Eero Saarinen, 1962** | [Facades+](https://facadesplus.com/eero-saarinens-bell-labs-stays-bright-with-the-largest-photovoltaic-skylight-in-the-u-s/) |
| Promotor | Somerset Development (compra en 2013) | Facades+ |
| Arquitecto de la rehabilitación | Alexander Gorlin Architects | [Architectural Record](https://www.architecturalrecord.com/articles/14447-bell-works-by-alexander-gorlin-architects) |
| Suministrador del vidrio FV | Onyx Solar (Ávila) | [Solar Power World](https://www.solarpowerworldonline.com/2018/04/bell-works-onyx-solar-skylight-case-study/) |
| Instalador / electricidad | Abender Electric | Solar Power World |
| Superficie de vidrio FV | **60.000 sq ft ≈ 5.574 m²** | Facades+ |
| Nº de vidrios | **3.200 paños**, en **24 acristalamientos distintos** | Facades+ |
| Potencia instalada | **175 kW** nominales | Solar Power World |
| VLT | **20 %** | Facades+ |
| Tecnología | a-Si capa fina laminada entre dos vidrios templados de seguridad | Facades+ |
| Inversores | 12 unidades SMA | Solar Power World |
| Plazo de instalación del vidrio | ~7 meses | Facades+ |
| Año | Obra 2017; el complejo entra en el National Register of Historic Places en junio de 2017 | Facades+ |

**Verificación cruzada de coherencia (cálculo propio):**
3.200 paños × 1,67 m²/paño (ficha GL.01a) = **5.344 m²** ≈ los 5.574 m² declarados.
3.200 × 57 Wp = **182,4 kWp** ≈ los 175 kW declarados.
175 kW / 5.574 m² = **31,4 Wp/m²**, coherente con los 34,0 Wp/m² de ficha para VLT 20 %.
Las tres cifras publicadas son mutuamente consistentes. **Fuente fiable.**

> **⚠ Error detectado en las fuentes.** Tanto Facades+ como Archpaper afirman que la
> instalación «*annually generates nearly 90 kilowatt hours*». Es un error de unidades
> evidente: 90 kWh/año para 175 kWp es absurdo (sería ~0,5 kWh/kWp·año). **No usar esa
> cifra.** La producción anual real del proyecto **NO ESTÁ VERIFICADA**: no he encontrado
> ninguna fuente que la publique correctamente.

### 5.2 Sistema constructivo — lo que sí está documentado

Este es el punto que más interesa a Mario, y la respuesta es notablemente sencilla:

> «*Replacing the windows was fairly straightforward; the original glass was removed, then
> the existing frames were cleaned and then fitted with advanced weather strips to seal the
> building-integrated photovoltaics.*»
> — Facades+ (URL arriba)

Es decir: **se retiró el vidrio original, se limpió la perfilería existente y se recibió el
vidrio fotovoltaico sobre ella con juntas de estanqueidad nuevas.** No hubo sistema de
soporte nuevo. El lucernario se resuelve **en las carpinterías que ya estaban**, dispuestas
en formaciones de caballete (*«assembled in a series of ridges»*), lo que da la pendiente de
evacuación sin necesidad de modificar geometría.

**Logística de montaje.** El riesgo real del proyecto no fue estructural sino de trazabilidad:
con 24 acristalamientos distintos, cada paño tenía que ir a su bahía y fila exactas.

> «*we created a model of each of the three sky roofs and identified every glazing and the
> position of the glazing with each bay and row of the sky roof. This model ensured we had
> the exact number of each glazing and the respective permanent position of the skyroof.*»
> — Joel Shandelman, CTO de Bell Works, en Facades+

**Cableado.** Cajas de conexión pequeñas visibles desde abajo, con conectores estándar
**MC4**; el cableado se ocultó **por una bandeja preexistente bajo los paños de vidrio**,
formando varias series («*plug-and-play system*»), hasta 12 inversores SMA
([Solar Power World](https://www.solarpowerworldonline.com/2018/04/bell-works-onyx-solar-skylight-case-study/)).
Es decir: **salida por el canto, recogida bajo el vidrio, no por dentro del montante.**

### 5.3 Lo que este proyecto NO documenta

Honestamente, la mayor parte de lo que pedía el encargo sobre estructura **no está publicado**:

- **NO VERIFICADO:** fabricante y designación del sistema de perfilería (era la carpintería
  original de 1962; ni Saarinen ni la rehabilitación publican el sistema).
- **NO VERIFICADO:** si hay rotura de puente térmico. Dada la fecha (1962), es
  razonablemente improbable, pero no lo afirmo.
- **NO VERIFICADO:** justificación de cargas de viento y nieve, y cómo se absorbió el
  sobrepeso. Es un dato relevante: el vidrio FV pesa **28,0 kg/m²** (GL.01a) frente a los
  ~20-25 kg/m² de un laminado convencional equivalente. El artículo no menciona refuerzo
  estructural, lo que sugiere que el incremento fue asumible por la estructura existente,
  **pero eso es inferencia mía, no dato publicado.**
- **NO VERIFICADO:** protocolo de sustitución de un vidrio roto y de mantenimiento.
- **NO VERIFICADO:** cifras de ahorro térmico o de reducción de deslumbramiento. Las fuentes
  afirman cualitativamente que el VLT del 20 % «reduce la ganancia solar», sin cuantificarlo.

**Alternativa española, por si el tribunal prefiere un caso nacional:** *Alcalá 33, Madrid*
(rehabilitación de edificio de 1900 del Conjunto Histórico Villa de Madrid, nueva sede de
Reny Picot, proyecto de Díaz & Díaz Arquitectos; 12 vidrios FV de 2.438 × 1.160 mm con
cámara de aire en el lucernario central sobre la escalera)
— <https://onyxsolar.com/photovoltaic-skylight-alcala-33> y
<https://www.diazydiazarquitectos.com/proyectos/rehabilitacion-reforma-y-cambio-de-uso-edificio-en-alcala-33-madrid/>.
Tiene **ficha técnica firmada** (§2.3) y es español, pero es de escala muy pequeña
(1.222,67 m² construidos en total) y **su sistema constructivo no está publicado en absoluto**.

> **Discrepancia entre fuentes que dejo señalada, no resuelta.** La página de proyecto de
> Onyx dice que los vidrios de Alcalá 33 miden **2.438 × 1.160 mm**, mientras que la ficha
> técnica firmada del mismo proyecto dice **1.110 × 2.140 mm**. No son el mismo vidrio.
> Puede que la ficha corresponda a una de varias tipologías, o que la web esté desactualizada.
> **He usado la ficha firmada, no la web**, por ser el documento técnico. Conviene
> confirmarlo con Onyx si el dato entra en el TFM.

---

### 5.4 Contraste con el detalle constructivo del CIEMAT (material interno del proyecto)

Bell Works documenta *qué se hizo*, pero no publica el despiece. Ese hueco lo cubre en parte
material que ya está en el propio proyecto: la presentación **«Integración de Fotovoltaica en
Edificios» (Nuria Martín Chivelet, CIEMAT, 2025)**, resumida en
`conocimiento fotovoltaico/Referencia/integracion-fotovoltaica-en-edificios-bipv.md`, incluye
en su apartado de **cubiertas acristaladas** (diapositivas 47-56) un detalle constructivo con
**ocho elementos**:

1. montantes y travesaños de aluminio;
2. separadores de puente térmico;
3. el módulo fotovoltaico;
4. la salida de cableado;
5. fijación con **silicona estructural**;
6. juntas selladas con **silicona neutra**;
7. cableado interno conducido **por los montantes**;
8. el conjunto resuelto como muro cortina adaptado a cubierta.

**Dónde coincide y dónde no con Bell Works.** Coincide en la tipología general —perfilería de
aluminio de montantes y travesaños— y en la estanqueidad por juntas de silicona neutra.
**Discrepa en el cableado**: el detalle del CIEMAT lo conduce *por dentro del montante*,
mientras que Bell Works lo recogió en *bandeja bajo los paños* (§5.2). Las dos soluciones son
válidas y la elección no es menor en un CPD: la variante por montante deja el cable fuera de
la sala, lo que es preferible frente al DB-SI y frente a los criterios de incendios del propio
centro de datos; la variante por bandeja es más barata y mucho más fácil de mantener, pero
mete cableado de continua sobre la sala técnica. **Conviene decidirlo explícitamente y
justificarlo**, no heredarlo del proyecto de referencia sin más.

**Marco normativo específico de BIPV que falta en el análisis del §4.** El CTE regula al
edificio, pero el módulo integrado tiene norma propia: **UNE-EN 50583 partes 1 y 2** (Europa)
e **IEC 63092 partes 1 y 2** (internacional), además del Reglamento de Productos de la
Construcción y la Directiva de Baja Tensión. Estas normas son las que exigen al módulo BIPV
cumplir simultáneamente las funciones constructivas —rigidez mecánica, protección frente a
lluvia/nieve/viento/granizo, sombreado e iluminación natural, aislamiento térmico, protección
contra incendios, protección acústica y separación entre ambientes— además de generar.
**Es previsiblemente la vía correcta para justificar el vidrio del lucernario en la memoria**,
más que forzar una cita del DB-SUA que, como se ha visto en §4.1, no dice lo que se le
atribuye. Queda **pendiente de verificar el articulado literal de la EN 50583-2**, que no se
ha consultado en este informe: se apunta como línea, no como conclusión.

*Fuente interna:* resumen de la presentación del CIEMAT ya indexado en el proyecto
(diapositivas 15, 19, 20 y 47-56). Es material **no citable** en el TFM sin verificación
adicional (regla 10 de CLAUDE.md), pero sirve como orientación técnica.

---

## 6. Tabla comparativa de las tres fichas

| | **1. Onyx c-Si** | **2. Onyx a-Si + PVB** | **3. AGC SunEwat Vision** |
| --- | --- | --- | --- |
| País | España (Ávila) | España (Ávila) | Bélgica / Japón |
| Tecnología | 6″ Mono 158 c-Si, separación entre células | a-Si capa fina | PERC monocristalina |
| Enfoque | Fabricante BIPV especialista | Fabricante BIPV especialista | Fabricante global de vidrio plano |
| **Wp/m²** | **115,0 – 178,2** (publicado) | **28,0 – 57,6** (publicado) | **máx. 180** (publicado) |
| VLT | 11 – 43 % (= grado de transparencia) | 0,2 – 28,4 % (EN 410) | NO VERIFICADO |
| **Factor solar g** | **NO VERIFICADO** | 22 – 41 % monolítico; **17 % en UGU** | **NO VERIFICADO** |
| **U (W/m²·K)** | 5,2 monolítico; **1,0** UGU 12/4/12 argón | 5,7 (3+4) / 5,2 (6T+3+6T); **1,5** UGU | NO VERIFICADO |
| Encapsulante | **EVA 1,80 mm** ⚠ | **PVB** (opción B) ✅ | NO VERIFICADO |
| EN 12600 | «según configuración» | **2(B)2 / 1(B)1** publicado | NO VERIFICADO |
| Coef. temp. Pmpp | −0,32 %/°C | −0,19 %/°C | NO VERIFICADO |
| Garantía producto | **5 años** | 5 años | **10 años** |
| Garantía potencia | 80 % / 10 años | 80 % / 10 años | **90 %/10 a. + 80 %/20 a.** |
| Ref. en lucernario | No documentada | **Bell Works, Alcalá 33** | Dulwich College (Singapur) |
| Ficha firmada disponible | Guía técnica | **Sí, dos de proyecto** | No |
| **Sobre 378 m²** | **43,5 – 67,4 kWp** | **10,6 – 21,8 kWp** | ~68 kWp teóricos |

### Precio

**No hay precio público verificable para ninguno de los tres productos.** Ni Onyx, ni AGC, ni
Megasol publican tarifa; el vidrio FV se cotiza siempre por proyecto (superficie, número de
tipologías, transparencia, composición). **No invento un rango.** Para el capítulo económico
hay dos vías legítimas: (a) pedir oferta a Onyx —tienen delegación en Ávila y herramientas de
estimación en su web, <https://onyxsolar.com/resources/documentation>—, o (b) tomar el coste
de un TFM de referencia y declararlo como tal. Lo que no se puede es poner una cifra €/m²
sin origen.

---

## 7. Lecciones para el TFM

### 7.1 Qué módulo recomendaría para V1a

**Recomendación: Onyx Solar, gama cristalina, con grado de transparencia ~35 %, y con la
pregunta del PVB hecha al fabricante antes de cerrar el capítulo.**

Los motivos, por orden de peso:

1. **Es la única opción que cumple el objetivo de potencia con dato publicado.** 129,6 Wp/m²
   × 378 m² = **49,0 kWp**, frente a los ~47 kWp de la hipótesis. No hay que interpolar ni
   estimar: es una fila de una ficha técnica.
2. **La capa fina queda descartada por aritmética.** A 34,0 Wp/m² (VLT 20 %) el tragaluz da
   12,9 kWp. Ni siquiera opaca al 0 % (57,6 Wp/m²) llegaría a 22 kWp. Si el TFM mantiene la
   cifra de 47 kWp, la capa fina **no es una alternativa, es un error de dimensionado**.
3. **Fabricante español con planta en Ávila**, lo que refuerza el argumento de proximidad y
   facilita pedir documentación y oferta real para el capítulo económico.
4. **La ficha 3 (AGC) no puede sostener el argumento térmico** que es la justificación
   declarada de V1a: sin g ni U publicados, no se puede escribir el apartado de reducción de
   carga térmica. Queda como alternativa de contraste, no como opción de proyecto.

**Condición que hay que resolver antes de darlo por bueno:** el cristalino estándar usa EVA.
Hay que preguntar a Onyx por la variante con PVB (§4.3). Es una pregunta de una línea con
consecuencias grandes: si la respuesta es negativa, V1a cae en el dilema potencia-vs-tramitación
y habría que rehacer el dimensionado con capa fina y renunciar al 2 % de cobertura.

**Sobre la hipótesis de VLT.** Recomiendo **cambiar VLT 20 % → ~35 %** y mantener los ~47 kWp.
Razones: (a) reproduce exactamente una fila publicada, sin interpolar; (b) un tragaluz con
VLT 35 % sigue dando control solar muy notable frente a un vidrio convencional; (c) evita
tener que defender un número interpolado ante el tribunal. Y hay que **dejar de usar
«VLT 20 %» y «grado de transparencia 20 %» como sinónimos**: la tabla de la §2.2 demuestra
que un vidrio nominal al 20 % transmite 16-17 % según EN 410.

**Sobre el argumento térmico, que es la justificación real de V1a.** El dato que lo sostiene
es el factor solar. Verificado tengo **g = 17 % en la UGU de Alcalá 33** con Ug = 1,5 W/m²·K.
Frente a un lucernario convencional (g típicamente 0,6-0,7 — **valor de referencia NO
VERIFICADO, hay que sacarlo de la ficha del vidrio actual del CPD o del CTE DB-HE**), la
reducción de la ganancia solar por el tragaluz es de en torno a un factor 4. **Ese es el
número que hace fuerte a V1a**, no los 76 MWh/año. Pero falta el equivalente para el
cristalino: **hay que pedir a Onyx el g de la configuración cristalina elegida.** Sin ese
dato el capítulo se queda cojo por el lado que más importa.

### 7.2 Qué implica el sistema estructural de Bell Works para nuestros 472 m²

La lección de Bell Works es tranquilizadora y desplaza el foco del problema:

1. **No hace falta un sistema de soporte nuevo.** En Bell Works se reutilizó la perfilería
   original de 1962: se desmontó el vidrio, se limpió el marco y se recibió el vidrio FV con
   juntas de estanqueidad nuevas. Para el CPD esto significa que **la primera tarea no es
   diseñar un muro cortina de cubierta, sino levantar el estado actual del lucernario**:
   sistema de perfilería, galce disponible, espesor máximo admisible y estado de las juntas.
   Si el galce actual admite el espesor del vidrio FV, V1a es una **sustitución de vidrio**,
   no una obra de estructura. Y eso cambia por completo el capítulo de presupuesto.
2. **El espesor es la restricción de encaje, no el peso.** Los tres candidatos van de
   9,8 mm (c-Si monolítico) a 35,76 mm (UGU de Alcalá 33). Un galce dimensionado para un
   laminado convencional de 6+6 probablemente admita el c-Si de 9,8 mm sin tocar nada,
   **pero casi con seguridad no admita una UGU de 35,76 mm**. Aquí hay un conflicto directo
   con el argumento térmico: la UGU es la que da Ug 1,5 y g 17 %, y es la que no cabe.
   **Es la segunda decisión de proyecto de V1a, y conviene tomarla explícitamente.**
3. **El sobrepeso es menor de lo que parece.** 28,0 kg/m² (Bell Works) o ~20 kg/m² (c-Si
   monolítico) frente a un laminado convencional. En Bell Works no consta refuerzo alguno.
   Aun así, sobre 472 m² hay que **verificar la estructura existente con el DB-SE-AE**,
   incluyendo la carga concentrada de mantenimiento sobre 50 mm de lado del §3.1.1.
4. **La pendiente ya la da la geometría existente.** Bell Works resolvió el drenaje con la
   disposición en caballetes que ya tenía el edificio. Hay que **medir la pendiente actual
   del tragaluz del CPD** y contrastarla con el mínimo de limpieza natural por lluvia
   (Megasol recomienda 15° para sus módulos; Onyx no publica mínimo — **NO VERIFICADO**).
   Un tragaluz casi horizontal acumulará suciedad y penalizará la producción de forma
   permanente: es un dato que debe entrar en el PR de la simulación PVsyst.
5. **El cableado se resuelve por debajo, no por dentro del montante.** Bell Works usó cajas
   IP65 con conectores MC4 y una bandeja bajo los vidrios. En un CPD esto tiene una
   implicación que no aparece en ninguna de las fuentes y que conviene pensar: **hay cableado
   de continua discurriendo sobre la sala**. Cabe revisarlo contra el DB-SI y contra los
   criterios de protección contra incendios propios del CPD. El vidrio de Onyx declara
   reacción al fuego **B-s1,d0** (EN 13501-1), que es un buen punto de partida.
6. **La verdadera dificultad es logística, no técnica.** Con 24 tipologías distintas, Bell
   Works necesitó un modelo que asignara cada paño a su bahía y fila. Los 472 m² del CPD
   tendrán muchas menos tipologías, pero **conviene contar el número de paños distintos**
   desde el principio: es lo que dispara el coste y el plazo.

### 7.3 Preguntas abiertas que hay que cerrar con datos, no con supuestos

| # | Pregunta | A quién |
| --- | --- | --- |
| 1 | ¿Sirven la gama cristalina laminada con **PVB** en lugar de EVA? | Onyx Solar |
| 2 | **Factor solar g y U** de la configuración cristalina elegida (falta el dato que sostiene el argumento térmico) | Onyx Solar |
| 3 | ¿Tienen **marcado CE como producto de construcción** (EN 14449 / EN 1279)? | Onyx Solar |
| 4 | **Inclinación mínima** admitida y garantía en posición horizontal | Onyx Solar |
| 5 | Estado actual del lucernario: sistema de perfilería, **espesor máximo de galce**, pendiente real, tipologías de paño | Levantamiento en obra / Mario |
| 6 | **g del vidrio actual** del tragaluz, para cuantificar la mejora | Ficha del vidrio existente |
| 7 | ¿Exige el CTE laminado en acristalamiento de cubierta sobre zona ocupada, y **en qué artículo**? | Tutor (Julio Amador) |
| 8 | Vigencia y contenido de **UNE 85247** | AENOR / biblioteca UPM |
| 9 | **Precio** por m² del vidrio FV | Oferta a Onyx o TFM de referencia |
| 10 | Articulado literal de **UNE-EN 50583-2 / IEC 63092-2**: ¿es esta la vía correcta para justificar el vidrio del lucernario, en lugar del DB-SUA? | AENOR / biblioteca UPM |

---

## 8. Índice de fuentes

**Fichas técnicas y documentación de fabricante**
1. Onyx Solar, *Technical Guide* (rev. 260630, 42 pp., ES/EN) — <https://onyxsolar.com/images/3.resources/Technical_guide_EN-ES_300626.pdf>
2. Onyx Solar, ficha de proyecto Bell Works GL.01a/GL.01b — <https://onyxsolar.com/images/5.projects/108.bell_works_us/bell-works-skylight-onyx-solar-pv-glass-photovoltaics-bipv-specs.pdf>
3. Onyx Solar, ficha de proyecto Alcalá 33 — <https://onyxsolar.com/images/5.projects/144.alcala-33/alcala-33-curtain-wall-onyx-solar-pv-glass-photovoltaics-bipv-data.pdf>
4. AGC, *SunEwat* brochure EN-08/2023 — <https://agc-glassasia.com/wp-content/uploads/2023/09/SunEwat_Brochure_0923_EN-Asia.pdf>
5. Megasol, *Installations- und Montageanleitung gerahmte Hochleistungsmodule* (05/2022) — <https://megasol.ch/wp-content/uploads/2022/06/Megasol_Installation-und-Montagenleitung_Uxx_052022.pdf>
6. Onyx Solar, aplicación lucernarios — <https://onyxsolar.com/building-applications/photovoltaic-skylight>
7. Onyx Solar, documentación y herramientas — <https://onyxsolar.com/resources/documentation>

**Normativa (fuente primaria)**
8. CTE, *DB-SUA* — <https://www.codigotecnico.org/pdf/Documentos/SUA/DBSUA.pdf>
9. CTE, *DA DB-SUA/1* (clasificación de vidrios, UNE-EN 12600) — <https://www.upv.es/contenidos/CADIVALT/info/CTEDADBSUA1.pdf>
10. CTE, *DB-SE-AE* — <https://www.codigotecnico.org/pdf/Documentos/SE/DBSE-AE.pdf>

**Proyecto de referencia**
11. Facades+ / The Architect's Newspaper (2019) — <https://facadesplus.com/eero-saarinens-bell-labs-stays-bright-with-the-largest-photovoltaic-skylight-in-the-u-s/>
12. Solar Power World (2018) — <https://www.solarpowerworldonline.com/2018/04/bell-works-onyx-solar-skylight-case-study/>
13. Architectural Record (2020) — <https://www.architecturalrecord.com/articles/14447-bell-works-by-alexander-gorlin-architects>
14. Onyx Solar, Bell Works — <https://onyxsolar.com/bell-works>
15. Onyx Solar, Alcalá 33 — <https://onyxsolar.com/photovoltaic-skylight-alcala-33>
16. Díaz & Díaz Arquitectos, Alcalá 33 — <https://www.diazydiazarquitectos.com/proyectos/rehabilitacion-reforma-y-cambio-de-uso-edificio-en-alcala-33-madrid/>

**Referencia técnica**
17. BauNetz Wissen, *PV in Überkopfverglasungen* — <https://www.baunetzwissen.de/solar/fachwissen/pv-am-gebaeude/pv-in-ueberkopfverglasungen-165778>
18. **(Interna, no citable)** N. Martín Chivelet, *Integración de Fotovoltaica en Edificios*, CIEMAT, 2025 — resumen indexado en `conocimiento fotovoltaico/Referencia/integracion-fotovoltaica-en-edificios-bipv.md` (detalle constructivo de cubierta acristalada, diapositivas 47-56; normas UNE-EN 50583 e IEC 63092, diapositiva 20).

**Fabricantes consultados sin ficha técnica verificable**
- **ertex solar** (Austria): fabrica módulos VSG y VSG-ISO para cubierta acristalada y declara que el montaje se resuelve «*mit Klemmleisten an den Glaskanten*» (con perfiles de presión en los cantos del vidrio), con la subestructura y el montaje a cargo de la obra (<https://www.ertex-solar.at/angebot/isolierendes-dach/>). **No publica fichas técnicas descargables**: el índice de descargas (<https://www.ertex-solar.at/ertexdownload/broschueren/>) no expone PDF y el catálogo de ArchiExpo está tras protección anti-bot. Un dato de terceros (~116 Wp/m², 40 kg/m², mono, PVB, EN 61215/61730 — <https://solarchitecture.ch/ertex-solar-vsg-laminated-safety-glass-module/>) corresponde a un módulo **opaco con impresión cerámica**, no al semitransparente: **no aplicable**. Es un candidato serio para V1a por su enfoque de constructor de vidrio, pero **hay que pedirle la ficha directamente**.
- **Metsolar** (Lituania): fabrica vidrio-vidrio semitransparente a medida (<https://metsolar.eu/products/met-glass-glass/>) pero **no publica ninguna cifra de Wp/m² ni ficha descargable**. Descartado por no verificable.
