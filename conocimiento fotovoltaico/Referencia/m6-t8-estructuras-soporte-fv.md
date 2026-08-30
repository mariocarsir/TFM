---
title: "Módulo 6 - Autoconsumo Fotovoltaico: Estructuras Soporte"
tipo: presentacion
autor: "Francisco Javier Hernández Plaza (Sales Manager, LONGI)"
anio: 2026
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T8_EstructuraSoporte.pdf"
tags: [fotovoltaica, autoconsumo, estructura-soporte, anclaje, cubierta, suelo, flotante, master-erma]
related: [trabajo-previo-modulo6-cpd]
---

# Módulo 6 - Autoconsumo Fotovoltaico: Estructuras Soporte (Hernández Plaza, 2026)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición 2025-2026, impartida por Francisco Javier Hernández Plaza (LONGI), sobre estructuras soporte de instalaciones FV. Clasifica las soluciones de mercado en tres grandes bloques según su cuota aproximada de aplicación: tejado/cubierta (~85%), suelo fijo (~10%) y agua/flotante (~5%), y detalla para cada uno los sistemas de anclaje típicos, la normativa de referencia (CTE) y un ejemplo de síntesis de cálculo estructural. Insiste en la importancia de la planificación, la adaptabilidad de la estructura a superficies no coplanares y la profesionalidad del instalador para evitar micro-fallos que comprometan la garantía del producto. Cierra con ejemplos de software comercial de diseño/cálculo de estructuras (Sunfer, Van der Valk/Ezzing, Schletter Creator). Documento eminentemente práctico y visual, orientado a instalación, con poco desarrollo analítico de cargas.

## Contenido técnico

### 1. Introducción a la estructura soporte
- Esquema conceptual de 3 capas: módulo fotovoltaico → conexión/sujeción → estructura soporte → conexión/sujeción → superficie fija.
- Alcance laboral de la instalación: A) montaje eléctrico, B) montaje mecánico (objeto de esta presentación), C) obras civiles/albañilería.
- Clasificación por tipo de superficie y cuota de mercado aproximada en autoconsumo:
  - Tejados (coplanar/inclinado, industrial/teja/plano): **~85%**
  - Suelo fijo (cimentación superficial/profunda, hincado mono/biposte, tornillo): **~10%** (suelo con seguimiento 1-2 ejes se reserva a *utility scale*, fuera del foco de autoconsumo)
  - Agua (flotante): **~5%**
- Características principales exigidas a la estructura: durabilidad, rápido ensamblaje, rápida instalación/sustitución de módulos, **adaptabilidad** (ninguna superficie de apoyo real está en el mismo plano), resistencia y seguridad conforme a códigos y legislación.
- Selección de solución = material + condicionantes: ubicación, ángulo de inclinación (coplanar = módulo y superficie de apoyo paralelos; inclinada = no paralelos), velocidad de viento y carga de nieve (acciones/códigos de construcción), tipo/tamaño/peso/tecnología del módulo, tipología del tejado, estudio geotécnico y topografía del suelo.

### 2. Normativa de aplicación y síntesis de cálculo
- Acciones consideradas en el cálculo estructural: uso/conservación (personas), viento, nieve, y carga permanente (peso propio del material de cubierta + instalaciones fijas, incluyendo módulos FV + estructura soporte); esta sobrecarga permanente es **normalmente < 12 kg/m²**, de ahí la recomendación de un "estudio de sobrecarga" previo.
- Marco normativo citado: CTE (Código Técnico de la Edificación, RD 314/2006, última modificación RD 732/2019), que remite a la LOE (Ley 38/1999) para los requisitos básicos de seguridad estructural; también se citan Eurocódigo, normas UL/BS u otros criterios propios según el caso.
- Debate abierto sobre la obligatoriedad de aplicar el CTE a una instalación FV sobre cubierta existente: la presentación concluye que la exigibilidad depende del contexto (pliegos públicos/privados, exigencia contractual, trámites de licenciamiento, o simplemente criterio del técnico competente como referencia válida), no de una obligación universal directa.
- Síntesis de cálculo (ejemplo en tejado, con combinaciones de carga según DIN 1055, coeficientes parciales de seguridad γ_g≈1,22/0,9 y γ_q≈1,35/0,5-0,6): se evalúan 3 combinaciones (peso propio+carga dominante+viento; peso muerto+aire+nieve; peso muerto+remolino de viento) y se exige que, para la combinación más desfavorable, la tensión de trabajo del material sea inferior a su tensión máxima y la deformación (flecha) sea inferior a la máxima admisible en barras/módulos.
- Mismo esquema de verificación se repite para suelo-hincado y suelo-cimentación superficial, con comprobación adicional de resistencia, vuelco y deslizamiento de la zapata (fórmula de verificación tensional N/A + M/W_y ≤ f_d).

