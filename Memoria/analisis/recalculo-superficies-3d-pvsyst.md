---
title: "Recálculo cerrado de V1a, V1b y V2 con las superficies medidas sobre el modelo 3D de PVsyst"
fecha: 2026-09-19
estado: cerrado
revision: 2
sustituye_a: "Memoria/analisis/estimacion-preliminar-variantes.md §4, §5.1 y §5.3 (superficies y potencias)"
script: "Memoria/analisis/scripts/recalc_superficies_3d.py"
fuentes_canonicas:
  - "Medición de Mario sobre el modelado 3D de PVsyst (19/09/2026): V1a 578,9109 m² · V1b 2.756,8828 m² · V2 3.536 m²"
  - "Respuestas de Mario de 19/09/2026 a las cinco preguntas abiertas de la revisión 1"
  - "Prompts/Capturas/situacion 3D V1 y V2.png · superficies v1 y v2.png · variantes pvsyst.png"
  - "Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv (3.832,0 MWh/año, 8.760 h)"
  - "Memoria/analisis/scripts/solar.py (modelo horario calibrado, −1,3 % frente al informe PVsyst del trabajo previo)"
  - "Documentacion de apoyo/Trabajo Autoconsumo CPD/Trabajo_DataCenter_Project.VC0-Report1.pdf"
tags: [fotovoltaica, autoconsumo, CPD, variantes, superficies, BIPV, marquesinas, PVsyst, geometria]
---

# Recálculo cerrado de V1a, V1b y V2 con las superficies del modelo 3D

> **Qué es este documento.** Mario midió las tres superficies sobre el modelado 3D que ha
> construido en PVsyst y, el mismo día, respondió a las cuatro preguntas que la revisión 1 dejó
> abiertas sobre esa medición. Con eso, **la geometría de V1a, V1b y V2 queda cerrada**: potencia,
> producción y autosuficiencia son ya cifras de trabajo, no horquillas.
>
> El modelo horario, la cadena de pérdidas y el perfil de carga no cambian: son los mismos que ya
> estaban calibrados contra el informe PVsyst del trabajo previo. **Lo único que ha cambiado es la
> geometría de entrada.** Cálculo reproducible en `scripts/recalc_superficies_3d.py`.

---

## 1. Lo que Mario ha cerrado, y lo que ha dejado abierto a propósito

| # | Pregunta de la revisión 1 | Respuesta | Efecto |
| --- | --- | --- | --- |
| **1** | Pendiente del lucernario | **0°: es horizontal.** Plano único, no faldones | Cae la hipótesis de ~35° de la rev.1 y la de 5° de catastro. La productividad de V1a baja a 1.540 kWh/kWp |
| **2** | ¿Las cifras llevan márgenes descontados? | **No.** Son la superficie máxima ideal | Los factores 0,80 / 0,70 / 0,82 / 0,90 se aplican **desde cero** sobre las tres |
| **3** | ¿Los 2.756,88 m² descuentan los patios? | **Sí.** Medición por polígonos de sección sobre la planta en H | Se adopta lo que la rev.1 llamaba *lectura B*: 358,74 kWp de techo por superficie |
| **4** | Fuente del 3D | **Catastro a escala 1:1, trazado a mano** en el editor 3D de PVsyst | Dato para la fase 1.4 de ERMA |
| **5** | ¿126 o 127 strings en V2? | **Diferida**: «*conforme avancemos en PVsyst veremos*» | Se documentan las dos, no se fija ninguna |

### 1.1 Por qué la respuesta 1 descarta la hipótesis de la revisión 1

La revisión 1 observó que 578,9109 / 472 = 1,2265, y que arccos(1/1,2265) = 35,4°, de donde
dedujo que el lucernario podía tener ~35° de pendiente y que los 578,91 m² serían superficie
*desarrollada*. **Era casualidad aritmética.** El lucernario es horizontal, así que superficie
desarrollada y proyección en planta coinciden y no hay ninguna corrección angular que aplicar. Los
578,9109 m² se usan tal cual, y de paso se resuelve sola la vieja discusión sobre si Google Earth
medía lo desarrollado y Catastro la proyección: en un plano a 0° no hay diferencia que discutir.

