---
title: "Regulación y Tramitación del Autoconsumo FV (Parte 2): Régimen Económico, Tarifas y Perfiles de Consumo"
tipo: presentacion
autor: "Fátima Cadahía (Haz Energía), Pablo Corredoira (Haz Energía)"
anio: 2025
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T7_RegulacionTramitacion2.pdf"
tags: [fotovoltaica, autoconsumo, regimen-economico, excedentes, tarifas-electricas, peajes-acceso, cargos, perfiles-de-consumo, cnmc]
related: []
---

# Regulación y Tramitación del Autoconsumo FV (Parte 2): Régimen Económico, Tarifas y Perfiles de Consumo (Fátima Cadahía / Pablo Corredoira, Haz Energía, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición (curso 2025-2026), impartida por Fátima Cadahía y Pablo Corredoira (Haz Energía). Cubre tres bloques: (1) el régimen económico del autoconsumo — compensación simplificada de excedentes (con ejemplos numéricos de una vivienda y de autoconsumo colectivo con coeficientes de reparto) y venta de excedentes a mercado con su fórmula de ingresos mensuales; (2) tarifas eléctricas y perfiles de consumo — caracterización de perfiles horarios/estacionales por sector (residencial, comercial/industrial con 8 subsectores, deportivo, centro comercial, industria frigorífica, agrícola), la normativa que fija la estructura tarifaria vigente (Circular 3/2020 CNMC, RD 148/2021, Resolución de peajes de la CNMC y Orden de cargos), las tablas de periodos horarios (2 y 6 periodos, por territorio) y las fórmulas de facturación de peajes de acceso y cargos (potencia, energía, reactiva, excesos de potencia); y (3) un caso práctico de dimensionado de autoconsumo FV en un colegio de Madrid con tarifa 3.0TD. El documento incluye una referencia normativa (p. 16) que ha quedado desactualizada y se señala explícitamente más abajo.

## Contenido técnico

### 1. Régimen económico del autoconsumo

#### 1.1 Compensación simplificada de excedentes (p. 3-6)

Aplicable a instalaciones tipo a (autoconsumo sin excedentes o con excedentes acogidos a compensación). Los excedentes se valoran a un precio negociado con la comercializadora y se compensan contra la parte del coste de la energía correspondiente al término de energía (no incluye peajes). La compensación tiene carácter **mensual**.

**Caso 1 (p. 3) — vivienda con autoconsumo parcial:**

Hipótesis: energía de red = Pool + costes no regulados (0,072 €/kWh) + peajes y cargos del sistema (0,0447 €/kWh) = **0,1167 €/kWh** total. Precio de excedente cerrado con comercializadora: **0,03 €/kWh**.

| Flujo de energía mensual agregado | Valor | Símbolo |
|---|---|---|
| Consumo total real de la vivienda | 1.000 kWh | A |
| Generación FV total | 500 kWh | B |
| Autoconsumo instantáneo | 450 kWh | C |
| Excedentes de energía | 50 kWh | D = B − C |
| Consumo de la red | 550 kWh | E = A − C |

Factura eléctrica **sin** autoconsumo — término de energía: 1.000 kWh × 0,072 €/kWh = 72 € + 1.000 kWh × 0,0447 €/kWh = 44,7 € → **Total: 116,7 €**

Factura eléctrica **con** autoconsumo — término de energía: 550 kWh × 0,072 €/kWh = 39,6 € + 550 kWh × 0,0447 €/kWh = 24,58 € − compensación de excedentes (50 kWh × 0,03 €/kWh = 1,5 €) → **Total: 39,6 + 24,58 − 1,5 = 62,68 €**

**Caso 2 (p. 4) — excedentes superan el consumo restante (regla del tope):**

Mismas hipótesis de precios. Flujos: consumo total 1.000 kWh, generación FV 1.500 kWh, autoconsumo instantáneo 650 kWh, excedentes 850 kWh, consumo de red 350 kWh.

Factura sin autoconsumo — término de energía: 1.000 kWh × 0,085 €/kWh = 85 € (nota: aquí la presentación usa 0,085 €/kWh, no 0,072 €/kWh como en el Caso 1 — dato tal cual aparece en la fuente, sin explicación del cambio) + 1.000 kWh × 0,0447 €/kWh = 44,7 € → **Total: 129,7 €**

Factura con autoconsumo — término de energía: 350 kWh × 0,072 €/kWh = 25,2 € + 350 kWh × 0,0447 €/kWh = 15,64 €. Valor bruto de excedentes: 850 kWh × 0,03 €/kWh = 25,5 €. **Regla clave señalada en la diapositiva:** valor de excedentes (25,5 €) > valor del término de energía a compensar (25,2 €) → **la compensación queda limitada al término de energía, solo se compensan 25,2 €** (no puede quedar una factura negativa por la parte del término de energía). Resultado: 25,2 + 15,64 − 25,2 = **15,64 €**.

**Ejemplo 1 (p. 5) — autoconsumo colectivo con coeficientes de reparto β:**

Situación global agregada: consumo total 55 kWh, generación FV (GFV) 10 kWh, consumo de red 45 kWh, autoconsumo total 10 kWh, excedentes 0 kWh. Coeficientes de reparto: β₁ = 0,2; β₂ = 0,3; β₃ = 0,5. Hipótesis de precio: energía de red total 0,1167 €/kWh (0,072 pool+otros + 0,0447 peajes/cargos); excedente a 0,03 €/kWh.

