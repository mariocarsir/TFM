---
type: source
title: "Proyecto de autoconsumo industrial con almacenamiento en la fábrica de San Martín PYL (Manuel Arcas Navarro, TFM ERMA UPM, 2024)"
created: 2026-08-16
updated: 2026-08-16
status: active
tags:
  - source
  - fotovoltaica
  - autoconsumo
  - almacenamiento
  - tfm-referencia
  - no-citable
source_type: thesis
author: "Manuel Arcas Navarro"
date_published: "2024"
url: null
source_id: src-172f6b5c8b5ffc6b4914
sha256: "312e92d83f4ceaa79d956ee5a65a05afed99a52b3f99815ea3380d75773ad8c2"
authority: secondary
independence_key: arcas-navarro-sanmartinpyl-tfm-2024
review_state: active
citable: false
related:
  - "[[autoconsumo-industrial-san-martin-pyl]]"
claim_ids:
  - clm-arcas2024-potencia-elegida
  - clm-arcas2024-almacenamiento-no-rentable
  - clm-arcas2024-resultados-financieros
  - clm-arcas2024-ahorro-anual
key_claims:
  - "Sistema elegido: tejado con 2 orientaciones, 1.626 kWp, PR 0,784, autoconsumo 96,60%, autosuficiencia 15,05% (p.22-37)"
  - "El almacenamiento en batería NO resulta rentable en ninguna estrategia estudiada, por bajo diferencial tarifario P1-P6 (~38%) y alto coste de batería (120 €/kWh) (p.38-45)"
  - "Resultados financieros (solo FV, sin batería): payback 6 años, TIR 18%, VAN 1.872.921 €, LCOE 0,023 €/kWh (p.47)"
  - "Ahorro anual medio conseguido: 268.695,16 €/año, equivalente a 13,4% de reducción de la factura eléctrica en 25 años (p.47-48)"
---

# Proyecto de autoconsumo industrial con almacenamiento en la fábrica de San Martín PYL (Manuel Arcas Navarro, 2024)

> **⚠️ NOTA DE NO-CITABILIDAD:** este documento es un TFM de otro autor (Manuel Arcas Navarro, Máster ERMA, curso 2023/2024, UPM). **No es fuente académica citable** en el TFM de Mario Carrión Sirvent. Sirve exclusivamente como referencia de estructura, metodología de cálculo y nivel de detalle esperado por el tribunal ERMA, por ser el trabajo más cercano en temática (autoconsumo fotovoltaico industrial con almacenamiento en baterías). `redactor-humanizador` NO debe citar esta página ni el resumen asociado como fuente de ninguna cifra o afirmación del documento final.

## Resumen

El TFM evalúa la viabilidad técnico-económica de un sistema de autoconsumo fotovoltaico, con y sin almacenamiento en baterías, en la fábrica de placa de yeso laminado (PYL) de PLACO (Saint-Gobain) en San Martín de la Vega (Madrid). Compara tres configuraciones simuladas en PVsyst y selecciona tejado con 2 orientaciones (1.626 kWp). Un modelo horario en Excel concluye que el almacenamiento en batería **no es rentable** en las condiciones estudiadas. El análisis económico final (solo FV, sin batería, financiación 100% propia) arroja payback de 6 años, TIR del 18%, VAN de 1.872.921 € y un ahorro del 13,4% sobre la factura eléctrica a 25 años.

El resumen técnico exhaustivo ya generado por `bibliotecario-pdf` (skill `resumen-tecnico`) — con ecuaciones, tablas y datos por página preservados, incluyendo su propia nota de no-citabilidad — vive en [[autoconsumo-industrial-san-martin-pyl]] (`conocimiento fotovoltaico/Referencia/autoconsumo-industrial-san-martin-pyl.md`).

## Uso permitido en el TFM de Mario

- Referencia de **estructura** del documento (índice, extensión, secuencia de capítulos) y de **metodología de cálculo** (cargas de viento CTE, dimensionado de cableado DC, sobredimensionamiento DC/AC, separación de filas por sombreado, estructura del modelo horario Excel de batería, estructura de LCOE combinado red+FV).
- Contraste metodológico para el capítulo de almacenamiento del CPD: es el caso más cercano con perfil de consumo 24/7 "plano" ya estudiado, y su conclusión de no-rentabilidad de la batería es un punto de partida útil a **recalcular con los datos propios del CPD** (otro perfil tarifario, otro ratio FV/consumo), no a asumir por extrapolación.

## Advertencias de uso

1. **No citable como fuente académica.** Ninguna cifra de este documento debe aparecer en la memoria del TFM de Mario atribuida a esta fuente; solo como inspiración de metodología, nunca como dato.
2. Cifras de mercado (precios de componentes, tarifas eléctricas 2023, coste de batería 120 €/kWh) están desactualizadas para el TFM de Mario (año de referencia distinto) — no reutilizar sin verificar contra fuente propia o `investigador-cientifico`.
3. El propio documento original contiene inconsistencias numéricas internas menores (consumo anual, potencia instalada, producción FV según distintas tablas) ya señaladas en el resumen — no reconciliadas, reportadas tal cual.

## Relacionado

- [[autoconsumo-industrial-san-martin-pyl]] — resumen técnico completo (no-citable, referencia de metodología)
