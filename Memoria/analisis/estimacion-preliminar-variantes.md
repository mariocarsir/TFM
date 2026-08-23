---
title: "Estimación preliminar de las tres variantes de autoconsumo FV del CPD"
fecha: 2026-08-23
estado: preliminar
margen_objetivo: "5–8 %"
fuentes_canonicas:
  - "Datos/Consumo CPD/Mensual/ (12 ficheros, resolución 5 min, dic-2024 → nov-2025)"
  - "Documentacion de apoyo/Trabajo Autoconsumo CPD/Trabajo_DataCenter_Project.VC0-Report1.pdf (PVsyst V8.0.19)"
  - "Datos/Imagenes/PlantaCPD.png y VistaSatelitalCPD.png (Google Earth)"
tags: [fotovoltaica, autoconsumo, CPD, variantes, BIPV, marquesinas, planta-suelo, geotermia]
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
| **V2** Marquesinas de parking | **2.461 m²** (1.723 m² de marquesina) | **351** | **576** | 100 % | **15,0 %** |
| **V1 + V2** (todo el emplazamiento) | ≈ 4.495 m² | **689** | **1.120** | 99,5 % | **29,1 %** |
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

Superficie del aparcamiento **medida: 2.461 m²**.

```
Recinto de aparcamiento                        2.461 m²
  × 0,70  (fracción cubrible con marquesina: plazas y parte
           de los pasillos, descontando accesos y giros)     1.723 m²  de marquesina
  × 0,90  (ocupación de módulo sobre la marquesina)          1.550 m²  de módulo
  × 226,7 W/m²                                         →       351 kWp
```

| Magnitud | Valor |
| --- | --- |
| Potencia | **351 kWp** |
| Producción | **576 MWh/año** (Y_F 1.639 kWh/kWp) |
| Autoconsumo A_PV | **100 %** — el pico (258 kW) no llega a los 437 kW de carga |
| **Cobertura C_D** | **15,0 %** (16,6 % si la geotermia ya ha bajado el consumo) |

> **Es la variante con mejor relación cobertura/esfuerzo de las tres.** Con 2.461 m² de un recinto
> que ya está pavimentado y sin uso en altura, aporta **más que toda la cubierta del edificio**
> (15,0 % frente al 14,2 % de V1), sin tocar el sistema de refrigeración, sin obra sobre un
> edificio en explotación y con la ventaja añadida de sombrear las plazas. No hay excedentes:
> todo lo que produce se consume.

Regla parametrizada, por si el recinto se amplía o se reconsidera el factor de cubrición:
**≈ 143 kWp, ≈ 234 MWh/año y ≈ 6,1 % del consumo por cada 1.000 m² de aparcamiento.**
Los primeros excedentes no aparecerían hasta ~5.500 m².

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

---

## 6. Escenario combinado

| Escenario | kWp | E_PV | A_PV | C_D vs 3.832 | C_D vs 3.467 (con geotermia) |
| --- | --- | --- | --- | --- | --- |
| V1a BIPV tragaluz | 47 | 76 MWh | 100 % | 2,0 % | 2,2 % |
| V1 (tragaluz + cubierta) | 338 | 544 MWh | 100 % | 14,2 % | 15,7 % |
| V2 (marquesinas, 2.461 m²) | 351 | 576 MWh | 100 % | 15,0 % | 16,6 % |
| **V1 + V2 (todo el emplazamiento)** | **689** | **1.120 MWh** | **99,5 %** | **29,1 %** | **31,4 %** |

**Todo lo que cabe en la propiedad, sin salir de ella, es el 29,1 % del consumo** — un 31,4 % si
antes se ha hecho la geotermia. Y llega ahí **sin generar prácticamente excedentes** (A_PV 99,5 %):
689 kWp es justo la potencia que la carga plana de 437 kW es capaz de absorber. Es un punto de
diseño notablemente limpio.

### 6.1 Cuánta planta en suelo hace falta para cerrar el balance

| Escenario de partida | Falta por cubrir | **V3 necesaria** |
| --- | --- | --- |
| V1 + V2, sin geotermia | 2.712 MWh/año | 1,51 MWp = **1,99 ha** (19.910 m²) |
| **V1 + V2, con geotermia** | **2.347 MWh/año** | **1,31 MWp = 1,72 ha** (17.231 m²) |

