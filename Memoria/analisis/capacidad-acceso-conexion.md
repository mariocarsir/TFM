---
title: "Capacidad de acceso de generación para la variante 3: análisis de los mapas de REE e i-DE"
fecha: 2026-08-31
estado: cerrado-con-condiciones
riesgo: "resuelto por vía RDL 7/2026 — condicionado a confirmación del nudo de aceptabilidad"
fuentes_canonicas:
  - "Datos/Capacidad AyC Generacion/2026_08_03_GRT_generacion.xlsx (Red Eléctrica, gestor de la red de transporte, publicación de 03/08/2026)"
  - "Datos/Capacidad AyC Generacion/2026_07_01_R1-001_Generacion.xlsx (i-DE Redes Eléctricas Inteligentes, código R1-001, publicación de 01/07/2026)"
  - "Bibliografia/Fuentes/Normativa/BOE_RDL_7-2026_PlanIntegral_OrienteMedio.pdf (BOE-A-2026-6544), disposición adicional décima"
  - "Bibliografia/Fuentes/Normativa/BOE_RD_1183-2020_acceso_conexion_consolidado.pdf, arts. 7 y 20.5"
  - "Datos/Google Earth/TFM.kmz (geometría de parcela y emplazamiento)"
  - "Datos/tarifa/2025 AGOSTO IBERDROLA.pdf (potencia contratada PC1 del CUPS ES0021000005763738ZG)"
tags: [acceso, conexion, capacidad, REE, i-DE, concurso, RDL-7-2026, autoconsumo, variante-3, Tres-Cantos]
---

# Capacidad de acceso de generación para la variante 3

> **Qué resuelve este documento.** Cierra el que era el riesgo crítico abierto del análisis de
> variantes (fila 7 del apartado 9 de `estimacion-preliminar-variantes.md`): si existe o no
> capacidad de acceso de generación en los nudos próximos a la parcela candidata. La respuesta
> corta es que **por la vía ordinaria no la hay, y que la única vía practicable es la que abre la
> disposición adicional décima del RDL 7/2026** — la misma norma que ya había desbloqueado la
> distancia de la variante 3.

---

## 1. Los dos ficheros y por qué hacen falta los dos

| Fichero | Publica | Fecha | Alcance |
| --- | --- | --- | --- |
| `2026_08_03_GRT_generacion.xlsx` | Red Eléctrica (GRT) | 03/08/2026 | 937 nudos de la red de transporte |
| `2026_07_01_R1-001_Generacion.xlsx` | i-DE (R1-001) | 01/07/2026 | 2.989 puntos de conexión de distribución, 437 en Madrid |

La variante 3 se conectaría en media tensión a la red de i-DE, así que la tentación es mirar solo
el fichero del distribuidor. **Es un error**, y es justo el error que este análisis evita: el
fichero de i-DE incluye una columna «Nudo Afección RdT» que remite al nudo de transporte cuya
capacidad condiciona la solicitud. Sin cruzar ambos ficheros, el dato del distribuidor se lee al
revés de como es.

## 2. Lo que dice i-DE por sí solo: aparente holgura

Cruzando las coordenadas UTM del fichero de i-DE con el centroide de la parcela
(UTM 30N X = 436.766, Y = 4.497.104, obtenido del `TFM.kmz`), los puntos de conexión más
próximos son los de la subestación **Tres Cantos 3570**, a 3,62 km del centroide de la parcela
(3,10 km al borde más cercano) y 2,31 km del CPD:

| Punto de conexión | Tensión | Capacidad disponible | Capacidad ocupada | Comentario de i-DE |
| --- | --- | --- | --- | --- |
| T.CANTOS T3 | 20 kV | 3,70 MW | 0,40 MW | Nudo de transporte en concurso de generación |
| T.CANTOS T4 | 20 kV | 3,70 MW | 0,69 MW | Nudo de transporte en concurso de generación |
| **T.CANTOS T7** | 20 kV | **22,31 MW** | 14,10 MW | — |
| **T.CANTOS T8** | 20 kV | **25,71 MW** | 10,32 MW | — |
| TCANTOS A1 | 66 kV | 3,70 MW | 0,00 MW | — |
| TCANTOS B1 | 66 kV | 18,02 MW | 0,00 MW | Nudo de transporte en concurso de generación |

Leído así, sobraría capacidad por un factor 10 frente a los 1,0–2,5 MW que necesita la variante 3.
**Ese es el dato que no hay que llevarse al documento.**

## 3. Por qué esa holgura es aparente: la afección a la red de transporte

Los **39 puntos de conexión** de i-DE en la provincia de Madrid del entorno de la parcela —los
seis de Tres Cantos 3570, los cuatro de Lavanderas 4196, los cinco de Colmenar Viejo 4013, el de
BBVA 4145 y los de San Agustín 4091— declaran **todos** el mismo nudo de afección:
**TRES CANTOS 220**. Y ahí es donde se decide.

Ficha de REE para ese nudo (código de subestación 50610):

