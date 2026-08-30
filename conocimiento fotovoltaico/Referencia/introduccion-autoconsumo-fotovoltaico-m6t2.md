---
title: "Introducción al autoconsumo fotovoltaico (M6_T2)"
tipo: presentacion
autor: "Julio Amador Guerra"
anio: "2025-2026 (20ª edición del Máster ERMA)"
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T2_IntroduccionFV.pdf"
tags: [fotovoltaica, autoconsumo, balance-energetico, almacenamiento, indices-energeticos, erma]
related: []
---

# Introducción al autoconsumo fotovoltaico (Julio Amador Guerra, 2025-2026)

## Resumen

Presentación docente del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA que introduce los conceptos base del autoconsumo FV: tipos de instalación según potencia, propiedad y ubicación; clasificación según destino de la energía excedente (total vs. parcial); definición formal de los índices energéticos de autoconsumo (autoconsumo, cobertura de la demanda, dependencia de la red) mediante un balance de energías en el punto de conexión; caracterización de perfiles de consumo horario por tipología de edificio; y, en el bloque final, la extensión de todo el aparato de balance e índices al caso con acumulación en batería. Incluye un ejemplo numérico completo resuelto paso a paso para una vivienda tipo en Madrid con un sistema de 2 kWp. Es la fuente docente directa de la nomenclatura E_PV/E_L/E_TUN/E_FUN/E_TS/E_FS/E_SO que debe emplearse de forma consistente en el modelo horario de almacenamiento del TFM.

## Contenido técnico

### 1. Portada y estructura (diapositivas 1, 2 y 22)

- Diapositiva 1 (portada del módulo): "Máster en Energías Renovables y Medio Ambiente", 20ª edición 2025-2026. Recuadro: "Módulo 6 — Autoconsumo Fotovoltaico" / "Introducción al autoconsumo fotovoltaico". Autor: Julio Amador Guerra, Universidad Politécnica de Madrid.
- Diapositiva 2 (índice) — **nota de discrepancia**: el encabezado de esta y de todas las diapositivas de contenido dice literalmente "Módulo 5. Autoconsumo fotovoltaico", mientras que la portada (diapositiva 1) y el nombre de fichero (`M6_T2_...`) dicen "Módulo 6". No se resuelve esta discrepancia por cuenta propia: probablemente una plantilla reutilizada de una edición anterior del máster en la que el tema era el Módulo 5; se reporta tal cual aparece en la fuente.
- Índice de la presentación (5 puntos, repetido idéntico en la diapositiva 22 de cierre):
  1. Tipos de instalaciones FV de autoconsumo
  2. Tipos de autoconsumo según el destino de la energía
  3. Índices energéticos de autoconsumo
  4. Perfiles de consumo horario
  5. Balance energético con acumulación

### 2. Concepto de autoconsumo fotovoltaico (diapositiva 3)

Definición operativa: "Producción fotovoltaica para consumo propio; sólo el exceso, si existe, se vierte a la red." Esquema de bloques: Generador fotovoltaico → Inversor → Red eléctrica interna (hacia instalación usuario) / Red eléctrica (excedentes).

**Opciones de propiedad del sistema FV:**
- Misma que el consumo.
- Empresa ajena (PPA — Power Purchase Agreement).

**Opciones de ubicación del sistema FV:**
- Edificio del consumo.
- Otro emplazamiento.

**Tipo de edificio/consumo:** Residencial, Comercial, Industrial.

**Nivel de tensión de conexión según la potencia instalada:**

| Rango de potencia | Nivel de tensión |
|---|---|
| P ≤ 15 kW | 1F BT (red monofásica en baja tensión) |
| P ≤ 100 kW | 3F BT (red trifásica en baja tensión) |
| 100 kW < P ≤ 10 MW | MT (media tensión) |
| P > 10 MW | AT (alta tensión) |

### 3. Tipos de instalaciones de autoconsumo FV (diapositivas 4-7)

**Clasificación por potencia** (diapositiva 4, con fotografías ilustrativas sin fuente citada):
- Residencial: P < 10 kW
- Comercial: 10 kW ≤ P ≤ 50 kW
- Industrial: P > 50 kW

