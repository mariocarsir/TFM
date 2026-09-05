# Índice propuesto — TFM Mario Carrión Sirvent

Autoconsumo fotovoltaico con almacenamiento en un centro de proceso de datos (CPD).

Consolidación del índice preliminar de Mario con los cuatro bloques aprobados a partir de
los TFM de años anteriores (`Documentacion de apoyo/Ejemplos TFM/`: Andrea Barrios 2022/23 y
Manuel Arcas 2023/24). Marcados con **[+]** los apartados nuevos respecto al preliminar.

Respeta la estructura oficial exigida por la normativa ERMA: índice → memoria (introducción,
descripción, cálculos, conclusiones, referencias) → anexos. Límite: 150 páginas.

---

## Preliminares

- Portada (plantilla oficial `Plantillas/Portada TFM.docx`)
- Portada de firmas
- Agradecimientos
- Resumen + palabras clave
- Códigos UNESCO **[+]**
- Abstract + keywords
- Índice general
- Índice de figuras
- Índice de tablas
- Índice de ecuaciones
- Lista de acrónimos y abreviaturas

## 1. Introducción

1.1. Contexto y motivación
1.2. Justificación: actualidad del tema y Objetivo de Desarrollo Sostenible (ODS) al que contribuye **[+]**
1.3. Objetivos del proyecto
1.4. Alcance del trabajo
1.5. Emplazamiento: ubicación del CPD (dirección/referencia catastral, coordenadas UTM) **[+]**
1.6. Metodología **[+]**

## 2. Estado del arte y marco normativo

2.1. Tecnologías de generación solar fotovoltaica
2.2. Integración arquitectónica: BIPV frente a BAPV
2.3. Almacenamiento electroquímico aplicado a autoconsumo **[+]**
2.4. Eficiencia energética en CPDs: métrica PUE
  — incluye la tendencia regulatoria: proyecto de RD de centros de datos del MITECO (audiencia
  pública, no exigible todavía), que fija 80 % renovable hora a hora y PUE ≤ 1,15 **[+]**
2.5. Normativa aplicable **[+ reformulado]**

*(La normativa NO se cita con `\cite` ni figura en el capítulo de Referencias: se relaciona aquí
de forma completa, al modo del apartado 1.4 de `TFM-MAD9_signed.pdf`, con título completo, qué
regula y cómo aplica a este proyecto. En el cuerpo del texto se menciona en forma larga la
primera vez y en forma corta a partir de la segunda.)*

2.5.1. Marco europeo
2.5.2. Normativa estatal con rango de ley
2.5.3. Normativa estatal de rango reglamentario
2.5.4. Normativa autonómica y local
2.5.5. Normas técnicas de referencia

## 3. Análisis del emplazamiento y perfil de consumo

3.1. Descripción del edificio: CPD Madrid
3.2. Criticidad y restricciones de operación del CPD: redundancia y SAIs **[+]**
3.3. Recurso solar: elección y contraste de bases de datos meteorológicas **[+ ampliado]**
3.4. Determinación del perfil horario de consumo
3.5. Datos económicos de partida: tarifa de acceso y periodos **[+]**
3.6. Restricciones del emplazamiento: sombras, cargas de viento y capacidad portante de cubierta **[+]**

## 4. Tipología de autoconsumo y tramitación **[+ capítulo nuevo]**

4.1. Modalidad de autoconsumo seleccionada
4.2. Procedimiento de legalización y agentes implicados
4.3. Plazos orientativos

## 5. Estudio de alternativas de integración

5.1. Definición de escenarios y tecnologías
5.2. Criterios de evaluación **[+]**
5.3. Selección de la solución óptima

## 6. Diseño e ingeniería de la solución fotovoltaica

6.1. Selección de componentes: módulos, inversores y estructura **[+]**
6.2. Dimensionado del campo generador: cálculo de strings y ratio DC/AC **[+ ampliado]**
6.3. Cálculos eléctricos y esquema unifilar
6.4. Simulación en PVsyst: pérdidas detalladas y diagrama de pérdidas **[+]**
6.5. Producción esperada: Performance Ratio, P50 y P90 **[+]**
6.6. Análisis del grado de autoconsumo y autosuficiencia

