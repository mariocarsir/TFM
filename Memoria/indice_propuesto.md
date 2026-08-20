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
2.5. Marco normativo y regulatorio

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

## 10. Pliego de condiciones técnicas

*(Normativa ERMA: "No suele ser parte de un TFM, pero en instalaciones y proyectos es
imprescindible indicar especificaciones técnicas, calidades y garantías de elementos
principales". Precedente de 2025: `TFM-MAD9_signed.pdf` incluye un capítulo de mantenimiento
y garantías equivalente — ver `conocimiento fotovoltaico/Referencia/analisis-comparativo-tfm-referencia-erma.md`.)*

10.1. Especificaciones de los materiales y componentes del proyecto
10.2. Calidades mínimas según normas aplicables
10.3. Pruebas y ensayos requeridos
10.4. Reglamentación y normativa específica
10.5. Aspectos del contrato: garantías de suministros y funcionamiento

## 11. Estudio de seguridad y salud

*(Normativa ERMA: "Apartado típico de TFM de proyecto/instalación".)*

11.1. Identificación de riesgos en fase de diseño y montaje
11.2. Medidas preventivas y de protección
11.3. Plan de seguridad básico

## 12. Planificación temporal **[+ capítulo nuevo]**

*(Puede degradarse a sección de otro capítulo si el volumen no lo justifica.)*

## 13. Conclusiones y líneas futuras

11.1. Conclusiones
11.2. Líneas futuras **[+]**

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
| Requisitos y datos de partida | Cap. 2 (marco normativo) + Cap. 3 (emplazamiento, consumo, recurso solar, restricciones) |
| Metodología y cálculos (hipótesis, procedimientos, herramientas) | Cap. 5-9, con PVsyst y Excel como herramientas de cálculo documentadas en el CLAUDE.md |
| Presentación y análisis de resultados | Secciones de resultados de los caps. 6, 7, 8 y 9 |
| Pliego de condiciones técnicas | Cap. 10 |
| Estudio de seguridad y salud | Cap. 11 |
| Planificación (si aplica) | Cap. 12 (puede degradarse a sección si el volumen no lo justifica) |
| Conclusiones | Cap. 13 — debe seguir las reglas de la guía: correspondencia 1:1 con alcances/resultados relevantes, sin elementos nuevos ni gráficas/tablas, no es un resumen, redacción clara y rigurosa |
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
| Nuevos caps. 10-11 (condiciones técnicas y seguridad) | Incluidos según la guía ERMA y el precedente de `TFM-MAD9_signed.pdf` (2025), que dedica un capítulo de mantenimiento y garantías equivalente. |
| Caps. 12 y 13 (antes 10 y 11) | Planificación temporal y conclusiones, desplazadas en numeración por la adición de los dos anteriores. |
| Sección 3.2 (criticidad del CPD) | Aportación propia: ningún ejemplo trata una carga crítica 24/7; es lo que diferencia este TFM y condiciona el dimensionado de baterías. |
