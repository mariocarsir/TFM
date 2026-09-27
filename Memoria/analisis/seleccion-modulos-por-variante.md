---
title: "Selección del módulo fotovoltaico por variante (V1a, V1b, V2, V3)"
tipo: analisis-tecnico
autor: ingeniero-dominio
fecha: 2026-09-27
estado: propuesta (pendiente de validación por Mario)
fase_erma: "Fase 3 — Selección del módulo"
sustituye_a: "Memoria/analisis/comparacion-modulos-fv.md (22/09/2026)"
tags: [modulo-fv, seleccion, BIPV, lucernario, cubierta, lastrado, poliurea, marquesinas, planta-suelo, V1a, V1b, V2, V3, PVsyst, ranking]
---

# Selección del módulo fotovoltaico por variante

> **Regla aplicada.** Toda cifra de ficha técnica lleva su fuente (numeradas en §9). Lo que no se
> ha podido verificar figura como **no verificado**. Nada procede de la memoria del modelo. Las
> puntuaciones son cálculo propio con el método de Arcas (1 = peor, N = mejor, empates a media) y
> se pueden rehacer si Mario cambia criterios o pesos. Los cálculos de densidad, kWp y longitud de
> string están en `Memoria/analisis/scripts/modulos_por_variante.py`.
>
> **Qué cambia respecto al 22/09.** Se abandona la idea de un módulo opaco único para V1b, V2 y V3.
> Cada variante define sus propios criterios, compara tres candidatos de su misma clase y elige. El
> argumento de los 1500 V, que en el documento anterior pesaba a favor de AIKO pensando en la V3,
> **deja de contar en la cubierta y en las marquesinas**, donde el inversor será de 1100 V.

## 0. Resultado en una tabla

| Variante | Módulo elegido | Reserva | Razón en una línea |
| --- | --- | --- | --- |
| **V1a** lucernario (BIPV) | **Onyx Solar c-Si, 35 % de transparencia** (182 Wp, 1650 × 850 mm) | Polysolar PS-MC-ST-60 (solo con transparencia ≥ 20 % confirmada) | **Sin cambios.** Ya se eligió con criterios propios de V1a (función de lucernario) |
| **V1b** cubierta plana, sheds lastrados | **AIKO Neostar 2P 475 W monovidrio** (AIKO-A475-MAH54Mw) | REC Alpha Pure-RX 470 | Máxima densidad en una variante limitada por superficie y strings largos (menos entradas DC); REC queda de reserva por su robustez mecánica, su clase BROOF(t2) y su PAN ya probado |
| **V2** marquesinas | **AIKO Neostar 2P+ 475 W vidrio-vidrio** (AIKO-A475-MAH54Dw) | Trina Vertex S+ TSM-440NEG9RC.27 (bifacial) | Vidrio-vidrio 2 + 2 mm con fuego clase A sobre vehículos y +8 % de kWp en la misma huella; Trina gana por puntos comerciales y es la opción si la simulación bifacial da más del ~8 % |
| **V3** planta en suelo | **LONGi Hi-MO 9 LR8-66HYD-670M** (bifacial, 2382 × 1134 mm) | JA Solar JAM66D45-630/LB | Los tres candidatos son AAA; LONGi gana en coeficiente de temperatura, degradación y garantía; JA declara compatibilidad con seguidor |

**Coincidencia V1b-V2.** Sale el mismo fabricante y la misma célula ABC en las dos variantes, pero
**no el mismo producto**: monovidrio 3,2 mm en la cubierta, vidrio-vidrio 2 + 2 mm en la marquesina.
Los criterios que llevan a cada uno son distintos (§3.4 y §4.5). Las dos versiones tienen los mismos
parámetros eléctricos, lo que permite reutilizar el diseño de strings (§6).

**Desviación respecto al Módulo 6.** El REC Alpha Pure-RX 470 que corrigió el tutor **no se
confirma en ninguna variante**, pero vuelve como reserva de V1b, que es precisamente la cubierta del
trabajo previo. La razón por la que REC cae ya no es su tensión de 1000 V pensando en la V3: en V1b
cae por densidad (−5,4 % de kWp en la misma superficie) y por strings de 14 módulos frente a 24, que
multiplican las entradas DC. Hay que escribirlo así en la memoria.

---

## 1. Método común

- **Formato de tabla:** filas de la diapositiva 16 de la guía ERMA (potencia, tecnología de célula,
  coeficiente de temperatura, LID, PID, garantías, características especiales, ranking, precio) más
  las filas propias de cada variante (§2.1, §3.1, §4.1, §5.1).
- **Puntuación:** método de Arcas, cap. 4.3 de `TFM_M_A.pdf` (pp. 16-17): valor de 1 a N por
  criterio, candidatos de la misma clase de potencia y de fabricantes bien posicionados.
- **Rankings (diap. 15):** se reutiliza la consulta del 22/09/2026 sin repetirla (CleanEnergyReviews,
  EnergySage, TaiyangNews, Black Ridge Research, PV-Tech). Bancabilidad AAA verificada en PV-Tech
  Q4 2025 para **LONGi, Trina y JA Solar** [7].
- **Precio:** categorías pvXchange de febrero de 2026 [13]: *High efficiency* (> 23 %) 0,130 €/Wp ·
  *Full black* 0,145 €/Wp · *Mainstream* (hasta 23 %) 0,115 €/Wp · *Low cost* 0,060 €/Wp (sin
  bancabilidad). Precio por categoría, no por modelo: ordena, no presupuesta.
- **Temperatura mínima provisional:** −10 °C para las tensiones máximas (§6). **Pendiente de AEMET**
  (fase 1.3), y en la V3 con la estación de Colmenar Viejo, no la de Tres Cantos.

---

## 2. V1a — lucernario horizontal (BIPV): se confirma

### 2.1 Criterios (sin cambios)

Requisito de paso: transparencia publicada ≥ 20 %. Puntuables: densidad Wp/m², transparencia, peso
para la perfilería existente, U y g publicados, coeficiente de temperatura, garantías, homologación
del laminado, datos para el PAN y referencias en lucernario. Todos salen de la **función** del
elemento (luz natural sobre el hall y control solar), no de la energía. Tabla completa y puntuación en
`comparacion-modulos-fv.md` §3.1-3.2 (Onyx 19,5 · Polysolar 21,0 · AGC 13,5).

### 2.2 Qué podría cambiar con la separación, y por qué no cambia

La categoría A ya era independiente en el documento anterior: nunca compartió módulo, PAN ni
inversor con el resto. Separar V1b, V2 y V3 no le afecta. **Se confirma Onyx c-Si al 35 %**: 330
módulos ≈ **60,1 kWp** sobre 463,1 m² de vidrio activo, con Polysolar de reserva condicionada a que
publique una versión ≥ 20 % de transparencia.

