---
title: "Proyecto de autoconsumo industrial con almacenamiento en la fábrica de San Martín PYL"
tipo: tfm-referencia
autor: "Manuel Arcas Navarro (cotutores: Jorge Pablo Muñiz Miguel, Julio Amador Guerra)"
anio: 2024
densidad: exhaustivo
fecha_resumen: 2026-08-16
fuente_original: "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Documentacion de apoyo\Ejemplos TFM\TFM_M_A.pdf"
tags: [fotovoltaica, autoconsumo, almacenamiento, baterias, PVsyst, industrial, TFM-referencia, analisis-economico, LCOE, cargas-de-viento]
related: []
---

# Proyecto de autoconsumo industrial con almacenamiento en la fábrica de San Martín PYL (Manuel Arcas Navarro, 2024)

> **Nota de no-citabilidad:** este documento es un TFM de otro autor (Máster ERMA, curso 2023/2024, UPM). No es fuente académica citable en el TFM de Mario Carrión, pero sirve como referencia de estructura, nivel de detalle, metodología de cálculo y formato esperado por el tribunal ERMA, por ser el trabajo más cercano en temática (autoconsumo fotovoltaico industrial con almacenamiento en baterías).

## Resumen

El TFM evalúa la viabilidad técnico-económica de instalar un sistema de autoconsumo fotovoltaico, con y sin almacenamiento en baterías, en la fábrica de placa de yeso laminado (PYL) de PLACO (grupo Saint-Gobain) en San Martín de la Vega (Madrid). Se parte de un consumo eléctrico horario real de 2023 (14,3 GWh/año, potencia media 1635 kW, perfil muy plano por operar 24h/365 días). Se comparan tres configuraciones simuladas en PVsyst (tejado con 2 orientaciones, tejado con 1 orientación, terreno anexo) y se selecciona la de tejado con 2 orientaciones (1.626 kWp) por su mejor relación CAPEX/ahorro, aunque no sea la de mayor autosuficiencia ni la de menor pérdidas. Un modelo horario en Excel para 2023 explora estrategias de carga/descarga de batería (carga de red en periodo barato P6, carga con excedentes FV) y concluye que el almacenamiento **no es rentable** en las condiciones actuales (batería a 120 €/kWh, diferencia de precio P1-P6 de solo ~38%). El análisis económico final (solo FV, sin batería, con financiación 100% propia) arroja payback de 6 años, TIR del 18%, VAN de 1.872.921 € y un ahorro del 13,4% sobre la factura eléctrica a 25 años (~268.695 €/año de media).

## Contenido técnico

### Índice completo del TFM (estructura de referencia)

```
1. Introducción ... 1
2. Objetivos y alcance
   2.1 Objetivos ... 1
   2.2 Alcance ... 2
3. Datos de partida
   3.1 Caracterización de la actividad industrial en San Martín PYL ... 3
   3.2 Consumo de la fábrica ... 4
   3.3 Datos económicos de partida ... 5
   3.4 Recurso solar y elección de base de datos ... 6
   3.5 Restricciones medioambientales ... 8
   3.6 Cargas de viento ... 10
4. Tipología de autoconsumo y selección de componentes
   4.1 Tipo de autoconsumo ... 14
   4.2 Tramitación ... 15
   4.3 Elección de los componentes del sistema
        4.3.1 Módulo fotovoltaico ... 16
        4.3.2 Inversor fotovoltaico ... 17
        4.3.3 Estructura de soporte ... 18
5. Diseño de la planta FV (PVsyst)
   5.1 Áreas, orientaciones e inclinaciones elegidas ... 22
   5.2 Pérdidas detalladas de cada sistema ... 23
        5.2.1 Cálculo del "string" o cadena ... 29
        5.2.2 Ratio DC/AC ... 30
   5.3 Cálculo energético y resultados sin almacenamiento
        5.3.1 Producción FV por kWp instalado ... 31
        5.3.2 Performance Ratio "PR" ... 33
        5.3.3 Percentiles P50 y P90 ... 34
        5.3.4 Diagrama de pérdidas ... 35
6. Diseño del sistema de almacenamiento ... 38
7. Análisis económico ... 46
8. Conclusiones ... 49
Referencias ... 50
Anexos
   Anexo 1: Ficha técnica del módulo fotovoltaico ... 52
   Anexo 2: Ficha técnica del inversor fotovoltaico ... 54
   Anexo 3: Ficha técnica de la estructura ... 57
   Anexo 4: Informe de PVsyst ... 59
```

**Relevancia para Mario:** este índice (8 capítulos + anexos, 51 páginas de memoria + 18 de anexos, ~69 páginas totales de contenido citable) es notablemente más corto que el límite ERMA de 150 páginas y que la estructura de 11 capítulos + anexos de `Memoria/indice_propuesto.md`. Sirve como referencia de "mínimo aceptado", no de objetivo. La secuencia datos de partida → tipología/componentes → diseño PVsyst → almacenamiento → económico → conclusiones es directamente homóloga a los capítulos de dimensionado (PVsyst), almacenamiento y análisis económico del TFM de Mario.

---

### 1. Introducción

El autoconsumo ha crecido por avances tecnológicos, sostenibilidad y cambios legislativos (eliminación del "Impuesto al sol", RD 900/2015, derogado en 2018). A nivel industrial permite reducir costes operativos; la batería mejora autosuficiencia y control del consumo. El trabajo analiza la posibilidad de autoconsumo con o sin almacenamiento en una industria de placa de yeso al sur de Madrid.

### 2. Objetivos y alcance

**Objetivo principal:** mostrar una posibilidad viable de implantar autoconsumo FV con o sin almacenamiento en la fábrica de San Martín PYL para reducir costes eléctricos.

**Objetivos específicos:**
- Analizar el consumo eléctrico de la fábrica y su perfil.
- Estudiar restricciones técnicas o ambientales.
- Elegir los componentes idóneos.
- Estudiar diferentes configuraciones ("layout") y elegir el óptimo.
- Comparar resultados de cada configuración.
- Comprobar la viabilidad económica de baterías.
- Realizar un análisis económico de la configuración elegida.

**Alcance:** análisis de necesidades eléctricas; identificación de superficies disponibles con menor sombreado; elección de componentes (módulos, inversores, estructura, baterías); cálculos eléctricos básicos (sección de cableado, ratio DC/AC, nº de módulos por cadena); simulación de configuraciones en PVsyst con pérdidas óhmicas, sombreado, suciedad y LID; modelo Excel de gestión de batería; modelo económico con CAPEX, O&M y ROI.

### 3. Datos de partida

#### 3.1 Caracterización de la actividad industrial

Fábrica de PLACO (grupo Saint-Gobain) en San Martín de la Vega, en servicio desde 2006, a 2 km de la cantera de mineral de yeso. Proceso: molienda (2 etapas, motores grandes + cintas transportadoras), homogeneizador (puentes grúa "stackers"), calcinación (molino de bolas "Claudius Peters", gas + electricidad), línea de fabricación (mezcla con agua/aditivos, cinta ~200 m), secadero (~150 m, gas natural + motores/ventiladores), take-off (corte, paletizado), y otros consumos (oficinas, laboratorio, carretillas eléctricas). Actividad continua 24h/7 días, con paradas solo por mantenimiento, 25-dic y 1-ene, o incidencias.

#### 3.2 Consumo de la fábrica

