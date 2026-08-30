---
title: "Bibliografía de referencia — autoconsumo y suministro renovable en centros de datos"
fecha: 2026-08-28
estado: "lista de lectura — NINGUNA de estas fuentes es citable todavía"
tags: [bibliografia, CPD, autoconsumo, PPA, 24-7-CFE, BESS]
---

# Bibliografía de referencia

> **Aviso de método.** Esto es una **lista de lectura**, no una bibliografía citable. Según la
> regla 10 del proyecto, ninguna de estas referencias puede aparecer en la memoria del TFM hasta
> que Mario la descargue, la apruebe y pase por `bibliotecario-pdf` + skill `resumen-tecnico`. Lo
> que sigue son candidatas ordenadas por utilidad, con lo que aporta cada una y por qué.
>
> Las **únicas fuentes ya verificadas y disponibles en local** son las normativas del bloque 1,
> descargadas a `Bibliografia/Fuentes/Normativa/` y leídas literalmente, y el material docente del
> bloque 0, ya procesado por `bibliotecario-pdf`.

---

## 0. Material docente ya procesado (no citable, pero utilizable como mapa)

| Fuente | Resumen local | Qué aporta |
| --- | --- | --- |
| `M1_T11_PPA.pdf` — *Renewable Power Purchase Agreement*, Marta Arias Álvarez (EDP), Máster ERMA M1, 2025 | `conocimiento fotovoltaico/Referencia/ppa-renovables-mercado-energetico.md` | **La vía PPA completa**: taxonomía on-site / off-site *sleeved* / virtual, articulado contractual, reparto de riesgos por modalidad de entrega, precios españoles (LevelTen P25 solar 38,97 €/MWh Q4 2024), precedentes españoles reales y ranking de compradores europeos (Equinix 539 MW, Amazon 1.876 MW). Analizado en el §7.4 de `estimacion-preliminar-variantes.md` |

Fuentes primarias que esa presentación cita y que **sí serían citables** si se descargan:
Reglamento (UE) 2024/1747, informes de **LevelTen Energy** (índice trimestral de precios PPA
europeos), **WindEurope** (*European PPA Market Outlook*), **PexaQuote / PPA Tracker**, Bird &
Bird, RE-Source y el BOE-A-2021-1251 de la subasta española.

---

## 1. Normativa — ya descargada y verificada (bloque citable)

| Fuente | Fichero local | Qué aporta |
| --- | --- | --- |
| Proyecto de RD de requisitos de sostenibilidad de centros de datos (MITECO, audiencia 27/08–04/09/2026) | `MITECO_2026_PRD_CentrosDatos_audiencia_publica.pdf` | **El núcleo.** Art. 8 adicionalidad 80 %, art. 9 correlación horaria 80 %, art. 12 requisitos del PPA, DT 4.ª PUE ≤ 1,15 / WUE ≤ 0,1 |
| Memoria de análisis de impacto normativo del anterior | `MITECO_2026_MAIN_PRD_CentrosDatos.pdf` | Justificación y cuantificación de impactos; útil para el capítulo de contexto |
| RDL 7/2026, de 20 de marzo (BOE-A-2026-6544) | `BOE_RDL_7-2026_PlanIntegral_OrienteMedio.pdf` | DF 14.ª: sube el autoconsumo a distancia a 5.000 m. DA 1.ª: habilita el RD anterior |
| RD 244/2019, texto consolidado (act. 21/03/2026) | `BOE_RD_244-2019_autoconsumo_consolidado.pdf` | Art. 3.g).iii) con la redacción vigente de las distancias; modalidades de autoconsumo |

Pendientes de descargar en este mismo bloque, si se quiere cerrar el marco:

- **Reglamento Delegado (UE) 2024/1364**, de 14 de marzo — anexo III, definición de PUE y WUE. Es
  la referencia a la que remite el art. 6 del proyecto de RD para *calcular* los indicadores.
- **Directiva (UE) 2023/1791** de eficiencia energética (refundida) — art. 12 y anexo VII, régimen
  de información de centros de datos.
- **RD 1183/2020** de acceso y conexión — el procedimiento que se activa por encima de 1 MW.
- **Ley 24/2013 del Sector Eléctrico**, art. 42 (línea directa) y art. 33 (acceso y conexión).

---

## 2. Marco conceptual: *24/7 Carbon-Free Energy* frente a *annual matching*

Es la literatura que da nombre y método a lo que el art. 9 del borrador español convierte en
obligación. **Es el encuadre que le falta al TFM** para situar su métrica horaria en un debate
internacional en vez de presentarla como una elección propia.

