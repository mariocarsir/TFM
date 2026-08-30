---
title: "Tipologías de Autoconsumo, configuraciones de medida y esquemas de conexión"
tipo: presentacion
autor: "Alberto Espliego Fernández (Servicio Técnico Especializado UFD)"
anio: 2025
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T11_EsquemasConexion.pdf"
tags: [fotovoltaica, autoconsumo, esquemas-conexion, proteccion-electrica, configuraciones-medida, BT, MT, REBT, ITC-BT-40, RD-1699-2011, ERMA]
related: [introduccion-autoconsumo-fotovoltaico-m6t2, fases-documentacion-autoconsumo-fv]
---

# Tipologías de Autoconsumo, configuraciones de medida y esquemas de conexión (Alberto Espliego Fernández, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición (2025-2026), impartida por un técnico de UFD (distribuidora, Servicio Técnico Especializado). Desarrolla de forma completa el marco normativo del autoconsumo eléctrico español, la clasificación de las 5 variables que definen cada tipología de autoconsumo (Clasificación, Modalidad, Proximidad, Modo de Funcionamiento, Tecnología), las 4 configuraciones de medida oficiales (A/B/C/D) tanto en BT como en MT, y los esquemas de conexión eléctrica más frecuentes (5 casos en BT, 2 casos en MT) con el detalle de elementos, envolventes y protecciones exigidas. El núcleo técnico más denso son las tablas de tarados exactos de los relés de protección obligatorios (Anti-Isla UNE-EN 62116, mínima/máxima tensión, frecuencia, sincronismo) tanto para instalaciones de generación en BT como para las protecciones generales en Centros de Transformación en MT (funciones ANSI 50, 51, 67N, 27L, 59, 81, 27B, 25). El documento distingue explícitamente las responsabilidades no resueltas por la normativa actual (certificación de inversores, verificación de Sistemas Anti-Vertido) y anuncia una actualización inminente de las ITC-BT-12/23/40/53 (prevista 1er trimestre de 2026).

## Contenido técnico

### 0. Portada e índice

- Máster en Energías Renovables y Medio Ambiente (ERMA), 20ª edición, 2025-2026, UPM.
- Módulo 6: Autoconsumo Fotovoltaico.
- Título de la sesión: "Tipologías de Autoconsumo, configuraciones de medida y esquemas de conexión".
- Ponente: **Alberto Espliego Fernández** (Servicio Técnico Especializado UFD, distribuidora eléctrica).
- Índice de la presentación:
  1. Tipologías de Autoconsumo (normativa aplicable + tipologías)
  2. Configuraciones de Medida (genéricas + opcionales)
  3. Esquemas de conexión BT (selección, elementos, requisitos técnicos, 5 casos frecuentes)
  4. Esquemas de conexión MT (selección, elementos, requisitos técnicos, 2 casos frecuentes)

### 1. Tipologías de Autoconsumo

#### 1.1 Normativa y legislación aplicable (p. 3)

Cada tipología de Autoconsumo resulta de la combinación de **cinco elementos**:
- **Clasificación**: Individual o Colectivo.
- **Modalidad**: SIN Excedentes o CON Excedentes (con "Compensación" o con "Venta").
- **Proximidad**: en Red INTERIOR (Instalación Interior/Enlace), a través de RED DISTRIBUCIÓN, MIXTO o COMPARTIDO.
- **Modo de Funcionamiento** (RD 1699/2011 e ITC-BT-40): Dependiente o Separado.
- **Tecnología de generación**: Renovable-Cogeneración-Residuos (REN-CO-RES) o de otro tipo.

Marco normativo completo citado (orden cronológico de la diapositiva):

| Norma | Fecha | Contenido |
|---|---|---|
| RDL 15/2018 | 5 de octubre de 2018 | Medidas urgentes para la transición energética; modifica las tipologías de Autoconsumo |
| RD 244/2019 | 5 de abril de 2019 (consolidado dic. 2022) | Junto con RDL 15/2018 e ITC-BT-40 (sept. 2013), conforma las 5 variables de tipología de Autoconsumo |
| ITC-BT-40 | septiembre de 2013 | Guía de aplicación; define protecciones/relés |
| RD 842/2002 | 2 de agosto de 2002 | Aprueba el Reglamento Electrotécnico para Baja Tensión (REBT) |
| Guía de aplicación ITC-BT-23 | noviembre de 2017 | Protección contra Sobretensiones; establece cómo deben protegerse las instalaciones |
| RD 1110/2007 | 24 de agosto de 2007 | Reglamento Unificado de puntos de medida del sistema eléctrico |
| RD 244/2019 | 5 de abril de 2019 | Modifica RD 1110/2007: todos los suministros Tipo 5 deben disponer de "Contadores Telegestionados", y preferentemente los de Tipo 4 y 3 |
| Orden TEC/1281/2019 | 19 de diciembre de 2019 | Aprueba nuevas ITCs y las configuraciones de medida específicas para Autoconsumo (incluidas medidas en "Serie") |
| RD 614/2001 | 8 de junio de 2001 | Junto con su "Guía técnica para la evaluación y prevención del riesgo eléctrico" (mayo 2014), cataloga qué elementos se consideran Interruptor-seccionador de corte en carga |
| Guía de aplicación ITC-BT-40 | septiembre de 2013 | Establece la necesidad de disponer de un Interruptor de corte en carga accesible a la distribuidora en el punto de medida (acceso directo libre y permanente) |
| RD 1699/2011 | 18 de noviembre de 2011 | Regula la conexión a red de instalaciones de producción de pequeña potencia (hasta 100 kW); junto con la guía de la ITC-BT-40 (sept. 2013) establecen todas las "Protecciones/Relés" necesarias |
| Resolución CNMC | 20 de mayo de 2021 | Establece cómo determinar la capacidad de acceso de generación a la red de distribución (≤100 kW en un punto de la red BT y Σ≤175 kW en una Salida BT y Σ≤400 kW en el conjunto del CT) |
| RDL 29/2021 | 21 de diciembre de 2021 | Autoriza el autoconsumo entre suministros e instalaciones en BT y AT, al incluir la "proximidad" en función de la distancia (hasta 2.000 m) independientemente del nivel de tensión |
| INF/DE/478/23 | 16 de mayo de 2024 (CNMC) | Aprueba nuevos formatos de los ficheros de intercambio de información entre distribuidores y comercializadores (versión 3.0) |

**Nota destacada en la diapositiva (recuadro azul)**: "El Ministerio va a actualizar múltiples ITCs del REBT e ITC-RAT-09 (previsiblemente 1er trimestre 2026) para unificar y normalizar todos los requisitos y elementos derivados de esta normativa: Relé Anti-Isla, Sistema Anti-Vertido (SAV), Protector Sobretensiones, Filtro PLC, Interruptor de Corte en Carga, etc..."

#### 1.2 Tipologías de Autoconsumo genéricas según la CNMC (p. 4)

- La CNMC ha establecido **30 códigos "Administrativos" de Autoconsumo** (con sus fórmulas de medida, facturación y liquidación específicas, y con sus características de titularidad y contractuales concretas).
- Desde el punto de vista de las instalaciones y medida, esos 30 códigos se resumen en distintas **TIPOLOGÍAS DE AUTOCONSUMO**:
  - **56 tipologías en BT**
  - **38 tipologías en MT**
  - **22 tipologías Combinadas MT/BT**
- Cada tipología implica una configuración de medida concreta que posteriormente se subdivide en varios esquemas de conexión distintos dependiendo de las potencias y tipos de fincas o suministros.
- Las tablas de la diapositiva (formato extenso, "Tipología de Autoconsumo BT" y "Tipología de Autoconsumo MT") desglosan cada código por: Clasificación/Modalidad/Proximidad/Tecnología/Medida (nombre y apellidos), código CNMC de la Tabla T13, código de medida y posible participación en Autoconsumo Combinado MT/BT. (No se reproducen aquí las ~90 filas completas; el detalle exacto de cada código concreto no es indispensable para el TFM y está disponible en la fuente original si Mario necesita un código específico).

