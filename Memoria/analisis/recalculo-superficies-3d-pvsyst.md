---
title: "Recálculo de V1a, V1b y V2 con las superficies medidas sobre el modelo 3D de PVsyst"
fecha: 2026-09-19
estado: preliminar
revision: 1
sustituye_a: "Memoria/analisis/estimacion-preliminar-variantes.md §4.2, §5.1 y §5.3 (superficies y potencias)"
script: "Memoria/analisis/scripts/recalc_superficies_3d.py"
fuentes_canonicas:
  - "Medición de Mario sobre el modelado 3D de PVsyst (19/09/2026): V1a 578,9109 m² · V1b 2.756,8828 m² · V2 3.536 m²"
  - "Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv (3.832,0 MWh/año, 8.760 h)"
  - "Memoria/analisis/scripts/solar.py (modelo horario calibrado, −1,3 % frente al informe PVsyst del trabajo previo)"
  - "Documentacion de apoyo/Trabajo Autoconsumo CPD/Trabajo_DataCenter_Project.VC0-Report1.pdf"
tags: [fotovoltaica, autoconsumo, CPD, variantes, superficies, BIPV, marquesinas, PVsyst, geometria]
---

# Recálculo de V1a, V1b y V2 con las superficies del modelo 3D

> **Qué es este documento.** Mario ha medido las tres superficies directamente sobre el modelado
> 3D que ha construido en PVsyst (con el *near shading* ya resuelto para V1 y V2). Esas cifras
> sustituyen a las estimaciones por catastro, Google Earth y KMZ que venía usando
> `estimacion-preliminar-variantes.md`. Este documento comprueba su coherencia, recalcula
> potencia, producción y autosuficiencia, y deja aislado lo que **no se puede cerrar sin
> preguntarle a Mario**.
>
> El modelo horario, la cadena de pérdidas y el perfil de carga no cambian: son los mismos que ya
> estaban calibrados contra el informe PVsyst del trabajo previo. **Lo único que cambia es la
> geometría de entrada.** Cálculo reproducible en `scripts/recalc_superficies_3d.py`.

---

## 1. Las cifras nuevas frente a las antiguas

| Superficie | Valor anterior | Origen anterior | **Valor 3D (19/09/2026)** | Δ |
| --- | --- | --- | --- | --- |
| **V1a** lucernario | 472 m² | Catastro (proyección horizontal) | **578,9109 m²** | **+22,7 %** |
| **V1b** cubierta | 2.231 m² de forjado → 1.562 m² netos | Catastro menos lucernario y patios, × 0,70 | **2.756,8828 m²** | **ver §3** |
| **V2** marquesinas | 3.332 m² | Huella de las filas F1–F8 del `TFM.kmz` | **3.536 m²** | **+6,1 %** |

### 1.1 La comprobación que hay que hacer primero

Antes de recalcular nada conviene sumar las dos superficies de cubierta y contrastarlas contra las
tres mediciones independientes del edificio que ya existen:

| Suma del modelo 3D | Referencia | Valor | Desviación |
| --- | --- | --- | --- |
| V1a + V1b = **3.335,79 m²** | Catastro | 3.111 m² | **+7,2 %** |
| ídem | Google Earth | 3.070 m² | +8,7 % |
| ídem | Polígono del `TFM.kmz` | 3.020 m² | +10,5 % |

**El modelo 3D mide entre un 7 y un 10 % más de cubierta que cualquiera de las tres fuentes
previas.** Eso no invalida la medición —un modelo 3D trazado con cuidado puede ser más fiel que un
polígono de catastro—, pero sí obliga a explicar de dónde sale la diferencia antes de propagarla a
la potencia instalada. Y la explicación no es la misma para V1a que para V1b.

---

## 2. V1a (578,9109 m²): la desviación no es ruido de medición, es información

Los 578,91 m² son **+22,7 %** sobre los 472 m² de catastro. Esa cifra es demasiado grande para
atribuirla a precisión de trazado, y demasiado redonda para ser casualidad:

```
578,9109 / 472 = 1,2265        →        arccos(1 / 1,2265) = 35,4°
```