### 3. Anclaje de módulos
- El manual de instalación del fabricante define ángulo de inclinación, ventilación, limpieza y tipo de sujeción (tornillo o pinza/clamp); advertencia explícita: **no perforar el marco del módulo** (reduce capacidad de carga y puede provocar corrosión).
- Puntos de anclaje típicos: cargas de ensayo normalizadas front 5400 Pa / back 2400 Pa (según nivel de carga bajo/alto); distancia de pinza típica **D = ¼ L** (regla práctica).
- Simplificación estructural del marco del módulo como viga isostática biapoyada (Ley de Hooke): acercar los apoyos hacia el interior de los extremos reduce el esfuerzo cortante máximo (qL/2), el momento flector máximo (qL²/8) y la flecha (5qL⁴/384EI), lo que se traduce en menos micro-fallos y mejor garantía de producto.
- Normas de ensayo de módulo referenciadas: DIN EN 61215 (cristalino) y DIN EN 61646 (capa fina); cargas de ensayo típicas 2400 Pa (obligatoria IEC 61215) o 5400 Pa (opcional).

### 4.1 Soluciones en cubierta/tejado
- **Coplanar en teja**: sistema tornillo (~95% de las instalaciones sobre teja) frente a sistema salvatejas/gancho (~5%); en material cerámico/hormigón se ancla con perforación + taco químico + inyección + inclusión de barrilla (curado 15-20 min) + sellante.
- **Coplanar/inclinado en tejado industrial (chapa/sandwich)**: anclaje directo en greca (parte superior o "agua" de la greca) o anclaje en subestructura (correas), con carriles y optimización del número de carriles por módulo (objetivo: menos de 2 carriles por módulo).
- **Inclinado en tejado industrial**: normalmente de 10° a 30°, con modalidades de apoyo tipo FixE/FixT en acero o madera.
- **Coplanar en tejado plano**: subestructura habitualmente de hormigón armado; acabados en baldosa cerámica, hormigón, grava o cubierta ajardinada; se evita perforar mediante sistemas contrapesados.
- **Sistemas contrapesados en tejado plano**: reparto de lastre por zonas (ejemplo con módulos de zona: 67,0 / 51,2 / 29,8 / 16,3 kg según posición), definición de estructura/tamaños, replanteo y juntas de dilatación (máx. recomendado ~30 m entre juntas); productos tipo bloque de hormigón prefabricado (p.ej. Solarbloc, ángulos 10°/12°/15°/18°) en triángulo abierto o cerrado.
- **Fachadas**: montaje inclinado/coplanar vertical con adaptador universal M8 y perfiles tipo Eco05.
- Mensaje transversal: "ninguna superficie de apoyo se encuentra en el mismo plano" → la adaptabilidad de la estructura y la profesionalidad del instalador son más determinantes que el cálculo teórico puro.

### 4.2 Soluciones en suelo
- **Poste hincado**: inserción directa del poste metálico con martillo perforador; sistema muy usado a escala utilitaria; no aplicable a arena suelta de baja cohesión ni a zonas con alta presencia de agua; requiere ensayo geotécnico (carga vertical y horizontal, composición/pH del suelo) para calcular la profundidad de hinca; instalación rápida y de bajo impacto ambiental.
- **Cimentación de hormigón** (prefabricada o in situ): recomendada donde no se puede hincar (rellenos sanitarios inactivos, roca madre); impacto ambiental bajo; debe dimensionarse frente a deslizamiento y vuelco.
- Tipologías por composición de módulos (1V-2V-3V / 2H-3H-4H-5H-6H), por número de apoyos (monoposte/biposte/triposte) y por sistema de apoyo (hincado/cimentación/atornillado).
- Tolerancias de ejecución del fabricante (ejemplo Schletter): inclinación este-oeste y norte-sur ±3°, torsión ±5°, desviación en planta ±30 mm, y tolerancias de hasta 100-200 mm frente a variaciones topográficas del terreno.
- Casos de "resultados inadecuados" mostrados como advertencia: falta de alineamiento y de adaptabilidad de los postes, cimentaciones deficientes con excavación irregular y postes descalzados.

