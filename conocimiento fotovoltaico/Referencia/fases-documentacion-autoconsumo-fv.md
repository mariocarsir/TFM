---
title: "Fases y documentación en el desarrollo de proyectos de Autoconsumo FV"
tipo: presentacion
autor: "Guillermo de la Cruz García (CEO Grupo Proingec)"
anio: 2025
densidad: ejecutivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T10_ProyectosAutoconsumoFV.pdf"
tags: [fotovoltaica, autoconsumo, tramitacion, gestion-operacion-mantenimiento, casos-reales]
related: []
---

# Fases y documentación en el desarrollo de proyectos de Autoconsumo FV (Guillermo de la Cruz García, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición 2025-2026, impartida por el CEO de Grupo Proingec. Recorre el ciclo completo de un proyecto de autoconsumo FV: fases desde la toma de datos hasta la puesta en marcha, normativa de generación mínima obligatoria (CTE DB-HE5), agentes implicados, documentación mínima exigible (Memoria Técnica vs. Proyecto Técnico según potencia), trámites y legalizaciones diferenciados por tramo de potencia y modalidad (con/sin excedentes), una lista de fabricantes Tier-1 de módulos, y un bloque extenso de Gestión, Operación y Mantenimiento (GOM) con estadísticas de averías, fallos comunes y requisitos documentales ante un siniestro. Incluye seis casos reales de Grupo Proingec con potencias y resultados de producción exactos. Documento de prioridad baja para el TFM (clasificación de Mario); resumen deliberadamente somero salvo en el caso PR2006-SCH, señalado como la referencia de caso real más próxima estructuralmente al CPD (industria + cubierta + inyección cero).

## Contenido técnico

### 1-2. Esquema general y fases del ciclo completo

- Esquema unifilar de ejemplo de instalación residencial con batería LiFePO4 (BMS 10 kWh), 4 strings de 6 módulos JASOLAR 460 Wp, 2 inversores HUAWEI SUN2000, contador bidireccional de compraventa. Marca "módulos FV" e "inversor FV" como elementos críticos del esquema.
- Fases del ciclo completo del proyecto (8 fases): (1) adquisición de información y toma de datos previa; (2) estudios previos y pre-dimensionamiento técnico y eco-financiero; (3) tramitaciones previas técnicas y administrativas; (4) para instalaciones ≤10 kWac → Memoria Técnica; (5) para instalaciones >10 kWac → Proyecto Básico + Proyecto de Ejecución + tramitaciones para permisos definitivos; (6) ejecución material (Dirección Facultativa, coordinación de seguridad y salud, pruebas de puesta en marcha, comunicación a organismos); (7) acta de recepción/entrega; (8) Gestión, Operación y Mantenimiento.

### 3. Normativa

- Remite a documento externo "NORMATIVA FV-2025" (no incluido en esta presentación).
- CTE DB-Sección HE5 "Generación mínima de energía eléctrica procedente de fuentes renovables" (versión 22/12/2023). Aplica a: (a) edificios nuevos >1.000 m² construidos; (b) ampliaciones que incrementen >1.000 m²; (c) reformas íntegras o cambio de uso característico que superen 1.000 m² construidos. La superficie construida incluye aparcamiento interior y excluye zonas exteriores comunes.
- Fórmula de potencia mínima a instalar (Pmin = la menor de P1 y P2):

$$P_1 = F_{pr;el} \times S$$
$$P_2 = 0,1 \times (0,5 \times S_c - S_{oc})$$

  donde: $P_{min}$ potencia a instalar [kW]; $F_{pr;el}$ factor de producción eléctrica = 0,005 kW/m² (uso residencial privado) o 0,010 kW/m² (resto de usos); $S$ superficie construida del edificio [m²]; $S_c$ superficie de cubierta no transitable o accesible únicamente para conservación [m²]; $S_{oc}$ superficie de esa cubierta ocupada por captadores solares térmicos [m²].
- Si por razones urbanísticas/arquitectónicas o protección oficial no se puede alcanzar la Pmin, debe justificarse analizando alternativas y adoptar la solución de máxima potencia posible.

### 4. Agentes implicados

- **Privados**: empresa eléctrica distribuidora, comercializadora eléctrica, operador de red (REE), bancos/entidades financieras, propietarios y colindantes, fabricantes, instaladores/contratistas/subcontratistas, ingenierías/arquitecturas, consultorías y due diligence legal/técnica, entidades de inspección y control (EICI, OCA).
- **Públicos**: ayuntamiento/municipalidad, administración autonómica (industria, medio ambiente, urbanismo, patrimonio y cultura), administración central (Ministerio de Industria), operador de red (REE), registros públicos (propiedad, mercantil).

