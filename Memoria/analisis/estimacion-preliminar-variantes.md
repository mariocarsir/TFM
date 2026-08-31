---
title: "Estimación preliminar de las tres variantes de autoconsumo FV del CPD"
fecha: 2026-08-23
actualizado: 2026-08-28
revision: 2  # V2 corregida a 3.332 m2 + marco regulatorio 2026
estado: preliminar
margen_objetivo: "5–8 %"
fuentes_canonicas:
  - "Datos/Consumo CPD/Mensual/ (12 ficheros, resolución 5 min, dic-2024 → nov-2025)"
  - "Documentacion de apoyo/Trabajo Autoconsumo CPD/Trabajo_DataCenter_Project.VC0-Report1.pdf (PVsyst V8.0.19)"
  - "Datos/Imagenes/PlantaCPD.png y VistaSatelitalCPD.png (Google Earth)"
  - "Datos/Google Earth/TFM.kmz (polígonos de parcela, cubierta, aparcamiento y subestaciones)"
  - "Bibliografia/Fuentes/Normativa/MITECO_2026_PRD_CentrosDatos_audiencia_publica.pdf (proyecto de RD, audiencia 27/08–04/09/2026)"
  - "Bibliografia/Fuentes/Normativa/BOE_RDL_7-2026_PlanIntegral_OrienteMedio.pdf (BOE-A-2026-6544)"
  - "Bibliografia/Fuentes/Normativa/BOE_RD_244-2019_autoconsumo_consolidado.pdf (texto consolidado, act. 21/03/2026)"
  - "Datos/Google Earth/Coordenadas CPD.png (40°35'53,61\" N, 3°43'1,81\" O — WGS84)"
tags: [fotovoltaica, autoconsumo, CPD, variantes, BIPV, marquesinas, planta-suelo, geotermia, BESS, parcela, regulacion, PPA, RDL-7-2026]
---

# Estimación preliminar de las tres variantes

> **Qué es este documento.** Dimensionado de primer orden (margen 5–8 %) de las tres variantes
> de diseño del TFM, a partir de los datos reales de consumo del CPD y de un modelo solar
> horario calibrado contra el informe PVsyst del trabajo previo. **No sustituye a la simulación
> PVsyst definitiva**: fija órdenes de magnitud y, sobre todo, delimita qué es físicamente
> alcanzable antes de invertir tiempo en simular.

---

## 1. El consumo real del CPD (cifra canónica corregida)

Se han procesado los **12 ficheros mensuales** a resolución de 5 minutos. Contra lo que se
suponía, **la serie está completa**: los datos van de **diciembre de 2024 a noviembre de 2025**,
y el fichero `12_2024.csv` cierra el año natural. No faltan meses; lo que falta es diciembre
de *2025*, que es irrelevante porque diciembre ya está representado por el de 2024.

| Magnitud | Valor | Origen |
| --- | --- | --- |
| **Consumo general** | **3.832 MWh/año** | Contador Gral (kWh), 12 meses |
| Consumo IT (contadores A + B) | 2.585 MWh/año | Contadores A y B (MWh) |
| **Consumo no-IT** (refrigeración + auxiliares) | **1.247 MWh/año** | Diferencia |
| **PUE medio ponderado** | **1,482** | Gral / (A+B) |
| Potencia media | 437 kW | Pot Gral |
| Potencia mínima / máxima | 300 kW / 528 kW | Pot Gral |
| **Amplitud del perfil diario medio** | **3,3 %** (433 → 448 kW) | Perfil horario |

> **Nota de unidades, importante:** «Contador Gral» está en **kWh** y «Contador A/B» están en
> **MWh**. Son contadores acumulados: el consumo del periodo es la diferencia entre la última y
> la primera lectura, no la suma de la columna.

### 1.1 El hallazgo que reencuadra todo el TFM

El trabajo previo del Módulo 6 introdujo en PVsyst una carga de **1.260 MWh/año**. El consumo
**no-IT** que se obtiene de los contadores es **1.247 MWh/año**: una diferencia del **1,0 %**.
Es decir, **el trabajo previo dimensionó contra la refrigeración, no contra el consumo total**,
tal y como su propio título anticipaba («… para sistema HVAC de un CPD»).

Consecuencia directa sobre la cifra más citada del trabajo previo:

| Referencia del denominador | C_D de los 102 kWp existentes |
| --- | --- |
| Solo HVAC (1.247 MWh) | **13,22 %** ← cifra del trabajo previo |
| **Consumo total (3.832 MWh)** | **4,29 %** ← cifra que corresponde al TFM |

Si el TFM se plantea sobre el **consumo total** del CPD (que es lo coherente con un estudio de
autoconsumo completo), el punto de partida no es el 13 % sino el **4,3 %**. Conviene fijar esto
con el tutor antes de redactar el capítulo 6, porque cambia el relato entero.

### 1.2 El perfil de carga: base pura 24/7

El perfil diario medio oscila entre **433 y 448 kW**, un **3,3 %** de amplitud. Es carga base
prácticamente perfecta, sin ciclo día/noche apreciable y sin distinción laborable/festivo
significativa. La estacionalidad también es débil: julio (344 MWh) frente a febrero (291 MWh),
apenas un 18 % de diferencia, atribuible al HVAC.

Esto tiene una consecuencia física que domina todo el diseño: **la instalación FV nunca puede
entregar más de ~437 kW útiles en ningún instante**. Todo lo que supere esa cifra es excedente.

---

## 2. Qué aportan los ficheros horarios

Los 11 ficheros `*_potDiff_horario_calendario.xlsx` contienen tres hojas:

| Hoja | Contenido | ¿Aporta información nueva? |
| --- | --- | --- |
| `Datos` | Copia íntegra del fichero mensual (5 min, 33 columnas) | **No.** Es idéntica al mensual. |
| `Promedio_por_hora` | Serie horaria de `Pot Gral − (Pot A + Pot B)` con nº de registros | **Sí, derivada:** es el perfil horario de la **potencia no-IT**. |
| `Resumen` | Media global de esa diferencia + perfil diario medio de 24 valores | **Sí, derivada:** perfil característico de la carga de refrigeración. |

En resumen: **no contienen ninguna variable medida que no esté ya en los mensuales**. Lo que
aportan es el cálculo ya hecho de la magnitud «potDiff» = potencia no-IT, agregada a hora y
promediada por hora del día. Es exactamente el input que alimentó el PVsyst del trabajo previo,
lo que confirma la interpretación del apartado 1.1.

**Dos avisos de calidad de dato:**

1. El **0,20 %** de los registros da `potDiff` **negativa** (hasta −186 kW), y hay 120 registros
   con `Pot Gral ≤ 0`. Son huecos de telemedida o resets de contador, no física. Hay que
   filtrarlos antes de usar la serie (en este análisis se han descartado los `Pot Gral ≤ 50 kW`).
2. Falta el fichero horario de **diciembre**, pero es indiferente: el mensual `12_2024.csv` lo cubre.

---

## 3. Metodología de la estimación

Modelo horario propio (8.760 h) construido y **calibrado contra el informe PVsyst del trabajo
previo**, que actúa como patrón:

| Comprobación | Modelo | PVsyst | Desviación |
| --- | --- | --- | --- |
| GlobHor anual | 1.785,8 kWh/m² | 1.785,8 | (impuesto) |
| DiffHor anual | 558,4 kWh/m² | 558,4 | (impuesto) |
| GlobInc a 10° / −30° | 1.918,5 kWh/m² | 1.937,6 | **−1,0 %** |
| E_PV de los 102 kWp | 164,45 MWh | 166,55 | **−1,3 %** |
| C_D sobre HVAC | 13,19 % | 13,22 % | **−0,2 %** |

Con desviaciones del orden del 1 %, el modelo está muy dentro del margen de 5–8 % pedido.

**Hipótesis de cálculo:** irradiancia mensual PVGIS 5.3 TMY repartida a hora según cielo claro
(Haurwitz), descomposición difusa por Erbs reescalada al total mensual de PVsyst, transposición
Hay-Davies, albedo 0,20; módulo REC Alpha Pure-RX (22,59 %, γ = −0,24 %/°C), modelo térmico
Faiman Uc = 20 W/m²K; cadena de pérdidas idéntica a la del trabajo previo (suciedad 1 %, IAM
1,9 %, mismatch 2,1 %, óhmicas 1 %, inversor 1,5 %, indisponibilidad 0,2 %, calidad +0,5 %).

**Inclinación óptima confirmada:** el modelo da máximo plano en **35–37° Sur** (2.118 kWh/m²),
coincidente con PVGIS. Cifra reutilizable para las variantes 2 y 3.

---

## 4. Geometría disponible

### 4.1 Cuál de las dos mediciones usar

Las dos parejas de superficies disponibles no son igual de fiables:

| Fuente | Tragaluz | Cubierta total | Ratio |
| --- | --- | --- | --- |
| **Catastro** | **472 m²** | **3.111 m²** | **15,2 %** |
| Google Earth | 614 m² | 3.070 m² | 20,0 % |

Midiendo en píxeles sobre `PlantaCPD.png`, el tragaluz ocupa el **14,9 %** de la huella del
edificio — coherente con catastro y no con Google Earth. La medición de Google Earth
probablemente recoge la **superficie desarrollada** del lucernario (con su pendiente) o incluye
la perfilería perimetral, mientras que catastro da la **proyección horizontal**. Se adopta
**catastro** como referencia y se anota Google Earth como cota superior.

### 4.2 Descuentos sobre la cubierta

La planta cenital muestra **dos patios interiores** (con arbolado visible) que son huecos, no
cubierta utilizable: ≈ **408 m²** medidos en píxeles. Y el resto del forjado está cuajado de
condensadoras, además de climatizadoras, cuartos técnicos y casetones de escalera.

```
Cubierta total (catastro)                      3.111 m²
  − tragaluz                                   −  472 m²
  − patios interiores                          −  408 m²
  = forjado de cubierta                         2.231 m²
  × 0,70  (retranqueos de seguridad, equipos que permanecen,
           pasillos de mantenimiento, casetones)             1.562 m²  disponibles
  × 0,82  (factor de aprovechamiento en sheds a 10°,
           el mismo que validó el trabajo previo)            1.281 m²  de módulo
  × 226,7 W/m²                                         →      290 kWp
```

---

## 5. Resultados por variante

Consumo de referencia: **3.832 MWh/año**.

| Variante | Superficie | kWp | E_PV (MWh/año) | A_PV | **% del consumo (C_D)** |
| --- | --- | --- | --- | --- | --- |
| **V1a** BIPV en tragaluz | 472 m² (378 m² de vidrio activo) | 47 | 76 | 100 % | **2,0 %** |
| **V1b** Cubierta convencional (liberada por geotermia) | 1.562 m² útiles | 290 | 468 | 100 % | **12,2 %** |
| **V1 = V1a + V1b** | ≈ 2.034 m² | **338** | **544** | 100 % | **14,2 %** |
| **V2** Marquesinas de parking | **3.332 m²** de huella (F1–F8) | **680** | **1.114** | 99,5 % | **28,9 %** |
| **V1 + V2** (todo el emplazamiento) | ≈ 5.366 m² | **1.017** | **1.658** | 85,0 % | **36,8 %** |
| **V3** Planta en suelo | *por cada 1 ha* | 758 | 1.362 | 95 % | **33,8 %** |

