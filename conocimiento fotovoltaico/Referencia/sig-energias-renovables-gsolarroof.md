---
title: "SIG y Energías Renovables: gSolarRoof"
tipo: presentacion
autor: "Javier Domínguez Bravo (CIEMAT, grupo gTIGER)"
anio: "Sin fecha (Máster ERMA, edición 2025-2026)"
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T13_SistemasInformacionGeografica.pdf"
tags: [fotovoltaica, autoconsumo, sig, gis, teledeteccion, lidar, pvgis, catastro, cartografia, gsolarroof]
related: []
---

# SIG y Energías Renovables: gSolarRoof (Javier Domínguez Bravo, CIEMAT — Máster ERMA Módulo 6, ed. 2025-2026)

## Resumen
Presentación de Javier Domínguez Bravo (grupo gTIGER, CIEMAT) dentro del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, que introduce los Sistemas de Información Geográfica (SIG) aplicados a energías renovables y detalla el modelo gSolarRoof para estimar el potencial fotovoltaico de tejados en entornos urbanos a partir de nubes de puntos LIDAR y modelos digitales de superficie. Recorre las fuentes de datos geográficos abiertos disponibles en España (IGN/PNOA-LIDAR, Catastro, PVGIS, ADRASE-CIEMAT, IDEs autonómicas), la tecnología LIDAR y sus aplicaciones, la metodología de cálculo de gSolarRoof (orientación, inclinación, sombras, accesibilidad de tejados) y varios casos de aplicación (Alpedrete, polígonos industriales de Don Benito/Plasencia, La Habana, Orcasitas). Cierra con ejemplos de TFM tutorizados por el grupo gTIGER-CIEMAT en esta línea, uno de ellos cotutorizado por Julio Amador Guerra (el mismo tutor del TFM de Mario).

## Contenido técnico

### 1. Grupo gTIGER y contexto (p. 3-6)
1. CIEMAT investiga en fotovoltaica, eólica, biocombustibles, solar térmica, desalación, microrredes, biomasa, gasificación, minihidráulica y eficiencia (p. 3).
2. gTIGER (Grupo de Tecnologías de la Información Geográfica y Energías Renovables): aplica las TIG para mejorar cuantitativa y cualitativamente la integración de renovables mediante mejor conocimiento de recursos, planificación energética y adecuación a la demanda. Líneas de investigación: energía rural, autoconsumo urbano, hibridación (p. 4).
3. Financiación de proyectos gTIGER: programas Interreg España-Portugal, Cooperación Española, colaboraciones con Naturgy e idealista, Ministerio de Transportes/Instituto Geográfico Nacional, universidad UE23, ayuntamientos como Alpedrete (p. 5).
4. IntiGIS: SIG para electrificación rural y generación descentralizada en países en desarrollo, con cálculo de LEC (coste de electrificación equivalente) por tecnología (fotovoltaica, minirred, diésel, eólico-diésel, central diésel) (p. 6).

### 2. Mapa nacional de capacidad de hibridación de renovables (p. 7-9)
1. Variables geográficas usadas, con fuente y escala/resolución (tabla, p. 7): límites administrativos y poblaciones (IGN), líneas de deslinde del Dominio Público Marítimo-Terrestre y zonas inundables (MITECO, 1:25.000), hidrografía (IGN, 1:25.000), red viaria/ferroviaria y aeropuertos (IGN/AENA, 1:5.000-1:100.000), Red Natura 2000/espacios protegidos/humedales RAMSAR/reservas de biosfera (MITECO, 1:50.000), vías pecuarias (MITECO), CORINE Land Cover y líneas eléctricas/subestaciones (IGN, 1:100.000), irradiación solar (ADRASE-CIEMAT a 5.000 m y ERA5-Copernicus a 0,25°/1.000 m), velocidad del viento (ERA5-Copernicus, 0,25°/1.000 m), modelo digital del terreno y pendientes (IGN, 200 m), sensibilidad por presencia de aves (SEO/BirdLife).
2. Dos aproximaciones metodológicas (p. 8): (1) mapa de aptitud basado en revisión de literatura científica, primera visión del potencial peninsular y Baleares, resultados optimistas (TFM + artículo + story map); (2) mapa de capacidad basado en lógica difusa + primer modelo de rentabilidad (flujo: ArcGIS Pro/Python → suitability map → algoritmo → profitability map → sensibility analysis).
3. Evolución del proyecto (p. 9): revisión en profundidad de la literatura sobre evaluación de emplazamientos para sistemas híbridos; 3 simulaciones basadas en indicadores económicos soportadas en Python; 3 tesis de máster defendidas (España e Italia) con la máxima calificación; 2 artículos publicados en revistas de impacto; base de datos geográfica actualizada. Próximos pasos: análisis horario, simulación de recurso eólico/solar de alta resolución espacio-temporal con adaptación del modelo WRF, desarrollo de un visor de mapas.

