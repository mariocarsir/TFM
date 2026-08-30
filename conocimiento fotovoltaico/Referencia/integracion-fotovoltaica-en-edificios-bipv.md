---
title: "Integración de Fotovoltaica en Edificios"
tipo: presentacion
autor: "Nuria Martín Chivelet (CIEMAT)"
anio: 2025
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T6_IntegracionArquitectonica.pdf"
tags: [fotovoltaica, bipv, integracion-arquitectonica, marquesinas, autoconsumo]
related: []
---

# Integración de Fotovoltaica en Edificios (Martín Chivelet, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición 2025-2026, impartida por Nuria Martín Chivelet (grupo BIPV del CIEMAT). Cubre la integración fotovoltaica en edificios (BIPV, *Building Integrated Photovoltaics*, frente a BAPV, *Building Added Photovoltaics*): tecnologías de módulo disponibles, funciones constructivas que un módulo BIPV debe cumplir (norma UNE-EN 50583 / IEC 63092), criterios de diseño fotovoltaico (insolación, temperatura, sombreado, suciedad, cableado, dispersión de parámetros), posibilidades de diseño de módulos especiales (tamaño, forma, color, transparencia) y ejemplos de aplicaciones arquitectónicas reales (fachadas, cubiertas, marquesinas, muros cortina). Cierra con las actividades de I+D+i del grupo BIPV del CIEMAT (proyecto RINGS-BIPV, rehabilitación del Edificio 42 del CIEMAT, IEA-PVPS Task 15).

**Nota de alcance (indicación explícita de Mario):** este tema contiene escaso contenido de valor para el TFM; sus aportaciones son complementarias ("pluses") y no deben condicionar decisiones de diseño. Aplica únicamente, si acaso, a la variante de marquesinas del parking (integración arquitectónica sobre estructura de aparcamiento), no a las otras variantes del TFM.

## Contenido técnico

### 1. Tecnologías de módulo para BIPV (diapositivas 2-11)
- Silicio cristalino estándar y avanzado (célula TOPCon con capa de óxido túnel, ejemplo comercial Huasun 490-520 W).
- Lámina delgada: flexible, curvable, integrable en cubiertas curvas y fachadas.
- Células orgánicas (OPV): ventajas — versatilidad, ligereza, colores/transparencia; desventajas — tecnología incipiente, menor rendimiento, degradación.
- Módulos tándem silicio-perovskita: ventajas — alta eficiencia, bajo coste, alto potencial BIPV; desventaja — tecnología en fase de desarrollo (no especificado nivel de madurez comercial).

### 2. BIPV vs. BAPV
- **BAPV** (*Building Added PV*): el módulo se añade al edificio, sin función constructiva.
- **BIPV** (*Building Integrated PV*): el módulo realiza una función constructiva en el edificio (fuente: *Building-Integrated Photovoltaics. A Technical Guidebook*, 2024, ISBN 9781032517056).
- Ubicaciones posibles de integración BIPV (diapositiva 15, fuente SUPSI 2020): 1) tejados, 2) fachadas ventiladas, 3) elementos externos, 4) marquesinas y lucernarios, 5) revestimientos, 6) muros cortina.

### 3. Ventajas y limitaciones de BIPV (diapositivas 16-17)
**Ventajas:** producción eléctrica descentralizada (ahorro en distribución/conducción), contribución al autoconsumo y reducción de picos de demanda, ahorro de terreno, ahorro en material constructivo, mejor integración visual, soluciones para rehabilitación energética.

**Limitaciones:** orientación/inclinación no siempre óptimas para producción eléctrica; temperatura de operación condicionada por la ventilación de la estructura; mayor probabilidad de sombreado parcial (efectos eléctricos y térmicos); diseño de módulos y sistemas condicionado por exigencias constructivas.

### 4. Los módulos BIPV como elementos constructivos (diapositiva 19)
Funciones exigibles según normativa (UNE-EN 50583 partes 1 y 2 en Europa; IEC 63092 partes 1 y 2 a nivel internacional; en la UE aplica también el Reglamento de Productos de la Construcción y la Directiva de Baja Tensión):
- a) Rigidez mecánica / integridad estructural
- b) Protección contra impactos climáticos primarios (lluvia, nieve, viento, granizo)
- c) Sombreado, iluminación diurna, aislamiento térmico
- d) Protección contra incendios
- e) Protección contra ruidos
- f) Separación entre ambientes interiores y exteriores
- g) Seguridad/cobijo

