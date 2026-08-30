---
title: "Diseño espacial de sistemas fotovoltaicos en edificios"
tipo: presentacion
autor: "Julio Amador Guerra"
anio: 2026
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T1_DisenoEspacial.pdf"
tags: [fotovoltaica, autoconsumo, diseno-espacial, sombras, orientacion, master-erma]
related: []
---

# Diseño espacial de sistemas fotovoltaicos en edificios (Julio Amador Guerra, 2026)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, UPM, 20ª edición 2025-2026. Cubre los criterios geométricos para disponer campos FV en edificios: formas de instalación (BAPV/BIPV), inclinación óptima, distancia entre filas para evitar sombras entre ellas o con obstáculos, protección solar de ventanas mediante lamas FV en fachada, y determinación de la superficie disponible (sombras lejanas/cercanas, antenas, normativa de seguridad contra incendios). Tratado de forma somera (tema no marcado como prioritario por Mario); se han extraído solo los aspectos con valor práctico directo para el dimensionado espacial del campo FV del CPD: fórmulas de separación entre filas, criterio de pérdidas máximas admisibles y disposición de módulos.

## Contenido técnico

### 1. Formas de instalación en edificios (BAPV/BIPV)

- **BAPV** (Building Applied PV, superpuesto): azotea, terraza, superposición sobre tejado/fachada.
- **BIPV** (Building Integrated PV, integrado): tejas FV, mantas solares, ventanas, lucernarios, toldos, marquesinas.
- Pérdidas máximas admisibles por orientación+inclinación y por sombras, respecto a la disposición óptima sin sombras (fuente: IDAE 2011, Pliego de Condiciones Técnicas de Instalaciones Conectadas a Red):

| Disposición | α+β (orientación+inclinación) | Sombras | Total |
|---|---|---|---|
| General (suelo/estructura libre) | 10 % | 10 % | 15 % |
| Superposición sobre cubierta | 20 % | 15 % | 30 % |
| Integración arquitectónica | 40 % | 20 % | 50 % |

### 2. Inclinación óptima y disposición de módulos

- Para Madrid, la inclinación óptima está en el rango **30°-35°**, según curva de irradiación solar anual G(kWh/m²·año) vs. inclinación (fuente AMT-Macagnan-Hay); la curva es plana entre 20°-45° (pérdida de captación pequeña en ese rango).
- Criterios técnicos de disposición: maximizar energía por potencia instalada y maximizar energía por área ocupada (compromiso, no coinciden).
- Disposiciones espaciales de módulos: **1V** (vertical, fila simple), **2V** (vertical, fila doble), **1H** (apaisada/horizontal, fila simple).
- Vertical (retrato) vs. horizontal (apaisado/paisaje): en sombreado parcial, la orientación horizontal reparte el sombreado entre más submódulos con menor pérdida relativa. Ejemplo dado: módulos en vertical con 6 células sombreadas (2 por submódulo) → pérdida de sombreado 21,5 %; módulos en apaisado con 12 células sombreadas (en un solo submódulo) → pérdida de sombreado solo 7,5 %.
- Definición de mesas: N<sub>S_H</sub> (nº de cadenas en horizontal) y N<sub>S_V</sub> (nº de cadenas en vertical); el número de series por mesa debe ser un número entero. La serie eléctrica debe coincidir con la disposición en fila (ejemplo 2×16) para minimizar pérdidas por sombreado, facilitar la conexión/canalización y evitar bucles que induzcan sobretensiones (norma IEC 62548 sobre minimización del área de bucle en el cableado, aplicable tanto a módulos de células enteras como de semi-células).

### 3. Distancia entre filas u obstáculos (núcleo del apartado, máxima relevancia para el TFM)

Fórmula general de distancia horizontal a un obstáculo o fila delantera de altura h:

$$d = \frac{h}{\tan \gamma_S}$$