### 3. ¿Qué son los SIG? (p. 12-14)
1. Definición (National Center for Geographic Information and Analysis, NCGIA): "un sistema de HW, SW y procedimientos diseñados para facilitar la obtención, gestión, manipulación, análisis, modelado y salida de datos espacialmente referenciados, para resolver problemas complejos de planificación y gestión" (p. 12).
2. Componentes/herramientas: Entrada (captura de información digital o digitalización de fuentes analógicas), Gestión (organización y extracción de información), Análisis (procesamiento y obtención de nueva información), Salida (visualización de datos y resultados) (p. 13).
3. Funcionalidades típicas: Localización (¿qué hay en...?), Condición (¿dónde sucede qué...?), Tendencias (¿qué ha cambiado...?), Rutas (¿cuál es el camino óptimo...?), Pautas (¿qué pautas existen...?), Modelos (¿qué ocurriría si...?) (p. 14).

### 4. Catálogo de fuentes de información GIS abiertas (p. 15-18, 42) — sección tratada con detalle por instrucción especial
1. **IGN — Instituto Geográfico Nacional** (p. 15): portal "Centro de Descargas" del IGN (sin URL literal en la diapositiva, solo nombre y captura de pantalla). Producto destacado: Plan Nacional de Ortofotografía Aérea (PNOA) → nubes de puntos LIDAR, con dos coberturas nacionales: LIDAR 1ª Cobertura (2008-2015) y LIDAR 2ª Cobertura (2015-actualidad), formato de fichero LAZ (comprimido de LAS), proyección UTM ETRS89 (huso correspondiente), superficies de descarga en cuadrículas de 2×2 km. También ofrece Modelos Digitales de Elevaciones (MDT02, MDT05, MDT25, MDT200) y mapas vectoriales/topográficos.
2. **Catastro — Dirección General del Catastro** (p. 16): "Sede Electrónica del Catastro", con módulo de "Consulta de Datos Catastrales" (ortofotos del PNOA integradas en el visor). Aporta cartografía catastral vectorial rústica y urbana → permite obtener la distribución de edificios e información pública asociada a las parcelas catastrales (referencia, uso, superficie).
3. **Radiación solar y clima** (p. 17), cuatro fuentes enumeradas explícitamente:
   - **SoDa** — "Solar Services for Professionals" (geometría solar, mapas de radiación, servicios web gratuitos y de pago).
   - **ADRASE** — "Acceso a Datos de RAdiación Solar de España" (desarrollado por CIEMAT): mapa de irradiación solar global horizontal de la península, promedio anual de valores diarios.
   - **PVGIS** — "Photovoltaic Geographical Information System" (Comisión Europea/JRC): mapas interactivos de irradiación mensual/anual, radiación directa/difusa, ángulo óptimo de inclinación, temperatura ambiente diaria.
   - **AEMET** — datos climáticos oficiales de España.
   (La diapositiva no incluye URLs textuales completas, solo el nombre de cada servicio junto con una captura de su interfaz; las direcciones exactas deben verificarse de forma independiente.)