Datos horarios reales de 2023 (año considerado representativo). Perfil de carga relativamente constante con tendencias estacionales leves (mayor consumo en invierno/verano por climatización), al menos 5 paradas de actividad productiva durante el año. Perfil diario: consumo superior de 7h a 13h (molienda activa).

- **Consumo medio de potencia 2023:** 1635 kW (valores máximos > 2000 kW).
- **Consumo total anual 2023:** 14.302.338 kWh (según Tabla 27, factura); 14.327.821 kWh según balance de PVsyst (E_User); 14.327.815 kWh según Tabla 25 (consumo anual de la fábrica usado en LCOE). Estas pequeñas discrepancias entre tablas del documento original no se han reconciliado — se documentan tal como aparecen en la fuente.
- Coste factura total 2023: 2.005.187,79 €.

**Tabla — Consumo y coste mensual 2023 (Ilustración 7):**

| Mes | Consumo (kWh) | Coste factura (€) |
|---|---|---|
| Enero | 1.331.777 | 186.715,14 |
| Febrero | 1.107.802 | 155.313,84 |
| Marzo | 1.254.900 | 175.936,98 |
| Abril | 1.227.808 | 172.138,68 |
| Mayo | 1.106.228 | 155.093,17 |
| Junio | 1.211.773 | 169.890,57 |
| Julio | 1.285.094 | 180.170,18 |
| Agosto | 1.253.606 | 175.755,56 |
| Septiembre | 1.208.211 | 169.391,18 |
| Octubre | 1.145.844 | 160.647,33 |
| Noviembre | 1.074.741 | 150.678,69 |
| Diciembre | 1.094.554 | 153.456,47 |
| **TOTAL** | **14.302.338** | **2.005.187,79** |

#### 3.3 Datos económicos de partida

Fábrica conectada a red de alta tensión, tarifa **6.XTD** (6 periodos, a diferencia de las tarifas de baja tensión con 3 periodos).

**Tabla 1 — Coste eléctrico por periodo:**

| P1 (€/kWh) | P2 (€/kWh) | P3 (€/kWh) | P4 (€/kWh) | P5 (€/kWh) | P6 (€/kWh) |
|---|---|---|---|---|---|
| 0,177366 | 0,171598 | 0,157384 | 0,143582 | 0,12875 | 0,124218 |

El periodo depende de hora, mes y día de la semana (tabla horaria completa por mes en Ilustración 5, fuente [1] Energigreen). Se generó un CSV con estos criterios para importar en PVsyst.

#### 3.4 Recurso solar y elección de base de datos

PVsyst dispone de 3 bases de datos: NASA-SSE (americana, más pesimista), Meteonorm y PVGIS (europeas). Comparando la radiación global de las tres, **Meteonorm se aproxima más a la media** de las 3 (PVGIS es más optimista, NASA más pesimista) → se elige Meteonorm.

Irradiación horizontal global anual en la ubicación (Meteonorm): **1741 kWh/m²/año**, con pico en junio-julio (~230-240 kWh/m²) y mínimo en diciembre-enero (~60-65 kWh/m²).

**Tabla 2 — Parámetros técnicos de la BBDD de Meteonorm:**

| Parámetro | Descripción |
|---|---|
| Fuentes de datos | Estaciones meteorológicas, satélites, modelos climáticos |
| Cobertura temporal | Desde 1980 hasta el presente, promedios 10-30 años |
| Cobertura espacial | Global, >8.000 estaciones meteorológicas, interpolación |
| Resolución espacial | ~30 km × 30 km |
| Resolución temporal | Horaria (interpolada), diaria (promedios), mensual (promedios) |
| Variables principales | Irradiancia solar global (directa/difusa), humedad relativa, velocidad del viento, radiación UV, presión atmosférica |
| Método de generación | Interpolación espacial/temporal, corrección satelital/modelos locales |
| Actualización | Meteonorm 8, datos hasta 2020 |

#### 3.5 Restricciones medioambientales

La cubierta de la fábrica no tiene restricción medioambiental. El terreno cercano (parcelas catastrales 199, 200, 202 y 1, Polígono 10, Chorrero, Valdemoro, Madrid — parcela 202: 33.518 m², suelo rústico agrario) requeriría recalificación a uso industrial (memoria justificativa). Verificación con visor Red Natura 2000: el terreno no está dentro de zonas de especial protección (las vegas del Jarama y Manzanares, con 56 especies protegidas de aves, están próximas pero no afectan). Herramienta MITECO para FV (comprobación de núcleos urbanos, masas de agua, especies amenazadas, ZEPA, LIC/ZEC, espacios naturales protegidos, humedales RAMSAR, reservas de biosfera, Camino de Santiago, vías pecuarias, Patrimonio UNESCO): **resultado positivo, sin restricciones excluyentes**.

#### 3.6 Cargas de viento (Código Técnico de la Edificación, DB-SE-AE)

**Ecuación de presión estática del viento:**

$$q_e = q_b \cdot c_e \cdot c_p$$

Donde:
- $q_b$: presión dinámica del viento.
- $c_e$: coeficiente de exposición (varía con altura y aspereza del entorno).
- $c_p$: coeficiente eólico o de presión (negativo = succión).

**Cálculo de $q_b$:** zona de estudio corresponde a la Zona A del mapa de zonas de viento de España (Ilustración 14, fuente CTE) → $q_b = 0,42\ kN/m^2$.

**Cálculo de $c_e$:** grado de aspereza del entorno nivel II (terreno rural llano sin obstáculos). Según Tabla 3.4 del CTE:
- Instalación en cubierta (h=12 m): $c_e = 2,9$
- Instalación en terreno (h=3 m): $c_e = 2,1$

**Cálculo de $c_p$:**
- **Cubierta** (a un agua, pendiente 5°, área > 10 m²): excluyendo zonas de borde (F, G), $c_p = -0,8$. (La cubierta del almacén es a dos aguas pero el coeficiente resultante es menos restrictivo, se usa el valor ya calculado).
- **Terreno** (marquesina a un agua, pendiente 30°, efecto del viento hacia arriba/succión, factor de obstrucción $\phi=0$): $c_p = -3,6$.

**Tabla 3 — Cargas de viento calculadas:**

| | $q_b$ (kN/m²) | $c_e$ | $c_p$ | $q_e$ (kN/m²) |
|---|---|---|---|---|
| En cubierta | 0,42 | 2,9 | -0,8 | -0,94 |
| En terreno | 0,42 | 2,1 | -3,6 | -3,17 |

Estos valores de carga estática (a succión) se usan después para validar la estructura de soporte (apartado 4.3.3).

### 4. Tipología de autoconsumo y selección de componentes

#### 4.1 Tipo de autoconsumo

Autoconsumo **individual, en alta tensión (AT)**, un único consumidor, conectado en red interior (generación en baja tensión). Se decide **sin excedentes** (instalando dispositivo anti-vertido) para facilitar trámites y evitar solicitud de punto de acceso/conexión (caro y difícil en instalaciones > 100 kW). Tipología CNMC: **31-A** (REN-CO-Res, individual, sin excedentes, red interior, esquema de medida real tipo A). Funcionamiento "Dependiente" (necesita la red, no opera aislado). Esquema de conexión: **Esquema 12** (Individual, sin excedentes, generación Ren-Co-Res y mismo titular por red interior, CPMC + CT interior, varios trafos, 100 < Pg ≤ 4000 kW, Pic ≤ 4000 kVA).

#### 4.2 Tramitación (según RD 244/2019 de 5 de abril)