Es decir: **si los 578,91 m² son la superficie *desarrollada* del lucernario y los 472 m² su
proyección horizontal, la pendiente implícita es de 35,4°**, no los 5° que se venían suponiendo.
La otra lectura posible es que el polígono 3D incluya la perfilería perimetral y los antepechos,
que en catastro no cuentan. Nótese además que los 578,91 m² caen justo entre los 472 m² de
catastro y los 614 m² que daba Google Earth, y que ya en su día se sospechó que Google Earth estaba
midiendo superficie desarrollada (`estimacion-preliminar-variantes.md` §4.1).

**Para el BIPV, la superficie desarrollada es la cifra correcta**: el vidrio fotovoltaico sustituye
al acristalamiento real, que es el inclinado, no su sombra en planta. Así que los 578,91 m² se
adoptan sin corrección. Lo que no se puede seguir arrastrando es la pendiente de 5°.

### 2.1 Por qué esto importa mucho más que el +22,7 % de superficie

| Hipótesis de geometría | GlobInc anual | Frente a la hipótesis actual |
| --- | --- | --- |
| Plano único 5° / −30° (hipótesis vigente) | 1.857,7 kWh/m² | referencia |
| Plano único 20° / −30° | 2.007,1 kWh/m² | +8,0 % |
| **Plano único 35° / −30°** | **2.053,5 kWh/m²** | **+10,5 %** |
| Faldón orientado al norte, 35° (azimut +150°) | 1.098,6 kWh/m² | **−40,9 %** |
| **A dos aguas 35°: mitad −30° y mitad +150°** | **1.576,0 kWh/m²** | **−15,2 %** |

La horquilla va de **−15 % a +10,5 %** según lo que sea realmente el lucernario. Es el mayor
factor de incertidumbre que queda en V1a, muy por encima del propio dato de superficie, y coincide
con el aviso que ya se añadió a la guía de PVsyst (`guia-diseno-pvsyst.md` §6, nota del
19/09/2026) sobre si el lucernario es un plano único o varios faldones. **La medición 3D refuerza
esa sospecha en lugar de despejarla.**

### 2.2 Resultado de V1a con la hipótesis vigente

Criterio de la guía (§7.2), sin cambios: factor de vidrio activo 0,80 y 125 Wp/m² para VLT ≈ 20 %.

```
Superficie 3D del lucernario                     578,91 m²
  × 0,80   factor de vidrio activo                463,13 m²  de vidrio FV
  × 125 Wp/m²  (VLT ≈ 20 %)                →       57,9 kWp
```

| Magnitud | Antes (472 m²) | **Ahora (578,91 m²)** |
| --- | --- | --- |
| Potencia | 47,2 kWp | **57,9 kWp** |
| Producción | 76 MWh/año | **92,6 MWh/año** (1.600 kWh/kWp) |
| A_PV | 100 % | **100 %** (pico 42 kW contra 437 kW de carga) |
| **C_D sobre 3.832 MWh** | 2,0 % | **2,42 %** |
| **C_D sobre 3.467 MWh** (con geotermia) | 2,2 % | **2,67 %** |

Sensibilidad a la transparencia del vidrio, recalculada:

| Transparencia | Densidad | kWp | E_PV | C_D (3.832) | C_D (3.467) |
| --- | --- | --- | --- | --- | --- |
| Alta (VLT > 30 %) | 90 Wp/m² | 41,7 | 66,7 MWh | 1,74 % | 1,92 % |
| **Media (VLT ≈ 20 %)** | **125 Wp/m²** | **57,9** | **92,6 MWh** | **2,42 %** | **2,67 %** |
| Baja (VLT ≈ 10 %) | 160 Wp/m² | 74,1 | 118,5 MWh | 3,09 % | 3,42 % |

> **El encuadre no cambia.** V1a sigue aportando en torno al 2,4 % del consumo. Sube desde el
> 2,0 %, pero sigue siendo marginal en energía: **la justificación del BIPV en la memoria es
> arquitectónica y de control solar, no energética.** Forzar el argumento energético sigue siendo
> el error fácil de este apartado.
>
> Aviso adicional sobre los 1.600 kWh/kWp: el modelo aplica la misma cadena de pérdidas que el
> resto de variantes, con Uc = 20 W/m²·K. Un BIPV integrado **sin ventilación posterior** trabaja
> más caliente (Uc ≈ 15), así que los 92,6 MWh son **cota superior**; cabe esperar entre un 1,5 y
> un 2,5 % menos cuando el sub-array se modele con su propio parámetro térmico.