### 5.1 Variante 1 — BIPV en tragaluz + cubierta liberada

El BIPV del tragaluz es, en términos energéticos, **casi irrelevante**: aporta un 2 % del
consumo. Su potencia depende mucho del grado de transparencia que se exija al vidrio:

| Transparencia del vidrio FV | Densidad | kWp | E_PV | C_D |
| --- | --- | --- | --- | --- |
| Alta (VLT > 30 %) | 90 Wp/m² | 34 | 54 MWh | 1,4 % |
| **Media (VLT ≈ 20 %)** | **125 Wp/m²** | **47** | **76 MWh** | **2,0 %** |
| Baja (VLT ≈ 10 %) | 160 Wp/m² | 60 | 97 MWh | 2,5 % |

> La justificación del BIPV en el TFM **no puede ser energética**: tiene que ser arquitectónica
> (integración, control solar del lucernario, reducción de la carga térmica que entra por él) y
> demostrativa. Como número de cobertura, 2 % es marginal. Vale la pena plantearlo así
> explícitamente y no forzar el argumento.

Lo que sí es sustancial es **liberar la cubierta**: pasar de los 450 m² del trabajo previo a
~1.562 m² triplica la potencia (102 → 290 kWp) y sube del 4,3 % al 12,2 % del consumo total.

### 5.2 El efecto oculto de la geotermia: reduce el propio consumo

Sustituir el *air-cooling* por refrigeración geotérmica no solo libera cubierta — **baja el
consumo del CPD**, porque el foco frío pasa de aire a 35–40 °C en verano a terreno estable a
15–17 °C. Estimando que la refrigeración es el 70 % del no-IT (873 MWh/año):

| Salto de rendimiento estacional | Ahorro | Nuevo consumo | Nuevo PUE |
| --- | --- | --- | --- |
| SEER 3,2 → 5,0 | 314 MWh/año (8,2 %) | 3.518 MWh | 1,361 |
| **SEER 3,2 → 5,5** | **365 MWh/año (9,5 %)** | **3.467 MWh** | **1,341** |
| SEER 3,0 → 6,0 | 436 MWh/año (11,4 %) | 3.396 MWh | 1,314 |

**Un ahorro de ~365 MWh/año equivale a lo que producirían ~205 kWp de FV** — es decir, la
geotermia rinde, como medida, más que toda la cubierta del trabajo previo, y sin ocupar
superficie. Es probablemente la palanca de mayor retorno de todo el estudio y merece capítulo
propio, no una nota al pie.

> ⚠️ Los valores de SEER son **estimaciones de orden de magnitud pendientes de verificar** con
> fuente citable (`investigador-cientifico`) y de contrastar con el rendimiento real de las
> máquinas instaladas. No deben entrar al documento tal cual.

### 5.3 Variante 2 — Marquesinas de parking

Superficie **medida sobre `TFM.kmz`**, donde Mario dibujó una a una las ocho filas de
marquesinas (polígonos `F1`–`F8`). Conviene no confundir las dos cifras que da el fichero: el
polígono `Parking - General` mide 6.252 m², pero **incluye las calles de circulación**; la huella
que realmente se puede cubrir es la suma de las filas.

```
Filas de marquesinas F1..F8 (huella medida)     3.332 m²
  × 0,90  (ocupación de módulo sobre la marquesina)          2.999 m²  de módulo
  × 226,7 W/m²                                         →       680 kWp
```

| Magnitud | Valor |
| --- | --- |
| Potencia | **680 kWp** |
| Producción | **1.114 MWh/año** (Y_F 1.639 kWh/kWp) |
| Autoconsumo A_PV | **99,5 %** — el pico (500 kW) roza ya los 437 kW de carga media |
| **Cobertura C_D** | **28,9 %** (31,3 % si la geotermia ya ha bajado el consumo) |

> **Es, con diferencia, la mejor variante de las tres.** Sobre un recinto ya pavimentado y sin uso
> en altura, **duplica lo que aporta toda la cubierta del edificio** (28,9 % frente al 14,2 % de
> V1), sin tocar el sistema de refrigeración, sin obra sobre un edificio en explotación y
> sombreando las plazas de paso. Los excedentes son testimoniales (5 MWh/año, un 0,5 % de la
> producción), así que sigue encajando en una configuración antivertido.

Regla parametrizada, por si se revisa la huella: **≈ 204 kWp, ≈ 334 MWh/año y ≈ 8,7 % del consumo
por cada 1.000 m² de marquesina**. Los excedentes empiezan a ser apreciables a partir de
~3.300 m², que es justo donde está el proyecto: **la variante 2 llega sola al límite de lo que el
CPD puede absorber en las horas centrales del día**, y todo lo que se añada por encima ya exige
batería para no verterse.

> **Corrección respecto a la versión anterior de este documento.** Se había partido de una
> superficie de aparcamiento de 2.461 m² y de un factor de cubrición del 0,70, lo que daba
> 1.723 m² de marquesina y 351 kWp. La medición real de las ocho filas sobre el KMZ da 3.332 m²
> de huella, de modo que **V2 pasa de 351 a 680 kWp y de 15,0 % a 28,9 % de cobertura**. Todas
> las cifras combinadas de los apartados 5.6 y 6 están recalculadas con el valor nuevo.

### 5.4 Variante 3 — Planta en suelo

Parámetros: 30° Sur, GCR 0,40, más un 20 % de viales, márgenes y centro de transformación.

- **Productividad:** **1.798 kWh/kWp/año**
- **Ocupación:** **13,2 m²/kWp = 1,32 ha/MWp**

**Aquí hay que separar dos preguntas que suenan iguales y no lo son.**

**(a) Cubrir el consumo en balance anual de energía** (se vierte el excedente de día y se importa
de noche; la red actúa de batería virtual):

| Objetivo | Potencia | **Superficie** | Excedentes | C_D *real* |
| --- | --- | --- | --- | --- |
| 50 % | 1,07 MWp | **1,41 ha** | 23 % | 38,5 % |
| **80 %** | **1,70 MWp** | **2,25 ha** (22.500 m²) | 47 % | 42,2 % |
| **100 %** | **2,13 MWp** | **2,81 ha** (28.100 m²) | 57 % | 43,4 % |

**(b) Cubrir el consumo de verdad, hora a hora** (autosuficiencia real, sin batería):

| Potencia | Superficie | C_D real | A_PV | Excedentes |
| --- | --- | --- | --- | --- |
| 0,5 MWp | 0,66 ha | 23,5 % | 100 % | 0 |
| 1,0 MWp | 1,32 ha | 37,8 % | 80,5 % | 350 MWh |
| 2,0 MWp | 2,64 ha | 43,1 % | 45,9 % | 1.946 MWh |
| 5,0 MWp | 6,60 ha | 46,3 % | 19,7 % | 7.218 MWh |
| 20 MWp | 26,4 ha | 48,6 % | 5,2 % | 34.103 MWh |

> ### El resultado más importante del análisis
>
> **Sin almacenamiento, la autosuficiencia satura en el 50,5 %, por mucha potencia que se
> instale.** No es una limitación de diseño: es la fracción del consumo del CPD que ocurre en
> horas de sol. Como la carga es plana 24/7, la otra mitad no hay FV que la cubra.
>
> **Por tanto, el 80 % o el 100 % de cobertura *real* son inalcanzables sin batería, a cualquier
> superficie.** Cuando el enunciado pide «la superficie para cubrir el 100 %», la respuesta
> honesta son 2,81 ha *en balance anual neto* — con la advertencia de que más de la mitad de esa
> energía (2.169 MWh) se vierte a la red y se vuelve a comprar por la noche.

### 5.5 Lo que sí llega al 80 % real: FV + batería

| Fotovoltaica | Superficie | Batería | **C_D real** |
| --- | --- | --- | --- |
| 2,13 MWp | 2,81 ha | — | 43,4 % |
| 2,13 MWp | 2,81 ha | 2 MWh | 60,9 % |
| 2,50 MWp | 3,30 ha | 3 MWh | 70,3 % |
| **3,00 MWp** | **3,96 ha** | **4 MWh** | **79,8 %** |
| 3,50 MWp | 4,62 ha | 5 MWh | 89,0 % |
| 4,00 MWp | 5,28 ha | 6 MWh | 96,9 % |

(rendimiento de ciclo 92 %, sin límite de potencia de carga/descarga — es una cota optimista
que habrá que refinar en el modelo horario de Excel del capítulo 7)

**Esto resuelve la duda abierta sobre cómo justificar el almacenamiento en el TFM.** En el
trabajo previo el A_PV ya era 100 % y no sobraba un solo kWh, de modo que el argumento clásico
de «aprovechar excedentes» no servía. Con las variantes ampliadas **sí aparecen excedentes
masivos** (57 % de la producción en la variante de 2,13 MWp), y la batería pasa a ser el único
medio de superar la barrera del 50,5 %. El argumento ya no hay que forzarlo: sale solo de los
números.

### 5.6 La parcela candidata identificada (58,8 ha)

Mario localizó una parcela apta y la delimitó a mano en `Datos/Google Earth/TFM.kmz`
(polígono `Layout1`, descripción «58,7 ha»). El fichero **sí es legible**: un `.kmz` es un ZIP
con un `doc.kml` dentro, de modo que sus polígonos se pueden medir directamente en lugar de
estimarlos sobre la vista aérea.

| Magnitud | Valor medido sobre el KMZ |
| --- | --- |
| **Superficie bruta** | **588.401 m² = 58,84 ha** (la anotación de Mario, 58,7 ha, cuadra al 0,2 %) |
| Envolvente | ≈ 961 m (E–O) × 1.135 m (N–S) |
| Centroide respecto al CPD | **3,72 km al noroeste** (rumbo 316°) |
| **Borde más cercano al CPD** | **2,93 km** |

**Capacidad instalable.** Con la misma ocupación del apartado 5.4 (13,2 m²/kWp: fijo a 30° Sur,
GCR 0,40, más un 20 % de viales, márgenes y centro de transformación):

```
Superficie bruta                                     588.401 m²
  × 0,85  (servidumbres, drenaje, retranqueos, franja cortafuegos)   500.141 m²  netos
  ÷ 13,2 m²/kWp                                            →          37,9 MWp
```

- **Capacidad bruta teórica: 44,6 MWp.** **Capacidad neta realista: ≈ 37,9 MWp.**
- Producción asociada: **68,1 GWh/año**, con una punta de **28,2 MW**.

> ### La parcela no es el cuello de botella: sobra suelo por un factor de veinte
>
> Esos 68,1 GWh/año son **17,8 veces el consumo anual del CPD** (3.832 MWh), y los 28,2 MW de
> punta son **59 veces** su punta de demanda (0,48 MW). Si se ocupara entera, **el 97,2 % de la
> producción se vertería a la red**: dejaría de ser un proyecto de autoconsumo para ser una
> planta comercial con PPA, que es otro TFM.
>
> La consecuencia de diseño es que **la superficie deja de ser la variable limitante** y el
> dimensionado pasa a gobernarlo el binomio potencia–batería. La pregunta útil ya no es «cuánto
> cabe», sino «cuánto conviene».