### 5. Documentos mínimos Memoria Técnica / Proyecto Técnico

- **Memoria Técnica** (instalaciones pequeñas): identificación propietario/instalador/ubicación, memoria técnica en formato normalizado por CC.AA., memoria descriptiva, cálculos eléctricos (dimensionamiento eléctrico y energético), presupuesto, esquema unifilar, croquis de trazado, planos de planta, fichas técnicas mínimas de inversor(es) y módulos, tipología de conexión, producción energética prevista.
- **Proyecto Técnico** (instalaciones medianas/grandes): memoria técnica descriptiva y constructiva; anejos (fichas técnicas de equipos y materiales, cálculos eléctricos, cálculos FV completos, comprobación/diseño estructural, justificación de cumplimiento CTE/PGOU/normativa municipal y cualquier otra normativa aplicable); pliego de condiciones técnicas; mediciones y presupuesto; planos y esquemas (ubicación, catastrales, implantación en plantas/secciones/alzados, detalles estructurales, esquema unifilar); Estudio Básico de Seguridad y Salud o Estudio de Seguridad y Salud si es obligatorio según **RD 1627/1997**; Plan de gestión de residuos. Documentación mínima de acompañamiento: nombramiento de Dirección Facultativa (en su caso), certificado de viabilidad geométrica, certificado de seguridad y solidez estructural, declaración responsable de conformidad urbanística — todos firmados por la DF o proyectista.

### 6. Trámites, legalizaciones y documentación

- Clasifica las instalaciones FV conectadas a red en: sin excedentes; con excedentes (con o sin compensación); e instalaciones aisladas de red. Remite a un documento externo ("TRAMITES_LEGALIZACIONES FV AUTOCON_CONECTADO RED") para el detalle.
- Dos tablas comparativas extensas (autoconsumo sin excedentes / con excedentes) que cruzan Entidad-Agente responsable × Trámite/Documentación × tramo de potencia (BT ≤10 kW, 10-100 kW, >100 kW, AT). Puntos relevantes: diseño de instalación exige Memoria Técnica hasta 10 kWac y Proyecto Técnico por encima; permisos de acceso y conexión exentos en general salvo instalaciones sobre suelo con avales de garantía (40 €/kW) a partir de umbrales de potencia; tramitación de acceso y conexión regulada por **RD 1955/2000** y **RD 1699/2011**; inscripción en RAIPRE solo aplica a instalaciones no acogidas a compensación >100 kW.

### 7. Ejemplos reales de proyectos de autoconsumo (Grupo Proingec)

| Proyecto | Tipología | Potencia pico | Potencia nominal | Detalle |
|---|---|---|---|---|
| PR2230 – GISA | Cubierta centro de calidad, autoconsumo con excedentes, BT | 70,98 kWp (61,88 + 9,1 kWp en 2 campos) | 68 kW | PR 76,74%/74,12%, autoconsumo 76,5+7,88 MWh/año, exportación 13,2+4,86 MWh/año (ver tabla completa abajo) |
| **PR2006 – SCH** | Cubierta de talleres, repostaje e instalaciones del Centro de Operaciones de **Sanchinarro de la EMT de Madrid**; autoconsumo instantáneo, conectado a BT interior, **inyección cero a red de distribución** | **186,45 kWp** | **185 kW** (proyecto inicial); *el panel "as-built" del mismo caso indica 100 kWac nominal, generación anual media 140.000 kWh/año y P.E.M. 186.000 €* (discrepancia entre cifra de proyecto inicial y as-built, no resuelta en la fuente) | Fecha proyecto 2015. Alcance Proingec: EPC, gestión, O&M, inversión económica, medida de ahorro energético. CONERSA (Consultora de Energías Renovables) como Empresa de Servicios Energéticos; Proingec realizó ingeniería y dirección de obra |
| PR2005 – CERRO | Cubierta de oficinas de la Sede Central de la EMT de Madrid; autoconsumo instantáneo, BT interior, inyección cero | 53,01 kWp | 51 kW (as-built: 51 kWac, generación anual media 70.000 kWh/año, P.E.M. 95.000 €, fecha proyecto 2015) | Mismo alcance y agentes que PR2006 |
| PR2227 – Pozuelo Concepción | Vivienda unifamiliar, cubierta, estructura fija coplanar, autoconsumo instantáneo con inyección de excedentes | 3,64 kWp | 3,0 kWac | — |
| PR2237 – Abantos | Vivienda unifamiliar, cubierta, estructura fija coplanar, con almacenamiento, inyección de excedentes | 11,04 kWp | 9,2 kW (inversores limitados por LGA) | Capacidad de almacenamiento 10 kWh |