#### 1.3 Tipologías de Autoconsumo BT — diagrama de decisión (p. 5)

Diagrama de flujo con 6 niveles de decisión, de arriba a abajo:

1. **MODALIDAD/CLASIFICACIÓN**: INDIVIDUAL (un único consumidor asociado a uno o varios productores) ↔ COLECTIVO (varios consumidores asociados a uno o varios productores).
2. **MODALIDAD**: CON Excedentes (posible vertido a la red, con Compensación ≤100 kW o con Venta de excedentes) ↔ SIN Excedentes (prohibido verter a la red, precisa de un Sistema Anti-Vertido - SAV). Reglas de flujo: "SOLO CON VENTA" y "SOLO COLECTIVOS" limitan qué combinaciones son posibles hacia Compartido/Mixto.
3. **PROXIMIDAD**: En Red INTERIOR ↔ COMPARTIDO ↔ MIXTO ↔ A través Red DISTRIBUCIÓN (interconexión consumo-generación en instalación interior (CGMP) o en instalación de enlace (CC-CDM-CGP), frente a interconexión a través de la red de distribución, que implica pago de PEAJES, 0 €).
4. **MODO DE FUNCIONAMIENTO**: DEPENDIENTE (ausencia de tensión en la red de distribución = desconectar todos los sistemas de generación) ↔ SEPARADO (ausencia de tensión = posible funcionar en "Isla" separado de la red, precisa de Conmutación).
5. **TECNOLOGÍA/TITULARIDAD**: REN-CO-RES Y MISMO TITULAR ↔ NO REN-CO-RES O DISTINTO TITULAR (precisa medir generación "Neta").
6. **CONFIGURACIÓN DE MEDIDA**: A "SOLO FRONTERAS" (Genérica) ↔ B/C "FRONTERA+GEN. NETA" ("D" Opcional).

Conclusión del flujo: "El esquema de conexión que determina las envolventes y elementos del punto de medida depende del TIPO DE FINCA y de la POTENCIA": FINCA 1-2 suministros (CPM) o Multi-suministro (CC-CMI) ← → P ≤ 50 kW (Medida Directa) o P > 50 kW (Medida Indirecta).

**Nota destacada**: "Hay múltiples combinaciones de los elementos anteriores que dan lugar a **56 tipologías de Autoconsumo (CNMC)**. Cada una implica una configuración de medida y un esquema de conexión distinto (**151** esquemas) con sus envolventes y/o elementos en los Puntos de Medida o CGMP."

#### 1.4 Tipologías de Autoconsumo MT — diagrama de decisión (p. 6)

Mismo esquema de 6 niveles, con diferencias específicas de MT:
- Proximidad en Red Interior en BT (CGMP, CPM, CGP o CBT) o CPMC en AT; interconexión a través de red distribución o Centro de Seccionamiento (implica pago de peajes).
- Modo de funcionamiento: **GENERAL** (dependiente, ausencia de red = desconectar generación; instalación equipotencial y con disparo y sincronismo en BT sobre 52-G) ↔ **EXCEPCIONAL** (separado, precisa conmutación; o CT alejado de CPMC o no equipotencial -protección en CT- o disparo y sincronismo en AT sobre 52-I).
- Conclusión: esquema de conexión depende del tipo de CT (CT aéreo o ≤50 kVA con CPM en BT, o Resto con celda de medida en AT) y de la potencia: P ≤ 1000 kVA (fusible) o P > 1000 kVA (interruptor).

**Nota destacada**: "Hay múltiples combinaciones de los elementos anteriores que dan lugar a **38 tipologías de Autoconsumo (CNMC)**. Cada una implica una configuración de la medida y un esquema de conexión distinto (**316** esquemas) con sus envolventes y/o elementos en los Puntos de Medida o BT."

#### 1.5 Tipologías de Autoconsumo Combinados MT/BT (p. 7)

Diferencias respecto a BT/MT individuales:
- Siempre CON Excedentes (con Compensación 100 kW o con Venta de excedentes); no existe la modalidad "Sin Excedentes".
- Proximidad: Compartido, Mixto o A través Red Distribución (≤500 m o en la misma finca y a través de red).
- Tipo de conexión: siempre DEPENDIENTE (no es posible funcionar en "Isla" separado de la red).
- Conclusión: esquema de conexión depende del nivel de tensión y de las potencias. En BT: 50 kW medida directa o indirecta. En AT: requisitos AT, 1000 kVA fusible o interruptor.

**Nota destacada**: "Hay múltiples combinaciones de los elementos anteriores que dan lugar a **22 tipologías de Autoconsumo (CNMC)**. Cada una implica una configuración de la medida y un esquema de conexión distinto (**¿?**, cifra no facilitada en la fuente) con sus envolventes y/o elementos en los Puntos de Medida o BT."

#### 1.6 Proximidad — condiciones detalladas (p. 8)

Las instalaciones de producción/generación son PRÓXIMAS a los suministros de consumo (y por tanto se pueden asociar a un mismo Autoconsumo, CAU) cuando se cumple alguna de las siguientes condiciones:

i. Estén conectadas a la red interior de los consumidores asociados o estén unidas a éstos a través de líneas directas.
ii. Estén conectadas a cualquiera de las redes de baja tensión derivadas del mismo centro de transformación.
iii. Se encuentren conectadas a una **distancia inferior a 500 metros** de los consumidores asociados (en BT o en AT). En caso de fotovoltaicas en cubierta o suelo industrial conectadas a través de red, el límite se amplía a **2.000 metros**.
iv. Estén ubicadas en una misma referencia catastral según sus primeros **14 dígitos** (finca, vía y nº, o parcela rural).

**Nota destacada (recuadro azul)**: "OJO al intentar asociar varias instalaciones de generación al mismo autoconsumo (CAU), pues todas las instalaciones de generación deben considerarse 'Próximas' a todos los suministros de consumo asociados. A veces es mejor configurar distintos autoconsumos." Un recuadro amarillo "OJO" en un ejemplo de imagen aérea señala que "TEÓRICAMENTE SOLO ESTOS SUMINISTROS DE CONSUMO SE PUEDEN ASOCIAR A AMBAS INSTALACIONES DE GENERACIÓN".

### 2. Configuraciones de Medida

#### 2.1 Configuraciones genéricas en BT (p. 9)

La CNMC, de acuerdo con el RD 244/2019 y la Orden TEC/1281/2019, estableció **4 Configuraciones de Medida**: 3 genéricas (A, B, C) y 1 opcional (D):

| Esquema de Medida | Descripción |
|---|---|
| **A** | Medida bidireccional en la Frontera del Consumidor con generación en una instalación interior (medida "Única" en la instalación de enlace) |
| **B** | Medida bidireccional de la Frontera de Consumidores con generación en una instalación interior (en las instalaciones de enlace) + medida de la "Energía Neta" generada (medida en la instalación en "Serie" con la medida de la frontera) |
| **C** | Medida de todos los "Consumo total" de todos los consumidores asociados + Medida bidireccional de la "Energía Neta" generada (todas las medidas de consumo y generación neta se realizan en las instalaciones de enlace y en "Paralelo" entre sí) |
| **D** (Opcional) | Medida del "Consumo total" de todos los consumidores asociados + Medida de la "Generación Bruta" + Medida del "Consumo de los Servicios Auxiliares" (todas las medidas de consumo, generación bruta y servicios auxiliares se realizan en las instalaciones de enlace y en "Paralelo" entre sí) |
| **E** (Excepcional) | Esquema de Medida "Singular" (previa aprobación por la administración competente) |

Leyenda de esquemas de medida (símbolos usados en todos los diagramas siguientes): Red-Acometida distribución (bidireccional), Derivación individual, Línea general, Medida Frontera Consumidor Bidireccional (Wh), Medida Generación Neta (Wh), Medida Consumo Total (Wh), Medida Servicios Auxiliares, Otros Suministros No Asociados, Instalación de Consumo Asociado, Instalación de Producción Asociada (1 o más instalaciones con mismo titular).

