---
title: "Guía de modelado en PVsyst — Variante 1 (cubierta del CPD) y protocolo común a las tres variantes"
tipo: guia-operativa
autor: "Generada para Mario Carrión Sirvent"
version_pvsyst: "V8.1.5"
fecha: 2026-09-19
revision: 2
estado: operativa
fuentes:
  - "conocimiento fotovoltaico/Manuales PVsyst/pvsyst-tutorial-v8-1-grid-connected-en.pdf (manual de usuario completo)"
  - "conocimiento fotovoltaico/Referencia/trabajo-previo-modulo6-cpd.md (cifras canónicas del baseline)"
  - "Memoria/analisis/recalculo-superficies-3d-pvsyst.md (geometría y potencias definitivas de V1a, V1b y V2)"
  - "Memoria/analisis/estimacion-preliminar-variantes.md (encuadre estratégico y V3)"
  - "Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv (carga horaria generada el 31/08/2026)"
tags: [PVsyst, guia, variante-1, cubierta, BIPV, autoconsumo, CPD, protocolo]
related: [trabajo-previo-modulo6-cpd, analisis-energetico-sistemas-fv-m6t5, m6-t8-estructuras-soporte-fv]
---

# Guía de modelado en PVsyst — Variante 1

> **Qué es este documento.** El protocolo completo, paso a paso, para levantar en PVsyst V8.1.5
> la **variante 1** (cubierta del CPD: BIPV en tragaluz + cubierta liberada por la geotermia), con
> los valores concretos que hay que teclear en cada casilla y **el criterio de aceptación de cada
> paso**. Los apartados 1 a 4 y 11 a 13 son comunes a las tres variantes: la V2 y la V3 reutilizan
> el mismo proyecto, la misma meteorología y la misma carga, y solo cambian lo que se indica en
> el apartado 14.
>
> **Cómo usarlo.** Está pensado para tenerlo abierto al lado de PVsyst e ir tachando. Cada fase
> termina en un **checkpoint** con un número concreto que tiene que salir. Si no sale, no se pasa
> a la fase siguiente: se depura ahí. Ese es todo el valor del documento — evita descubrir en la
> fase 8 que la meteorología estaba mal importada en la fase 1.

---

## 0. Estado de partida: qué está listo y qué bloquea

**Revisión 2 (19/09/2026).** La geometría de las tres variantes ya no sale de catastro ni del
KMZ: sale del **modelado 3D que Mario ha levantado dentro de PVsyst**, y Mario ha cerrado las
cuatro dudas que quedaban sobre esa medición. Toda la guía está reescrita sobre esas cifras. La
cadena de cálculo completa y reproducible está en `Memoria/analisis/recalculo-superficies-3d-pvsyst.md`
y en `Memoria/analisis/scripts/recalc_superficies_3d.py`.

### 0.1 Las superficies definitivas y de dónde salen

| Variante | Superficie 3D | Qué es exactamente | Potencia de trabajo |
| --- | --- | --- | --- |
| **V1a** lucernario | **578,9109 m²** | Polígono del tragaluz central, **plano horizontal** | **57,89 kWp** |
| **V1b** cubierta | **2.756,8828 m²** | Suma de los polígonos de tejado de las alas de la H, **ya neta de lucernario y de los dos patios** | **338,40 kWp** |
| **V2** marquesinas | **3.536 m²** | Huella de las filas de marquesina del aparcamiento | **716,28 kWp** (127×12) o **710,64 kWp** (126×12) |

**Fuente de la geometría, para declararla en la fase 1.4 de ERMA:** planos de **Catastro a escala
1:1**, trasladados **a mano** al editor de escena 3D de PVsyst. No hay importación de CAD, porque
PVsyst no admite DWG/DXF para el cálculo de sombreados (coherente con lo ya anotado en la memoria
del proyecto sobre importación de terreno). La medición es del **19/09/2026**.

**Cuatro precisiones de Mario que fijan cómo se usan esas cifras** — las cuatro estaban abiertas
en la revisión 1 y las cuatro están cerradas:

1. **El lucernario es horizontal, 0° de inclinación.** No 5° (hipótesis vieja de catastro) ni ~35°
   (hipótesis que la revisión 1 dedujo del cociente 578,9109/472; era casualidad numérica). Al ser
   horizontal, superficie desarrollada y proyección en planta coinciden: **no hay corrección
   angular que aplicar**.
2. **Ninguna de las tres cifras lleva márgenes descontados.** Son la *superficie máxima ideal* que
   se podría llegar a ocupar. Los factores de reducción (0,80 de vidrio activo, 0,70 de
   retranqueos y equipos, 0,82 de empaquetado en sheds, 0,90 de ocupación de marquesina) se
   aplican **desde cero** sobre ellas.
3. **Los dos patios interiores ya están fuera.** Mario midió **polígonos de tejado independientes
   por sección** sobre la planta en H, no un rectángulo envolvente con agujeros, así que el hueco
   entre las patas de la H queda excluido por construcción. En el modelo 3D los dos patios están
   además dibujados como **huecos pasantes**.
4. **El reparto de inversores de la V2 queda abierto a propósito.** Mario prefiere decidir entre
   126 y 127 strings cuando se llegue a esa fase dentro de PVsyst. Aquí se documentan las dos.

> **Una desviación que hay que declarar, no esconder.** V1a + V1b del 3D suman **3.335,8 m²**,
> un **+7,2 %** sobre los 3.111 m² de catastro; y el forjado de cubierta del 3D (2.756,9 m²)
> supera en **+23,6 %** el forjado que se deducía de catastro (2.231 m²). Se adopta la medición 3D
> —es la que va a alimentar la simulación de sombras, y está trazada sobre planos a escala—, pero
> la fase 1.4 de ERMA exige declarar la fuente de cada superficie, así que esa diferencia se
> menciona expresamente en la memoria. Si el tutor pregunta de dónde sale, la respuesta es que
> catastro da superficie construida y el 3D mide polígonos de cubierta trazados sobre el plano.

### 0.2 Insumos

| Insumo | Estado | Dónde está |
| --- | --- | --- |
| Carga horaria del CPD, 8.760 h, formato PVsyst | **Listo** | `Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv` |
| Carga horaria solo no-IT (por si el tutor acota el alcance a HVAC) | **Listo** | `Datos/PVsyst/Entradas/carga_horaria_CPD_noIT_8760.csv` |
| Emplazamiento, meteorología, albedo | **Listo** | Apartado 2 de esta guía |
| Escena 3D del CPD y del aparcamiento (sombras cercanas) | **Listo** | Modelada por Mario el 19/09/2026 |
| Módulo e inversor de la cubierta (V1b) | **Listo** | REC Alpha Pure-RX 470 Wp + familia Huawei SUN2000 KTL-M2 |
| Geometría de las tres variantes | **Listo** | Apartado 0.1 |
| Cadena de pérdidas del trabajo previo | **Listo** | Apartado 8 de esta guía |
| **N.º de entradas DC del SUN2000-100KTL-M2** | **A verificar** | Condiciona el reparto de strings de V1b (apartado 7.1) |
| **Datasheet del vidrio BIPV del tragaluz (V1a)** | **BLOQUEANTE** | Punto abierto n.º 1 del apartado 13 |