---

## 3. V1b (2.756,8828 m²): la cifra es ambigua y no se puede cerrar sin preguntar

Este es el punto delicado del recálculo. **No se puede dar por supuesto que los 2.756,88 m² sean
superficie neta de módulo**, porque la cascada de la guía (§7.1) tiene tres peldaños y no consta
cuáles ha recorrido ya la medición de Mario:

```
Cubierta total (catastro)                                   3.111 m²
  − lucernario                                              −  472 m²   ← ¿descontado en el 3D? SÍ (V1a es polígono aparte)
  − patios interiores (2 patios, medidos en píxeles)        −  408 m²   ← ¿descontado en el 3D? DESCONOCIDO
  = forjado de cubierta                                      2.231 m²
  × 0,70   retranqueos, equipos que permanecen, pasillos
           de mantenimiento, casetones de escalera           1.561,7 m² ← ¿aplicado en el 3D? NO (es un criterio, no geometría)
  × 0,82   factor de aprovechamiento en sheds a 10°          1.280,6 m²
  × 226,7 W/m²                                        →        290,3 kWp
```

Los factores 0,70 y 0,82 **no pueden estar en la medición 3D**: el 0,70 es un criterio de
ocupación (retranqueos de seguridad, equipos que se quedan, pasillos) y el 0,82 es la penalización
de empaquetado en filas a 10°. Un polígono dibujado sobre el modelo no los contiene. Así que la
cifra de Mario es, con seguridad, **superficie bruta**, y hay que aplicárselos.

Lo que sí está abierto es **si esos 2.756,88 m² descuentan o no los dos patios interiores**.

### 3.1 Las tres lecturas posibles

| Lectura | Supuesto | Cascada | kWp bruto |
| --- | --- | --- | --- |
| **A** | La cifra es bruta y **aún incluye los patios** | (2.756,88 − 408) × 0,70 × 0,82 × 226,7 | **305,7 kWp** |
| **B** | La cifra **ya excluye** lucernario y patios | 2.756,88 × 0,70 × 0,82 × 226,7 | **358,7 kWp** |
| **C** | La cifra es **superficie neta disponible** | 2.756,88 × 0,82 × 226,7 | 512,5 kWp ← **incorrecta, no usar** |

La lectura C es la trampa: es la que sale de leer «2.756,88 m² de cubierta candidata a módulos»
como si ya fuese el resultado de aplicar el 0,70. Daría un salto del +76 % sobre los 290 kWp
anteriores y sería insostenible ante el tutor, porque implicaría que en la cubierta de un CPD en
explotación no hay ni retranqueos de seguridad ni equipos que permanezcan.

### 3.2 Cuál de las dos lecturas válidas es más probable

El contraste con catastro deshace buena parte del empate:

| Lectura | Forjado de cubierta implícito | Catastro | Desviación |
| --- | --- | --- | --- |
| **A** | 2.756,88 − 408 = **2.348,9 m²** | 2.231 m² | **+5,3 %** |
| **B** | **2.756,9 m²** | 2.231 m² | **+23,6 %** |

El modelo 3D mide un **+7,2 %** más de cubierta total que catastro (§1.1). La lectura A produce
una desviación del **+5,3 %** en el forjado, perfectamente coherente con ese sesgo global. La
lectura B exigiría un **+23,6 %**, que ninguna diferencia de trazado explica: serían 526 m² de
forjado que catastro no ve.

> **Por tanto se adopta la lectura A (305,7 kWp) como cifra de trabajo**, y la B (358,7 kWp) se
> deja anotada como techo superior condicionado a que Mario confirme que en su modelo 3D **los dos
> patios interiores están recortados como huecos**. Adoptar la más restrictiva de dos lecturas
> defendibles es, además, lo que pide la fase 2 de la metodología ERMA: se instala la potencia que
> resulta del criterio más restrictivo.

### 3.3 Traducción a módulos, strings e inversores