| Concepto | MPE (parques: fotovoltaica y eólica) |
| --- | --- |
| Margen de capacidad de acceso total | 326 MW |
| Criterio limitante | WSCR_Nudo (potencia de cortocircuito) |
| **Capacidad NO disponible** | **326 MW** |
| Motivo | *Margen zonal reservado concurso por resolución SEE/posible concurso/NTJ* |
| Capacidad disponible para MPE conectados a red de distribución | **0 MW** |
| Capacidad disponible para MPE conectados a red de transporte | **0 MW** |
| Capacidad liberada para autoconsumo (RDL 7/2026) | **0 MW** |

Es decir: el nudo tiene 326 MW de margen técnico y **ninguno de ellos es solicitable**. Todo el
margen está congelado porque el nudo pertenece a una bolsa zonal (E345_SEPE en el criterio
estático, D74_SEPE en el dinámico) que contiene un nudo declarado en concurso de capacidad.

**Conclusión de este apartado: por el procedimiento general del artículo 7 del RD 1183/2020, la
variante 3 no obtendría permiso de acceso. Los 22–25 MW «disponibles» de T7 y T8 son capacidad
de la red de distribución que el gestor de transporte no puede aceptar.**

## 4. La salida: la disposición adicional décima del RDL 7/2026

El mismo real decreto-ley que elevó a 5.000 m la distancia del autoconsumo a través de la red
introdujo un segundo mecanismo, menos conocido, que resuelve exactamente este bloqueo. Texto
literal de la **disposición adicional décima**, apartado 1:

> «En aquellos nudos en los que la persona titular de la Secretaría de Estado de Energía haya
> resuelto o resuelva la celebración de un concurso de capacidad conforme a lo previsto en el
> artículo 20.5 del Real Decreto 1183/2020 […] **se liberará el 10 por ciento del total de la
> capacidad disponible en cada uno de esos nudos que se encuentre reservada para concurso** […]
> a nuevas instalaciones de generación de electricidad que utilicen fuentes de energía primaria
> renovable siempre que estas cumplan las siguientes condiciones:
> a) Estar asociadas a una modalidad de autoconsumo.
> b) El cociente entre la potencia contratada en el periodo P1 y la potencia de generación
> instalada sea al menos 0,5.»

Y el apartado 2, que es el que hace que esto sirva para un proyecto conectado en media tensión:

> «La capacidad liberada […] podrá ser otorgada tanto a instalaciones que accedan directamente a
> la red de transporte, **como a las que accedan a través de la red de distribución cuando estas
> requieran de informe de aceptabilidad por parte del gestor de la red de transporte**.»

### 4.1 Dónde está esa capacidad: Tres Cantos GIS 220

El fichero de REE incorpora seis columnas nuevas para este mecanismo. En el entorno del CPD hay
**dos** nudos de 220 kV, y la norma los trata de forma distinta:

| Nudo REE | Código | d(CPD) | d(parcela) | Motivo de no disponibilidad | Liberada autoconsumo MPE | Otorgada | **Disponible** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TRES CANTOS 220 | 50610 | 2,33 km | 3,10 km | Margen zonal reservado | 0 MW | 0 MW | **0 MW** |
| **TRES CANTOS GIS 220** | **50611** | **0,59 km** | **2,35 km** | **Concurso por resolución SEE** | **24 MW** | **0 MW** | **24 MW** |

La diferencia no es arbitraria y encaja con el articulado: la liberación del 10 % se aplica a los
nudos **en los que se ha resuelto celebrar un concurso**, no a los que simplemente pertenecen a
una bolsa zonal contaminada por un nudo en concurso. Tres Cantos GIS 220 es de los primeros
(24 / 244 = 9,8 % de su capacidad no disponible); Tres Cantos 220, de los segundos, y por eso se
queda con cero.

### 4.2 Verificación de esta lectura contra el conjunto del fichero

La interpretación no se ha dado por buena sin comprobarla en los 937 nudos:

- **335 nudos** de toda España tienen capacidad liberada para autoconsumo mayor que cero.
- **Los 335, sin una sola excepción**, llevan «Concurso por resolución SEE» en el motivo de
  capacidad no disponible. Ningún nudo con reserva meramente zonal recibe liberación.
- La **mediana del cociente** entre capacidad liberada y capacidad no disponible es **0,100**,
  exactamente el 10 % que fija la disposición adicional décima.

El dato del fichero y el texto de la norma dicen lo mismo, lo que permite usar ambos con
seguridad en el documento.

### 4.3 Panorama de la Comunidad de Madrid

Treinta y cinco nudos madrileños tienen capacidad liberada para autoconsumo, y **ninguno de ellos
tiene capacidad disponible por la vía ordinaria**: en toda la Comunidad, la columna de capacidad
disponible para MPE conectados a distribución vale cero en todos los nudos con liberación. Los
mayores son Majadahonda 220 (70 MW), Ventas del Batán 220 (69 MW) y Hortaleza 220 (68 MW), todos
ellos muy lejos del emplazamiento. **Dentro del radio de 5 km que exige el autoconsumo a través
de la red, el único nudo con capacidad de cualquier tipo es Tres Cantos GIS 220.** La variante 3
depende, literalmente, de un único nudo.

## 5. La condición b) fija un techo de potencia a la variante 3