> **Consecuencia práctica, y hay que asumirla antes de empezar:** la **V1b (cubierta, 338 kWp)
> se puede simular hoy entera**. La **V1a (BIPV en tragaluz, 58 kWp) no**, porque el vidrio
> fotovoltaico semitransparente **no está en la base de datos de PVsyst** y hay que darlo de alta
> a mano con un datasheet real (Onyx Solar u otro fabricante). Sin ese PDF, cualquier módulo que
> se invente contamina el resultado con una cifra no trazable, que es justo lo que la regla 5 del
> `CLAUDE.md` prohíbe.
>
> **Recomendación:** montar hoy la variante con la orientación de cubierta, y **dejar la segunda
> orientación preparada pero vacía**. Cuando llegue el datasheet, se añade el sub-array del BIPV
> y se vuelve a simular la misma variante: no se pierde nada del trabajo hecho. El apartado 6
> explica cómo dejarlo preparado.
>
> Recuerda además que el BIPV solo aporta un **2,33 %** del consumo: si al final se cae, la V1 pasa
> de 16,56 % a 14,24 % de cobertura. No es lo que decide la variante.

### 0.3 Errata detectada en la captura del proyecto (19/09/2026)

En la pantalla de proyecto que Mario compartió, el proyecto `TFM_DataCenter.PRJ` tiene cargado
`Carrasqueira_MN82.SIT` / `Carrasqueira_MN82_SYN.MET` — **Meteonorm 8.2, Portugal**. Es un
emplazamiento heredado de una plantilla, no el del CPD. **Hay que sustituirlo por el emplazamiento
del apartado 2 antes de simular nada**, o todas las variantes saldrán con la meteorología
equivocada y el checkpoint 1 no pasará. Lo mismo aplica al aviso rojo de esa pantalla («*the
orientation "Fijo, Incl. 10.0°, Azim. -30.0°" is referenced by the sub-array #1, but no 3D field
is attached to this orientation*»): la escena 3D está dibujada, pero todavía **no hay campos FV
asignados** a las orientaciones (`PV Fields (0)`, `Active area 0.00 m²`).

---

## 1. Cómo se organizan los tres proyectos y las variantes

Esto conviene decidirlo **antes** de crear nada, porque en PVsyst las variantes de un mismo
proyecto comparten obligatoriamente emplazamiento, meteorología y carga. Cambiar eso a mitad
obliga a rehacer.

| Proyecto PVsyst | Emplazamiento | Variantes que cuelgan | Por qué van juntas |
| --- | --- | --- | --- |
| **`TFM_CPD_TresCantos`** | CPD (RD Europa 3, Tres Cantos) | `VC0` baseline · `VC1` variante 1 · `VC2` variante 2 | Mismo emplazamiento y mismo consumo. El aparcamiento de la V2 está a 216 m: misma meteorología, mismo TMY. |
| **`TFM_Parcela_TresCantos`** | Parcela de 58,84 ha, a 2,93 km | `VC3` variante 3 (+ BESS) | Es **otro emplazamiento**: otras coordenadas, otro TMY. No puede ser una variante del proyecto anterior. |

**Nomenclatura de variantes** (se teclea en el campo del nombre de la variante, arriba a la derecha):

- `VC0 — Baseline trabajo previo (102 kWp)`
- `VC1 — V1 Cubierta CPD (BIPV + liberada)`
- `VC2 — V2 Marquesinas aparcamiento`
- `VC3 — V3 Planta en suelo + BESS`

> **Por qué existe la VC0.** No es relleno. Es el **patrón de calibración**: se reconstruye el
> sistema del trabajo previo (102 kWp) dentro del proyecto nuevo, y si PVsyst devuelve los
> **166,55 MWh** que ya dio en enero, queda demostrado que el emplazamiento, la meteorología y la
> cadena de pérdidas están bien introducidos. A partir de ahí, todo lo que salga de la VC1, VC2 y
> VC3 es creíble. Sin esa comprobación, un error de importación de meteorología se propagaría a
> las tres variantes sin que nada lo delatase. Es la fase 3 de esta guía y **es obligatoria**.

---

## 2. Fase 1 — Proyecto y emplazamiento

**Ruta:** pantalla principal → `Project design` → `Grid-Connected`.

> El autoconsumo **no es un tipo de proyecto propio** en PVsyst. Se elige `Grid-Connected` y el
> autoconsumo se activa después, dentro de la variante, definiendo el perfil de carga del usuario
> (manual v8-1, §1.1 y §7). Si buscas un botón de «self-consumption» en la pantalla inicial, no
> existe.

### 2.1 Datos del emplazamiento

En `Project` → botón del sitio → `New` (o `Databases` → `Geographical sites`):

| Campo | Valor a introducir | Origen |
| --- | --- | --- |
| Site name | `Tres Cantos CPD` | — |
| Country / Region | España / Comunidad de Madrid | — |
| **Latitud** | **40,5982 °N** | 40° 35′ 53,61″ N (`Coordenadas CPD.png`, WGS84) |
| **Longitud** | **−3,7172 °O** | 3° 43′ 1,81″ O |
| **Altitud** | **741 m** | Trabajo previo §1.1 |
| **Huso horario** | **UTC+1** | — |
| **Albedo** | **0,20** | Trabajo previo §1.1 — valor por defecto de PVsyst para entorno urbano |

### 2.2 Meteorología

**Fuente: PVGIS 5.3, TMY, importada por API.** No es una preferencia estética: es lo que usó el
trabajo previo, y **si se cambia de base de datos, la VC0 no reproducirá los 166,55 MWh** y se
pierde el patrón de calibración y la comparabilidad con el baseline que el tutor ya corrigió.

Ruta: en la ventana del sitio, pestaña de importación → seleccionar `PVGIS` → versión `5.3` →
`TMY` → importar. La clave de API, si la pide, se configura en `Options` → `Preferences`.

El trabajo previo también importó el **horizonte lejano desde la API de PVGIS**: altura media
1,5°, factor difuso 1,00, factor albedo 0,91. Impórtalo igual (`Horizon` dentro de la variante).

> **Checkpoint 1 — meteorología.** Abre la tabla de valores mensuales del fichero meteorológico
> importado y comprueba estas tres cifras anuales:
>
> | Magnitud | Valor que tiene que salir |
> | --- | --- |
> | **GlobHor** (irradiación global horizontal) | **1.785,8 kWh/m²** |
> | **DiffHor** (difusa horizontal) | **558,44 kWh/m²** |
> | **T_Amb** (temperatura media anual) | **14,23 °C** |
>
> Si no cuadran, has importado otra base de datos, otra versión o el TMY de otro punto de la
> malla. **Párate aquí.** Ningún resultado posterior valdrá nada.

---