### 5. Los módulos BIPV como generadores eléctricos (diapositivas 21-23)
Rendimiento eléctrico global depende de: rendimiento del módulo (tecnología y diseño), coeficiente de rendimiento del sistema *PR* (diseño de sistema, inversor), rendimiento energético final $Y_f$ (irradiación, *PR*).

**Criterios fotovoltaicos de diseño (1er criterio: favorecer la insolación), con aspectos adicionales:**
- Reducir temperatura de trabajo del módulo.
- Evitar/reducir sombreados.
- Disminuir pérdidas por disparidad de corriente/tensión.
- Evitar acumulación de suciedad.
- Reducir pérdidas en conexiones y cableado.
- Permitir buen seguimiento del PMP (punto de máxima potencia).

Ecuación de pérdida de potencia por temperatura (silicio cristalino):
$$P_2 \approx P_1 \cdot [1 - \gamma \cdot (T_2 - T_1)], \quad \gamma \cong 0{,}004\ /°C \text{ (Si-c)}$$

Gráfica de pérdidas de potencia (%) vs. incremento de temperatura (0-50 °C): silicio cristalino ~20% a 50 °C de incremento (la curva de mayor pendiente); CIS intermedio; CdTe y silicio amorfo con menor pendiente, ~10-12% a 50 °C.

Índices de autoconsumo y autosuficiencia (fuente: Martín & Montero, *Energy and Buildings* 150, 2017):
$$SCI\,(\%) = \frac{\text{PV energy consumed}}{\text{PV energy produced}} \cdot 100 \qquad SSI\,(\%) = \frac{\text{PV energy consumed}}{\text{Electricity consumed}} \cdot 100$$

Otros efectos cuantificados en las gráficas: pérdidas por reflexión angular según grado de suciedad del módulo (superficie limpia/sucia/muy sucia, mínimo hacia 20-40° de inclinación, aumentando fuertemente hacia 90°); ejemplo real de pérdidas por desacoplo (dispersión de parámetros) al no dividir en hileras: **6%**.

### 6. Diseño de módulos especiales (diapositivas 32-45)
Parámetros modificables del módulo BIPV: tamaño y forma, curvatura y flexibilidad, estructura constructiva, densidad de células, color. Estos afectan a: rendimiento eléctrico, transmitancia térmica, iluminación natural, factor solar, rendimiento de color, deslumbramiento, aislamiento eléctrico.
- Ejemplo de densidad de células: módulo de 100 W con 54 células reduce potencia al bajar a 35 células (valor resultante no especificado en la fuente, planteado como ejercicio).
- Estructura típica de laminado FV: vidrio de bajo contenido en hierro (*low iron glass*) — EVA — células — EVA — Tedlar.
- Ejemplos de transparencia: silicio cristalino en marquesinas/muros cortina; lámina delgada semitransparente (Onyx Solar, Würth Solar, Heliatek).
- Colores de célula y módulo: fabricantes citados Solartec s.r.o. y Onyx Solar; referencia IEA-PVPS informe coloreado BIPV.

### 7. Ejemplos de proyectos BIPV — Aplicaciones arquitectónicas (diapositivas 47-56)
- **Lamas y parasoles:** Torre Garena (BP Solar); Centro de Investigación de Enfermedades Neurológicas, Fundación Reina Sofía (Madrid); Sede de la Fundación Metrópoli, Alcobendas (Madrid).
- **Cubiertas acristaladas:** ejemplo Visual Center, TFM previo; detalle constructivo con 8 elementos (montantes y travesaños de aluminio, separadores de puente térmico, módulo FV, salida de cableado, fijación con silicona estructural, juntas selladas con silicona neutra, cableado interno en montantes).
- **Cubiertas ciegas inclinadas y planas:** varios ejemplos fotográficos (biblioteca Varennes, cubiertas piramidales, tejas fotovoltaicas).
- **Pérgolas y marquesinas** (relevante para variante de marquesinas de parking del TFM): Centro Comercial La Vaguada (Madrid) — pérgola/marquesina de acceso con módulos semitransparentes; Sede social de Telefónica (Madrid) — cubierta plana con calles peatonales entre filas de módulos. No se detallan en la fuente parámetros de dimensionado, inclinación ni datos de producción específicos de marquesinas de aparcamiento.
- **Fachadas ventiladas:** Edificio de Energías Renovables del CIEMAT; Manchester College of Arts and Technology.
- **Muros cortina tradicionales y modulares:** Sede de Schott Ibérica (Barcelona); Biblioteca de Mataró (TFM de referencia citado en la propia presentación).