| Concepto | **Lectura A (trabajo)** | Lectura B (techo) |
| --- | --- | --- |
| Superficie de módulo | 1.348,3 m² | 1.582,5 m² |
| Módulos REC Alpha Pure-RX 470 Wp | **648** | 756 |
| Strings × módulos en serie | **54 × 12** | 63 × 12 |
| **Potencia real instalada** | **304,56 kWp** | **355,32 kWp** |
| Superficie ocupada por módulo | 1.343,3 m² ✔ | 1.567,2 m² ✔ |
| Inversores Huawei SUN2000-100KTL-M2 | **3** (18 strings cada uno) | 3 (21 strings cada uno) |
| **Ratio DC/AC** | **1,015** | 1,184 |

> **Un efecto lateral que conviene señalar: la lectura A resuelve sola la objeción del ratio
> DC/AC.** La guía (§7.1) dejaba abierto que con 287,6 kWp y tres inversores de 100 kW el ratio
> salía **0,96**, un valor bajo que había que justificar o corregir. Con 304,56 kWp el reparto es
> **54 strings entre 3 inversores = 18 strings exactos cada uno** y el ratio sube a **1,015**. El
> punto abierto n.º 3 de la guía deja de ser un problema: ya no sobra inversor.

### 3.4 Resultado de V1b

| Magnitud | Antes (1.562 m² netos) | **Lectura A** | Lectura B |
| --- | --- | --- | --- |
| Potencia | 290,3 kWp | **304,56 kWp** | 355,32 kWp |
| Producción | 468 MWh/año | **491,0 MWh/año** | 572,9 MWh/año |
| Productividad | 1.612 kWh/kWp | **1.612 kWh/kWp** | 1.612 kWh/kWp |
| A_PV | 100 % | **100 %** (pico 220 kW) | 100 % (pico 256 kW) |
| **C_D sobre 3.832 MWh** | 12,2 % | **12,81 %** | 14,95 % |
| **C_D sobre 3.467 MWh** | 13,5 % | **14,16 %** | 16,52 % |

---

## 4. V2 marquesinas (3.536 m²)

Los 3.536 m² son **+6,1 %** sobre los 3.332 m² de las filas F1–F8 del KMZ. Es una diferencia del
mismo orden que el sesgo general del modelo 3D y no plantea ninguna ambigüedad de método: la
marquesina es una estructura nueva, su superficie es la que se proyecte, y el criterio cerrado
(`estimacion-preliminar-variantes.md` §5.3) es huella × 0,90 de ocupación de módulo.

```
Huella de marquesinas (3D)                       3.536,0 m²
  × 0,90   ocupación de módulo sobre la marquesina 3.182,4 m²
  × 226,7 W/m²                               →      721,5 kWp
```

| Concepto | Valor |
| --- | --- |
| Módulos | 1.524 |
| Strings × serie | 127 × 12 |
| **Potencia real** | **716,28 kWp** |
| Superficie de módulo | 3.159,3 m² ✔ cabe en 3.182,4 |

> **Aviso de reparto por inversor.** 127 es primo: no se reparte en partes iguales entre
> inversores. Bajando a **126 strings (7 × 18)** salen 1.512 módulos = **710,64 kWp**, con
> **7 × SUN2000-100KTL-M2** y ratio DC/AC = **1,015**, el mismo criterio que V1b lectura A. La
> producción baja a **1.164,5 MWh** y el C_D a **30,0 %**. Es la configuración recomendada por
> simetría con V1b; las cifras de la tabla siguiente son las de 716,28 kWp y la diferencia es de
> décimas.

| Magnitud | Antes (3.332 m²) | **Ahora (3.536 m²)** | Con geotermia |
| --- | --- | --- | --- |
| Potencia | 679,8 kWp | **716,28 kWp** | ídem |
| Producción | 1.114 MWh/año | **1.173,7 MWh/año** (1.639 kWh/kWp) | ídem |
| Pico de generación | ~500 kW | **529 kW** | ídem |
| **A_PV** | 99,5 % | **98,6 %** | **95,8 %** |
| Excedentes | 5 MWh (355 h) | **16,5 MWh (559 h)** | **49,5 MWh (957 h)** |
| **C_D sobre 3.832 MWh** | 28,9 % | **30,20 %** | — |
| **C_D sobre 3.467 MWh** | 31,3 % | — | **32,43 %** |

### 4.1 El detalle que cambia de signo: V2 ya no es «excedente testimonial»