**Qué fracción de la parcela hace falta realmente.** Barrido de potencia y capacidad de batería
sobre la serie horaria de carga (rendimiento de ciclo 92 %), con la planta en suelo como única
fuente:

| Objetivo de **autosuficiencia real** | Fotovoltaica | Superficie | **% de la parcela** | Batería |
| --- | --- | --- | --- | --- |
| 80 % | 2,25 MWp | 2,97 ha | **5,9 %** | 4,5 MWh |
| 90 % | 2,50 MWp | 3,30 ha | **6,6 %** | 5,5 MWh |
| 95 % | 2,75 MWp | 3,63 ha | **7,3 %** | 6,0 MWh |
| 98 % | 3,00 MWp | 3,96 ha | **7,9 %** | 6,5 MWh |
| **99 %** | **3,25 MWp** | **4,29 ha** | **8,6 %** | **7,0 MWh** |
| 100 % | — | — | — | **inalcanzable** |

El 100 % estricto no se alcanza ni con 25 MWp y 60 MWh: la curva se satura en torno al 99,9 %
porque siempre queda algún episodio invernal de varios días nublados encadenados que agotaría
cualquier batería de ciclo diario. Cubrir ese último 0,1 % exigiría almacenamiento estacional,
que no tiene sentido técnico ni económico frente a mantener la acometida de red como respaldo.

**Combinando con la fotovoltaica del propio emplazamiento** (V1 + V2 = **1.017 kWp**,
**1.658 MWh/año**, que ya cubren por sí solos el **36,8 %** del consumo):

| Escenario | Objetivo | Planta en suelo | Superficie | % parcela | Batería | FV total |
| --- | --- | --- | --- | --- | --- | --- |
| Sin geotermia | 80 % | 1,25 MWp | 1,65 ha | 3,3 % | 4,4 MWh | 2,27 MWp |
| Sin geotermia | 90 % | 1,50 MWp | 1,98 ha | 4,0 % | 5,6 MWh | 2,52 MWp |
| Sin geotermia | 95 % | 2,00 MWp | 2,64 ha | 5,3 % | 5,9 MWh | 3,02 MWp |
| Sin geotermia | 99 % | 2,50 MWp | 3,30 ha | 6,6 % | 6,6 MWh | 3,52 MWp |
| **Con geotermia** | **80 %** | **1,00 MWp** | **1,32 ha** | **2,6 %** | **4,1 MWh** | **2,02 MWp** |
| Con geotermia | 90 % | 1,25 MWp | 1,65 ha | 3,3 % | 5,1 MWh | 2,27 MWp |
| **Con geotermia** | **95 %** | **1,75 MWp** | **2,31 ha** | **4,6 %** | **5,3 MWh** | **2,77 MWp** |
| Con geotermia | 99 % | 2,25 MWp | 2,97 ha | 5,9 % | 6,0 MWh | 3,27 MWp |

Con la variante 2 corregida, **el 80 % de autosuficiencia real se alcanza con 1,32 ha de planta
en suelo — el 2,6 % de la parcela — y 4,1 MWh de batería.**

**Sobre el dimensionado de la batería.** La potencia de descarga que exige el despacho no pasa
de **0,43–0,47 MW** — es, exactamente, la punta de demanda del CPD, porque la carga es plana.
Frente a los 4–7 MWh de capacidad eso da una tasa de **0,07–0,11 C**, es decir, **entre 9 y 14
horas de autonomía nominal**. No es un BESS convencional de 2–4 h de los que dominan el mercado
de arbitraje: es un sistema orientado a energía, no a potencia, y esa relación C/P condicionará
tanto la elección de tecnología como el coste unitario en el capítulo económico.

#### 5.6.1 La distancia de 2,93 km: el problema está resuelto por normativa de marzo de 2026

El borde más cercano de la parcela está a **2,93 km del CPD** y su centroide a 3,72 km. En una
versión anterior de este documento se señaló como riesgo crítico. Lo era: el criterio general de
proximidad del RD 244/2019 son **500 m** entre equipos de medida, y 2,93 km lo incumplía por un
factor de casi seis. **Lo que ha cambiado no es la distancia de la parcela, sino la norma.**

El **Real Decreto-ley 7/2026, de 20 de marzo** (BOE-A-2026-6544, convalidado por el Congreso el
26 de marzo de 2026, BOE-A-2026-7125), en su **disposición final decimocuarta, apartado Uno**,
dio nueva redacción a la letra iii) del apartado g) del artículo 3 del RD 244/2019. La redacción
resultante **mantiene los 500 m como regla general y añade un segundo párrafo** con un supuesto
específico para fotovoltaica y eólica:

> «También tendrá la consideración de instalación de producción próxima a las de consumo y
> asociada a través de la red, aquella instalación de generación que empleando tecnología
> fotovoltaica o eólica **con una potencia de hasta 5 MW**, esta se conecte al consumidor o
> consumidores a través de las líneas de transporte o distribución y siempre que estas se
> encuentren **a una distancia inferior a 5.000 metros** de los consumidores asociados. A tal
> efecto se tomará la distancia entre los equipos de medida en su proyección ortogonal en
> planta.»
>
> — RD 244/2019, art. 3.g).iii), redacción dada por la DF 14.ª del RDL 7/2026

**La variante 3 cumple las dos condiciones con holgura:**

| Condición del art. 3.g).iii) | Exigencia | Caso del CPD | ¿Cumple? |
| --- | --- | --- | --- |
| Tecnología | Fotovoltaica o eólica | Fotovoltaica | Sí |
| Potencia | ≤ 5 MW | 1,0–2,5 MWp según objetivo | Sí, con margen |
| Distancia entre equipos de medida | < 5.000 m | 2.930 m (borde) – 3.720 m (centroide) | Sí, con margen |

Es decir: **la planta en suelo puede acogerse a autoconsumo a través de la red sin necesidad de
línea directa ni de renunciar a la figura de autoconsumo.** El criterio de la distancia, que era
el obstáculo, se resolvió cinco meses antes de redactarse este análisis. Conviene medir la
distancia definitiva entre los equipos de medida reales —no entre centroides— cuando se fije la
posición del centro de seccionamiento de la planta, pero incluso el peor caso (3,72 km) deja
1,3 km de margen.

Dos observaciones que conviene no perder:

- **La línea directa no era inviable, pero ya no hace falta.** La objeción de que 3 km de línea
  directa son técnicamente imposibles es correcta *en baja tensión*: 2,5 MW a 400 V son 3.608 A,
  y ni con diez conductores de 240 mm² por fase la caída baja del 58 %. Pero una línea directa no
  obliga a trabajar en BT: los mismos 2,5 MW a **20 kV son 72 A**, con una caída del **0,4 %** y
  unas pérdidas de **9,7 kW (0,39 %)** sobre 3 km de 150 mm² de aluminio subterráneo. Es una
  línea de distribución completamente ordinaria. Cálculo reproducible en
  `scripts/linea_directa.py`. La línea directa queda, por tanto, como alternativa técnica válida
  y no como imposibilidad —simplemente, el autoconsumo a través de la red es más barato.
- **La vía del PPA sigue abierta como comparación económica**, no como necesidad regulatoria.
  Deja de ser el plan B forzoso para convertirse en un término de comparación en el capítulo
  económico: autoconsumo a distancia frente a PPA con una planta de terceros.

Los puntos de conexión que el propio KMZ trae mapeados sirven ahora para dimensionar la
infraestructura de evacuación, no para resolver el encaje regulatorio:

| Subestación | Distancia al CPD | Distancia a la parcela |
| --- | --- | --- |
| **La Cereal 220 / 400** | **0,56 km** | 2,41 km |
| **Tres Cantos GIS 220** | **0,59 km** | 2,35 km |
| Tres Cantos 220 | 2,33 km | 3,10 km |
| BBVA 4145 66 | 2,48 km | 3,98 km |
| Lavander 4196 | 8,67 km | 4,28 km |
| Colmenar Viejo 4013 | 8,54 km | 4,68 km |
| San Agustín de Guadalix 4091 | 11,64 km | 11,99 km |

Sigue en pie que, con 1–2,5 MWp, la potencia de acceso de la planta supera 1 MW y el
procedimiento de acceso y conexión no es el simplificado (RD 1183/2020).

---

## 5bis. Las tres variantes como alternativas excluyentes

> **Encuadre.** Mario planteó V1, V2 y V3 como **variantes**, es decir, como alternativas que se
> comparan y entre las que se elige una. Este apartado responde a esa pregunta en sus propios
> términos: qué da cada una **por separado**, con y sin batería, y bajo qué figura jurídica de
> autoconsumo quedaría. El apartado 6 mantiene el escenario combinado como **caso adicional**,
> no como sustituto de la comparación. Cálculo en `scripts/variantes_excluyentes.py`, salida
> íntegra en `salidas_variantes_excluyentes.txt`.

### 5bis.1 Qué da cada variante por sí sola

| Variante | kWp | E_PV | A_PV | **C_D sin batería** | Excedentes | Horas con vertido |
| --- | --- | --- | --- | --- | --- | --- |
| **V1** Cubierta (BIPV + liberada) | 338 | 544 MWh | 100 % | **14,2 %** | **0 MWh** | **0 h** |
| **V2** Marquesinas (3.332 m²) | 680 | 1.114 MWh | 99,5 % | **28,9 %** | 5 MWh | 355 h |
| **V3** Planta suelo 1,00 MWp | 1.000 | 1.798 MWh | 80,5 % | 37,8 % | 350 MWh | 2.273 h |
| **V3** Planta suelo 2,00 MWp | 2.000 | 3.597 MWh | 45,9 % | 43,1 % | 1.946 MWh | 3.282 h |
| **V3** Planta suelo 2,25 MWp | 2.250 | 4.046 MWh | 41,3 % | 43,6 % | 2.374 MWh | 3.399 h |
| **V3** Planta suelo 2,50 MWp | 2.500 | 4.496 MWh | 37,6 % | 44,1 % | 2.807 MWh | 3.485 h |

**El dato que hay que leer dos veces:** de 1,00 a 2,50 MWp, el C_D sin batería sube de 37,8 % a
44,1 %. **Se multiplica por 2,5 la potencia y se ganan 6 puntos.** Todo lo demás se vierte. Es la
barrera del 50,5 % del apartado 5.5 vista de cerca: contra una carga plana, sobredimensionar el
campo fotovoltaico sin almacenamiento no sirve prácticamente de nada.

### 5bis.2 La batería: imprescindible en V3, inútil en V1 y V2

Techo de autosuficiencia alcanzable con batería de capacidad infinita:

| Variante | C_D sin batería | **Techo con batería** | Ganancia | ¿Batería justificada? |
| --- | --- | --- | --- | --- |
| **V1** | 14,2 % | **14,2 %** | **0,0 pp** | **No.** Nunca hay excedente que almacenar |
| **V2** | 28,9 % | **29,1 %** | **0,2 pp** | **No.** 5 MWh/año de excedente, irrelevante |
| **V3** 1,00 MWp | 37,8 % | 45,5 % | 7,7 pp | Marginal |
| **V3** 2,00 MWp | 43,1 % | 86,0 % | **42,9 pp** | **Sí, decisiva** |
| **V3** 2,25 MWp | 43,6 % | 96,0 % | **52,4 pp** | **Sí, decisiva** |
| **V3** 2,50 MWp | 44,1 % | 99,2 % | **55,1 pp** | **Sí, decisiva** |

La razón es geométrica y no económica: V1 y V2 nunca superan de forma apreciable los ~437 kW de
carga plana, así que **no producen excedente que guardar**. La batería no es una mejora general
del autoconsumo: **es el complemento específico de una planta sobredimensionada**.

### 5bis.3 Cuánta batería, y la comprobación de la hipótesis de 2,25–2,50 MWp

Capacidad mínima de BESS para cada objetivo de autosuficiencia **real**:

| Variante | 50 % | 60 % | 70 % | **80 %** | **90 %** |
| --- | --- | --- | --- | --- | --- |
| V1 / V2 | — | — | — | — | — |
| V3 1,50 MWp | 0,99 MWh | 2,22 MWh | — | — | — |
| V3 2,00 MWp | 0,79 MWh | 1,93 MWh | 3,10 MWh | **4,51 MWh** | — |
| V3 2,25 MWp | 0,73 MWh | 1,87 MWh | 3,01 MWh | **4,20 MWh** | **5,73 MWh** |
| V3 2,50 MWp | 0,68 MWh | 1,82 MWh | 2,96 MWh | **4,11 MWh** | **5,36 MWh** |

Y los pares FV + BESS más económicos para cada objetivo (coste orientativo 0,55 k€/kWp y
0,30 k€/kWh, solo para ordenar):

| Objetivo C_D real | **MWp** | **BESS** | Superficie | % de la parcela | Excedentes |
| --- | --- | --- | --- | --- | --- |
| **80 %** | **2,00** | **4,5 MWh** | 2,64 ha | 5,3 % | 274 MWh |
| **85 %** | 2,25 | 4,9 MWh | 2,97 ha | 5,9 % | 499 MWh |
| **90 %** | **2,25** | **5,7 MWh** | 2,97 ha | 5,9 % | 273 MWh |
| 95 % | 2,50 | 6,3 MWh | 3,30 ha | 6,6 % | 499 MWh |

> **La hipótesis de 2,25–2,50 MWp para el 80–90 % es correcta**, con una precisión que conviene
> fijar: esa potencia da el 80–90 % **solo acompañada de 4–6 MWh de batería**. Sola, se queda en
> el 43–44 %. La potencia fija el techo; **la batería es la que decide dónde se aterriza dentro
> de ese techo.**
>
> La potencia de descarga que pide el modelo es de **471 kW** — la punta de la carga plana. Con
> 4–6 MWh eso son **0,08–0,12 C y 9–13 h de autonomía**: una batería de **energía**, no la de
> potencia de 2–4 h que domina el mercado. Es un condicionante real de suministro y de coste.

### 5bis.4 Tipología de autoconsumo de cada variante

Encadenando el RD 244/2019 con la reforma del RDL 7/2026:

| Variante | Distancia | Figura del art. 3.g) | Modalidad del art. 4 | ¿Permisos de acceso? |
| --- | --- | --- | --- | --- |
| **V1** | 0 m, mismo edificio | **Próxima de red interior** (art. 3.g.i) | **Sin excedentes** (nunca vierte) | **No** — exenta por art. 7.1.b).i) |
| **V2** | **216 m** | **Red interior o línea directa** (art. 3.g.i) — ver 5bis.5 | **Sin excedentes**, con antivertido | **No** — exenta por art. 7.1.b).i) |
| **V3** | 2,93 km | **Próxima a través de la red** (art. 3.g, párr. 2.º) | **Con excedentes obligatoriamente** (art. 4.5.c) | **Sí** — art. 7.1.b).iii) |

### 5bis.5 V2: los 216 m y las dos referencias catastrales

Datos aportados por Mario el 29/08/2026 y verificados sobre el `TFM.kmz`:

| Dato | Valor |
| --- | --- |
| Referencia catastral del **aparcamiento** | `9347902VK3994N` |
| Referencia catastral del **edificio del CPD** | `9347904VK3994N` |
| Distancia CPD → aparcamiento (medida sobre el KMZ) | **215,8 m** (Mario: 216 m) |
| Borde de cubierta → borde de aparcamiento | 138 m |

**Las dos referencias no coinciden en sus 14 primeros dígitos** (difieren en el séptimo carácter:
`9347902…` frente a `9347904…`). Son dos parcelas catastrales distintas, así que **la vía del
art. 3.g).iv) —misma referencia catastral— no está disponible.** Conviene decirlo explícitamente
en la memoria porque es la puerta que uno esperaría usar y no sirve.

Quedan dos vías, y **la elección no es administrativa sino de trazado eléctrico**:

| Vía | Cómo se materializa | Figura resultante | Consecuencia |
| --- | --- | --- | --- |
| **Art. 3.g).i)** — red interior **o línea directa** | Cable propio de 216 m del aparcamiento al cuadro del CPD, sin pisar red de distribuidora | **Próxima de red interior** | **Sin excedentes**, exenta de permisos (art. 7.1.b.i), energía autoconsumida **exenta de peajes y cargos** |
| **Art. 3.g).iii)** — menos de 500 m | Conexión a la red de distribución en el aparcamiento | **Próxima a través de la red** | **Con excedentes obligatoria** (art. 4.5.c), **exige permisos** (art. 7.1.b.iii) y **paga peaje** por la energía autoconsumida (ver 7.6) |

Los 216 m cumplen holgadamente los 500 m del art. 3.g).iii), de modo que **V2 encaja por las dos
vías**. Pero son muy distintas en consecuencias: la primera es la de un autoconsumo convencional
y la segunda arrastra todo el aparato de la variante 3. **Recomendación: tender los 216 m de línea
propia.** Nótese además que el art. 3.g).i) admite expresamente la **línea directa** como forma de
cumplir la condición i, de modo que atravesar dos referencias catastrales distintas no rompe el
encaje mientras la línea sea propia y no de la distribuidora.

### 5bis.6 Por qué la V3 no puede ser «sin excedentes»: los vertidos, en cifras

La razón de fondo no es jurídica sino física, y hay que separarla en dos.

**Primero, lo estructural.** En la V3 la energía **llega al CPD precisamente inyectándola en la
red**: la planta vierte en su nudo y el CPD retira del suyo, y la distribuidora casa las dos series
hora a hora (apartado 7.5.1). Un mecanismo antivertido en la planta —que por definición «impide en
todo momento el vertido de energía eléctrica a la red» (art. 3.k del RD 244/2019)— **bloquearía el
propio mecanismo de entrega**. La planta no dejaría de verter: dejaría de producir. No es que la
modalidad esté prohibida; es que no existe.

**Segundo, y esto responde a si un buen diseño podría evitar los excedentes: no puede.**

| Configuración V3 | Vertido | % de E_PV | Horas con vertido | Pico vertido |
| --- | --- | --- | --- | --- |
| 2,00 MWp, sin batería | 1.946 MWh | 54,1 % | 3.282 h | 1.052 kW |
| **2,00 MWp + 4,51 MWh** | **273 MWh** | **7,6 %** | 696 h | 832 kW |
| 2,25 MWp, sin batería | 2.374 MWh | 58,7 % | 3.398 h | 1.238 kW |
| **2,25 MWp + 5,73 MWh** | **274 MWh** | **6,8 %** | 631 h | 831 kW |
| 2,25 MWp + 10 MWh | 185 MWh | 4,6 % | 471 h | 728 kW |
| 2,25 MWp + **20 MWh** | **163 MWh** | **4,0 %** | 414 h | 728 kW |

**Cuadruplicar la batería de 5,7 a 20 MWh solo baja el vertido de 274 a 163 MWh.** El excedente no
es un problema de tamaño de batería: es **estacional**. Su reparto mensual con 2,25 MWp + 5,73 MWh
lo enseña sin lugar a dudas:

| Mes | E F M A M J J A S O N D |
| --- | --- |
| MWh vertidos | 0 · 5 · 37 · 0 · 33 · **51** · **58** · **45** · 43 · 1 · 0 · 0 |

De junio a septiembre se concentra el 72 % del vertido. La causa es aritmética: el CPD consume
**10,5 MWh/día** constantes, y en julio una planta de 2,25 MWp produce del orden de **14 MWh/día**.
Sobran ~3,5 MWh **todos los días de julio**, y la batería llega llena al final de cada jornada.
Para absorberlos habría que trasladar energía de julio a diciembre, no de mediodía a medianoche:
eso es **almacenamiento estacional**, fuera del alcance de este TFM y del estado del arte comercial.

> **La conclusión que interesa para la memoria:** un antivertido en la V3 no «evitaría» esos
> 274 MWh — los **recortaría**. Serían 274 MWh/año generables y tirados, un 6,8 % de la producción.
> El vertido no es un defecto de diseño que se pueda corregir dimensionando mejor: es la
> consecuencia inevitable de cubrir con una fuente estacional una demanda que no lo es.

**V2 y el antivertido.** V2 vierte 5 MWh/año en 355 horas. Un mecanismo antivertido recortaría esa
producción y la variante seguiría siendo *sin excedentes* perdiendo un 0,4 % de la generación.
Alternativamente, **50 kWh de batería bastan para llevar el vertido a cero** sin recortar nada. Es
la única función que tiene una batería en V2, y a esa escala es un detalle de diseño, no una
inversión.

**Y la pregunta de si la batería cambia la tipología: no, no la cambia por sí sola.** Lo que
define la modalidad es el mecanismo antivertido (art. 4.1.a), no el almacenamiento. La batería
puede *facilitar* que una instalación se mantenga sin excedentes al absorber los picos, y en V2
haría justo eso. Pero **en V3 no hay elección posible**: el art. 4.5.c) obliga a *con excedentes*
por mucha batería que se ponga, porque la energía viaja por la red de un nudo a otro. La batería
reduce cuánto se vierte; no cambia la figura jurídica.

---

## 6. Escenario combinado (caso adicional, no sustituye a la comparación)

| Escenario | kWp | E_PV | A_PV | C_D vs 3.832 | C_D vs 3.467 (con geotermia) |
| --- | --- | --- | --- | --- | --- |
| V1a BIPV tragaluz | 47 | 76 MWh | 100 % | 2,0 % | 2,2 % |
| V1b Cubierta liberada | 290 | 468 MWh | 100 % | 12,2 % | 13,5 % |
| V1 (tragaluz + cubierta) | 338 | 544 MWh | 100 % | 14,2 % | 15,7 % |
| **V2 (marquesinas, 3.332 m²)** | **680** | **1.114 MWh** | **99,5 %** | **28,9 %** | **31,3 %** |
| **V1 + V2 (todo el emplazamiento)** | **1.017** | **1.658 MWh** | **85,0 %** | **36,8 %** | **38,1 %** |