Vale la pena dejarlo escrito como aviso de método: **un cociente de superficies que coincide con
el coseno de un ángulo plausible no demuestra nada.** Con dos mediciones independientes de la
misma superficie, siempre existe *algún* ángulo que explica su cociente.

### 1.2 Cómo se ha verificado la respuesta 3

Mario remitió a las capturas. Lo que se lee en ellas:

- `situacion 3D V1 y V2.png` — el CPD está modelado como una **planta en H**: dos barras
  paralelas unidas por un tramo central, con la cubierta sensiblemente a un mismo nivel y un
  resalto corrido en la banda central. **Los dos patios interiores están dibujados como huecos
  pasantes**: se ve el fondo de la escena a través de ellos.
- `superficies v1 y v2.png` — vista en planta con el marcado de Mario. El **recuadro rojo** es la
  banda central, el lucernario (V1a). Los **recuadros cian** son las alas de la H (V1b), marcados
  **sección por sección**, no como un rectángulo envolvente.

Eso confirma la hipótesis: midiendo polígono a polígono por sección, **el hueco entre las patas
de la H queda fuera por construcción** y no hay que restarlo aparte. Se adopta la *lectura B* de
la revisión 1 y se descartan la A (restar 408 m² de patios) y la C (tratar la cifra como
superficie neta de módulo).

> **Lo que no se ha hecho, y conviene decirlo.** Se intentó verificar la cifra midiendo en píxeles
> el área marcada en la captura y escalándola con el rectángulo rojo. Mario advirtió que los
> recuadros son orientativos —dibujados a mano y deprisa, solo para indicar qué superficie ocupa
> cada variante—, así que **esa comprobación se descarta y no aporta ninguna cifra a este
> documento**. La única fuente de las superficies es la medición que Mario hizo dentro de PVsyst.

### 1.3 Errata detectada de paso en `variantes pvsyst.png`

El proyecto `TFM_DataCenter.PRJ` tiene cargado **`Carrasqueira_MN82.SIT` / `.MET` — Meteonorm 8.2,
Portugal**, heredado de una plantilla. Hay que sustituirlo por el emplazamiento de Tres Cantos
antes de simular nada. En la misma pantalla, las variantes existentes son `VC0: Real`,
`VC2: IncOptima`, `VC3: AcimutOptimo`, `VC4: V1` y `VC5: V2`, y el aviso rojo indica que la escena
3D está dibujada pero **todavía no hay campos FV asignados** a las orientaciones (`PV Fields (0)`,
`Active area 0.00 m²`).

---

## 2. Las superficies definitivas

| Superficie | Valor anterior | Origen anterior | **Valor 3D (19/09/2026)** | Δ |
| --- | --- | --- | --- | --- |
| **V1a** lucernario | 472 m² | Catastro | **578,9109 m²**, horizontal | **+22,7 %** |
| **V1b** cubierta | 2.231 m² de forjado | Catastro menos lucernario y patios | **2.756,8828 m²**, ya neta de ambos | **+23,6 %** |
| **V2** marquesinas | 3.332 m² | Huella de las filas F1–F8 del `TFM.kmz` | **3.536 m²** | **+6,1 %** |

**Fuente:** planos de **Catastro a escala 1:1**, trasladados a mano al editor de escena 3D de
PVsyst, porque el programa no admite DWG/DXF para el cálculo de sombreados. Esta es la frase que
hay que llevar literalmente a la **fase 1.4 de la metodología ERMA**, que exige declarar la fuente
de cada superficie.

### 2.1 La desviación frente a catastro, declarada y no escondida

| Suma del modelo 3D | Referencia | Valor | Desviación |
| --- | --- | --- | --- |
| V1a + V1b = **3.335,79 m²** | Catastro | 3.111 m² | **+7,2 %** |
| ídem | Google Earth | 3.070 m² | +8,7 % |
| ídem | Polígono del `TFM.kmz` | 3.020 m² | +10,5 % |
| Solo V1b = **2.756,88 m²** | Forjado deducido de catastro | 2.231 m² | **+23,6 %** |

Se adopta la medición 3D: está trazada sobre plano a escala y es **la misma geometría que va a
gobernar la simulación de sombras cercanas**, de modo que dimensionado y pérdidas quedan por
primera vez sobre la misma base. Pero la diferencia se declara en la memoria en lugar de dejarla
implícita. La explicación defendible ante el tutor es que **catastro da superficie construida y el
modelo 3D mide polígonos de cubierta**, que no son lo mismo: el segundo recoge vuelos, resaltos y
cuerpos añadidos que la referencia catastral no desglosa.