- **Previo a construcción:** proyecto técnico visado (solo si conexión en AT), autorización administrativa previa y de construcción, trámite municipal de licencia de obras.
- **Posterior a construcción:** inspección OCA (cada 3 años en AT, 5 en BT), certificado fin de obra, boletín eléctrico, autorización de explotación (potestativo CCAA), contrato técnico de acceso, inscripción en registro.
- **Puesta en marcha.**

Se decide sin excedentes: no se pide punto de acceso/conexión (>15 kW requiere solicitud, >100 kW requiere aval), no se hace compensación de excedentes (no permitida >100 kW) ni venta a mercado — el excedente, si lo hay, se destina a cargar baterías.

#### 4.3 Elección de componentes

**4.3.1 Módulo fotovoltaico** — Comparativa de 4 fabricantes, mismos 605 Wp:

| Característica | JA SOLAR JAM78-S30-605-MR | Canadian Solar HiKu7 Mono PERC | Trina TSM-DE20-605 | Jinko Solar JKM-605N-78HL4-V |
|---|---|---|---|---|
| Potencia pico STC (Wp) | 605 | 605 | 605 | 605 |
| Tecnología de célula | Mono PERC Half-Cut | Mono PERC Half-Cut | Mono Half-Cell | Mono N-Type Half-Cut |
| Peso (kg) | 31,1 | 28,2 | 30,9 | 30,6 |
| Dimensiones (mm) | 2465×1134 | 2172×1303 | 2172×1303 | 2465×1134 |
| Coef. temperatura potencia (%/°C) | -0,35 | -0,34 | -0,34 | -0,3 |
| Eficiencia (%) | 21,6 | 21,4 | 22,8 | 21,6 |
| Garantía potencia (años) | 25 | 12 | 25 | 30 |
| Garantía producto (años) | 12 | 25 | 12 | 12 |
| Protección salinidad/amoniaco | Sí/Sí | Sí/Sí | Sí/Sí | Sí/Sí |
| Precio (€/Wp) | 0,16 | 0,19 | 0,15 | 0,18 |

Comparativa gráfica tipo radar (5 ejes: coeficiente potencia-temperatura, eficiencia, precio, tamaño, garantías) → **módulo elegido: Trina TSM-DE20-605** (mejor combinación en las categorías medidas).

**4.3.2 Inversor fotovoltaico** — Comparativa de 3 marcas para gran potencia:

| Característica | Ingecon Sun 1500TL U B578 | Power Electronics Frame 3-FS-1251_H | SMA Sunny Central UP 2200 |
|---|---|---|---|
| Potencia nominal AC (kVA) | 1502 | 1250 | 2200 |
| Rendimiento máximo (%) | 98,9 | 98,6 | 98,6 |
| Rendimiento europeo (%) | 98,5 | 98,4 | 98,4 |
| Nº entradas DC | 15 | 40 | 24 |
| Intervalo DC seguim. máx. potencia (V) | 822-1300 | 520-820 | 570-950 |
| Intensidad máxima DC (A) | 1870 | 2500 | 3600 |
| Tensión nominal AC (V) | 578 | 330 | 385 |
| Peso (kg) | 1710 | 4500 | (dimensiones 2780×2318×1588 mm, peso no indicado en ficha) |
| Limitación alta Tª (°C) | 57 | 50 | 60 |
| Precio (€/W) | 0,300 | 0,250 | 0,350 |
| Garantía (años) | 5, ampliable a 25 | 5, ampliable a 25 | 5, ampliable a 25 |

Comparativa radar (eficiencia, operatividad alta Tª, precio, garantías, rango tensión MPP, peso) → **inversor elegido: Ingecon Sun 1500TL U B578**, por competitividad y buena adaptabilidad al campo FV (curva I-V confirma compatibilidad de tensiones/corrientes del conjunto FV con los límites del inversor: $V_{mpp,min}$≈822V, $V_{mpp,max}$≈1300V, $I_{max,CC}$≈2700A).

**4.3.3 Estructura de soporte** — Perfiles de aluminio cortos anclados a chapa grecada (tornillos/remaches), módulos en horizontal fijados con pinzas al lado largo. Comparativa de 3 fabricantes:

| | Fischer | Novotegra | Sunfer |
|---|---|---|---|
| Precio (€/módulo) | 18,9 | 12,8 | 13,8 |
| Resistencia fijación | Remache | Tornillo autorroscante | Tornillo autorroscante |
| Adaptabilidad | Menor, remache | Mayor, tornillos | Mayor, tornillos |
| Durabilidad | Buena, 12 años garantía | Buena, 10 años garantía | Peor (montaje en valle de greca), 10 años garantía |
| Componentes | Pinza, perfil, remache, cinta EPDM | Pinza, perfil (junta EPDM incluida), tornillo | Pinza, perfil (junta EPDM incluida), tornillo |

→ **Estructura elegida: Novotegra** (más competitiva en precio, menor nº de componentes al incluir cinta EPDM integrada, montaje en la parte alta de la greca → menos problemas de humedad que Sunfer).

**Comprobación de cargas de viento sobre la estructura elegida:**

Datos del tornillo Novotegra: a=25 mm, b=6 mm, c=16 mm. Según tabla de cargas recomendadas a extracción en chapa de acero (Tabla 6, ficha técnica Index) para tornillo ST 6.3 con espesor de chapa e=1 mm (interpolado): carga recomendada ≈ 1 kN por tornillo.

- Cada módulo se soporta con 8 tornillos (2 por cada uno de los 2 perfiles).
- $Q$ (carga aplicada sobre el módulo) $= -0,94\ kN/m^2 \times (2,172 \times 1,303)\ m^2 = -2,66\ kN$
- $Q_{max}$ (carga máxima) $= -1\ kN/tornillo \times 8\ tornillos = -8\ kN$
- Como $|Q| < |Q_{max}|$, la situación es favorable con margen amplio.

### 5. Diseño de la planta FV (PVsyst)

#### 5.1 Áreas, orientaciones e inclinaciones elegidas — 3 sistemas comparados

| | Sistema 1 (tejado, 2 orientaciones) | Sistema 2 (tejado, 1 orientación) | Sistema 3 (terreno) |
|---|---|---|---|
| Inclinación | 5° | 5° | 36° (óptima) |
| Orientación (norte=0°) | 242° y 62° | 242° | 180° (sur) |
| Disposición | Horizontal | Horizontal | Horizontal |
| Módulos por cadena | 28 | 28 | 28 |
| Potencia instalable | 1,6 MWp (1.626 kWp) | ~1 MWp (1.055 kWp) | ~3 MW (3.405 kWp) |

- **Sistema 1:** aprovecha toda la superficie del tejado (desviado 62° del sur, inclinación 5°); es la opción "conservadora" pero no óptima de aprovechamiento solar.
- **Sistema 2:** una única orientación, mejora el rendimiento un 1,5% frente al Sistema 1, pero instala menos potencia (~1 MW).
- **Sistema 3:** instalación en terreno (parcela oeste de la fábrica), inclinación óptima 36°, orientación sur 0°, mejora el rendimiento ~20% respecto a los sistemas 1 y 2; requeriría estructura fija y adquisición del terreno (mayor CAPEX).

#### 5.2 Pérdidas detalladas — pérdidas generales (comunes a los 3 sistemas)