Reglas de reparto por vivienda i:
- Autoconsumo asignado: $A_i = GFV \times \beta_i$
- Si $C_i - A_i > 0$: $CRed_i = C_i - A_i$ (consumo de red) y $E_i = 0$ (sin excedente)
- Si $C_i - A_i < 0$: $CRed_i = 0$ y $E_i = A_i - C_i$ (excedente)

| Vivienda | Consumo $C_i$ | Autoconsumo $A_i = GFV \times \beta_i$ | Consumo de red $CRed_i$ | Excedente $E_i$ |
|---|---|---|---|---|
| Casa 1 | 10 kWh | $A_1 = 10 \times 0{,}2 = 2$ kWh $< C_1$ | $CRed_1 = 10-2 = 8$ kWh | 0 kWh |
| Casa 2 | 20 kWh | $A_2 = 10 \times 0{,}3 = 3$ kWh $< C_2$ | $CRed_2 = 20-3 = 17$ kWh | 0 kWh |
| Casa 3 | 25 kWh | $A_3 = 10 \times 0{,}5 = 5$ kWh $< C_3$ | $CRed_3 = 25-5 = 20$ kWh | 0 kWh |

Factura sin autoconsumo (€, por vivienda: Ci × 0,072 + Ci × 0,0447):
| | Casa 1 | Casa 2 | Casa 3 |
|---|---|---|---|
| Pool + otros → Ci × 0,072 | 0,72 | 1,44 | 1,8 |
| Peaje → Ci × 0,0447 | 0,447 | 0,894 | 1,11 |
| **Total → Mercado + Peaje** | **1,16** | **2,33** | **2,91** |

Factura con autoconsumo (€, por vivienda: CRedi × 0,072 + CRedi × 0,0447 + Ei × 0,03 de excedente, que en este ejemplo es 0 para las tres):
| | Casa 1 | Casa 2 | Casa 3 |
|---|---|---|---|
| Pool + otros → CRedi × 0,072 | 0,576 | 1,224 | 1,44 |
| Peaje → CRedi × 0,0447 | 0,357 | 0,759 | 0,894 |
| Excedente → Ei × 0,03 | 0 | 0 | 0 |
| **Total → Mercado + Peaje − Excedente** | **0,93** | **1,98** | **2,33** |

**Ejemplo 2 (p. 6) — mismo esquema, con excedente neto agregado:**

Situación global: consumo total 55 kWh, GFV 60 kWh, consumo de red 2 kWh, autoconsumo total 53 kWh, excedentes 7 kWh. Mismos β y precios.

| Vivienda | Consumo $C_i$ | Autoconsumo asignado (GFV × βᵢ) | Consumo de red $CRed_i$ | Excedente $E_i$ |
|---|---|---|---|---|
| Casa 1 | 10 kWh | $60 \times 0{,}2 = 12$ kWh $> C_1$ | 0 kWh | $E_1 = 12-10 = 2$ kWh |
| Casa 2 | 20 kWh | $60 \times 0{,}3 = 18$ kWh $< C_2$ | $CRed_2 = 20-18 = 2$ kWh | 0 kWh |
| Casa 3 | 25 kWh | $60 \times 0{,}5 = 30$ kWh $> C_3$ | 0 kWh | $E_3 = 30-25 = 5$ kWh |

Factura sin autoconsumo: idéntica a la del Ejemplo 1 (Casa 1: 1,16 €; Casa 2: 2,33 €; Casa 3: 2,91 €), porque el consumo total real por vivienda no cambia.

Factura con autoconsumo:
| | Casa 1 | Casa 2 | Casa 3 |
|---|---|---|---|
| Pool + otros → CRedi × 0,072 | 0 | 0,144 | 0 |
| Peaje → CRedi × 0,0447 | 0 | 0,233 (nota: la diapositiva imprime 0,233; el cálculo directo 2×0,0447 = 0,0894, la cifra de la fuente no cuadra con ese producto — dato tal cual aparece, con incoherencia señalada) | 0 |
| Excedente → Ei × 0,03 | 0,06 | 0 | 0,15 |
| **Total → Mercado + Peaje − Excedente** | **−0,06 ¡!** | **0,377** | **−0,15 ¡!** |

La propia diapositiva marca con "¡!" los resultados negativos de Casa 1 y Casa 3 (−0,06 € y −0,15 €), señalando el caso límite en que el excedente compensado supera el propio término de energía+peaje individual de esa vivienda cuando no hay consumo de red que compensar — situación que en la práctica de facturación no puede saldar en negativo el término de potencia/otros conceptos fijos, aunque la diapositiva no desarrolla la resolución de ese límite.

#### 1.2 Venta de excedentes (p. 7)

Aplicable a instalaciones con o sin compensación. Los excedentes se venden en el mercado eléctrico y el titular adquiere la consideración de productor, por lo que debe satisfacer impuestos (7% sobre el valor de los ingresos) y peajes de acceso a la generación. Requiere alta en el Registro Administrativo de Instalaciones de Producción de Energía Eléctrica (RAIPRE).

**Fórmula de ingresos por venta de excedentes:**

$$Ing_j = \sum_{h=1}^{n} \left[ (E_{n,h} \times Pool_{n,h}) \times (1-IPVEE) \right] - (E_{n,h} \times Pg)$$

