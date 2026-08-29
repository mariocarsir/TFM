---
type: meta
title: Hot Cache
status: developing
created: 2026-08-05
updated: 2026-08-29
tags:
  - meta
  - hot-cache
---

# Recent Context

## Last Updated

2026-08-29 — save: sesión completa sobre las tres variantes de autoconsumo FV
del CPD (V1 cubierta, V2 marquesinas, V3 planta en suelo) tratadas como
alternativas excluyentes, y el marco normativo 2026 que las condiciona.
Nota creada: [[variantes-fv-normativa-autoconsumo-2026]].

## Key Recent Facts

- **V3 (planta en suelo) es normativamente factible**: la distancia se mide
  en proyección ortogonal en planta (línea recta entre equipos de medida), y
  el RDL 7/2026 amplió el supuesto de proximidad de 500 a 5.000 m para FV/eólica
  ≤ 5 MW (el umbral previo NUNCA fueron 2.000 m, eso fue un error corregido en
  la propia sesión). Con 2,93 km de la parcela candidata, sobra margen.
- **Solo V3 necesita permiso de acceso y conexión** (RD 1183/2020): V1 y V2
  son autoconsumo sin excedentes, exentas por el art. 7.1.b).i) del
  RD 244/2019. V3 es obligatoriamente con excedentes (art. 4.5.c) y por tanto
  sí necesita permiso (art. 7.1.b).iii). Es la asimetría que decide la
  barrera de entrada real de cada variante, no la superficie ni el coste.
- **La bateria es inútil en V1 y V2** (nunca hay excedente relevante que
  guardar: techo de C_D 14,2 % y 29,1 % respectivamente) y **decisiva en V3**
  (de 43,6 % sin batería a 90 % con 2,25 MWp + 5,7 MWh).
- **El vertido de la V3 es estacional y prácticamente irreducible**: incluso
  cuadruplicando la batería de 5,7 a 20 MWh, el vertido solo baja de 274 a
  163 MWh/año, porque se concentra en verano (72 % entre junio y septiembre),
  cuando la producción diaria supera con creces el consumo diario constante
  del CPD. Es almacenamiento estacional, fuera del alcance del TFM.
- **La energía autoconsumida de la V3 SÍ paga peaje** (familia de peajes TDA
  de la Circular 3/2020 de la CNMC, 6.1TDA en media tensión) aunque los
  arts. 17.1/18.1 del RD 244/2019 sugieran exención total — esa exención es
  solo de cargos, no de peajes, cuando hay transferencia a través de la red.
- **La batería de autoconsumo no entra en el régimen de acceso flexible**
  salvo que se le dé capacidad de cargar de la red (DT 5.ª RD 244/2019: en
  autoconsumo comparte medida y protecciones con la generación, no es
  instalación independiente). Decisión de diseño: cargar solo de la FV.
- **El acceso a la red se solicita para un nudo concreto elegido por el
  promotor** (RD 1183/2020 art. 10.1, por encima de 100 kW), no lo asigna el
  gestor. La SET candidata de conexión para la V3 es Tres Cantos 3570
  (220/66/20 kV), a 3,10 km de la parcela — la más próxima con nivel de MT.
  La distribuidora de la zona es i-DE (Iberdrola), no UFD.
- Los hooks SessionStart/Stop de claude-obsidian invocan el comando literal
  `python3`; en Windows nativo solo existe `python.exe` en el PATH. Fix: shim
  `python3.bat` en el directorio de la instalacion de Python.
- Toda mutación del vault en Windows nativo está bloqueada por diseño
  (`UNSUPPORTED_PLATFORM`); las transacciones se aplican vía WSL2/Ubuntu
  apuntando al script core en la ruta `/mnt/c/...` del lado Windows.