---

## 3. V1a — BIPV en el lucernario horizontal

```
Superficie 3D del lucernario                     578,9109 m²   (plano horizontal, 0°)
  × 0,80   factor de vidrio activo                463,1  m²  de vidrio FV
  × 125 Wp/m²  (VLT ≈ 20 %)                →       57,89 kWp
```

| Magnitud | Antes (472 m², 5°) | **Ahora (578,91 m², 0°)** |
| --- | --- | --- |
| Potencia | 47,2 kWp | **57,89 kWp** |
| GlobInc anual | 1.857,7 kWh/m² | **1.785,6 kWh/m²** (−3,9 %) |
| Productividad | 1.600 kWh/kWp | **1.540 kWh/kWp** |
| Producción | 76 MWh/año | **89,2 MWh/año** |
| A_PV | 100 % | **100 %** (pico 42 kW contra 437 kW de carga) |
| **C_D sobre 3.832 MWh** | 2,0 % | **2,33 %** |
| **C_D sobre 3.467 MWh** (con geotermia) | 2,2 % | **2,57 %** |

### 3.1 Ser horizontal cuesta, y hay que reportarlo con su signo

Es el único punto donde la geometría real es **peor** que la hipótesis que sustituye. Un plano a 0°
en Madrid recibe un 3,9 % menos de irradiación que uno a 5° orientado al sureste, y V1a pasa a ser
**la superficie que peor rinde de todo el proyecto**:

| Plano | Inclinación | Productividad |
| --- | --- | --- |
| **V1a lucernario** | **0°** | **1.540 kWh/kWp** |
| V1b cubierta | 10° / −30° | 1.612 kWh/kWp |
| V2 marquesinas | 8° / −30° | 1.639 kWh/kWp |

La pérdida absoluta es pequeña —3,4 MWh/año, porque V1a es marginal— pero es una cifra que se
reporta, no se maquilla. En contrapartida, cerrar la pendiente elimina de golpe la horquilla de
**−15 % a +10,5 %** que la revisión 1 tenía abierta sobre la producción de V1a, que era el mayor
factor de incertidumbre que quedaba en la variante.

### 3.2 Las dos sensibilidades que siguen vivas

La transparencia del vidrio, que decidirá el datasheet:

| Transparencia | Densidad | kWp | E_PV | C_D (3.832) | C_D (3.467) |
| --- | --- | --- | --- | --- | --- |
| Alta (VLT > 30 %) | 90 Wp/m² | 41,7 | 64,2 MWh | 1,68 % | 1,85 % |
| **Media (VLT ≈ 20 %)** | **125 Wp/m²** | **57,89** | **89,2 MWh** | **2,33 %** | **2,57 %** |
| Baja (VLT ≈ 10 %) | 160 Wp/m² | 74,1 | 114,1 MWh | 2,98 % | 3,29 % |

Y las sombras y la suciedad, que pesan en un plano horizontal más que en cualquier otro del
proyecto: un acristalamiento a 0° no se autolimpia con la lluvia y recibe la sombra de todos los
petos, casetones y equipos que lo rodean en la cubierta.

| Sombras | Suciedad | E_PV | C_D (3.832) |
| --- | --- | --- | --- |
| **0,5 %** (hipótesis vigente) | **2 %** | **89,2 MWh** | **2,33 %** |
| 5 % | 2 % | 85,4 MWh | 2,23 % |
| 10 % | 3 % | 80,4 MWh | 2,10 % |
| 15 % | 3 % | 76,2 MWh | 1,99 % |

Entre el caso optimista y el pesimista hay **13 MWh y 0,34 pp de C_D**. El valor bueno sale de la
simulación de sombras cercanas, que ya tiene la escena 3D montada: es una de las primeras cosas
que conviene mirar al arrancar la VC1.