**Nota destacada**: "La configuración de medida 'A' es la genérica para cualquier tipología de Autoconsumo **individual** conectado en la instalación interior (CGMP) del suministro de consumo asociado."

Detalle "CONFIGURACIÓN A" (Genérica: Individual en CGMP de instalación interior, 1 contador bidireccional en Frontera del Consumidor):
- Fincas 1 suministro (con CPM): 1 contador Wh en CPM → CGMP.
- Fincas 2 suministros (con CPM2): 2 contadores Wh → 2 CGMP.
- Fincas ≥ 2 suministros (con CGP + CC/MMI): centralización o MMI en cuarto de contadores → CGMP + otros suministros no asociados.
- Ubicación medida del SAV en CGMP en autoconsumos sin excedentes: esquema con IGA, SAV, PST tipo 2, diferencial (DIF.), circuitos interiores de consumo.

Dos recuadros rojos destacados:
- "En caso de autoconsumos SIN EXCEDENTES, el Sistema Anti-Vertido (SAV) deberá instalarse en el CGMP (Cuadro General de mando y Protección) situado en la instalación interior del suministro de consumo asociado."
- "En caso de autoconsumos INDIVIDUALES en RED INTERIOR con un único contador en el Punto Frontera, y para garantizar el correcto funcionamiento del ICP interno del contador telegestionado, la instalación de generación siempre debe conectarse en el CGMP de la instalación interior (detrás de la IGA y Diferencial), y NO en la CPM, MMI o Centralización del Punto de Medida."

#### 2.2 Configuración B en BT — variantes (p. 10)

Config. "B" (medida de la generación "Neta" en SERIE) es la genérica cuando la generación se conecta en la instalación interior (CGMP) de uno de los suministros de consumo asociados, en cualquiera de los siguientes casos:
- Si la generación NO es de tipo Renovable, Cogeneración o Residuos.
- Si la generación pertenece a un titular distinto al del consumo (puede precisar de un contrato para los servicios auxiliares).
- Si se trata de una Hibridación (combinación de Cogeneración y Autoconsumo en un mismo suministro).
- Si se trata de un autoconsumo colectivo compartido o mixto.

Cuatro subvariantes ilustradas con diagramas completos de contadores/CPM/CGMP:
- **B(II)** — Individual en red interior: en "Serie" en CGMP de instalación interior (1 contador bidireccional en Frontera del Consumidor + 1 contador en cada Generación Neta).
- **B(CC)** — Colectivo Compartido: a través de red y en "Serie" en CGMP de suministro con generación (1 contador bidireccional en Frontera de cada consumidor + 1 contador en cada Generación Neta en CPM).
- **B(IM)** — Individual Mixto: a través de red distribución y en "Serie" en CGMP de instalación interior (1 contador bidireccional en Frontera del Consumidor + 1 contador en cada Generación Neta).
- **B(CM)** — Colectivo Mixto: a través de red distribución y en "Serie" en CGMP (1 contador bidireccional en Frontera de cada consumidor + 1 contador en cada Generación Neta en CPM).

Dos recuadros destacados:
- "Cuando el contador para medida de la generación 'Neta' se instala en SERIE con el del Punto Frontera, dicho contador de la generación neta NO hace falta ubicarlo en el límite de la propiedad."
- "OJO — En edificios en régimen de propiedad horizontal, las instalaciones de producción en autoconsumos 'Colectivos' NO pueden conectarse en la instalación interior de ninguno de los consumidores asociados."
- "En la configuración 'B' cuando la instalación generadora se conecta en el CGMP de la instalación interior del suministro de consumo asociado, la CPM para medir la Generación 'Neta' se instalará en 'SERIE' con la medida del 'Punto Frontera' cerca de la generación."

#### 2.3 Configuración C en BT — variantes (p. 11)

Config. "C" (medida de la generación "Neta" en PARALELO) es la genérica cuando la generación se conecta en la instalación de enlace (de otros suministros de consumo asociados o propias, para volcar toda su energía a través de la red de distribución).

Seis subvariantes con diagramas completos:
- **C(II)** — Individual en red interior, "Paralelo" en instalación de enlace (1 contador en Consumo Total + 1 contador bidireccional en cada Generación Neta).
- **C(CI)** — Colectivo en red interior, "Paralelo" en instalación de enlace.
- **C(IR)** — Individual a través de Red de distribución (1 contador bidireccional en Frontera del Consumidor + 1 contador en cada Generación Neta).
- **C(CR)** — Colectivo a través de Red de distribución (1 contador bidireccional en Frontera de cada consumidor + 1 contador en cada Generación Neta en CPM).
- **C(IM)** — Individual Mixto: a través de red distribución y en "Paralelo" en instalación de enlace.
- **C(CM)** — Colectivo Mixto: a través de red distribución y en "Paralelo" en instalación de enlace.

Detalle adicional: "Ubicación medida del SAV en IGM (si Centralización), en CDM (si Derivación LGA), en Autoconsumos Colectivos sin excedentes: generación → IGM-MLD (o CDM-PST) → columnas de medida (consumo) → columnas de medida (generación)".

**Nota destacada**: "La configuración 'C' es la utilizada siempre en los autoconsumos 'a través de la red de distribución', y como opción a los autoconsumos con configuración 'B' (aunque implica instalaciones más caras) pero con todas las medidas de generación y consumo en 'PARALELO'."

#### 2.4 Configuraciones opcionales en BT — Configuración D (p. 12)

La configuración de medida "D" es **opcional** (siempre puede ser sustituida por una configuración "B" o "C"), y solo es aplicable a los "Autoconsumos con VENTA DE EXCEDENTES", pero encarece bastante la instalación del punto de medida debido a que:
- Todas las medidas se realizan en paralelo y deben realizarse en un punto de medida accesible a la distribuidora.
- Todos los circuitos (Consumo, Generación Bruta y Servicios Auxiliares) deben converger en el punto de medida.
- Se precisan envolventes más grandes para alojar los contadores (muchas veces debe instalarse una centralización de contadores).

Diagrama de transición: Esquema Medida "A" → PASO A OPCIÓN → Esquema Medida "C" → PASO A OPCIÓN "D" → Esquema Medida "D" (con nota: necesita CGP en límite de propiedad, necesita conjunto de CPMs en límite de la propiedad o centralización/armario de contadores, circuitos de servicios auxiliares y de recarga).

Tres subvariantes: **D(II)** (Individual en red interior, "Paralelo" en instalación de enlace: 1 contador en Consumo Total + 1 contador en cada Generación Bruta + 1 contador en cada SS.AA.); **D(IR)** (Individual a través de Red de distribución); **D(IM)** (Individual Mixto: a través red Distribución y en "Paralelo" en instalación de enlace).

**Nota destacada (recuadro azul)**: "Es aconsejable no optar por la configuración 'C' (como opción a los esquemas 'A' o 'B') ni la configuración 'D' (como opción a cualquier otro esquema de medida) pues encarecen y complican mucho las instalaciones de enlace y de medida; tanto en lo que afecta a las envolventes que conforman la propia Medida, como el tendido de los circuitos de cada instalación (Consumo, Generación y Servicios Auxiliares) hasta la misma."

#### 2.5 Configuraciones genéricas en MT (p. 13)

Misma estructura de 4 configuraciones (A/B/C/D) + E excepcional que en BT, con la misma descripción textual. Diferencias en MT:

- La forma de realizar la medida depende del **tipo de CT**, de la **potencia de transformación** y de la **potencia de la instalación de generación**:
  - CT "intemperie sobre poste" en una CPM en BT.
  - CT "Pie de Apoyo" o "interior" de Potencia ≤ 50 kVA en una CPM en BT.
  - CT "Pie de Apoyo" de Potencia 50 < Pot. ≤ 400 kVA en el CT en MT.
  - CT "interior" de Potencia 50 < Pot. ≤ 4000 kVA en un CPMC en MT.
  - CT de potencia ≥ 4000 kVA en una subestación o en AT (Un > 36 kV).