La condición b) de la disposición adicional décima no es un trámite: es una **restricción de
dimensionado** que hasta ahora no estaba en el análisis de variantes.

De la factura de i-DE de agosto de 2025 (CUPS ES0021000005763738ZG, el del complejo Siemens de
Tres Cantos) se lee **PC1 = 2.300 kW**. Aplicando el cociente mínimo de 0,5:

$$P_{\text{gen,max}} = \frac{P_{\text{contratada,P1}}}{0,5} = \frac{2.300\ \text{kW}}{0,5} = 4.600\ \text{kW} = 4,6\ \text{MW}$$

Dos lecturas, según a qué punto de suministro se asocie el autoconsumo:

| Escenario | Potencia contratada P1 | Techo de generación | ¿Cabe la V3? |
| --- | --- | --- | --- |
| Autoconsumo asociado al **CUPS actual del complejo** | 2.300 kW | **4,6 MW** | Sí, con holgura (V3 combinada 1,0 MW; V3 aislada 2,25–2,50 MW) |
| Autoconsumo asociado a un **punto de suministro nuevo y propio del CPD** | ≈ 600 kW estimados (máx. medido 528 kW) | **≈ 1,2 MW** | Solo la V3 combinada (1,0 MW). **La V3 aislada de 2,25–2,50 MW quedaría fuera** |

Obsérvese además que el techo de 4,6 MW es **más restrictivo que el límite de 5 MW** del
artículo 3.g).iii) del RD 244/2019 en su redacción del RDL 7/2026. Si el proyecto se asocia al
CUPS actual, la potencia máxima de la variante 3 la fija esta condición b), no el límite de la
modalidad de autoconsumo.

> **Cautela pendiente.** «Potencia de generación instalada» debe entenderse conforme a la
> definición aplicable a instalaciones fotovoltaicas (menor entre la suma de potencias nominales
> de inversores y la suma de potencias pico de módulos). Con relación DC/AC mayor que 1 el techo
> se aplicaría sobre el valor que corresponda, y conviene fijarlo antes de cerrar el dimensionado.

## 6. La ventana se cierra el 21 de marzo de 2028

El apartado 3 de la disposición adicional décima limita el mecanismo a **dos años desde la entrada
en vigor** del real decreto-ley (BOE de 21/03/2026): pasado ese plazo, la capacidad no otorgada
vuelve a quedar reservada para concurso. El apartado 4 añade que **la no acreditación en tiempo y
forma** de la modalidad de autoconsumo y del cociente de potencia **supone la caducidad automática
de los permisos de acceso y conexión**.

Para el TFM esto es una ventaja argumental: el proyecto se plantea dentro de una ventana temporal
concreta y verificable, y el propio calendario de tramitación pasa a ser un elemento de diseño y
no un trámite accesorio.

## 7. Lo que queda por confirmar

| # | Asunto | Por qué importa |
| --- | --- | --- |
| 1 | **Qué nudo de aceptabilidad corresponde realmente a un punto de conexión en la parcela** | Ningún punto de i-DE del fichero declara afección a *Tres Cantos GIS 220*, pero REE le reconoce **3 posiciones existentes a red de distribución**. O hay un desfase de nomenclatura entre ambos ficheros, o esas posiciones son de otro titular. **Es la incógnita de la que depende toda la variante 3** y se resuelve con una consulta formal a i-DE sobre el punto concreto. |
| 2 | Desfase de fechas entre publicaciones | El fichero de i-DE es de **01/07/2026** y el de REE de **03/08/2026**. i-DE aún no refleja el mecanismo de la DA 10.ª en ninguna columna propia. Conviene contrastar con la publicación de i-DE de agosto o septiembre. |
| 3 | Definición de «potencia de generación instalada» a efectos de la condición b) | Fija el techo real: 4,6 MW o el valor que resulte de aplicar la definición sobre AC o DC (apartado 5). |
| 4 | A qué punto de suministro se asocia el autoconsumo | Decide entre un techo de 4,6 MW y uno de ≈1,2 MW (apartado 5), y por tanto si la variante 3 aislada sigue siendo defendible. |

## 8. Consecuencias para el documento

1. **El riesgo crítico queda cerrado, pero no como se esperaba.** No hay capacidad por la vía
   ordinaria: la hay por una vía excepcional, acotada en el tiempo y condicionada.
2. **El capítulo de tramitación gana un contenido propio y actual.** El TFM puede explicar el
   mecanismo de la disposición adicional décima con datos publicados y verificados, algo que
   ninguno de los tres TFM de referencia aborda.
3. **El RDL 7/2026 resuelve los dos obstáculos de la variante 3** —la distancia y la capacidad—
   por dos vías independientes. Eso refuerza el encaje regulatorio del trabajo y conviene
   presentarlo así de forma explícita.
4. **Aparece una restricción de dimensionado nueva** (condición b), que debe incorporarse al
   capítulo de dimensionado junto al límite de 5 MW de la modalidad.
5. **La variante 3 pasa a depender de un único nudo.** Es un riesgo de proyecto que hay que
   declarar como tal en la memoria, no esconder.