> **El encuadre no cambia.** V1a aporta en torno al 2,3 % del consumo. **La justificación del BIPV
> en la memoria es arquitectónica y de control solar, no energética**, y ahora hay un motivo más
> para no forzar el argumento energético: es la superficie que peor rinde por kWp.
>
> Aviso térmico que sigue vigente: el modelo aplica la cadena de pérdidas común con
> **Uc = 20 W/m²·K**. Un BIPV integrado **sin ventilación posterior** trabaja más caliente
> (Uc ≈ 15), así que los 89,2 MWh son **cota superior**; cuenta entre un 1,5 y un 2,5 % menos
> cuando el sub-array se modele con su propio parámetro térmico.

---

## 4. V1b — cubierta de las alas de la H

```
Cubierta de las alas de la H (3D)                2.756,8828 m²
  ├─ ya neta del lucernario (V1a es polígono aparte)
  └─ ya neta de los dos patios interiores (medición por secciones)
  × 0,70   retranqueos, equipos que permanecen, pasillos
           de mantenimiento, casetones de escalera            1.929,8  m²
  × 0,82   factor de aprovechamiento en sheds a 10°           1.582,5  m²  de módulo
  × 226,7 W/m²                                        →         358,74 kWp   ← techo por superficie
```

El 0,70 y el 0,82 se aplican **enteros**. Ninguno de los dos puede estar contenido en un polígono
dibujado sobre el modelo: el 0,70 es un **criterio de ocupación** (retranqueos de seguridad,
equipos que se quedan, pasillos de mantenimiento) y el 0,82 es la **penalización de empaquetado**
en filas a 10°. Leer los 2.756,88 m² como si ya fuesen superficie neta de módulo daría 512 kWp y
sería insostenible ante el tutor: implicaría que en la cubierta de un CPD en explotación no hay ni
retranqueos ni equipos que permanezcan.

### 4.1 El limitante deja de ser la superficie y pasa a ser el inversor

Los 358,74 kWp dan 763 módulos, es decir **63 strings** de 12. Y 63 strings entre 3 inversores
Huawei SUN2000-100KTL-M2 tocan a **21 por inversor**, por encima de las **20 entradas DC** que da
el equipo (10 MPPT × 2 strings). La corriente no es el problema —el informe del trabajo previo da
154 A para 18 strings a 50 °C, es decir **8,6 A por string**, y dos en paralelo caben de sobra en
los 30 A de la entrada—; el problema es el número de entradas.

| Configuración | Strings | Módulos | kWp | Inversores | Ratio DC/AC | Veredicto |
| --- | --- | --- | --- | --- | --- | --- |
| **3 × 20 strings** | **60** | **720** | **338,40** | **3 × 100 kW** | **1,128** | **la de trabajo** |
| 63 strings en 3 inversores | 63 | 756 | 355,32 | 3 × 100 kW | 1,184 | 21 strings/inversor: no caben |
| 63 strings en 4 inversores | 63 | 756 | 355,32 | 4 × 100 kW | 0,888 | ratio bajo, CAPEX peor |
| 63 strings con string de 14 | 54 × 14 | 756 | 355,32 | 3 × 100 kW | 1,184 | posible, pero cambia una decisión ya validada por el tutor |

**Se adopta 60 strings × 12 = 720 módulos = 338,40 kWp.** Tres motivos:

1. **Ratio DC/AC = 1,128**, prácticamente idéntico al **1,13** del trabajo previo que corrigió el
   propio tutor del TFM.
2. **No toca la longitud de string de 12 módulos**, ya validada en la ventana MPP 200–1000 V.
3. **Ocupa el 94,3 %** de la superficie neta (1.492,6 m² de 1.582,5 m²). El 5,7 % restante se
   declara como margen que impone la arquitectura eléctrica, no como superficie desaprovechada.

> **Esto cierra de otra manera el viejo punto abierto del ratio DC/AC.** En la versión de catastro
> (287,6 kWp, 3 inversores) el ratio salía **0,96** y había que justificar que sobraba inversor.
> Con la superficie real el problema se invierte: **sobra cubierta, no inversor**. En términos de
> la **fase 2 de la metodología ERMA**, el criterio más restrictivo de la V1b deja de ser el n.º 2
> (superficie disponible) y pasa a ser una restricción de equipo. Es un cambio de criterio
> limitante y merece una frase explícita en la memoria.
>
> **Queda por verificar** que el SUN2000-100KTL-M2 admite efectivamente 20 entradas DC. El trabajo
> previo montó 18 strings en un solo inversor y nunca llegó al límite, así que ese dato **no está
> todavía en ninguna fuente canónica del proyecto**. Si admitiese más, la configuración buena pasa
> a ser 63 × 12 = 355,32 kWp con ratio 1,184 y C_D 14,95 %.