- La configuración de las protecciones necesarias depende también del tipo de CT, de la potencia de transformación y de la potencia de la instalación de generación, y además de la presencia o no de un Sistema Anti-Vertido (SAV):
  - CT "intemperie sobre poste" o "Pie de Apoyo": fusibles XS y 59N.
  - CT "interior" Pot. ≤ 1000 y Pg ≤ 100 kW: celda fusibles y 59N.
  - CT 1000 < Pot. ≤ 4000 kVA y Pg ≤ 100 kW: celda interruptor, 50, 51, 67 y 59N.
  - Si Pg > 100 kW: celda interruptor, 50, 51, 67, 27, 59, 81 y 59N.

Leyenda del diagrama MT: Celda Línea → Trafo x kVA → CPM → Cuadro BT → Red de distribución (medida frontera consumidor bidireccional); Celda Protección y Medida homopolar (Wh, medida generación neta); Celda medida consumo total; Medida generación bruta (en red interior); Medida servicios auxiliares; Instalación de consumo asociado; Instalación de producción asociada; CGP o Cuadro BT (con BTVCs).

Recuadro rojo: "En caso de autoconsumos MT SIN EXCEDENTES, el Sistema Anti-Vertido (SAV) deberá instalarse bien en BT: en el CGMP de la instalación interior en BT o en el Cuadro BT del CT del suministro de consumo asociado, o bien en MT en la celda de medida situada en el CPMC (Centro de Protección y Medida del Cliente)."

#### 2.6 Configuración A MT — diagramas detallados (p. 14)

La configuración de medida en MT es mucho más complicada que en BT pues hay que tener en cuenta muchos más elementos: Tipo de CT, Potencia de transformación, Potencia de generación, nº de Trafos. La configuración "A" es la genérica para cualquier tipología de Autoconsumo individual conectado en la instalación interior en BT del suministro de consumo asociado.

Casos ilustrados: CT intemperie sobre apoyo P ≤ 400 kVA; CT a pie de apoyo P ≤ 50 kVA (opcional); CT a pie de apoyo 50 < P ≤ 400 kVA; CT interior P ≤ 50 kVA (opcional); CT interior P ≤ 1000 kVA (Pgener. ≤ 100 kW); CT interior 1000 < P ≤ 4000 kVA (Pgener. ≤ 100 kW); suministro MT con varios trafos (Pgener. ≤ 100 kW); suministro MT con varios trafos (100 < Pgener. ≤ 4000 kW).

**Nota destacada**: "En los suministros MT con medida en BT, la medida se realiza en una CPM como la de los suministros BT, pero en aquellos en los que la medida se realiza en MT, dicha medida se realizará en un CPMC (Centro de Protección y Medida del Cliente) situado cerca del Centro de Seccionamiento de la distribuidora que además de la Celda de Medida incorpora los equipos y elementos necesarios para la protección del suministro MT (Según legislación vigente)."

#### 2.7 Configuración B MT — muchas variantes (p. 15)

"La configuración de medida 'B' (con medida de la generación 'Neta') tiene muchas variantes": combinaciones de generación conectada a través de Red de Distribución, Red Interior (CPMC o CT con CPM), varios trafos, distintas potencias, incluyendo un caso marcado explícitamente como **"CONFIGURACIÓN NO PERMITIDA"** (no pueden existir suministros generadores en MT sin medida en Frontera para Sistemas Autónomos MT).

#### 2.8 Configuraciones C y D en MT (p. 16)

"Las configuraciones de medida 'C' y 'D' tienen muchas más variantes, y aunque son posibles hay que tratar de evitarlas." Diagrama de transición Esquema A → Esquema C → Esquema D, con nota: "Al fluir de necesitar una única celda de medida en MT y adicionalmente una celda de medida en BT (si el consumo se mide en MT), necesitaría una celda de línea en el circuito de cada circuito, necesitaría traf. y las celdas de medida en cada circuito, generación auxiliares y de generación en cada línea."

**Nota destacada**: "Es aconsejable no optar por las configuraciones 'C' y 'D' de medida pues encarecen y complican bastante la instalación, tanto de la propia Medida como los circuitos hasta la misma de cada instalación (Consumo, Generación y Servicios Auxiliares)."

### 3. Esquemas de conexión BT

#### 3.1 Selección del "Esquema de Conexión" en BT (p. 17)

Metodología en 4 pasos, usando tablas-anexo referenciadas (no incluidas en esta presentación, remiten a "Anexo 07" y "Anexo 06" de un documento externo):

1. Conocer la "Tipología" del Autoconsumo (mediante "Nombre y Apellidos" —primeras 5 columnas— o mediante "Codificación CNMC" —1ª columna amarilla—).
2. Determinar el "Esquema de Conexión" (2ª columna amarilla) en función de tipo de finca y potencias.
3. Consultar el "Esquema de Conexión" en modo "Dependiente" (en el Anexo 07, según el número de la 2ª columna amarilla).
4. Si el modo es "Separado", ver cómo se debe instalar el Sistema de Conmutación (Figuras del Anexo 06).

Variables completas de clasificación repetidas:
- **Clasificación**: Individual, Colectivo.
- **Modalidad**: Sin Excedentes, Con Compensación de Excedentes, Con Venta de Excedentes.
- **Proximidad**: Instalación Interior (CGMP), Instalación de Enlace, A través de Red de Distribución, Mixta (2= Instalación interior y red distribución), Compartida (1 Interior y consumo a través de red).
- **Tecnología**: Renovable-Cogeneración-Residuos, Renovable P ≤ 100 kW, NO Ren-Co-Res, Cualquiera.
- **Esquema Medida**: A; B(II), B(IM), B(CI), B(CC), B(CM); C(II), C(IR), C(IM), C(CI), C(CC), C(CR), C(CM); D(II), D(IR), D(IM) (Opcional).
- **Tipo Conexión**: Finca 1 suministro (CPM); Finca 2 suministros (CPM); Finca multisuministro (CGP + CC o CMI); Directa a red distribución (CPM, CC-CMI).
- **Potencia Gen.**: Pg ≤ 50 kW (Directa CPM o CC); 50 < Pg ≤ 100 kW (Indirecta CPM o CMI); 100 < Pg ≤ 400 kW (Indirecta CPM o CMI).
- **Potencia Con.**: Pc ≤ 50 kW (Directa CPM o CC); 50 < Pc ≤ 100 kW (Indirecta CPM o CMI); 100 < Pc ≤ 400 kW (Indirecta CPM o CMI).
- **Modo Funcionamiento**: Dependiente, Separado.

La tabla de la derecha (extensa) numera esquemas de conexión del 1 al ~29 con columnas: Clasificación Autoconsumo / Modalidad de Autoconsumo / Punto de Conexión entre consumo y generación / Tecnología de Generación / Esquema de Conexión / Contraprestación con la medida / Tipología CNMC / Tipo de instalaciones y potencias / Potencia instalación consumo asociado / Potencia instalación generación asociada / Modo de funcionamiento / Esquema de conexión / Disposición de elementos. Un ejemplo desarrollado ("ESQUEMA 7"): Individual - Sin Excedentes - en CGMP con Red Interior - Generación (NO Ren-Co-Res) - Finca 1 Suministro - 50 < Pg ≤ 400 kW y Pc ≤ 50 kW - Modo Dependiente, con su diagrama de circuito correspondiente (contador bidireccional en frontera + SAV en instalación interior CGMP).

#### 3.2 Elementos asociados al autoconsumo en BT (p. 18)

Principales elementos que puede ser necesario instalar en un autoconsumo:

- **Protector contra sobretensiones transitorias** — **PST Tipo 1** ("Protector Sobretensiones Transitorias Tipo 1"): debe situarse antes de los equipos de medida y descargar las mismas hacia el Borne de Tierra de Protección de la Finca (si la intensidad nominal del conjunto es >125 A precisa de fusibles previos propios).
- **Espacio para poder instalar un filtro PLC** ("Power Line Carrier") u otros elementos de gestión del suministro: espacio reservado por parte de UFD en los suministros que introduzcan "Ruidos" que impidan la Telegestión de los Contadores.
- **Interruptor de Maniobra Individual (IMI)** de corte en carga en el lado del suministro: donde realizar la 1ª maniobra de corte en carga para aislar el Punto de Medida de posibles retornos de tensión desde el interior del Suministro, manteniendo siempre comunicación con el contador.
- **Sistema Anti-Vertido (SAV)** y su medida aguas arriba del punto de interconexión: equipo de Medida bidireccional del circuito situado aguas arriba del punto de las instalaciones de enlace donde se interconectan las instalaciones de producción con los suministros de consumo asociados, para actuar sobre un interruptor del circuito de generación o sobre los inversores cuando se vaya a verter energía hacia la red de distribución.
- Sistema de conmutación al modo de funcionamiento "Separado" (uso muy infrecuente).
- **CDMLG** ("Caja Derivación y Medida de la Línea General"): caja que permite derivar una LGA "Principal" (con posibilidad de medida para un SPL o MAV) en hasta 5 LGAs "Derivadas", estando cada una de ellas protegida en su origen por una BTVC.
- **CGMP** ("Cuadro General de Mando y Protección"): elementos internos ilustrados: IGA, POP, PST-2, Diferencial, MAV, PIA-1..n.

#### 3.3 Requisitos técnicos para conexión de Autoconsumos en BT (p. 19) — TABLA CRÍTICA DE TARADOS

De acuerdo a toda la legislación vigente, y especialmente según lo estipulado en el **RD 1699/2011** y la **ITC-BT-40**, los elementos y protecciones mínimas que ha de disponer un suministro en BT con sistemas de generación son:

**EN PUNTO DE MEDIDA:**
- Protección fusible en el lado "Red" del Punto de Medida.
- Protector Tipo 1 contra sobretensiones transitorias previo al equipo de medida.
- Medida bidireccional (contadores preferentemente "Telegestionados").
- Reserva de espacio para Filtro PLC (*), SAV u otros equipos de gestión del suministro.
- Interruptor manual de Corte en Carga en el lado "Suministro" del Punto de Medida (NO para Relés).

**INSTALACIÓN INTERIOR:**
- Protector Tipo 2 contra sobretensiones transitorias en el Cuadro General de Mando y Protección.
- Protección externa contra el rayo en las ubicadas a la intemperie no cubiertas por el CTE.
- Protección diferencial (Tipo A 30 mA).

**EN CMPG o INVERSOR (protecciones y tarados exactos):**
- Interruptor automático **52-G**, con relé de enclavamiento, sobre el que actuarán los Relés de protección.
- **Relé Anti-Isla** que cumpla Norma **UNE EN 62116 V2** (con una actuación inferior a **1 segundo**).
- **Dispositivo Sincronizador (25)**: actuar con sincronismo durante mínimo **60 s**.
- **Relé Mínima Tensión (27)**: tarado al **-15%** (máx. **1,5 s**).
- **Relé Máxima Tensión (59)**: tarado al **+10%** (máx. **1,5 s**) y **+15%** (máx. **0,2 s**).
- **Relé de Frecuencia (81)**: tarado entre **48 Hz** (máx. **3 s**) y **50,5 Hz** (máx. **0,5 s**).

(*) Para garantizar la telegestión de los contadores (tanto el suyo propio como el del resto de suministros conectados a la misma red BT) se debe reservar un espacio para poder montar un Filtro PLC aguas abajo del contador (de momento solo existen Filtros PLC para suministros de medida directa, P ≤ 50 kW; en el caso de suministros de medida indirecta el filtro deberá venir incorporado en los Inversores o poder instalarse en los circuitos interiores generadores de ruido).

Tres preguntas retóricas destacadas en recuadros rojos (responsabilidades no resueltas por la normativa vigente):
1. "¿Quién CERTIFICA que los 'INVERSORES' cumplen con todos los requisitos de la norma UNE 217002, para garantizar que no pueden funcionar en 'Isla', que tienen separación galvánica, que no se inyecta continua en la red y que no se generan ni transmiten sobretensiones hacia la red?"
2. "Puesto que los Autoconsumos SIN Excedentes ya no tienen que pedir 'Acceso y Conexión' y la Distribuidora No revisa el proyecto ni verifica/precinta protecciones, ¿Quién CERTIFICA que el 'SISTEMA ANTI-VERTIDO' cumple con los ensayos del nuevo Anexo I de la ITC-BT-40?"
3. "¿Cómo se garantiza el cumplimiento del apartado 4.3.1 de la ITC-BT-40 que limita la potencia máxima de generación a conectar a la red de distribución (Mitad de la capacidad de la Salida) cuando se conectan varias instalaciones de autoconsumo con excedentes < 15 kW en entornos urbanos?"

**Nota destacada final**: "Se van a actualizar totalmente las ITC-BT-12, 23, 40, 53 (y otras ITCs del REBT relacionadas con instalaciones de enlace) para unificar y normalizar en un único Reglamento (el REBT) todo los requisitos técnicos exigibles a las instalaciones con Generación, Almacenamiento y especialmente todas las novedades relacionadas con el Autoconsumo."

#### 3.4 Esquemas de Conexión BT más frecuentes — 5 Casos (p. 20-24)

**Caso 1 (p. 20): INDIVIDUAL - SIN EXCEDENTES - RED INTERIOR - DEPENDIENTE - RENOVABLE**

Corresponde a una finca individual (casa o chalet), con autoconsumo renovable (placas fotovoltaicas) de aproximadamente **3-9 kW** conectado en su instalación interior (en el CGMP) como un circuito más con su PIA, sin excedentes (con sistema anti-vertido y que no precisa pedir permisos de acceso y conexión) y en modo de funcionamiento dependiente (sin posibilidad de funcionamiento en isla).

Elementos numerados (1-22) en el diagrama: 1) Acometida (Derivación en "T" o "Reparto de Red"); 2) Caja de Protección y Medida (CPM); 3) Pletina para posible conexión de red en reparto (entrada/salida); 4) Fusibles de la CPM (protección de la LCI); 5) Protector contra sobretensiones transitorias (Tipo 1); 6) Pletina conexión tierra protección finca; 7) Contador medida directa; 8) Espacio para filtro PLC o equipos de gestión; 9) Interruptor-seccionador de seguridad; 10) Borne para conexión de la LCI; 11) Línea conexión individual de la instalación generadora; 12) Cuadro General de Mando y Protección (CGMP); 13) Interruptor general automático (IGA); 14) Protector contra sobretensiones transitorias (Tipo 2) y temporales (POP); 15) Tierra de protección de la finca; 16) Interruptor diferencial; 17) Medida del mecanismo anti-vertido (MAV); 18) Pequeños interruptores automáticos (PIAs) de circuitos interiores; 19) Línea de conexión individual de la instalación generadora; 20) Instalación generadora - Cuadro Mando y Protección de Generación (CMPG); 21) Instalación generadora (conjunto generación-almacenamiento-inversor); 22) Interruptor Protecciones Generación (IPG).

Notas destacadas:
- La CPM de medida directa debe ubicarse en el límite entre la propiedad y la vía pública y contener todos los elementos asociados al autoconsumo necesarios en el Punto de Medida (Protector contra Sobretensiones Transitorias, posible Filtro PLC e Interruptor de Maniobra Individual).
- La medida del Sistema Anti-Vertido (SAV) debe ubicarse en el Cuadro General de Mando y Protección (CGMP) del suministro.
- La instalación fotovoltaica puede disponer de su propio Cuadro de Mando y Protección de Generación (CMPG) y desde el mismo conectarse en un PIA del CGMP del suministro.

**Caso 2 (p. 21): INDIVIDUAL - CON COMPENSACIÓN O VENTA DE EXCEDENTES - RED INTERIOR - DEPENDIENTE - RENOVABLE**

