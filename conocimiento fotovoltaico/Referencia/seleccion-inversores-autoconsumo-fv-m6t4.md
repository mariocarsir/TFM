---
title: "Selección de inversores para autoconsumo FV"
tipo: presentacion
autor: "Jean-François Picard (AMARA NZero)"
anio: 2025
densidad: exhaustivo
fecha_resumen: 2026-08-30
fuente_original: "Documentacion de apoyo/Presentaciones Master/M6 Autoconsumo/Presentaciones/M6_T4_SeleccionInversores.pdf"
tags: [fotovoltaica, autoconsumo, inversores, almacenamiento, dc-coupling, ac-coupling, mppt, erma-m6]
related: [introduccion-autoconsumo-fotovoltaico-m6t2, dimensionamiento-baterias-autoconsumo, diseno-espacial-fv-edificios-m6t1, m6-t8-estructuras-soporte-fv]
---

# Selección de inversores para autoconsumo FV (Jean-François Picard, AMARA NZero, 2025)

## Resumen

Presentación del Módulo 6 (Autoconsumo Fotovoltaico) del Máster ERMA, 20ª edición 2025-2026, impartida por Jean-François Picard (AMARA NZero) sobre selección de inversores fotovoltaicos de conexión a red. Cubre las funciones principales del inversor (conversión CC/CA, seguimiento MPP, sincronización y protección de red, apoyo a la estabilidad de red, limitación de inyección, monitorización), los cinco tipos de inversores según topología (string/multi-string, MLPE con micro-inversores y optimizadores, híbridos/acumulación, centrales, y solución integrada de media tensión), las dos arquitecturas de acoplamiento de baterías (DC-coupling vs AC-coupling, con sus subtipos de inversor híbrido, convertidor CC/CC e inversor cargador), los criterios técnicos de selección (potencia CA, compatibilidad de red, eficiencia europea, rango de tensión CC, número de MPPT, corriente Isc/Impp), aspectos de seguridad (arco eléctrico, conectores MC4, AFCI, RSD) y consideraciones prácticas de configuración (módulos en serie/paralelo, ratio DC/AC, herramientas de dimensionado del fabricante). Es la fuente directa para la decisión pendiente del TFM entre DC-coupling y AC-coupling en la arquitectura de baterías del capítulo 7.

## Contenido técnico

### 1. Presentación de AMARA NZero (contexto, no técnico para el TFM)

Partner estratégico de la transición energética. Presencia en 15 países (España, Portugal, Italia, Francia, Bulgaria, Rumanía, Grecia, EEUU, México, Brasil, Colombia, Panamá, R. Dominicana, Marruecos, China). Cifras 2023-2024: 715 M€ facturación 2023, 1.028 M€ previsión 2024, 1.817 empleados, 65 años de experiencia, 500.000 m² de almacenes, +12 almacenes propios en Iberia (+200.000 m²) y 8 almacenes In House. Áreas: solar, eólica (repuestos y mantenimiento), hidráulica. Servicios: asesoramiento técnico, cálculo de acumulación, cálculos estructurales, servicio postventa, formaciones, ecosistema digital (tienda online, área de gestión privada), Amara NZero Finance.

### 2. Inversores de conexión a red — funciones principales (diapositivas 9-18)

**Funciones principales del inversor:**
1. Convertir la corriente continua (CC) de los módulos FV en corriente alterna (CA) para inyección a la red.
2. Ajustar el punto de funcionamiento del campo solar (regulación MPP).
3. Sincronización con la red eléctrica (V, Hz).
4. Proteger y avisar de fallos eléctricos (Rcd, PE).
5. Ayudar a la estabilidad de la red (tensión, FRT — Fault Ride Through).
6. Comunicación de datos y monitorización.
7. Retos de futuro: smart grid, gestión de cargas y almacenamiento.

**Esquema de concepto (diapositiva 11):** puente rectificador con conmutadores S1-S6, diodos D1-D2, condensadores C1-C4, inductancias L1-L4, que convierte la onda continua (V+ constante en el tiempo) en la onda sinusoidal de salida.

**Búsqueda del punto de máxima potencia (PMP o MPP):**
- Ecuación fundamental: Potencia (W) = Tensión (V) × Corriente (I).
- Ejemplo de curva I-V de módulo FV: Voc = 35V, VMpp = 30V, con conexión a carga de tensión fija (batería 12V) se pierde potencial de generación frente a trabajar en el PMP.
- Diferencia entre regulador/cargador de batería (convertidor CC/CC, ajusta a Vpmp, Ipmp fijos de la batería, p.ej. 12V) e inversor de conexión a red (convertidor CC/CA, trabaja en Vcc, Icc del PMP real, salida trifásica 230V R,S,T).
- Utilidad de varios MPPT: varias orientaciones, varias inclinaciones, evitar sombras de obstáculos, mayor flexibilidad de configuración. Ejemplo gráfico de tejado con MPPT1, MPPT2, MPPT3 en distintas orientaciones/inclinaciones (acimut e inclinación configurables independientemente por entrada).

**Seguridad de la red:**
- Vigilancia: tensiones (min./máx.) en España: 195V/253V; frecuencia (min./máx.): 48Hz/51Hz; impedancia de red; funcionamiento en isla.
- Desconexión: por valores fuera de límites, por desconexión de red, por servicio/mantenimiento o fallo.
- Métodos de protección: ENS (Einrichtung zur Netzüberwachung mit Zuordnung der Schalteinrichtung), desplazamiento de fase, control vectorial.
- Principales normas citadas: **UNE-EN 62116:2014 V2**, **UNE 217001:2020**, **UNE 217002:2020**, **RD 1699/2011**, Norma Técnica de Supervisión (NTS) (UE) 2016/631, Huecos de tensión P.O. 12.3.

**Apoyo a la estabilidad de la red frente a huecos de tensión** (válido para plantas/agrupaciones FV >2MW): caída brusca de tensión por causas externas (cortocircuitos, picos de consumo). Gráfica tensión (pu) vs tiempo (s): caída desde 1pu hasta ~0,2pu, permanencia en zona gris (duración de la falta), recuperación hasta 0,95pu tras el despeje de la falta. El inversor debe permanecer conectado dentro del área gris; existen requisitos de generación de energía reactiva para ayudar a la recuperación del hueco.