### 2.3 Hallazgo lateral que Mario debe conocer (no cambia la elección hoy)

Al investigar la seguridad del vidrio en marquesinas (§4) ha aparecido el **DMEGC Greenhouse
GH340M107-B40HS7**: vidrio-vidrio 2 + 2 mm, ~43 % de área transparente, 340 W, 2278 × 1134 mm
(**131,6 W/m²**, cálculo propio), 31,4 kg, garantía de producto 15 años y de potencia 30 años
(87,4 %) [24]. DMEGC anunció en julio de 2025 la homologación alemana DIBt Z-70.3-309 para
aplicaciones sobre cabeza, como único fabricante Tier 1 [23]. Frente a Onyx: densidad equivalente
con más transparencia y garantía de producto triple.

No se incorpora a la tabla porque: (a) es un módulo **con marco** de 30 mm pensado para
invernaderos y marquesinas, y no está comprobado que encaje en la perfilería del lucernario; (b)
«área transparente» no es lo mismo que transmisión luminosa (VLT); (c) **no está verificado** que la
homologación Z-70.3-309 cubra este modelo concreto. **Decisión de Mario:** si le interesa, se abre
como cuarto candidato de V1a con esas tres comprobaciones.

---

## 3. V1b — cubierta plana con impermeabilización líquida (sheds lastrados)

### 3.1 Criterios y de dónde sale cada uno

| # | Criterio | Origen | Por qué pesa en V1b |
| --- | --- | --- | --- |
| 1 | Eficiencia / densidad | Arcas + diap. 16 | La variante está limitada por superficie (1.582,5 m² netos de módulo) |
| 2 | Coeficiente de temperatura | Arcas + diap. 16 | Cubierta en Madrid; efecto moderado con sheds ventilados |
| 3 | Carga mecánica trasera (succión) | Propio; M6-T8 [20] | Sheds sobre cubierta expuesta; el ensayo trasero limita la presión local de viento que admite el módulo |
| 4 | Encaje en estructuras lastradas estándar a 10° | Propio; fichas K2 y Van der Valk [17][18] | La impermeabilización no admite perforaciones (§3.2) |
| 5 | Peso y tamaño para el manejo | Arcas | Montaje a mano en cubierta |
| 6 | LID del primer año | Diap. 16 | |
| 7 | Garantías | Arcas + diap. 16 | |
| 8 | Precio (categoría pvXchange) | Arcas + diap. 16 | |
| 9 | Posición en ranking / bancabilidad | Diap. 15-16 | Peso bajo: la inversión es del propio usuario, no se financia con proyecto |
| 10 | Longitud de string con inversor de 1100 V | Propio | El límite de V1b en la revisión 2 de superficies **fueron las entradas DC** [21] |
| 11 | Corriente Isc frente a la entrada por MPPT | Propio | Inversores de string de cubierta |
| 12 | Comportamiento al fuego como cubierta | Propio | Campo FV sobre las salas de un CPD en explotación |
| 13 | PAN disponible en PVsyst | Propio | Sin PAN no hay simulación |

### 3.2 Qué impone la impermeabilización de poliurea o poliuretano líquido

Lo que se ha podido documentar, y lo que no:

1. **Estructura no perforante.** Una membrana líquida continua y adherida pierde su razón de ser si
   se perfora para anclar. Las estructuras lastradas trabajan por peso propio, sin anclaje, y son la
   solución habitual para no tocar la impermeabilización [16][17][18]. Condición del lastre: K2 lo
   admite con pendiente de cubierta ≤ 3° [17]; Van der Valk, hasta 5° [18].
2. **Capa de protección entre apoyos y membrana.** Todo punto de contacto necesita una lámina o
   almohadilla compatible (EPDM o separador aprobado) para evitar punzonamiento y abrasión con los
   ciclos térmicos [16]. K2 incluye para ello la manta de EPDM «Dome Mat S» [17]. Para el caso
   concreto de una membrana de **poliuretano líquido lastrada**, Sika especifica un geotextil de
   poliéster (S-Felt T-300) como capa de separación, nivelación y protección bajo el lastre [19].
   Ojo: ese sistema de Sika es para lastre de losas o grava en general, no para una estructura FV;
   sirve como precedente del fabricante, no como homologación.
3. **Compatibilidad declarada: no verificada para membranas líquidas.** K2 declara su sistema para
   cubiertas con lámina monocapa, bituminosas, de hormigón, con grava o ajardinadas [17]; Van der
   Valk, para cubiertas con grava, ajardinadas o estructura metálica [18]. **Ninguno de los dos
   menciona las membranas líquidas** (poliurea o PU). Hay que pedir por escrito al fabricante de la
   impermeabilización la compatibilidad química de la almohadilla y, si procede, que mantenga la
   garantía de la cubierta [16].
4. **Retirada futura.** La poliurea y el PU líquido se renuevan por recubrimiento. Un sistema
   lastrado se desmonta sin dejar huella [18], a diferencia de los soportes pegados o soldados a la
   membrana (espuma de poliuretano proyectada, termosoldado) que están apareciendo como alternativa
   al lastre [22]: estos obligan a cortar la membrana para desmontar. **Recomendación: lastrado con
   protección, no adherido.**
5. **Sobrecarga admisible.** Módulo y estructura suelen quedar por debajo de 12 kg/m², pero es un
   dato a contrastar con el estudio estructural del edificio [20]. El lastre se reparte por zonas
   (más en bordes y esquinas) [20].

**Conclusión para la elección del módulo:** la impermeabilización condiciona la **estructura**, no
el módulo. Al módulo solo le pide dos cosas: que su formato entre en los sistemas lastrados estándar
(criterio 4) y que su peso no desequilibre la sobrecarga, cosa que ninguno de los tres hace (§3.3,
nota de peso).

### 3.3 Tabla comparativa

Candidatos: los mismos tres del 22/09 (misma clase de 54 células de media célula, ~2 m²), con
tabla completa y fuentes en `comparacion-modulos-fv.md` §4.1. Aquí se recogen las filas de la
diap. 16 y las propias de V1b.