Frente a las **2,81 ha** que haría falta si la planta en suelo fuese la única medida, el conjunto
**baja el requisito de suelo a 1,72 ha: un 39 % menos**. Este es el argumento para defender la
combinación de variantes en vez de compararlas como alternativas excluyentes.

### 6.2 El conjunto completo V1 + V2 + V3 con geotermia

**1.994 kWp** (338 en cubierta + 351 en marquesinas + 1.305 en suelo) → **3.467 MWh/año**, que
iguala exactamente el consumo en balance anual. Pero la autosuficiencia real sigue siendo del
**43,7 %**, con **1.953 MWh** vertidos a la red y recomprados de noche. Añadiendo batería:

| Batería | C_D real |
| --- | --- |
| — | 43,7 % |
| 1 MWh | 53,4 % |
| 2 MWh | 63,0 % |
| 3 MWh | 72,4 % |
| **4 MWh** | **80,2 %** |

---

## 7. Resumen ejecutivo

1. **El consumo total del CPD es 3.832 MWh/año**, no 1.260. Los 1.260 MWh del trabajo previo
   eran solo refrigeración y auxiliares. El C_D de partida del TFM es **4,3 %**, no 13,2 %.
2. **La carga es plana al 3,3 %**: base pura 24/7 de ~437 kW. Esto gobierna todo el diseño.
3. **V1** (BIPV 2,0 % + cubierta liberada 12,2 %) = **14,2 %**. El BIPV es marginal en energía;
   justifíquese por arquitectura, no por producción.
4. **La geotermia ahorra ~365 MWh/año (9,5 %)** por sí sola, equivalente a 205 kWp de FV sin
   ocupar superficie. Es la mejor relación resultado/esfuerzo del estudio.
5. **V2** (marquesinas sobre los 2.461 m² de aparcamiento) = **15,0 %**, con 351 kWp y sin un solo
   kWh de excedente. **Rinde más que toda la cubierta del edificio** y es mucho menos invasiva:
   es la variante con mejor relación cobertura/esfuerzo de las tres.
6. **Todo el emplazamiento (V1 + V2) llega al 29,1 %** — 31,4 % con geotermia — con A_PV 99,5 %.
   Ahí se agota la superficie propia.
7. **V3**: **1,32 ha/MWp**. En solitario, **2,81 ha** para el 100 % en balance anual y **2,25 ha**
   para el 80 %. Pero **combinada con V1 + V2 y geotermia bastan 1,72 ha** (−39 %). La combinación
   es lo que hay que defender, no la comparación entre variantes excluyentes.
8. **Sin batería la autosuficiencia real satura en 50,5 %.** Sobre el conjunto completo, llegar al
   **80 % real exige 4 MWh** de almacenamiento.
9. **La batería queda justificada** por esta barrera, no por el argumento de excedentes que no
   valía en el trabajo previo.

## 8. Pendiente de cerrar

| # | Asunto | Cómo |
| --- | --- | --- |
| 1 | ~~Superficie del aparcamiento~~ | **Cerrado: 2.461 m²** (aportado por Mario, 23/08/2026). |
| 2 | **Parcela para la planta en suelo** | Identificar y medir ≈1,72 ha; comprobar titularidad y clasificación urbanística. Es ahora el dato crítico. |
| 2b | Factor de cubrición del aparcamiento (0,70) | Verificar contra la trama real de plazas y viales del recinto. |
| 3 | Alcance del TFM: ¿total o solo HVAC? | Confirmar con Julio Amador — cambia el denominador de todo. |
| 4 | SEER real de las enfriadoras y del sistema geotérmico | `investigador-cientifico` + placa de características. |
| 5 | Densidad de potencia del vidrio BIPV | Datasheet de fabricante (Onyx Solar u otro) vía `bibliotecario-pdf`. |
| 6 | Reparto del no-IT (refrigeración / UPS / iluminación) | Se ha supuesto 70/22/8. Verificar si hay submedida. |
| 7 | Capacidad del punto de conexión | Con >1 MW cambia el procedimiento de acceso (RD 1183/2020). |