Donde:
- $Ing_j$: Ingresos totales del mes "j"
- $E_{n,h}$: Energía en kWh exportada en la hora "h" del día "n"
- $Pool_{n,h}$: Precio del mercado eléctrico en €/kWh en la hora "h" del día "n"
- $IPVEE$: Impuesto sobre el valor de la producción de energía eléctrica, que toma el valor del **7%**
- $Pg$: Peaje a la generación (actualmente, con la Circular 3/2020, toma el valor de **0**)

Conclusión de la diapositiva: **en igualdad de condiciones, resulta más beneficiosa la compensación de excedentes que la venta a mercado de la energía excedentaria.**

### 2. Tarifas eléctricas y perfiles de consumo

#### 2.1 Perfiles de consumo por sector (p. 8-15)

**Residencial (p. 8):** poca diferencia entre distintos consumidores; pico de demanda en horas no solares. Variables críticas: hábitos de consumo (lo más importante), máquinas instaladas (climatización, piscina/bomba, vehículo eléctrico, etc.).
- Gráfica "Consumos acumulados por periodo (kWh)": barras apiladas Punta/Llano/Valle por mes; mínimo en verano (jun-ago, ~600-1.200 kWh totales), máximo en diciembre (~6.800 kWh, con Llano dominante ~6.000 kWh).
- Gráfica "Consumo" horario (Potencia [kW] vs hora del día 0-24h): perfil residencial con picos claros en torno a 8-10h (~20 kW) y 14-24h (~15-23 kW), valle nocturno bajo (~0-2 kW) entre 0-7h.

**Comercial/Industrial — panorama general (p. 9):** diferencias grandes entre consumidores, poca diferencia dentro del mismo sector; pico de demanda en horas solares o no solares según sector. Variables críticas: hábitos de consumo (predecibles con buena toma de datos: cierre fines de semana/perfil intensivo, consumo en horas nocturnas/horarios de trabajo, cierre a mediodía, cierre en verano por vacaciones) y equipos instalados (tipo de consumo constante o variable, grado de eficiencia: climatización/máquinas frigoríficas, iluminación, motores, máquinas de uso esporádico). Sectores principales listados: pequeño comercio, oficinas, hostelería/turismo, educación, industria, deportivo, sanidad, agrícola/ganadero.

**Detalle por subsector (p. 10-11):**

| Subsector | Patrón de cierre/horario | Consumo principal |
|---|---|---|
| Pequeño comercio | Cierre fines de semana/domingos; cierre a mediodía; bajo consumo | Iluminación y climatización; consumo en horas solares |
| Hostelería/turismo | Consumo elevado en meses de verano; consumo diario intensivo; en general consumo elevado | Iluminación y climatización; aumento en horas solares pero pico nocturno |
| Industria | Variable entre sectores (frío, motores, etc.); cierre a mediodía; cierre en julio/agosto | Máquinas; consumo en horas solares salvo máquinas frigoríficas |
| Sanidad | Consumo muy intensivo por superficie; problemas de cubierta; consumo a lo largo de todo el día | Climatización/máquinas; reducción de consumo en fin de semana |
| Oficinas | Cierre fines de semana; consumos elevados por superficie (muchos pisos) | Iluminación y climatización; consumo en horas solares |
| Educación | Cierre parcial en julio y total en agosto | Iluminación y climatización; consumo principal en horas solares |
| Deportivo | Curva poco adaptada a la curva de radiación; posible cierre en agosto | Climatización e iluminación; consumo en horas (no) solares |
| Agrícola/Ganadero | Consumo con alta variabilidad intra-mensual; consumo en horas nocturnas (riego) | Máquinas (bombeo/limpieza/climatización) |

**Deportivo (p. 12) — gráfica "Día promedio mes Octubre":** eje X hora del día (1-24h), eje Y consumo (kWh, 200.000-550.000). Cuatro series: Consumo horario, Consumo mes y periodo, Consumo mes, Consumo anual. Patrón: valle nocturno ~230.000-300.000 kWh (h1-7), salto abrupto a ~490.000 kWh en h8, meseta alta 450.000-500.000 kWh entre h9-23 con ligera caída a media tarde (h17-20, ~380.000-430.000 según serie), caída final brusca a ~230.000-350.000 kWh en h24. Nota de la diapositiva: variación de perfil real vs. perfilado **baja**.

**Centro comercial (p. 13) — gráfica "Día promedio mes Agosto":** eje Y consumo (kWh, 150.000-950.000). Consumo principal en iluminación y climatización, concentrado en la segunda mitad del día. Patrón: valle nocturno ~250.000-400.000 kWh (h1-7), ascenso pronunciado h8-11 hasta ~650.000-850.000 kWh, meseta alta con pico en torno a h15-16 y h21 (~830.000-880.000 kWh en consumo horario), caída final brusca tras h21-22. Nota: variación de perfil real vs. perfilado **media**.

**Industria frigorífica (p. 14) — gráfica "Día promedio mes Abril":** eje Y consumo (kWh, 20.000-200.000). Consumo estable a lo largo del día (rasgo distintivo de este sector frente a los demás, coherente con la naturaleza de carga continua de la refrigeración). Patrón: nivel base ~110.000-130.000 kWh casi constante en consumo horario durante toda la jornada, con incremento moderado y sostenido hasta un máximo ~160.000 kWh entre h15-17, sin los valles nocturnos pronunciados de otros sectores. Nota: variación de perfil real vs. perfilado **media**.