- **Suciedad:** ubicación árida, actividad industrial de yeso (polvo). Se toma referencia de estudio norteamericano [8] (Kimber et al., 2006 IEEE WCPEC) en ubicación rural/desértica: **5% anual** respecto a la producción global. Se recomiendan 2 limpiezas anuales coincidiendo con paradas de mantenimiento.
- **Efecto LID (Light Induced Degradation):** módulos de silicio monocristalino, degradación inicial ~2% según fabricante, degradación anual del 0,53% (Trina), tomándose la mitad (0,252%) por considerarse lineal a lo largo de la vida útil.
- **Pérdidas por "mismatch":** 2% general.
- **Indisponibilidad:** 2% anual = 7,3 días/año, distribuidos en 3 periodos.
- **Pérdidas óhmicas** (calculadas solo para el sistema de 2 orientaciones, 1.626 kWp, 2688 módulos en 96 cadenas de 28 módulos, agrupadas en 12 cajas colectoras "Combiner box" de 8 cadenas cada una; tramo cadena-caja en cobre, tramo caja-inversor en aluminio):

**Tabla 7 — Datos de partida cálculo del cableado:**

| Parámetro | Valor |
|---|---|
| Potencia por cadena | 16.940 W |
| Intensidad por cadena | 17,6 A |
| Intensidad por caja | 141 A (17,6×8) |
| Voltaje por cadena y por caja | 980 V |
| Longitud máxima línea de Cu | 30 m |
| Longitud máxima línea de Al | 220 m |
| Resistividad Cu a 90°C | 0,023 Ω·mm²/m |
| Resistividad Al a 90°C | 0,036 Ω·mm²/m |

Cálculo según ITC-BT-14 y BT-15 (REBT), objetivo de caída de tensión combinada Cu+Al < 1,5%.

**Sección tramo Cu** (caída de tensión considerada 0,5% en este tramo):

$$S = \frac{\rho \cdot 2 \cdot L \cdot I}{\Delta U}$$

$$S = \frac{0,023 \times 2 \times 30 \times 17,6}{0,005 \times 980} = 4,95\ mm^2 \Rightarrow \text{cable comercial } S=6\ mm^2$$

**Sección tramo Al:**

$$S = \frac{0,036 \times 2 \times 220 \times 141}{0,01 \times 980} = 227,9\ mm^2 \Rightarrow \text{cable comercial } S=240\ mm^2$$

**Caída de tensión total con cables elegidos:**

$$\Delta U = \Delta U_{Cu} + \Delta U_{Al} = \frac{0,023 \times 2 \times 30 \times 17,6}{6} + \frac{0,036 \times 2 \times 220 \times 141}{240} = 13,35\ V$$

$$\Delta U\% = \frac{13,35}{980}\times100 = 1,36\%\ (< 1,5\%)$$

**Tabla 8 — Cantidad de cable necesario:**

| Parámetro | Valor |
|---|---|
| Cable 6 mm² aprox. por cadena | 15 m |
| Cable 240 mm² aprox. por caja | 100 m |
| Nº cables por circuito | 2 (+ y -) |
| Cable total 6 mm² | 2×15×96 = 2.880 m |
| Cable total 240 mm² | 2×100×12 = 2.400 m |

Esquema unifilar: 12 cajas colectoras de 8 cadenas cada una → inversor central (15 entradas disponibles, 3 quedan libres).

**Pérdidas específicas:**

- **Desorientación (Tabla 9):**

| | Sistema 1 | Sistema 2 | Sistema 3 |
|---|---|---|---|
| Pérdidas respecto al óptimo | 19,2% | 15,4% | 0% (orientación e inclinación óptimas) |

- **Sombreados cercanos (solo Sistema 3, terreno):** criterio de que en el solsticio de invierno (21 dic, UTC+1) no haya sombreado al mediodía solar (13h).

$$\gamma_s = 90 - \alpha - \Phi = 90 - 23,5 - 40,2 = 26,3°$$

Donde $\gamma_s$ = elevación solar máxima 21-dic; $\alpha$ = inclinación eje terrestre (23,5°); $\Phi$ = latitud (40,2°).

Separación mínima entre filas:

$$d_{min} = b \cdot \frac{\sin(\gamma_s+\beta)}{\sin \gamma_s}$$

Con $b$ = longitud del módulo en la fila (2 módulos en vertical: $b=2\times2,172+0,06=4,4\ m$), $\beta$=36° (inclinación):

$$d_{min} = 4,4 \times \frac{\sin(26,3+36)}{\sin(26,3)} = 8,8\ m$$

Simulación por lotes en PVsyst (sensibilidad PR / pérdidas por sombreado vs. pitch): a partir de pitch=11-12 m, la mejora de PR y reducción de pérdidas se estabiliza → se toma **Pitch = 12 m > 8,8 m** (margen de seguridad). Con este pitch se confirma sin sombreados el 21-dic al mediodía. Pérdida de haz lineal por sombreado: 3,6% en solsticio de invierno, 0,3% en solsticio de verano y equinoccio (Sistema 3).

- **Sombreados cercanos Sistemas 1 y 2 (tejado):** chimenea de la prezona (leve, primeras horas de mañana en invierno) y edificio de calcinación (a partir de las 16h, sombras importantes sobre la mayoría de módulos). Pérdida de haz lineal: 2,3% (solsticio invierno), 0,1% (verano), 0,4% (equinoccio).

#### 5.2.1 Cálculo del "string" o cadena

**Tabla 10 — Datos de módulo:** $I_{sc}$=18,57 A; $V_{oc}$=41,7 V; 28 módulos en serie; 96 cadenas en paralelo.

**Tabla 11 — Datos del inversor:** $V_{max}$=1500 V; $V_{MPPmin}$=822 V; $V_{MPPmax}$=1300 V; $I_{max}$=2700 A; $P_{max}$=1953 kWp.

**Tabla 12 — Datos eléctricos del conjunto:**

| Parámetro | Valor | Límite |
|---|---|---|
| $V_{OCserie}$ | 28×41,7 = 1167 V | < 1300 V |
| $I_{MAXconjunto}$ | 96×18,57 = 1782 A | < 2700 A |
| $P_{conjunto}$ | 1.626 kWp | < 1.953 kWp |

#### 5.2.2 Ratio DC/AC (sobredimensionamiento)

$$R_{DC-AC} = \left(\frac{Potencia_{pico}}{Potencia_{nominal\,inversor}} - 1\right) \times 100$$

Curva de eficiencia del inversor: si la potencia de entrada DC baja de 25% de la nominal, la eficiencia decrece. Simulación por lotes de PVsyst (sistema 2 orientaciones) variando nº de cadenas: la energía útil generada crece linealmente con el sobredimensionamiento; las pérdidas por limitación de potencia crecen linealmente; las pérdidas por limitación de intensidad son nulas hasta ~15% de sobredimensionamiento y crecen rápido hasta 25%.

$$R_{DC-AC} = \left(\frac{1626}{1352}-1\right)\times100 = 20,3\%$$

Valor elegido por límite de superficie de tejado disponible; pérdidas por intensidad/potencia contenidas a este nivel; valor típico según referencia del distribuidor Amara [13].

#### 5.3 Cálculo energético y resultados sin almacenamiento

**Tabla 13 — Producción específica de cada sistema:**

| Sistema | Pérdidas por colección (kWh/kWp/día) | Pérdidas del sistema (kWh/kWp/día) | Energía útil producida (kWh/kWp/día) |
|---|---|---|---|
| 1 (1.626 kWp) | 0,92 | 0,11 | 3,76 |
| 2 (1.055 kWp) | 0,93 | 0,14 | 3,79 |
| 3 (3.405 kWp) | 1,12 | 0,13 | 4,29 |

