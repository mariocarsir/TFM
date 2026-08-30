---
type: concept
title: "Contraste con normativa expuesta en presentaciones"
created: 2026-08-30
updated: 2026-08-30
status: developing
tags:
  - concept
  - normativa
  - autoconsumo
  - presentaciones
  - erma
  - rdl-7-2026
  - peajes
domain: "Normativa / TFM"
complexity: advanced
related:
  - "[[variantes-fv-normativa-autoconsumo-2026]]"
---

# Contraste con normativa expuesta en presentaciones

> **Encargo (30/08/2026).** Mario pidió cruzar la normativa registrada en
> `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx` contra la citada en las diapositivas del
> máster, en dos direcciones: normativa del Excel omitida en las diapositivas, y normativa de las
> diapositivas desactualizada respecto al Excel. Criterio impuesto: **el Excel es siempre la versión
> más actualizada y la referencia autorizada.**

He cruzado las **15 normativas del Excel** contra **52 PDFs** de presentaciones (las 14 de M6 al completo + el resto de módulos), con verificación del texto literal de cada diapositiva crítica. Resultado:

---

## Comprobación 1 — Normativa del Excel ausente en las diapositivas

**Presentes y correctamente citadas (8/15):** Ley 24/2013 · RDL 15/2018 · RD 244/2019 · RD 1183/2020 · RD 148/2021 · RD 1699/2011 · Circular 3/2020 CNMC · (RD 900/2015 como antecedente).

**Omitidas (7/15)**, separando lo imputable de lo cronológico:

| Norma | Estado | Comentario |
|---|---|---|
| **RDL 7/2026** | Ausente en M6 | **Sí aparece en `M15_T10_Regulacion.pdf` (pp. 11, 13, 16, 17)**, pero solo en su vertiente de hitos/hibridación/almacenamiento. Ninguna diapositiva de M6 lo cita. |
| **Resolución CNMC peajes 18/12/2025** | **Omisión real** | Existía al hacerse las diapositivas (BOE 22/12/2025) y no se recogió. |
| **Circular 1/2024 CNMC** (acceso de demanda) | **Omisión real** | En vigor desde 12/01/2025. No aparece en ninguna presentación del máster. |
| **Reglamento Delegado (UE) 2024/1364** (centros de datos) | **Omisión real** | No aparece en ningún módulo. Es la norma europea de evaluación de CPD — directamente tu objeto de estudio. |
| **Directiva (UE) 2023/1791** (eficiencia energética) | **Omisión real** | No aparece en ningún módulo. |
| **Reglamento (UE) 2024/1747** | Ausente en M6 | Sí está en `M1_T11_PPA.pdf` (pp. 9-10). |
| **Proyecto de RD de CPD + su MAIN** | Omisión cronológica | Publicados el 27/08/2026, posteriores a las clases. No imputable. |

---

## Comprobación 2 — Normativa citada que está desactualizada

**1. [CRÍTICO] Los 5 km aparecen como norma *no aprobada*.** `M6_T7_RegulacionTramitacion1.pdf` pp. 38-40, bajo el título literal **«Normativa pendiente de aprobación: Ampliación del radio y nueva modalidad»**, dice: *«Se aumenta el radio de distancia máxima de los consumidores a 5 km… De generación fotovoltaica, con P ≤ 5 MWn, ubicadas en cubierta, suelo industrial o estructuras artificiales…»*. Eso es exactamente la **DF 14.ª apdo. Uno del RDL 7/2026**, que según el Excel está **en vigor desde el 22/03/2026**. El contenido es correcto; el **estatus jurídico que le atribuye la diapositiva es falso a día de hoy**. Es justo el punto del que depende tu variante 3.