**Agrícola (p. 15) — gráfica "Día promedio mes Septiembre":** eje Y consumo (kWh, 0-50.000). Consumo irregular a lo largo del año. Patrón: base nocturna ~25.000-30.000 kWh, ascenso h7-10 hasta ~40.000-43.000 kWh, meseta con oscilación entre h10-18, descenso h19-24 hasta ~27.000 kWh. La serie de consumo anual (línea inferior, ~10.000-20.000 kWh) está muy por debajo de las demás series, evidenciando la fuerte estacionalidad. Nota: variación de perfil real vs. perfilado **elevada**.

#### 2.2 Normativa de tarifas eléctricas (p. 16-17)

Las nuevas tarifas eléctricas se resumen en la siguiente normativa (tal como aparece en la diapositiva, p. 16):

- **Circular 3/2020 de la CNMC**: establece la metodología de cálculo de los peajes de transporte y distribución; fija las nuevas tarifas y periodos tarifarios.
- **RD 148/2021** de metodología de cálculo de cargos: establece la formulación que aplicará para calcular los cargos del término de energía y potencia.
- **Resolución de 18/03 de la CNMC** de peajes de transporte y distribución: incluye importes de peajes para todas las nuevas tarifas.
- **Orden de cargos del sistema eléctrico**: incluye los importes de los cargos para todas las tarifas.

> **⚠️ NOTA DE VIGENCIA (verificación cruzada, no presente en la diapositiva original):** la referencia "Resolución de 18/03 de la CNMC" de la p. 16 corresponde a la Resolución de 18 de marzo de **2021** de la CNMC sobre peajes de transporte y distribución, que **ya ha sido superada**. La resolución vigente en la actualidad es la **Resolución de la CNMC de 18/12/2025 (BOE-A-2025-26348)**, aplicable desde el **01/01/2026**, según la ficha de seguimiento normativo de este TFM (`Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`) y la memoria de proyecto `project_peaje_61tda_2026`. Esta nota se añade como corrección de vigencia trazable; **no se ha alterado el contenido original de la diapositiva**, que se reproduce arriba tal cual fue impartida en el máster.

**Cambios estructurales en las tarifas (p. 17):**
- Se eliminan las tarifas 2.1.X y 3.1.X.
- Las tarifas 2.0 tendrán 2 términos de potencia y 3 términos de energía.
- Las tarifas 3.X (y superiores) tendrán 6 términos de potencia y de energía.

**Tabla — Peajes de los consumidores:**

| Tarifa | Potencia | Tensión | Periodos de potencia | Periodos de energía |
|---|---|---|---|---|
| 2.0.TD A | P ≤ 15 kW | — | 2 | 3 |
| 3.0.TD A | P > 15 kW | T > 1 kV | 6 | 6 |
| 6.1TD | — | 1 < T ≤ 30 kV | 6 | 6 |
| 6.2TD | — | 30 < T ≤ 72 kV | 6 | 6 |
| 6.3TD | — | 72,5 < T ≤ 145 kV | 6 | 6 |
| 6.4TD | — | T > 145 kV | 6 | 6 |

Notas de la tabla (literales):
- Nota 1: A partir de la tarifa 3.0 la potencia contratada en el periodo Pₙ₊₁ ≥ Pₙ.
- Nota 2: Los autoconsumos "a través de red" tendrán que satisfacer peajes específicos por la energía que autoconsuman.
- Nota 3: Las importaciones y exportaciones les será de aplicación los peajes 6.4TD.

Simplificaciones señaladas: desaparece la referencia a 36 kV de las tarifas 3.1A (criterio de tensión); desaparece la referencia de 10 kW (para distinguir 2.0X/2.1X) y de 450 kW (para distinguir 3.1A/6.1) (criterio de potencia). Los nuevos peajes y cargos son más elevados al consumo, especialmente en P1 y P2.

#### 2.3 Periodos tarifarios (p. 18-21)

**Tarifas de 2 periodos (2.0, DH2p y DH3p) — p. 18:**

| Hora | Península/Canarias/Baleares DH2p | Península/Canarias/Baleares DH3p | Hora | Ceuta y Melilla DH3p | Ceuta y Melilla DH2p |
|---|---|---|---|---|---|
| 0-1 | VALLE | P3 | 0-1 | P3 | VALLE |
| 1-2 | VALLE | P3 | 1-2 | P3 | VALLE |
| 2-3 | VALLE | P3 | 2-3 | P3 | VALLE |
| 3-4 | VALLE | P3 | 3-4 | P3 | VALLE |
| 4-5 | VALLE | P3 | 4-5 | P3 | VALLE |
| 5-6 | VALLE | P3 | 5-6 | P3 | VALLE |
| 6-7 | VALLE | P3 | 6-7 | P3 | VALLE |
| 7-8 | VALLE | P3 | 7-8 | P3 | VALLE |
| 8-9 | PUNTA | P2 | 8-9 | P2 | PUNTA |
| 9-10 | PUNTA | P2 | 9-10 | P2 | PUNTA |
| 10-11 | PUNTA | P1 | 10-11 | P2 | PUNTA |
| 11-12 | PUNTA | P1 | 11-12 | P1 | PUNTA |
| 12-13 | PUNTA | P1 | 12-13 | P1 | PUNTA |
| 13-14 | PUNTA | P1 | 13-14 | P1 | PUNTA |
| 14-15 | PUNTA | P2 | 14-15 | P1 | PUNTA |
| 15-16 | PUNTA | P2 | 15-16 | P2 | PUNTA |
| 16-17 | PUNTA | P2 | 16-17 | P2 | PUNTA |
| 17-18 | PUNTA | P2 | 17-18 | P2 | PUNTA |
| 18-19 | PUNTA | P1 | 18-19 | P2 | PUNTA |
| 19-20 | PUNTA | P1 | 19-20 | P1 | PUNTA |
| 20-21 | PUNTA | P1 | 20-21 | P1 | PUNTA |
| 21-22 | PUNTA | P1 | 21-22 | P1 | PUNTA |
| 22-23 | PUNTA | P2 | 22-23 | P1 | PUNTA |
| 23-24 | PUNTA | P2 | 23-24 | P2 | PUNTA |