### 8. Actividades BIPV del CIEMAT (diapositivas 57-64)
- Grupo BIPV del CIEMAT: innovación en integración FV en edificios, ensayos/caracterización/modelización, diseño de sistemas BIPV, estudios de potencial.
- Proyecto **RINGS-BIPV** (CIEMAT + UPM, financiación PID2021-124910OB-C31-C32): modelización avanzada de módulos y sistemas BIPV; fachada coloreada de ensayo en el CIEMAT; mapa de potencial SSI por manzana urbana.
- Caso de estudio: rehabilitación con fachada ventilada del **Edificio 42** (sede de la División de Energías Renovables del CIEMAT), construido en dos fases 1970-1980, con módulos FV disponibles en el propio centro.
- Caracterización de módulos BIPV en el CIEMAT: comportamiento térmico (transmitancia U-value, con balance de resistencias térmicas $1/U = 1/h_e + 1/h_t + 1/h_i$ y diagrama de intercambios de calor conducción/convección/radiación), comportamiento solar (transmitancia lumínica y factor solar, caracterización SHGC), comportamiento eléctrico (curvas características y rendimiento, coeficientes de variación con temperatura, resistencia a sombreamientos parciales, efectos de suciedad, pérdidas angulares, efectos espectrales).
- Actividad internacional: IEA-PVPS Task 15 "Enabling Framework for the Development of BIPV" — catálogo de informes técnicos (políticas, clasificación de aplicaciones, casos de negocio, caracterización multifuncional, herramientas de diseño y rendimiento, mercado, rutas de I+D, definiciones internacionales, modelos de negocio).

## Datos clave (con página/diapositiva de origen)

- Ejemplo real de pérdidas por desacoplo al no dividir en hileras por dispersión de parámetros: **6%** (diapositiva ~30).
- Coeficiente de temperatura del silicio cristalino: $\gamma \cong 0{,}004\ /°C$ (diapositiva 27).
- Normas BIPV de referencia: UNE-EN 50583 (partes 1-2), IEC 63092 (partes 1-2) (diapositiva 20).
- Ubicaciones normalizadas de integración BIPV: 6 categorías (tejados, fachadas ventiladas, elementos externos, marquesinas/lucernarios, revestimientos, muros cortina) (diapositiva 15).
- Proyecto RINGS-BIPV financiado con referencia PID2021-124910OB-C31-C32 (diapositiva 61).
- Ejemplo de marquesina/pérgola FV citado: Centro Comercial La Vaguada, Madrid, y Sede social de Telefónica, Madrid (diapositiva ~53).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: posiblemente al capítulo de descripción de la instalación/variantes de emplazamiento (ver `Memoria/indice_propuesto.md`), únicamente en la variante de marquesinas de parking.
- **Qué aporta exactamente**: contexto conceptual general sobre BIPV/BAPV y ejemplos ilustrativos de marquesinas fotovoltaicas construidas (La Vaguada, Telefónica), pero sin datos de dimensionado, producción ni coste aplicables directamente al CPD del TFM. Por instrucción explícita de Mario, esta fuente **no debe condicionar** decisiones de diseño de ninguna de las variantes del TFM; es material de contexto complementario ("plus"), no un input técnico de cálculo.
- **Confianza en los datos**: todos los datos y cifras reportados están tal como aparecen en la fuente, citados con su diapositiva de origen. Donde la fuente no especifica un valor (p. ej. potencia resultante del ejercicio de densidad de células, diapositiva 44), se ha indicado explícitamente.

## Notas de procesamiento

- Densidad Ejecutiva aplicada según encargo explícito (sin preguntar a Mario), dado que el propio Mario clasificó este tema como de prioridad baja / análisis somero.
- Documento de 64 diapositivas revisado en su totalidad (todas las páginas se visualizaron) para localizar correctamente la sección de marquesinas/pérgolas, pero el resumen se ha mantenido deliberadamente breve y de nivel ejecutivo, omitiendo detalle de figuras, tablas completas y bibliografía secundaria no esencial, conforme al nivel de densidad solicitado.
- La bibliografía completa de la presentación (diapositiva 63) no se ha reproducido íntegra por ser material de referencia de la propia autora, no bibliografía citable de este TFM (regla 10 de CLAUDE.md: el redactor-humanizador no debe citar de aquí sin verificación adicional).