**Todo lo que cabe en la propiedad, sin salir de ella, es el 36,8 % del consumo** — un 38,1 % si
antes se ha hecho la geotermia. Con la superficie de marquesinas ya medida, el emplazamiento
propio aporta más del doble de lo que aportaba la estimación anterior.

Aparece aquí un umbral de diseño que antes no existía: **el A_PV cae al 85,0 %**, con 249 MWh/año
de excedente. Con 1.017 kWp la producción de mediodía ya rebasa los ~437 kW que la carga plana
puede absorber, de modo que **una configuración estrictamente antivertido empezaría a recortar
producción**. O se vierte a la red, o se almacena. Es el primer punto del estudio en que la
batería deja de ser una opción de mejora y pasa a ser necesaria para no desperdiciar energía ya
generada — y ocurre **antes incluso de plantear la planta en suelo**.

### 6.1 Cuánta planta en suelo hace falta para cerrar el balance

| Escenario de partida | Falta por cubrir | **V3 necesaria** |
| --- | --- | --- |
| V1 + V2, sin geotermia | 2.174 MWh/año | 1,21 MWp = **1,60 ha** (16.000 m²) |
| **V1 + V2, con geotermia** | **1.809 MWh/año** | **1,01 MWp = 1,33 ha** (13.300 m²) |

Frente a las **2,81 ha** que haría falta si la planta en suelo fuese la única medida, el conjunto
**baja el requisito de suelo a 1,33 ha: un 53 % menos**, y a solo el **2,7 % de la parcela
localizada**. Este es el argumento para defender la combinación de variantes en vez de
compararlas como alternativas excluyentes.

### 6.2 El conjunto completo V1 + V2 + V3 con geotermia

**2.024 kWp** (338 en cubierta + 680 en marquesinas + 1.006 en suelo) → **3.467 MWh/año**, que
iguala exactamente el consumo en balance anual. Pero la autosuficiencia real sigue siendo del
**43,8 %**, con **1.949 MWh** vertidos a la red y recomprados de noche. Añadiendo batería:

| Batería | C_D real | Excedentes | Energía de red |
| --- | --- | --- | --- |
| — | 43,8 % | 1.949 MWh | 1.949 MWh |
| 1 MWh | 53,5 % | 1.552 MWh | 1.613 MWh |
| 2 MWh | 63,1 % | 1.156 MWh | 1.278 MWh |
| 3 MWh | 72,2 % | 783 MWh | 963 MWh |
| **4 MWh** | **79,7 %** | **477 MWh** | **703 MWh** |
| 6 MWh | 87,2 % | 172 MWh | 445 MWh |

---

## 7. El marco regulatorio cambió mientras se hacía este análisis

Dos normas de 2026 afectan de lleno al TFM, y las dos cuelgan del mismo tronco. Conviene tratarlas
juntas porque una **habilita** la variante 3 y la otra **la exige**.

### 7.1 El RDL 7/2026 desbloquea la variante 3

Ya desarrollado en el apartado 5.6.1: la disposición final decimocuarta del **Real Decreto-ley
7/2026, de 20 de marzo** (BOE-A-2026-6544, convalidado el 26 de marzo, BOE-A-2026-7125) dio nueva
redacción al art. 3.g).iii) del RD 244/2019: junto a la regla general de **500 m**, que se mantiene,
añadió un supuesto de **5.000 m** para instalaciones fotovoltaicas o eólicas de hasta **5 MW**. Con 2,93 km y 1–2,5 MWp, la planta en
suelo entra en el supuesto con margen.

#### 7.1.1 El apartado que legaliza el escenario combinado

La misma disposición final decimocuarta, en su **apartado Dos**, dio nueva redacción al
**artículo 4.5 del RD 244/2019**, y ahí hay dos frases que condicionan el diseño de este TFM
tanto como la distancia:

> «b) En ningún caso un sujeto consumidor podrá estar asociado de forma simultánea a más de una
> de las modalidades de autoconsumo reguladas en el presente artículo **con la única excepción de
> un autoconsumo individual sin excedentes combinado con un autoconsumo mediante instalaciones
> próximas y asociadas a través de la red**.
>
> c) En aquellos casos en que se realice autoconsumo mediante instalaciones próximas y asociadas
> a través de la red, el autoconsumo **deberá pertenecer a la modalidad de suministro con
> autoconsumo con excedentes**.»

**Lectura para el TFM, en dos consecuencias:**

1. **La combinación V1 + V2 + V3 es exactamente la única excepción que la norma admite**, y no lo
   era antes. La cubierta y las marquesinas pueden explotarse como **autoconsumo individual sin
   excedentes** (con mecanismo antivertido, art. 4.1.a), mientras la planta en suelo funciona en
   paralelo como **instalación próxima a través de la red**. El escenario combinado del apartado 6
   deja de ser una hipótesis de trabajo y pasa a tener encaje jurídico expreso.
2. **La variante 3 no puede ser «sin excedentes»**: la letra c) la obliga a ser *con excedentes*.
   Esto no es un matiz formal, porque encadena con el artículo 7.1.b).iii) del propio RD 244/2019:
   toda instalación de producción con excedentes por encima de 15 kW **debe disponer de sus
   propios permisos de acceso y conexión**. Es decir, la planta en suelo necesita capacidad de
   acceso de generación en el nudo — la normativa de distancia la habilita, pero no la exime del
   procedimiento del RD 1183/2020. Ver el apartado 7.5.
   
   El contraste con V1 y V2 es nítido: al ser *sin excedentes*, el artículo 7.1.b).i) las declara
   **exentas de obtener permisos de acceso y conexión**. Esa asimetría —no la superficie ni el
   coste— es la principal barrera de entrada de la variante 3.

### 7.2 El proyecto de RD de centros de datos: el 80 % deja de ser una ambición y pasa a ser un umbral

El mismo RDL 7/2026, en su **disposición adicional primera**, ordenó aprobar por real decreto los
requisitos de sostenibilidad aplicables a los centros de datos. Ese desarrollo está **ahora mismo
en audiencia pública**:

| | |
| --- | --- |
| Norma | *Proyecto de Real Decreto por el que se regulan los requisitos de sostenibilidad energética, medioambiental y de resiliencia y soberanía digital aplicables a los centros de datos* |
| Trámite | Audiencia e información pública, MITECO |
| Plazo | **27 de agosto – 4 de septiembre de 2026** |
| Documentos | `Bibliografia/Fuentes/Normativa/MITECO_2026_PRD_CentrosDatos_audiencia_publica.pdf` y su memoria de análisis de impacto normativo |

**Lo que exige, artículo por artículo:**

| Art. | Requisito | Cifra |
| --- | --- | --- |
| 2.1 | Ámbito: centros de datos que soliciten permisos de acceso y conexión (RD 1183/2020) | potencia de acceso **≥ 1 MW** (también grupos de CPD en la misma ubicación y titularidad que agreguen esa potencia) |
| 2.3 | Obligación de publicidad del art. 14 | potencia de TI **≥ 500 kW** |
| 6.1 | Eficiencia energética e hídrica: clase «A» de la etiqueta europea (Directiva (UE) 2023/1791) | transitoriamente, hasta agosto de 2027: **PUE ≤ 1,15** y **WUE ≤ 0,1** (anexo III del Reglamento Delegado (UE) 2024/1364) |
| 7 | Los requisitos renovables decaen si la cuota renovable nacional supera el 90 % en el año n−2 | **90 %** |
| 8 | **Adicionalidad**: cubrir el 80 % del consumo total con autoconsumo (RD 244/2019) o PPA con productores renovables ubicados en España | **80 %**, con acta de puesta en servicio no anterior en más de **18 meses** |
| 9 | **Correlación horaria**: la energía consumida **en cada hora** respaldada al menos en un 80 % por renovable generada **en esa misma hora** | **80 % horario** |
| 10 | Recargo sobre peajes y cargos por incumplimiento | **65 %**, +10 puntos por cada año consecutivo adicional |
| 12 | Características exigidas a los PPA | duración mínima **10 años**, elevación a escritura pública |

El artículo 9.1 dice literalmente:

> «(…) deberán garantizar que la energía consumida en cada hora se encuentra respaldada, al menos
> en un **80 por ciento**, por un volumen equivalente de electricidad de origen renovable
> **generada en esa misma hora**. El respaldo podrá articularse mediante alguna de las modalidades
> de autoconsumo previstas en el Real Decreto 244/2019, de 5 de abril, o mediante uno o más
> contratos de compra de electricidad renovable a plazo (…)»

> ### Por qué esto reorienta el TFM
>
> **La métrica que exige el borrador es exactamente la que este análisis lleva calculando.** No es
> el balance anual neto —el que daba «100 % de cobertura» con 2,81 ha— sino la **autosuficiencia
> real hora a hora**, que es el C_D que se ha venido reportando en todas las tablas. Y el umbral
> que fija, el **80 %**, es justo el objetivo que se había elegido como referencia.
>
> Dicho de otro modo: el criterio de diseño que se adoptó por rigor técnico resulta ser, cinco
> meses después, el criterio regulatorio. Eso convierte la tabla del apartado 5.6 en algo más que
> un ejercicio académico.
>
> **Y el artículo 9.3 menciona expresamente las «instalaciones de producción y, en su caso, de
> almacenamiento asociadas»** a efectos de verificar el cumplimiento horario. El almacenamiento no
> es un añadido opcional en el esquema de la norma: es un medio reconocido para cumplirla. Esto
> refuerza, desde el lado regulatorio, la justificación de la batería que en el apartado 5.5 se
> había obtenido solo desde el lado físico.

### 7.3 El CPD de este TFM no está sujeto, y esa es una decisión que hay que argumentar

Hay que ser precisos con el ámbito, porque es tentador exagerarlo:

- El artículo 2.1 aplica la norma a los centros de datos **que hayan solicitado o vayan a
  solicitar** los permisos de acceso y conexión.
- La **disposición transitoria tercera** lo cierra: los requisitos «se aplicarán a todos los
  centros de datos **que se conecten con posterioridad a su entrada en vigor**», entendiendo por
  conectado el que está acoplado eléctricamente y tiene contrato ATR suscrito.
- El CPD de este TFM está en explotación, con contrato ATR vigente. **No queda sujeto.**
- Tampoco alcanzaría el umbral del artículo 2.3 para la obligación de publicidad: su potencia de
  TI media es de ~295 kW (2.585 MWh/año), por debajo de los 500 kW.

**Pero el proyecto del TFM sí lo activa.** Instalar 1–2,5 MWp en una parcela a 2,93 km exige
solicitar permisos de acceso y conexión para la planta, y una ampliación o modificación de la
potencia de acceso del propio CPD entraría en el supuesto del artículo 2.1. Conviene por tanto
plantear el diseño como **conforme por anticipado**: no porque obligue hoy, sino porque es la
dirección en la que va la norma y porque un CPD con PUE 1,482 está lejísimos del 1,15 que se
exigirá a los nuevos.