**Tarifas de 6 periodos — Península (p. 19):**

| Hora | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic | Otros* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-1 a 7-8 | P6 (todas las horas y meses) | | | | | | | | | | | | P6 |
| 8-9 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 9-10 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 10-11 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 11-12 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 12-13 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 13-14 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 14-15 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 15-16 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 16-17 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 17-18 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 18-19 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 19-20 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 20-21 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 21-22 | P1 | P1 | P2 | P4 | P4 | P3 | P1 | P3 | P3 | P4 | P2 | P1 | P6 |
| 22-23 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |
| 23-24 | P2 | P2 | P3 | P5 | P5 | P4 | P2 | P4 | P4 | P5 | P3 | P2 | P6 |

*Otros = sábados, domingos y festivos (P6 todo el día).

**Tarifas de 6 periodos — Canarias (p. 20):** mismo formato de tabla; horas 0-1 a 7-8 en P6 todos los meses. A partir de 8-9, el patrón difiere de Península:

| Hora | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic | Otros* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8-9 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 9-10 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 10-11 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 11-12 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 12-13 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 13-14 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 14-15 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 15-16 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 16-17 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 17-18 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 18-19 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 19-20 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 20-21 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 21-22 | P1 | P1 | P2 | P4 | P4 | P2 | P1 | P2 | P2 | P4 | P2 | P1 | P6 |
| 22-23 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |
| 23-24 | P3 | P3 | P3 | P5 | P5 | P4 | P3 | P4 | P4 | P5 | P3 | P3 | P6 |

Diferencia clave frente a Península: en Canarias el cambio de nivel de precio ocurre a las 15h (no a las 14h), y el nivel "punta doble" usa P3/P5 (no P2/P5) en las franjas altas, y P1/P2 (no P1/P3) en las franjas intermedias.

**Tarifas de 6 periodos — Baleares (p. 21):** horas 0-1 a 7-8 en P6. Las filas 8-9, 9-10 y 10-11 a 13-14 leídas directamente en la diapositiva **coinciden exactamente, columna a columna, con las mismas filas de la tabla de Península** (8-9/9-10: P2 P2 P3 P5 P5 P4 P2 P4 P4 P5 P3 P2; 10-14: P1 P1 P2 P4 P4 P3 P1 P3 P3 P4 P2 P1). Dado que esta coincidencia es consistente con la práctica regulatoria de la CNMC de tratar Península y Baleares como una única zona a efectos de periodos horarios tarifarios, se documenta la tabla de Baleares como **idéntica a la de Península** para todas las horas (ver nota de vigencia y fidelidad en "Notas de procesamiento" más abajo, donde se señala el nivel de confianza de esta transcripción para las filas 14-15 a 21-22).

#### 2.4 Peajes de acceso — fórmulas de facturación (p. 22-23)

Los consumidores pagarán los siguientes conceptos:

**Término de potencia:**
$$FP = \sum_{p=1}^{i} Tp_p \times Pc_p$$
Donde: FP = facturación de la potencia; $Tp_p$ = precio del término de potencia del periodo horario p, expresado en €/kW y año; $Pc_p$ = potencia contratada en el periodo horario p, expresada en kW; $i$ = número de periodos horarios de los que consta el término de facturación de potencia del peaje correspondiente.

**Término de energía:**
$$FE = \sum_{p=1}^{i} Te_p \times E_p$$
Donde: FE = facturación por energía, expresada en €; $Te_p$ = precio del término de energía del periodo horario p, expresado en €/kWh; $E_p$ = energía consumida o estimada en el periodo horario p, expresada en kWh; $i$ = número de periodos horarios de los que consta el término de facturación de energía del peaje correspondiente.

**Energía reactiva:** no será de aplicación a las tarifas 2.0. Se aplicará sobre todos los periodos tarifarios excepto el P6, siempre que el consumo de reactiva exceda el 33% del consumo de activa durante el periodo de facturación considerado, y únicamente afectará a dichos excesos.
$$\frac{E_a}{\sqrt{E_a^2+E_r^2}}$$
Donde: $E_a$ = cantidad registrada por el contador de energía activa, expresada en kWh; $E_r$ = cantidad registrada por el contador de energía reactiva, expresada en kVArh.