## 3. Fase 2 — La carga horaria del usuario

Aquí está la mejora más grande respecto al trabajo previo. Aquel introdujo **12 valores
mensuales** de consumo (1.260 MWh de HVAC), y con valores mensuales PVsyst supone la carga
**constante dentro de cada mes**. Para calcular autoconsumo hora a hora eso es tosco. Ahora
tenemos la serie real de 8.760 horas, construida a partir de los 12 ficheros de contador a
resolución de 5 minutos.

**Ruta:** dentro de la variante → `System` → sección de autoconsumo → `User's needs` →
`Load values from a CSV hourly file` → cargar el fichero.

**Fichero a cargar:**

```
Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv
```

**Cómo está construido** (para que puedas defenderlo en la memoria y ante el tutor):

- Origen: los 12 ficheros de `Datos/Consumo CPD/Mensual/`, columna `Pot Gral`, resolución 5 min,
  de **diciembre de 2024 a noviembre de 2025** (año natural completo).
- Filtro de calidad: se descartan los registros con `Pot Gral ≤ 50 kW` o `≥ 800 kW` — huecos de
  telemedida y resets de contador. Se cae el **0,23 %** de los registros.
- Agregación a hora y remapeo a un **año civil de 365 días (2025)**: diciembre se toma de 2024,
  el resto de 2025. **El 99,8 % de las 8.760 horas es dato medido real**; las 14 horas restantes
  se rellenan con el perfil medio mes-hora.
- Reescalado final a la cifra canónica de **3.831,96 MWh/año**.

**Comprobaciones que ya trae hechas el fichero:**

| Magnitud | Valor |
| --- | --- |
| Energía anual | **3.832,0 MWh** |
| Potencia media | **437,4 kW** |
| Potencia mínima / máxima | **360,0 / 499,4 kW** |
| Mes punta / mes valle | julio 344,3 / febrero 291,4 MWh |
| PUE resultante (Gral / IT) | **1,482** |

**Formato del fichero** (manual v8-1, §7): CSV con separador `;`, primera columna la fecha en
`dd/mm/aaaa hh:mm`, segunda columna el valor con **la unidad en la segunda fila** (`kW`), y año
**no bisiesto** — PVsyst da errores de interpretación con años de 366 días. El fichero cumple las
tres condiciones.

> **Si PVsyst no interpreta bien los decimales:** el fichero principal usa **coma decimal**
> (convención española, coherente con el separador `;`). Si al previsualizar la importación ves
> las potencias truncadas o a cero, carga en su lugar
> `carga_horaria_CPD_general_8760_puntodecimal.csv`, que es el mismo fichero con punto decimal.

> **Decisión de alcance que sigue abierta.** El pendiente n.º 3 del análisis preliminar es si el
> TFM se dimensiona contra el **consumo total (3.832 MWh)** o solo contra el **HVAC (1.247 MWh)**,
> como hizo el trabajo previo. Esta guía asume **consumo total**, que es lo coherente con un
> estudio de autoconsumo completo y con el artículo 9 del borrador de RD de centros de datos. Si
> Julio Amador dice lo contrario, **no hay que rehacer nada**: se carga
> `carga_horaria_CPD_noIT_8760.csv` en su lugar y se vuelve a simular. Por eso están generados
> los dos ficheros.

> **Checkpoint 2 — carga.** Tras importar, PVsyst muestra el resumen del perfil. Comprueba:
> **3.832 MWh anuales** y una **potencia media de 437 kW**. Si sale la mitad o el doble, has
> cargado el fichero equivocado o PVsyst ha interpretado kW como kWh.

---

## 4. Fase 3 — VC0: la calibración obligatoria

Reconstruye el sistema del trabajo previo dentro del proyecto nuevo. Es media hora de trabajo y
es lo que da validez a todo lo demás.

> **Atajo si encuentras el `.PRJ` original del Módulo 6 (2026-09-03):** Mario localizó el
> proyecto PVsyst real del trabajo previo. En ese caso no hace falta reconstruir el sistema a
> mano: se duplica ese proyecto, se renombra a `VC0 — Baseline trabajo previo (102 kWp)` y se
> sustituye **solo la carga** (1.260 MWh → `carga_horaria_CPD_general_8760.csv`, 3.832 MWh),
> dejando meteorología, sistema, sombras y pérdidas intactos — son justo lo que el Checkpoint 3
> verifica. Ya se contrastó que su orientación real es `Unlimited sheds` 10°/−30°, coincidente
> con la tabla de abajo.

| Parámetro | Valor |
| --- | --- |
| Orientación | `Unlimited sheds`, inclinación **10°**, azimut **−30°** |
| N.º de sheds | 27 · separación 1,42 m · anchura sensible 1,21 m |
| GCR | **86,3 %** · bandas inactivas 0,02 m arriba y abajo |
| Módulo | **REC Alpha Pure-RX 470 Wp** (`REC470AA Pure-RX` en la base de datos) |
| Configuración | **18 strings × 12 módulos en serie** = 216 módulos = **101,52 kWp** |
| Inversor | Huawei **SUN2000-100KTL-M2** · 1 unidad · 90,0 kWac utilizados |
| Sombras cercanas | `Linear shadings` (modelo lineal) |
| Pérdidas | Las del apartado 8 de esta guía |
| Carga | La de la fase 2 (aquí **sí** cambia respecto al trabajo previo: 3.832 MWh en lugar de 1.260) |

> **Checkpoint 3 — el que decide si sigues o depuras.** Simula la VC0 y mira el informe:
>
> | Magnitud | Valor que tiene que salir | Tolerancia |
> | --- | --- | --- |
> | **E_PV (`Produced Energy`)** | **166,55 MWh** | ± 0,5 % → 165,7–167,4 MWh |
> | **GlobInc** | **1.937,6 kWh/m²** | ± 0,5 % |
> | **PR** | **84,67 %** | ± 0,5 pp |
> | Producción específica | **1.641 kWh/kWp** | ± 0,5 % |
>
> **Ojo, y esto es importante:** el `C_D` (*solar fraction*) **NO** dará el 13,22 % del trabajo
> previo, sino **≈ 4,3 %**. No es un error: es la consecuencia directa de haber cambiado el
> denominador de 1.260 a 3.832 MWh. Es exactamente el hallazgo del apartado 1.1 del análisis
> preliminar, y verlo salir de PVsyst con tus propios ojos es la confirmación independiente de
> que el trabajo previo dimensionaba contra la refrigeración, no contra el consumo total.
>
> Si **E_PV** cuadra pero **C_D** no da ~4,3 %, el problema está en la carga (fase 2).
> Si **E_PV** no cuadra, el problema está en la meteorología (fase 1) o en las pérdidas (fase 8).
> Esa separación de diagnóstico es justo para lo que sirve este checkpoint.

---

## 5. Fase 4 — VC1: crear la variante

Con la VC0 validada, duplícala: `Variant` → `New` a partir de la VC0 (así hereda meteorología,
carga, pérdidas y horizonte sin volver a teclearlos). Renómbrala
`VC1 — V1 Cubierta CPD (BIPV + liberada)`.