Eso da, además, un argumento adicional y no buscado para la geotermia del apartado 5.2: el
PUE estimado bajaría de **1,482 a ~1,341**. Sigue por encima de 1,15, pero recorta el 30 % de la
distancia. Cerrar esa brecha del todo exigiría medidas de refrigeración que quedan fuera del
alcance de este TFM, y merece la pena decirlo explícitamente en la memoria en vez de dejarlo
implícito.

### 7.4 Si se optase por la vía del PPA

Ha dejado de ser la salida forzosa, pero sigue siendo el término de comparación económica. El
artículo 12 del borrador fija qué tendría que cumplir un PPA para servir a efectos de
adicionalidad y correlación horaria, y **tres de esas condiciones descartan de entrada las
soluciones más habituales en grupos multinacionales**:

- **c)** «No se considerarán válidos los contratos financieros suscritos por la sociedad matriz o
  por otra sociedad del grupo en los que dicha relación no quede reflejada.» → un PPA virtual
  firmado a nivel de grupo no computaría.
- **e)** Exclusión de coberturas basadas en productos a plazo de mercados organizados «cuyo origen
  renovable se acredite exclusivamente mediante garantías de origen». → comprar GdO sueltas no
  vale.
- **f)** Duración mínima de **diez años**, y **g)** elevación a escritura pública.

Es decir: el borrador empuja hacia el PPA físico, nominado a instalaciones concretas y de largo
plazo, que es precisamente el modelo que en la literatura se asocia al *24/7 carbon-free energy
matching* frente al simple *annual matching* con certificados.

#### 7.4.1 Qué modalidad de PPA encaja aquí

La taxonomía estándar distingue tres estructuras, y la elección no es de matiz sino estructural:

| Modalidad | Flujo físico | Qué resuelve | Encaje con la variante 3 |
| --- | --- | --- | --- |
| **Físico *on site*** | La planta está en el emplazamiento del consumidor | Suministro directo, sin red | No aplica: la parcela está a 2,93 km |
| **Físico *off site* (*sleeved*)** | La energía llega por la red a través de una comercializadora que hace de intermediaria | Suministro real + atributos verdes | **Es la estructura equivalente al esquema de la variante 3** si se descarta el autoconsumo a distancia |
| **Virtual (VPPA)** | No hay flujo físico: solo liquidación financiera por diferencias + garantías de origen | Cobertura de precio y atributos, no suministro | **Descartado** por el art. 12.c) y 12.e) del borrador de RD |

El punto que conviene retener: con el RDL 7/2026 en la mano, el autoconsumo a distancia es la vía
preferente y el PPA *sleeved* es el plan B. Pero **no son excluyentes en el capítulo económico**:
el precio del PPA es el término de comparación natural para el LCOE que arroje el modelo propio.

#### 7.4.2 Órdenes de magnitud y precedentes del mercado español

Cifras tomadas de la presentación `M1_T11_PPA.pdf` del propio máster (Marta Arias Álvarez, EDP,
2025), resumida en `conocimiento fotovoltaico/Referencia/ppa-renovables-mercado-energetico.md`.
**Material docente, no citable:** antes de entrar en la memoria hay que reextraer cada cifra de su
fuente primaria (LevelTen Energy, WindEurope, PexaQuote, BOE).

- **Precio de referencia solar en España:** índice LevelTen P25, **38,97 €/MWh** en Q4 2024
  (−9,4 % interanual), con caídas adicionales de ~5 % en Q1 2025 y un repunte del +4,2 % en junio
  de 2025. Es menos de la mitad del P25 europeo mixto (75,97 €/MWh).
- **Subasta española** (BOE-A-2021-1251): 2.036 MW FV adjudicados entre **14,89 y 28,9 €/MWh**.
  Es un suelo de mercado, no un precio contratable hoy, y conviene decirlo al usarlo.
- **España es el primer mercado europeo de PPA** por capacidad acumulada: **6.852 MW**, muy por
  delante de Suecia (4.043) y Alemania (3.429).
- **Duración modal en España/Portugal: 10 años** (12 de 16 contratos de 2020-2022) — coincide
  exactamente con el mínimo que exigirá el art. 12.f) del borrador de RD.
- **Precedentes españoles físicos *off site*:** Acciona–Telefónica (100 GWh/año, 10 años),
  Iberdrola–Orange (200 GWh/año, 12 años), Endesa–Cellnex (300 GWh/año, 10 años). El único
  *on site* documentado, Iberdrola–Makro, es de **6 MW**.

> ### Dos hallazgos que refuerzan el planteamiento del TFM
>
> **1. La carga plana 24/7 es el perfil de comprador que el mercado PPA prefiere.** La modalidad
> *baseload* es la que mejor reparte el riesgo de precio y de volumen entre las partes, frente a
> *as generated* (riesgo al comprador) y *as consumed* (riesgo al vendedor). Un CPD de
> 3.832 MWh/año con ~437 kW planos es el arquetipo. Lo que en el apartado 5.5 aparecía como el
> gran problema técnico —la carga plana satura el C_D en el 50,5 %— es, en el mercado de
> contratos, una ventaja.
>
> **2. Los operadores de centros de datos ya son los mayores compradores europeos.** En 2023
> Amazon compró **1.876 MW**, **Equinix 539 MW** (quinto comprador europeo y operador de CPD
> puro), Microsoft 351 MW y Google 346 MW. El PPA no es una alternativa exótica para un CPD: es
> lo que hace el sector. Esto da respaldo documental al bloque 4 de
> `Memoria/analisis/referencias-autoconsumo-cpd.md`.
>
> **Y una laguna que es en sí misma un resultado:** de los diez acuerdos españoles de septiembre
> de 2025 recogidos en la fuente, **ninguno declara capacidad de almacenamiento asociada**, pese a
> que el Reglamento (UE) 2024/1747 ya anticipa cláusulas de flexibilidad y almacenamiento en los
> PPA. El mercado sigue contratando energía anual, no energía horaria. **Ahí es exactamente donde
> el art. 9 del borrador español y este TFM se adelantan.**

### 7.5 Evacuación, punto de conexión y capacidad de acceso

Este es el apartado que decide si la variante 3 es ejecutable, y es independiente de todo lo
anterior: la distancia ya está resuelta y el suelo sobra, pero **la capacidad puede no existir**.

#### 7.5.1 Por qué hay que evacuar a la red sí o sí

Encadenando los tres preceptos ya citados:

| Precepto | Qué dice | Consecuencia |
| --- | --- | --- |
| RD 244/2019 art. 4.5.c) *(red. RDL 7/2026)* | El autoconsumo a través de la red **debe ser con excedentes** | La V3 no puede llevar antivertido |
| RD 244/2019 art. 7.1.b).iii) | Con excedentes y > 15 kW → **permisos de acceso y conexión obligatorios** | La V3 entra en el RD 1183/2020 |
| RD 244/2019 art. 3.g) | La energía llega al consumidor **«a través de las líneas de transporte o distribución»** | No hay línea propia: se inyecta en un nudo y se retira en otro |

De ahí la idea que conviene fijar: **en el autoconsumo a distancia no hay ningún electrón que
viaje de la planta al CPD.** La planta inyecta en su nudo, el CPD consume del suyo, y lo que los
une es una **liquidación horaria** que hace la distribuidora aplicando el anexo I del RD 244/2019.
El autoconsumo es real a efectos de facturación y **virtual a efectos físicos**. Por eso el
artículo 3.g) insiste dos veces en que la distancia se mide **entre los equipos de medida**: lo
que la norma acota no es la longitud de un cable, sino la separación entre dos puntos frontera.

#### 7.5.2 Cuándo la evacuación va a una SET, y de qué red

**El nudo lo elige y lo nombra el solicitante.** El artículo 10.1 del RD 1183/2020 es explícito:

> «En el caso de los permisos de acceso y de conexión para las instalaciones de generación de
> **más de 100 kW**, las solicitudes deberán efectuarse **para un nudo o tramo de línea concreto
> de la red**.»

Es decir, el promotor identifica el nudo —o el tramo de línea— y solicita ahí; en transporte, eso
obliga además a localizar previamente la SET de afección. Lo que hace el gestor es **evaluar** si
hay capacidad (art. 11) y responder con una **propuesta previa** (art. 12) que fija tensión,
ubicación exacta, potencias de cortocircuito y el pliego de condiciones técnicas de la conexión —
o denegar (art. 9). El promotor propone el nudo; el gestor valida y concreta el punto. Para el
orden de magnitud de la variante 3 (1–2,5 MWp) el escenario esperable es
conexión a la **red de distribución en media tensión**, y dentro de ella caben dos soluciones muy
distintas en coste:

| Solución | Cuándo | Implicación |
| --- | --- | --- |
| **Entronque en línea aérea/subterránea de MT existente** (15/20 kV) | Hay capacidad en el nudo y la línea admite la potencia | La más barata: CT de la planta + celdas + tramo de conexión |
| **Conexión directa a barras de una SET de distribución** | La línea no admite la potencia, o el gestor lo impone | Obliga a llevar la línea hasta la SET y, en su caso, a ampliar posición |
| **Conexión a la red de transporte (≥ 132/220 kV)** | Solo si el gestor lo exige por saturación | Descartable a esta escala: la SET propia y la posición en 220 kV no guardan proporción con 1–2,5 MW |

**El inventario de subestaciones del `TFM.kmz`** (versión de Mario del 29/08/2026, once
subestaciones con sus niveles de tensión) no es un dato de contexto: es **el mapa de puntos de
conexión candidatos**. Medidas sobre el KMZ, ordenadas por distancia a la parcela:

| Subestación | d. al CPD | **d. a la parcela** | Tensiones | Gestor |
| --- | --- | --- | --- | --- |
| Tres Cantos GIS 220 | 0,59 km | **2,35 km** | 220 kV | REE |
| La Cereal 220 – La Cereal 400 | 0,56 km | **2,41 km** | 400/220 kV | REE |
| **Tres Cantos 220 – T.CANTOS 3570 20 – TCANTOS A1 3570 66** | 2,33 km | **3,10 km** | **220/66/20 kV** | REE + i‑DE |
| BBVA 4145 66 | 2,48 km | 3,98 km | 66 kV | i‑DE |
| Lavander 4196 20 – Lavanderas A 4196 66 | 8,66 km | 4,28 km | 66/**20** kV | i‑DE |
| C. Viejo 4013 20 – C. Viejo A 4013 66 | 8,54 km | 4,68 km | 66/**20** kV | i‑DE |
| i‑DE Alcobe.M 3227 20 | 7,84 km | 10,78 km | 20 kV | i‑DE |
| Alcobendas 220 | 7,87 km | 10,80 km | 220 kV | REE |
| i‑DE Equinix 4457 66 | 8,47 km | 11,35 km | 66 kV | i‑DE |
| Fuencarral 220 – Fuencarral 400 | 9,56 km | 12,32 km | 400/220 kV | REE |
| i‑DE Fuenca.M 3308 20 – Fuencarr 3308 66/132 | 9,71 km | 12,48 km | 132/66/**20** kV | i‑DE |

> **El resultado que decide el punto de conexión.** Las dos subestaciones más próximas a la
> parcela —Tres Cantos GIS y La Cereal, a 2,35 y 2,41 km— son **exclusivamente de transporte**:
> no tienen nivel de media tensión, así que **no son puntos de conexión viables** para una planta
> de 2–2,5 MW. La primera con nivel de **20 kV** es **Tres Cantos 3570**, a **3,10 km** de la
> parcela. Es, con diferencia, la candidata natural: transformación 220/66/20 en el mismo
> emplazamiento y a solo 2,33 km del propio CPD.
>
> **Y el prefijo «i‑DE» de las etiquetas resuelve la duda del apartado 7.5.3: la distribuidora de
> la zona es i‑DE (Iberdrola Distribución), no UFD.** La numeración de cuatro dígitos (3570, 4196,
> 4013, 3227, 3308, 4145, 4457) es la nomenclatura de Iberdrola. Confírmese igualmente con el CUPS.
>
> Curiosidad con valor de contexto para la memoria: el inventario incluye una **SET «i‑DE Equinix
> 4457» de 66 kV**, es decir, un centro de datos de la zona con subestación propia dedicada. Es un
> término de comparación útil sobre el orden de magnitud al que trabaja el sector.

**Falta identificar las líneas de MT que cruzan o bordean la parcela**, que es lo que realmente
decide el coste de conexión: entroncar en una línea de 20 kV existente es mucho más barato que
llevar la línea hasta las barras de Tres Cantos 3570.

#### 7.5.3 Qué mapa de capacidad hay que mirar

Desde el RDL 7/2026 (disposición final decimoquinta, que reescribió el art. 2.k) del
RD 1183/2020) la capacidad de acceso está definida en dos sentidos que **no son intercambiables**:

> «k) *Capacidad de acceso*: será la potencia activa máxima que podrá **inyectarse** a la red por
> una instalación de generación de electricidad **o absorbida** de la red por una instalación de
> demanda (…)»

De modo que hay **dos contabilidades separadas** y el proyecto toca las dos, pero por motivos
distintos:

| Contabilidad | Quién la consume | En este TFM |
| --- | --- | --- |
| **Capacidad de acceso de GENERACIÓN** | La planta de la V3, que inyecta | **Es la que hay que consultar.** Sin capacidad de generación en el nudo, la variante 3 no existe, por mucho suelo y mucha distancia habilitada que haya |
| **Capacidad de acceso de DEMANDA** (firme u ordinaria / flexible) | El CPD, que absorbe | Solo si se amplía la potencia de acceso del CPD. **Ojo:** hacerlo es justo lo que activaría el ámbito del art. 2.1 del proyecto de RD de centros de datos (apartado 7.3) |

**Dónde mirar, en la práctica:**

1. **Identificar primero la distribuidora** por el CUPS de la factura del CPD. En el entorno de
   Tres Cantos la distribuidora es **i‑DE (Iberdrola Distribución)**, según las etiquetas del
   `TFM.kmz` y la nomenclatura numérica de sus subestaciones — **confirmar contra el CUPS de la
   factura**. (Una versión anterior de este documento apuntaba a UFD; era una conjetura, y el
   inventario de subestaciones la desmiente.)
2. **Red de distribución:** consultar el mapa/fichero de capacidad de la distribuidora que
   resulte. Los ficheros descargables (xlsx/csv) son más fiables que el visor cartográfico.
3. **Red de transporte:** el mapa de capacidad de acceso publicado por Red Eléctrica, para los
   nudos de 220 kV del inventario.
4. **Sesgo a tener presente:** la capacidad publicada es una **foto con fecha**, y en la red de
   distribución española la saturación de nudos es la norma y no la excepción. El dato hay que
   fecharlo en la memoria y, si es determinante, contrastarlo con una consulta formal al gestor.

#### 7.5.4 El acceso flexible y el régimen de la batería

> **Corrección (29/08/2026).** Una versión anterior de este apartado afirmaba que la batería del
> TFM entra en el régimen de acceso flexible del art. 33.13 de la Ley 24/2013. **Es incorrecto para
> una batería de autoconsumo**, por lo que se explica a continuación. La afirmación solo vale para
> almacenamiento que solicita permiso de acceso propio.

**Dónde NO se aplica: la batería integrada en el autoconsumo.** La **disposición transitoria
quinta del RD 244/2019** resuelve el encaje de las baterías de autoconsumo:

> «(…) dichos elementos de almacenamiento se instalarán de tal forma que **compartan equipo de
> medida y protecciones con la instalación de generación**.»

Es decir: en autoconsumo, la batería **no es una instalación independiente**. Va detrás del mismo
contador y de las mismas protecciones que el campo fotovoltaico, y jurídicamente forma parte de la
instalación de generación. No solicita permiso propio, luego no hay «permiso de demanda» que pueda
ser firme o flexible. Y el **RD 1183/2020, art. 3.2** lo cierra por el otro lado, excluyendo de su
ámbito a las instalaciones de almacenamiento «**cuando las mismas nunca inyecten energía a las
redes de transporte o distribución**».

**Consecuencia por variante:**

| Batería en… | ¿Instalación independiente? | ¿Permiso de acceso de demanda? | ¿Art. 33.13 (flexible)? |
| --- | --- | --- | --- |
| **V1 / V2** (sin excedentes, nunca inyecta) | No: DT 5.ª, comparte medida y protecciones | **No** | **No aplica** |
| **V3, hibridada con la planta**, cargando solo de la FV | No: parte de la instalación de generación | **No** por sí misma | **No aplica** |
| **V3, con capacidad de cargar de la red** | **Sí** | **Sí** | **Sí, flexible por imperativo legal** |

**La frontera real es si la batería puede cargar de la red**, no dónde esté físicamente. Y es una
decisión de diseño con consecuencias: una batería que solo carga de la fotovoltaica se queda fuera
de todo el régimen de acceso; una que además pueda cargar de la red —para arbitraje, o para
garantizar el 80 % horario del borrador de RD en días de poco sol— entra en él.

**El aparente conflicto con la DT sexta se resuelve así:** el art. 33.13 es la **regla de futuro**
(los permisos que se otorguen serán flexibles) y la DT sexta es la **vía de migración** para el
almacenamiento que **ya tiene** un permiso de demanda firme concedido antes de la reforma. A esos
no se les puede reconvertir el permiso por decreto, así que se les da un plazo de tres meses y se
usa como incentivo la pérdida de las exenciones de peajes y cargos. No hay contradicción: una cosa
es lo que se concede a partir de ahora y otra qué se hace con lo ya concedido.



El RDL 7/2026 no solo tocó las distancias del autoconsumo: **creó la figura del acceso flexible**
y la aplicó al almacenamiento de forma imperativa. Su preámbulo lo explica:

> «(…) se regula la figura del **acceso flexible** a las redes eléctricas (…). Frente al modelo
> tradicional "firme" del acceso —que exige garantizar el suministro todas las horas del año y
> deja sin utilizar márgenes de red disponibles— el acceso flexible (…) permitirá que
> determinados **consumos modulables y el almacenamiento** se conecten bajo condiciones
> explícitas de disponibilidad de red. Con ello **aflora capacidad adicional hoy bloqueada** (…)»

Y el articulado lo convierte en obligación. La **disposición final octava, apartado Seis**, añadió
un **apartado 13 al artículo 33 de la Ley 24/2013**:

> «13. Los permisos de acceso y conexión de las **instalaciones de almacenamiento** serán
> permisos de **acceso flexibles desde la perspectiva de demanda**.»

**Qué significa esto para este TFM.** El CPD ya está conectado y con contrato ATR, así que la
reforma del acceso de demanda no le afecta *como consumidor*. Y su batería, mientras cargue solo
de la fotovoltaica, tampoco entra en el régimen. **Solo si se le da capacidad de cargar de la red**
pasa a ser instalación de almacenamiento con permiso propio, y entonces:

1. Ese permiso de demanda será **flexible por imperativo legal** (art. 33.13) — no es una opción.
2. Le aplicarían las exenciones de peajes y cargos sobre la energía de carga: **art. 1.3.b) del
   RD 148/2021** exime de cargos «la energía consumida por los titulares de instalaciones de
   almacenamiento (…) **que sea posteriormente inyectada en la red**», y **art. 2.2.d) de la
   Circular 3/2020** exime de peajes a «las baterías de almacenamiento conectadas en la red de
   transporte o distribución». La lógica es evitar el doble pago: se paga cuando la energía se
   consume de verdad, no cuando solo pasa por la batería.
3. **Por qué la batería no cuenta como «consumidor».** Normalmente, todo lo que retira energía de
   la red es consumidor y paga peajes y cargos por ello. Si la batería contase como consumidor,
   cada kWh pagaría al cargarse y **volvería a pagar** cuando el CPD lo gastase: peaje doble por
   la misma energía. Para evitarlo, el nuevo último párrafo del art. 39.3 de la Ley 24/2013
   declara que **no tienen consideración de consumidor** las instalaciones de producción
   hibridadas con almacenamiento que, conforme a su permiso, puedan consumir de la red. La
   consecuencia práctica: **una batería hibridada con la planta de la V3 y una batería suelta
   junto al CPD no son la misma figura jurídica ni pagan lo mismo.**

> **Sobre la demanda flexible como oportunidad para centros de datos.** La intuición es correcta y
> la norma la respalda: el acceso flexible existe precisamente para **consumos modulables**, y en
> un contexto de nudos saturados es la puerta que queda abierta. El problema es igual de real: un
> CPD con compromisos de disponibilidad no puede ofrecer modulación de su carga de TI. **La salida
> que la propia norma sugiere no es modular el CPD, sino modular su almacenamiento**, que es lo
> que el art. 33.13 declara flexible por defecto. Para un CPD *nuevo*, presentar el conjunto
> CPD + BESS puede ser la diferencia entre obtener acceso y no obtenerlo. Para este CPD, que ya
> está conectado, el interés es menor pero no nulo: es el marco en el que se va a tramitar su
> batería.

> **Riesgo abierto que sustituye al de la distancia.** El apartado 5.6.1 cerró el riesgo
> regulatorio de los 2,93 km. Lo que ocupa ahora ese lugar en la lista de riesgos del proyecto no
> es la superficie ni el coste: es **si existe capacidad de acceso de generación disponible** en
> algún nudo razonablemente próximo a la parcela. Es una comprobación de horas, no de semanas, y
> conviene hacerla antes de invertir tiempo en la simulación PVsyst de la variante 3.

### 7.6 La energía autoconsumida de la V3 SÍ paga peaje de red

> **Corrección (29/08/2026), con impacto directo en el capítulo económico.** Una versión anterior
> de este documento afirmaba, apoyándose en los artículos 17.1 y 18.1 del RD 244/2019, que la
> energía autoconsumida renovable está «exenta de todo tipo de peajes y cargos» también en el
> autoconsumo a distancia. **Al ir a la fuente que fija los peajes, resulta que no es así.**

La **Circular 3/2020 de la CNMC**, que es la norma que establece la metodología de los peajes,
explica el matiz en su preámbulo:

> «El artículo 9 de la Ley 24/2013 establece que la energía autoconsumida de origen renovable,
> cogeneración o residuos estará exenta de todo tipo de cargos y peajes. **En caso de que se
> produzca una transferencia de energía a través de la red de distribución en instalaciones
> próximas a efectos de autoconsumo, se podrán establecer las cantidades que resulten de aplicación
> por el uso de dicha red de distribución.**»

Y su **artículo 2.3** lo aplica sin ambigüedad:

> «Asimismo, la circular será de aplicación para la determinación de los pagos por el uso de las
> redes de los autoconsumidores por la energía consumida de la red **y por la energía autoconsumida
> en el caso instalaciones próximas a través de la red**.»

Para materializarlo, la Circular crea una **familia de peajes específica, los «TDA»** (art. 9.3):
2.0TDA, 3.0TDA y 6.1TDA a 6.4TDA, compuestos **solo de términos de energía** —sin término de
potencia— aplicables a la energía autoconsumida a través de la red. Para una planta y un CPD en
media tensión el que aplicaría es el **6.1TDA** (tensiones entre 1 y 30 kV).

**La regla, ordenada:**

| Concepto | V1 y V2 (red interior) | **V3 (a través de la red)** |
| --- | --- | --- |
| Energía autoconsumida — **peajes** | **Exenta** | **Paga peaje 6.1TDA** (solo términos de energía) |
| Energía autoconsumida — **cargos** | **Exenta** (Ley 24/2013 art. 9.5) | **Exenta** (la salvedad de la Circular es solo por *uso de red*) |
| Energía retirada de la red | Peajes y cargos completos | Peajes y cargos completos |

> **Por qué importa.** El argumento de que «el autoconsumo a distancia sale mucho más barato que un
> PPA porque no paga red» **queda matizado**: sí paga red, aunque con un peaje reducido y sin
> término de potencia. La ventaja económica de la variante 3 frente a un PPA es real pero **menor
> de lo que este documento daba a entender**, y el capítulo 8 tiene que cuantificar el 6.1TDA sobre
> los ~3.400 MWh/año autoconsumidos, no darlos por gratuitos. **Es la corrección de mayor impacto
> económico de todo el análisis hasta la fecha.**
>
> Pendiente: los **valores numéricos** del 6.1TDA los fija la CNMC por resolución anual, no la
> Circular. Hay que localizar la resolución vigente para 2026 antes de meter cifras.


---

## 8. Resumen ejecutivo

1. **El consumo total del CPD es 3.832 MWh/año**, no 1.260. Los 1.260 MWh del trabajo previo
   eran solo refrigeración y auxiliares. El C_D de partida del TFM es **4,3 %**, no 13,2 %.
2. **La carga es plana al 3,3 %**: base pura 24/7 de ~437 kW. Esto gobierna todo el diseño.
3. **V1** (BIPV 2,0 % + cubierta liberada 12,2 %) = **14,2 %**. El BIPV es marginal en energía;
   justifíquese por arquitectura, no por producción.
4. **La geotermia ahorra ~365 MWh/año (9,5 %)** por sí sola, equivalente a 205 kWp de FV sin
   ocupar superficie. Es la mejor relación resultado/esfuerzo del estudio, y además baja el PUE
   de 1,482 a ~1,341.
5. **V2** (marquesinas sobre los **3.332 m²** de huella medida) = **28,9 %**, con **680 kWp**.
   **Duplica lo que aporta toda la cubierta del edificio** y es mucho menos invasiva: es la mejor
   variante de las tres, con diferencia.
6. **Todo el emplazamiento (V1 + V2) llega al 36,8 %** — 38,1 % con geotermia — pero el A_PV cae
   al **85,0 %**: con 1.017 kWp ya sobran 249 MWh/año. **La batería se hace necesaria antes
   incluso de plantear la planta en suelo.**
7. **V3**: **1,32 ha/MWp**. Combinada con V1 + V2 y geotermia, cerrar el balance anual exige solo
   **1,33 ha** (frente a 2,81 ha si fuese la única medida: **−53 %**). La combinación es lo que
   hay que defender, no la comparación entre variantes excluyentes.
8. **Sin batería la autosuficiencia real satura en 50,5 %.** Con V1 + V2 + geotermia, el **80 %
   real** se alcanza con **1,32 ha de planta en suelo y 4,1 MWh** de almacenamiento.
9. **La batería queda justificada** por esta barrera física, no por el argumento de excedentes que
   no valía en el trabajo previo — y ahora también por vía regulatoria (punto 12).
10. **La parcela localizada tiene 58,84 ha y admitiría ≈37,9 MWp** (68,1 GWh/año, 17,8 veces el
    consumo del CPD). **El suelo deja de ser la restricción**: el 80 % de autosuficiencia real
    necesita el **2,6 % de la parcela**. El 100 % estricto no se alcanza ni con 25 MWp y 60 MWh —
    el último 0,1 % exigiría almacenamiento estacional.
11. **La distancia de 2,93 km ya no es un obstáculo.** El **RDL 7/2026, de 20 de marzo** elevó de
    500 m —la regla general, que sigue vigente— a **5.000 m** el límite del autoconsumo a través
    de la red, en un supuesto nuevo y específico para instalaciones FV o eólicas de hasta 5 MW. La variante 3 encaja con margen, sin línea directa y sin renunciar a la figura de
    autoconsumo. (Y la línea directa tampoco era imposible: lo era en BT, no en MT — 2,5 MW a
    20 kV son 72 A y un 0,4 % de caída sobre 3 km.)
12. **El proyecto de RD de centros de datos en audiencia pública (27/08–04/09/2026) exigirá que el
    80 % de la energía consumida en CADA HORA esté respaldada por renovable generada en esa misma
    hora**, más adicionalidad del 80 % y PUE ≤ 1,15. **Es exactamente la métrica de este análisis
    y exactamente su objetivo.** El CPD actual no queda sujeto (ya está conectado, DT 3.ª), pero
    el proyecto del TFM activaría el supuesto al solicitar nuevos permisos de acceso.

## 9. Pendiente de cerrar

| # | Asunto | Cómo |
| --- | --- | --- |
| 1 | ~~Superficie del aparcamiento~~ | **Cerrado: 3.332 m² de huella de marquesinas** (filas F1–F8 del `TFM.kmz`; confirmado por Mario el 28/08/2026 — `Parking - General`, 6.252 m², incluye las calles y no es la cifra buena). |
| 2 | ~~Localizar la parcela~~ | **Cerrado: 58,84 ha medidas sobre `TFM.kmz` (28/08/2026).** Sobra suelo por un factor 20. |
| 2a | ~~Encaje regulatorio de la distancia (2,93 km)~~ | **Cerrado: encaja.** RD 244/2019 art. 3.g).iii), redacción de la DF 14.ª del RDL 7/2026: hasta 5 MW y menos de 5.000 m. Falta solo medir la distancia definitiva **entre equipos de medida** cuando se fije el centro de seccionamiento. |
| 2c | **Titularidad y clasificación urbanística de la parcela** | **Dato crítico ahora.** Sede electrónica del Catastro + planeamiento de Tres Cantos / Colmenar Viejo. Con 1,33 ha necesarias sobre 58,84 disponibles hay mucho margen para elegir la subparcela más favorable. |
| 3 | Alcance del TFM: ¿total o solo HVAC? | Confirmar con Julio Amador — cambia el denominador de todo. El art. 9 del borrador de RD apunta claramente al consumo total. |
| 4 | SEER real de las enfriadoras y del sistema geotérmico | `investigador-cientifico` + placa de características. Ahora tiene más peso: de ello depende el PUE que se pueda alegar. |
| 5 | Densidad de potencia del vidrio BIPV | Datasheet de fabricante (Onyx Solar u otro) vía `bibliotecario-pdf`. |
| 6 | Reparto del no-IT (refrigeración / UPS / iluminación) | Se ha supuesto 70/22/8. Verificar si hay submedida. |
| 7 | ~~Capacidad de acceso de GENERACIÓN en los nudos próximos a la parcela~~ | **Cerrado con condiciones el 31/08/2026** sobre los mapas de REE (03/08/2026) e i‑DE (01/07/2026). **Por la vía ordinaria NO hay capacidad**: los 39 puntos de i‑DE del entorno cuelgan de *TRES CANTOS 220*, cuyos 326 MW de margen MPE están íntegramente marcados como no disponibles por reserva zonal de concurso (0 MW solicitables). **La salida es la DA 10.ª del RDL 7/2026**, que libera el 10 % de la capacidad reservada en nudos de concurso para autoconsumo y admite expresamente el acceso vía distribución: *TRES CANTOS GIS 220* (a 0,59 km del CPD y 2,35 km de la parcela) tiene **24 MW liberados y 0 otorgados**. Aparece además un techo de potencia nuevo por la condición b) del apartado 1 (P1/P_gen ≥ 0,5): **4,6 MW** con el CUPS actual. Análisis completo en `capacidad-acceso-conexion.md`. |
| 7c | **Confirmar el nudo de aceptabilidad de un punto de conexión en la parcela** | **Nueva incógnita crítica, heredera de la anterior.** Ningún punto de i‑DE declara afección a *Tres Cantos GIS 220*, pero REE le reconoce 3 posiciones existentes a red de distribución. Toda la V3 depende de que el punto de conexión caiga bajo el GIS y no bajo *Tres Cantos 220*. Se resuelve con consulta formal a i‑DE. Ver `capacidad-acceso-conexion.md` §7. |
| 6a | **Valores vigentes del peaje 6.1TDA para 2026** | **Impacto económico alto.** La Circular 3/2020 crea el peaje pero los precios los fija la CNMC por resolución anual. Sin ese dato no se puede cuantificar el coste de red de la variante 3 (apartado 7.6). |
| 6b | Trazado eléctrico de la V2: ¿línea propia de 216 m o conexión a red? | Decide si V2 es *red interior* (exenta de permisos y de peajes) o *a través de la red* (con permisos y con peaje). Ver 5bis.5. Recomendación: línea propia. |
| 6c | ¿La batería podrá cargar de la red? | Decide si entra en el régimen de acceso de demanda flexible (art. 33.13 Ley 24/2013) o queda fuera por la DT 5.ª del RD 244/2019. Ver 7.5.4. |
| 7a | Trazado de las líneas de MT que cruzan o bordean la parcela | Decide el coste de conexión (entronque en línea frente a llevar línea hasta SET). No está en el `TFM.kmz`. |
| 7b | Tensión de suministro actual del CPD y si ya dispone de CT propio | Condiciona el coste de cualquier alternativa de línea directa y la ampliación de potencia de acceso. De la factura y del esquema unifilar. |
| 8 | **Seguimiento del proyecto de RD de centros de datos** | La audiencia pública cierra el **4 de septiembre de 2026**. Vigilar el texto final antes de la entrega del TFM (15/09/2026) y, sobre todo, si el 80 % horario y el PUE 1,15 sobreviven al trámite. |
| 9 | Contraste con casos reales de CPD | **En marcha.** La vía PPA ya está cubierta (§7.4, a partir de `M1_T11_PPA.pdf` procesado). Queda descargar y procesar vía `bibliotecario-pdf` la literatura de *24/7 carbon-free energy matching* y los índices de precio primarios; lista de lectura priorizada en `Memoria/analisis/referencias-autoconsumo-cpd.md`. |
