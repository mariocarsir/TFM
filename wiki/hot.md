---
type: meta
title: Hot Cache
status: developing
created: 2026-08-05
updated: 2026-08-30
tags:
  - meta
  - hot-cache
---

# Recent Context

## Last Updated

2026-08-30 — corrección: la discrepancia sobre el umbral de 2.000 m del art.
3.g).iii) del RD 244/2019 estaba mal resuelta a favor del lado equivocado.
Verificado contra el articulado y corregidas las notas
[[variantes-fv-normativa-autoconsumo-2026]] y las memorias de proyecto
afectadas.

## Key Recent Facts

- **El art. 3.g).iii) del RD 244/2019 tiene dos párrafos con historiales
  distintos**: el primero (regla general, 500 m) nunca ha cambiado; el
  segundo (supuesto especial de FV en cubierta/suelo industrial/estructuras)
  sí ha subido de cifra varias veces — 500→1.000 m (RDL 18/2022)→**2.000 m**
  (RDL 20/2022)→**5.000 m** sin restricción de ubicación (RDL 7/2026, DF 14.ª
  apdo. Uno, en vigor 22/03/2026). La diapositiva `M6_T12` p. 14 del máster
  que citaba 2.000 m **era correcta para su fecha**; el error estaba en la
  sesión del 29/08 que la dio por equivocada.
- **La capa normativa de las diapositivas de M6 está congelada antes del
  22/03/2026**: no usarlas como fuente normativa; manda
  `Bibliografia/Fuentes/Normativa/NormativaLinks.xlsx`. Detalle completo del
  contraste (omisiones + desactualizaciones) en
  [[contraste-normativa-presentaciones]].
- **Los peajes de las diapositivas están caducados**: `T9` p. 5 usa la
  Resolución de 4/12/2024 y `T7_2` p. 16 la de 2021. La vigente es la
  Resolución de 18/12/2025 (BOE-A-2025-26348), aplicable desde el 01/01/2026.
- **V3 es normativamente factible**: distancia en proyección ortogonal y el
  RDL 7/2026 amplía a 5.000 m para FV ≤ 5 MW; la parcela está a 2,93 km.
- **Solo V3 necesita permiso de acceso y conexión**: V1 y V2 son sin
  excedentes (exentas, art. 7.1.b.i del RD 244/2019); V3 es obligatoriamente
  con excedentes (art. 4.5.c del RD 244/2019).
- **La batería es inútil en V1 y V2 y decisiva en V3** (de 43,6 % a 90 % de
  C_D con 2,25 MWp + 5,7 MWh). Su vertido es estacional e irreducible.
- **La energía autoconsumida de V3 sí paga peaje** (6.1TDA): la exención del
  RD 244/2019 es solo de cargos, no de peajes.
- Toda mutación del vault exige WSL2 (`UNSUPPORTED_PLATFORM` en Windows
  nativo); los wikilinks resuelven por nombre de archivo ASCII kebab-case.
- **Lección operativa**: al verificar un artículo con varios párrafos, cruzar
  el historial de modificación de CADA párrafo por separado — la estabilidad
  de uno no se puede generalizar al otro. Regla guardada en la memoria
  persistente del proyecto (`feedback_normativa_fuente_primaria`, fuera del
  vault de Obsidian).

## Recent Changes

- Corregidas [[variantes-fv-normativa-autoconsumo-2026]] y dos memorias de
  proyecto (`project_marco_regulatorio_2026`, `project_localizacion_cpd_parcela_v3`)
  y una de feedback (`feedback_normativa_fuente_primaria`): el umbral de
  2.000 m del segundo párrafo del art. 3.g).iii) sí existió (RDL 20/2022), no
  era un error a corregir.
- Creada [[contraste-normativa-presentaciones]]: dos comprobaciones
  (omisiones y desactualizaciones) sobre 15 normas y 52 PDFs.

## Active Threads

- Localizar los valores vigentes del peaje 6.1TDA 2026 antes del capítulo
  económico.
- Consultar capacidad de acceso en la SET Tres Cantos 3570 (i-DE) antes de
  simular la V3 en PVsyst.
- Decidir el trazado eléctrico de V2 (línea propia de 216 m vs. red).
- Empezar a redactar el capítulo 2 del TFM.