**Clasificación individual/colectivo** (diapositiva 5): instalación individual (vivienda unifamiliar) vs. colectiva (bloque de edificios con paneles distribuidos en varias cubiertas). Fuente: *Guía del autoconsumo colectivo*, IDAE 2024.

**Evolución de potencia instalada de autoconsumo en España** (diapositiva 6) — gráfica de barras apiladas (eje izquierdo: potencia instalada anual en MW, escala lineal 0-3000; eje derecho: potencia acumulada de autoconsumo en MW, escala logarítmica 1-10000) por categoría (Industriales, Residenciales, Comerciales, Aisladas) y año, más una serie de línea con la potencia acumulada total:

| Año | Industriales (MW) | Residenciales (MW) | Comerciales (MW) | Aisladas (MW) | Potencia acumulada de autoconsumo (MW) |
|---|---|---|---|---|---|
| 2020 | 334 | 113 | 137 | 12 | 1.539 |
| 2021 | 493 | 385 | 313 | 12 | 2.742 |
| 2022 | 1.178 | 802 | 501 | 25 | 5.249 |
| 2023 | 1.020 | 372 | 291 | 23 | 6.955 |
| 2024 | 674 | 275 | 207 | 27 | 8.137 |

Tendencia: crecimiento sostenido de la potencia acumulada 2020→2024 (de 1.539 a 8.137 MW), con un máximo de instalación anual en 2022 (segmento industrial dominante, 1.178 MW) y descenso de la instalación anual nueva en 2023-2024 respecto al pico de 2022, aunque la acumulada sigue creciendo. Fuente: Unión Española Fotovoltaica (UNEF), https://www.unef.es/es/autoconsumo.

**Distribución de la potencia FV en Europa por segmento, 2024-2029 (proyección)** (diapositiva 7) — gráfica de barras apiladas al 100%, tres categorías (Residencial, Comercial e Industrial, Grandes plantas):

| Año | Residencial (%) | Comercial e Industrial (%) | Grandes plantas (%) |
|---|---|---|---|
| 2024 | 18 | 37 | 44 |
| 2025 | 16 | 36 | 48 |
| 2026 | 16 | 35 | 49 |
| 2027 | 16 | 36 | 48 |
| 2028 | 16 | 36 | 48 |
| 2029 | 16 | 38 | 46 |

Tendencia: el peso relativo residencial cae del 18% (2024) al 16% (estable 2025-2029); grandes plantas gana peso hasta ~48-49% en 2026-2028 y retrocede ligeramente a 46% en 2029; comercial e industrial se mantiene en banda 35-38%. Fuente: SolarPower Europe.

### 4. Tipos de autoconsumo según el destino de la energía (diapositivas 8-11)

**Autoconsumo total = sin excedentes** (diapositiva 8): "La energía generada se consume íntegramente en la red interior a la que está conectada la instalación generadora." Ejemplo ilustrado: generación fotovoltaica y demanda en la ETSIDI-UPM (gráfica temporal multi-día, generación en naranja muy inferior y aplanada frente a un consumo en azul con picos periódicos de hasta ~280 kWh en horario laborable — perfil de "2 trafos"). Fuente: CONERSA.

**Autoconsumo parcial = con excedentes** (diapositivas 9-10):
- Ejemplo de consumo doméstico en día laborable con cielo claro (diapositiva 9): gráfica kW vs. horas del día (1-24). Se distinguen cuatro zonas: "Consumo cubierto con electricidad de la red" (banda superior), "Energía excedente (EE) FV — que deberá ser almacenada de alguna forma" (banda inferior negativa, valle de hasta -2,5 kW entre horas 12-14), "Consumo cubierto con electricidad FV (energía autoconsumida instantáneamente)", y la curva de "Consumo eléctrico" (pico ~3,5 kW entorno a la hora 13) frente a la curva de "Generación FV". Fuente: ECLAREON.
- Perfiles diarios de generación y consumo para un día de verano y un día de invierno, vivienda en Suiza (diapositiva 10): dos gráficas, eje "Electricity (kWh)" 0-30 vs. "Hour" 0-23, series Building el. consumption, Total production, Façades production, Roof production. Verano: producción total con pico ~25 kWh entre horas 12-15; consumo con pico secundario ~15 kWh hacia hora 20. Invierno: producción total notablemente menor, pico ~17 kWh hacia hora 13; consumo con pico nocturno ~15 kWh hacia horas 19-20. Fuente: *Building-Integrated Photovoltaic. A Technical Guidebook*, ed. Nuria Martín Chivelet et al., IEA PVPS.