| Característica | **REC Alpha Pure-RX 470** | **AIKO Neostar 2P 475 (Mw)** | **LONGi Hi-MO X6 465** |
| --- | --- | --- | --- |
| Potencia STC · tecnología | 470 W · N-type HJT | 475 W · N-type ABC | 465 W · HPBC |
| Eficiencia | 22,6 % | **23,8 %** | 22,8 % |
| Coef. temp. Pmax | **−0,24 %/°C** | −0,26 %/°C | −0,28 %/°C |
| LID 1.er año · degradación anual | 2 % · 0,25 %/año | ≤ 1 % · ≤ 0,35 %/año | < 1 % · 0,40 %/año |
| PID | no declarado | no declarado | no declarado |
| Garantía potencia / producto | **92 % a 25 años** / 20 (25) años | 88,85 % a 30 años / 15 años (ampliable a 25) | 89,4 % a 25 años / 15 años |
| Características especiales | Vidrio AR 3,2 mm; granizo 55 mm (PVEL); IEC 61701 / 62716 | Monovidrio 3,2 mm; optimización frente a sombreado parcial (fabricante) | Monovidrio 3,2 mm |
| Ranking · bancabilidad | 1.º CER y EnergySage · CC+ (**no verificado**) | 3.º CER · B (**no verificado**) | 2.º en envíos · **AAA** |
| Precio (categoría pvXchange) | 0,145 €/Wp (Full black) | 0,130 €/Wp (High efficiency) | 0,115 €/Wp (Mainstream) |
| Dimensiones · peso | 1728 × 1205 mm · 22,7 kg | 1757 × 1134 mm · 21,5 kg | 1800 × 1134 mm · 21,6 kg |
| **Carga trasera (succión)** | **−4000 Pa** | −2400 Pa | −2400 Pa |
| **Encaje en lastrados a 10°** [17][18] | Ancho 1205 mm: cabe en Van der Valk (≤ 1250 apaisado) y K2 D-Dome (≤ 1400); **no** en K2 S-Dome (≤ 1170) | Cabe en los tres | Cabe en los tres |
| **Tensión máx. sistema · Ns con 1100 V** | 1000 V · **14** módulos | 1500 V · **24** | 1500 V · **25** |
| **Isc STC** | **8,95 A** | 14,35 A | 14,93 A |
| **Fuego** [10][11][12] | IEC 61730 clase C · **EN 13501-5 BROOF(t2)** · EN 13501-1 clase E | IEC clase C | IEC clase C |
| PAN en PVsyst | **Sí** (informe del M6) | **no verificado** | **no verificado** |
| **kWp en 1.582,5 m²** | 759 uds · **356,7 kWp** | 794 uds · **377,1 kWp** | 775 uds · **360,4 kWp** |

> **Nota de peso.** Repartido sobre los 2.756,88 m² de cubierta, el peso de los módulos es de
> 6,25 kg/m² con REC, 6,19 con AIKO y 6,07 con LONGi (cálculo propio: n.º de módulos × peso ÷
> superficie). La diferencia entre candidatos es de **0,2 kg/m²**: el módulo no decide la
> sobrecarga; la deciden la estructura y el lastre.

### 3.4 Puntuación y justificación

| Criterio | REC | AIKO | LONGi |
| --- | --- | --- | --- |
| 1 Eficiencia / densidad | 1 | 3 | 2 |
| 2 Coef. temperatura | 3 | 2 | 1 |
| 3 Carga trasera | 3 | 1,5 | 1,5 |
| 4 Encaje en lastrados | 1 | 2,5 | 2,5 |
| 5 Peso y tamaño | 1 | 3 | 2 |
| 6 LID | 1 | 2,5 | 2,5 |
| 7 Garantías | 3 | 2 | 1 |
| 8 Precio | 1 | 2 | 3 |
| 9 Ranking / bancabilidad | 2 | 2 | 3 |
| 10 Longitud de string (1100 V) | 1 | 2 | 3 |
| 11 Isc frente a MPPT | 3 | 2 | 1 |
| 12 Fuego como cubierta | 3 | 1,5 | 1,5 |
| 13 PAN disponible | 3 | 1,5 | 1,5 |
| **Total** | **26** | **27,5** | **25** |

**Elegido: AIKO Neostar 2P 475 W monovidrio.** Gana, pero por poco, y conviene decirlo así. Sus
argumentos son los ligados a lo que limita la variante:

1. **Densidad.** +20 kWp frente a REC (+5,7 %) y +17 kWp frente a LONGi en la misma cubierta.
2. **Strings largos.** 24 módulos por string con un inversor de 1100 V frente a los 14 de REC. Para
   ~794 módulos son **33 strings** en vez de **54**: menos entradas DC, que fue exactamente lo que
   limitó la V1b en la revisión 2 de superficies [21].
3. **LID ≤ 1 %** frente al 2 % de REC.

**Reserva: REC Alpha Pure-RX 470.** Queda a un punto y medio, con tres ventajas que no son menores
en una cubierta de CPD: **−4000 Pa** de carga trasera (margen frente a succión en esquinas si el
lastre se ajusta al mínimo), **BROOF(t2)** declarado —el único de los tres con clasificación europea
de comportamiento al fuego exterior de cubierta— y **PAN probado** en el informe del Módulo 6. Si la
comprobación de viento de la fase 6 o la normativa de incendios aplicable a la cubierta (a revisar,
§8, pendiente 7) exigen más de lo que declara AIKO, se pasa a REC y se acepta perder ~20 kWp.

LONGi queda tercero: es el más barato y el más bancable, pero en una cubierta de ~377 kWp pagada por
el propio usuario la bancabilidad pesa poco y su densidad es la segunda.

### 3.5 Cautelas

- El factor 0,82 de empaquetado en sheds se validó con la geometría de REC. Van der Valk da un paso
  estándar de 1500 mm en apaisado a 10° [18]; con el ancho de AIKO (1134 mm) hay que **rehacer la
  disposición en la escena 3D** antes de dar por buenos los 794 módulos.
- Con la separación por variantes, el inversor de V1b **ya no tiene por qué ser el Huawei
  SUN2000-100KTL-M2**. Si se mantiene: 10 MPPT y 20 entradas [25] (dato que la revisión 2 tenía
  pendiente), 1100 V de tensión máxima [25] y **30 A por MPPT** (**no verificado**: fragmento de
  buscador, no ficha). Con dos strings AIKO por MPPT, Imp = 27,3 A cabe; Isc = 28,7 A también, con
  poco margen para el factor 1,25 del dimensionado de protecciones. Se cierra en la fase 4.

---

## 4. V2 — marquesinas de aparcamiento

### 4.1 Criterios y de dónde sale cada uno