Tabla de detalle PR2230-GISA (dos campos FV):

| Parámetro | Campo FV 61,88 kWp | Campo FV 9,1 kWp |
|---|---|---|
| Potencia panel (Wp) | 455 | 455 |
| Inclinación | 33° | 33° |
| Nº inversores | 2 | 1 |
| Potencia inversor (kWac) | 30 | 8 |
| Factor de rendimiento PR (%) | 76,74 | 74,12 |
| Fracción solar SF (%) | 32,43 | 42,70 |
| Producción específica (kWh/kWp/año) | 1449 | 1400 |
| Necesidades de consumo (MWh/año) | 236 | 18,44 |
| Producción anual GFV (MWh/año) | 89,66 | 12,74 |
| Autoconsumo (MWh/año) | 76,5 | 7,88 |
| Importación de red (MWh/año) | 159,4 | 10,57 |
| Exportación a red (MWh/año) | 13,2 | 4,86 |

**Relevancia destacada — caso PR2006-SCH**: es el caso real más próximo estructuralmente al CPD del TFM entre los seis presentados: nave/edificio industrial (talleres, repostaje) con cubierta fija, autoconsumo instantáneo e inyección cero a red de distribución, escala de decenas a ~200 kWp. No es un CPD (no hay perfil de carga 24/7 ni criterios de disponibilidad TIER), pero sirve de referencia de arquitectura eléctrica y de la práctica de "inyección cero" en un entorno con consumo industrial propio.

### 8. Lista Tier-1 de módulos FV

- La lista Tier-1 de Bloomberg (BNEF) clasifica fabricantes de paneles FV por "solvencia y capacidad de financiación", actualizada trimestralmente; **no implica garantía de calidad técnica, rendimiento o eficiencia**.
- Requisitos: financiación bancaria (≥6 proyectos solares de ≥10 MW en 2025 con ≥6 bancos distintos en los últimos dos años); fabricación propia con integración vertical; estabilidad financiera (sin bancarrota ni impago de bonos); proyectos financiados por bancos comerciales (no de desarrollo) y a gran escala.
- Tabla de fabricantes Tier-1 (Q3 2025, ordenados por capacidad; nota de la fuente: cifras estimadas a partir de información pública, verificar con el informe BloombergNEF del trimestre):

| Fabricante | País | Capacidad (GW) | Tecnología principal |
|---|---|---|---|
| LONGi Solar | China | 150 | TOPCon/PERC |
| Tongwei Solar | China | 130 | TOPCon/HJT |
| JA Solar | China | 120 | TOPCon |
| Jinko Solar | China | 110 | TOPCon |
| Trina Solar | China | 105 | TOPCon |
| Canadian Solar | Canadá/China | 90 | TOPCon/Bifacial |
| Risen Energy | China | 60 | PERC/TOPCon |
| First Solar | EE.UU. | 52 | CdTe (película fina) |
| Astronergy (CHINT) | China | 50 | TOPCon |
| Huasun | China | 45 | HJT |
| Seraphim | China | 30 | PERC |
| Eging PV | China | 28 | PERC |
| Suntech | China | 27 | PERC/TOPCon |
| ZNShine | China | 25 | PERC |
| Jolywood | China | 22 | TOPCon |
| Qcells | Corea del Sur | 20 | TOPCon/Q.ANTUM |
| Meyer Burger | Suiza | 12 | HJT / I+D perovskita |

### 9. Gestión, Operación y Mantenimiento (GOM)

