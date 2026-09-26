---
name: project-seleccion-modulos-fv
description: "Propuesta 22/09/2026 (pendiente de validar por Mario): V1a Onyx c-Si 35 % 182 Wp; V1b/V2/V3 AIKO Neostar 2P 475 W (reserva LONGi LR7-54HTH-465M). REC del M6 NO confirmado"
metadata:
  type: project
---

Comparativa 3+3 en `Memoria/analisis/comparacion-modulos-fv.md` (método Arcas 4.3 + diap. 15-17 ERMA).

- **V1a:** Onyx c-Si transparencia 35 %, 129,6 Wp/m² → 330 uds ≈ 60,1 kWp sobre 463,1 m². Polysolar PS-MC-ST (199 Wp/m², DIBt) gana por puntos pero solo publica 10 % de transparencia → no cumple la función del lucernario. PAN a crear a mano; pedir a Onyx Voc/Vmp con 3 cifras y g.
- **V1b/V2/V3:** AIKO 475 W (23,8 %, 1500 V) 19 pts, LONGi 17, REC 13. REC cae por 1000 V (malo para V3), 2 % LID año 1, menor eficiencia.
- ~377 kWp V1b (794 uds) y ~758 kWp V2 (1.597 uds), sin ajustar a strings.

**Why:** el módulo se elige antes que el inversor; Isc 14,35 A del AIKO invalida el reparto de strings del Huawei hecho con REC (8,6 A).
**How to apply:** si Mario valida, recalcular strings, excedentes de V2 y disposición 3D con 1757×1134 mm. Si prima bancabilidad en V3 → LONGi. Desviación frente al M6 que corrigió el tutor: decirlo en la memoria. Relacionado: [[project-superficies-3d-variantes]].