| # | Criterio | Origen | Por qué pesa en V2 |
| --- | --- | --- | --- |
| 0 | **Vidrio-vidrio** (requisito de paso) | Propio; diap. 16 («glass-glass») | Vidrio sobre personas y vehículos: sin lámina trasera que degrade y con el encapsulante reteniendo fragmentos |
| 1 | Eficiencia / densidad | Arcas + diap. 16 | Huella limitada (3.182,4 m² de módulo) y variante más productiva del TFM |
| 2 | Ganancia bifacial | Diap. 16 («bifacial») | Solo existe si la marquesina no lleva chapa bajo el módulo (§4.2) |
| 3 | Carga trasera (succión) | Propio | Marquesina abierta: el viento actúa por las dos caras |
| 4 | Reacción al fuego del módulo | Propio | Cubre vehículos aparcados |
| 5 | Espesor del vidrio | Propio | Rigidez y seguridad del laminado sobre cabeza |
| 6 | Coeficiente de temperatura | Arcas + diap. 16 | |
| 7 | Garantías | Arcas + diap. 16 | |
| 8 | LID y degradación anual | Diap. 16 | |
| 9 | Ranking / bancabilidad | Diap. 15-16 | |
| 10 | Precio | Arcas + diap. 16 | |
| 11 | Peso | Arcas | Montaje en altura; efecto menor sobre la estructura |
| 12 | Isc frente a MPPT | Propio | Con cara trasera, la Isc sube con el albedo |

### 4.2 Los dos modelos de mercado de marquesina

| | **A. Marquesina «integrada»: el módulo es la cubierta** | **B. Estructura para montar módulos estándar encima** |
| --- | --- | --- |
| Cómo es | Perfiles de aluminio que son a la vez fijación del módulo y **canalón de evacuación**: la cubierta queda estanca sin chapa [27]. En el extremo, laminados BIPV sin marco con homologación de vidrio sobre cabeza [23] | Pilares y jácenas de acero galvanizado, perfilería de aluminio y módulos enmarcados en vertical u horizontal; **semiestanca por defecto** (drenaje controlado), estanca solo con **chapa bajo el módulo**; inclinación estándar de 10° [26] |
| Módulo | Vidrio-vidrio (enmarcado o laminado) | Cualquiera enmarcado |
| Estanqueidad | Sí | Parcial; total solo con chapa |
| Cara trasera | Libre: la ganancia bifacial existe | Libre si es semiestanca; **anulada** si lleva chapa |
| Normativa estructural | Una solución declara CTE DB-SE-AE, DB-SE-A y Eurocódigos 0, 1 y 3 [27] | Acero galvanizado según ISO 1461 [26]; cálculo CTE a comprobar en fase 6 |
| Seguridad del vidrio sobre cabeza | En Alemania exige homologación DIBt (DIN 18008) [23][28]; en España **no se ha localizado** una exigencia equivalente para módulos (**no verificado**) | Igual problema: el módulo sigue estando sobre cabeza salvo que haya chapa debajo |

**Lectura para el TFM.** En la práctica las dos vías convergen: ambas montan **módulos enmarcados de
formato estándar**, y lo que cambia es si la perfilería hace de canalón o hay chapa. La verdadera
marquesina BIPV (laminado sin marco homologado) es otra categoría de producto y de precio, y no
aporta nada que V2 necesite. **Se propone la vía A con módulo vidrio-vidrio enmarcado sobre perfiles
canalón**: estanca, sin chapa y con el vidrio-vidrio como argumento de seguridad. Si Mario prefiere
una marquesina estándar con chapa (vía B estanca), el criterio 2 (bifacialidad) desaparece y la
elección se refuerza a favor del módulo monofacial (§4.5).

### 4.3 Candidatos

Tres módulos vidrio-vidrio de la clase de 54 células (media célula, 1,99-2,22 m²):

1. **AIKO Neostar 2P+ 475 W vidrio-vidrio** (AIKO-A475-MAH54Dw): la versión de doble vidrio del
   módulo de V1b; monofacial (vidrio trasero con fondo blanco) [14].
2. **Trina Vertex S+ TSM-440NEG9RC.27**: bifacial vidrio-vidrio transparente; Trina es **AAA** y 5.º
   en CleanEnergyReviews [15].
3. **Jinko Tiger Neo 54HL4M-BDV 525 W**: bifacial vidrio-vidrio TOPCon; Jinko, 1.º en envíos (Black
   Ridge) [29].

Quedan fuera REC Alpha Pure-RX y LONGi Hi-MO X6 Explorer, que son de lámina trasera o monovidrio.

### 4.4 Tabla comparativa

| Característica | **AIKO Neostar 2P+ 475 (Dw)** | **Trina Vertex S+ 440** | **Jinko Tiger Neo 525 BDV** |
| --- | --- | --- | --- |
| Revisión de ficha | V4.1_202510 | TSM_EN_2023_B | Z2-EU (2025) |
| Potencia STC | 475 W | 440 W | 525 W |
| Tecnología | N-type ABC, 108 medias células | N-type i-TOPCon, 144 medias células | N-type TOPCon, 108 medias células |
| Eficiencia | **23,8 %** | 22,0 % | 23,61 % |
| Coef. temp. Pmax / Voc / Isc | **−0,26** / −0,22 / +0,05 %/°C | −0,30 / −0,24 / +0,04 %/°C | −0,29 / −0,25 / +0,045 %/°C |
| LID 1.er año · anual | **≤ 1 % · ≤ 0,35 %** | 1 % · 0,4 % | 1 % · 0,40 % |
| PID | no declarado | «resistencia PID» genérica, sin cifra | «Anti-PID Guarantee», sin cifra |
| Garantía potencia / producto | **88,85 %** a 30 años / 15 años (ampliable a 25) | 87,4 % a 30 años / **25 años** | 87,4 % a 30 años / 15 años |
| Vidrio delantero + trasero | **2,0 + 2,0 mm** semitemplado | 1,6 + 1,6 mm termoendurecido | **2,0 + 2,0 mm** (AR + termoendurecido) |
| Bifacialidad | No (monofacial, fondo blanco) | **80 ± 5 %** | **80 ± 5 %** |
| Carga frontal / trasera (ensayo) | 5400 / 2400 Pa | 5400 / **4000 Pa** | 5400 / 2400 Pa |
| Fuego | **IEC clase A** | «Excelente», sin clase (**no verificado**) | IEC clase C |
| Dimensiones · peso | 1757 × 1134 × 30 mm · 24,2 kg | 1762 × 1134 × 30 mm · **21,0 kg** | 1961 × 1134 × 30 mm · 27,0 kg |
| Voc / Isc / Vmp / Imp (STC) | 41,24 V / 14,35 A / 34,80 V / 13,66 A | 52,2 V / **10,67 A** / 44,0 V / 10,01 A | 41,23 V / 15,88 A / 35,05 V / 14,98 A |
| Tensión máx. · fusible | 1500 V · 25 A | 1500 V · 25 A | 1500 V · 35 A |
| Ranking · bancabilidad | 3.º CER · B (**no verificado**) | 5.º CER · **AAA** | 1.º envíos · **no verificado** |
| Precio (categoría pvXchange) | 0,130 €/Wp | **0,115 €/Wp** | 0,130 €/Wp |
| PAN en PVsyst | **no verificado** | **no verificado** | **no verificado** |
| **kWp en 3.182,4 m²** | 1.597 uds · **758,6 kWp** | 1.592 uds · 700,5 kWp | 1.431 uds · 751,3 kWp |