**Premisa de proyecto que hay que dejar escrita en la memoria:** la V1b supone que la cubierta
**queda liberada** porque las condensadoras se sustituyen por un sistema geotérmico. Sin esa
sustitución no hay 1.582 m² útiles de cubierta, sino los 450 m² del trabajo previo. La geotermia
no es un adorno de la variante: **es su condición de existencia**, y además reduce el propio
consumo en ~365 MWh/año (9,5 %) y baja el PUE de 1,482 a ~1,341. El cambio de superficie del
recálculo 3D **no toca esta premisa**: mídase como se mida, sin geotermia la cubierta sigue
ocupada.

---

## 6. Fase 5 — VC1: las dos orientaciones

La V1 tiene dos planos distintos, así que la variante necesita **dos orientaciones**. PVsyst V8
lo soporta de forma nativa: en la ventana `Orientation`, el botón **`Add Orientation`** añade
planos, y después **cada sub-array se asocia a una orientación** (manual v8-1, §3 y §4.1).

| # | Orientación | Field type | Inclinación | Azimut | Sub-array asociado |
| --- | --- | --- | --- | --- | --- |
| **1** | Cubierta liberada (V1b) | `Unlimited sheds` | **10°** | **−30°** | REC Alpha Pure-RX, 338,40 kWp |
| **2** | Tragaluz BIPV (V1a) | `Fixed tilted plane` | **0°** | irrelevante (teclea −30° o 0°) | Vidrio FV — **pendiente de datasheet** |

**Parámetros de los sheds de la orientación 1** — se mantienen los del trabajo previo, que ya
están validados por el tutor y por la comprobación de cargas de viento y nieve del CTE:

| Parámetro | Valor |
| --- | --- |
| Inclinación / azimut | 10° / −30° |
| Separación entre sheds | 1,42 m |
| Anchura sensible (*collector width*) | 1,21 m |
| **GCR** | **86,3 %** |
| Bandas inactivas | 0,02 m superior / 0,02 m inferior |
| N.º de sheds | **90 sheds** — el baseline monta 216 módulos en 27 sheds, es decir **8 módulos por shed**; 720 ÷ 8 = 90 exactos. PVsyst ajusta el reparto al confirmar el sistema. |

> **Por qué 10° y no los 35–37° óptimos.** Es la decisión contraintuitiva que ya defendió el
> trabajo previo y que aquí se hereda: con un GCR del 86,3 %, subir la inclinación obliga a
> separar más las filas y **reduce la potencia total instalable en una superficie fija**. La
> pérdida por inclinación (8,62 %) se compensa con creces con los kWp adicionales. En cubierta
> limitada **manda la superficie, no el óptimo angular**. Ese argumento hay que reutilizarlo tal
> cual en la memoria, y **no** aplicarlo a la V3, donde el suelo sobra por un factor 20 y sí se
> va a los 35°.

> **El tragaluz es horizontal: 0°. Cerrado el 19/09/2026 por Mario.** Se acabaron las tres
> hipótesis que circulaban:
>
> - **Los 5° heredados de catastro** eran una suposición del análisis preliminar. No valen.
> - **Los ~35° que dedujo la revisión 1 del recálculo** salían de que 578,9109/472 = 1/cos(35,4°).
>   Era coincidencia aritmética, no geometría.
> - **La sospecha de que fuese a dos aguas o en diente de sierra** queda descartada: es un plano
>   único, horizontal. Una sola orientación `Fixed tilted plane`, no varias.
>
> Consecuencias prácticas, todas favorables a la claridad del capítulo:
>
> 1. **El azimut deja de importar.** A 0° de inclinación el acimut no entra en el cálculo de
>    irradiación. Teclea el que quieras (−30° por coherencia visual con el resto del proyecto);
>    PVsyst lo ignorará.
> 2. **Superficie desarrollada = superficie en planta.** Los 578,9109 m² se usan tal cual, sin
>    corrección por coseno. La pregunta «¿es desarrollada o proyección?» pierde el sentido.
> 3. **La producción específica baja, no sube.** Pasar de la hipótesis de 5°/−30° a horizontal
>    reduce la GlobInc anual de 1.857,7 a **1.785,6 kWh/m²** (−3,9 %) y la productividad de 1.600
>    a **1.540 kWh/kWp**. Un plano horizontal en Madrid pierde frente a cualquier inclinación
>    moderada al sur. Es una pérdida pequeña en términos absolutos (3,4 MWh/año) porque V1a es
>    marginal, pero hay que reportarla con su signo, no maquillarla.
> 4. **La suciedad y las sombras pesan más que en cualquier otro plano del proyecto.** Un
>    acristalamiento horizontal no se autolimpia con la lluvia como uno inclinado, y recibe la
>    sombra de todos los petos, casetones y equipos que lo rodean en la cubierta. La hipótesis de
>    trabajo mantiene **2 % de suciedad y 0,5 % de sombras** por coherencia con el resto de la
>    cadena, pero **el valor bueno sale de la simulación de sombras cercanas sobre la escena 3D,
>    que ya está montada**. El apartado 7.2 trae la sensibilidad completa: entre el caso optimista
>    y un 15 % de sombras con 3 % de suciedad hay 13 MWh, es decir 0,34 pp de C_D.

**Cómo dejar la orientación 2 preparada sin bloquearte:** créala con `Add Orientation`, ponle
**0°** de inclinación, ponle nombre `Tragaluz BIPV` y **no le asocies ningún sub-array todavía**.
PVsyst avisará de que hay una orientación sin módulos; es un aviso, no un error, y puedes simular
igual. Cuando llegue el datasheet, solo hay que dar de alta el módulo y añadir el sub-array.

---

## 7. Fase 6 — VC1: el sistema (módulos, inversores, strings)

### 7.1 Dimensionado de la orientación 1 (cubierta, V1b)

Cadena de cálculo, desde la medición 3D hasta los módulos, para que sea auditable de punta a
punta. **El punto de partida ya no es catastro**: es el polígono de tejado de las alas de la H
medido sobre la escena 3D de PVsyst, que ya excluye el lucernario y los dos patios interiores.

```
Cubierta de las alas de la H (modelo 3D, 19/09/2026)         2.756,8828 m²
  ├─ ya NETA del lucernario (V1a es polígono aparte)
  └─ ya NETA de los dos patios (medición por secciones)
  × 0,70   retranqueos, equipos que permanecen, pasillos
           de mantenimiento, casetones de escalera            1.929,8 m²
  × 0,82   factor de aprovechamiento en sheds a 10°
           (el mismo que validó el trabajo previo)            1.582,5 m²  de módulo
  × 226,7 W/m²  (densidad del REC Alpha Pure-RX)        →       358,74 kWp   ← techo por superficie
```