- **Agentes implicados**: promotor/propietario, instalador, proyectista, dirección facultativa/de obra, operador/mantenedor, fabricante/suministrador, entidad financiera, comercializadora, distribuidora; y en el ámbito de seguros: asegurador, tomador, asegurado, beneficiario, póliza, prima.
- **Protocolos GOM** (procedimientos de mantenimiento con código PMP_ID y periodicidad): módulo FV (fijación anual; limpieza con agua desmineralizada semestral, sin jabón ni abrasivos); seguidor solar (revisión visual semanal; comprobación/reparación de apriete, engrase, corrosión, deformaciones y cimentación semestral); reapriete anual de tornillería con pares normalizados según Directiva VDI 2230 (Feb. 2003, μA=0,08, μB=0,12): M6=7,8 Nm, M8=19,1 Nm, M10=38,0 Nm, M12=66,5 Nm, M14=107,0 Nm, M16=168,0 Nm; inversor ≤20 kWac (semestral: inspección visual, disipación de calor, limpieza de LEDs/ventiladores/disipadores, apriete de conexiones, comprobación de corrosión y suciedad); cuadros de distribución/protecciones y cableado/conexionado BT (anual: disparo de disyuntores, fusibles, aislamiento, medición de Vca/Icc por string, EPI obligatorio: guantes y herramientas aislantes, botas dieléctricas).
- **Estadística de averías (certificadora alemana TÜV, análisis de >1,5 GW de instalaciones FV en funcionamiento)**: el 50% de los problemas de una instalación FV se origina en los paneles solares; de ese 50%, el 41% se debe a fallos de "bus bar" (conexiones entre células) y el 45% a corrosión y/o degradación del panel.
- **Tipos de avería de módulo**: amarilleamiento/pardeamiento (yellowing/browning) por degradación UV del encapsulante EVA, visible a simple vista, típico de los primeros años y asociado a mala calidad de materiales; Degradación Inducida por Potencial (DIP/PID), favorecida por climas cálidos y húmedos, corriente de fuga de iones entre marco y células a través del EVA y capa antirreflectante, degradación de producción de hasta 30%; propagación de incendios (documentado con casos fotográficos de cubiertas siniestradas).
- Averías de inversor: rotura de descargadores de sobretensión, calentamientos por deficiente instalación/mantenimiento, rotura de condensadores, fallo de ventiladores, averías de electrónica por sobrecargas, fallo de tarjeta de comunicación.
- Averías por defectos de diseño, proyecto e instalación: sobredimensionamiento FV, mala planificación, secciones/protecciones inadecuadas, especificación de materiales incorrectos o incompatibles, errores de cálculo estructural (hasta colapso estructural), fallos de replanteo, defectos de puesta a tierra equipotencial, aislamiento/IP inadecuado, goteras en cubiertas.
- **Tabla de fallos comunes y prácticas inadecuadas** organizada en 4 bloques — 1. Selección de ubicación (orientación norte/oeste, sombreado no estacional, corrosión en zonas de agua salada); 2. Diseño y planificación (carga estructural, resistencia al viento, rayos/puesta a tierra, conexiones eléctricas); 3. Instalación física (sombreado entre filas, corrosión, configuración de campo FV, inversor mal ubicado, cableado, conductores, baterías mal instaladas); 4. Seguridad (EPI de caídas, condiciones adversas, medidas de organización/estructurales/técnicas en caso de incendio) — y mantenimiento/inspección (técnico y a cargo del propietario).
- **Durabilidad de la instalación**: 25-30 años mínimo con módulo/inversor de calidad y mantenimiento adecuado (pueden seguir funcionando más años con menor producción por degradación modular). En España, el **RD 1565/2010** (derogado en 2014 por el **RD 413/2014** y la **Orden IET/1045/2014**) fija la vida útil regulatoria de las instalaciones FV en 30 años para el cálculo de rentabilidad razonable. Caso "Apolo II" (Dictamen Pericial de Durabilidad, nov. 2011): ensayo probado ante notario sobre módulos con 36 años de uso (1975-2011) y escaso mantenimiento, con degradación total del 4% en un modelo y del 23-32% en otro; conclusión del dictamen (p. 23, apdo. 4): "en el peor de los casos observados y estudiados, la durabilidad de los paneles o módulos fotovoltaicos atendiendo exclusivamente a ellos mismos, se puede establecer en una vida media de 50 años".
- **Documentación exigible en caso de siniestro**: memoria técnica o proyecto técnico con presupuesto de ejecución; factura de ejecución de la instalación; CIE; inspecciones periódicas; contrato de venta/compensación de excedentes o acuerdo de reparto, en su caso; licencia de actividad de venta de energía no acogida a compensación; comunicación formal del siniestro a la aseguradora en plazo contractual; documentación probatoria de daños (fotos, vídeos, actas notariales); facturas de bienes siniestrados; facturas y curvas de carga horarias de los últimos 12 meses; registros completos de inversores de al menos 12 meses; registros horarios de energía producida (contador FV) y de irradiancia (si hay CTE) de al menos 12 meses.