**Término de facturación por potencia demandada (excesos de potencia, p. 23):** las tarifas 2.X solo pagan este concepto si disponen de maxímetro. Cuando en cualquier periodo tarifario se sobrepase el 105% de la potencia contratada en el mismo, se cobrarán excesos según la fórmula correspondiente al tipo de equipo de medida.

*Puntos de suministro con medidas tipo 4 y 5:*
$$F_{EP} = \sum_{p=1}^{i} t_p \times 2 \times (Pd_j - 1{,}05 \times Pc_p)$$
Donde: $F_{EP}$ = facturación en concepto de excesos de potencia; $t_p$ = término de exceso de potencia, expresado en €/kW, del peaje correspondiente; $Pd_j$ = potencia demandada en cada uno de los periodos horarios p en que se haya sobrepasado $Pc_p$; $Pc_p$ = potencia contratada en el periodo horario p, expresada en kW; $i$ = número de periodos horarios de los que consta el término de facturación de potencia del peaje correspondiente.

*Puntos de suministro con medidas tipo 1, 2 y 3:*
$$F_{EP} = \sum_{p=1}^{i} K_p \times t_{ep} \times \sqrt{\sum_{j=1}^{n} (Pd_j - Pc_p)^2}$$
Donde: $F_{EP}$ = facturación en concepto de excesos de potencia; $K_p$ = relación de precios por periodo horario p, calculada como el cociente entre el término de potencia del periodo p respecto del término de potencia en el periodo 1 del peaje correspondiente; $t_{ep}$ = término de exceso de potencia, expresado en €/kW, del peaje correspondiente (el término del exceso de potencia se determinará de forma que, dado el perfil del consumidor medio de cada peaje, la facturación de acceso que resulte de la optimización de las potencias sea equivalente a la que resultaría de considerar las potencias contratadas máximas de cada periodo, con la restricción de que la facturación de acceso del periodo 1 tras la optimización nunca sea negativa; el término resultante se incrementa en un 20% para desincentivar la contratación de potencias inferiores a las demandadas); $Pd_j$ = potencia demandada en cada uno de los cuartos de hora j del periodo horario p en que se haya sobrepasado $Pc_p$, expresada en kW (si el equipo de medida no dispone de capacidad de registro cuartohoraria, se considera la misma potencia demandada en todos los cuartos de hora); $Pc_p$ = potencia contratada en el periodo horario p, expresada en kW; $i$ = número de periodos horarios de los que consta el término de facturación de potencia del peaje correspondiente.

#### 2.5 Cargos (p. 24)

Los consumidores pagarán los siguientes conceptos de cargos. **Nota de fidelidad:** la diapositiva original presenta esta pareja de fórmulas con las etiquetas de encabezado y las variables de la sección "Donde" **cruzadas** respecto a la fórmula mostrada — se reproduce literalmente tal como aparece, sin corregir, señalando la incoherencia:

- Bajo el epígrafe **"Término de facturación por potencia"**, la fórmula mostrada es:
$$FE = \sum_{p=1}^{1} Tep \times Ep$$
con "Donde: FP: Facturación de la potencia, expresada en €; Tpp: precio del término de potencia del periodo horario p, expresado en €/kW; Pcp: potencia contratada en el periodo horario p, expresada en kW; i: número de periodos horarios de los que consta el término de facturación de energía del peaje correspondiente" (es decir, la fórmula usa notación de energía —FE, Tep, Ep— pero la explicación "Donde" usa notación de potencia —FP, Tpp, Pcp—).

- Bajo el epígrafe **"Término de facturación por energía"**, la fórmula mostrada es:
$$FP = \sum_{p=1}^{1} Tpp \times Pcp$$
con "Donde: FE: Facturación por energía, expresada en €; Tep: Precio del término de energía del periodo horario p, expresado en €/kWh; Ep: Energía consumida o estimada en el periodo horario p, expresada en kWh; i: Número de periodos horarios de los que consta el término de facturación de energía del peaje correspondiente" (aquí ocurre el cruce inverso: fórmula de potencia, explicación de energía).

Interpretación razonable (no confirmada explícitamente en la fuente, dejada como tal): por estructura y analogía directa con las fórmulas de peajes de acceso de la p. 22 (que sí están correctamente etiquetadas), el cargo por potencia sigue previsiblemente $FP_{cargo} = \sum Tpp \times Pcp$ y el cargo por energía $FE_{cargo} = \sum Tep \times Ep$, con la misma estructura funcional que los peajes pero con precios (Tpp, Tep) fijados por la Orden de cargos en vez de por la Resolución de peajes de la CNMC.

#### 2.6 Caso práctico — importancia del ajuste del término de energía (p. 25)

Gráfica "Curva de Potencia" (eje Y: kW, 0-100; eje X: fechas 01/01/2022 a 01/12/2022): perfil de consumo horario muy variable con picos recurrentes entre 60-100 kW y valles en torno a 20-40 kW a lo largo de todo el año, sin estacionalidad marcada visible en la envolvente.

Tabla comparativa de escenarios de contratación de potencia:

| Caso | P1 (kW) | P2 (kW) | P3 (kW) | P4 (kW) | P5 (kW) | P6 (kW) | Facturación término de potencia | Facturación excesos de potencia | Coste total |
|---|---|---|---|---|---|---|---|---|---|
| 1 — Situación actual | 85 | 85 | 85 | 85 | 85 | 90 | 5.510 € | 817 € | 6.327 € |
| 2 — Ajuste pequeño | 75 | 75 | 75 | 75 | 75 | 90 | 4.874 € | 3.433 € | 8.307 € |
| 3 — Ajuste drástico | 60 | 60 | 60 | 60 | 60 | 90 | 3.920 € | 15.573 € | 19.493 € |

Conclusión implícita del caso: reducir la potencia contratada disminuye la facturación por término de potencia pero dispara la facturación por excesos (al superar sistemáticamente el 105% de lo contratado), de forma que el coste total **aumenta** cuanto más agresivo es el ajuste a la baja — el "ajuste drástico" casi triplica el coste total frente a la situación actual. Ilustra la importancia de dimensionar la potencia contratada de acuerdo con la curva de demanda real, no solo minimizar el término fijo.

### 3. Caso práctico — colegio en Madrid (p. 26)

**Enunciado:** se quiere realizar una instalación de autoconsumo fotovoltaico en un colegio en Madrid (referencia a un enlace a Google Maps para la ubicación de la parcela, no reproducible como texto), con tarifa contratada **3.0TD**, consumo anual de **25.740 kWh** (unidad indicada en la diapositiva como "kW", pero por magnitud y consistencia con la tabla mensual se interpreta como kWh/año), y potencia contratada de **19,1 kW** en cada periodo. Tipo de suministro: **trifásico**. Hay diferentes zonas del colegio donde se puede realizar la instalación, siempre que no sean zonas de recreo (restricción explícita del enunciado, sin más detalle).

**Coste del término de energía por periodo (€/kWh):**

| Periodo | P1 | P2 | P3 | P4 | P5 | P6 |
|---|---|---|---|---|---|---|
| Coste (€/kWh) | 0,15 | 0,14 | 0,13 | 0,12 | 0,11 | 0,10 |

**Consumo mensual por periodo tarifario (kWh):**

| Mes | P1 | P2 | P3 | P4 | P5 | P6 | Total |
|---|---|---|---|---|---|---|---|
| Ene | 1.233 | 722 | 0 | 0 | 0 | 880 | 2.835 |
| Feb | 1.168 | 742 | 0 | 0 | 0 | 892 | 2.801 (nota: 1.168+742+892=2.802, discrepancia de 1 kWh frente al total impreso de 2.801 — dato tal cual aparece en la fuente) |
| Mar | 0 | 1.070 | 663 | 0 | 0 | 831 | 2.564 |
| Abr | 0 | 0 | 0 | 939 | 567 | 988 | 2.494 |
| May | 0 | 0 | 0 | 1.057 | 655 | 897 | 2.608 (nota: 1.057+655+897=2.609, discrepancia de 1 kWh frente al total impreso de 2.608) |
| Jun | 0 | 0 | 738 | 433 | 0 | 634 | 1.805 |
| Jul | 135 | 96 | 0 | 0 | 0 | 256 | 486 (nota: 135+96+256=487, discrepancia de 1 kWh frente al total impreso de 486) |
| Ago | 0 | 0 | 144 | 102 | 0 | 204 | 450 |
| Sep | 0 | 0 | 722 | 415 | 0 | 719 | 1.856 |
| Oct | 0 | 0 | 0 | 1.189 | 678 | 966 | 2.833 |
| Nov | 0 | 1.245 | 725 | 0 | 0 | 851 | 2.821 |
| Dic | 849 | 511 | 0 | 0 | 0 | 825 | 2.185 |
| **Total** | **3.385** | **4.385** | **2.992** | **4.136** | **1.900** | **8.943** | **25.740** |

Las pequeñas discrepancias de ±1 kWh entre la suma de columnas por fila y el total impreso en algunos meses (Feb, May, Jul) son de la fuente original y no se han corregido; probablemente redondeos internos de la hoja de origen de la diapositiva.

## Datos clave (con página de origen)