## 7. Diseño del sistema de almacenamiento **[+ capítulo nuevo — núcleo del TFM]**

7.1. Justificación y criterios de dimensionado
7.2. Selección de la tecnología de baterías
7.3. Estrategia de gestión: carga y descarga por periodos tarifarios
7.4. Modelo horario anual y degradación
7.5. Comparativa de resultados con y sin almacenamiento

## 8. Análisis económico

8.1. Mediciones y presupuesto detallado **[+ ampliado]**
8.2. Hipótesis de partida: costes, ahorros e incentivos fiscales **[+]**
8.3. Escenarios de evolución del precio de la electricidad **[+]**
8.4. Rentabilidad: VAN, TIR, payback y LCOE **[+ LCOE]**
8.5. Análisis de sensibilidad **[+]**

## 9. Análisis medioambiental

9.1. Huella de carbono y emisiones evitadas
9.2. Fin de vida y reciclaje de módulos y baterías **[+]**

## 10. Estudio de seguridad y salud — PENDIENTE DE ACORDAR CON EL TUTOR

*(La normativa ERMA lo sitúa entre los apartados «cuando proceda», es decir, opcional, y ninguno
de los tres TFM de referencia lo incluye — ver `Memoria/analisis/comparacion-estructura-tfm.md`.
Se mantiene en el índice a la espera de que Julio Amador confirme si lo espera.)*

10.1. Identificación de riesgos en fase de diseño y montaje
10.2. Medidas preventivas y de protección
10.3. Plan de seguridad básico

## 11. Planificación temporal **[+ capítulo nuevo]**

*(Puede degradarse a sección de otro capítulo si el volumen no lo justifica. Único precedente:
Barrios, cap. III.6.)*

## 12. Conclusiones y líneas futuras

12.1. Conclusiones
12.2. Líneas futuras **[+]**

## Referencias

## Anexos

- Anexo A. Planos **[+]**
- Anexo B. Fichas técnicas de los equipos **[+]**
- Anexo C. Informe de simulación PVsyst **[+]**
- Anexo D. Flujos de caja **[+]**
- Anexo E. Modelo de gestión del almacenamiento **[+]**

---

## Correspondencia con la estructura genérica ERMA **[+]**

La normativa ERMA (`Documentacion de apoyo/GUIA Elaboracion TFM ERMA20.pdf`, pp. 5-19) propone
un índice genérico de ejemplo (Introducción → Requisitos y datos de partida → Metodología y
cálculos → Presentación y análisis de resultados → Otros apartados → Conclusiones →
Referencias → Anexos). Este TFM no repite esos títulos literales — organiza el contenido en
capítulos temáticos propios, como hacen los dos TFM de referencia — pero cada categoría
genérica debe quedar cubierta en algún punto del documento:

| Categoría genérica ERMA | Dónde se cubre en este índice |
|---|---|
| Introducción (objetivo, alcance, justificación, emplazamiento, antecedentes, normas) | Cap. 1, con las subsecciones 1.1-1.6 (emplazamiento/ODS/metodología) |
| Requisitos y datos de partida | Cap. 2 (normativa aplicable) + Cap. 3 (emplazamiento, consumo, recurso solar, restricciones) |
| Metodología y cálculos (hipótesis, procedimientos, herramientas) | Cap. 5-9, con PVsyst y Excel como herramientas de cálculo documentadas en el CLAUDE.md |
| Presentación y análisis de resultados | Secciones de resultados de los caps. 6, 7, 8 y 9 |
| Pliego de condiciones técnicas | **Eliminado** (05/09/2026): opcional por normativa y sin precedente en ninguno de los tres TFM de referencia |
| Estudio de seguridad y salud | Cap. 10, pendiente de acordar con el tutor |
| Planificación (si aplica) | Cap. 11 (puede degradarse a sección si el volumen no lo justifica) |
| Conclusiones | Cap. 12 — debe seguir las reglas de la guía: correspondencia 1:1 con alcances/resultados relevantes, sin elementos nuevos ni gráficas/tablas, no es un resumen, redacción clara y rigurosa |
| Referencias | Capítulo "Referencias" (IEEEtran, compatible con el formato "número entre corchetes" que acepta la guía) |
| Anexos | Anexos A-E |