**Tratamiento de la energía excedente** (diapositiva 11):
- **Reconocida:** balance neto / batería virtual, etc. (Consumo neto = Consumo − excedentes); venta de la energía en el mercado eléctrico.
- **No reconocida:** se pierde; gestión de la demanda (cargas diferidas); acumulación (el excedente se almacena en baterías).

### 5. Índices energéticos de autoconsumo — balance sin acumulación (diapositivas 12-17)

Esquema de bloques común a esta sección: irradiancia $G_I$ → Instalación fotovoltaica (energía captada $E_A$) → inversor → contador bidireccional ($E_{NG}$ generada neta tras inversor) → bus de conexión, del que salen $E_{TUN}$ (inyectada a la red de distribución) y $E_{FUN}$ (consumida de la red de distribución) hacia la Red Pública de Distribución a través de un segundo contador bidireccional, y $E_L$ hacia la Instalación usuario. $E_{AUTO,PV}$ es la fracción de $E_{NG}$ que se consume instantáneamente en la instalación usuario.

**Definiciones (diapositiva 12):**
- $E_{PV}$: energía generada por el sistema fotovoltaico.
- $E_{TUN}$: energía inyectada en la red de distribución.
- $E_{FUN}$: energía consumida de la red de distribución.
- $E_L$: energía consumida (por la instalación usuario).

**Balance energético general (sin acumulación):**
$$E_{PV} + E_{FUN} = E_L + E_{TUN}$$

**Energía fotovoltaica autoconsumida** (energía consumida aportada por fotovoltaica):
$$E_{AUTO,PV} = E_L - E_{FUN} = E_{PV} - E_{TUN}$$

**Energía neta aportada por la red:**
$$E_{NUN} = E_{FUN} - E_{TUN} = E_L - E_{PV}$$

**Ejemplo gráfico** (diapositiva 13): perfil horario de una vivienda, kW vs. horas 1-24. Curva $E_L$ (consumo eléctrico, azul, pico ~4,5 kW hacia la hora 20, valle hacia la hora 4) y curva $E_{PV}$ (generación fotovoltaica, roja, pico ~4,5 kW hacia la hora 13). Zona roja sombreada = $E_{AUTO,PV}$ (intersección de ambas curvas). Zonas verdes rayadas: "Energía importada de la red eléctrica" (mañana y noche, corresponde a $E_{FUN}$) y "Energía exportada a la red eléctrica" (mediodía, eje negativo hasta -3 kW, corresponde a $E_{TUN}$). Fuente: http://hectevi.blogspot.com.es.

**Índices energéticos formales (diapositiva 14):**

Porcentaje de autoconsumo:
$$A_{PV} = \frac{E_{AUTO,PV}}{E_{PV}} \cdot 100$$

Cobertura de la demanda sin balance neto:
$$C_D = \frac{E_{AUTO,PV}}{E_L} \cdot 100$$

Cobertura de la demanda con balance neto:
$$C_{D,NM} = \frac{E_{PV}}{E_L} \cdot 100$$

Dependencia de la red:
$$D_G = \frac{E_{NUN}}{E_L} \cdot 100$$

Relaciones entre índices:
$$C_{D,NM} \cdot A_{PV} = C_D$$
$$C_{D,NM} + D_G = 100$$

**Caso particular: autoconsumo total** (diapositiva 15), definido por $E_{TUN} = 0 \Leftrightarrow E_{PV} = E_{AUTO,PV}$:
$$E_L = E_{PV} + E_{FUN}$$
$$E_{AUTO,PV} = E_{PV} = E_L - E_{FUN}$$
$$E_{NUN} = E_{FUN} = E_L - E_{PV}$$
$$A_{PV} = \frac{E_{AUTO,PV}}{E_{PV}} \cdot 100 = 100\%$$
$$C_D = \frac{E_{AUTO,PV}}{E_L} \cdot 100 = C_{D,NM} = \frac{E_{PV}}{E_L} \cdot 100$$
$$D_G = \frac{E_{NUN}}{E_L} \cdot 100 = \frac{E_{FUN}}{E_L} \cdot 100$$

