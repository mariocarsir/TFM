---
type: concept
title: "Variantes FV del CPD: normativa de autoconsumo 2026"
created: 2026-08-29
updated: 2026-08-30
status: developing
tags:
  - concept
  - fotovoltaica
  - autoconsumo
  - normativa
  - cpd
  - almacenamiento
  - rdl-7-2026
domain: "Fotovoltaica / TFM"
complexity: advanced
related: []
---

# Variantes FV del CPD: normativa de autoconsumo 2026

Nota-hub de la sesión del **29/08/2026** sobre las tres variantes de autoconsumo del TFM (V1
cubierta, V2 marquesinas, V3 planta en suelo) y el marco normativo que las condiciona. Cierra el
trabajo iniciado el 28/08/2026 (parcela de 58,84 ha, geometría del `TFM.kmz`). Análisis completo en
`Memoria/analisis/estimacion-preliminar-variantes.md` (apartados 5bis y 7), commits
`3a7007e`, `ae99d84`, `313367e` de la rama `worktree-estimacion-variantes-fv`.

## Resultado central: las tres variantes, como alternativas excluyentes

| | **V1 Cubierta** | **V2 Marquesinas** | **V3 Planta en suelo** |
| --- | --- | --- | --- |
| Potencia | 338 kWp | 680 kWp | 2,00–2,50 MWp |
| Distancia al CPD | 0 m | **216 m** | 2,93 km (borde) / 3,72 km (centroide) |
| C_D sin batería | 14,2 % | 28,9 % | 43–44 % |
| **Techo de C_D con batería** | 14,2 % (no mejora) | 29,1 % (no mejora) | **86–99 %** |
| ¿Batería útil? | No | No | **Sí, decisiva** |
| Figura RD 244/2019 art. 3.g) | Próxima de red interior | Red interior **o** línea directa (dos referencias catastrales distintas) | Próxima **a través de la red** |
| Modalidad art. 4 | Sin excedentes | Sin excedentes (antivertido con sentido) | **Con excedentes obligatoria** — el antivertido no puede existir aquí |
| ¿Permiso de acceso y conexión? | No (art. 7.1.b.i) | No (art. 7.1.b.i) | **Sí** (art. 7.1.b.iii) |
| Peaje sobre lo autoconsumido | Exento | Exento | **Paga 6.1TDA** (Circular 3/2020) |

**Hipótesis de Mario confirmada con matiz:** 2,25–2,50 MWp dan 80–90 % de C_D real, pero **solo
acompañados de 4–6 MWh de batería** — solos se quedan en 43–44 %. La potencia fija el techo; la
batería decide dónde se aterriza dentro de él.

## Por qué la V3 no puede llevar antivertido: los vertidos, en cifras

La energía de V3 **llega al CPD inyectándola en la red** (la distribuidora casa las dos series hora
a hora); un antivertido bloquearía el propio mecanismo de entrega. Y aunque se ampliase mucho la
batería, el vertido no baja a cero porque es **estacional**, no diario:

| Configuración | Vertido | % de E_PV |
| --- | --- | --- |
| 2,25 MWp + 5,73 MWh (el par que da 90 % de C_D) | 274 MWh | 6,8 % |
| 2,25 MWp + 20 MWh (cuadriplicando la batería) | 163 MWh | 4,0 % |

El 72 % del vertido se concentra entre junio y septiembre (el CPD consume 10,5 MWh/día constantes;
en julio la planta produce ~14 MWh/día). Es almacenamiento estacional, fuera de alcance del TFM.

## El marco normativo 2026, y las correcciones aplicadas durante la sesión

Esta sesión corrigió varios errores propios, todos verificados contra el articulado literal
(`Bibliografia/PDFs/` y `Bibliografia/Normativa/`), no de memoria del modelo:

1. **La distancia previa: el primer párrafo del art. 3.g).iii) nunca cambió (500 m); el segundo sí,
   varias veces.** El RDL 7/2026 (DF 14.ª, apdo. Uno) dice literalmente «se modifica la letra
   iii)», es decir sustituye su texto completo, no que se limite a añadirle un párrafo a un texto
   intacto. La regla general de 500 m (primer párrafo) es la que nunca ha cambiado. Pero el
   segundo párrafo — el supuesto especial para FV en cubierta/suelo industrial/estructuras — sí
   llevaba subiendo de cifra desde 2019 (500 → 1.000 m con el RDL 18/2022 → **2.000 m** con el
   RDL 20/2022, documentado en `M6_T12_AnalisisRentabilidadI.pdf` p. 14 del máster), y el
   RDL 7/2026 lo reemplazó por su versión vigente: **5.000 m**, sin restricción de ubicación,
   para FV/eólica ≤ 5 MW. **Corrección del 30/08/2026** sobre una primera lectura (29/08/2026) que
   había generalizado la estabilidad del primer párrafo al segundo, dándolos por un único umbral
   que "siempre fueron 500 m". La distancia se mide **en proyección ortogonal en planta** (línea
   recta entre equipos de medida), no por la línea de evacuación.