### 4.2 Resultado de V1b

| Magnitud | Antes (1.562 m² netos) | **Ahora (338,40 kWp)** | Techo por superficie (355,32 kWp) |
| --- | --- | --- | --- |
| Potencia | 290,3 kWp | **338,40 kWp** | 355,32 kWp |
| Producción | 468 MWh/año | **545,6 MWh/año** | 572,9 MWh/año |
| Productividad | 1.612 kWh/kWp | **1.612 kWh/kWp** | 1.612 kWh/kWp |
| A_PV | 100 % | **100 %** (pico 244 kW) | 100 % (pico 256 kW) |
| **C_D sobre 3.832 MWh** | 12,2 % | **14,24 %** | 14,95 % |
| **C_D sobre 3.467 MWh** | 13,5 % | **15,74 %** | 16,52 % |

---

## 5. V2 — marquesinas (3.536 m²)

```
Huella de marquesinas (3D)                       3.536,0 m²
  × 0,90   ocupación de módulo sobre la marquesina 3.182,4 m²
  × 226,7 W/m²                               →      721,45 kWp   ← techo por superficie
```

**El reparto de strings queda abierto por decisión expresa de Mario**, para cerrarlo dentro de
PVsyst. Las dos opciones son viables y las dos están calculadas; ninguna se fija como definitiva:

| | **127 strings × 12** | **126 strings × 12** |
| --- | --- | --- |
| Módulos | 1.524 | 1.512 |
| **Potencia** | **716,28 kWp** | **710,64 kWp** |
| Superficie de módulo | 3.159,3 m² ✔ | 3.134,4 m² ✔ |
| Inversores | 7, reparto **no uniforme** (127 es primo) | **7 × 18 exactos** |
| Ratio DC/AC | 1,023 | 1,015 |
| E_PV | 1.173,7 MWh | 1.164,5 MWh |
| **C_D (3.832 MWh)** | **30,20 %** | **30,01 %** |
| Excedentes recortados | 16,5 MWh en 559 h | 14,4 MWh en 520 h |

A favor de 127: aprovecha 5,6 kWp más de una superficie que ya está pagada. A favor de 126: el
unifilar y la tabla de la fase 6 de ERMA quedan simétricos, y el ratio coincide con el criterio
del resto del proyecto. La diferencia es de **0,19 puntos de C_D**, así que la decisión es de
claridad documental, no de ingeniería.

| Magnitud | Antes (3.332 m²) | **Ahora (716,28 kWp)** | Con geotermia |
| --- | --- | --- | --- |
| Potencia | 679,8 kWp | **716,28 kWp** | ídem |
| Producción | 1.114 MWh/año | **1.173,7 MWh/año** (1.639 kWh/kWp) | ídem |
| Pico de generación | ~500 kW | **529 kW** | ídem |
| **A_PV** | 99,5 % | **98,6 %** | **95,8 %** |
| Excedentes | 5 MWh (355 h) | **16,5 MWh (559 h)** | **49,5 MWh (957 h)** |
| **C_D sobre 3.832 MWh** | 28,9 % | **30,20 %** | — |
| **C_D sobre 3.467 MWh** | 31,3 % | — | **32,43 %** |

### 5.1 V2 ya no es «excedente testimonial»

Con 3.332 m² el excedente eran 5 MWh/año y se podía despachar como irrelevante. Con 3.536 m² el
pico sube a **529 kW**, ya por encima de los 437 kW de carga media, y el excedente pasa a
**16,5 MWh/año en 559 horas** — **49,5 MWh en 957 horas, un 4,2 % de la producción**, si la
geotermia entra en el alcance.

Como V2 está planteada como **autoconsumo sin excedentes con antivertido**, esos MWh **no se
exportan: se pierden**, recortados por el limitador.

| Escenario | Excedente recortado | Batería mínima para vertido cero | Ganancia de C_D con batería infinita |
| --- | --- | --- | --- |
| V2 sin geotermia | 16,5 MWh | **0,16 MWh** | +0,36 pp |
| V2 con geotermia | 49,5 MWh | **0,38 MWh** | +1,21 pp |