donde γ_S es el ángulo de altura solar. Regla práctica citada: usando γ_S = 26° → d ≈ 2·h; usando γ_S = 21° → d ≈ 2,5·h (valores de referencia para evitar sombras en la franja horaria ±2h/±3h del mediodía solar, según diagrama de trayectorias solares con líneas D1-D14/A1-A10 en función de acimut y elevación).

**Altura solar en el mediodía del solsticio de invierno** (peor caso de sombras):

$$\gamma_{S} = 90° - |\varphi - \delta|, \quad \delta = -23,45°\ (\text{solsticio de invierno})$$

Tabla de referencia:

| Ciudad | Latitud φ | Altura solar γ_S (mediodía, solsticio invierno) |
|---|---|---|
| Ginebra | 46,5° | 20° |
| Madrid | 40,5° | 26° |
| Cádiz | 36,5° | 30° |

**Separación entre filas sobre suelo/cubierta plana** (módulos inclinados β respecto al plano horizontal), a partir de la longitud del módulo L_m:

$$d_1 = \frac{L_m \cdot \operatorname{sen}\beta}{\operatorname{tg}\gamma_S} \qquad d_2 = L_m \cdot \cos\beta \qquad L_{NS} = d_1 + d_2$$

- d₁: espacio libre entre filas necesario para no sombrear la fila siguiente.
- d₂: proyección horizontal del propio módulo.
- L_NS: separación total entre filas (pitch).
- **Factor de ocupación del terreno (Ground Cover Ratio, GCR)**: $GCR = L_{NS} / L_m$.

Ejemplos numéricos dados en la fuente (L_m = 2 m):
- **Cádiz** (φ=36,5°, β=30°): γ_SI=30° → d₁=1,7 m, d₂=1,7 m, L_NS=3,5 m, GCR=1,7.
- **Ginebra** (φ=46,45°, β=36°, usando γ_SI≈20°): d₁=3,2 m, d₂=1,6 m, L_NS=4,8 m, GCR=2,4.
- Conclusión explícita: a mayor latitud, mayor separación necesaria entre filas para una misma inclinación/longitud de módulo (menor altura solar en invierno).

**Variante para tejados o terrenos inclinados** (inclinación del propio tejado/terreno β_T respecto al plano horizontal):

$$d_1 = \frac{L_m \cdot \operatorname{sen}(\beta-\beta_T)}{\operatorname{tg}(\gamma_S+\beta_T)} \qquad d_2 = L_m \cdot \cos(\beta-\beta_T) \qquad L_{NS}=d_1+d_2$$

- Para cada latitud existe un óptimo inclinación-separación que depende de: energía captada (inclinación óptima vs. pérdidas por sombreado entre filas), coste de la estructura soporte (CTE, velocidad del viento según altura del edificio, efecto "vela": a menor inclinación, menor coste estructural) y superficie utilizada de cubierta/terreno (a mayor superficie, mayor coste para la misma potencia).

### 4. Soluciones constructivas para cubierta plana

- **Sistema T10 (Sunpower)**: estructura triangular de perfil bajo, reduce el efecto vela.
- **Sistema Este-Oeste**: módulos enfrentados formando una "V" invertida sin huecos entre filas. Ventajas: sin pérdidas por sombreado entre filas, mayor densidad de energía por m², diseño aerodinámico (menor contrapeso necesario) y curva de producción diaria más "plana" (mejor ajuste a perfiles de consumo con dos picos, mañana/tarde).
- Ejemplo real: Centro Comercial La Vaguada (Madrid), instalación en azotea con estructura de lastre sobre grava.

### 5. Tejados inclinados y superficies reducidas