**Apoyo a la estabilidad de red por frecuencia:**
- Norma alemana: disminuir potencia un 40% por Hz entre 50,2 y 51,5 Hz; desconectar por encima de 51,5Hz.
- Norma italiana: disminuir un 83,3% por Hz entre 50,3 y 51,5 Hz; desconectar por encima de 51,5Hz. (Figura 40 del original: "Curva di riduzione della potenza attiva in sovra frequenza").

**Inyección cero / limitación de inyección a red** (cumplimiento **UNE 217001:2020**, mismos requisitos que RD 244/2019 Anexo 1):
- Potencia consumo > Potencia FV disponible → el inversor trabaja en el PMP.
- Potencia consumo < Potencia FV disponible → el inversor cambia de punto de trabajo al Punto de Potencia Requerida (PPR), moviéndose por la curva I-V hacia tensiones mayores.
- Potencia consumo = 0W → el inversor lleva la tensión de trabajo a Voc (circuito abierto), la corriente pasa a 0A (PPR=0).
- Mecanismo: al cambiar la tensión de trabajo del campo FV cambia la corriente resultante, permitiendo ajustar la potencia entregada hasta parar la producción si no hay consumo.

**Monitorización** (creciente importancia, cada vez más valor añadido): datalogger (V, I, W, etc.), puertos de comunicación, canal de sensores ambientales, aviso de alarma, API, integración en SCADA, mantenimiento preventivo, acceso remoto a inversores.

### 3. Tipos de inversores de conexión a red (diapositivas 19-40)

**Clasificación general por topología eléctrica:**
- De cadena (string): campo de módulos FV único → inversor FV.
- MLPE (Module Level Power Electronic): único módulo FV (a veces 2) → optimizador CC/CC → inversor FV, o → micro-inversor CC/CA directo.
- Híbrido (FV/Acumulación): campo de módulos FV + batería → inversor híbrido (con backup incluido u opcional).
- Solo de acumulación: batería → inversor de batería (backup externo o incluido).
- Batería AC: batería → inversor de batería con backup incluido, en el lado de red.
- Todos conectan finalmente a red eléctrica a través de contador de energía bidireccional.

**Rangos de potencia por tecnología (diapositiva 21):**
| Tipo | Rango de potencia |
|---|---|
| Inversores multi-string | ±1,5 – 330 kWn (evolucionó a ±1,5–110 kWn en la diapositiva siguiente) |
| MLPE, Microinversores & Optimizadores | ±1000 Wn |
| Inversores híbridos (o de acumulación) | ±1,5 – 10 kWn |
| Inversores de gran potencia (Centrales) | >50 kWn hasta varios MW |

**Clasificación detallada por tecnología (diapositiva 23):**
1. **Inversor string y multi-string** (desde ~1kW hasta >330kW): la gran mayoría de los inversores del mercado.
2. **Inversores híbridos y de acumulación**: híbrido controla tanto el generador FV como carga/descarga de batería; de acumulación controla únicamente la carga/descarga de la batería (necesita inversor(es) FV adicional(es)).
3. **MLPE** (Module Level Power Electronic — electrónica de potencia a nivel de módulo): micro-inversores desde 250W hasta ~1600W (salida AC a nivel de módulo); optimizadores de módulos desde 250W hasta ~1500W (circuito CC de optimizadores hasta el inversor).
4. **Inversores "centrales"**: 1 solo MPPT.
5. **Inversores de solución integrada** (Utility Scale/Mega Station, >500kW hasta varios MW): inversores + cabina + parametría de media tensión + transformador de media tensión.

#### 3.1 Inversores string/multi-string

- **Inversor string**: una cadena de módulos por inversor, único PMP.
- **Inversor multi-string**: varias cadenas de módulos independientes por inversor (múltiple PMP), rango típico 1kW...50kW (hasta 200kW), reducción de cableado y bus de CC, óptimo para diferentes orientaciones/inclinaciones o pocas sombras parciales localizadas.
- **Pros**: más económico que MLPE, conversión más eficiente, menos probabilidad de fallo (menos equipos).
- **Contra**: pérdidas por sombreado/deterioro/suciedad, más limitación de configuración, necesidad de validar configuración por string, monitorización solo a nivel de string.
- **Ejemplos de marcas**: SMA, Fronius, Solis, Huawei.
- **Configuración considera principalmente**: potencia nominal AC, rango de tensión de trabajo (Vmppt min y V start; Vmppt max y Voc), número de entradas CC, número de MPPTs, corriente de entrada (Impp nominal e Isc máxima).
- Tabla de ejemplo de "posibilidades de diseño" de un software de dimensionado con combinaciones de strings PV1/PV2, potencia (kWp) y ratios RP (81%-117%) y CA/CCP.

#### 3.2 MLPE — Micro-inversores

