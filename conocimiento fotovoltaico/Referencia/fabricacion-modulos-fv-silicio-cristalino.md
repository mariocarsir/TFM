---
title: "Módulos FV de silicio cristalino. Fabricación, defectos, selección"
tipo: presentacion
autor: "Dr. Eduardo Forniés (Quality Manager, Sonnedix)"
anio: 2026
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T3_FabricacionModulosFV.pdf"
tags: [fotovoltaica, modulo-fv, celula-solar, fabricacion, TOPCon, PERC, HJT, defectos, seleccion-panel]
related: [trabajo-previo-modulo6-cpd]
---

# Módulos FV de silicio cristalino. Fabricación, defectos, selección (Eduardo Forniés, 2026)

## Resumen

Presentación del Módulo 6 (Autoconsumo FV) del Máster ERMA, impartida por el Quality Manager de Sonnedix, que recorre la cadena de valor completa del módulo fotovoltaico de silicio cristalino: purificación de silicio, crecimiento del cristal, fabricación de la célula (BSF, PERC, TOPCon), ensamblado del módulo y control de calidad mediante electroluminiscencia (EL). Dedica su bloque final (sección 4) a la tendencia tecnológica de célula (PERC → TOPCon/HJT → tándem de perovskita), a las tecnologías de módulo que aportan ganancia energética (bifacial, half-cut, MBB, shingled) y a los criterios de selección de panel, cerrando con una checklist abierta sin recomendación única. Es la fuente de mayor relevancia directa para justificar la elección de tecnología de célula/módulo en el capítulo de dimensionado del TFM, aunque no fija un criterio de selección cerrado: deja la decisión como una lista de disyuntivas sin resolver.

## Contenido técnico

### 1. Introducción: cadena de valor, costes, LCOE

1. Cadena de valor del silicio (p.2): Polysilicon → Ingots → Wafers → Solar Cells → PV Modules.
2. Evolución de costes (p.3): precio medio de venta (ASP) del módulo PV cayó de ~4 $/Wp (2006) a ~0,2 $/Wp (2020). Desglose de coste "best-in-class" por etapa de fabricación (estimación a finales de 2024, fuente BloombergNEF, US cents/W): silicio 1,3; silicio a oblea 1,3; oblea a célula 1,6; célula a módulo 6,5; coste total in-house 10,7. (No se especifica en la fuente el desglose de qué componentes conforman el 6,5 c/W de "célula a módulo").
3. LCOE (p.4):
   $$LCOE = \frac{I_0 + \sum_{t=1}^{n} \frac{A_t}{(1+i)^t}}{\sum_{t=1}^{n} \frac{M_{t,el}}{(1+i)^t}}$$
   donde $I_0$ = inversión inicial, $A_t$ = coste total anual en el año t, $M_{t,el}$ = electricidad producida en el año t (kWh), $i$ = tasa de interés real (%), $n$ = vida económica (años). Rango de LCOE comparado (€cent₂₀?/kWh, sin año base especificado en la fuente): FV 1400h sol ≈ 3-4; FV 1800h ≈ 2; FV 2000h ≈ 1,5-2; eólica onshore ≈ 5-6; térmica carbón (lignito) ≈ 11-18; térmica carbón (antracita) ≈ 12-20; ciclo combinado de gas ≈ 9-13; turbinas de gas ≈ 13-22.

### 2. Purificación del silicio (sección 3.1)

1. Silicio de grado metalúrgico (MG-Si, pureza 98%-99,9%): reducción de cuarzo con carbón en horno de arco eléctrico a 2000 °C: $SiO_2 + C \rightarrow Si + CO_2$.
2. Purificación química a silicio de grado electrónico (EG-Si, pureza 99,9999%-99,999999%), proceso Siemens: reactor de lecho fluidizado a 300 °C con HCl: $Si + 3HCl \rightarrow SiHCl_3 + H_2$; destilación en columnas; reactor Siemens a 1200 °C: $2SiHCl_3 + 2H_2 \rightarrow 2Si + 6HCl$, produce polisilicio de alta pureza con concentración de impurezas Ci < 1 ppm (10¹³ cm⁻³).

### 3. Crecimiento del cristal (sección 3.2)