Fuentes de la tabla: AIKO [14], Trina [15], Jinko [29]; rankings del 22/09 y [7]; precios [13].

### 4.5 Puntuación y justificación

| Criterio | AIKO Dw | Trina | Jinko |
| --- | --- | --- | --- |
| 1 Eficiencia / densidad | 3 | 1 | 2 |
| 2 Ganancia bifacial | 1 | 2,5 | 2,5 |
| 3 Carga trasera | 1,5 | 3 | 1,5 |
| 4 Fuego | 3 | 2 | 1 |
| 5 Espesor del vidrio | 2,5 | 1 | 2,5 |
| 6 Coef. temperatura | 3 | 1 | 2 |
| 7 Garantías | 2 | 3 | 1 |
| 8 LID y degradación | 3 | 1,5 | 1,5 |
| 9 Ranking / bancabilidad | 1 | 3 | 2 |
| 10 Precio | 1,5 | 3 | 1,5 |
| 11 Peso | 2 | 3 | 1 |
| 12 Isc frente a MPPT | 2 | 3 | 1 |
| **Total** | **25,5** | **27** | **19,5** |

**Por puntos gana Trina, por un punto y medio.** Sus ventajas son reales —AAA, garantía de producto
de 25 años, −4000 Pa traseros, el precio de categoría más bajo—, pero cuatro de los seis criterios
que gana en solitario (precio, peso, Isc y bancabilidad) son **comerciales o de dimensionado del
inversor**, y ninguno toca lo que limita la variante.

**Elegido: AIKO Neostar 2P+ 475 W vidrio-vidrio**, por tres razones ligadas a la función:

1. **Densidad en la variante más productiva.** 758,6 kWp frente a 700,5 kWp: **+58 kWp (+8,3 %)**
   sobre la misma huella. Para que Trina iguale la energía anual con su cara trasera, la ganancia
   bifacial simulada tendría que superar **~8 %** (cálculo propio: 758,6 / 700,5). Sobre asfalto,
   que refleja poco, no hay dato verificado que lo sostenga; lo dirá PVsyst.
2. **Seguridad sobre vehículos.** Único de los tres con **fuego IEC clase A** declarado, y vidrio de
   2 + 2 mm frente a 1,6 + 1,6 mm.
3. **Robustez frente a la solución estructural.** Si la marquesina acaba siendo estanca con chapa
   (vía B, §4.2), la ventaja bifacial de Trina y Jinko desaparece y la de AIKO no se toca.

**Reserva: Trina Vertex S+ 440 bifacial.** Pasa a elegido si ocurre cualquiera de estas dos cosas:
la simulación bifacial de PVsyst sobre el pavimento real da **más del ~8 %** de ganancia, o Mario y
el tutor priorizan bancabilidad y precio. Antes habría que confirmar su clase de fuego.

**Matiz que conviene escribir:** con ~758 kWp la V2 **vierte más** que con los 716 kWp del
recálculo (pico por encima de la carga plana de ~437 kW [21]). Parte de los +58 kWp de AIKO se la
comerá el antivertido. Hay que recalcular los excedentes antes de defender la densidad como
argumento cuantitativo; como argumento cualitativo sigue en pie.

Jinko queda tercero: su densidad es casi la de AIKO, pero su clase de fuego (C) y la Isc más alta
de los tres (15,88 A, 17,48 A con cara trasera [29]) juegan en contra justo donde V2 es sensible.

---

## 5. V3 — planta en suelo en Colmenar Viejo

### 5.1 Criterios y de dónde sale cada uno

| # | Criterio | Origen | Por qué pesa en V3 |
| --- | --- | --- | --- |
| 0 | **1500 V** (requisito de paso) | Propio; estándar de planta en suelo | Strings largos, menos cajas y cableado |
| 0 | **Bancabilidad AAA** (requisito de paso) | Diap. 15 (PV-Tech) | Varios MWp, previsiblemente financiados |
| 1 | Eficiencia / densidad (kWp/ha) | Arcas | **Peso bajo:** el suelo sobra (58,84 ha frente a 3-4 ha); lo que limita es la capacidad de acceso (~4,6 MW) |
| 2 | Bifacialidad | Diap. 16 | Suelo natural, estructura elevada |
| 3 | Coef. temperatura | Arcas + diap. 16 | Energía por kWp, que es lo que cuenta cuando limita la potencia |
| 4 | Degradación | Diap. 16 | Horizonte de 30 años |
| 5 | Garantías | Diap. 16 | |
| 6 | Precio (€/Wp, LCOE) | Diap. 16 | En utility es el criterio dominante |
| 7 | Compatibilidad con fija y seguidor | Propio | Decisión de estructura aún abierta |
| 8 | Isc frente a MPPT | Propio | Inversores de 1500 V |
| 9 | Peso | Arcas | Manejo de módulos de 33 kg |

Formato de la clase: 132 medias células, **2382 × 1134 mm (2,70 m²)**, vidrio-vidrio 2 + 2 mm,
bifacial. Es el formato que usan los fabricantes AAA para planta en suelo.

### 5.2 Tabla comparativa