- Cada módulo (o grupo) funciona en su PMP; rango típico 200W-600W aprox.; suelen ser monofásicos (instalación puede ser trifásica); se conectan en paralelo entre ellos en AC (no en serie como los optimizadores).
- **Pros**: montaje en estructura debajo de módulos, mayor producción (PMP a nivel módulo, -€/kWh), mayor flexibilidad de configuración, simplicidad de configuración y montaje, más seguros (tensión CC <80V), monitorización a nivel de módulo, mantenimiento más sencillo, rápida localización de fallos, simplicidad de logística, no existe único punto de fallo, ya existen módulos con micro-inversores incorporados.
- **Contra**: mayor coste/kW, menor eficiencia por inversor, más equipos de potencia (más probabilidad de fallo).
- **Marca destacada**: Enphase (con software de compatibilidad online).
- **Configuración considera**: tensión min/max de trabajo y circuito abierto, potencia del módulo vs inversor, número de inversores por ramal AC (la corriente de salida se suma).
- Ejemplo de calculadora Enphase (https://enphase.com/es-es/installers/microinverters/calculator): tabla de especificaciones IQ7/IQ7+/IQ7X con compatibilidad de celda (60/72/96), potencia recomendada, máxima potencia de salida (240VA/1,04A, 290VA/1,26A, 315VA/1,37A a 230V) y número total de inversores por circuito de 16A (12, 10, 9 respectivamente).

#### 3.3 MLPE — Optimizadores

- Optimización total (cada módulo con optimizador en su PMP óptimo) vs optimización parcial (grupos de módulos sin optimizar intercalados). Rango típico 200W-1600W. El optimizador es un convertidor CC/CC (necesita inversor CC/CA adicional). Se conectan en serie entre ellos, en CC (a diferencia de los micro-inversores en paralelo AC). Ya existen Smart Modules con optimizadores incorporados.
- **Pros optimización total**: mayor producción, mayor flexibilidad/simplicidad de configuración (sombras, orientación, strings largos), monitorización a nivel de módulo, más seguridad, rápida localización de fallos, cadenas largas.
- **Pros optimización parcial**: similares con menor coste relativo.
- **Contra**: mayor coste/kW, único punto de fallo posible, más equipos de potencia.
- **Marcas**: Tigo, Huawei, SolarEdge.
- Tabla técnica SolarEdge (parámetros P300/P370/P401/P404/P405/P485/P500/P505): tipo de módulo compatible (60/72/96 células, capa fina, tensión alta, bifacial), potencia máxima de entrada @STC (340W-505W), valor máximo absoluto de tensión de entrada (Voc a temp+baja): 48V-125V, rango de operación MPPT (8-125V según modelo), corriente máxima de entrada Isc (10,1A-14A). Mínimo/máximo de optimizadores por string: 6-8 mínimo, 25 máximo, potencia máxima por string ejemplo 5,7kW (HD Wave).

#### 3.4 Inversores centrales

- Un único PMP por inversor (en general), necesaria agrupación de strings, rango de potencias ≥50kW (típicos 100kW o más), generalmente >100kW.
- **Pros**: alta eficiencia de conversión, menor coste/kW, menos probabilidad de fallo, posibilidad de string de 1500Vcc según modelo, salida a tensiones AC normalizadas para trafo MT.
- **Contra**: posibles pérdidas por sombreado, poca flexibilidad de configuración, más complejo de configurar (cajas de agrupación, string paralelo), posibles pérdidas considerables en cableado CC, único punto de fallo posible, logística de transporte y montaje.
- **Ejemplos**: SMA Highpower Peak3 (150kW, 1 MPPT), Huawei SUN2000 330-KTL-H1 (330kW, 6 MPPT).
- **Configuración considera**: potencia nominal AC, tensión mínima de trabajo CC, tensión máxima de trabajo y circuito abierto, número de entradas CC, número de MPPT (suele ser 1 o pocos), corriente nominal/máxima por entrada, número de entradas en cajas de agrupación de strings, corriente máxima de las cajas de agrupación.
- Ejemplo de software de configuración: generador FV1 340/514 (A:17x20), verificación de compatibilidad FV/inversor con potencia CC máx (102,00kW inversor vs 119,00kWp entrada), tensión CC min/máx, corriente entrada máx (180A vs 177,7A), corriente cortocircuito máx (325A vs 189,6A); indicadores de rendimiento: ratio de potencia nominal 86%, eficiencia del inversor 99,3%.

#### 3.5 Solución integrada de media tensión (Utility Scale)

- Gran potencia (típicos varios MW, generalmente >2MW), cabina para intemperie, transformador elevador y elementos de protección en MT.
- **Pros**: alta eficiencia de conversión, menor coste €/kW, menos probabilidad de fallo.
- **Contra**: único PMP por inversor (o pocos), posibles pérdidas por sombreado, poca flexibilidad de configuración, posibles pérdidas en cableado CC, único punto de fallo, logística de transporte e instalación.
- Ejemplo: SMA MV Power Station 4400/4950/5000/5500/6000.
- **Configuración considera**: potencia nominal AC, tensión mínima/máxima de trabajo CC y circuito abierto, número de entradas CC, número de MPPT (1 o 2), corriente nominal/máxima por entrada, número de entradas y corriente máxima de las cajas de agrupación de strings, número máximo de cajas de agrupación.

### 4. Soluciones para el almacenamiento — DC-coupling vs AC-coupling (diapositivas 41-56, sección clave para el TFM)

**Concepto base:**
- **Acoplamiento en corriente continua CC (DC coupling)**: los módulos FV se conectan directamente al inversor (que integra carga/descarga de batería en el lado CC), con un único paso de conversión CC/CA hacia la red y las cargas.
- **Acoplamiento en corriente alterna CA (AC coupling)**: el generador FV pasa por su propio inversor CC/CA hacia el bus AC; la batería se conecta a través de un inversor-cargador independiente (CA↔CC) al mismo bus AC.
- Gráfica de perfil diario (Solar Production vs Energy Usage, barras naranjas/azules) ilustrando el reparto de excedente solar hacia carga de batería y descarga posterior en horas sin sol.

**4.1 Inversores híbridos, DC coupling (un solo inversor FV+batería):**
- Carga de batería desde CC incluida en el inversor. Suelen ser inversores string, monofásicos o trifásicos. Rango típico 1-10kW aprox (ya se ven modelos de 50, 100, 150kW).
- **Pros**: un solo inversor para módulos y acumulación, mayor eficiencia (menos etapas de conversión CC/AC), más económico (menos equipos), menos posibilidad de fallo, simplicidad de configuración y montaje, monitorización en un solo portal, servicio técnico simplificado (un solo proveedor), preparado para baterías futuras aunque no se usen desde el inicio.
- **Contra**: menos flexibilidad de elección de capacidad de baterías, existe un único punto de fallo.
- **Marcas y modelos**: Kostal Plenticore Plus (3p, 4-10kW), SMA Smart Energy (3ph, 5-10kW), Fronius Primo GEN24 (1p, 3-6kW) / Symo GEN24 (3p, 3/4/5kW), Huawei SUN2000 L1 (1p, 2-5kW) / SUN2000 M1 (3p, 3-10kW). Baterías compatibles: BYD, Fronius, Huawei.
- **Criterios de selección**: potencia nominal AC de salida, tensión mínima/máxima de trabajo CC (FV), número de entradas CC, número de MPPT (1 o 2), corriente nominal/máxima por entrada, número de entradas para batería, corriente nominal/máxima por entrada de batería, **compatibilidad con tipos de batería (litio HV, litio LV, Plomo)**, posibilidad y limitaciones de ampliabilidad y escalabilidad.

**4.2 Convertidor CC/CC, DC coupling (retrofit de acumulación sobre instalación FV existente):**
- Carga desde CC; interesante para añadir almacenamiento a instalaciones ya existentes sin cambiar el inversor FV.
- **Pros**: cierta mejora de eficiencia (menos etapas CC/AC), permite mantener instalaciones existentes, flexibilidad de elección de baterías, puede permitir diferentes marcas de inversores.
- **Contra**: complejidad de monitorización si hay varias marcas, más riesgo de fallo (varios equipos), varias marcas complica el servicio técnico.
- **Criterios de selección**: potencia nominal CC (carga/descarga), tensión mínima/máxima de trabajo CC (conectada al campo FV), número de entradas CC (FV), número de MPPT, corriente nominal/máxima por entrada, número de entradas para batería, corriente nominal/máxima por entrada, compatibilidad de baterías (litio HV, LV, Plomo), ampliabilidad/escalabilidad.

**4.3 Inversores cargadores, AC coupling (batería independiente del inversor FV):**
- Carga desde AC; suelen ser inversores exclusivos para baterías (sin entrada de FV); modelos monofásicos y trifásicos; para baterías de litio HV, LV o incluso ácido-plomo; rango de potencias muy variado y muy flexible.
- **Pros**: más versatilidad de configuración y escalable, más capacidad de acumulación, más potencia AC desde baterías, más flexibilidad de selección de baterías (independiente del inversor FV), ideal para retrofit en instalaciones existentes.
- **Contra**: menos eficiencia (varias etapas de conversión), menos económico (más equipos que en DC coupling), más posibilidad de fallo, puede requerir varios portales de monitorización, varias marcas complica el servicio técnico.
- **Marcas y modelos**: SMA (Sunny Boy Storage 1p 2,5-6kW; Sunny Tripower Storage 60kW; Sunny Island), Kostal Plenticore Battery Inverter (3p, 5 y 10kW), Tesla Powerwall 2 (batería AC 14kWh, incluye inversor AC — nota: la Powerwall 3 es un All-in-One con inversor híbrido incluido), Enphase IQ Battery 10T/3T (batería AC 10 y 3kWh, incluye inversor AC).
- **Criterios de selección**: potencia máxima AC (necesaria en carga y descarga de baterías), tensión de trabajo CC (batería con inversor, LV o HV), número de entradas CC para baterías, corriente nominal/máxima por entrada CC, posibilidad de conectar varias baterías.

### 5. Principales características de selección de los inversores (diapositivas 58-70)

**Aspectos generales — prioridades a definir antes de elegir:** mayor producción energética, máxima seguridad, monitorización al detalle, menor precio, control remoto, mantenimiento predictivo, garantía y robustez, logística, servicio postventa local.

**Datos técnicos — Características en corriente alterna (CA):**
- Potencia nominal del inversor.
- Compatibilidad con la red eléctrica: tensión (Vca) y frecuencia (Hz), inyección trifásica/monofásica, régimen de neutro (TT, IT, TN).
- Legislación, seguridad y elementos de protección.
- Eficiencia del inversor (máxima, europea, y a la tensión nominal).

**Características en corriente continua (CC):**
- Número de MPPT.
- Número de entradas CC (total y por MPPT).
- Corriente máxima por cada entrada (o MPPT).
- Tensión nominal del inversor, tensión mínima y máxima (Voc y Vpmp).
- Máxima potencia CC admisible (ratio DC/AC).
- Eficiencia del sistema según la configuración.

**Otras características (no menos importantes):** monitorización (datos disponibles, retención temporal, acceso remoto), servicio técnico, garantía.

**Potencia AC — marco normativo español:**
- En autoconsumo, la potencia de la instalación = suma de la potencia nominal de los inversores fotovoltaicos, según **RD 1699/2011** (potencia hasta 100kW).
- La legislación española define la potencia de una instalación FV según la potencia nominal de los inversores al 100% de carga en funcionamiento continuo (no la potencia pico/máxima en periodo corto).
- Nota: ciertos países europeos exigen Potencia Nominal = Potencia Máxima, cada vez más común en el mercado.
- La potencia del generador FV (módulos) se llama "potencia pico" o "kWp"; para instalaciones >100kW rige el **RD 1955/2000**.

**Compatibilidad con la red eléctrica (RD 1699/2011):**
- Voltaje estándar Europa: circuito monofásico 230V AC fase-neutro; circuito trifásico 230V AC fase-neutro y 400V AC entre fases; frecuencia 50Hz.
- Tabla de protecciones de desconexión (comparativa RD 661/2007 vs RD 1699/2011, España):

| Parámetro | Umbral de protección | Tiempo máx. actuación |
|---|---|---|
| Sobretensión fase 1 | Un+10% | 1,5s |
| Sobretensión fase 2 | Un+15% | 0,2s |
| Tensión mínima | Un-15% | 1,5s |
| Frecuencia máxima | 50,5Hz | 0,5s |
| Frecuencia mínima | 48Hz | 3s |

| Norma | U_ACmax | t_UACmax | U_ACmin | t_UACmin | f_max | t_fmax | f_min | t_fmin |
|---|---|---|---|---|---|---|---|---|
| RD 661/2007 | 253V (nivel1)/264,5V (nivel2) | 1,5s (nivel1)/0,2s (nivel2) | 195,5V | 1,5s | 51Hz | 0,5s | 48Hz | 3s |
| RD 1699/2011 | 253V (nivel1)/264,5V (nivel2) | 1,5s (nivel1)/0,2s (nivel2) | 195,5V | 1,5s | 50,5Hz | 0,5s | 48Hz | 3s |

**Eficiencia y rendimiento:**
- Eficiencia máxima del inversor (η máx.) según tensión de trabajo = eficiencia a tensión nominal (Unom). Gráfica: curvas de η[%] vs Pac/PacEur para tres tensiones CC (Ucc,r=680V, alcanza 98% ηmax; UPMPmax=800V; UMPPmin=440V con 2 seguidores simétricos, ~91% al 0% de carga subiendo a ~97-98%).
- **Eficiencia europea (η Eur.)**: fórmula ponderada según potencia de salida instantánea (diapositiva 60):

η_euro = 0,03·η_5%Pn + 0,06·η_10%Pn + 0,13·η_20%Pn + 0,10·η_30%Pn + 0,48·η_50%Pn + 0,20·η_Pn

  donde η50 = eficiencia del inversor al 50% de su potencia nominal, P50 = 50% de la potencia nominal. Gráfica de ejemplo: η5=84,9%, η10=90,8%, η20=93,8%, η30=94,8%, η50=95,4%, η100=95,0%, con barras de "peso" en el eje secundario (3%, 6%, 13%, 10%, 48%, 20%).
- Nota: también debería considerarse la eficiencia total de la instalación según configuración (pérdidas por sección/longitud de cableado, especialmente en CC, y pérdidas por más cadenas de módulos para una misma potencia CC).

**Número de seguidores MPP (diapositivas 65-70) — ejemplos visuales de tejados complejos** (residencial con múltiples orientaciones, nave industrial extensa, tejado a dos aguas, complejo industrial con varias naves) ilustrando la pregunta "¿cuántos MPPT mínimo necesito (e inversores)?".

**Comparativa esquemática de configuraciones MPPT:**
- Inversor con único seguidor PMP: usado en inversor central (varios strings en paralelo) o inversor de un solo string. Ejemplo: 3 grupos de 10 módulos en paralelo dentro de un mismo MPPT1 → 30 módulos, un único PMP1. Con sombra parcial en un grupo, el PMP1 se degrada a PMP1' (menor potencia) porque las perturbaciones de una cadena afectan a las demás en paralelo.
- Inversor/solución con varios seguidores PMP: inversores multi-string, solución con optimizadores (MLPE), solución con micro-inversores (MLPE). Ejemplo: 3 grupos de 10 módulos cada uno en su propio MPPT (PMP1, PMP2, PMP3) independiente → 30 módulos, 3 PMP independientes, cada grupo optimiza su propio punto sin afectar a los demás.

**Optimización de potencia con sombras parciales:** mejoras del algoritmo de búsqueda del PMP para plantas con sombras parciales, ya que en estas condiciones la curva de potencia presenta dos picos (máximo local y máximo global). Comparativa gráfica: inversor sin escaneo periódico se queda en el punto de máxima potencia "local" (menor); inversor con búsqueda del punto de máxima potencia global (con escaneo periódico) encuentra el pico correcto de mayor potencia.

**Rango de tensión de funcionamiento permitido (diapositiva 72, repetida en 84):**
- **Tensión de arranque** (Vmin, start, init): por debajo, el inversor no trabaja. Peor situación con temperatura máxima.
- **Rango de tensión PMP** (Vpmp min/max): rango dentro del cual el inversor trabaja a potencia nominal; fuera de este rango puede trabajar pero no a potencia nominal (siempre a menor potencia). Peores situaciones: Vmin a temperatura alta, Vmax a temperatura mínima.
- **Tensión de circuito abierto** (Voc): tensión máxima que permiten los componentes (inversor y módulos); por encima existe riesgo de avería (peor situación con temperatura mínima). Valores típicos máximos de 1000V o 1500V.
- Codificación por colores de zonas de tensión sobre el eje Vdc(V): naranja = tensión demasiado baja (no trabaja, no se estropea), verde = rango óptimo de trabajo, amarillo = fuera del rango MPP (trabaja, no óptimo), rojo = tensión demasiado alta (peligro de avería).
- Ejemplo de tabla técnica de curvas de potencia de salida vs tensión de entrada CC para modelos S5-EH1P3K-L a S5-EH1P6K-L: potencia PV recomendada máx (4800W-8000W), tensión máxima de entrada 600V, tensión nominal 330V, tensión de arranque 120V, rango MPPT 90-520V, rango MPPT a carga completa entre 100-520V y 200-520V según modelo.

**Topología con o sin transformador:**
- El transformador da aislamiento galvánico entre generador CC y red AC, pero reduce el rendimiento (pérdidas).
- No es obligatorio incorporar transformador de aislamiento galvánico siempre que se cumplan las directrices y normas de la Nota de interpretación del REBT.
- **Con transformador**: más costoso, más peso, menos eficiencia.
- **Sin transformador (TL)**: más económico, más ligero, mejor eficiencia; sin separación galvánica; no aptos para módulos FV que requieren puesta a tierra de uno de los dos polos DC.
- **Con transformador de alta frecuencia (HF)**: peso reducido y eficiencia mejorada respecto al transformador convencional.

### 6. Seguridad (diapositivas 75-80)

**Arco eléctrico**: riesgo de incendio en instalaciones FV, ilustrado con imagen de arco entre conductores de cobre y panel FV en llamas.

**Conectores DC — análisis FMEA de fallos:**
- FMEA (Failure Modes and Effects Analysis) de TÜV Rheinland: rating de fallos de módulos FV por RPN (Risk Priority Number); entre los peores: "different kinds of connectors" (~1500 RPN), "connector not properly connected", "breakage of the front glass".
- FMEA CPN (Cost Priority Number) del proyecto SolarBankability (Comisión Europea, Horizon 2020): top 20 fallos técnicos por impacto económico (€/kWp/año de pérdida): los tres peores son "wrong/absent cable connection" (€3,93), "broken/burnt connectors" (€2,67), "wrong installation" (€1,35); otros incluyen error message (€0,17), potential induced degradation (€0,21), glass breakage (€0,27), tracker failure (€0,31), broken module (€0,24), wrong/absent cables (€0,36), improper installation (€0,45), burnt supply cable/socket (€0,60), broken transformer (€0,66), inverter not operating (€0,67), shading (€0,68), damaged cable (€0,69), improper/inadequate installation (€0,71), soiling (€0,86).

**Conectores MC4**: MC4 no es un estándar sino un nombre comercial registrado y protegido (Stäubli), no compatible con ningún otro conector. Especificaciones incluyen niveles de tensión (TÜV 1000V/1500V, UL 1000V/1500V), rango de secciones de cable (1,5mm² a 10mm²/8-14 AWG), sistema de bloqueo (safety locking device, según NEC 2014), tecnología Multilam de larga estabilidad, certificaciones TÜV, cTÜVus, UL, EAC, CSA, JET, CQC.

**AFCI (Arc Fault Current Interruption)** — interruptor de circuito por fallo de arco: mitiga proactivamente el riesgo de incendio, detecta arco eléctrico en el circuito, avisa del peligro mediante app y portal web. Tabla de protecciones típicas de ficha técnica de inversor: protección anti-isla, sobrecorriente de salida, cortocircuito, **AFCI integrado (protección de falla de arco DC)**, interruptor de DC integrado, polaridad inversa DC, sobrevoltaje fotovoltaico, anti-retorno de batería. Gráfica de espectro de frecuencia (Nominal Power dB vs Frequency kHz) comparando sistema con arco vs sin arco (pico de amplitud entre 20-60kHz en presencia de arco).

**RSD (Rapid Shut Down)**: normativa **NEC 690.12** (USA y América principalmente): "los circuitos del sistema dentro y más allá de los perímetros del edificio se reducen a 80 voltios o menos dentro de los 30 segundos". Esquema con componentes PEFS-PL, PEFS-EL, dispositivo Rapid Shutdown en el tejado, Junction Box, Emergency Shutdown Switch para uso de bomberos.

### 7. Otros aspectos generales de selección (diapositivas 81-83)

- **Precio** (comparado por relación €/W, factor muy importante en el mercado).
- **Grado de protección** contra infiltraciones para instalación exterior (p.ej. IP65).
- **Peso** (kg), relevante para instalación y mantenimiento (sustitución/reparación).
- **Opciones disponibles y sus costes**: comunicación y monitorización (portal web tiempo real/API, datalogger, acceso y parametrización remota, comunicación por protocolos estándar TCP/Modbus/Sunspec, protecciones contra sobretensión sustituibles o no, gestión de consumos/activación de cargas).
- **Garantía**: duración y forma de aplicarla (sustitución o reparación, coste de transportes, compensación económica).
- **Servicio postventa**: quién lo ofrece (fabricante conocido/de confianza vs empresa subcontratada), portes de envíos/desplazamientos, equipo técnico en España.

**Resumen de criterios de decisión según prioridad (diapositiva 83):**
| Prioridad | Solución recomendada |
|---|---|
| Seguridad (rapid shut-down, tensiones CC bajas, arco eléctrico) | MLPE, AFCI |
| Precio | Minimizar número de inversores; si hay/habrá acumulación, elegir inversor híbrido |
| Maximizar producción anual | MLPE |
| Varios MPPT | MLPE, multi-string, varios inversores |
| Monitorización detallada a nivel de módulo | MLPE |
| Monitorización con control remoto/integración API/SCADA | Consultar fabricantes |
| Control de consumos (cargas), gestión de carga de VE | Solo algunos fabricantes lo ofrecen |
| Servicio postventa | Fabricante con presencia en España/Europa y atención en idioma requerido |
| Inyección cero con certificación | Cumplimiento del Anexo 1 del ITC-BT-40 (norma UNE 217001:2020) |

### 8. Fichas técnicas de inversores — ejemplos reales (diapositivas 85-90)

**SMA Sunny Boy 3.0/3.6/4.0/5.0/6.0** (entrada DC): potencia máxima de generador 5500-9000Wp, tensión máxima de entrada 600V, rango de tensión MPP 110-500V a 210-500V según modelo, tensión de entrada nominal 365V, tensión mínima/inicial 100V/125V, corriente máxima de entrada A/B 15A/15A, corriente de cortocircuito máx A/B 20A/20A, 2 MPPT independientes (A:2 strings, B:2 strings). Salida AC: 3000W a 6000W según modelo a 230V/50Hz.

**Fronius ECO 25.0-3-S / 27.0-3-S**: corriente máxima de entrada 44,2A/47,7A, corriente máxima de cortocircuito por serie FV 71,6A, tensión mínima de entrada 580V, tensión CC mínima de puesta en servicio 650V, tensión de entrada nominal 580V, tensión máxima de entrada 1000V, rango de tensión MPP 580-850V, 1 seguidor MPP, 6 entradas CC, máxima salida del generador FV 37,8kWpico. Salida: potencia nominal CA 25000W/27000W, máxima corriente de salida 36,1A/39,0A, acoplamiento a red 3-NPE 380V/220V o 3-NPE 400V/230V (+20%/-30%), frecuencia 50/60Hz (45-65Hz), THD <2,0%, factor de potencia 0-1 ind./cap.

**Inversor central de ejemplo (tipo Huawei, sin marca explícita en la diapositiva)**: eficiencia máxima 98,8%@480V, 98,6%@380/400V; eficiencia europea 98,6%@480V, 98,4%@380/400V. Entrada: tensión máxima 1100V, corriente máxima/cortocircuito por MPPT 26A/40A, tensión de arranque 200V, rango MPPT 200-1000V, tensión nominal de entrada 720V@480Vac/600V@400Vac/570V@380Vac, 20 entradas, 10 MPPT. Salida: potencia nominal AC 100.000W, potencia aparente máxima 110.000VA, tensión de salida 480/400/380V 3W+(N)+PE, frecuencia 50/60Hz, corriente nominal/máxima de salida según tensión, factor de potencia ajustable 0,8LG...0,8LD, THD máx <3%.

**SolarEdge SE12.5K/SE15K/SE16K/SE17K/SE25K/SE27.6K** (con optimizador): potencia nominal/máxima de salida CA 12500-27600VA, tensión de salida 380/220V o 400/230V, frecuencia 50/60±5Hz, redes trifásicas WYE con neutro (3/N/PE). Entrada: potencia máxima CC 16850-37250W, sin transformador (sin puesta a tierra), tensión máxima de entrada 1000Vdc, tensión de entrada CC nominal 750Vdc, corriente máxima de entrada 21-40Adc, rendimiento máximo 98-98,3%, rendimiento ponderado europeo 97,6-98%.

**Enphase IQ8 Series Microinverters (IQ8MC-72-M-INT / IQ8AC-72-M-INT / IQ8HC-72-M-INT)**: compatibilidad con 54-72 células (108-144 células partidas). Entrada CC: tensión mínima/máxima 18/60V, tensión de entrada de arranque 22V, tensión asignada de entrada 35,0/36,5/37,0V, rango SPMP 25/45-29,5/45V, tensión de operación mínima/máxima 18/49V, corriente máxima de entrada 14A, corriente de cortocircuito máxima permitida 25A (20A calculada con factor de seguridad 1,25 según IEC 62548), potencia máxima de entrada 480/530/560W. Salida CA: potencia aparente máxima 330/366/384VA, potencia asignada 325/360/380W, tensión nominal de red 230V, tensión mínima/máxima 184/276V, corriente máxima de salida 1,43/1,59/1,67A, frecuencia nominal 50Hz.

### 9. Derating por temperatura (diapositiva 91)

Gráfica de potencia de salida relativa (output power/rated power) vs temperatura ambiente para tres niveles de tensión CC (Vdc=550V, 600V, 850V): la potencia se mantiene en ~1,0-1,1 hasta ~35-40°C, luego decrece linealmente hasta valores de 0,9 (Vdc=550V), 0,85 (600V) y 0,78 (850V) a 60°C. Segunda gráfica en valores absolutos de potencia de salida (W) vs temperatura ambiente (-25°C a 60°C) para 540Vdc, 600Vdc y 800Vdc: mantiene ~110 hasta ~20-25°C, luego decrece hasta 60-77 a 60°C.
**Efecto**: pérdida de producción y reducción de la vida útil de los componentes.

### 10. Aspectos técnicos de la configuración (diapositivas 93-107)

**Herramientas de dimensionado de fabricantes** (diapositiva 94, enlaces):
- SMA: https://www.sunnydesignweb.com
- Fronius: https://fronius.solarconfigurator.de/solar.configurator/quick ; https://creator.fronius.com/pv-design
- Huawei: https://eu.smartdesign.huawei.com
- Kostal: http://updates.solarschmiede.de/download.php (Kostal SolarPlan)
- Enphase: https://enphase.com/es-es/installers/microinverters/calculator
- SolarEdge: https://designer.solaredge.com/sites

**Datos técnicos claves de los módulos FV** (curva I-V a 25°C y 1kW/m²):
- **PMP**: punto de máxima potencia (donde el inversor busca trabajar siempre para máxima producción).
- **Voc**: tensión de circuito abierto — la Voc resultante de las series FV no debe superar nunca la Voc permitida del inversor (peor caso a temperatura mínima), o lo estropea.
- **Vpmp**: tensión en máxima potencia — debería estar próxima a la tensión nominal del inversor para mayor eficiencia (a temperatura normal).
- **Isc**: corriente de cortocircuito — no debe superar nunca la corriente admitida en las entradas del inversor (peor caso a temperatura máxima), o lo estropea.
- **Impp**: corriente de máxima potencia — no debería superar la Impp admitida del inversor para evitar recortes de corriente (hasta 10% sería admisible), peor caso a temperatura máxima.

**Módulos FV en serie** (inversor string): la tensión se suma (tensión total CC = suma de tensiones de cada módulo); la corriente es la misma para todo el circuito (corriente total CC = corriente del módulo que menos produce). En caso de sombra parcial de un solo panel, toda la fila (string) se ve afectada.

**Módulos FV en paralelo** (nota: configuración más académica, no se suele usar en sistemas de conexión a red): la corriente se suma (corriente total CC = suma de corrientes de cada módulo); la tensión es la misma para todo el conjunto (tensión total CC = tensión de 1 módulo). En caso de sombra: sombra parcial tiene efecto leve (afecta principalmente al módulo sombreado); sombra pronunciada reduce la tensión de toda la cadena.

**Módulos FV en serie/paralelo**: corriente total CC = suma de corriente de las filas en paralelo; tensión total CC = tensión de cada cadena en serie (las cadenas en paralelo deben tener igual tensión).

**Corriente de los módulos FV — reglas de compatibilidad:**
- La Isc del inversor nunca debe ser superada por la Isc del módulo FV.
- La Impp del inversor puede ser superada por la Impp del módulo FV, sabiendo que puede haber recortes en momentos puntuales; se recomienda no sobrepasar, o muy poco.
- Comparativa de corrientes Isc/Impp por generación de módulo según tamaño de célula partida: Trina Vertex S R (G12R, 182mm×210mm) 10,86/10,36A; módulos M6 166mm (hasta 2019 aprox.) 11,6/11,04A; Trina Vertex S (G12, 210mm) 12,4/11,85A; LONGI/JA Solar M10 182mm 14,02/13,12A; Trina Vertex G12 210mm (555W) 18,6/17,25A.
- Ejemplos de fichas de compatibilidad de corriente de inversores: SMA Sunny Tripower 5.0/6.0/8.0/10.0 Smart Energy (corriente máxima de entrada A/B 12,5A/12,5A a 12,5A/25A, cortocircuito 20A/20A a 20A/40A); modelos S5-EH1P3K-L a P6K-L (corriente máxima de entrada 15A/15A, cortocircuito 22,5A/22,5A, 2 MPPT/2 cadenas); Fronius Primo GEN24 3.0-6.0 PLUS (2 MPPT, corriente máxima disponible 22A/12A por MPPT, conectable en paralelo hasta 36A, cortocircuito 33A/18A); Huawei SUN2000-2KTL-L1 a 6KTL-L1 (máx. intensidad por MPPT 12,5A, cortocircuito por MPPT 18A).
- Gráfica de curva diaria de potencia de salida (kW) de planta FV a lo largo del día, con meseta plana ~950-960kW entre 10:00 y 15:00, ilustrando el efecto de clipping por Impp superada en horas centrales.

**Ratio DC/AC (sobredimensionado del campo FV respecto al inversor):**
- No hay reglas fijas; depende del caso.
- Para instalación "estándar" se admite un mínimo de ~10% más de potencia pico que de potencia nominal del inversor (regla "generalizada" de hasta ~20% kWp/kW). Ejemplo: 20% = 12kWp de módulos con inversor de 10kW.
- Hoy en día se comentan ratios DC/AC de hasta 50% y más según condiciones.
- **Factores que afectan el ratio DC/AC**: ubicación del proyecto (zonas de menor irradiación son más propensas a ratio alto), orientación del generador FV (instalaciones con varias orientaciones son más propensas a ratio alto), gran demanda energética (si toda la energía se consume, es más propenso a ratio alto).
- **Procedimiento recomendado**: 1º determinar la potencia del generador (según uso, necesidad, superficie disponible, energía requerida); 2º determinar la potencia del inversor en función del generador solar; 3º determinar si el inversor debe tener varias entradas/MPPT para su posterior elección.
- Gráfica conceptual: potencia sobredimensionada (Psobredimensionada) vs potencia del inversor (Pinversor) vs potencia nominal (Pnominal) a lo largo de 24h, mostrando "incremento de energía debido al sobredimensionamiento" y zona de "clipping" (pérdida por recorte) cuando la curva de potencia disponible supera Pinversor.
- **Estudio de sensibilidad** (gráficas de barras, ubicaciones Jaén y Bilbao, orientaciones Este/Este-Oeste/Sur, ratio DC/AC de 100% a 170%): el incremento de energía producida anual crece de forma decreciente con el ratio (de ~0,1% a 100% hasta ~0,6% a 170%), mientras las pérdidas por clipping crecen negativamente de forma más pronunciada a partir de ratio ~140-150% (hasta -0,06% a -0,08% en 170% para orientación Sur, la más penalizada por concentrar producción en menos horas).

**Ejercicios de práctica propuestos (diapositiva 108, sin resolver en la fuente):**
1. Módulos JA Solar gama JAM66S30 (~500Wp) con inversor SMA Sunny Tripower CORE1 50kW — pregunta sobre limitaciones y alternativas de inversor de igual potencia.
2. Módulos Trina VERTEX TSM-DE20 (~600W) con el mismo inversor SMA Sunny Tripower CORE1 50kW — pregunta sobre qué valor cambia sustancialmente respecto al punto 1 y cómo afecta a la configuración.
3. Módulo LONGi HiMo X6 (LR5HTB, ~420W) con inversor Fronius Primo Gen24 usando los 2 MPPT — pregunta sobre limitaciones.

**Enlaces de interés citados en la fuente**: www.idae.es, https://amaranzero.es/catalogo/solar, https://www.sma.de/es, www.fronius.com, https://solar.huawei.com, www.kostal-solar-electric.com, www.enphase.com, www.solaredge.com.

## Datos clave (con página/diapositiva de origen)

- (Diapositiva 4-5) Cifras de AMARA NZero: 715 M€ facturación 2023, 1.028 M€ previsión 2024, 1.817 empleados, presencia en 15 países.
- (Diapositiva 13) Rangos de tensión de red españoles admitidos por inversor: 195V-253V, frecuencia 48-51Hz.
- (Diapositiva 13) Normas citadas para seguridad de red: UNE-EN 62116:2014 V2, UNE 217001:2020, UNE 217002:2020, RD 1699/2011, NTS (UE) 2016/631.
- (Diapositiva 15) Norma alemana de reducción de potencia por sobrefrecuencia: -40%/Hz entre 50,2-51,5Hz; norma italiana: -83,3%/Hz entre 50,3-51,5Hz.
- (Diapositiva 16) Inyección cero regida por UNE 217001:2020, equivalente al RD 244/2019 Anexo 1.
- (Diapositiva 21) Rangos de potencia por tecnología: string/multi-string ±1,5-330kWn; MLPE ±1000Wn; híbridos ±1,5-10kWn; centrales >50kW hasta varios MW.
- (Diapositiva 34) SolarEdge P300-P505: potencia máx. entrada 340-505W, tensión máxima absoluta 48-125V según modelo.
- (Diapositiva 36) Inversores centrales: SMA Highpower Peak3 150kW (1 MPPT); Huawei SUN2000 330-KTL-H1 (330kW, 6 MPPT).
- (Diapositiva 43) Inversores híbridos DC-coupling: rango típico 1-10kW (ya hay modelos de 50/100/150kW).
- (Diapositiva 53) Tesla Powerwall 2: batería AC 14kWh con inversor AC incluido; Powerwall 3 es All-in-One con inversor híbrido.
- (Diapositiva 61) Potencia de instalación FV en España según RD 1699/2011 = suma de potencia nominal de inversores (hasta 100kW); RD 1955/2000 para >100kW.
- (Diapositiva 63) Tabla comparativa RD 661/2007 vs RD 1699/2011: frecuencia máxima cambia de 51Hz a 50,5Hz (t=0,5s); resto de parámetros de tensión y frecuencia mínima idénticos (195,5V/1,5s; 48Hz/3s).
- (Diapositiva 64) Fórmula de eficiencia europea η_euro con pesos 3%/6%/13%/10%/48%/20% para P5/P10/P20/P30/P50/Pn.
- (Diapositiva 72/84) Valores típicos máximos de tensión de circuito abierto (Voc) del inversor: 1000V o 1500V.
- (Diapositiva 78) FMEA SolarBankability: peor fallo económico "wrong/absent cable connection" con €3,93/kWp/año de pérdida; "broken/burnt connectors" €2,67/kWp/año.
- (Diapositiva 80) Normativa NEC 690.12 (RSD): circuitos reducidos a ≤80V dentro de 30 segundos.
- (Diapositiva 96) Comparativa de corriente Isc/Impp de módulos por tamaño de célula: desde 10,86/10,36A (G12R 182mm) hasta 18,6/17,25A (G12 210mm, módulo 555W Trina Vertex).
- (Diapositiva 99) Regla generalizada de ratio DC/AC: mínimo ~10%, "generalizada" ~20% kWp/kW; hoy en día se comentan ratios de hasta 50% y más.
- (Diapositiva 101) Estudio de sensibilidad ratio DC/AC en Jaén y Bilbao: pérdidas por clipping alcanzan hasta -0,06%/-0,08% a ratio 170% en orientación Sur.

## Relevancia para el TFM

- **Capítulos del índice a los que aporta**: Capítulo 6 (dimensionado del sistema FV, PVsyst) y muy especialmente **Capítulo 7 (estrategia de carga/descarga y arquitectura del sistema de almacenamiento)**, ver `Memoria/indice_propuesto.md`.
- **Qué aporta exactamente**: Es la fuente primaria y única disponible en la base de conocimiento del TFM para resolver la **decisión pendiente DC-coupling vs. AC-coupling** de la arquitectura de baterías (registrada como pendiente en memoria `project_hallazgos_presentaciones_master.md`). La presentación detalla de forma exhaustiva las tres arquitecturas posibles (inversor híbrido DC-coupling, convertidor CC/CC DC-coupling para retrofit, e inversor cargador AC-coupling) con sus pros/contras, marcas comerciales y criterios técnicos de selección — material directamente citable como apoyo técnico no normativo. También aporta el marco normativo de conexión a red aplicable al capítulo de marco regulatorio (RD 1699/2011, UNE 217001:2020 para inyección cero) y criterios de dimensionado (ratio DC/AC, número de MPPT, compatibilidad de corriente Isc/Impp) relevantes para justificar decisiones de configuración del inversor en PVsyst.
- **Confianza en los datos**: Todas las cifras, tablas y normas están extraídas literalmente de la presentación original (documento no citable en el TFM por ser material docente de terceros — apoyo conceptual únicamente, no fuente bibliográfica). Ninguna cifra fue completada con conocimiento general del modelo; donde la fuente no especifica un dato (p.ej. marca del inversor de la diapositiva 87) se ha indicado explícitamente como no identificado en la fuente.

## Notas de procesamiento

Documento leído íntegro (96 páginas/diapositivas, en cuatro bloques de lectura consecutivos: 1-20, 21-40, 41-60, 61-80, 81-96). Ninguna diapositiva fue omitida. Las diapositivas de portada e índice repetidas (aparecen 5 veces a lo largo del documento como separadores de sección) no se han duplicado en el resumen, consolidándose su contenido bajo los epígrafes correspondientes. La diapositiva 87 (SUN2000-100KTL, entrada de eficiencia 98,8%/98,6%) no indica marca explícita en el pie de imagen visible, aunque los parámetros de la tabla (nomenclatura SUN2000, 10 MPPT, 100kW) sugieren fabricante Huawei por coherencia con el resto de la presentación — señalado aquí como inferencia razonable, no como dato confirmado en la fuente. Las imágenes puramente ilustrativas (fotos de tejados, arco eléctrico, logos de fabricantes) se han descrito solo cuando aportaban contenido técnico relevante (p.ej. tablas incrustadas en capturas de software).