Sistema 3 tiene más pérdidas por sombreado pero mayor producción específica por su orientación/inclinación óptimas; su gráfica mensual es más plana (menor pico en verano, mayores valores en invierno). Sistemas 1 y 2 muy similares, ligera ventaja para el 2.

**Tabla 14 — Performance Ratio (PR) — valor medio anual:**

| Sistema | PR |
|---|---|
| 1 | 0,784 |
| 2 | 0,780 |
| 3 | 0,775 |

$$PR = \frac{E_{real}}{E_{teórica}} = \frac{E_{real}}{G \cdot A \cdot \eta_{STC}}$$

El Sistema 1 (2 orientaciones) obtiene el **mejor PR**. En todos los sistemas el PR cae en verano por reducción de voltaje con altas temperaturas.

**Tabla 15 — Percentiles P50 y P90 (producción anual):**

| Sistema | P50 (MWh) | P90 (MWh) |
|---|---|---|
| 1 | 2233 | 2106 |
| 2 | 1458 | 1376 |
| 3 | 5332 | 5030 |

(P50 = mediana/escenario más probable; P90 = 90% probabilidad de superarlo, escenario conservador para financiación).

**Tabla 16 — Diagrama de Sankey de pérdidas (resumen numérico extraído del Anexo 4, Sistema 1 — 2 orientaciones):**

| Etapa | Valor |
|---|---|
| Irradiación horizontal global | 1741 kWh/m² |
| Sombreados cercanos: pérdida de irradiancia | -0,63% |
| Factor IAM en global | -3,42% |
| Factor de pérdida de suciedad | -5,00% |
| Irradiancia efectiva en colectores | 1596 kWh/m² × 7607 m² colect. |
| Eficiencia en STC | 21,38% |
| Conjunto de energía nominal (con efic. STC) | 2.595.828 kWh |
| Pérdida FV debido a nivel de irradiancia | -0,77% |
| Pérdida FV debido a temperatura | -6,32% |
| Pérdida de calidad de módulo | +0,50% |
| LID - Degradación inducida por luz | -2,00% |
| Pérdidas de desajuste, módulos y cadenas | -2,15% |
| Pérdida óhmica del cableado | -0,98% |
| Pérdida por mezcla de orientación | -0,03% |
| Energía virtual del conjunto en MPP | 2.302.453 kWh |
| Pérdida del inversor durante la operación (eficiencia) | -1,47% |
| Pérdida del inversor por umbral de potencia/voltaje | -0,08% |
| Consumo nocturno | -0,02% |
| Energía disponible en la salida del inversor | 2.266.359 kWh |
| Indisponibilidad del sistema | -1,49% |
| **Despacho: al usuario desde red / al usuario desde solar / a la red** | **12.171.122 / 2.156.699 / 75.844 kWh** |

**Tabla 17 — Resultados de autosuficiencia y autoconsumo:**

| Sistema | Autoconsumo | Autosuficiencia |
|---|---|---|
| 1 | 96,60% | 15,05% |
| 2 | 98,09% | 9,98% |
| 3 | 79,49% | 29,58% |

A mayor potencia instalada, mayor autosuficiencia (menor dependencia de la red) pero menor autoconsumo (más excedentes no consumidos in situ).

**Tabla 18 — Resumen de la instalación FV elegida:**

| Parámetro | Valor |
|---|---|
| Disposición | Sistema 1, 2 orientaciones, instalado en tejado |
| Potencia pico | 1.626 kWp |
| Ratio DC/AC | 20,3% |
| Generación FV anual | 2.156.699 kWh (Tabla 18) / 2.232.543-2.232.903 kWh según otras tablas del documento (discrepancia de la fuente entre "energía entregada al usuario desde solar" y "producida"; no reconciliada, reportada tal cual) |
| Consumo anual | 14.304.338 kWh |
| Autoconsumo | 96,60% |
| Autosuficiencia | 15,05% |
| Inversor | Ingecon Sun 1500TL U B578 |
| Módulo | Trina TSM-DE20-605 |
| Configuración | 12 cajas (Combiner Box) de 8 cadenas cada una, 28 módulos por cadena, 2.688 módulos en total |

### 6. Diseño del sistema de almacenamiento

Coste de batería considerado: **~120 €/kWh almacenado**. Modelo horario en Excel (8.760 filas, año 2023) con producción FV a salida de inversor (de PVsyst), consumo horario real, coste eléctrico por periodo.

**Estrategias estudiadas para cada sistema:**

- **Sistema 1 (1626 kWp) y Sistema 2 (1055 kWp):**
  - *Carga de red:* la batería se carga solo de la red en el periodo más barato (P6) y se descarga en el periodo más caro (P1 y P2). Diagrama lógico: si periodo=P6 y hay capacidad libre → cargar 10%/hora hasta máximo; si periodo=P1 o P2 y batería >10% de carga → descargar 10%/hora hasta 10% de carga; en otros periodos, mantener capacidad.
  - *Carga fotovoltaica:* la producción FV se destina a cargar la batería cuando está en periodo "barato" (P4, P5 o P6) y hay capacidad, el resto al consumo; en periodos "caros" (P1, P2, P3) se descarga la batería al consumo si hay capacidad disponible.

- **Sistema 3 (3405 kWp, terreno):** al ser suficientemente grande como para generar excedentes reales, la energía se destina primero al consumo y los excedentes se envían a la batería, que se descarga en el periodo P1.

**Tabla 19 — Datos para el cálculo del sistema con almacenamiento:**

| Parámetro | Valor |
|---|---|
| Vida útil instalación (años) | 12 |
| Eficiencia de la batería (RTP) | 89% |
| Capacidad considerada (kWh) | 5000 |
| Tasa de carga/descarga | 0,1C (10%/hora) |
| Carga máxima | 95% |
| Carga mínima | 10% |
| Autodescarga | 2% mensual (no considerada — ciclos diarios) |
| Coste instalación FV (€/Wp) | 0,7 |
| Coste batería (€/kWh) | 120 |

Vida útil de baterías 12 años (optimista) → requiere 1 recambio a mitad de la vida útil de la instalación FV (25 años). Capacidad de batería 5.000 kWh equivalente a un contenedor industrial de 20 pies.

**Columnas relevantes de la hoja Excel (Ilustración 47):** A=fecha; B=hora; C=periodo tarifario; D=coste (€/kWh); E=consumo eléctrico horario (kWh); F=producción FV a salida de inversor (kWh, de PVsyst); G=energía comprada de la red sin batería (=E−F, o 0); J=capacidad de la batería a nivel horario; K=energía entregada por el sistema FV+batería; L=energía comprada a la red con batería; N=gasto horario sin batería (G×D); O=gasto horario con batería (L×D).

**Tabla 20 — Comparativa de ahorros (25 años):**

| Sistema | Estrategia | Gasto base sin batería (€) | Gasto anual con batería (€) | Ahorro en 25 años con batería (€) | Ahorro en 25 años solo FV (€) |
|---|---|---|---|---|---|
| 2 orientaciones | Carga de FV | 1.692.164,29 | 1.752.289,86 | 4.046.768,35 | 6.749.907,56 |
| 2 orientaciones | Carga de red | | 1.681.527,46 | 5.815.828,16 | |
| 1 orientación | Carga de FV | 1.797.853,63 | 1.839.648,45 | 2.262.503,45 | 4.507.373,91 |
| 1 orientación | Carga de red | | 1.785.552,58 | 3.614.900,21 | |
| En terreno | Carga de excedentes FV | 1.381.206,96 | 1.355.714,10 | 12.715.862,25 | 14.923.540,71 |