| Característica | **LONGi Hi-MO 9 LR8-66HYD-670M** | **JA Solar JAM66D45-630/LB** | **Trina Vertex N TSM-620NEG19RC.20** |
| --- | --- | --- | --- |
| Revisión de ficha | 20260120 V2.0 | Global-EN-20241105A | TSM_EN_2024_A |
| Potencia STC | 670 W | 630 W | 620 W |
| Tecnología | HPBC (contacto posterior) | N-type TOPCon | N-type i-TOPCon |
| Eficiencia | **24,8 %** | 23,3 % | 23,0 % |
| Coef. temp. Pmax / Voc / Isc | **−0,26** / −0,200 / +0,050 %/°C | −0,290 / −0,250 / +0,045 %/°C | −0,29 / −0,24 / +0,04 %/°C |
| LID 1.er año · anual | **< 1 % · 0,35 %** | 1 % · 0,4 % | 1 % · 0,40 % |
| PID | no declarado | no declarado | «resistencia PID» genérica |
| Garantía potencia / producto | **88,85 %** a 30 años / 12 años | 87,4 % a 30 años / 12 años | 87,4 % a 30 años / 12 años |
| Bifacialidad | 75 ± 5 % | **80 ± 5 %** | **80 ± 5 %** |
| Vidrio | 2,0 + 2,0 mm termoendurecido | 2,0 / 2,0 mm | 2,0 + 2,0 mm (trasero con rejilla blanca) |
| Carga frontal / trasera | 5400 / 2400 Pa | 5400 / 2400 Pa | 5400 / 2400 Pa |
| Fuego | IEC clase C | UL tipo 29 / clase C | no declarado |
| Peso | **32,6 kg** | 33,1 kg | 33,7 kg |
| Voc / Isc / Vmp / Imp (STC) | 50,12 V / 16,86 A / 41,38 V / 16,19 A | 48,90 V / 16,18 A / 40,70 V / 15,48 A | 49,6 V / **15,91 A** / 41,4 V / 14,99 A |
| Tensión máx. · fusible | 1500 V · 35 A | 1500 V · 35 A | 1500 V · 35 A |
| Seguidor | Sin declaración | **Taladros para Nextracker** en la ficha | Sin declaración |
| Característica especial | Diseño antipolvo (fabricante: ≥ 2 % más de producción mensual; **no cuantificado por terceros**) | — | — |
| Bancabilidad | **AAA** | **AAA** | **AAA** |
| Precio (categoría pvXchange) | 0,130 €/Wp | 0,130 €/Wp | **0,115 €/Wp** |
| PAN en PVsyst | **no verificado** | **no verificado** | **no verificado** |
| **Densidad** (fija 30° S, GCR 0,40 + 20 %) | **12,09 m²/kWp · 827 kWp/ha** | 12,86 m²/kWp · 777 kWp/ha | 13,07 m²/kWp · 765 kWp/ha |

Fuentes de la tabla: LONGi [30], JA [31], Trina [32]; bancabilidad [7]; precios [13].

La densidad usa la misma hipótesis que `estimacion-preliminar-variantes.md` §5.4 (13,2 m²/kWp con
REC); con 3 MWp, LONGi ocuparía ~3,6 ha y Trina ~3,9 ha.

### 5.3 Puntuación y justificación

| Criterio | LONGi | JA | Trina |
| --- | --- | --- | --- |
| 1 Densidad (peso bajo, se puntúa igual) | 3 | 2 | 1 |
| 2 Bifacialidad | 1 | 2,5 | 2,5 |
| 3 Coef. temperatura | 3 | 1,5 | 1,5 |
| 4 Degradación | 3 | 1,5 | 1,5 |
| 5 Garantías | 3 | 1,5 | 1,5 |
| 6 Precio | 1,5 | 1,5 | 3 |
| 7 Compatibilidad con seguidor | 1,5 | 3 | 1,5 |
| 8 Isc frente a MPPT | 1 | 2 | 3 |
| 9 Peso | 3 | 2 | 1 |
| **Total** | **20** | **17,5** | **16,5** |

Sin el criterio de densidad (porque en V3 no limita el suelo): LONGi 17 · JA 15,5 · Trina 15,5. El
orden no cambia.

**Elegido: LONGi Hi-MO 9 670 W.** En una planta limitada por potencia de acceso, no por suelo, lo
que cuenta es la **energía por kWp** y su evolución a 30 años: LONGi tiene el mejor coeficiente de
temperatura (−0,26 %/°C), la menor degradación (0,35 %/año) y la mejor garantía de potencia
(88,85 % a 30 años). Su bifacialidad algo menor (75 % frente a 80 %) recorta parte de esa ventaja;
PVsyst dirá cuánto.

**Reserva: JA Solar JAM66D45-630/LB.** Bifacialidad del 80 % y la única ficha que declara la fijación
para seguidor. Si la V3 se estudia con seguidor a un eje, JA pasa por delante.

**Trina**, con el precio de categoría más bajo, es la opción si el análisis económico (LCOE) se hace
con precios reales y la diferencia de €/Wp compensa la energía. Se deja anotado para
`analista-economico`.

**Frente al 22/09.** La bancabilidad, que allí era el argumento para tener LONGi de reserva «por si
pesa en V3», deja de discriminar: en V3 es requisito de paso y los tres lo cumplen.

---

## 6. Implicaciones para el inversor, variante por variante

Cálculo propio con **Tmín = −10 °C provisional** (ΔT = 35 K); se recalcula con los datos de AEMET.

| Variante | Módulo | Voc STC → Voc(−10 °C) | Isc STC | Tensión del sistema | Ns máx. | Notas para la fase 4 |
| --- | --- | --- | --- | --- | --- | --- |
| **V1a** | Onyx 182 Wp | 24 V → 26,4 V (β −0,28) | 9,66 A | **1000 V** (límite del módulo) | 37 | Inversor propio y pequeño (~50-60 kW); Voc/Vmp con 2 cifras, pedir ficha exacta |
| **V1b** | AIKO 475 Mw | 41,24 V → **44,4 V** | **14,35 A** | Inversor de **1100 V** | **24** | Comprobar corriente máx. por MPPT (≥ 2 × 14,35 A con margen). Con REC (reserva): Voc(−10 °C) 71,2 V y **1000 V** del módulo → 14 por string |
| **V2** | AIKO 475 Dw | 41,24 V → **44,4 V** | **14,35 A** | Inversor de **1100 V** | **24** | Mismo diseño de string que V1b. Con Trina (reserva): 56,6 V → 19 por string, Isc 10,67 A (11,52 A con 10 % de cara trasera) |
| **V3** | LONGi 670 | 50,12 V → **53,6 V** | **16,86 A** (19,75 A con +20 % de cara trasera) | Inversor de **1500 V** | **27** | La Isc con ganancia bifacial es la que dimensiona entradas y fusibles (35 A por módulo); con JA: 28 por string |

**Consecuencia práctica de la separación:** V1b y V2 comparten tensión (1100 V), Voc, Isc y longitud
de string, lo que permite un **único modelo de inversor para las dos** aunque el módulo no sea el
mismo producto. V3 va a 1500 V y con otro inversor, como ya era previsible. V1a sigue aparte.

---

## 7. Contrapeso: qué se pierde al no tener un módulo único