- Cubiertas con inclinaciones pequeñas: colocación en fila directamente sobre el faldón, sin necesidad de estructura de inclinación adicional.
- Superposición sobre tejado inclinado: ventajas (estructura soporte reducida, mayor estética, instalación más fácil), inconvenientes (pérdidas respecto a la disposición óptima, pérdidas adicionales por temperatura al no ventilar por la parte trasera, mantenimiento más complejo).
- Ejemplo real: nave industrial 1,9 MWp en Barcos, Navarra.
- Módulos triangulares o de formato recortado para aprovechar superficies irregulares en tejados a dos/cuatro aguas.
- Soluciones ante sombras parciales o poca superficie: **optimizadores de potencia** (uno por módulo, MPPT independiente antes del inversor central; menor coste, mayor rendimiento en sombreado parcial, requieren inversor compatible) y **microinversores** (uno por módulo, conversión DC/AC individual; facilidad de ampliación, todo el cableado en AC, no necesitan inversor central). Tabla comparativa incluida en la fuente (p. 39 aprox.).

### 6. Protección solar de ventanas (lamas FV en fachada)

Geometría para dimensionar voladizos/lamas FV verticales en fachada que dan sombra en verano pero dejan pasar el sol en invierno (o equinoccio):

$$d_A = l_m \cdot \cos\beta \qquad h_1 = l_m \cdot \operatorname{sen}\beta$$
$$h_2 = \frac{d_A}{\operatorname{tg}\theta_{ZE}} \qquad h_2+h_3 = \frac{d_A}{\operatorname{tg}\theta_{ZSV}}$$

donde θ_ZE es el ángulo cenital en el mediodía solar del equinoccio (θ_ZE = φ) y θ_ZSV el del solsticio de verano (θ_ZSV = 90° − γ_SV, con γ_SV = 90° − (φ−δ), δ=+23,45° en verano).

Ejemplos numéricos (l_m = 1,6 m):
- **Ginebra** (φ=46,45°, β=36°): γ_SV=67°, d_A=1,3 m, h₁=0,9 m, h₂=1,2 m, h₃=1,8 m, h₂+h₃=3,1 m.
- **Madrid** (φ=41,45°, β=30°): γ_SV=72°, d_A=1,4 m, h₁=0,8 m, h₂=1,6 m, h₃=2,7 m, h₂+h₃=4,3 m.

### 7. Determinación de la superficie disponible

- **Sombras lejanas**: se evalúan con el diagrama de trayectorias solares y el perfil de horizonte (obtenido p. ej. de la API de PVGIS, "Horizon from PVGIS website"), superponiendo el perfil de obstáculos del entorno sobre las curvas de elevación/acimut solar por meses.
- **Sombras cercanas**: se modelan en 3D (edificios, torres, chimeneas próximas); ejemplo con diagrama de pérdidas anual (informe tipo PVsyst): sombreados cercanos → -15,51 % de pérdida de irradiancia; -9,92 % adicional por sombreados lejanos/horizonte; -2,63 % de pérdida eléctrica por cálculo detallado de módulos sombreados. Cadena completa desde irradiación horizontal global (1671 kWh/m²) hasta energía inyectada a red (9,36 MWh) con todas las pérdidas intermedias desglosadas.
- Ejemplos de estudios de potencial FV con selección entre varias superficies de un mismo edificio (TFM de Samuel Díaz, Universidad Carlos III de Madrid, Campus de Leganés): comparación de potencia instalable en disposición 1H vs. 1V evitando sombras en ±2 h del mediodía del solsticio de invierno (valores de ejemplo: subcampos de 17,3-26,1 kW_p según orientación/disposición).
- Criterios de selección de ubicación del campo FV dentro de una cubierta: captación solar (orientación/inclinación/sombras), integración arquitectónica/impacto visual, optimización del sistema soporte, cercanía al punto de conexión (red de distribución o interior), accesibilidad para montaje y mantenimiento, e interferencia con otros usos de la cubierta.
- Influencia de antenas, cables y otros elementos salientes: se determinan zonas de sombra proyectada sobre el campo FV mediante diagramas de trayectoria solar acimut-elevación superpuestos a la geometría del obstáculo (ejemplo con antenas de TV a 8,20 m de altura).
- **Requisitos normativos de superficie disponible por seguridad** (Reglamento de seguridad contra incendios en establecimientos industriales, fuente: presentación de Pedro Rodríguez Díaz, opra.info, 20/12/2023):
  - Subcampos FV de longitud máxima l ≤ 45 m.
  - Franjas libres entre subcampos: a ≥ 1,2 m.
  - Si la superficie FV total > 500 m²: franja perimetral libre de 1 m de ancho.
  - Alrededor de lucernarios, escotillas de tejado, etc.: distancia mínima de 1 m.
  - Requisitos de acceso en cubiertas inclinadas (fuente: Orange County Fire Marshal Committee): espacio libre de 1 m desde la pared exterior que soporta la carga de fuego, 1 m desde la cumbrera y 0,5 m a cada lado de una limahoya/limatesa; cada faldón con módulos FV necesita dos "caminos" de acceso de al menos 1 m de ancho.