Gasto anual sin FV (base): **2.007.688,59 €**.

**Tabla 21 — Comparativa de costes (CAPEX):**

| Sistema | CAPEX solo fotovoltaica | CAPEX fotovoltaica + batería |
|---|---|---|
| 2 orientaciones | 1.138.200,00 € | 2.338.200,00 € |
| 1 orientación | 738.500,00 € | 1.938.500,00 € |
| En terreno | 2.383.500,00 € | 3.583.500,00 € |

**Conclusión del capítulo 6:** en todos los casos resulta más rentable NO instalar batería y usar solo FV. El caso "en terreno sin batería" es el más rentable en términos absolutos, pero su CAPEX es muy elevado y no incluye costes de adquisición de terreno ni tramitación → se descarta. **Se elige el sistema de 2 orientaciones sin batería** por generar mayor ahorro con CAPEX más contenido.

**Exploración de estrategias de descarga de batería (sensibilidad):**

| Estrategia de descarga | Ahorro (sistema 2 orientaciones, carga de red) |
|---|---|
| Descargando en P1 | 5.778.226,95 € |
| Descargando en P1 y P2 | 5.815.826,16 € (óptimo) |
| Descargando en P1, P2 y P3 | 5.664.165,32 € |

Descargar solo en P1 infrautiliza la batería; descargar en P1+P2+P3 satura la batería en P2/P3 y deja poca capacidad para P1 (el periodo más favorable). El óptimo es **descargar en P1 y P2**.

**Motivos de la no rentabilidad de la batería:**
1. El consumo de la fábrica es muy superior a la producción FV incluso en los meses de mayor producción (subdimensionamiento FV por limitación de espacio en tejado).
2. Diferencia de precio entre P1 y P6 de solo **38% (~47 €/MWh)** — insuficiente para compensar el coste de la batería. El documento cita [14] que modelos con arbitraje batería rentable requieren diferencias valle-punta de ~100 €/MWh o hasta 300%.
3. Alto coste actual de la batería (120 €/kWh).

Se advierte (fuente [15], pv magazine) que se pronostica una caída del precio de baterías del 50% para 2030, lo que podría cambiar la conclusión y merecería un estudio de sensibilidad futuro.

### 7. Análisis económico

Aplicado a la configuración elegida: **Sistema 1, 2 orientaciones, 1.626.000 Wp, sin batería**.

**Tabla 22 — Costes supuestos:**

| Módulos (€/Wp) | Inversor (€/W) | Estructura (€/módulo) | BOP (€/Wp) | Mano de obra (€/Wp) | Mantenimiento (€/año) |
|---|---|---|---|---|---|
| 0,15 | 0,3 | 12,8 | 0,2 | 0,15 | 5.700 |

**Tabla 23 — Datos de partida para el cálculo económico:**

*Parámetros económicos:* tasa interés 5%; inflación 2%; periodo devolución deuda 5 años; periodo de amortización 25 años; contingencia 25%; tasa de descuento 5%; IVA 21%; coste O&M 4 €/kW; otros costes 0 €/kW; seguro anual 4 €/kW; peajes 0 €/MWh.

*Inversión:* CAPEX 1.232.000 €; DEVEX 50.000 €; **inversión total 1.282.000 €** (100% propia, 0% externa); IVA inversión 269.220 €; desembolso 0 €; amortización 51.280 €.

*Parámetros técnicos:* potencia instalada 1.616 kW (dato de tabla, ligeramente distinto de 1.626 kWp usado en otras secciones — inconsistencia de la fuente); horas equivalentes de producción 1.381 h; producción anual de energía 2.232.000 kWh.

*Ahorros:* ahorro bruto 0,142 €/kWh.

**Supuestos del cálculo (25 años, flujo de caja anual):**
- Inversión 100% con fondos propios.
- Cada kWh producido por el sistema FV supone un ahorro bruto de 0,142 €/kWh (coste medio del kWh comprado de la red en 2023).
- Degradación anual de 0,25%/año (mitad de la degradación anual del módulo) reduce la producción y el ahorro cada año hasta el año 25 (fin de vida útil).
- Contingencia del 25% aplicada sobre el beneficio tras impuestos, para permisos, reposición de equipos e imprevistos.
- IVA 21% sobre el CAPEX.

**Tabla 24 — Resultados financieros del proyecto:**

| Indicador | Valor |
|---|---|
| Período de retorno (Payback) | 6 años |
| Inversión total | 1.282.000 € |
| LCOE | 0,023 €/kWh |
| VAN | 1.872.921 € |
| TIR | 18% |

**Cálculo del LCOE final combinado (Tabla 25):**

| Parámetro | Valor |
|---|---|
| LCOE_red (coste de comprar energía de la red) | 0,142 €/kWh |
| C (consumo anual de la fábrica) | 14.327.815 kWh |
| P (producción fotovoltaica anual) | 2.232.903 kWh |
| E_red (energía comprada de la red, instalando FV) | 12.171.121 kWh |
| LCOE_FV (coste del kWh que sale del sistema FV) | 0,023 €/kWh |

$$LCOE_{final} = \frac{LCOE_{red}\cdot E_{red} + LCOE_{FV}\cdot P}{C} = 0,123\ €/kWh$$

**Tabla 26 — Ahorro conseguido:**

| LCOE_red | LCOE_final | Ahorro |
|---|---|---|
| 0,142 €/kWh | 0,123 €/kWh | 13,4% |

**Tabla 27 — Ahorro mensual y anual con instalación FV (año promedio):**

| Mes | Consumo (kWh) | Coste factura sin FV (€) | Coste factura con FV (€) | Ahorro anual con FV (€) |
|---|---|---|---|---|
| Enero | 1.331.777 | 186.715,14 | 161.695,31 | 25.019,83 |
| Febrero | 1.107.802 | 155.313,84 | 134.501,79 | 20.812,05 |
| Marzo | 1.254.900 | 175.936,98 | 152.361,42 | 23.575,56 |
| Abril | 1.227.808 | 172.138,68 | 149.072,10 | 23.066,58 |
| Mayo | 1.106.228 | 155.093,17 | 134.310,68 | 20.782,48 |
| Junio | 1.211.773 | 169.890,57 | 147.125,24 | 22.765,34 |
| Julio | 1.285.094 | 180.170,18 | 156.027,37 | 24.142,80 |
| Agosto | 1.253.606 | 175.755,56 | 152.204,32 | 23.551,25 |
| Septiembre | 1.208.211 | 169.391,18 | 146.692,76 | 22.698,42 |
| Octubre | 1.145.844 | 160.647,33 | 139.120,59 | 21.526,74 |
| Noviembre | 1.074.741 | 150.678,69 | 130.487,74 | 20.190,94 |
| Diciembre | 1.094.554 | 153.456,47 | 132.893,30 | 20.563,17 |
| **TOTAL** | 14.302.338 | 2.005.187,79 | 1.736.492,62 | **268.695,16 €** |

### 8. Conclusiones (texto íntegro resumido)