### 4.3 Soluciones en agua (flotante)
- Ubicaciones típicas: balsas de riego, balsas industriales, presas y embalses, plantas hidroeléctricas, plantas de tratamiento de aguas, lagos naturales, balsas mineras o terrenos inundables.
- Ventajas señaladas: aprovechamiento de superficie disponible sin ocupar suelo, incremento de producción FV (por refrigeración) y reducción de la evaporación del embalse.
- Componentes del sistema flotante (fuente: isifloating): módulos de 60/72 células, flotador modular de HDPE-UV con inclinación de 5°, alta flotabilidad (240 kg por panel FV, 95 kg/m²), velocidad máxima de viento soportada 180 km/h; flotador secundario para pasillos de mantenimiento, salida de cables y soporte de inversores de string.
- Parámetros de diseño a definir: delimitación de contornos (coronación, caminos de servicio, nivel máximo de explotación), elementos de protección (vallados, muretes), profundidad máxima, pendiente de taludes, perfil topográfico del fondo, entradas/salidas de agua, variación de niveles (diseño/máximo/media), altura máxima de ola y corrientes.

### 5. Software de diseño y cálculo
- Herramientas comerciales citadas como ejemplo (sin desarrollo de uso): Sunfer Project / Selector Sunfer / MyEnstall (sunferenergy.com), Van der Valk / Ezzing (projectTool), y Schletter Creator (schletter-group.com).

## Datos clave (con página/minuto de origen)
- Reparto por tipología de superficie en autoconsumo: cubierta ~85%, suelo fijo ~10%, agua ~5% (p. 6).
- Sobrecarga permanente típica de módulos + estructura sobre cubierta: normalmente **< 12 kg/m²** (p. 12).
- Sistema de anclaje coplanar en teja: tornillo ~95% de instalaciones vs. salvatejas ~5% (p. 27).
- Distancia de pinza de sujeción del módulo: regla práctica **D = ¼ L** (p. 20).
- Cargas de ensayo de módulo: 2400 Pa (compulsory, IEC 61215) / 5400 Pa (opcional) (p. 22).
- Sistema flotante: 240 kg de flotabilidad por panel, 95 kg/m², viento máximo soportado 180 km/h, inclinación 5° (p. 73).
- Norma de referencia para la obligatoriedad de cálculo estructural en cubierta: CTE (RD 314/2006, mod. RD 732/2019), remitiendo a LOE (Ley 38/1999) (p. 13-14).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo de definición constructiva del sistema FV (estructura soporte), y transversalmente al capítulo de dimensionado si se opta por instalación en cubierta plana del CPD (ver `Memoria/indice_propuesto.md`).
- **Qué aporta exactamente**: catálogo somero de tipologías de estructura soporte y criterios de selección (cubierta plana con contrapesos siendo la opción más probable para el CPD dada la cubierta central de 102 kWp ya referenciada en el trabajo previo); recuerda que la sobrecarga permanente admisible en cubierta (~12 kg/m²) es un dato a verificar contra el estudio estructural específico del edificio del CPD, no un valor genérico aplicable sin más. Este tema fue marcado por Mario como de prioridad baja, por lo que este resumen ejecutivo no sustituye un análisis normativo de cargas CTE si la fase de diseño lo requiriera.
- **Confianza en los datos**: cifras y porcentajes tal como aparecen en las diapositivas de un proveedor comercial (LONGI); no son cifras normativas oficiales sino estimaciones de mercado del ponente — usar como orientación, no como cifra canónica citable.

## Notas de procesamiento

Densidad Ejecutiva fijada de antemano (prioridad baja según clasificación de Mario). Documento de 80 páginas leído en su totalidad para localizar la estructura (todas las páginas fueron abiertas), pero el resumen omite deliberadamente, por tratarse de material repetitivo o puramente fotográfico sin dato técnico adicional: la mayoría de las fotografías de "ejemplos de obra" y "resultados inadecuados" (solo se referencian como advertencia cualitativa), los enlaces a vídeos de YouTube incrustados en varias diapositivas, y el despiece detallado de piezas/pares de apriete de los ejemplos de cálculo (se cita el método pero no cada tornillo). No se ha desarrollado el cálculo CTE de cargas de viento/nieve más allá de lo expuesto en las diapositivas, conforme al encargo de análisis somero.