## Datos clave (con página de origen)

- Fórmula de potencia mínima FV obligatoria (CTE DB-HE5): $P_{min}=\min(F_{pr;el}\times S,\ 0,1\times(0,5S_c-S_{oc}))$, con $F_{pr;el}$= 0,005 kW/m² (residencial) o 0,010 kW/m² (resto) (p. 7).
- **PR2006-SCH** (caso real más próximo al CPD): 186,45 kWp pico / 185 kW nominal, autoconsumo instantáneo con inyección cero a red, cubierta industrial de Sanchinarro-EMT Madrid, 2015 (pp. 17-18); nota: el panel as-built del mismo proyecto cita 100 kWac nominal y 140.000 kWh/año de generación media, P.E.M. 186.000 € — discrepancia no resuelta en la fuente.
- PR2005-CERRO: 53,01 kWp pico / 51 kW nominal, mismo esquema de inyección cero, generación anual media 70.000 kWh/año, P.E.M. 95.000 € (pp. 19-20).
- Estadística TÜV sobre >1,5 GW de instalaciones FV: 50% de averías originadas en paneles; de ese 50%, 41% por "bus bar" y 45% por corrosión/degradación (p. 36).
- Vida útil regulatoria española de instalaciones FV: 30 años (RD 413/2014 + Orden IET/1045/2014), frente a una vida media observada de hasta 50 años en el caso pericial Apolo II (2011) (pp. 75-76).
- Pares de apriete normalizados de tornillería de estructura/seguidor (Directiva VDI 2230): M6=7,8 Nm; M8=19,1 Nm; M10=38,0 Nm; M12=66,5 Nm; M14=107,0 Nm; M16=168,0 Nm (p. 31).
- Normativa de construcción/seguridad citada sin necesidad de verificación cruzada (fuera del Excel de normativa del TFM): RD 1627/1997 (Seguridad y Salud en obras), RD 1955/2000 y RD 1699/2011 (acceso y conexión a red), RD 413/2014 y Orden IET/1045/2014 (retribución y vida útil regulatoria FV).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: principalmente capítulos de tramitación administrativa y de gestión/operación/mantenimiento (GOM) de la instalación; el caso PR2006-SCH puede aportar un punto de comparación cualitativo en la introducción o discusión sobre inyección cero en entornos industriales.
- **Qué aporta exactamente**: contexto de procedimiento (fases, documentación mínima, trámites por tramo de potencia) y una checklist de fallos/prácticas inadecuadas y protocolos de mantenimiento útiles como referencia de buenas prácticas de diseño, aunque no aporta cifras de cálculo trasladables directamente al CPD salvo la referencia estructural del caso PR2006-SCH.
- **Confianza en los datos**: todas las cifras citadas provienen literalmente de las diapositivas indicadas; la discrepancia de potencia nominal en PR2006-SCH (185 kW en la diapositiva de resumen vs. 100 kWac en el panel as-built) se señala explícitamente y no se resuelve, pues no aparece aclaración en la fuente.

## Notas de procesamiento

- Densidad Ejecutiva fijada por el encargo (tema de prioridad baja según clasificación de Mario), sin preguntar nivel de densidad.
- Documento de 79 páginas. Leídas íntegramente las páginas 1-40 y 60-79. **Se omitieron las páginas 41-59** (contenido correspondiente al resto del bloque "3. Averías de módulos FV" dentro de GOM — previsiblemente más tipologías de fallo entre "Amarilleamiento/DIP" (p. 40) y "Propagación de incendios" (p. 60), como microfisuras, hot-spots, delaminación o daños por granizo) por tratarse de contenido de detalle adicional dentro de una sección ya cubierta con ejemplos representativos, coherente con el nivel Ejecutivo solicitado.
- No se ha podido verificar el documento externo "NORMATIVA FV-2025" ni "TRAMITES_LEGALIZACIONES FV AUTOCON_CONECTADO RED" citados como referencias en las diapositivas 5 y 13: son documentos aparte no incluidos en este PDF.
- Todas las imágenes de averías, esquemas unifilares y fichas de proyecto son descriptivas; no se han podido extraer valores numéricos adicionales de las imágenes de baja resolución (p. ej. planos de PR2005/PR2006) más allá del texto legible en las fichas de proyecto.