- Consumo eléctrico muy plano (poca variación), lo que en un principio hacía pensar que el almacenamiento sería interesante para desplazar excedentes a horas nocturnas.
- Meteonorm elegida por aproximarse mejor a la media de las 3 bases de datos de PVsyst.
- No existen restricciones medioambientales relevantes en la zona de estudio; las cargas de viento se calculan según CTE para dimensionar la estructura con seguridad.
- Componentes elegidos: módulo **Trina 605 W**, inversor **Ingecon**, estructura **Novotegra**.
- Tipología de autoconsumo: sin excedentes, red interior, individual, energía renovable, AT, con varios centros de transformación.
- De los 3 sistemas comparados (2 orientaciones, 1 orientación, terreno), el **sistema en terreno** tiene más pérdidas por sombreado pero mejor orientación; el **sistema de 2 orientaciones** consigue mejor PR (0,784), autoconsumo del 96% y autosuficiencia del 15% → **es el elegido**, por mejor aprovechamiento de la cubierta y por evitar la adquisición del terreno. Solo ~4% de excedentes (instalación subdimensionada respecto al consumo), lo que confirma que no interesa vender excedentes a red.
- String/cadena: 28 módulos por cadena; sobredimensionamiento DC/AC óptimo: **20,3%**.
- Producción eléctrica anual simulada: **2233 MWh (confianza 50%)** o **2106 MWh (confianza 90%)**.
- Sistema de almacenamiento: ninguna estrategia de carga/descarga (excedentes, generación FV, electricidad de red) produce más ahorro a 25 años que la instalación FV sin batería. Causas: alto coste actual de baterías, subdimensionamiento FV respecto al consumo de la fábrica, pequeña diferencia de precios entre P1 y P6 (solo 30-38%).
- Análisis económico de la configuración elegida (2 orientaciones, sin batería, 100% fondos propios): **payback ~6 años, TIR 18%, VAN > 1.800.000 €, ahorro anual medio > 250.000 €**. Se concluye que el sistema es técnicamente eficiente y financieramente rentable bajo las condiciones actuales.

### Anexos (contenido técnico relevante)

**Anexo 1 — Ficha técnica módulo Trina Vertex TSM-DE20 (backsheet monocristalino, rango 585-605W):**
- Potencia pico máxima: 605 W (0~+5W tolerancia positiva); eficiencia máxima 21,4%.
- Datos eléctricos STC (para 605W): $V_{oc}$=41,7 V; $I_{sc}$=18,57 A (según cuerpo del TFM); tabla de la ficha muestra también valores para 585-610W.
- Dimensiones: 2172×1303×35 mm; peso 30,6 kg (cuerpo del texto) / ficha indica 30,7 kg aprox.
- Coeficiente de temperatura de potencia: -0,34%/°C; NOCT 43°C(±2°C).
- Garantía producto 12 años; garantía de potencia 25 años, degradación anual 0,55% (ficha) / 0,53% citado en el cuerpo del texto — leve discrepancia entre cuerpo y ficha técnica, reportada tal cual.
- Tensión máxima del sistema: 1500V DC (IEC); fusible serie máximo 30A.
- Certificaciones: IEC 61215/61730, ISO 9001/14001/45001, CE.

**Anexo 2 — Ficha técnica inversor Ingecon Sun Storage PowerMax U B Series (1500 Vdc), familia completa 1170TL-1640TL:**
- Modelo usado: **1500TL U B578**. Potencia AC a 77°F/122°F: 1.502 kVA/1.251 kVA.
- Rango de tensión de batería: 917-1.300 V; tensión máxima 1.500 V; corriente máxima 2.004 A.
- Rendimiento máximo 98,9%; CEC 98,5%.
- Funciones de gestión de batería: Energy Time Shifting (inyección nocturna de energía solar almacenada), Ramp Rate Control, Peak-shaving, Frequency Regulation, Active Power Reserve, Digital Q Compensation.
- Protecciones: descargadores tipo 2, interruptor DC motorizado, monitorización de fallo de aislamiento, protección anti-isla, interruptor AC.
- Rango de temperatura ambiente: -4°F a +131°F; altitud máx. 6.562 ft (2.000 m); estándares EMC/seguridad: UL9540, UL1741, IEC 62109, entre otros.

**Anexo 3 — Ficha técnica estructura Novotegra (sistema de pinzas para cubierta de chapa trapezoidal):**
- Componentes premontados: pinza intermedia/final (para marco de módulo 30-42 mm y 43-52 mm), rail corto (con EPDM preconfeccionado y trama perforada), protección antideslizante del módulo, tornillo de fijación a chapa sin arranque de viruta.
- Variantes: rail corto C24 (económica) y C47 (mayor ventilación posterior del módulo).

**Anexo 4 — Informe completo de simulación PVsyst v7.4.6 (Sistema 1, 2 orientaciones, 1626 kWp):**

- Sitio: SN_PYL_meteonorm, España. Latitud 40,21°N; longitud -3,62°W; altitud 620 m; UTC+1; albedo 0,20.
- Meteonorm 8.1 (2005-2017), Sat=52%, sintético.
- PV Field: 2 orientaciones fijas, tilt/azimut 5°/62° y 5°/-118°.
- Sombreados cercanos: lineal (tabla rápida).
- 2.688 módulos, 1.626 kWp; 1 inversor, 1.352 kWac; Pnom ratio (DC/AC) 1,203 (nota: 1,203 según informe PVsyst vs. 1,20 en tabla anterior del cuerpo del texto — pequeña discrepancia de redondeo).
- **Resultados resumen (Results summary):** energía producida 2.232.543 kWh/año; energía usada (consumo) 14.327.821 kWh/año; producción específica 1.373 kWh/kWp/año; PR 78,44%; fracción solar (SF) 15,05%.
- **Producción mensual (GlobHor, GlobInc, EArray, E_User, E_Solar, E_Grid, EFrGrid) — tabla completa PVsyst (kWh, salvo GlobHor/GlobInc en kWh/m²):**

| Mes | GlobHor | GlobInc | T_Amb (°C) | EArray (kWh) | E_User (kWh) | E_Solar (kWh) | E_Grid (kWh) | EFrGrid (kWh) |
|---|---|---|---|---|---|---|---|---|
| Enero | 64,1 | 65,1 | 6,01 | 86.662 | 1.331.789 | 82.229 | 2.863 | 1.249.560 |
| Febrero | 86,2 | 87,4 | 7,51 | 119.926 | 1.107.911 | 109.194 | 2.707 | 998.606 |
| Marzo | 138,1 | 139,3 | 11,14 | 189.669 | 1.256.638 | 182.314 | 4.504 | 1.074.323 |
| Abril | 172,7 | 173,2 | 13,86 | 234.498 | 1.227.891 | 226.891 | 4.152 | 1.000.859 |
| Mayo | 204,9 | 205,0 | 18,75 | 271.333 | 1.105.910 | 243.105 | 24.310 | 862.806 |
| Junio | 226,3 | 226,0 | 24,40 | 291.953 | 1.211.688 | 283.523 | 4.305 | 928.290 |
| Julio | 240,3 | 240,4 | 27,84 | 304.578 | 1.285.262 | 294.781 | 5.554 | 990.481 |
| Agosto | 215,5 | 212,2 | 27,17 | 271.111 | 1.253.387 | 237.079 | 9.545 | 1.016.308 |
| Septiembre | 157,7 | 158,6 | 22,04 | 207.726 | 1.208.327 | 199.243 | 5.491 | 1.009.084 |
| Octubre | 111,6 | 112,8 | 16,58 | 150.752 | 1.144.093 | 140.884 | 7.562 | 1.003.210 |
| Noviembre | 71,7 | 73,0 | 9,86 | 97.477 | 1.076.685 | 86.327 | 2.428 | 990.358 |
| Diciembre | 55,7 | 56,8 | 4,80 | 74.947 | 1.118.490 | 71.128 | 2.422 | 1.047.362 |
| **Año** | **1740,8** | **1750,2** | 16,03 | **2.300.653** | **14.327.821** | **2.156.699** | **75.844** | **12.171.122** |