> **Por qué el 0,70 y el 0,82 se aplican enteros y no a medias.** Mario ha confirmado que los
> 2.756,8828 m² son la *superficie máxima ideal*, sin ningún margen descontado. Ni podía ser de
> otro modo: el 0,70 es un **criterio de ocupación** (retranqueos de seguridad, equipos que se
> quedan, pasillos) y el 0,82 es la **penalización de empaquetado** en filas a 10°; ninguno de los
> dos es geometría que un polígono dibujado sobre el modelo pueda contener. El error a evitar aquí
> —y es el fácil— es leer «2.756,88 m² de cubierta candidata» como si ya fuese superficie neta de
> módulo: daría 512 kWp y sería insostenible ante el tutor, porque implicaría que en la cubierta
> de un CPD en explotación no hay ni retranqueos ni equipos que permanezcan.

**Traducción a módulos y strings:**

| Concepto | Cálculo | Resultado |
| --- | --- | --- |
| Módulos que caben por superficie | 358.740 W ÷ 470 W | 763,3 → **763** |
| Módulos por string | Se hereda del baseline (validado en ventana MPP 200–1000 V) | **12** |
| N.º de strings por superficie | 763 ÷ 12 = 63,6 | **63** (se redondea a la baja) |
| Potencia que cabe en la cubierta | 63 × 12 × 470 W | **355,32 kWp** |
| Superficie que ocuparía | 756 × 2,073 m²/módulo | **1.567,2 m²** ✔ cabe en los 1.582,5 m² |

**Y aquí aparece una restricción nueva que no existía con 287 kWp: las entradas DC del inversor.**

El **Huawei SUN2000-100KTL-M2** tiene **10 MPPT** y una intensidad máxima DC de 30 A por entrada
(cifras del trabajo previo). Con dos strings en paralelo por MPPT —que la corriente admite de
sobra: el informe del baseline da 154 A para 18 strings a 50 °C, es decir **8,6 A por string**—
salen **20 strings como máximo por inversor**. Con 63 strings y 3 inversores tocarían a 21, y no
caben.

| Configuración | Strings | Módulos | kWp | Inversores | Ratio DC/AC | Veredicto |
| --- | --- | --- | --- | --- | --- | --- |
| **3 × 20 strings** | **60** | **720** | **338,40** | **3 × 100 kW** | **1,128** | **la de trabajo** |
| 63 strings en 3 inversores | 63 | 756 | 355,32 | 3 × 100 kW | 1,184 | **21 strings/inversor: no caben** |
| 63 strings en 4 inversores | 63 | 756 | 355,32 | 4 × 100 kW | 0,888 | ratio demasiado bajo, CAPEX peor |
| 63 strings alargando el string | 54 × 14 | 756 | 355,32 | 3 × 100 kW | 1,184 | posible, pero cambia una decisión ya validada por el tutor |

**Se adopta 60 strings × 12 módulos = 720 módulos = 338,40 kWp**, con **3 × SUN2000-100KTL-M2** a
20 strings exactos cada uno. Tres motivos:

1. **Ratio DC/AC = 1,128**, prácticamente idéntico al **1,13** del trabajo previo. El tutor
   corrigió ese trabajo: reencontrarse con su propio número es lo mejor que le puede pasar a esta
   página de la memoria.
2. **No toca la longitud de string de 12 módulos**, que ya está validada en la ventana MPP
   200–1000 V y en las curvas I-V a temperaturas extremas.
3. **Ocupa el 94,3 %** de la superficie neta disponible (1.492,6 m² de los 1.582,5 m²). El 5,7 %
   restante no es superficie desperdiciada por error: es el margen que deja la arquitectura
   eléctrica, y en la memoria se declara como tal.

> **Esto reabre y cierra de otra manera el viejo punto abierto del ratio DC/AC.** En la versión de
> catastro (287,6 kWp, 3 inversores) el ratio salía **0,96** y había que justificar que sobraba
> inversor. Con la superficie real el problema se invierte: **sobra cubierta, no inversor**, y el
> limitante pasa de ser la superficie a ser el número de entradas DC. Es un cambio de criterio
> limitante en el sentido de la fase 2 de ERMA, y merece una frase explícita en la memoria.
>
> **Lo que hay que verificar antes de darlo por bueno:** que el SUN2000-100KTL-M2 admite
> efectivamente **20 entradas DC** (10 MPPT × 2). El trabajo previo montó 18 strings en un solo
> inversor y nunca llegó al límite, así que ese dato **no está en ninguna fuente canónica del
> proyecto todavía**. Pide el datasheet de Huawei y procésalo con `bibliotecario-pdf` antes de
> cerrar el unifilar. Si resultase que admite más de 20 entradas, la configuración buena pasa a
> ser 63 × 12 = 355,32 kWp con ratio 1,184, y hay que rehacer este apartado y el 10.1.

### 7.2 Dimensionado de la orientación 2 (tragaluz, V1a) — bloqueado

| Concepto | Valor |
| --- | --- |
| Superficie del tragaluz (modelo 3D) | **578,9109 m²**, plano horizontal |
| Factor de vidrio activo | 0,80 → **463,1 m²** |
| Densidad supuesta (VLT ≈ 20 %, transparencia media) | **125 Wp/m²** |
| **Potencia** | **57,89 kWp** |
| Inclinación / azimut | **0°** / irrelevante |

**Sensibilidad a la transparencia del vidrio**, que es la variable que de verdad mueve esta
orientación y que decidirá el datasheet:

| Transparencia | Densidad | kWp | E_PV | C_D (3.832 MWh) | C_D (3.467 MWh) |
| --- | --- | --- | --- | --- | --- |
| Alta (VLT > 30 %) | 90 Wp/m² | 41,7 | 64,2 MWh | 1,68 % | 1,85 % |
| **Media (VLT ≈ 20 %)** | **125 Wp/m²** | **57,89** | **89,2 MWh** | **2,33 %** | **2,57 %** |
| Baja (VLT ≈ 10 %) | 160 Wp/m² | 74,1 | 114,1 MWh | 2,98 % | 3,29 % |

**Sensibilidad a sombras y suciedad**, que es lo que hay que afinar con la escena 3D ya montada.
Un acristalamiento horizontal rodeado de petos, casetones y equipos de cubierta no se parece a un
plano despejado:

| Sombras | Suciedad | E_PV | C_D (3.832 MWh) |
| --- | --- | --- | --- |
| **0,5 %** (hipótesis vigente) | **2 %** | **89,2 MWh** | **2,33 %** |
| 5 % | 2 % | 85,4 MWh | 2,23 % |
| 10 % | 3 % | 80,4 MWh | 2,10 % |
| 15 % | 3 % | 76,2 MWh | 1,99 % |

**Qué falta:** el módulo BIPV **no está en la base de datos de PVsyst** y hay que crearlo en
`Databases` → `PV modules` → `New` a partir de un datasheet real. El manual dedicado es
`pvsyst-tutorial-v8-components-database-en.pdf`. Necesitas del fabricante, como mínimo: Pmpp,
Vmpp, Impp, Voc, Isc, coeficientes de temperatura, superficie del vidrio y VLT.