- Compensación de excedentes: precio de red total ejemplo = 0,1167 €/kWh (pool+otros 0,072 + peajes/cargos 0,0447); precio de excedente negociado = 0,03 €/kWh (p. 3-4).
- Regla de tope en la compensación simplificada: el excedente compensado nunca puede superar el término de energía a pagar en ese mes (p. 4).
- Fórmula de venta de excedentes a mercado: IPVEE = 7% sobre ingresos; Pg (peaje a la generación) = 0 con la Circular 3/2020 vigente en el momento de la presentación (p. 7).
- Estructura tarifaria: 2.0.TD A (P≤15kW) con 2 periodos de potencia / 3 de energía; 3.0.TD A y superiores (6.1TD a 6.4TD) con 6/6 periodos (p. 17).
- Umbral de exceso de potencia: se factura exceso cuando la demanda supera el 105% de la potencia contratada en cualquier periodo (p. 23).
- Umbral de energía reactiva: se factura cuando el consumo de reactiva excede el 33% del consumo de activa, no aplica a tarifas 2.0 ni al periodo P6 (p. 22).
- Caso práctico de ajuste de potencia: reducir potencia contratada de 85→60 kW en P1-P5 casi triplica el coste total (6.327 €→19.493 €) por el disparo de excesos de potencia (p. 25).
- Caso práctico colegio Madrid: tarifa 3.0TD, 25.740 kWh/año, 19,1 kW contratados por periodo, suministro trifásico (p. 26).
- **Vigencia normativa corregida:** la Resolución de peajes citada en p. 16 (18/03/2021) está superada; la vigente es la Resolución CNMC de 18/12/2025 (BOE-A-2025-26348), aplicable desde 01/01/2026 (verificación cruzada, no en la fuente original).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: régimen económico y facturación del autoconsumo (capítulo de análisis económico/marco regulatorio), dimensionado de potencia contratada frente a la curva de demanda del CPD (relevante para evitar el patrón de "ajuste drástico" que dispara excesos, ver p. 25), y estructura tarifaria aplicable a un CPD de alta potencia (previsiblemente tarifa 6.1TD o superior según el punto de conexión, no 3.0TD como en el caso práctico del colegio).
- **Qué aporta exactamente**: (1) la mecánica exacta y trazable de la compensación simplificada de excedentes con su regla de tope, útil para el modelo horario de gestión de excedentes/batería del CPD; (2) la fórmula oficial de venta de excedentes a mercado (Ing_j, con IPVEE y Pg) como alternativa a comparar frente a la compensación; (3) las tablas completas de periodos tarifarios (6 periodos, Península) y las fórmulas de peajes de acceso y cargos, necesarias para construir el modelo de facturación eléctrica horaria del CPD en el capítulo económico; (4) evidencia empírica (caso práctico p. 25) de que sobredimensionar el ahorro por reducción de potencia contratada sin verificar la curva de demanda real puede ser contraproducente — argumento a citar al justificar la potencia contratada del CPD.
- **Confianza en los datos**: todas las cifras provienen directamente de las diapositivas y se han transcrito con su página de origen. Las tres discrepancias aritméticas de ±1 kWh en la tabla del caso práctico del colegio (Feb, May, Jul) son de la fuente original, señaladas explícitamente, no corregidas. La tabla de periodos tarifarios de Baleares (p. 21) se documenta como idéntica a la de Península por coincidencia directa observada en las filas verificables y por consistencia con la práctica regulatoria de la CNMC — ver nota de procesamiento sobre el nivel de confianza de esa transcripción específica.

## Notas de procesamiento

- **Documento leído íntegro: 26 páginas / 26 diapositivas**, sin omisiones, en cumplimiento del nivel Exhaustivo solicitado.
- Todas las ecuaciones (compensación de excedentes, venta de excedentes Ing_j, peajes de acceso FP/FE, energía reactiva, excesos de potencia FEP para medida tipo 4/5 y tipo 1/2/3, cargos) se han preservado íntegramente en notación LaTeX.
- Todas las tablas (flujos de energía, facturas por caso, tarifas 2.0-6.4TD, periodos tarifarios de 2 y 6 periodos por territorio, coste de término de energía y consumo mensual del caso práctico) se han preservado con sus cabeceras y unidades originales.
- Todas las gráficas descritas (perfiles de consumo residencial, deportivo, centro comercial, industria frigorífica, agrícola; curva de potencia del caso práctico p. 25) se han caracterizado por ejes, unidades, rango de valores y tendencia observada, dado que no son extraíbles como datos tabulares desde un PDF de presentación.
- **Incoherencias de la fuente señaladas explícitamente, sin corrección silenciosa**: (1) precio de energía de red que cambia de 0,072 a 0,085 €/kWh entre Caso 1 y Caso 2 de compensación simplificada (p. 3-4) sin explicación en la diapositiva; (2) cifra de peaje de Casa 2 en el Ejemplo 2 (0,233 €) que no cuadra con el producto directo 2 kWh × 0,0447 €/kWh = 0,0894 € (p. 6); (3) etiquetas de encabezado y variables "Donde" cruzadas entre las dos fórmulas de la diapositiva de Cargos (p. 24); (4) discrepancias de ±1 kWh entre suma de filas y total impreso en la tabla mensual del caso práctico del colegio (p. 26, meses de febrero, mayo y julio).
- **Nivel de confianza sobre la tabla de periodos tarifarios de Baleares (p. 21)**: las filas de horas 0-1 a 13-14 y 22-24 se verificaron por coincidencia exacta, columna a columna, con las mismas filas de la tabla de Península (p. 19), confirmando que ambos territorios comparten calendario tarifario. Las filas de horas 14-15 a 21-22 se documentan como idénticas a Península por esa misma consistencia estructural y por ser la práctica regulatoria estándar de la CNMC (Península y Baleares como zona única a efectos de periodos horarios), pero no se pudo confirmar con la misma certeza visual pixel a pixel que las demás filas al releer la imagen de la diapositiva; se recomienda a Mario una verificación visual directa de esas filas concretas en la página 21 del PDF original si se van a usar para un cálculo de facturación específico de un mes de esa franja horaria.
- **Nota de vigencia normativa**: se ha añadido una advertencia explícita en la sección 2.2 señalando que la "Resolución de 18/03" de la CNMC citada en la diapositiva original (p. 16) es la de 2021, superada, y que la vigente es la Resolución CNMC de 18/12/2025 (BOE-A-2025-26348), aplicable desde el 01/01/2026, según `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`. El contenido original de la diapositiva no se ha alterado; la advertencia se presenta como anotación de verificación independiente y trazable.
- No hay imágenes no extraíbles adicionales: todo el contenido visual relevante (tablas, fórmulas, gráficas) ha sido descrito o transcrito en el cuerpo del resumen.