## Cambios respecto al índice preliminar

| Cambio | Motivo |
|---|---|
| Nuevo cap. 7 de almacenamiento | El preliminar no tenía ningún apartado de baterías pese a estar en el título del TFM. En Arcas (2023/24) es un capítulo completo. |
| Nuevo cap. 4 de tramitación | Presente en los dos ejemplos; el tribunal espera el recorrido administrativo (modalidad, CAU, punto de acceso). |
| Cap. 6 desdoblado y ampliado | El preliminar cerraba dimensionado y producción en 3 secciones; se añade el rigor de simulación (pérdidas, PR, P50/P90) que ambos ejemplos documentan. |
| Cap. 3 ampliado | Se incorporan restricciones estructurales (viento, cubierta), elección de BBDD meteorológica y datos económicos de partida, todo tomado de Arcas. |
| Cap. 8 ampliado | Se añaden mediciones, incentivos fiscales, escenarios de precio, LCOE y sensibilidad (Barrios + Arcas). |
| Nuevos caps. 1.2, 1.5 (emplazamiento/ODS) | Exigencia normativa ERMA: localización formal con referencia catastral/UTM y justificación con Objetivos de Desarrollo Sostenible. |
| Sección 3.2 (criticidad del CPD) | Aportación propia: ningún ejemplo trata una carga crítica 24/7; es lo que diferencia este TFM y condiciona el dimensionado de baterías. |

## Cambios del 5 de septiembre de 2026

Derivados de la comparación estructural con los tres TFM de referencia
(`Memoria/analisis/comparacion-estructura-tfm.md`) y de la decisión sobre el tratamiento de la
normativa.

| Cambio | Motivo |
| --- | --- |
| **Eliminado el capítulo de pliego de condiciones técnicas** | La normativa ERMA lo sitúa entre los apartados «cuando proceda» (opcional) y ninguno de los tres TFM de referencia lo incluye. Lo más parecido es el cap. 7 de Fernandes, «Mantenimiento y garantías», que no es un pliego. |
| Seguridad y salud pasa de cap. 11 a cap. 10 y queda marcado como pendiente | Igual de opcional y sin precedente en los ejemplos; decisión del tutor. |
| Planificación temporal 12 → 11; conclusiones 13 → 12 | Renumeración por la eliminación del pliego. Corregida de paso la numeración interna de conclusiones, que decía 11.1/11.2. |
| **2.5 pasa de «Marco normativo y regulatorio» a «Normativa aplicable»**, con cinco subsecciones por jerarquía | La normativa no se cita con `\cite` ni aparece en Referencias: se relaciona completa en una sección propia al modo del apartado 1.4 de Fernandes. |
| El proyecto de RD de centros de datos del MITECO se traslada a 2.4 | No es derecho vigente (audiencia pública), así que no cabe en «Normativa aplicable»; como tendencia regulatoria sobre el PUE justifica el enfoque del TFM. |

### Propuestas abiertas tras la comparación

| Propuesta | Origen |
| --- | --- |
| Capítulo ligero de mantenimiento y garantías | Fernandes cap. 7; sustituto natural del pliego eliminado |
| Bloque de definiciones y expresiones matemáticas en los preliminares | Fernandes, «Definiciones y expresiones matemáticas» (11 ecuaciones) |
| Monitorización como sección del cap. 6, no como capítulo | Fernandes cap. 4 y Barrios 5.5 |
| Acotar la extensión del cap. 2 por el tope de 150 páginas | Ningún ejemplo tiene estado del arte; es la mayor divergencia propia |
| Revisar si la portada de firmas debe mantenerse | No la pide la guía ERMA y ningún ejemplo la lleva |