Con 3.332 m² el excedente eran 5 MWh/año y se podía despachar como irrelevante. Con 3.536 m² el
pico sube a **529 kW**, ya claramente por encima de los 437 kW de carga media, y el excedente pasa
a **16,5 MWh/año en 559 horas**. Y si la geotermia entra en el alcance, la carga baja y el
excedente se triplica hasta **49,5 MWh en 957 horas**, un **4,2 % de la producción**.

Esto tiene una consecuencia práctica concreta, porque V2 está planteada como **autoconsumo sin
excedentes con antivertido**: esos MWh **no se exportan, se pierden**. Son producción recortada por
el limitador. Cuantificado:

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

## 5. Tabla de síntesis

Todas las cifras del modelo horario calibrado. Consumo de referencia: **3.832 MWh/año** sin
geotermia y **3.467 MWh/año** con ella (−365 MWh, ver `estimacion-preliminar-variantes.md` §5.2).

### 5.1 Sin geotermia (denominador 3.832 MWh)

| Variante | kWp | E_PV (MWh) | kWh/kWp | A_PV | **C_D** | Excedentes | Pico |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **V1a** BIPV lucernario | 57,9 | 92,6 | 1.600 | 100 % | **2,42 %** | 0 | 42 kW |
| **V1b** cubierta — **lectura A** | **304,6** | **491,0** | 1.612 | 100 % | **12,81 %** | 0 | 220 kW |
| V1b cubierta — lectura B | 355,3 | 572,9 | 1.612 | 100 % | 14,95 % | 0 | 256 kW |
| **V1 = V1a + V1b (A)** | **362,5** | **583,7** | 1.610 | 100 % | **15,23 %** | 0 | 262 kW |
| V1 = V1a + V1b (B) | 413,2 | 665,5 | 1.611 | 100 % | 17,37 % | 0 | 298 kW |
| **V2** marquesinas | **716,3** | **1.173,7** | 1.639 | **98,6 %** | **30,20 %** | 16,5 | 529 kW |
| **V1(A) + V2** | 1.078,7 | 1.757,4 | 1.629 | 81,9 % | **37,56 %** | 317,9 | 791 kW |
| V1(B) + V2 | 1.129,5 | 1.839,2 | 1.628 | 79,5 % | 38,15 % | 377,3 | 827 kW |

### 5.2 Con geotermia (denominador 3.467 MWh)

| Variante | kWp | E_PV (MWh) | A_PV | **C_D** | Excedentes |
| --- | --- | --- | --- | --- | --- |
| **V1a** BIPV lucernario | 57,9 | 92,6 | 100 % | **2,67 %** | 0 |
| **V1b** cubierta — **lectura A** | **304,6** | **491,0** | 100 % | **14,16 %** | 0 |
| V1b cubierta — lectura B | 355,3 | 572,9 | 100 % | 16,52 % | 0 |
| **V1 = V1a + V1b (A)** | **362,5** | **583,7** | 100 % | **16,83 %** | 0 |
| V1 = V1a + V1b (B) | 413,2 | 665,5 | 100 % | 19,20 % | 0 |
| **V2** marquesinas | **716,3** | **1.173,7** | **95,8 %** | **32,43 %** | 49,5 |
| **V1(A) + V2** | 1.078,7 | 1.757,4 | 76,6 % | **38,81 %** | 411,8 |

### 5.3 Delta frente a las cifras que estaban en circulación

| | Antes | **Ahora (lectura A)** | Δ potencia | Δ C_D |
| --- | --- | --- | --- | --- |
| V1a | 47,2 kWp · 2,0 % | **57,9 kWp · 2,42 %** | +22,7 % | +0,4 pp |
| V1b | 290,3 kWp · 12,2 % | **304,6 kWp · 12,81 %** | +4,9 % | +0,6 pp |
| **V1** | 337,5 kWp · 14,2 % | **362,5 kWp · 15,23 %** | +7,4 % | **+1,0 pp** |
| **V2** | 679,8 kWp · 28,9 % | **716,3 kWp · 30,20 %** | +5,4 % | **+1,3 pp** |
| V1 + V2 | 1.017 kWp · 36,8 % | **1.078,7 kWp · 37,56 %** | +6,1 % | +0,8 pp |