## Datos clave (con página aproximada de origen)

- Inclinación óptima en Madrid: 30°-35° (p. 6).
- Pérdidas máximas admisibles (orientación+inclinación / sombras / total): General 10/10/15 %, Superposición 20/15/30 %, Integración 40/20/50 % (p. 5).
- Fórmula de distancia entre filas/obstáculos: d = h / tg γ_S; reglas prácticas d≈2h (γ_S=26°) y d≈2,5h (γ_S=21°) (pp. 18-19).
- Altura solar mediodía solsticio invierno: Madrid 26° (φ=40,5°) (p. 20).
- Fórmulas GCR y separación entre filas (d₁, d₂, L_NS) en cubierta plana y en tejado inclinado (pp. 22, 25).
- Ejemplo comparativo vertical vs. apaisado ante sombreado parcial: pérdida 21,5 % vs. 7,5 % (p. 8).
- Requisitos normativos de seguridad contra incendios: subcampos ≤45 m, franjas ≥1,2 m, franja perimetral 1 m si superficie >500 m² (p. 56).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo de dimensionado del campo FV (cálculo de la distancia entre filas de las marquesinas/cubierta del CPD) y, en su caso, apartado de justificación de la disposición de módulos (vertical/horizontal) y de la superficie disponible neta tras aplicar los requisitos de seguridad contra incendios.
- **Qué aporta exactamente**: da las fórmulas y el criterio de partida para justificar en la memoria la separación entre filas del campo FV del CPD (d₁, d₂, L_NS, GCR) y para verificar si la disposición del trabajo previo del CPD (referenciado en memoria de Mario) es coherente con el criterio de pérdidas máximas admisibles (15 % para disposición General en suelo/estructura libre, que es el caso más probable del CPD).
- **Confianza en los datos**: todas las fórmulas y valores numéricos son tal como aparecen en la fuente, con su cita de origen cuando la presentación la incluye (IDAE 2011, IEC 62548, PVGIS, TFM de Samuel Díaz, Orange County Fire Marshal Committee). No se han verificado de forma independiente estas cifras; ante cualquier uso directo en el TFM, contrastar con la norma o fuente primaria citada.

## Notas de procesamiento

Densidad Ejecutiva fijada de antemano (no se preguntó a Mario, tal como se indicó en el encargo). Documento de 58 diapositivas revisado íntegramente a nivel de escaneo visual (todas las páginas se han visualizado), pero el resumen se ha limitado deliberadamente a los aspectos de diseño espacial/geométrico (distancias entre filas, sombreado, orientación, superficie disponible) con valor práctico para el TFM, dejando fuera desarrollo exhaustivo de: ejemplos fotográficos repetidos de instalaciones reales, comparativa completa optimizadores/microinversores (solo se cita la existencia y ventajas resumidas), y el detalle completo del diagrama de pérdidas PVsyst de la p. 51 (solo se han extraído las cifras relativas a sombreados). No se ha localizado bibliografía formal (no es documento citable); no lleva Referencia IEEE. Presentación no fechada de forma explícita en portada más allá de "20 EDICIÓN 2025-2026"; año de referencia tomado del propio máster (2026, curso actual).