**Ejemplo numérico completo resuelto** (diapositivas 16-17, preservado literalmente tal como aparece en la fuente):

Datos de partida:
- Consumo medio de vivienda en España: $E_L = 3.487$ kWh (fuente citada en la diapositiva como "I.D.A.E. 20...", año parcialmente tapado por el logotipo del máster en el PDF original — no se puede confirmar el año exacto de la fuente IDAE desde esta diapositiva; no completar con conocimiento externo).
- Sistema fotovoltaico conectado a red en Madrid, 2 kWp.
- Producción media anual asumida: 1.500 kWh/kWp/año $\Rightarrow E_{PV} = 3.000$ kWh.
- Hipótesis de partida: autoconsumo del 60% ($A_{PV} = 60\%$).

Desarrollo paso a paso:
$$A_{PV} = \frac{E_{AUTO,PV}}{E_{PV}} \cdot 100 = 60\% \Rightarrow E_{AUTO,PV} = 0{,}6 \cdot E_{PV} = 1.800 \text{ kWh}$$
$$E_{AUTO,PV} = E_L - E_{FUN} = E_{PV} - E_{TUN}$$
$$E_{FUN} = E_L - E_{AUTO,PV} = 3.487 - 1.800 = 1.687 \text{ kWh}$$
$$E_{TUN} = E_{PV} - E_{AUTO,PV} = 3.000 - 1.800 = 1.200 \text{ kWh}$$
$$E_{NUN} = E_{FUN} - E_{TUN} = 1.687 - 1.200 = 487 \text{ kWh}$$

Cálculo de índices sobre el mismo ejemplo:
$$C_D = \frac{E_{AUTO,PV}}{E_L} \cdot 100 = \frac{1.800}{3.487} \cdot 100 = 51{,}6\%$$
$$C_{D,NM} = \frac{E_{PV}}{E_L} \cdot 100 = \frac{3.000}{3.487} \cdot 100 = 86\%$$
$$D_G = \frac{E_{NUN}}{E_L} \cdot 100 = \frac{487}{3.487} \cdot 100 = 14\%$$

Verificación de las relaciones entre índices con los valores del ejemplo:
$$C_{D,NM} \cdot A_{PV} = C_D \Rightarrow 0{,}86 \cdot 0{,}6 = 0{,}516 \;(\checkmark)$$
$$C_{D,NM} + D_G = 86 + 14 = 100 \;(\checkmark)$$

### 6. Perfiles de consumo horario (diapositivas 18-19)

**Tipología de perfiles por tipo de edificio** (diapositiva 18) — cuatro gráficas, cada una con series Laborable/Sábado/Domingo, eje x horas (2-24), eje y consumo normalizado (kW o p.u., escalas distintas por gráfica):

1. **Intensivo mañanas** (colegios y oficinas): pico laborable pronunciado (~3,2, escala propia) en torno a la hora 10; sábado y domingo prácticamente planos y bajos (~0,2-0,5).
2. **Intensivo tardes** (hoteles y restaurantes): laborable con pico ~1,7 hacia las horas 18-20; sábado con forma similar; domingo algo menor en el pico de tarde.
3. **Ininterrumpido** (hospitales, hipermercados, granjas, industrias, etc.): curva relativamente plana entre ~0,9 y ~1,45 a lo largo de todo el día, similar para los tres tipos de día.
4. **Mañana y tarde** (universidades, tiendas, talleres de coches, etc.): perfil bimodal con pico de mañana (~1,9-2,0) y pico de tarde (~1,7-1,8); domingo bajo y plano (~0,6).

Fuente: *Caracterización del autoconsumo fotovoltaico en edificios públicos y comerciales con conexión a red*. Belén Téllez. Trabajo Fin de Máster en Ingeniería de la Energía, UPM.

**Ejemplos de perfiles adicionales** (diapositiva 19) — gráfica consumo (%) vs. Hour (0-23), cuatro series (Residential, Commercial, Optimistic, Pesimistic):