**Ninguna conclusión estratégica del análisis preliminar se cae.** V2 sigue siendo la mejor
variante con diferencia y sigue aportando el doble que toda la cubierta del edificio; V1a sigue
siendo marginal en energía; la batería sigue sin justificarse ni en V1 ni en V2; y la barrera
estructural del 50,5 % de autosuficiencia sin almacenamiento sigue intacta. Lo que hay es un
desplazamiento de escala de en torno a **+1 punto de C_D por variante**.

Dato nuevo que sí merece anotarse: **V2 cruza por primera vez el 30 % de autosuficiencia**, y
**V1 + V2 llega al 37,6 %** (38,8 % con geotermia), a menos de 13 puntos del techo físico del
50,5 %.

---

## 6. Qué hay que preguntarle a Mario

| # | Pregunta | Qué decide | Impacto |
| --- | --- | --- | --- |
| **1** | **¿Los 2.756,88 m² de V1b descuentan los dos patios interiores?** En el modelo 3D, ¿los patios están recortados como huecos o el polígono pasa por encima? | Elige entre lectura A (304,6 kWp) y lectura B (355,3 kWp) | **50,8 kWp y 2,1 pp de C_D.** Es la pregunta más importante de esta lista |
| **2** | **¿Cuál es la pendiente real del lucernario, y es un plano único o varios faldones?** El cociente 578,91 / 472 apunta a ~35°, no a los 5° supuestos | La orientación del sub-array BIPV | De **−15 % a +10,5 %** sobre la producción de V1a. Si hay un faldón al norte, ese faldón pierde el 41 % |
| **3** | ¿Los 578,91 m² son superficie desarrollada (el acristalamiento real) o proyección en planta? | Si hay que corregir la superficie de vidrio | Si fuese proyección, V1a vuelve a ~47 kWp |
| **4** | ¿Sobre qué base se ha trazado el 3D — satélite, plano de cubiertas, levantamiento? | Explica el sesgo sistemático del +7,2 % frente a catastro y permite decidir qué fuente manda en la fase 1.4 de ERMA | Trazabilidad ante el tutor: la fase 1.4 exige declarar la fuente de cada superficie |
| **5** | ¿Confirma el reparto de V2 en 126 strings (7 × 18 inversores, DC/AC 1,015) en lugar de 127? | El esquema eléctrico de V2 | Décimas de producción, pero cierra el unifilar |

> **Sobre la pregunta 1 y cómo resolverla sin esperar.** Si Mario puede exportar del 3D la
> superficie de cada polígono por separado, basta con ver si existen dos polígonos de unos 200 m²
> cada uno (los patios) o si no están. También sirve mirar si la suma de los polígonos de cubierta
> del 3D da 2.756,88 m² con los patios dentro o fuera.

---

## 7. Qué hay que corregir en los documentos ya escritos

| Documento | Qué cambia |
| --- | --- |
| `Memoria/analisis/estimacion-preliminar-variantes.md` | §4.2, §5.1, §5.3, §5bis.1, §5bis.2 y el resumen ejecutivo usan 472 / 1.562 / 3.332 m² y 47 / 290 / 680 kWp. Quedan superados por este documento. Se ha añadido un aviso al principio |
| `conocimiento fotovoltaico/Referencia/guia-diseno-pvsyst.md` | §0, §5, §6, §7.1, §7.2, §10.1 y §12: la banda de aceptación de la VC1 (464 / 540 MWh, C_D 12,1 / 14,1 %) y el número de módulos (612, 51 strings) están calculados sobre 1.562 m². Hay que rehacerlos con 304,56 kWp. El punto abierto n.º 3 (ratio DC/AC 0,96) queda resuelto: con la lectura A sale 1,015 |
| Memoria persistente | `project-v1a-lucernario-bipv`, `project-v1b-cubierta-liberada-geotermia`, `project-consumo-real-cpd` y `project-localizacion-cpd-parcela-v3` contienen las superficies antiguas |

**Lo que no cambia y conviene decirlo explícitamente:** la premisa geotérmica sigue siendo la
condición de existencia de V1b (sin ella la cubierta vuelve a los 450 m² del trabajo previo,
midiéndose como se mida), la decisión de BIPV para V1a está tomada y no se reabre, y la modalidad
de autoconsumo de cada variante (§5bis.4 del análisis preliminar) no se ve afectada por un cambio
de superficie del 5 %.