Corresponde a una finca individual (nave o industria), con autoconsumo renovable (placas fotovoltaicas o cogeneración) de aproximadamente **50-100 kW** conectado en su instalación interior (en CGMP) como un circuito más con su interruptor automático, con excedentes (con compensación o venta de excedentes) y en modo de funcionamiento generalmente dependiente (sin posibilidad de funcionamiento en isla).

Elementos adicionales frente al Caso 1 (medida indirecta): Transformadores de Intensidad (7), Dispositivo de Verificación (8), Contador Medida Indirecta (9), Fusible Protección Equipo Comunicación (10), Equipo de Comunicación (Telemedida) (11), Interruptor-Seccionador de Seguridad (12).

Notas: la CPM de medida indirecta debe ubicarse en el límite entre la propiedad y la vía pública y contener los elementos asociados al autoconsumo (PST + IMI). La instalación fotovoltaica debe disponer de su propio CMPG y conectarse en un interruptor automático del CGMP de la finca. Si se quiere poder funcionar en modo "Separado" se debe incorporar un conmutador en el CGMP.

**Caso 3 (p. 22): COLECTIVO - SIN EXCEDENTES - RED INTERIOR - DEPENDIENTE - RENOVABLE**

Corresponde a una finca multisuministro (edificio de viviendas con poca superficie de tejado), con autoconsumo renovable (placas fotovoltaicas) de unos **25 kW** conectado en su red interior (en una posición de la centralización con su propia medida de la generación neta), sin excedentes (con sistema anti-vertido y que no precisa pedir permisos de acceso y conexión) y en modo de funcionamiento dependiente (sin posibilidad de funcionamiento en isla).

**Nota destacada**: "En los Autoconsumos COLECTIVOS SIN EXCEDENTES todos los suministros conectados aguas abajo del donde se instala el Sistema Anti-Vertido (SAV) deben asociarse al autoconsumo."

Notas adicionales: la centralización debe ubicarse en un cuarto/armario de contadores accesible del interior de la finca y contener los elementos asociados al autoconsumo necesarios en el Punto de Medida (Protector contra Sobretensiones Transitorias, posibles Filtros PLC e Interruptores de Maniobra Individuales). La instalación fotovoltaica debe disponer de su propio CMPG y desde el mismo conectarse en una posición de la centralización con su propio contador. La medida del SAV debe ubicarse en la columna del IGM previa al embarrado horizontal de la centralización.

**Caso 4 (p. 23): COLECTIVO - CON COMPENSACIÓN O VENTA DE EXCEDENTES - RED INTERIOR - DEPENDIENTE - RENOVABLE**

Corresponde a una finca multisuministro (edificio de viviendas con mucha superficie para placas), con autoconsumo renovable (placas fotovoltaicas) de unos **50-100 kW** conectado en su red interior (en una CMI para suministros de medida indirecta), con excedentes (con compensación o venta de excedentes) y en modo de funcionamiento dependiente (sin posibilidad de funcionamiento en isla).

Notas: la CMI debe ubicarse en un cuarto/armario de contadores accesible del interior de la finca y contener los elementos asociados al autoconsumo necesarios en el Punto de Medida (PST + IMI). La instalación fotovoltaica debe disponer de su propio CMPG y desde el mismo conectarse en la CMI con su propio contador. El IGM de la centralización solo precisa de protector contra sobretensiones y no de MAV. Debe existir una CDM o CGP con BTVCs que permita disponer de varias Líneas Generales.

**Caso 5 (p. 24): COLECTIVO - A TRAVÉS DE RED DE DISTRIBUCIÓN**

Corresponde a varias fincas de consumo asociadas al mismo autoconsumo (con cualquier tecnología de generación) de aproximadamente **80 kW** en el que el intercambio de energía entre la generación y los puntos de consumo se realiza a través de la red de distribución (con pago de peajes), con venta de excedentes (participación en el mercado).

**Nota destacada**: "En los Autoconsumos con proximidad A TRAVÉS DE RED cada suministro o instalación asociada al autoconsumo debe conectarse a la red de forma independiente; con la CPM, CMI o Centralización de Contadores que le corresponda. Los suministros de consumo existentes con el punto de medida que ya tenían, y la instalación de generación incorporando todos los elementos necesarios para una 'Generación Neta'."

Notas adicionales: las CPMs deben ubicarse en el límite entre la propiedad y la vía pública, mientras que las centralizaciones o CMIs deben ubicarse en un cuarto o armario de contadores accesible del interior de la finca, y en cualquier caso la instalación fotovoltaica debe disponer de su propio CMPG y desde el mismo conectarse en una CPM de medida indirecta.

### 4. Esquemas de conexión MT

#### 4.1 Selección del "Esquema de Conexión" en MT (p. 25)

Misma metodología en 4 pasos que en BT, adaptada a MT. Variables adicionales específicas de MT:

- **Tipo CT Gener.**: CT exterior (intemperie o a pie de apoyo); CT interior P ≤ 50 kVA (Medida BT); CT interior 1 Trafo (Medida MT); CT interior varios Trafos o dedicado.
- **Potencia Gen.**: Pg ≤ 50 kW (Directa BT en CPM); 50 < Pg ≤ 100 kW (Indirecta BT en CPM); 100 < Pg ≤ 400 kW (Indirecta BT en CPM); 50 < Pg ≤ 100 kW (Celda MT); 100 < Pg ≤ 4000 kW (Celda MT).
- **Potencia Con.**: Pc ≤ 50 kW (Directa BT en CPM); 50 < Pc ≤ 100 kW (Indirecta BT en CPM); 100 < Pc ≤ 400 kW (Indirecta BT en CPM); 50 < Pc ≤ 100 kW (Celda MT); 100 < Pc ≤ 4000 kW (Celda MT).
- **Tipo Conexión**: GENERAL (Dependiente y Equipotencial y Sincronismo-Disparo 52-G en BT); EXCEPCIONAL (Separado o no equipotencial o Sincronismo-Disparo 52-I en MT).

Un aviso "4º SI LE CORRESPONDE ALGUNA 'EXCEPCIONALIDAD' CONSULTAR CÓMO DEBE HACERSE (Figuras del Anexo 06)" remite a un anexo externo.

#### 4.2 Elementos asociados al autoconsumo en MT (p. 26)

**Nota destacada (izquierda)**: "La medida del 'Sistema Anti-Vertido' (SAV) siempre es preferible ubicarla físicamente en el punto situado inmediatamente aguas arriba del punto en el que se interconectan las instalaciones de generación y consumo y en serie con el contador de frontera, frente a la segunda opción contemplada en el nuevo Anexo I de la ITC-BT-40 que contempla medir todos los consumos y agregarlos para regular la generación."

Diagramas de ubicación del MAV en 4 escenarios: MAV en CGMP en autoconsumos sin excedentes en CTs particulares con medida en BT (CPM); MAV en Cuadro BT en autoconsumos sin excedentes en CTs particulares con medida en MT; MAV en celda de medida en CTs con varios trafos (Pg ≤ 100 kW en celda de medida MT; Pg > 100 kW en celda medida lado suministro).

**Nota destacada (derecha)**: "Los suministros MT se ven afectados por una serie de 'Excepcionalidades' que implican modificar el esquema general de conexión:
- Cuando el CT no tiene equipotencialidad con el CPMC, los relés de protección no se ubicarán en el CPMC sino en cada CT individual.
- Cuando el sincronismo y disparo no se vaya a realizar en BT, se realizará en el CPMC en MT actuando sobre el interruptor automático 52-I."

Se ilustra el caso "CT CONSUMO o SS.AA. 1000 < P ≤ 4000 kVA" con Celda Línea → Celda Protecciones MT (protección 50-51-67N) → Celda Interruptor Automático → Trafo 1031 a 4000 kVA → Cuadro BT, y variantes de CT Generación (celda fusible o interruptor automático 52-I, con disparo 52-G en BT).

#### 4.3 Requisitos técnicos para conexión de Autoconsumos en MT (p. 27) — TABLA CRÍTICA DE TARADOS Y RANGOS REGULABLES