**Acción:** pedir el datasheet de Onyx Solar (o equivalente) y procesarlo con `bibliotecario-pdf`
antes de tocar esta parte. Es el punto abierto n.º 1 del apartado 13.

> **Y no olvides el encuadre.** El BIPV aporta el **2,33 %** del consumo. Su justificación en el
> TFM **no puede ser energética**: es arquitectónica (integración en el lucernario, control solar,
> reducción de la carga térmica que entra por él — que además realimenta al HVAC) y demostrativa.
> Forzar el argumento energético es el error fácil aquí, y ahora hay un motivo más para no
> forzarlo: **al ser horizontal, V1a produce menos** por kWp que cualquier otro plano del proyecto
> (1.540 kWh/kWp frente a 1.612 de la cubierta y 1.639 de las marquesinas).
>
> Aviso térmico que sigue vigente: el modelo aplica la cadena de pérdidas común con
> **Uc = 20 W/m²·K**. Un BIPV integrado **sin ventilación posterior** trabaja más caliente
> (Uc ≈ 15), así que los 89,2 MWh son **cota superior**; cuenta entre un 1,5 y un 2,5 % menos
> cuando el sub-array se modele con su propio parámetro térmico.

---

## 8. Fase 7 — Pérdidas: replicar exactamente el baseline

**Regla que gobierna todo el capítulo de resultados: las tres variantes comparten la misma
cadena de pérdidas.** Si la V1 lleva unas hipótesis y la V2 otras, la comparación entre variantes
—que es el núcleo del TFM— deja de ser válida. Se copian del trabajo previo, sin tocar nada:

| Concepto | Dónde se introduce en PVsyst | Valor |
| --- | --- | --- |
| Modelo térmico | `Thermal parameter` | **Uc = 20,0 W/m²·K · Uv = 0,0 W/m²·K·m/s** |
| Cableado DC | `Ohmic losses` | Resistencia global tal que dé **1,5 % en STC** (→ ~1,0 % anual real) |
| Calidad de módulo | `Module quality loss` | **−0,53 %** (es una **ganancia** de +0,5 %, no una pérdida) |
| Mismatch módulos / strings | `Module mismatch` | **2,00 % en MPP / 0,05 %** |
| Suciedad | `Soiling loss` | **1,0 %** anual |
| IAM | `IAM losses` → perfil definido por el usuario | Tabla de abajo |
| Indisponibilidad | `Unavailability` | **0,5 % del tiempo** (1,8 días, 3 periodos) |
| LID / PID | — | **0,0 %** (el REC Alpha Pure-RX es 0 % LID y anti-PID) |

**Perfil IAM a introducir punto por punto:**

| 0° | 30° | 45° | 60° | 70° | 75° | 80° | 85° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,000 | 1,000 | 1,000 | 0,974 | 0,907 | 0,832 | 0,688 | 0,445 | 0,000 |

**Sombras cercanas:** `Linear shadings` (modelo lineal), igual que el baseline. Con `Unlimited
sheds` PVsyst calcula el sombreado mutuo entre filas de forma analítica y **no hace falta
construir la escena 3D**. El factor 0,70 aplicado a la cubierta ya descuenta los equipos que
permanecen y los retranqueos, así que modelarlos otra vez en 3D los contaría dos veces.

> **Cuándo sí habría que montar la escena 3D:** si el tutor pide justificar el sombreado de los
> casetones de escalera y de las condensadoras que se mantengan, o si al final la geotermia no
> libera toda la cubierta y quedan obstáculos dispersos. Es varias horas de trabajo. **No lo
> hagas ahora**: documenta la hipótesis del 0,70 y déjalo como posible refinamiento.

---

## 9. Fase 8 — Autoconsumo y antivertido

La V1 es **autoconsumo sin excedentes**, en la modalidad de **red interior** del artículo 3.g).i)
del RD 244/2019 — misma referencia catastral, mismo edificio, **exenta de permisos de acceso y
conexión** por el artículo 7.1.b).i). Físicamente nunca vierte: 338 kWp contra una carga plana de
437 kW dan **0 MWh de excedente y 0 horas de vertido**.

En PVsyst hay que reflejarlo. Dos vías, equivalentes en el resultado:

1. En la sección de autoconsumo del `System`, marcar que **no se permite la inyección a red**
   (es lo que el informe del trabajo previo reporta como `no grid reinjection`).
2. Si esa casilla no aparece en tu versión: `Grid Power limitation` (manual v8-1, §6.3), límite
   **0 kW aplicado en el punto de inyección** (`at the injection point level`, no `at the inverter
   level`), y marcar `Account as separate loss` para que el recorte aparezca desglosado como
   `EUnused` en el diagrama de pérdidas.

> **Checkpoint 4 — antivertido.** En el informe, **`EUnused` tiene que salir ≈ 0 MWh**. En el
> baseline salió −0,01 MWh. Si sale un valor apreciable, significa que el campo está superando la
> carga en algunas horas y el antivertido está recortando producción real — algo que en la V1 no
> debería ocurrir nunca. Si ocurre, revisa que la carga se haya importado bien (checkpoint 2).

---

## 10. Fase 9 — Simular y validar el resultado

### 10.1 Banda de aceptación de la VC1

El análisis preliminar predice estos valores. **Si PVsyst cae dentro de la banda, la variante
está bien montada**; si se sale, hay algo mal en el sistema o en las pérdidas:

| Magnitud | Predicción del análisis | Banda de aceptación (± 3 %) |
| --- | --- | --- |
| **E_PV** solo cubierta (V1b, **338,40 kWp** reales) | **545,6 MWh** | 529–562 MWh |
| **E_PV** total V1 (338,40 + 57,89 = **396,3 kWp**) | **634,8 MWh** | 616–654 MWh |
| **Producción específica** V1b | **1.612 kWh/kWp** | 1.560–1.660 kWh/kWp |
| **Producción específica** V1a (plano horizontal) | **1.540 kWh/kWp** | 1.490–1.590 kWh/kWp |
| **PR** | ~84 % | 82–86 % |
| **A_PV** (autoconsumo) | **100 %** | exacto |
| **C_D** solo cubierta | **14,24 %** | 13,8–14,7 % |
| **C_D** total V1 | **16,56 %** | 16,1–17,1 % |
| **Excedentes** | **0 MWh** | ≈ 0 |
| Pico de generación de la V1 | **286 kW** | contra 437 kW de carga media: nunca vierte |

> **Cuidado con dos cifras que se parecen y no son la misma.** La cubierta admite por superficie
> **355,32 kWp** (63 × 12), pero el sistema que se monta son **338,40 kWp** (60 × 12) porque los
> strings se reparten entre tres inversores de 20 entradas. Si tecleas 63 strings, PVsyst simulará
> **572,9 MWh** y **14,95 %** de C_D, y la banda de arriba no cuadrará: no es un error de la guía,
> es que has montado otro sistema. La tabla del apartado 7.1 explica por qué se elige el de 60.