- **Loss diagram** (idéntico al reportado en Tabla 16 del cuerpo, con valores absolutos): irradiación horizontal 1741 kWh/m² → +0,5% global incidente → -0,63% sombreados cercanos → -3,42% IAM → -5,00% suciedad → irradiancia efectiva 1596 kWh/m²·7607 m² colect. → eficiencia STC 21,38% → energía nominal 2.595.828 kWh → -0,77% nivel irradiancia, -6,32% temperatura, +0,50% calidad módulo, -2,00% LID, -2,15% mismatch, -0,98% óhmicas, -0,03% mezcla orientación → energía virtual MPP 2.302.453 kWh → -1,47% eficiencia inversor, -0,08% umbral voltaje, -0,02% consumo nocturno → energía disponible salida inversor 2.266.359 kWh → -1,49% indisponibilidad → despacho: 12.171.122 kWh al usuario desde red, 2.156.699 kWh al usuario desde solar, 75.844 kWh a la red.
- **P50-P90 evaluation:** variabilidad global (datos meteo + sistema) 4,4%; P50=2233 MWh; P90=2106 MWh; P95=2071 MWh; variabilidad absoluta 98 MWh. Incertidumbres consideradas: modelado módulo FV 1,0%; eficiencia inversor 0,5%; suciedad/mismatch 1,0%; degradación 1,0%.
- **Single-line diagram:** 28×TSM-DE20-605 por string (8 strings) → 30 m cable → Combiner×12 → 100 m → Combiner → 500 m → inversor 1352 kVA → punto de inyección (medida kWh).

## Datos clave (con página de origen)

- Consumo eléctrico fábrica 2023: 14.302.338 kWh/año, potencia media 1635 kW, tarifa 6.XTD 6 periodos (p. 4-5).
- Coste eléctrico por periodo P1-P6: 0,177366 / 0,171598 / 0,157384 / 0,143582 / 0,12875 / 0,124218 €/kWh (p. 5).
- Base de datos climática elegida: Meteonorm, irradiación 1741 kWh/m²/año (p. 6-7).
- Cargas de viento CTE: $q_e$=-0,94 kN/m² en cubierta, -3,17 kN/m² en terreno (p. 13).
- Módulo elegido: Trina TSM-DE20-605, 605 Wp, eficiencia 21,4-22,8%, coef. temp -0,34%/°C (p. 16, Anexo 1 p. 52-53).
- Inversor elegido: Ingecon Sun 1500TL U B578, 1502 kVA, rendimiento máx. 98,9% (p. 17, Anexo 2 p. 54-56).
- Estructura elegida: Novotegra, sistema de pinzas (p. 18-19, Anexo 3 p. 57-58).
- Sistema elegido: 2 orientaciones (tejado), 1.626 kWp, 2.688 módulos, 96 cadenas de 28, ratio DC/AC 20,3% (p. 22-30, 37).
- Producción anual FV: 2.232.543-2.232.903 kWh (P50); 2.106.339 kWh (P90); PR 78,4%; autoconsumo 96,6%; autosuficiencia 15,05% (p. 31-37, Anexo 4 p. 60-68).
- Almacenamiento en batería: NO rentable en ninguna estrategia estudiada (carga red P6/descarga P1-P2, carga FV, carga con excedentes); capacidad batería modelada 5000 kWh, coste 120 €/kWh (p. 38-45).
- CAPEX solo FV (2 orientaciones): 1.138.200 € (sin IVA) / inversión total 1.282.000 € (con DEVEX e IVA) (p. 41, 46).
- Resultados financieros: payback 6 años, LCOE FV 0,023 €/kWh, VAN 1.872.921 €, TIR 18% (p. 47).
- LCOE combinado (red + FV): 0,123 €/kWh vs. 0,142 €/kWh sin FV → ahorro 13,4% (p. 47).
- Ahorro anual medio: 268.695,16 € (p. 48).
- Normativa/fuentes citadas: RD 900/2015 (impuesto al sol, derogado 2018), RD 244/2019 (tramitación autoconsumo), CTE DB-SE-AE (cargas de viento), ITC-BT-14/BT-15 REBT (cableado), esquema CNMC 31-A / esquema de conexión 12 (UFD grupo Naturgy) (p. 1, 10-13, 14-15, 25).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta:** capítulo de dimensionado FV/PVsyst (metodología de comparación de configuraciones, cálculo de string, ratio DC/AC, pérdidas), capítulo de diseño del sistema de almacenamiento (estructura de modelo horario en Excel, diagramas lógicos de carga/descarga, análisis de sensibilidad de estrategias), capítulo de análisis económico (estructura de CAPEX, LCOE combinado red+FV, VAN/TIR/payback), y como referencia de estructura/extensión general del documento.
- **Qué aporta exactamente:** ejemplo completo y trazable de metodología de cálculo de cargas de viento (CTE), dimensionado de cableado DC (ITC-BT-14/15), cálculo de sobredimensionamiento DC/AC óptimo, criterio de separación entre filas por sombreado (fórmula del solsticio de invierno), y —de especial interés para el caso de Mario (CPD con demanda constante 24/7, similar al perfil "muy plano" de esta fábrica)— una demostración razonada de por qué el almacenamiento puede NO ser rentable cuando el diferencial de precio entre periodos tarifarios es bajo y la instalación FV está subdimensionada respecto al consumo. Este resultado es un contraste útil a validar/contrastar con el caso específico del CPD de Mario (que puede tener otro perfil tarifario y otro ratio FV/consumo).
- **Confianza en los datos:** todas las cifras provienen literalmente del PDF original (texto, tablas e ilustraciones descritas), con página de origen indicada. Se han señalado explícitamente las pequeñas discrepancias internas del documento original (p.ej. consumo anual 14.302.338 vs. 14.327.821/14.327.815 kWh según la tabla; potencia instalada 1.616 vs. 1.626 kWp; producción anual 2.156.699 vs. 2.232.543/2.232.903 kWh) tal como aparecen en la fuente, sin resolverlas ni completarlas con criterio propio.

## Notas de procesamiento

- Documento de 75 páginas PDF (69 páginas de contenido numerado + portada/índices sin numerar). Se leyó el **100% del documento, sin muestreo**, en 4 tramos de páginas (1-20, 21-40, 41-60, 61-75), dado el nivel de densidad EXHAUSTIVO solicitado explícitamente y la relevancia del documento como TFM de referencia más cercano.
- Las imágenes/gráficas (mapas, esquemas de conexión eléctrica, capturas de PVsyst, radares comparativos, fotos de estructuras) se han descrito textualmente (ejes, tendencias, contenido) pero no se han podido representar visualmente en este resumen Markdown.
- Se detectaron varias inconsistencias numéricas menores dentro del propio documento original entre distintas tablas que deberían coincidir (consumo anual, potencia instalada, producción anual FV) — se han señalado explícitamente en el resumen en cada caso, sin intentar resolverlas.
- Las referencias bibliográficas [1]-[15] del TFM original se han mencionado en el cuerpo del resumen donde son relevantes, pero no se han verificado ni se reproducen como bibliografía propia (este documento no es citable).