2. **El apartado Dos de la misma DF 14.ª (art. 4.5 RD 244/2019) legaliza combinar** autoconsumo
   individual sin excedentes con autoconsumo a través de la red — es la única excepción admitida,
   y por eso el escenario V1+V2+V3 combinado tiene ahora encaje jurídico expreso. El mismo apartado
   obliga a que la V3 sea *con excedentes*.
3. **El nudo de conexión lo elige el promotor**, no el gestor (RD 1183/2020 art. 10.1: por encima
   de 100 kW la solicitud se hace "para un nudo o tramo de línea concreto"). Corrección de un error
   propio inicial.
4. **La energía autoconsumida de la V3 SÍ paga peaje** (peaje 6.1TDA en MT). Corrección de mayor
   impacto económico: se había asumido la exención total de los arts. 17.1/18.1 del RD 244/2019,
   pero la Circular 3/2020 de la CNMC (que fija los peajes) crea una familia específica —los
   TDA— para la energía autoconsumida a través de la red. Los cargos sí siguen exentos.
5. **La batería de autoconsumo NO entra en el régimen de acceso flexible** salvo que se le dé
   capacidad de cargar de la red. La DT 5.ª del RD 244/2019 obliga a que comparta equipo de medida
   y protecciones con la generación (no es instalación independiente); el art. 3.2 del RD 1183/2020
   excluye del ámbito al almacenamiento que nunca inyecta. Decisión de diseño adoptada: **batería
   que carga solo de la fotovoltaica** — cargar de red no aporta ahorro (mismas pérdidas de ida y
   vuelta sin arbitraje claro) y activaría todo el procedimiento de acceso de demanda.
6. **La distribuidora de la zona es i-DE (Iberdrola), no UFD** — corregido tras el inventario de
   subestaciones del `TFM.kmz` (numeración de cuatro dígitos característica de i-DE).

## Geometría verificada sobre el `TFM.kmz`

- Referencias catastrales: aparcamiento `9347902VK3994N`, edificio del CPD `9347904VK3994N` — **no
  coinciden en los 14 primeros dígitos**, así que la vía del art. 3.g).iv) (misma referencia
  catastral) no está disponible para V2; entra por la i) (línea propia, recomendado) o la iii)
  (500 m, arrastra a régimen de V3).
- Distancia CPD–aparcamiento medida: **215,8 m** (Mario: 216 m).
- Inventario de 11 subestaciones (versión del KMZ del 29/08 16:37): las dos más próximas a la
  parcela (Tres Cantos GIS, La Cereal, ~2,4 km) son solo de transporte, sin MT. La primera con
  20 kV es **Tres Cantos 3570, a 3,10 km de la parcela** — candidata natural de conexión. Incluye
  una SET dedicada "i-DE Equinix 4457" (66 kV), término de comparación con otro CPD de la zona.

## Entregables de la sesión

- `Memoria/analisis/estimacion-preliminar-variantes.md` — apartados 5bis (variantes excluyentes) y
  7 (marco regulatorio) ampliados y corregidos.
- `Memoria/analisis/scripts/variantes_excluyentes.py` — modelo horario de cada variante por
  separado, con y sin batería.
- `Bibliografia/Normativa/NormativaLinks.xlsx` — tabla de 14 normas consultadas (tipo, título,
  fecha, vigencia, resumen, URL), formateada con autofiltro y validación; columna URL pendiente de
  que Mario aporte los enlaces.
- Cuatro PDF normativos nuevos en `Bibliografia/PDFs/` y `Bibliografia/Normativa/` (RD 1183/2020,
  RD 148/2021, Circular 3/2020, más los ya existentes del RDL 7/2026 y el RD 244/2019).

## Pendiente

- Valores vigentes del peaje 6.1TDA para 2026 (resolución anual de la CNMC, no está en la Circular).
- Trazado de las líneas de MT que cruzan o bordean la parcela — decide el coste real de conexión.
- Confirmar la distribuidora (i-DE) contra el CUPS de la factura del CPD.
- Consultar capacidad de acceso de **generación** disponible en Tres Cantos 3570 antes de simular
  la V3 en PVsyst — es el riesgo crítico abierto, sustituye al que tenía la distancia.
- Decidir el trazado eléctrico de V2 (línea propia de 216 m vs. conexión a red) antes del capítulo
  económico.