1. Monocristalino — proceso Czochralski (p.8), 14 pasos: carga de policristal Siemens/FBR en crisol → fusión (polisilicio + dopante) → introducción de cristal semilla → inicio de crecimiento → extracción del lingote (tirado del cristal) → cropping (corte por sierra de banda) del lingote → bricking/squaring (escuadrado) → grinding/pulido de esquinas → pegado a sustrato de vidrio → wafering con hilo de diamante (kerf loss 90-100 µm por corte) → baño químico para disolver el pegamento → limpieza, singulación e inspección.
   - Oblea monocristalina resultante: 160 µm de espesor, 244 cm² de superficie. Utilización neta de silicio (incluyendo pérdidas de kerf y rendimiento, con reciclaje de corona/cola/cuerdas): ~16,0 g/oblea, equivalente a 3,05 g/W(DC) para una eficiencia de célula del 21,5%.
2. Multicristalino: crecimiento en bloque por solidificación direccional en horno (imágenes de proceso industrial, p.9); sin ecuaciones ni parámetros numéricos adicionales en la fuente.

### 4. Fabricación de la célula solar (sección 3.3)

1. Proceso base (célula mono, p.10): recepción de oblea → limpieza y texturizado (baños alcalinos o ácidos) → difusión de fósforo (CVD) → edge etching (aislamiento de bordes) → deposición de recubrimiento antirreflectante (ARC) → serigrafía dual: 1er impreso de dedos frontales, 2º impreso de buses frontales → co-firing en horno de banda (fusión de contactos) → test y clasificación eléctrica de la célula.
2. Célula PERC (Passivated Emitter and Rear Cell), pasos principales (p.11): deposición de PSG (Phospho-silicate glass, $P_2O_5+SiO_2$) a 780 °C; ARC = $SiN_x$; grabado con HF+HNO₃ (frontal) y HF (texturizado); apertura de contactos láser (LCO); pasta de aluminio en cara posterior con aleación Si-Al como Back Surface Field (BSF); co-firing a 850 °C.
3. Célula TOPCon (Tunnel Oxide Passivated Contacts), estructura tipo N (p.13-14, 88): deposición de óxido túnel (1-2 nm) por LPCVD; capa de polisilicio (150 nm) por LPCVD; difusión de boro en vidrio borosilicato ($B_2O_3+SiO_2$) a 1000 °C; grabado frontal HF+HNO₃; grabado posterior con NaOH; PECVD de $Si_3N_4$ (80 nm); ALD de $Al_2O_3$; serigrafía de contactos Ag/Al; firing a 850 °C.
4. Comparación TOPCon vs. PERC (p.87): TOPCon es base tipo N con contacto posterior pasivado por óxido túnel + poli-Si (capa selectiva de portadores); PERC es base tipo P con emisor y cara posterior pasivados dieléctricamente, contacto BSF local de aluminio.
5. Comparativa de tecnologías de célula (p.91), tabla de procesos: 
   | Tecnología | Nº de pasos principales | Rasgo distintivo |
   |---|---|---|
   | P-type Al-BSF | 7 | BSF de aluminio en toda la cara posterior |
   | P-type PERC / PERC+ | 8 | pasivación posterior + BSF local vía apertura láser de contactos |
   | N-type HJT | 6 | capas de a-Si:H (i/n/p) + TCO frontal y posterior; solo dedos serigrafiados (compatible con tecnología "Smart Wire") |
6. Ensayo de degradación UV en TOPCon (p.89-90, módulo 2022): tras 30 kWh/m² de exposición UV, pérdida de potencia P = −2,6%; tras 65 kWh/m² de exposición UV, pérdida de potencia P = −0,2% (mejora respecto al primer punto, comportamiento de estabilización tras degradación inicial). No se detalla en la fuente el mecanismo causante ni condiciones de ensayo más allá de estos dos puntos.

### 5. Asociación de células y materiales del módulo (sección 3.4)

1. Asociación en serie: ejemplo de 72 células en serie de 7,5 W cada una → 540 W de módulo; se ilustra el riesgo de una célula defectuosa/sombreada que reduce la potencia de la rama y la necesidad de diodos de bypass (p.21).
2. Materiales estándar de un módulo (p.22-23): vidrio, células solares, tab-ribbon, EVA, fibra, backsheet (TPT o poliéster), cables de conexión, caja de conexiones (junction box), perfiles/marco, etiquetas, tornillos, bus bar ribbon, silicona.

### 6. Línea de fabricación y control de calidad (sección 3.5)

