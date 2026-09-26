---
name: bipv-encapsulante-pvb-eva
description: La regla «solo PVB vale en acristalamiento de cubierta» es alemana-austríaca, NO española; verificado que en España ni la normativa ni el IETcc penalizan el EVA
metadata:
  type: project
---

Para la variante V1a (BIPV en el tragaluz del CPD) se creyó que el riesgo de proyecto
era el **encapsulante del laminado**. Verificado a fondo: **en España no lo es.**

**Lo que sigue siendo cierto:**

- El cristalino de Onyx Solar (el único que da los ~47 kWp buscados sobre 378 m²,
  a 129,6 Wp/m² con transparencia 35 %) se lamina con **EVA 1,80 mm**.
- La capa fina a-Si de Onyx ofrece opción **PVB 1,52 mm** — y los dos lucernarios
  realmente ejecutados documentados (Bell Works, Alcalá 33) usan PVB.
- En la práctica constructiva **alemana-austríaca**, para *Überkopfverglasung* solo
  el laminado con PVB tiene aprobación de base (*abZ*); el EVA requiere
  *Einzelgenehmigung*.

**Lo que se ha corregido (búsqueda normativa española, sección 9 del informe
`Memoria/analisis/bipv-tragaluz-fichas-tecnicas.md`):**

- **NO existe norma, ley ni documento español que exija PVB frente a EVA** en
  acristalamiento FV horizontal o inclinado sobre zona ocupada.
- **ISO/TS 18178:2018** (la norma internacional específica de vidrio FV laminado)
  admite PVB y EVA *en la misma frase, en pie de igualdad*.
- **DITEX 692EX/24 del IETcc-CSIC** (12/09/2024): España evaluó favorablemente un
  módulo FV acristalado **con EVA** para cerramiento de **cubiertas y marquesinas**,
  clasificado en el área «cubiertas, lucernarios y claraboyas». Contraevidencia
  directa. Cautela: es DITEX (prototipo experimental), no DIT pleno, y su PDF no
  está publicado.
- La cadena española (UNE-EN 12488 montaje, UNE-EN ISO 12543 y UNE-EN 14449
  producto) es de **prestación y conformidad**, no prescribe intercalario.

**Why:** el encargo original y el propio informe daban por trasladable a España el
criterio alemán. Escribirlo así en el TFM sería una afirmación normativa falsa.

**How to apply:** el PVB puede defenderse como **buena práctica europea**, nunca como
exigencia española, y siempre declarando la limitación. La pregunta a Onyx sobre
cristalino con PVB sigue mereciendo hacerse por prestación, pero **ya no es la
pregunta que desbloquea V1a**: la rama cristalino+EVA (~49 kWp) es viable en España.
Ver [[cte-lucernario-db-sua-matiz]] y [[normativa-vidrio-cubierta-espana]].