- El `source_id` del ledger NUNCA se inventa: es
  `stable_source_id(kind, locator, sha256)` de `claude_obsidian/ledgers.py`
  (paquete del plugin, no vive en este repo). `review_status` solo admite
  `unreviewed/active/superseded/rejected` (no existe un estado
  "no-citable" propio: la no-citabilidad de un TFM de referencia se impone
  con `authority: secondary`/`community` + notas en cada claim + aviso en el
  cuerpo de la página, nunca con un enum inventado). `risk` de un claim solo
  admite `normal/high`; `high` exige dos fuentes independientes para poder
  aceptarse, así que una única fuente no revisada por pares sigue siendo
  `normal`, con la reserva puesta en `notes`, no en `risk`.
- Los wikilinks del vault resuelven por el nombre de archivo (ASCII
  kebab-case, sin tildes), no por el `title` del frontmatter: aunque el
  título de una nota sea "Resúmenes", el archivo y el enlace correcto son
  `resumenes.md` / `[[resumenes]]`, siguiendo la convención ya usada en
  `wiki/concepts/` y `wiki/sources/`.

## Recent Changes

- Creada nota conceptual: [[variantes-fv-normativa-autoconsumo-2026]],
  resumiendo la sesión del 29/08/2026 sobre las tres variantes de autoconsumo
  del CPD tratadas como alternativas excluyentes y el marco normativo 2026
  (RDL 7/2026, RD 1183/2020, RD 244/2019, Circular 3/2020 de la CNMC), con
  seis correcciones normativas aplicadas durante la propia sesión.
- Creada nota conceptual: [[git-worktrees]].
- Registrada la primera fuente bibliográfica citable del TFM:
  [[perpinan-2013-energia-solar-fotovoltaica]] (Perpiñán Lamigueiro, 2013).
- Registradas dos fuentes de referencia NO citables (TFM de otros autores del
  Máster ERMA, usados solo como referencia de estructura/metodología, nunca
  citables en el TFM de Mario):
  [[arcas-2024-autoconsumo-industrial-san-martin-pyl]] (Manuel Arcas Navarro,
  2024, autoconsumo industrial San Martín PYL — concluye que el
  almacenamiento NO es rentable en ese caso) y
  [[fernandes-alves-2025-autoconsumo-mad9]] (Diego Fernandes Alves, 2025,
  autoconsumo sin excedentes Amazon MAD9 con almacenamiento en media
  tensión — aporta el método de degradación de batería por ciclos
  equivalentes más útil metodológicamente para el capítulo 7 de Mario).
- Creado el nodo temático [[resumenes]] que agrupa y relaciona las tres
  fuentes anteriores por temas compartidos (autoconsumo industrial,
  almacenamiento en baterías, PVsyst, análisis económico VAN/TIR/LCOE,
  Performance Ratio), con enlace bidireccional añadido en cada una de las
  tres páginas fuente.
- Registrada una tercera fuente de referencia NO citable:
  [[barrios-2023-evaluacion-fv-autoconsumo-gran-industria]] (Andrea Barrios
  López, 2023, evaluación FV para autoconsumo en gran industria — descarta
  el almacenamiento por baja energía excedentaria, complementario a la
  conclusión de San Martín PYL; aporta la metodología de tramitación
  administrativa y de dimensionado eléctrico más detallada de las tres
  fuentes de referencia). Actualizado [[resumenes]] para incorporarla a la
  comparativa (ahora con 4 filas: Perpiñán, Arcas, Fernandes Alves, Barrios).

## Active Threads

- **Excel `Bibliografia/Normativa/NormativaLinks.xlsx`** creado con 14 normas
  y columna de URL pendiente: Mario va a pasar los enlaces en una sesión
  nueva para completarlo.
- Localizar los valores vigentes del peaje 6.1TDA para 2026 (resolución
  anual de la CNMC) antes de meterlos en el capítulo económico.
- Consultar capacidad de acceso de generación en la SET Tres Cantos 3570
  (i-DE) antes de simular la V3 en PVsyst — riesgo crítico abierto.
- Decidir el trazado eléctrico de V2 (línea propia de 216 m vs. conexión a
  red) antes del capítulo económico.
- Empezar a redactar el capítulo 2 del TFM.
- Ingestar el resto de resúmenes de `Bibliografia/Resumenes/` y
  `conocimiento fotovoltaico/Referencia/` a medida que `bibliotecario-pdf`
  los vaya generando.