> La producción específica de la V1b (1.612 kWh/kWp) sale ligeramente **por debajo** de la del
> baseline (1.641 kWh/kWp) y eso es correcto, no un fallo: el modelo del análisis preliminar corre
> sistemáticamente un ~1,3 % bajo respecto a PVsyst. Espera que **PVsyst dé un poco más** que la
> predicción — si da 1.630–1.650 kWh/kWp, perfecto. La de la V1a es más baja (1.540) por la razón
> física de que el plano es **horizontal**, y ahí sí debe salir más baja también en PVsyst.

### 10.2 Dónde leer los 9 parámetros de la tabla ERMA

La guía metodológica del Módulo 6 pide una tabla de 9 parámetros. Este es el mapeo exacto contra
el informe de PVsyst, **verificado** reproduciendo las cifras del baseline:

| Parámetro ERMA | Símbolo | De dónde sale en el informe PVsyst | Comprobación con el baseline |
| --- | --- | --- | --- |
| Irradiación global sobre el generador | Y_R | `GlobInc` (kWh/m²) | 1.937,60 |
| Índice de productividad del generador | Y_A | `EArray` ÷ Pnom(STC) | 169,43 MWh ÷ 101,52 kWp = **1.668,7** ✔ |
| Índice de productividad final | Y_F | `E_Solar` ÷ Pnom(STC) | 166,55 ÷ 101,52 = **1.640,6** ✔ |
| Rendimiento (*Performance Ratio*) | PR | Y_F ÷ Y_R (PVsyst lo da directo) | 1.640,98 ÷ 1.937,60 = **84,69 %** ✔ |
| Energía total producida | E_PV | `Produced Energy` | 166,55 MWh |
| Autoconsumo | A_PV | `E_Solar` ÷ `E_PV` × 100 | 100 % |
| Autosuficiencia sin balance neto | C_D | `Solar Fraction` = `E_Solar` ÷ `E_User` × 100 | 13,22 % (baseline) |
| Autosuficiencia con balance neto | C_D,NM | Igual a C_D cuando no hay vertido | 13,22 % |
| Dependencia de la red | D_G | `EFrGrid` ÷ `E_User` × 100 = 100 − C_D | 86,78 % |

> **Ojo con Pnom(STC).** Es la potencia real instalada (720 × 470 = **338,40 kWp**), no el techo
> por superficie de 358,74 ni el de strings de 355,32. En el baseline eran 101,52 kWp, no 102 — y
> con 102 las cuentas de arriba no cuadran. Este detalle es la causa más habitual de que un PR
> salga «raro» por unas décimas.

### 10.3 Qué exportar y dónde guardarlo

| Qué | Cómo | Dónde |
| --- | --- | --- |
| Informe completo | `Report` → exportar PDF | `Datos/PVsyst/VC1_V1_Cubierta_Report.pdf` |
| Resultados horarios | `Hourly results` → CSV (marcar `E_Solar`, `E_User`, `EFrGrid`, `EArray`, `GlobInc`) | `Datos/PVsyst/VC1_V1_Cubierta_horario.csv` |
| Captura de la pantalla de sistema | — | `conocimiento fotovoltaico/Capturas/AAAA-MM-DD_HHMM.png` |

> **El CSV horario no es opcional.** Es la entrada del modelo económico en Excel (VAN, TIR, LCOE)
> y del modelo de gestión de batería del capítulo 7. Expórtalo siempre, aunque la variante no
> lleve batería: para la V1 sirve para demostrar en la memoria, hora a hora, que el excedente es
> cero y que por tanto **la batería no está justificada en esta variante** — que es una conclusión
> del TFM, no una omisión.

---

## 11. Errata heredada que no hay que arrastrar

Del trabajo previo, ya detectadas. Al trasladar cifras a la memoria:

| Dice | Debe decir |
| --- | --- |
| E_PV = 165,55 MWh (diapositiva 23) | **166,55 MWh** (el informe PVsyst es consistente en 3 páginas) |
| Huawei SUN2000-100**TKL**-M2 | Huawei SUN2000-100**KTL**-M2-400Vac |
| Tolerancia de potencia «0,53 % de pérdida» | Es **ganancia de +0,5 %** (*loss fraction* −0,53 %) |

---

## 12. Qué cambia para la V2 y la V3

El proceso es el mismo. Solo cambian estos parámetros:

| Paso | V1 (cubierta) | V2 (marquesinas) | V3 (planta en suelo) |
| --- | --- | --- | --- |
| Proyecto | `TFM_CPD_TresCantos` | **El mismo** | **Otro**: `TFM_Parcela_TresCantos` |
| Emplazamiento | CPD | El mismo (216 m) | Parcela a 2,93 km — coordenadas propias y **TMY propio** |
| Orientaciones | 2 (**10°/−30°** y **0° horizontal**) | 1 · **8° / −30°** | 1 · **30–35° / 0° (sur)** |
| Field type | `Unlimited sheds` + `Fixed tilted plane` | `Unlimited sheds` | `Unlimited sheds` (o seguidor, si se estudia) |
| Superficie / potencia | 2.756,88 + 578,91 m² → **396,3 kWp** | **3.536 m² → 716,28 kWp** (127×12) | 1,32 ha/MWp → **2,00–2,50 MWp** |
| Módulos / strings | 720 (60×12) + BIPV | **1.524 (127×12)** o **1.512 (126×12)** — ver abajo | por decidir |
| Inversores | 3 × 100 kW · DC/AC **1,128** | **7 × 100 kW** · DC/AC **1,023** o **1,015** | por decidir |
| Carga | La misma | La misma | La misma |
| Autoconsumo | Sin excedentes, red interior | Sin excedentes + antivertido | **Con excedentes, obligatoriamente** (art. 4.5.c) |
| Antivertido en PVsyst | Límite 0 kW | Límite 0 kW | **Sin límite** — el vertido es legal y hay que cuantificarlo |
| Batería | **No** (0 pp de ganancia) | **No** (0,36 pp) | **Sí, decisiva**: 4–6 MWh, estrategia `Increased Self-consumption` |
| C_D esperado | **16,56 %** | **30,20 %** (127) / **30,01 %** (126) | 43–44 % sin batería · 80–90 % con ella |

> **El reparto de strings de la V2 está deliberadamente sin cerrar.** Mario lo dejó abierto el
> 19/09/2026: «*eso ahora no tiene mucho sentido responderlo, conforme avancemos en PVsyst
> veremos*». Las dos opciones son viables y las dos están calculadas; **no se fija ninguna como
> definitiva hasta esa fase**:
>
> | | **127 strings** | **126 strings** |
> | --- | --- | --- |
> | Módulos | 1.524 | 1.512 |
> | Potencia | **716,28 kWp** | **710,64 kWp** |
> | Superficie de módulo | 3.159,3 m² ✔ (de 3.182,4 disponibles) | 3.134,4 m² ✔ |
> | Inversores | 7, reparto **no uniforme** (127 es primo: 18+18+18+18+18+18+19) | 7 × 18 exactos |
> | Ratio DC/AC | 1,023 | 1,015 |
> | E_PV | 1.173,7 MWh | 1.164,5 MWh |
> | C_D | 30,20 % | 30,01 % |
> | Excedentes recortados | 16,5 MWh en 559 h | 14,4 MWh en 520 h |
>
> A favor de 127: aprovecha 5,6 kWp más de una superficie que ya está pagada. A favor de 126: el
> unifilar y la tabla de la fase 6 de ERMA quedan simétricos, y el ratio coincide con el criterio
> del resto del proyecto. La diferencia energética es de **0,19 puntos de C_D**, así que la
> decisión es de claridad documental, no de ingeniería.

