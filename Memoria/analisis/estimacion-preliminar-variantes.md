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
  - "Bibliografia/PDFs/MITECO_2026_PRD_CentrosDatos_audiencia_publica.pdf (proyecto de RD, audiencia 27/08–04/09/2026)"
  - "Bibliografia/PDFs/BOE_RDL_7-2026_PlanIntegral_OrienteMedio.pdf (BOE-A-2026-6544)"
  - "Bibliografia/PDFs/BOE_RD_244-2019_autoconsumo_consolidado.pdf (texto consolidado, act. 21/03/2026)"
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
versión anterior de este documento se señaló como riesgo crítico, porque el umbral que se venía
manejando para el autoconsumo a través de la red eran 2.000 m. **Ese umbral ya no está vigente.**

El **Real Decreto-ley 7/2026, de 20 de marzo** (BOE-A-2026-6544, convalidado por el Congreso el
26 de marzo de 2026, BOE-A-2026-7125), en su **disposición final decimocuarta**, modificó el
artículo 3.g) del RD 244/2019. El texto consolidado vigente dice literalmente:

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

## 6. Escenario combinado

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
7/2026, de 20 de marzo** (BOE-A-2026-6544, convalidado el 26 de marzo, BOE-A-2026-7125) elevó de
2.000 a **5.000 m** la distancia admisible para el autoconsumo a través de la red, para
instalaciones fotovoltaicas o eólicas de hasta **5 MW**. Con 2,93 km y 1–2,5 MWp, la planta en
suelo entra en el supuesto con margen.

### 7.2 El proyecto de RD de centros de datos: el 80 % deja de ser una ambición y pasa a ser un umbral

El mismo RDL 7/2026, en su **disposición adicional primera**, ordenó aprobar por real decreto los
requisitos de sostenibilidad aplicables a los centros de datos. Ese desarrollo está **ahora mismo
en audiencia pública**:

| | |
| --- | --- |
| Norma | *Proyecto de Real Decreto por el que se regulan los requisitos de sostenibilidad energética, medioambiental y de resiliencia y soberanía digital aplicables a los centros de datos* |
| Trámite | Audiencia e información pública, MITECO |
| Plazo | **27 de agosto – 4 de septiembre de 2026** |
| Documentos | `Bibliografia/PDFs/MITECO_2026_PRD_CentrosDatos_audiencia_publica.pdf` y su memoria de análisis de impacto normativo |

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
    2.000 a **5.000 m** el límite del autoconsumo a través de la red para instalaciones FV de
    hasta 5 MW. La variante 3 encaja con margen, sin línea directa y sin renunciar a la figura de
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
| 7 | Capacidad del punto de conexión | Con >1 MW cambia el procedimiento de acceso (RD 1183/2020). |
| 8 | **Seguimiento del proyecto de RD de centros de datos** | La audiencia pública cierra el **4 de septiembre de 2026**. Vigilar el texto final antes de la entrega del TFM (15/09/2026) y, sobre todo, si el 80 % horario y el PUE 1,15 sobreviven al trámite. |
| 9 | Contraste con casos reales de CPD | **En marcha.** La vía PPA ya está cubierta (§7.4, a partir de `M1_T11_PPA.pdf` procesado). Queda descargar y procesar vía `bibliotecario-pdf` la literatura de *24/7 carbon-free energy matching* y los índices de precio primarios; lista de lectura priorizada en `Memoria/analisis/referencias-autoconsumo-cpd.md`. |
