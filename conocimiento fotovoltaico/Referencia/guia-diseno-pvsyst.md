---
title: "Guía de modelado en PVsyst — Variante 1 (cubierta del CPD) y protocolo común a las tres variantes"
tipo: guia-operativa
autor: "Generada para Mario Carrión Sirvent"
version_pvsyst: "V8.1.5"
fecha: 2026-08-31
estado: operativa
fuentes:
  - "conocimiento fotovoltaico/Manuales PVsyst/pvsyst-tutorial-v8-1-grid-connected-en.pdf (manual de usuario completo)"
  - "conocimiento fotovoltaico/Referencia/trabajo-previo-modulo6-cpd.md (cifras canónicas del baseline)"
  - "Memoria/analisis/estimacion-preliminar-variantes.md (geometría y potencias de las tres variantes)"
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

| Insumo | Estado | Dónde está |
| --- | --- | --- |
| Carga horaria del CPD, 8.760 h, formato PVsyst | **Listo** | `Datos/PVsyst/Entradas/carga_horaria_CPD_general_8760.csv` |
| Carga horaria solo no-IT (por si el tutor acota el alcance a HVAC) | **Listo** | `Datos/PVsyst/Entradas/carga_horaria_CPD_noIT_8760.csv` |
| Emplazamiento, meteorología, albedo | **Listo** | Apartado 2 de esta guía |
| Módulo e inversor de la cubierta (V1b) | **Listo** | REC Alpha Pure-RX 470 Wp + familia Huawei SUN2000 KTL-M2 |
| Geometría de la cubierta (superficies y descuentos) | **Listo** | 1.562 m² útiles → 290 kWp |
| Cadena de pérdidas del trabajo previo | **Listo** | Apartado 8 de esta guía |
| **Datasheet del vidrio BIPV del tragaluz (V1a)** | **BLOQUEANTE** | Pendiente n.º 5 del análisis preliminar |

> **Consecuencia práctica, y hay que asumirla antes de empezar:** la **V1b (cubierta, 290 kWp)
> se puede simular hoy entera**. La **V1a (BIPV en tragaluz, 47 kWp) no**, porque el vidrio
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
> Recuerda además que el BIPV solo aporta un **2,0 %** del consumo: si al final se cae, la V1 pasa
> de 14,2 % a 12,2 % de cobertura. No es lo que decide la variante.

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
sustitución no hay 1.562 m² disponibles, sino los 450 m² del trabajo previo. La geotermia no es
un adorno de la variante: **es su condición de existencia**, y además reduce el propio consumo en
~365 MWh/año (9,5 %) y baja el PUE de 1,482 a ~1,341.

---

## 6. Fase 5 — VC1: las dos orientaciones

La V1 tiene dos planos distintos, así que la variante necesita **dos orientaciones**. PVsyst V8
lo soporta de forma nativa: en la ventana `Orientation`, el botón **`Add Orientation`** añade
planos, y después **cada sub-array se asocia a una orientación** (manual v8-1, §3 y §4.1).

| # | Orientación | Field type | Inclinación | Azimut | Sub-array asociado |
| --- | --- | --- | --- | --- | --- |
| **1** | Cubierta liberada (V1b) | `Unlimited sheds` | **10°** | **−30°** | REC Alpha Pure-RX, 290 kWp |
| **2** | Tragaluz BIPV (V1a) | `Fixed tilted plane` | **5°** | **−30°** | Vidrio FV — **pendiente de datasheet** |

**Parámetros de los sheds de la orientación 1** — se mantienen los del trabajo previo, que ya
están validados por el tutor y por la comprobación de cargas de viento y nieve del CTE:

| Parámetro | Valor |
| --- | --- |
| Inclinación / azimut | 10° / −30° |
| Separación entre sheds | 1,42 m |
| Anchura sensible (*collector width*) | 1,21 m |
| **GCR** | **86,3 %** |
| Bandas inactivas | 0,02 m superior / 0,02 m inferior |
| N.º de sheds | **76–77 sheds** — el baseline monta 216 módulos en 27 sheds, es decir **8 módulos por shed**; 612 ÷ 8 = 76,5. PVsyst ajusta el reparto al confirmar el sistema. |

> **Por qué 10° y no los 35–37° óptimos.** Es la decisión contraintuitiva que ya defendió el
> trabajo previo y que aquí se hereda: con un GCR del 86,3 %, subir la inclinación obliga a
> separar más las filas y **reduce la potencia total instalable en una superficie fija**. La
> pérdida por inclinación (8,62 %) se compensa con creces con los kWp adicionales. En cubierta
> limitada **manda la superficie, no el óptimo angular**. Ese argumento hay que reutilizarlo tal
> cual en la memoria, y **no** aplicarlo a la V3, donde el suelo sobra por un factor 20 y sí se
> va a los 35°.

> **Los 5° del tragaluz son una hipótesis, no un dato medido.** Es la pendiente que se supuso en
> el análisis preliminar. Cuando tengas el detalle constructivo del lucernario (o una foto de
> perfil acotada), corrígela. A 47 kWp, el impacto en el resultado global de la V1 es de décimas.