| Referencia | Dónde | Por qué interesa |
| --- | --- | --- |
| *24/7 carbon-free electricity matching accelerates adoption of advanced clean energy technologies* | ScienceDirect, `S2542435124005440` | Demuestra que el emparejamiento horario arrastra tecnología (almacenamiento, firmeza) que el anual no arrastra. Sostiene el argumento de la batería |
| *On the means, costs, and system-level impacts of 24/7 carbon-free energy procurement* | ScienceDirect, `S2211467X24001950` | **Cuantifica el sobrecoste del horario frente al anual.** Directamente utilizable en el capítulo económico |
| *The State of 24/7 Carbon-free Energy* — World Resources Institute | wri.org | Estado del arte y taxonomía; bueno para el capítulo de contexto |
| *A Year of Operating a Data Center with 24/7 Carbon-free Energy* — EdgeConneX / Gridmatic | PDF público en edgeconnex.com | **Caso real documentado de un año completo.** Lo más parecido a lo que el TFM quiere demostrar |
| Google + AES, campus de Virginia | Nota técnica de AES | Mezcla solar + eólica + hidráulica + BESS para **≥90 % de las horas**. Muestra que con una sola tecnología no se llega: sirve para justificar por qué aquí el 100 % no es alcanzable |

**Advertencia:** el *Climate Neutral Data Centre Pact* (AWS, Google, Microsoft) exige emparejamiento
**anual**, no horario. Conviene usarlo como contraste — es exactamente el criterio que el borrador
español supera.

---

## 3. Metodología de dimensionado FV + batería con métricas de autoconsumo

Ninguna es de centros de datos, pero son las que fijan el aparato de cálculo que el TFM ya está
usando (A_PV, C_D, efecto de la limitación de vertido y del almacenamiento).

| Referencia | Dónde | Por qué interesa |
| --- | --- | --- |
| *Self-Consumption and Self-Sufficiency in Photovoltaic Systems: Effect of Grid Limitation and Storage Installation* | *Energies* 14(6), 1591, MDPI | **La más alineada con el método del TFM**: define y separa autoconsumo y autosuficiencia, y estudia el efecto de limitar el vertido — que es justo el caso antivertido del CPD |
| *Optimization of Large-Scale Battery Storage Capacity in Conjunction with Photovoltaic Systems for Maximum Self-Sustainability* | *Energies* 15(10), 3845, MDPI | Curva de autosuficiencia frente a capacidad de batería; el mismo tipo de barrido del apartado 5.6 |
| *Sizing Photovoltaic Self-Consumption Systems... Using Performance Metrics and Real Consumption Data* | *Sustainability*, doi 10.3390/su18062991 | Dimensionado a partir de perfiles de consumo reales medidos, como aquí |

---

## 4. Casos de centros de datos con FV en cubierta

| Referencia | Dónde | Dato |
| --- | --- | --- |
| *On-site rooftop solar at data centers: Everything you need to know* | DataCenterDynamics | Panorama del sector y sus límites |
| Equinix ME1, Melbourne | Nota de prensa 2024 | **1 MW en cubierta** sobre un CPD en explotación. Contrasta con los **539 MW de PPA** que la misma empresa firmó en Europa en 2023 (`ppa-renovables-mercado-energetico.md`, dp. 46): **la cubierta propia es tres órdenes de magnitud menor que la compra externa.** Ese contraste es, por sí solo, un argumento de la memoria |
| Orange, CPD de Varsovia | Nota de prensa 2024 | FV en cubierta sobre CPD europeo |
| *Energy Management for Renewable-Colocated AI Data Centers* | arXiv 2507.08011 | Colocación de generación renovable junto al CPD — el esquema de la variante 3 |

> ### El dato que conviene extraer de este bloque
>
> En la práctica del sector, **la FV en cubierta de un centro de datos cubre porcentajes de un solo
> dígito** de su consumo. La razón es de densidad de potencia: un CPD moderno demanda del orden de
> 1 kW por m² de sala, mientras que la fotovoltaica entrega ~42 W por m² de cubierta en media anual
> a esta latitud. El cociente es implacable.
>
> **El CPD de este TFM es un caso atípicamente favorable**: al ser un CPD de empresa alojado en un
> edificio grande y de baja densidad, y disponer además de un aparcamiento propio, el conjunto
> V1 + V2 alcanza el **36,8 %** sin salir de la propiedad. Merece la pena señalarlo en la memoria
> en lugar de darlo por normal: **el resultado es bueno, y su comparación con el sector lo
> demuestra.** Verificar la cifra de densidad de potencia antes de escribirla.

---

## 5. Qué falta buscar

1. **Un caso español de autoconsumo a distancia** al amparo del nuevo límite de 5 km. La norma es
   de marzo de 2026, así que puede que aún no haya casos publicados; si no los hay, decirlo.
2. ~~**Precios de PPA en España**~~ — **cubierto en primera aproximación** por el bloque 0
   (38,97 €/MWh solar P25 en Q4 2024, duración modal 10 años). Falta **la fuente primaria
   citable**: el índice trimestral de LevelTen Energy y/o el *European PPA Market Outlook* de
   WindEurope, con el dato más reciente disponible en 2026 en lugar del de 2024.
3. **Coste unitario de BESS de larga duración** (€/kWh para sistemas de 8–12 h), que es la relación
   C/P que sale en el apartado 5.6 y **no** la de los BESS de 2–4 h de los que hay más datos.
4. **SEER de enfriadoras geotérmicas** frente a aire, con fuente de fabricante.