- Residential: valle ~2,6% hacia la hora 4-5; sube gradualmente hasta un pico ~5,9% hacia la hora 21.
- Commercial: meseta ~5,4% entre las horas 10-14; desciende por la noche hasta ~3%.
- Optimistic: mínimo ~0,9% hacia la hora 4; sube con fuerza hasta un pico ~6,6% hacia las horas 13-14, se mantiene alto hasta la hora 20 (~6%).
- Pesimistic: pico temprano ~5,5% en la hora 1; desciende a un mínimo ~2,9% hacia las horas 16-17; repunta a ~5,6% hacia la hora 22.

Fuente: https://learn.ieco.io/es/documentation/consumption/typical-profiles.

### 7. Balance energético con acumulación (diapositivas 20-21) — fórmula canónica relevante para el TFM

Esquema de bloques ampliado respecto al de la sección 5: se añade el bloque "Batería" conectado al bus de continua/alterna, con dos flujos adicionales entre el bus y la batería y una pérdida propia de la batería.

**Definiciones nuevas (diapositiva 20):**
- $E_{TS}$: energía inyectada en la batería (carga).
- $E_{FS}$: energía suministrada por la batería (descarga).
- $E_{SO}$: energía perdida en la batería.

**Ecuación de balance energético con acumulación (fórmula canónica solicitada, preservada literalmente):**
$$E_L = E_{PV} - E_{TUN} - E_{TS} + E_{FS} + E_{FUN}$$

**Desarrollo bajo la hipótesis de que toda la energía de la batería va a la carga** (diapositiva 21):

Pérdida de energía en la batería:
$$E_{SO} = E_{TS} - E_{FS}$$

Energía fotovoltaica autoconsumida directamente (= energía consumida aportada de forma instantánea por fotovoltaica, sin pasar por la batería):
$$E_{AUTO,PV} = E_{PV} - E_{TUN} - E_{TS} = E_L - E_{FUN} - E_{FS}$$

Energía fotovoltaica autoconsumida total (directa + procedente de la batería):
$$E_{AUTO\ TOTAL,PV} = E_{AUTO,PV} + E_{FS} = E_{PV} - E_{TUN} - E_{SO}$$

Porcentaje de autoconsumo (con batería):
$$A_{PV} = \frac{E_{AUTO,PV} + E_{FS}}{E_{PV}} \cdot 100$$

Cobertura de la demanda sin balance neto (con batería):
$$C_D = \frac{E_{AUTO,PV} + E_{FS}}{E_L} \cdot 100$$

No se incluye en la fuente un ejemplo numérico resuelto para el caso con acumulación (a diferencia del caso sin acumulación de las diapositivas 16-17); solo se dan las expresiones simbólicas anteriores. No se completa este vacío con valores de ejemplo propios.

## Datos clave (con página/diapositiva de origen)