| Se pierde | Cuánto pesa aquí |
| --- | --- |
| **Repuestos y compras.** Un solo modelo simplifica el almacén de repuestos y la negociación de volumen | Menos de lo que parece: V1b y V2 son la misma plataforma AIKO (mismos datos eléctricos) y V3 es otra escala de compra (MWp, otro proveedor y otra logística). V1a nunca pudo compartir |
| **Un solo PAN en PVsyst** | Hay que dar de alta **cuatro** PAN (Onyx, AIKO Mw, AIKO Dw, LONGi) en vez de dos. Los dos AIKO difieren solo en vidrio, peso y comportamiento térmico |
| **Homogeneidad ante el tribunal.** Una tabla y una decisión se defienden más rápido que cuatro | Es el coste real. Se compensa con una tabla-resumen (§0) y porque cada decisión se apoya en el criterio que limita su variante, que es justo lo que pide la fase 2 de la guía ERMA |
| **Continuidad con el Módulo 6** | Se mantiene parcialmente: REC vuelve como reserva de V1b, la cubierta del trabajo previo |

**Por qué, aun así, compensa separar.** Con un módulo único, uno de los argumentos decisivos era la
tensión de 1500 V que solo necesita la V3, y se aplicaba a una cubierta que trabajará con inversores
de 1100 V. Esa es la clase de incoherencia que un tutor detecta: se elige para una variante con
criterios de otra. Separar la elección hace visibles los criterios que sí importan en cada sitio
—estructura no perforante y fuego en la cubierta, vidrio sobre cabeza en la marquesina, energía por
kWp y bancabilidad en la planta— y el coste logístico es pequeño porque V1b y V2 convergen de forma
natural en la misma plataforma.

---

## 8. Pendientes

| # | Pendiente | Quién | Bloquea |
| --- | --- | --- | --- |
| 1 | **Validar las cuatro elecciones**, en especial V2 (AIKO frente a Trina, que gana por puntos) | **Mario** | Todo lo demás |
| 2 | ¿Marquesina estanca con perfiles canalón (vía A) o estándar semiestanca / con chapa (vía B)? | **Mario** | Criterio bifacial de V2 |
| 3 | ¿Se abre DMEGC Greenhouse como cuarto candidato de V1a? (§2.3) | **Mario** | Solo si interesa |
| 4 | Comprobar PAN en la BD de PVsyst 8.1.5: AIKO-A475-MAH54Mw, AIKO-A475-MAH54Dw, LONGi LR8-66HYD-670M (y reservas REC, Trina NEG9RC.27, JA JAM66D45) | Mario → `piloto-pvsyst` | Simulación |
| 5 | Pedir al fabricante de la **impermeabilización** (poliurea / PU) la compatibilidad escrita de las almohadillas de apoyo (EPDM o geotextil) y el mantenimiento de su garantía; confirmar si la membrana es poliurea o PU | Mario (propiedad del edificio) | Estructura V1b, fase 6 |
| 6 | Sobrecarga admisible de la cubierta y pendiente real (lastre solo con ≤ 3-5°) | Mario / estudio estructural | Estructura V1b |
| 7 | Normativa de incendios aplicable a un campo FV sobre la cubierta de un CPD (clase de cubierta, compartimentación; en el TFM de Diego se usaron bloques < 400 m² con pasillos de 3,5 m por RSCIEI) — **no verificada aquí** | `investigador-cientifico` | Criterio 12 de V1b y reserva REC |
| 8 | Carga de viento CTE (succión) en marquesina y en esquinas de cubierta frente a −2400 Pa (AIKO) y −4000 Pa (REC, Trina) | Fase 6 | Estructuras |
| 9 | Simular en PVsyst la ganancia bifacial de Trina sobre el pavimento real; umbral de decisión ~8 % | Mario en PVsyst | Elección V2 |
| 10 | Recalcular excedentes de V2 con ~758 kWp | `ingeniero-dominio` | Argumento de densidad en V2 |
| 11 | Rehacer disposición de sheds (V1b) con 1757 × 1134 mm y paso real del sistema lastrado elegido | Mario en PVsyst 3D | 794 módulos de V1b |
| 12 | Verificar corriente máx. por MPPT del inversor de V1b/V2 (30 A del SUN2000-100KTL-M2 **no verificado**) | Fase 4 | Strings V1b/V2 |
| 13 | Tmín/Tmáx diurnas de AEMET: Tres Cantos (V1, V2) y **Colmenar Viejo (V3)** | Fase 1.3 | Ns de las cuatro variantes |
| 14 | Clase de fuego de Trina NEG9RC.27 (y de NEG19RC.20) | `investigador-cientifico` | Reserva V2 |
| 15 | Garantía de producto de AIKO en España (15 o 25 años) y disponibilidad de las dos versiones | Consulta a AIKO Europa | Cap. 9 |
| 16 | Onyx: ficha con Voc/Vmp de tres cifras, factor g y oferta (arrastrado del 22/09) | Mario | PAN V1a |
| 17 | Dar de alta las fichas citables con `bibliotecario-pdf` (AIKO Mw y Dw, LONGi Hi-MO 9, Onyx, reservas) | `bibliotecario-pdf` | Redacción |
| 18 | **Elegir la estructura soporte de las cuatro variantes** (producto y fabricante reales, con ficha): V1a, perfilería existente del lucernario; V1b, sistema lastrado no perforante compatible con la membrana líquida (K2, Van der Valk u otro); V2, **marquesina concreta** (vía A o B, fabricante, inclinación, cimentación) —los módulos de la tabla §4.4 son enmarcados de catálogo y la marquesina se compra aparte—; V3, fija o seguidor a un eje. Sin urgencia para la marquesina (el mercado admite el formato de 1134 mm de ancho), pero es **obligatorio**: alimenta el apartado de estructura soporte de la memoria, que debe cubrir las cuatro variantes y no solo V2. Decidir también si ese apartado sigue dentro del 6.1 o pasa a sección propia del cap. 6 | Mario + `ingeniero-dominio` | Apartado de estructura soporte; pendientes 2, 6 y 8 |

---

## 9. Fuentes

Las referencias [1]-[19] del documento del 22/09 que no se han vuelto a consultar se identifican
por su número original en `comparacion-modulos-fv.md` §7. Las nuevas o reconsultadas hoy:

**Criterios y método**
1. M. Arcas, TFM (2024), cap. 4.3 — `Documentacion de apoyo/Ejemplos TFM/TFM_M_A.pdf`
2. J. Amador, *GUIA_PLANTILLA Estudio Autoconsumo FV ERMA20.pptx*, diap. 15-17 — `Documentacion de apoyo/Trabajo Autoconsumo CPD/`

**Rankings y precios**
7. PV Tech, bancabilidad AAA Q4 2025 (LONGi, Trina, JA) — <https://www.pv-tech.org/ja-solar-moves-to-aaa-rating-in-latest-pv-moduletech-bankability-ratings-report/>
13. pvXchange vía Rinnovabili, categorías y precios de febrero de 2026 (reconsultado el 27/09/2026) — <https://www.rinnovabili.net/business/energy/photovoltaic-module-prices-2025-updated-data/>