**Cómo dejar la orientación 2 preparada sin bloquearte:** créala con `Add Orientation`, ponle
5° / −30°, ponle nombre `Tragaluz BIPV` y **no le asocies ningún sub-array todavía**. PVsyst
avisará de que hay una orientación sin módulos; es un aviso, no un error, y puedes simular igual.
Cuando llegue el datasheet, solo hay que dar de alta el módulo y añadir el sub-array.

---

## 7. Fase 6 — VC1: el sistema (módulos, inversores, strings)

### 7.1 Dimensionado de la orientación 1 (cubierta, V1b)

Cadena de cálculo, desde catastro hasta módulos, para que sea auditable de punta a punta:

```
Cubierta total (catastro)                                   3.111 m²
  − tragaluz                                                −  472 m²
  − patios interiores (medidos en píxeles sobre PlantaCPD)  −  408 m²
  = forjado de cubierta                                      2.231 m²
  × 0,70   retranqueos, equipos que permanecen, pasillos,
           casetones de escalera                             1.561,7 m²  disponibles
  × 0,82   factor de aprovechamiento en sheds a 10°
           (el mismo que validó el trabajo previo)           1.280,6 m²  de módulo
  × 226,7 W/m²  (densidad del REC Alpha Pure-RX)        →      290,3 kWp
```

**Traducción a módulos y strings:**

| Concepto | Cálculo | Resultado |
| --- | --- | --- |
| Módulos que caben | 290.300 W ÷ 470 W | 617,7 → **617** |
| Módulos por string | Se hereda del baseline (validado en ventana MPP 200–1000 V) | **12** |
| N.º de strings | 617 ÷ 12 = 51,4 | **51** (se redondea a la baja, criterio conservador) |
| **Módulos totales** | 51 × 12 | **612** |
| **Potencia instalada** | 612 × 470 W | **287,6 kWp** |
| Superficie ocupada | 612 × 2,073 m²/módulo | **1.269 m²** ✔ cabe en los 1.280,6 m² |

**Inversores.** Con 3 unidades de **Huawei SUN2000-100KTL-M2** (100 kWac) el reparto es limpio:
**17 strings por inversor** (3 × 17 = 51). Ratio DC/AC = 287,6 / 300 = **0,96**.

> **Ese 0,96 es bajo frente al 1,13 del trabajo previo, y hay que justificarlo o corregirlo.**
> El argumento a favor de mantenerlo: aquí **no hay excedentes** — cada kWh producido desplaza
> una compra de red a precio de tarifa 6.1TD, y la carga plana de 437 kW absorbe todo lo que el
> campo pueda dar (pico DC estimado ~240 kW). Recortar por inversor **sí tendría coste real**, a
> diferencia de una planta de venta. Un DC/AC próximo a 1,0 es defendible en autoconsumo sin
> excedentes.
> El argumento en contra: tres inversores de 100 kW para 288 kWp encarecen el CAPEX sin producir
> más, y eso pesa en el capítulo 8.
> **Esto es una decisión de ingeniería, no de manejo del programa.** Antes de cerrarla, pásala
> por `ingeniero-dominio` con el datasheet real en la mano y comprueba en el informe que la
> pérdida `Inverter loss over nominal power` sale **< 0,5 %** — si sale ~0,0 % con 3 inversores,
> es señal de que sobra inversor. Usa el `Pre-sizing help` de la esquina superior derecha de la
> ventana `System` para contrastar alternativas rápido.

### 7.2 Dimensionado de la orientación 2 (tragaluz, V1a) — bloqueado

| Concepto | Valor |
| --- | --- |
| Superficie del tragaluz (catastro) | 472 m² |
| Factor de vidrio activo | 0,80 → **377,6 m²** |
| Densidad supuesta (VLT ≈ 20 %, transparencia media) | **125 Wp/m²** |
| **Potencia** | **47,2 kWp** |

**Qué falta:** el módulo BIPV **no está en la base de datos de PVsyst** y hay que crearlo en
`Databases` → `PV modules` → `New` a partir de un datasheet real. El manual dedicado es
`pvsyst-tutorial-v8-components-database-en.pdf`. Necesitas del fabricante, como mínimo: Pmpp,
Vmpp, Impp, Voc, Isc, coeficientes de temperatura, superficie del vidrio y VLT.

**Acción:** pedir el datasheet de Onyx Solar (o equivalente) y procesarlo con `bibliotecario-pdf`
antes de tocar esta parte. Es el pendiente n.º 5 del análisis preliminar.

> **Y no olvides el encuadre.** El BIPV aporta el **2,0 %** del consumo. Su justificación en el
> TFM **no puede ser energética**: es arquitectónica (integración en el lucernario, control solar,
> reducción de la carga térmica que entra por él — que además realimenta al HVAC) y demostrativa.
> Forzar el argumento energético es el error fácil aquí.

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
| **E_PV** solo cubierta (V1b, **287,6 kWp** reales) | **464 MWh** | 450–478 MWh |
| **E_PV** total V1 (287,6 + 47,2 = **334,8 kWp**) | **540 MWh** | 524–556 MWh |
| **Producción específica** | **1.612 kWh/kWp** | 1.560–1.660 kWh/kWp |
| **PR** | ~84 % | 82–86 % |
| **A_PV** (autoconsumo) | **100 %** | exacto |
| **C_D** solo cubierta | **12,1 %** | 11,7–12,5 % |
| **C_D** total V1 | **14,1 %** | 13,7–14,5 % |
| **Excedentes** | **0 MWh** | ≈ 0 |