1. Etapas de línea de ensamblado (p.24): 1. Tabber-stringer (soldadura célula-célula) → 2. Matrixing → 3. Interconnection (interconexión de strings) → 4. EL Test → 5. Lay-up → 6. Lamination → 7. Cooling → 8. Edge trimming → 9. Colocación de junction box + soldadura de bus bars + enmarcado → 10. Dispensador de silicona de marco → 11. Flash tester → 12. EL Test → 13. Packaging.
2. Test de electroluminiscencia (EL, p.30): excitación eléctrica directa de las células que emiten luminiscencia captada por cámara; las áreas inactivas (roturas de célula, centros de recombinación, tab-ribbons no soldados, dedos mal impresos) aparecen como zonas oscuras sin emisión. Es la herramienta de control de calidad de fábrica y de campo usada a lo largo de toda la presentación para detectar microfisuras, interrupciones de dedos y defectos de proceso (numerosos ejemplos visuales pp.31-37, 89-90, 99, no reproducibles en texto).

### 7. Degradación de backsheet (sección 3.6)

1. Caso de campo (Villena, <14 años de operación, p.83-84): agrietamiento y desprendimiento (chalking) del backsheet observado en módulos en servicio.
2. Se documenta que dos formulaciones de backsheet distintas en la misma instalación presentan patrones de degradación diferentes (p.84), sin cuantificar en la fuente qué materiales son ni la tasa de degradación de cada uno.

### 8. Tendencia tecnológica de célula (sección 4.1)

1. Cuota de mercado de tecnologías de célula (p.85-86, fuentes ITRPV/S&P Global 2023 y PV ModuleTech Nov. 2024): la célula PERC (tipo P) pierde cuota frente a conceptos tipo N por menor coste de producción de estos últimos; se proyecta declive marcado de PERC entre 2028-2034, sustituida por TOPCon, heterounión de silicio (SHJ/HJT), back-contact (IBC) y, más adelante, tándem.
   - Evolución histórica real (gráfico PV ModuleTech, p.86): p-type multi BSF domina 2005-2017 → p-type mono PERC domina ~2017-2021 → n-type mono TOPCon en ascenso 2021-2029, ganando cuota mayoritaria; back-contact con cuota creciente.
2. Eficiencias límite citadas (p.85): PERC bifacial, eficiencia industrial máxima < 24%; HJT tipo N y TOPCon tipo N, eficiencia industrial máxima < 26%; tándem (perovskita sobre silicio, CIGS-perovskita, perovskita-perovskita, orgánico-perovskita), eficiencia teórica máxima < 38%.

### 9. Tecnologías de módulo (sección 4.3)

1. Bifacial: ganancia energética del 5% al 30% frente a monofacial en sistemas inclinados, dependiendo de orientación, albedo y ángulo de inclinación (no se especifica en la fuente un valor único recomendado).
2. MBB (Multi Bus Bar): hasta 12 busbars por célula; gana energía al reducir la resistencia serie.
3. Half-cut cells (células cortadas por la mitad): reduce pérdidas por resistencia serie (~3% más de potencia) al reducir la corriente por célula, y reduce la pérdida de potencia por sombreado parcial.
4. Módulos shingled (tejado/solapados): interconexión por solapamiento de células sin gap entre ellas, maximiza área activa del módulo.
5. Deficiencias de diseño de interconexión densa (sección 4.4, p.93-94): la interconexión "tiling ribbon" presenta riesgo de microfisuras y degradación de rendimiento — la fuente concluye explícitamente que "debería rechazarse" ("should be rejected"). Alternativa: interconexión "paving"/"Smart Soldering" (secciones triangular + plana + small-gap), que incrementa la eficiencia del módulo un 0,3% frente a un producto MBB convencional, aunque la fuente advierte que deben compartirse ensayos de estrés extendidos y certificados para minimizar el riesgo.

### 10. Tamaños de célula (sección 4.5)

| Formato | Lado (mm) | Área relativa vs. G1 |
|---|---|---|
| G1 (legado) | 158,75 | referencia |
| M6 (transición) | 166 | +8,8% |
| M10 | 182 | +30,6% |
| G12 | 210 | +75% |

Evolución de potencia de módulo asociada al aumento de tamaño de célula y a la transición tecnológica (fuente: Aiko Cells): de ~125 W (2002, era "Top-runner") a >700 W (era "8.0", G12 Plus tipo N, hacia 2022 en adelante).