- Umbrales de potencia por nivel de tensión de conexión (diapositiva 3): ≤15 kW → 1F BT; ≤100 kW → 3F BT; 100 kW-10 MW → MT; >10 MW → AT.
- Umbrales de potencia por segmento de mercado (diapositiva 4): Residencial <10 kW; Comercial 10-50 kW; Industrial >50 kW.
- Potencia de autoconsumo acumulada en España: 1.539 MW (2020) → 8.137 MW (2024) (diapositiva 6, fuente UNEF).
- Distribución de potencia FV en Europa 2024: Residencial 18%, Comercial e Industrial 37%, Grandes plantas 44%; proyección 2029: 16% / 38% / 46% (diapositiva 7, fuente SolarPower Europe).
- Consumo medio de vivienda en España usado en el ejemplo: $E_L = 3.487$ kWh (diapositiva 16, fuente IDAE, año no legible en el documento).
- Productividad específica asumida para el ejemplo de Madrid: 1.500 kWh/kWp/año (diapositiva 16).
- Resultado completo del ejemplo numérico (2 kWp, Madrid, $A_{PV}=60\%$ supuesto): $E_{PV}=3.000$ kWh; $E_{AUTO,PV}=1.800$ kWh; $E_{FUN}=1.687$ kWh; $E_{TUN}=1.200$ kWh; $E_{NUN}=487$ kWh; $C_D=51{,}6\%$; $C_{D,NM}=86\%$; $D_G=14\%$ (diapositivas 16-17).
- Ecuación de balance sin acumulación: $E_{PV}+E_{FUN}=E_L+E_{TUN}$ (diapositiva 12).
- Ecuación de balance con acumulación (fórmula canónica): $E_L = E_{PV} - E_{TUN} - E_{TS} + E_{FS} + E_{FUN}$ (diapositiva 20).
- Relaciones de verificación entre índices: $C_{D,NM}\cdot A_{PV}=C_D$ y $C_{D,NM}+D_G=100$ (diapositiva 14, verificadas numéricamente en diapositiva 17).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: fundamentalmente el capítulo 7 (dimensionado y estrategia de gestión del sistema de almacenamiento) y, de forma transversal, el capítulo 6 (dimensionado del campo fotovoltaico / autoconsumo), donde se definen y calculan los índices de autoconsumo, cobertura de la demanda y dependencia de la red. Ver `Memoria/indice_propuesto.md`.
- **Qué aporta exactamente**: esta presentación es la fuente docente directa (autoría del propio tutor, Julio Amador Guerra) de la nomenclatura y la ecuación de balance energético **con acumulación**, $E_L = E_{PV} - E_{TUN} - E_{TS} + E_{FS} + E_{FUN}$, junto con las definiciones de $E_{TS}$ (energía inyectada en la batería), $E_{FS}$ (energía suministrada por la batería) y $E_{SO}$ (pérdida en la batería, $E_{SO}=E_{TS}-E_{FS}$). Esta ecuación y esta nomenclatura deberían ser la base formal del modelo horario de Excel del capítulo 7: cada hora del año, el balance debe cuadrar según esta expresión, y los índices $A_{PV}$, $C_D$ y $D_G$ del caso con batería (fórmulas de la diapositiva 21) son los indicadores de resultado que probablemente haya que reportar en el capítulo. El ejemplo numérico resuelto de las diapositivas 16-17, aunque es del caso *sin* batería, fija el patrón de cálculo y de presentación (diagrama con valores + verificación cruzada de relaciones entre índices) que puede replicarse para validar el modelo horario con almacenamiento.
- **Confianza en los datos**: todas las ecuaciones, definiciones de variables, cifras del ejemplo numérico y datos de las gráficas están tomados literalmente de las diapositivas indicadas; ninguno se ha completado con conocimiento general del modelo. El año de la fuente IDAE del dato de consumo medio de vivienda (3.487 kWh) no es legible en el PDF (tapado por un logotipo) y se reporta como tal, sin inventarlo. No es documento citable en el TFM (presentación docente del propio máster, sin ISBN/DOI ni edición formal): solo sirve como apoyo interno, nunca como referencia bibliográfica IEEE.

## Notas de procesamiento

- Documento leído íntegro: 22 diapositivas (22 páginas del PDF), sin omisiones. Densidad Exhaustivo aplicada según encargo (tema clasificado como IMPORTANTE/alta profundidad), sin preguntar a Mario.
- Extraído mediante lectura visual directa del PDF (herramienta `Read` nativa por rangos de páginas: 1-20 y 21-22), no mediante script de texto; todas las ecuaciones, tablas y datos de gráficas se han transcrito a partir de la imagen renderizada de cada diapositiva.
- Discrepancia sin resolver en la propia fuente: la portada (diapositiva 1) y el nombre de archivo indican "Módulo 6", pero el encabezado de todas las diapositivas de contenido y de índice dice "Módulo 5. Autoconsumo fotovoltaico". Se reporta explícitamente, no se asume cuál es el correcto.
- La diapositiva 22 es una repetición exacta de la diapositiva 2 (índice), aparentemente usada como cierre de la presentación; no aporta contenido técnico adicional y no se ha duplicado en este resumen.
- El año de la fuente "I.D.A.E." citada en la diapositiva 16 para el consumo medio de vivienda en España (3.487 kWh) queda parcialmente oculto por el logotipo del máster superpuesto en el PDF; no se ha podido determinar el año exacto y se reporta la limitación en vez de asumir un año.
- No se ha detectado ningún ejemplo numérico resuelto para el caso con acumulación (batería); solo aparecen las expresiones simbólicas de las diapositivas 20-21. Se deja constancia explícita de esta ausencia en la sección de contenido técnico correspondiente.
- Ninguna imagen decorativa (logotipos, fotografías de instalaciones sin datos asociados) se ha descrito en detalle por no aportar contenido técnico.