> **Por qué 464 MWh y no los 468 del análisis preliminar.** El análisis calculó sobre los
> **290,3 kWp** que caben en la superficie; el sistema real monta **287,6 kWp** porque los strings
> se redondean a la baja (51 × 12 en lugar de 51,4). Es la misma cifra escalada, no una
> discrepancia. Lo mismo vale para los 540 MWh de la V1 completa frente a los 544 del análisis.

> La producción específica de la V1 (1.612 kWh/kWp) sale ligeramente **por debajo** de la del
> baseline (1.641 kWh/kWp) y eso es correcto, no un fallo: el modelo del análisis preliminar
> corre sistemáticamente un ~1,3 % bajo respecto a PVsyst. Espera que **PVsyst dé un poco más**
> que la predicción — si da 1.630–1.650 kWh/kWp, perfecto.

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

> **Ojo con Pnom(STC).** Es la potencia real instalada (612 × 470 = **287,64 kWp**), no la
> redondeada de 290. En el baseline eran 101,52 kWp, no 102 — y con 102 las cuentas de arriba no
> cuadran. Este detalle es la causa más habitual de que un PR salga «raro» por unas décimas.

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
| Orientaciones | 2 (10°/−30° y 5°/−30°) | 1 · **8° / −30°** | 1 · **30–35° / 0° (sur)** |
| Field type | `Unlimited sheds` | `Unlimited sheds` | `Unlimited sheds` (o seguidor, si se estudia) |
| Superficie / potencia | 1.562 m² → **288 kWp** | 3.332 m² → **680 kWp** | 1,32 ha/MWp → **2,00–2,50 MWp** |
| Carga | La misma | La misma | La misma |
| Autoconsumo | Sin excedentes, red interior | Sin excedentes + antivertido | **Con excedentes, obligatoriamente** (art. 4.5.c) |
| Antivertido en PVsyst | Límite 0 kW | Límite 0 kW | **Sin límite** — el vertido es legal y hay que cuantificarlo |
| Batería | **No** (0 pp de ganancia) | **No** (0,2 pp) | **Sí, decisiva**: 4–6 MWh, estrategia `Increased Self-consumption` |
| C_D esperado | 14,2 % | 28,9 % | 43–44 % sin batería · 80–90 % con ella |

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
| 1 | **Datasheet del vidrio BIPV** | La orientación 2 de la V1 (47 kWp, 2 % del consumo) | Mario → `bibliotecario-pdf` |
| 2 | **Alcance: consumo total o solo HVAC** | El denominador de todos los C_D. Los dos ficheros de carga ya están generados | Julio Amador |
| 3 | Modelo de inversor definitivo de la V1b | El ratio DC/AC (0,96 con 3×100 kW) y el CAPEX del capítulo 8 | `ingeniero-dominio` + datasheet |
| 4 | Pendiente real del tragaluz (se supone 5°) | Décimas en la V1 | Detalle constructivo o foto acotada |
| 5 | Capacidad de acceso de generación en los nudos próximos a la parcela | La **viabilidad entera de la V3**, no su simulación | Mapa de capacidad de i-DE |

> El punto 5 no afecta a lo que hay que teclear en PVsyst, pero conviene tenerlo presente: la V3
> se puede simular perfectamente y dar un resultado excelente, y aun así ser inviable si no hay
> capacidad de acceso en el nudo. Es el riesgo crítico abierto del proyecto.

---

## 14. Resumen: el orden de trabajo de hoy

1. Crear el proyecto `TFM_CPD_TresCantos` con el emplazamiento del apartado 2. → **Checkpoint 1**
2. Importar PVGIS 5.3 TMY y el horizonte. → **Checkpoint 1**
3. Importar la carga horaria `carga_horaria_CPD_general_8760.csv`. → **Checkpoint 2**
4. Montar la **VC0** (102 kWp del trabajo previo) y simular. → **Checkpoint 3** ← *el que decide*
5. Duplicar a **VC1**, añadir las dos orientaciones (la del BIPV vacía de momento).
6. Dimensionar la cubierta: 612 módulos, 51 strings × 12, 3 inversores.
7. Verificar que las pérdidas y el IAM se han heredado intactos de la VC0.
8. Antivertido a 0 kW en el punto de inyección. → **Checkpoint 4**
9. Simular, contrastar contra la banda del apartado 10.1, exportar PDF + CSV horario.
10. Anotar en la memoria el resultado y las hipótesis marcadas en esta guía.

Con esto la V1 queda cerrada salvo el BIPV. La V2 son los pasos 5 a 9 otra vez con los parámetros
de la columna correspondiente del apartado 12, y no debería llevar más de una tarde.