**2. [CRÍTICO] La regla de distancia vigente se presenta como 500 / 2.000 m.** `T7_1` p. 5 (*«en BT a distancia ≤ 500 m, (ii bis) FV en cubierta, suelo industrial o estructura a distancia ≤ 2.000 m»*, anotado «Ampliado por RDL 20/2022») y la nota al pie de `T12` p. 14 (*«hasta los 2.000 metros (anteriormente 1.000 m desde el RDL 18/2022, que amplió los 500 m originales)»*). Superado por el RDL 7/2026. Si citas estas diapositivas, la V3 a 2,93 km sale ilegal por un factor de casi seis.

**3. [ALTA] Peajes de acceso, un ejercicio (o cinco años) por detrás.** `T9_BateriasAutoconsumo` p. 5 cita la *Resolución de 6 de marzo de 2025* que modifica la *Resolución de 4 de diciembre de 2024* (valores 2025); `T7_2` p. 16 cita una *«Resolución de 18/03»* (la de 2021). La autorizada por el Excel es la **Resolución de 18 de diciembre de 2025 (BOE-A-2025-26348)**, con valores aplicables desde el 01/01/2026. Esto afecta directamente al 6.1TDA de tu modelo económico.

**4. [MEDIA] Circular 3/2020 citada sin su modificación viva.** `T7_2` pp. 7 y 16, `T12` p. 13 y `T9` p. 5 la citan «a secas». El Excel registra que la **Circular 1/2025 (BOE-A-2025-2044)** modificó los arts. 7.4, 8, 11, la DA 2.ª y el anexo I, y desde el 01/04/2025 el art. 9 más los nuevos art. 15 y DT 4.ª/5.ª. El valor Pg = 0 sigue siendo válido (art. 2), pero hay que citar el consolidado.

**5. [MEDIA] La Ley 9/2025 como fuente del art. 4.5 del RD 244/2019.** `T7_1` pp. 4 y 35 atribuyen a la Ley 9/2025 la combinación «individual sin excedentes + a través de red con excedentes». El Excel documenta que ese art. 4.5 fue **reescrito después por el RDL 7/2026 (DF 14.ª apdo. Dos)**: el fondo sobrevive, pero la fuente vigente es otra. Además la diapositiva **omite la letra c)**, que obliga a que el autoconsumo a través de la red sea *siempre* con excedentes — precisamente la duda que planteabas en `Prompt_VariantesAutoconsumoNormativa.md`.

**6. [MEDIA] RD 1699/2011 como fuente de las condiciones de acceso y conexión.** `T7_1` p. 9 remite a *«Título II. RD 1699/2011»*. El Excel registra que su **art. 5, «Determinación de las condiciones técnicas de acceso y la conexión», está íntegramente derogado** por la DD única.b) del RD 1183/2020, con efecto 31/12/2020. (En cambio, las citas de `T11` pp. 19/27 y `T4` pp. 50-51 al RD 1699/2011 para protecciones y definición de potencia siguen siendo válidas — ahí no hay problema.)

**7. [BAJA] «RD 900/2015. Derogado por el RD 244/2019»** (`T7_1` p. 3). Formalmente correcto, pero omite que el RDL 15/2018 ya lo había vaciado antes (arts. 7.1, 7.2, 5, 8.1, 18, 23, 25…). Imprecisión, no error.

**8. [Limpio] Ninguna presentación cita el RDL 7/2025**, el que decayó al no convalidarse y que el Excel marca como «no citar nunca». Verificado con búsqueda precisa en los 52 PDFs.

---

**Conclusión operativa:** el material de M6 es fiable en método pero su capa regulatoria quedó congelada **antes del 22/03/2026**. Los dos puntos que te pueden hacer daño de verdad son el nº 1-2 (te llevarían a descartar la V3 por distancia) y el nº 3 (peajes de 2025 en el modelo económico). El Excel gana en los ocho casos.

## Relacionado

- [[variantes-fv-normativa-autoconsumo-2026]] — marco normativo 2026 de las tres variantes, donde ya se fijó el criterio de los 5.000 m del RDL 7/2026.
