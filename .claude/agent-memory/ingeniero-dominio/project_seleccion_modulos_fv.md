---
name: project-seleccion-modulos-fv
description: "Propuesta 27/09/2026 (pendiente de validar): módulo INDEPENDIENTE por variante — V1a Onyx 35 %; V1b AIKO 475 monovidrio (reserva REC); V2 AIKO 475 vidrio-vidrio (reserva Trina bifacial, que gana por puntos); V3 LONGi Hi-MO 9 670 (reserva JA)"
metadata:
  type: project
---

Documento vigente: `Memoria/analisis/seleccion-modulos-por-variante.md` (27/09/2026). El de 22/09
(`comparacion-modulos-fv.md`, módulo opaco único AIKO para V1b/V2/V3) queda SUPERADO pero se
conserva por sus fichas. Script: `Memoria/analisis/scripts/modulos_por_variante.py`.

- **V1a:** Onyx c-Si 35 %, 330 uds ≈ 60,1 kWp. Sin cambios. Hallazgo lateral: DMEGC Greenhouse (43 % área transparente, 131,6 W/m², DIBt Z-70.3-309 no confirmado para ese modelo) — Mario decide si se abre.
- **V1b:** AIKO-A475-MAH54Mw, 794 uds ≈ 377,1 kWp, 24/string a 1100 V. Puntos 27,5 vs REC 26 vs LONGi 25. REC reserva (−4000 Pa, BROOF(t2), PAN probado). Poliurea/PU líquido condiciona la ESTRUCTURA (lastrada con almohadilla/geotextil, no adherida), no el módulo; K2 y Valk no declaran membranas líquidas.
- **V2:** AIKO-A475-MAH54Dw (2+2 mm, fuego IEC clase A), 1.597 uds ≈ 758,6 kWp. Trina NEG9RC.27 gana por puntos (27 vs 25,5) con criterios comerciales; pasa a elegido si la ganancia bifacial simulada > ~8 %. Vía de marquesina propuesta: perfiles-canalón estanca sin chapa.
- **V3:** LONGi LR8-66HYD-670M, 827 kWp/ha (GCR 0,40 +20 %), 27/string a 1500 V. Los tres (LONGi, JA, Trina) son AAA → bancabilidad no discrimina.

**Why:** Mario (27/09) separó la elección porque el argumento de 1500 V pensando en V3 no tenía sentido para una cubierta.
**How to apply:** no volver a proponer un módulo único; V1b y V2 comparten datos eléctricos → un mismo inversor de 1100 V. Tmín −10 °C provisional (AEMET pendiente; V3 con Colmenar Viejo). Relacionado: [[project-superficies-3d-variantes]].