De acuerdo a toda la legislación vigente, y especialmente según lo estipulado en el **RD 1699/2011**, en el **RAT-RLAT** y en la **ITC-BT-40**, los elementos y protecciones mínimas que ha de disponer un suministro en MT con sistemas de generación son:

**PROTECCIÓN, MEDIDA Y MANIOBRA EN CENTROS MT (CPMC o CTs):**
- Seccionamiento por ambos lados del Punto de Medida (lado "Red" y lado "Interior Suministro").
- Protector **59-N** (homopolar) en MT con actuación sobre el interruptor **52-G** en BT (salvo que exista MAV).
- Medida bidireccional (contadores "Telemedidos").
- En CT interior si Pot. generación > 100 kW, **protecciones generales** con actuación sobre 52-I en MT:
  - **50**: Sobreintensidad fases instantánea. Regulable de **0,3 a 10 In**.
  - **51**: Sobreintensidad fases temporizada. Regulable de **0,3 a 10 In**, temporización ajustable **0,1÷4 s**.
  - **67N**: Direccional tierra. Con temporización ajustable **0÷5 s**.
- En CT interior si Pot. generación > 100 kW, **protecciones generación** con actuación sobre 52-G en BT:
  - **27L**: Mínima tensión lado red. Regulable de **0,7 a 1,0 Un**, temporización ajustable **0÷2 s**.
  - **59**: Máxima tensión. Regulable de **0,9 a 1,3 Un**, temporización ajustable **0÷2 s**.
  - **81**: Máxima y Mínima frecuencia. Regulable de **51 a 48 Hz**, temporización ajustable **0÷5 s**.
- En CT interior si Pot. generación > 100 kW, **sincronismo y permiso cierre** con actuación sobre 52-I en MT:
  - **27B**: Mínima tensión lado interior. Regulable de **0,7 a 1,0 Un**, temporización ajustable **0÷2 s**.
  - **25**: Sincronismo tensiones ambos lados ajustado **60 s** para "permiso de Cierre".

**PROTECCIÓN EN INSTALACIÓN DE GENERACIÓN BT** (idénticas a las de BT, repetidas aquí para el contexto MT):
- Interruptor automático **52-G**, con relé enclavamiento, sobre el que actuarán Relés de protección MT y BT.
- **Relé Anti-Isla** que cumpla Norma **UNE EN 62116 V2** (con una actuación inferior a **1 segundo**).
- **Dispositivo Sincronizador (25)**: actuar con sincronismo durante mínimo **60 s**.
- **Relé Mínima Tensión (27)**: tarado al **-15%** (máx. **1,5 s**).
- **Relé Máxima Tensión (59)**: tarado al **+10%** (máx. **1,5 s**) y **+15%** (máx. **0,2 s**).
- **Relé de Frecuencia (81)**: tarado entre **48 Hz** (máx. **3 s**) y **50,5 Hz** (máx. **0,5 s**).

Nota lateral: "Listado de MAV e Inversores verificados en página web UFD" (con captura de pantalla de la web de UFD mostrando el buscador de "Autoconsumo" → "Información técnica sobre Autoconsumo").

Mismas dos preguntas retóricas que en BT (repetidas, referidas ahora al contexto MT):
1. "¿Quién CERTIFICA que los 'INVERSORES' cumplen con todos los requisitos de la norma UNE 217002, para garantizar que no pueden funcionar en 'Isla', que tienen separación galvánica, que no se inyecta continua en la red y que no se generan ni transmiten sobretensiones hacia la red?"
2. "Puesto que los Autoconsumos SIN Excedentes ya no tienen que pedir 'Acceso y Conexión' y la Distribuidora No revisa el proyecto ni verifica/precinta protecciones. ¿Quién CERTIFICA que el 'SISTEMA ANTIVERTIDO' cumple con los ensayos del nuevo Anexo I de la ITC-BT-40?"

#### 4.4 Esquemas de Conexión MT más frecuentes — 2 Casos (p. 28-29)

**Caso 1 MT (p. 28): INDIVIDUAL - CON EXCEDENTES - RED INTERIOR - RENOVABLE ≤ 100 kW**

Corresponde a una instalación industrial individual (nave o fábrica) con suministro en MT de pequeña/mediana potencia (1 Trafo ≤ 1000 kVA), con autoconsumo renovable (placas fotovoltaicas) de potencia **inferior a 100 kW** conectadas en BT en su instalación interior (en el Cuadro BT del CT), con excedentes (precisa pedir permisos de acceso y conexión) para aprovechar la generación en los momentos de inactividad (festivos, vacaciones, etc.) acelerando la amortización de la instalación, en modo de funcionamiento dependiente (sin posibilidad de funcionamiento en isla, pues TIEPI muy bajo) e instalación "Equipotencial" (placas en tejado de la nave donde también se ubica el conjunto CPMC+CT compartiendo misma tierra de protección).

Esquema: Celda Protección Fusible + Celda Medida MT (Wh + relé homopolar RAF + 59N) → Trafo ≤ 1000 kVA → Cuadro BT → circuitos interiores consumo, con conexión de generación (52-G) con protecciones e inversor.

**Nota destacada**: "El CPMC y el CT normalmente conforman un único 'local' (cercano al 'Centro de Seccionamiento' de la distribuidora) que es totalmente 'equipotencial' con toda la instalación interior del suministro incluida la instalación de generación (todo está conectado a la misma tierra de protección)."

Notas adicionales: la instalación fotovoltaica debe disponer de su propio CMPG y desde el mismo se conectará directamente en el Cuadro BT del CT como cualquier otro circuito interno del suministro (o en cualquier sub-cuadro de la instalación interior en BT del suministro). Las protecciones en BT que actúan sobre el interruptor 52-G son exactamente las mismas que las requeridas para un autoconsumo en un suministro BT. La única protección extra que hay que instalar respecto a un suministro de consumo corresponde a la protección **59N** de máxima tensión homopolar (que podrá aprovechar uno de los devanados de los Trafos de Tensión del sistema de medida) y que actuará sobre el interruptor 52-G en BT.

**Caso 2 MT (p. 29): INDIVIDUAL - CON EXCEDENTES - RED INTERIOR - RENOVABLE o COGENERACIÓN > 100 kW**

Corresponde a una gran instalación industrial individual (1 Trafo ≤ 4000 kVA), con autoconsumo renovable o cogeneración de potencia **superior a 100 kW** conectadas en BT en su instalación interior (generalmente en el Cuadro BT del CT), con excedentes (precisa pedir permisos de acceso y conexión) para poder aprovechar toda la capacidad de generación acelerando la amortización de la instalación, en modo de funcionamiento dependiente (también se podría funcionar en modo "Separado" aprovechando el interruptor 52-I) e instalación "Equipotencial" (la generación comparte la misma tierra de protección que el conjunto CPMC+CT) con sincronización en BT.

Esquema: Celda Línea → Celda Protección y Medida MT (3 TI, homopolar, Wh, RAF, protección 50-51-67N) → Celda Interruptor Automático 52-I (permiso cierre, protección 27L-59-81-59N) → Celda Medida Tensión Lado Suministro (RAF, protección 27B, permiso cierre) → Trafo ≤ 4000 kVA → Cuadro BT → circuitos interiores consumo + conexión generación con SS.AA., protecciones, inversor (52-G).

Tres recuadros rojos destacados:
- "El interruptor 52-I del CPMC puede utilizarse para posibilitar el funcionamiento en modo separado."
- "Si no existiera equipotencialidad entre la ubicación del CPMC (que siempre estará cercano al 'Centro de Seccionamiento' de la distribuidora) y la generación, habría que desplazar el CT cerca de la instalación de generación, o diseñar una instalación con varios CTs, hasta que exista equipotencialidad con la generación."
- "Si se desea sincronizar en MT sobre el interruptor 52-I, debe instalarse un relé 25 junto a la protección 27B."