> **V2 ya no es «excedente testimonial», y eso hay que escribirlo.** Con 3.536 m² el pico de
> generación sube a **529 kW**, por encima de los 437 kW de carga media del CPD, y el antivertido
> recorta **16,5 MWh en 559 horas** al año (**49,5 MWh en 957 horas** si entra la geotermia, un
> 4,2 % de la producción). No se exportan: se pierden. La conclusión de fondo no cambia —un pack
> de 0,16–0,38 MWh para recuperar eso no lo paga nadie, así que **la batería sigue sin
> justificarse en V2**—, pero ya no se puede afirmar que la variante nunca vierte. Es un dato del
> capítulo de resultados y sostiene el argumento correcto: **V2 está justo en el límite de lo que
> el CPD puede absorber**, y cualquier ampliación por encima de esa huella exige almacenamiento o
> cambiar de modalidad.

> **Los dos avisos que más tiempo te van a ahorrar en la V3:**
>
> 1. **La V3 va en otro proyecto.** Si intentas meterla como variante del proyecto del CPD,
>    heredará el emplazamiento del CPD y estarás simulando la planta en la ubicación equivocada.
> 2. **La batería de la V3 no es la del mercado estándar.** El modelo pide **471 kW de descarga
>    con 4–6 MWh** de capacidad: eso son **0,08–0,12 C** y 9–13 h de autonomía. Es una batería de
>    **energía**, no de potencia. Al elegirla en PVsyst, comprueba que la potencia de descarga
>    configurada llega a los 471 kW y que el C-rate del pack de la base de datos lo admite. Y
>    recuerda la decisión ya tomada: **la batería no carga de red**, solo de excedente FV — que es
>    justo lo que hace la estrategia `Increased Self-consumption` del manual (§8.2: «*the battery
>    never feeds the grid, it only starts charging when PV production exceeds the instantaneous
>    demand*»).

---

## 13. Puntos abiertos que condicionan esta guía

| # | Asunto | Qué bloquea | Quién lo cierra |
| --- | --- | --- | --- |
| 1 | **Datasheet del vidrio BIPV** | La orientación 2 de la V1 (57,89 kWp, 2,33 % del consumo) | Mario → `bibliotecario-pdf` |
| 2 | **Alcance: consumo total o solo HVAC** | El denominador de todos los C_D. Los dos ficheros de carga ya están generados | Julio Amador |
| 3 | **N.º de entradas DC del SUN2000-100KTL-M2** | Si son 20, V1b = 338,40 kWp (DC/AC 1,128); si admite más, 355,32 kWp (1,184). Afecta al apartado 7.1, al 10.1 y al CAPEX del capítulo 8 | Datasheet de Huawei → `bibliotecario-pdf` |
| 4 | **Reparto de strings de la V2: 126 o 127** | El unifilar de la V2 y la tabla de la fase 6 de ERMA. **Diferido expresamente por Mario** al momento de montarlo en PVsyst | Mario, en la fase de sistema de la VC2 |
| 5 | Capacidad de acceso de generación en los nudos próximos a la parcela | La **viabilidad entera de la V3**, no su simulación | Mapa de capacidad de i-DE |
| 6 | Sombreado real sobre el lucernario horizontal | Entre 0,5 % y 15 % de sombras hay 13 MWh y 0,34 pp de C_D en la V1a | Simulación de sombras cercanas sobre la escena 3D ya montada |

**Puntos que la revisión 2 cierra y que ya no hay que arrastrar:**

| Cerrado | Cómo quedó |
| --- | --- |
| Pendiente del tragaluz | **0°, horizontal.** Plano único, no faldones. Confirmado por Mario el 19/09/2026 |
| ¿Superficie desarrollada o proyección? | Deja de aplicar: al ser horizontal, coinciden |
| ¿Los 2.756,88 m² descuentan los patios? | **Sí.** Medición por polígonos de sección sobre la planta en H |
| ¿Las superficies traen márgenes aplicados? | **No.** Son la superficie máxima ideal; los factores se aplican desde cero |
| Fuente de la geometría | Catastro 1:1 trazado a mano en el editor 3D de PVsyst |
| Ratio DC/AC de 0,96 de la V1b | Desaparece: con la superficie real el limitante deja de ser la cubierta y pasa a ser la entrada DC del inversor |

> El punto 5 no afecta a lo que hay que teclear en PVsyst, pero conviene tenerlo presente: la V3
> se puede simular perfectamente y dar un resultado excelente, y aun así ser inviable si no hay
> capacidad de acceso en el nudo. Es el riesgo crítico abierto del proyecto.

---

## 14. Resumen: el orden de trabajo de hoy

0. **Corregir el emplazamiento del proyecto**: quitar `Carrasqueira_MN82` (Portugal) — ver 0.3.
1. Crear el proyecto `TFM_CPD_TresCantos` con el emplazamiento del apartado 2. → **Checkpoint 1**
2. Importar PVGIS 5.3 TMY y el horizonte. → **Checkpoint 1**
3. Importar la carga horaria `carga_horaria_CPD_general_8760.csv`. → **Checkpoint 2**
4. Montar la **VC0** (102 kWp del trabajo previo) y simular. → **Checkpoint 3** ← *el que decide*
5. Duplicar a **VC1**, añadir las dos orientaciones: cubierta **10°/−30°** y tragaluz **0°**
   (esta última vacía de momento, a la espera del datasheet BIPV).
6. Dimensionar la cubierta: **720 módulos, 60 strings × 12, 3 inversores**, 90 sheds.
7. Asignar los campos FV de la escena 3D a las orientaciones (ahora mismo hay `PV Fields (0)`).
8. Verificar que las pérdidas y el IAM se han heredado intactos de la VC0.
9. Antivertido a 0 kW en el punto de inyección. → **Checkpoint 4**
10. Simular, contrastar contra la banda del apartado 10.1 (**545,6 MWh**, **C_D 14,24 %** sin el
    BIPV), exportar PDF + CSV horario.
11. Anotar en la memoria el resultado y las hipótesis marcadas en esta guía.

Con esto la V1 queda cerrada salvo el BIPV. La V2 son los pasos 5 a 10 otra vez con los parámetros
de la columna correspondiente del apartado 12 —decidiendo allí si van 126 o 127 strings— y no
debería llevar más de una tarde.