4. **Otros servicios de datos comarcales y regionales** (p. 18): se muestran capturas de tres Infraestructuras de Datos Espaciales (IDE) autonómicas — **Geoportal IDEM** (Infraestructura de Datos Espaciales de la Comunidad de Madrid, con capas de Medio Físico, Cubierta Terrestre, Calidad Ambiental, Gestión del Territorio, Vías de Comunicación, Unidades Administrativas, Sociedad y Cultura, Información Geodésica y Cartográfica, Base Topográfica Armonizada 1:5.000, Toponimia), **IDE Rioja** (`larioja.org`) e **ICV** (Institut Cartogràfic Valencià, Generalitat Valenciana, visor y descargas en `gva.es`). Además se citan como fuente genérica: bases de datos de ayuntamientos y planes de ordenación urbana, IDEs del resto de comunidades autónomas, e información de empresas y particulares (esta última sujeta a autorización).
5. **CNIG — "Potencial de Energía Solar de Edificios"** (p. 42): visor público por edificio con energía solar anual estimada por tejado, con escala de color de 200 a 2.200 kWh/m²/año, y buscador por dirección.

### 5. Tecnología LIDAR (p. 19-23)
1. LIDAR (Light Detection And Ranging): tecnología de teledetección óptica que utiliza pulsos de luz láser para muestrear la superficie terrestre; el barrido genera una nube de puntos con la que se determina la altura y forma de cualquier elemento sobre el terreno (árboles, edificios, infraestructuras) (p. 19).
2. Un mismo pulso puede generar varios rebotes (retornos) según las superficies reflectoras que atraviesa antes de llegar al suelo — ejemplo dado: 1er reflejo en la copa de los árboles, 2º en las ramas, 3er reflejo en el terreno (p. 20). Plataformas de captura mostradas: satélite, helicóptero, vehículo terrestre, embarcación, trípode terrestre.
3. Aplicaciones: planificación urbana e infraestructuras (líneas eléctricas, carreteras, túneles) (p. 21); zonas costeras, arqueología, zonas forestales, inundaciones (p. 22).
4. Uso de drones para fotogrametría/restitución 3D como alternativa o complemento al LIDAR aerotransportado (p. 23).

### 6. Metodología del modelo gSolarRoof (p. 24-32)
1. Flujo de procesado (p. 24): Delimitación de la zona → Recopilación de los datos → Edición y clasificación de los datos → Definición de la base de datos → Modelo Digital de Superficie (MDS) → [Tejados: inclinación, orientación, sombras, accesibilidad] + Radiación solar → Cálculo de la superficie de tejados disponible → Fotovoltaica (potencia instalada, energía anual generada) y Agua Caliente Sanitaria (energía anual generada) → Emisiones de CO₂ evitadas.
2. El MDS se genera a partir de la elevación de la nube de puntos LIDAR o de restitución fotogramétrica de imágenes de dron, con clasificación previa de la nube por tipo de superficie (suelo, vegetación baja/media/alta, edificio, agua, líneas eléctricas, ruido, etc.) (p. 25).
3. Factores de radiación solar considerados: posición del sol (latitud, hora del día, época del año), configuración del entorno (distribución de la zona urbana, topografía del terreno, características de la superficie), condiciones atmosféricas (nubes, partículas de polvo, aerosoles, humedad) (p. 26). Parámetros de cálculo: configuración del periodo de tiempo por meses, latitud, parámetros topográficos (edificios, árboles, ordenación de tejados), proporción de radiación difusa y transmisibilidad atmosférica (p. 27).
4. Tipología de edificios analizables: monumentos y edificios singulares, naves industriales, con delimitación de zonas de acceso a los tejados (p. 28); tipos de tejados considerados: cubiertas curvas, tejados planos con estructura soporte inclinada, tejados a dos aguas residenciales, cubiertas de naves industriales (p. 29).
5. Orientación óptima en el hemisferio norte: cara al sur; inclinación óptima de los módulos: algunos grados por debajo de la latitud local (aprox. 10° menos) (p. 30). El modelo calcula mapas de orientación e inclinación por tejado individual a partir del MDS.
6. Distinción operativa (p. 32): tejados planos → los módulos se instalan sobre una estructura con inclinación y orientación diseñadas para maximizar la eficiencia; tejados inclinados → la posición de los módulos viene determinada por la inclinación existente del tejado, situándolos en las zonas con menores pérdidas de energía.