Notas adicionales: la instalación fotovoltaica debe disponer de su propio CMPG y desde el mismo se conectará directamente en el Cuadro BT del CT (o en cualquier sub-cuadro de la instalación interior en BT del suministro). Las protecciones en BT que actúan sobre el interruptor 52-G son exactamente las mismas que las requeridas para un autoconsumo en un suministro BT. Al ser la potencia de generación > 100 kW debe instalarse una celda con interruptor automático sobre la que actuarán las protecciones **50, 51 y 67N** obteniendo los permisos de cierre de los relés **27L y 27B**. Por otro lado deben instalarse las protecciones: **27L, 59, 81 y 59N** (que podrán aprovechar los devanados de los Trafos de Tensión del sistema de medida) y que actuarán sobre el interruptor 52-G en BT.

#### 4.5 Cierre (p. 30)

Diapositiva final: "MUCHAS GRACIAS POR SU ATENCIÓN".

## Datos clave (con página de origen)

- Las 5 variables que definen cualquier tipología de Autoconsumo: Clasificación, Modalidad, Proximidad, Modo de Funcionamiento, Tecnología (p. 3).
- CNMC: 30 códigos Administrativos de Autoconsumo → 56 tipologías BT, 38 tipologías MT, 22 combinadas MT/BT (p. 4).
- Condiciones de Proximidad: <500 m (BT/AT general) o <2.000 m (FV en cubierta/suelo industrial a través de red), o misma referencia catastral (14 dígitos) (p. 8).
- Resolución CNMC 20/05/2021: capacidad de acceso ≤100 kW en un punto BT, Σ≤175 kW en una Salida BT, Σ≤400 kW en el conjunto del CT (p. 3).
- RDL 29/2021: proximidad ampliada a 2.000 m independientemente del nivel de tensión (p. 3).
- 4 Configuraciones de Medida: A (solo frontera), B (generación neta en Serie), C (generación neta en Paralelo), D (opcional: consumo total + generación bruta + SS.AA. en Paralelo) (p. 9, 13).
- 56 tipologías BT → 151 esquemas de conexión; 38 tipologías MT → 316 esquemas de conexión; 22 tipologías combinadas MT/BT → esquemas no cuantificados en la fuente (p. 5, 6, 7).
- **Relé Anti-Isla**: Norma UNE-EN 62116 V2, actuación < 1 s (p. 19, 27).
- **Dispositivo Sincronizador (25)**: sincronismo mínimo 60 s (p. 19, 27).
- **Relé Mínima Tensión (27)**: tarado -15%, máx. 1,5 s (p. 19, 27).
- **Relé Máxima Tensión (59)**: tarado +10% máx. 1,5 s y +15% máx. 0,2 s (p. 19, 27).
- **Relé de Frecuencia (81)**: tarado 48 Hz máx. 3 s y 50,5 Hz máx. 0,5 s (p. 19, 27).
- Protecciones generales MT (Pg > 100 kW) sobre 52-I: 50 (sobreintensidad instantánea, 0,3-10 In), 51 (sobreintensidad temporizada, 0,3-10 In, 0,1-4 s), 67N (direccional tierra, 0-5 s) (p. 27).
- Protecciones generación MT (Pg > 100 kW) sobre 52-G: 27L (mínima tensión lado red, 0,7-1,0 Un, 0-2 s), 59 (máxima tensión, 0,9-1,3 Un, 0-2 s), 81 (máx./mín. frecuencia, 51-48 Hz, 0-5 s) (p. 27).
- Sincronismo y permiso cierre MT: 27B (mínima tensión lado interior, 0,7-1,0 Un, 0-2 s), 25 (sincronismo, 60 s permiso de cierre) (p. 27).
- Protección 59N (homopolar) en MT, actúa sobre 52-G en BT salvo existencia de MAV (p. 27).
- Casos de referencia de potencia de los 5 esquemas BT: 3-9 kW (chalet individual), 50-100 kW (nave/industria individual), 25 kW (colectivo edificio poca superficie), 50-100 kW (colectivo edificio mucha superficie), ~80 kW (colectivo a través de red) (p. 20-24).
- Casos de referencia MT: individual renovable ≤100 kW con 1 trafo ≤1000 kVA; individual renovable/cogeneración >100 kW con 1 trafo ≤4000 kVA (p. 28-29).
- Actualización normativa anunciada: ITC-BT-12, 23, 40, 53 e ITC-RAT-09, prevista para el 1er trimestre de 2026, para unificar Relé Anti-Isla, SAV, Protector Sobretensiones, Filtro PLC, Interruptor de Corte en Carga (p. 3).
- Umbral de intensidad que exige fusibles previos en el PST Tipo 1: >125 A (p. 18).
- Filtro PLC: solo existe actualmente para medida directa (P ≤ 50 kW); en medida indirecta debe incorporarse en el inversor (p. 19).

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: fundamentalmente la fase 6 de la metodología ERMA (definición constructiva/diseño eléctrico de la instalación), y de forma transversal el capítulo de marco normativo y el de tramitación administrativa (permisos de acceso y conexión según modalidad con/sin excedentes).
- **Qué aporta exactamente**: proporciona los esquemas eléctricos completos de conexión BT y MT con todos los elementos exigidos (CPM/CPMC, CGMP, CMPG, SAV, IMI, PST, filtro PLC) y, sobre todo, los **tarados numéricos exactos y trazables** de cada relé de protección obligatorio (Anti-Isla, mínima/máxima tensión, frecuencia, sincronismo, y en MT las funciones ANSI 50/51/67N/27L/59/81/27B/25) que deberán citarse en la definición constructiva del sistema de protecciones de la instalación FV del CPD. También aclara la elección de Configuración de Medida (A/B/C/D) aplicable según la modalidad de autoconsumo elegida para el CPD (previsiblemente individual con excedentes, dado el marco regulatorio 2026 ya registrado en memoria — ver [[project_marco_regulatorio_2026]] y [[project_tipologia_autoconsumo_variantes]]) y el Caso 2 BT (o el Caso 2 MT si la potencia de generación asociada al CPD supera 100 kW, lo cual es previsible dada la escala del proyecto) son los esquemas de referencia más directamente aplicables al dimensionado del punto de conexión.
- **Confianza en los datos**: todos los tarados y rangos regulables provienen literalmente de las diapositivas 19 y 27 de la fuente (RD 1699/2011, ITC-BT-40, RAT-RLAT), citados sin interpretación. Las cifras de tipologías/esquemas (56/151, 38/316, 22/?) están explícitamente en las notas destacadas de las diapositivas 5, 6 y 7. No se ha completado ningún dato con conocimiento general del modelo; donde la fuente no facilita una cifra (p. ej. nº de esquemas combinados MT/BT) se indica explícitamente como "no especificado en la fuente" (marcado como "¿?" en el propio original).

## Notas de procesamiento

Documento leído íntegro (30 pp., incluyendo portada, índice y diapositiva de cierre). Todas las tablas de configuraciones de medida (A/B/C/D) y todos los tarados numéricos de relés de protección (BT y MT) se han preservado con sus unidades, rangos y tiempos de actuación exactos, tal como exigía el encargo. No se ha reproducido en detalle el contenido íntegro de las dos tablas extensas de "Tipología de Autoconsumo BT/MT según CNMC" (diapositiva 4, ~90 filas con códigos administrativos individuales) ni las decenas de diagramas de variantes de Configuración B y C en MT (diapositivas 15-16, con docenas de sub-esquemas gráficos por combinación de CT/potencia/trafos): son ilustraciones repetitivas de la misma lógica ya documentada textualmente (configuración A/B/C/D + condiciones de aplicación), y su valor para el TFM es nulo salvo que Mario necesite un código CNMC administrativo concreto, en cuyo caso debe consultarse el PDF original en esas páginas. No se detectaron ecuaciones matemáticas explícitas en el documento (es una presentación de esquemas normativos y eléctricos, no de cálculo); los "rangos regulables" de los relés de protección MT (p. ej. 50: 0,3 a 10 In) se han preservado como tales, no como fórmulas. No hubo errores de extracción; todas las páginas se visualizaron correctamente como imágenes de alta resolución.
