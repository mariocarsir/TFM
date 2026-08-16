---
type: source
title: "Energía Solar Fotovoltaica (Perpiñán Lamigueiro, 2013)"
created: 2026-08-16
updated: 2026-08-16
status: active
tags:
  - source
  - fotovoltaica
  - bibliografia-tfm
  - radiacion-solar
  - almacenamiento
source_type: book
author: "Óscar Perpiñán Lamigueiro"
date_published: "2013-03"
url: "http://procomun.wordpress.com/documentos/libroesf"
source_id: src-9c7e1dd83466536bf360
sha256: "f028b3f2f74519de77a45c9e6ed92589be2982256326cc832bdd4b38e91959dd"
authority: primary
independence_key: perpinan-lamigueiro-esf-2013
review_state: active
related:
  - "[[Perpiñán_2013]]"
claim_ids:
  - clm-perpinan2013-beta-opt
  - clm-perpinan2013-llp-metodo
  - clm-perpinan2013-pr-rango
  - clm-perpinan2013-almacenamiento-plomo-acido
key_claims:
  - "β_opt = 3,7 + 0,69|φ| — inclinación óptima para sistemas estáticos (p.16)"
  - "Método LLP (Loss of Load Probability) como referencia metodológica de dimensionado de almacenamiento autónomo (p.104-108)"
  - "Performance Ratio anual típico 0,4-0,85, promedio europeo 0,74 (p.88)"
  - "El capítulo de almacenamiento (cap. 7) trata exclusivamente baterías de plomo-ácido, sin datos de ion-litio"
---

# Energía Solar Fotovoltaica (Perpiñán Lamigueiro, 2013)

Manual/libro docente de libre distribución (licencia CC BY-NC-SA 3.0 España, v.
1.5, marzo 2013, 192 pp.) que cubre geometría solar, radiación incidente,
física de la célula solar, sistemas conectados a red (SFCR), sistemas
autónomos (SFA) y de bombeo (SFB), y seguridad eléctrica. Es la referencia
citable de biblioteca del TFM con más peso metodológico para el dimensionado
del campo fotovoltaico y para el método de fiabilidad de almacenamiento
(LLP), aunque su capítulo de acumulación cubre solo química de plomo-ácido.

## Resumen citable

El resumen técnico exhaustivo ya generado por `bibliotecario-pdf` (skill
`resumen-tecnico`) — con ecuaciones, tablas y datos por página preservados —
vive en el vault como [[Perpiñán_2013]]
(`Bibliografia/Resumenes/Perpiñán_2013.md`). Es la única fuente que
`redactor-humanizador` debe citar de este libro, siguiendo la regla 10 de
`CLAUDE.md` (prohibido citar de memoria del modelo).

## Uso en el TFM

- Base física trazable (geometría solar, radiación en plano inclinado,
  célula solar, generador) para justificar hipótesis de cálculo del
  dimensionado FV.
- Método LLP (ecs. 7.8-7.18) como marco conceptual de fiabilidad para el
  dimensionado del almacenamiento del CPD, aunque el TFM usará baterías de
  ion-litio y un modelo horario en Excel en vez del método estadístico
  diario del libro.
- Valores orientativos de eficiencia de componentes (inversor, cableado,
  regulador, batería) citables cuando no haya datos de fabricante, siempre
  marcados como "valores orientativos" de esta fuente.
- Procedimientos de configuración eléctrica generador-inversor (módulos en
  serie/paralelo, ventana MPP) aplicables al dimensionado del campo FV.

## Advertencias de uso

1. La normativa española citada (RD 1578/2008, RD 1699/2011, RD 1565/2010,
   RD 436/2004, RD 1663/2000) está desactualizada — derogada/sustituida por
   el RD 244/2019 (regulación vigente de autoconsumo). No citar el
   contenido normativo de este libro como vigente.
2. El capítulo 7 (Sistemas Fotovoltaicos Autónomos) trata exclusivamente
   baterías de plomo-ácido. No contiene datos de baterías de ion-litio, la
   tecnología prevista para el almacenamiento del CPD del TFM.
3. No usar como fuente de cifras de mercado FV actuales (dato de
   2011-2012) ni de normativa vigente de conexión a red.

## Relacionado

- [[Perpiñán_2013]] — resumen técnico completo (fuente citable primaria)