> **La conclusión de fondo no cambia: la batería sigue sin justificarse en V2.** Un pack de
> 0,16–0,38 MWh para recuperar entre 16 y 50 MWh anuales no lo paga nadie. Pero **sí cambia el
> matiz que hay que escribir en la memoria**: ya no se puede decir que V2 «nunca vierte». Vierte
> 559 horas al año y el antivertido recorta un 1,4 % de la producción (4,2 % con geotermia). Es un
> dato que hay que declarar en el capítulo de resultados, no esconderlo, y que además da pie al
> argumento correcto: V2 está **justo en el límite** de lo que el CPD puede absorber, y cualquier
> ampliación por encima de esa huella exige ya almacenamiento o cambiar de modalidad.

---

## 6. Tabla de síntesis

Todas las cifras del modelo horario calibrado. Consumo de referencia: **3.832 MWh/año** sin
geotermia y **3.467 MWh/año** con ella (−365 MWh, ver `estimacion-preliminar-variantes.md` §5.2).

### 6.1 Sin geotermia (denominador 3.832 MWh)

| Variante | kWp | E_PV (MWh) | kWh/kWp | A_PV | **C_D** | Excedentes | h vertido | Pico |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **V1a** BIPV lucernario 0° | **57,9** | **89,2** | 1.540 | 100 % | **2,33 %** | 0 | 0 | 42 kW |
| **V1b** cubierta (3 × 20 strings) | **338,4** | **545,6** | 1.612 | 100 % | **14,24 %** | 0 | 0 | 244 kW |
| V1b techo por superficie | 355,3 | 572,9 | 1.612 | 100 % | 14,95 % | 0 | 0 | 256 kW |
| **V1 = V1a + V1b** | **396,3** | **634,8** | 1.602 | 100 % | **16,56 %** | 0 | 0 | 286 kW |
| **V2** marquesinas 127 strings | **716,3** | **1.173,7** | 1.639 | **98,6 %** | **30,20 %** | 16,5 | 559 | 529 kW |
| V2 marquesinas 126 strings | 710,6 | 1.164,5 | 1.639 | 98,8 % | 30,01 % | 14,4 | 520 | 525 kW |
| **V1 + V2 (127)** | **1.112,6** | **1.808,5** | 1.625 | **80,4 %** | **37,94 %** | 354,6 | 2.147 | 814 kW |
| V1 + V2 (126) | 1.106,9 | 1.799,2 | 1.625 | 80,7 % | 37,87 % | 347,9 | 2.135 | 810 kW |

### 6.2 Con geotermia (denominador 3.467 MWh)

| Variante | kWp | E_PV (MWh) | A_PV | **C_D** | Excedentes | h vertido |
| --- | --- | --- | --- | --- | --- | --- |
| **V1a** BIPV lucernario 0° | 57,9 | 89,2 | 100 % | **2,57 %** | 0 | 0 |
| **V1b** cubierta (3 × 20 strings) | 338,4 | 545,6 | 100 % | **15,74 %** | 0 | 0 |
| V1b techo por superficie | 355,3 | 572,9 | 100 % | 16,52 % | 0 | 0 |
| **V1 = V1a + V1b** | **396,3** | **634,8** | 100 % | **18,31 %** | 0 | 0 |
| **V2** marquesinas 127 strings | **716,3** | **1.173,7** | **95,8 %** | **32,43 %** | 49,5 | 957 |
| V2 marquesinas 126 strings | 710,6 | 1.164,5 | 96,0 % | 32,26 % | 46,0 | 925 |
| **V1 + V2 (127)** | **1.112,6** | **1.808,5** | **75,0 %** | **39,13 %** | 451,8 | 2.447 |

### 6.3 Delta frente a las cifras que estaban en circulación

| | Catastro / KMZ | Revisión 1 (lectura A) | **Revisión 2, cerrada** | Δ sobre catastro |
| --- | --- | --- | --- | --- |
| V1a | 47,2 kWp · 2,0 % | 57,9 kWp · 2,42 % | **57,89 kWp · 2,33 %** | **+22,7 %** |
| V1b | 290,3 kWp · 12,2 % | 304,56 kWp · 12,81 % | **338,40 kWp · 14,24 %** | **+16,6 %** |
| **V1** | 337,5 kWp · 14,2 % | 362,5 kWp · 15,23 % | **396,3 kWp · 16,56 %** | **+17,4 %** |
| **V2** | 679,8 kWp · 28,9 % | 716,28 kWp · 30,20 % | **716,28 kWp · 30,20 %** | +5,4 % |
| V1 + V2 | 1.017 kWp · 36,8 % | 1.078,7 kWp · 37,56 % | **1.112,6 kWp · 37,94 %** | **+9,4 %** |