### 7. Casos de aplicación (p. 10-11, 40-42) — tratamiento somero
1. gSolarRoof aplicado a municipios (ej. Miraflores de la Sierra, mapa de irradiación solar global anual por tejado, Comunidad de Madrid) y a polígonos industriales (colaboración con Naturgy/Comunidad de Madrid; proyecto IDERCEXA en los polígonos de Don Benito, Badajoz, y Plasencia, Cáceres, cofinanciado por Interreg España-Portugal) (p. 10-11, 40).
2. Alpedrete: Premio CONAMA 2018 a la sostenibilidad de pequeños y medianos municipios, mapa solar municipal ("Alpedrete Municipio Solar") (p. 11).
3. "Habana Ciudad Solar" (Guanabacoa, Cuba): visor de mapa solar cofinanciado por Cooperación Española, con metodología documentada en el Informe Técnico CIEMAT nº 1512 (octubre 2022), "Metodología para la elaboración del mapa solar de La Habana (Cuba)" (Martín Ávila, A.M.; Domínguez Bravo, J.; Zarzalejo Tirado, L.F.; Domínguez Benito, M.) (p. 41).
4. CNIG: visor público "Potencial de Energía Solar de Edificios" a escala de edificio individual, ya descrito en el catálogo de fuentes (p. 42).

### 8. Máster ERMA — propuestas de TFM tutorizadas por gTIGER/CIEMAT (p. 44-47) — tratamiento somero
1. Ejemplo de TFM ya defendido en el propio Máster ERMA: "Estimación del potencial fotovoltaico para autoconsumo de los edificios públicos de Alpedrete mediante PVsyst" (Guillermo Sande García, curso 2016/2017, tutores Javier Domínguez Bravo y **Julio Amador Guerra**) (p. 44).
2. Publicación derivada del grupo: Domínguez Bravo, J.; Domínguez Benito, M.; Martín Ávila, A.M.; Arranz Arranz, B., "Transición Energética y Ecosocial: Aprovechamiento del Potencial Solar para una Comunidad Energética en Orcasitas", Hábitat y Sociedad, (17), 79-106. DOI: 10.12795/HabitatySociedad.2024.i17.05 (p. 45).
3. Propuesta de TFM 1 ofertada: "Herramientas para el fomento de comunidades energéticas" — aplicar el modelo gSolarRoof (`gsolarroof.eu/que-hacemos/`) a la evaluación del potencial solar de todos los edificios de una comunidad energética, con revisión crítica de modelos y herramientas existentes. Tutor: Javier Domínguez (CIEMAT), javier.dominguez@ciemat.es (p. 46).
4. Propuesta de TFM 2 ofertada: "Evaluación del potencial de plantas híbridas eólico-fotovoltaicas en España" — dentro del proyecto de mapa nacional de capacidad de hibridación, aplicando SIG a la determinación del potencial de plantas híbridas conectadas a red del orden de MW, considerando criterios técnico-económicos, ambientales y sociales. Tutores: Javier Domínguez y Luis Arribas (CIEMAT) (p. 47).

## Datos clave (con página de origen)
- PNOA-LIDAR: dos coberturas nacionales, 2008-2015 y 2015-actualidad, formato LAZ, proyección UTM ETRS89 (p. 15).
- MDT del IGN disponible en cuatro resoluciones: MDT02, MDT05, MDT25, MDT200 (p. 15); en el mapa de hibridación se usa concretamente el de 200 m (p. 7).
- Irradiación solar de referencia nacional usada en el proyecto de hibridación: ADRASE-CIEMAT a 5.000 m de resolución y ERA5-Copernicus a 0,25°/1.000 m (p. 7).
- Inclinación óptima orientativa de módulos: latitud local menos aprox. 10°, orientación cara al sur (hemisferio norte) (p. 30).
- CNIG "Potencial de Energía Solar de Edificios": escala de energía solar anual de 200 a 2.200 kWh/m²/año (p. 42).
- Informe metodológico de referencia para mapas solares urbanos: CIEMAT, Informe Técnico 1512 (octubre 2022) (p. 41).
- TFM ERMA precedente en esta misma línea de trabajo: Sande García (2016/2017), cotutorizado por Julio Amador Guerra — el mismo tutor del TFM de Mario (p. 44).