**Fichas técnicas**
10. REC, *Alpha Pure-RX 460-485 W*, IEC EN 8.2026 V8 (reconsultada para clase de fuego) — <https://www.recgroup.com/sites/default/files/2025-01/Web_DS_REC%20Alpha%20Pure-RX_EN.pdf>
11. AIKO, *Neostar 2P Mono-Glass 450-475 W*, DS_EN_2405_V1.1 (reconsultada para clase de fuego) — <https://www.solargain.com.au/sites/default/files/2024-09/Aiko-Neostar-475w.pdf>
12. LONGi, *Hi-MO X6 Max Explorer LR7-54HTH*, 20240511 V2 — `Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Ejercicios y Ejemplos/Configuraciones/Configuraciones/Fichas tecnicas Longi/ES_Datasheet_LR7_54HTH_X6_MAX_Explorer.pdf`
14. AIKO, *Neostar 2P+ AIKO-A-MAH54Dw 455-475 W*, V4.1_202510 — <https://aikosolar.com/wp-content/uploads/2025/10/Neostar-2Pplus_188-AIKO-A-MAH54Dw_455-475W-1757x1134x30mm_White-background-and-black-frame_V4.1_202510_DsDr_EN.pdf> · página de producto — <https://aikosolar.com/en/products/neostar-2pplus54-dual-glass/>
15. Trina Solar, *Vertex S+ TSM-NEG9RC.27*, TSM_EN_2023_B — <https://static.trinasolar.com/sites/default/files/VertexS_NEG9RC.27_EN_2023_B_web.pdf>
29. Jinko Solar, *Tiger Neo 54HL4M-BDV 495-525 W*, Z2-EU (2025) — <https://jinkosolar.eu/wp-content/uploads/2025/01/JKM495-525N-54HL4M-BDV-Z2-EU.pdf>
30. LONGi, *Hi-MO 9 LR8-66HYD 635-670M*, 20260120 V2.0 — <https://static.longi.com/Hi_MO_9_Hydro_Clear_LR_8_66_HYD_635_670_M_V2_V2_0_EN_e4931b34cd.pdf>
31. JA Solar, *JAM66D45 LB 605-630 W*, Global-EN-20241105A — <https://www.jasolar.eu/fileadmin/data/products/4.0/JAM66D45_LB.pdf>
32. Trina Solar, *Vertex N TSM-NEG19RC.20 590-620 W*, TSM_EN_2024_A — <https://static.trinasolar.com/sites/default/files/Datasheet_210R_NEG19RC.20_EN_2024A_web.pdf>
24. DMEGC, *Greenhouse GHxxxM107-B40HS7 325-340 W*, Ver. 20250903 — <https://www.dmegcsolar.com/upload/img/2025-12/692e9eef284de.pdf>

**Estructura, cubierta e impermeabilización (V1b)**
16. Sun Supply PV, *Ballasted Solar Mounting Systems 2026 Buyer's Guide* (almohadillas EPDM o lámina aprobada en todo punto de contacto; confirmación escrita del fabricante de la cubierta para conservar su garantía; trata TPO, EPDM, PVC y multicapa, **no** membranas líquidas) — <https://sunsuppv.com/solar-panel-mounting-systems-for-ballasted-flat-roofs/>
17. K2 Systems, *Dome 6 System*, catálogo técnico (inclinaciones, formatos, cubiertas admitidas, Dome Mat S, lastre ≤ 3°) — <https://catalogue.k2-systems.com/en/mounting-systems/flat-roof-systems/k2-dome-6-system/>
18. Van der Valk Solar Systems, *Datasheet ValkPro+* (2023) (formatos por configuración, paso, lastre ≤ 5°, desmontaje) — <https://www.pvo-int.com/wp-content/uploads/2019/01/en-datasheet-valkpro-2023.pdf>
19. Sika, *Liquid Applied Membrane — Warm Roof System and Ballast with Sikalastic-625 BMS* (S-Felt T-300 como capa de protección bajo lastre) — <https://source.thenbs.com/product/sika-liquid-applied-membrane-warm-roof-system-and-ballast-with-sikalastic-625-bms/9322rJGximpEkhoxb8AWQh/999gvSEmcCLM1JStdHmpUQ>
20. Resumen de M6-T8, *Estructuras soporte FV* (sobrecarga < 12 kg/m², lastre por zonas) — `conocimiento fotovoltaico/Referencia/m6-t8-estructuras-soporte-fv.md`
22. Solar Power World (abril de 2026), *Manufacturers develop non-penetrative alternatives to ballasts for rooftop solar* — <https://www.solarpowerworldonline.com/2026/04/manufacturers-develop-non-penetrative-alternatives-to-ballasts-for-rooftop-solar/>
25. Photomate, *Huawei SUN2000-100KTL-M2* (10 MPPT, 20 strings, 1100 V) — <https://www.photomate.eu/sun2000-100ktl-m2>

**Marquesinas (V2)**
23. PV Tech (julio de 2025), *DMEGC Solar achieves prestigious DIBt certification for overhead applications* (Z-70.3-309, único Tier 1) — <https://www.pv-tech.org/industry-updates/dmegc-solar-achieves-prestigious-dibt-certification-for-overhead-applications/> · pv magazine — <https://www.pv-magazine.com/press-releases/dmegc-solar-achieves-prestigious-dibt-certification-for-overhead-applications-as-the-only-tier-1-manufacturer-worldwide/>
26. Solarstem, *Marquesina fotovoltaica para parking* (IFrame/ZFrame: semiestanca por defecto, estanca con chapa, 10°) — <https://solarstem.com/sistemas-de-montaje/marquesina-fotovoltaica-parking-solar/>
27. Aplitech Energy, *Marquesinas fotovoltaicas* (perfiles de aluminio que son fijación y canalón; CTE y Eurocódigos) — <https://www.aplitech-energy.com/marquesinas-fotovoltaicas/>
28. DIBt, *Overhead glazing* (DIN 18008) — <https://www.dibt.de/en/construction-products-and-technniques/overview/productgroups/detail/construction-product/overhead-glazing>

**Documentos internos del proyecto**
21. `Memoria/analisis/recalculo-superficies-3d-pvsyst.md` (rev. 2) — superficies, límite de entradas DC en V1b, excedentes de V2 · `estimacion-preliminar-variantes.md` §5.4 — hipótesis de ocupación de V3
- `conocimiento fotovoltaico/Referencia/instalacion-fotovoltaica-centro-logistico-mad9.md` — precedente de Diego: módulo bifacial vidrio-vidrio de formato grande (JA 550 Wp) en cubierta plana con strings de 22 a 1500 V, y bloques < 400 m² por RSCIEI