**Ninguna conclusión estratégica del análisis preliminar se cae.** V2 sigue siendo la mejor
variante con diferencia y sigue aportando casi el doble que toda la cubierta del edificio; V1a
sigue siendo marginal en energía; la batería sigue sin justificarse ni en V1 ni en V2 por separado;
y la barrera estructural del 50,5 % de autosuficiencia sin almacenamiento sigue intacta.

Tres datos nuevos que sí merecen anotarse:

1. **V2 cruza el 30 % de autosuficiencia** y **V1 + V2 llega al 37,94 %** (39,13 % con geotermia),
   a menos de 13 puntos del techo físico del 50,5 %.
2. **V1 + V2 vierte 354,6 MWh en 2.147 horas** y el A_PV cae al 80,4 %. Ese es el primer escenario
   del proyecto en el que la batería tiene algo real que hacer **sin necesidad de llegar a la
   planta en suelo**, y hay que calcularlo con el modelo horario antes de afirmar nada.
3. **El criterio limitante de la V1b ha cambiado de naturaleza**: ya no manda la superficie, manda
   el número de entradas DC del inversor.

---

## 7. Qué queda abierto

| # | Asunto | Qué decide | Quién lo cierra |
| --- | --- | --- | --- |
| **1** | **N.º de entradas DC del SUN2000-100KTL-M2** | 338,40 kWp (ratio 1,128) frente a 355,32 kWp (ratio 1,184) en V1b. 17 kWp y 0,7 pp de C_D | Datasheet de Huawei → `bibliotecario-pdf` |
| **2** | **Reparto de strings de V2: 126 o 127** | El unifilar de V2 y la tabla de la fase 6 de ERMA. **Diferido expresamente por Mario** | Mario, en la fase de sistema de la VC2 en PVsyst |
| **3** | Sombreado real sobre el lucernario horizontal | 13 MWh y 0,34 pp de C_D en V1a | Simulación de sombras cercanas sobre la escena 3D ya montada |
| **4** | Datasheet del vidrio BIPV | La densidad Wp/m² de V1a (41,7 a 74,1 kWp según VLT) | Mario → `bibliotecario-pdf` |
| **5** | Emplazamiento del proyecto PVsyst | Ahora mismo apunta a Carrasqueira (Portugal). Bloquea cualquier simulación | Mario, antes de arrancar la VC0 |

---

## 8. Qué hay que corregir en los documentos ya escritos

| Documento | Estado |
| --- | --- |
| `conocimiento fotovoltaico/Referencia/guia-diseno-pvsyst.md` | **Reescrito** (revisión 2): §0 rehecho con las superficies y la fuente, §0bis eliminado, §5, §6, §7.1, §7.2, §10.1, §12, §13 y §14 actualizados |
| `Memoria/analisis/estimacion-preliminar-variantes.md` | **Reescrito** (revisión 3): §4, §5, §5.1, §5.3, §5bis.1, §5bis.2, resumen ejecutivo y pendientes |
| Memoria persistente | `project-v1a-lucernario-bipv`, `project-v1b-cubierta-liberada-geotermia`, `project-consumo-real-cpd` y `project-localizacion-cpd-parcela-v3` contienen las superficies antiguas |
| Cifras combinadas de `estimacion-preliminar-variantes.md` §5.6 y §6 | Siguen calculadas sobre la versión del KMZ. Quedan del lado conservador y **no se han rehecho**: si se usan en la memoria, recalcular primero |

**Lo que no cambia y conviene decirlo explícitamente:** la premisa geotérmica sigue siendo la
condición de existencia de V1b (sin ella la cubierta vuelve a los 450 m² del trabajo previo,
midiéndose como se mida), la decisión de BIPV para V1a está tomada y no se reabre, y la modalidad
de autoconsumo de cada variante (§5bis.4 del análisis preliminar) no se ve afectada por un cambio
de superficie.