### 11. Selección de módulo (sección 4.6, p.98)

La presentación cierra el bloque de selección con una checklist de disyuntivas sin resolver (representada como opción ✔ / ✘ con un signo de interrogación explícito), sin ofrecer un criterio de decisión cerrado en la fuente:
- Tamaño de célula: M10 (182 mm) vs. G12 (210 mm).
- Monofacial vs. bifacial.
- Dimensiones de módulo: 1130×2256 mm vs. 1300×2380 mm.
- Tipo de interconexión de celdas (asociado a los esquemas de las pp.93-94: tiling vs. paving).
- Tecnología de célula: TOPCon, HJT o PERC.

No se especifica en la fuente qué combinación recomienda el ponente ni bajo qué criterio (coste, disponibilidad, degradación, aplicación) debería resolverse cada disyuntiva.

## Datos clave (con página de origen)

- Coste de fabricación best-in-class 2024 estimado: 10,7 c$/W total in-house, del cual 6,5 c$/W corresponde a "célula a módulo" (p.3).
- Oblea monocristalina Czochralski: 160 µm espesor, 244 cm², ~16,0 g/oblea, 3,05 g/W(DC) a 21,5% de eficiencia de célula (p.8).
- Eficiencia industrial máxima: PERC bifacial <24%, TOPCon/HJT tipo N <26%, tándem de perovskita <38% teórico (p.85).
- Degradación UV en TOPCon: −2,6% a 30 kWh/m² UV, −0,2% a 65 kWh/m² UV (p.89-90).
- Ganancia bifacial: 5%-30% en sistemas inclinados según orientación/albedo/tilt (p.92).
- Ganancia por half-cut cells: ~3% más de potencia por reducción de resistencia serie (p.92).
- Ganancia por interconexión "Smart Soldering"/paving: +0,3% de eficiencia de módulo vs. MBB convencional (p.94).
- Tamaños de célula: G1 158,75 mm → G12 210 mm (+75% de área) (p.95).
- Interconexión "tiling ribbon": riesgo de microfisuras, "debería rechazarse" según la fuente (p.93).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: capítulo de dimensionado del campo fotovoltaico (selección de tecnología de panel/célula), y como contexto de mercado/tendencia tecnológica si el TFM justifica la elección de módulo TOPCon/PERC/HJT.
- **Qué aporta exactamente**: justificación técnica del estado del arte de tecnologías de célula (PERC vs. TOPCon vs. HJT) y de módulo (bifacial, half-cut, MBB, tamaños de célula) que puede citarse al argumentar la elección de un modelo de panel comercial concreto en el capítulo de dimensionado. Es material de apoyo/contexto, no una fuente citable en el TFM (presentación de máster, sin ISBN/DOI ni revisión por pares).
- **Confianza en los datos**: cifras trazables a la página de la presentación indicada en cada apartado; varias cifras citan fuentes secundarias dentro de la propia presentación (BloombergNEF, ITRPV, S&P Global, PV ModuleTech, Aiko Cells) que no han sido verificadas de forma independiente — si se cita cualquiera de estas cifras en el TFM, debe verificarse contra la fuente primaria antes de su uso (regla de `investigador-cientifico`).

## Notas de procesamiento

Densidad EJECUTIVA fijada por el encargo (tema clasificado como de prioridad baja por Mario) — no se preguntó al usuario. Documento de 102 páginas; se leyeron íntegras las páginas 1-40 y 83-102 (portada, secciones 1, 3.1-3.6 y 4.1-4.6, cierre). Se omitió la lectura de las páginas 41-82, que corresponden mayoritariamente a: (a) el resto del detalle de la línea de fabricación (interconexión, laminado, encolado de vidrio posterior — ya cubierto de forma suficiente en las etapas 1-13 listadas en la sección 6 de este resumen) y (b) una extensa galería de ejemplos de imágenes de electroluminiscencia mostrando defectos de fabricación específicos (interrupciones de dedos, microfisuras, células rotas, etc.), que aporta ejemplos visuales adicionales del mismo fenómeno ya descrito cualitativamente en la sección 6 (test EL) pero sin datos numéricos o procedimentales nuevos relevantes para la selección de panel del TFM. Si en el futuro se necesita el detalle exhaustivo de la taxonomía de defectos de electroluminiscencia, este documento debe reprocesarse en densidad Estándar o Exhaustiva cubriendo las páginas 41-82.