## Relevancia para el TFM
- **Capítulos del índice a los que aporta**: capítulo de localización/emplazamiento del CPD y análisis de la variante 3 (autoconsumo a través de red, parcela candidata a más distancia); ver memorias de proyecto `project_localizacion_cpd_parcela_v3` y `project_marco_regulatorio_2026`.
- **Qué aporta exactamente**: catálogo verificado de fuentes GIS gratuitas, complementarias a Google Earth, para caracterizar candidatas a parcela de la variante 3: IGN/PNOA-LIDAR (modelo 3D del terreno y edificaciones existentes), Catastro (delimitación exacta y titularidad de parcelas), PVGIS y ADRASE-CIEMAT (irradiación solar del emplazamiento concreto), y el Geoportal IDEM (Comunidad de Madrid, donde se ubica el CPD) para cartografía temática regional de ordenación del territorio. Aporta además un antecedente académico directo: el tutor de Mario, Julio Amador Guerra, ya cotutorizó un TFM ERMA con este mismo grupo (gTIGER-CIEMAT) sobre potencial fotovoltaico de edificios públicos mediante PVsyst (Alpedrete, 2016/2017).
- **Confianza en los datos**: nombres de servicios, siglas y logos tomados literalmente de las diapositivas. La presentación **no incluye ninguna URL textual completa** para IGN, Catastro, PVGIS, ADRASE, SoDa, AEMET, IDEM, IDE Rioja ni ICV — solo el nombre del portal y una captura de su interfaz. Antes de citar o enlazar estas fuentes en el TFM, sus direcciones deben verificarse de forma independiente (regla de cifras/fuentes canónicas de CLAUDE.md); la única URL literal presente en el documento es `gsolarroof.eu/que-hacemos/` (p. 46).

## Notas de procesamiento
- Densidad ejecutiva aplicada por encargo explícito del equipo (tema de prioridad baja para Mario), con tratamiento reforzado únicamente en la sección 4 ("Catálogo de fuentes de información GIS abiertas") por instrucción especial del encargo.
- El PDF tiene 48 páginas según el índice interno del archivo. Se leyeron íntegramente las páginas 1-32 (portada, gTIGER, mapa de hibridación, ¿qué son los SIG?, catálogo de fuentes, LIDAR, metodología gSolarRoof) y 40-48 (casos de aplicación finales, propuestas de TFM, cierre).
- **Se omitieron las páginas 33-39** (continuación de ejemplos de aplicación de gSolarRoof previa a la sección "Master ERMA") por ser redundantes con los casos ya cubiertos en las páginas 10-11, y por el nivel de densidad ejecutivo asignado; no se afirma nada sobre su contenido concreto.
- Aviso de numeración: el número de página impreso en el pie de cada diapositiva (footer) no coincide con la posición real dentro del archivo a partir de, aproximadamente, la página 33 del PDF (ejemplo: la página 40 del archivo muestra footer "46"; la página 48 del archivo muestra footer "55"). Todas las citas de página de este resumen usan la posición real dentro del archivo PDF (la aceptada por el parámetro de lectura por rangos), no el número de pie de página impreso en la diapositiva.
- No se detectó ninguna URL completa de forma literal en el texto de las diapositivas para las fuentes GIS del catálogo (IGN, Catastro, PVGIS, ADRASE, SoDa, AEMET, IDEM, IDE Rioja, ICV); solo nombres de portal/servicio y capturas de pantalla de sus interfaces.
