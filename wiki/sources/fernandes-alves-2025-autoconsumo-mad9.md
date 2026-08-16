---
type: source
title: "Instalación fotovoltaica para autoconsumo en centro logístico de almacenaje (Amazon MAD9) (Fernandes Alves, 2025)"
created: 2026-08-16
updated: 2026-08-16
status: active
tags:
  - source
  - fotovoltaica
  - autoconsumo
  - almacenamiento
  - baterias
  - PVsyst
  - industrial
  - tfm-referencia
  - no-citable
  - analisis-economico
  - LCOE
  - VAN
  - TIR
  - media-tension
source_type: thesis
author: "Diego Fernandes Alves (tutor: Julio Amador Guerra)"
date_published: "2025"
url: null
source_id: src-124b39acc88046c98ba7
sha256: "2f885181c5eba6b522323de9f69d07661419ec3f9d7fbfabe4e4abe22815a841"
authority: community
independence_key: fernandes-alves-mad9-tfm-2025
review_state: active
citable: false
related:
  - "[[instalacion-fotovoltaica-centro-logistico-mad9]]"
claim_ids:
  - clm-mad9-potencia-config
  - clm-mad9-bateria-seleccion
  - clm-mad9-resultado-economico
  - clm-mad9-resultado-energetico
key_claims:
  - "Potencia final 2.710 kWp (4.928 módulos JA Solar 550 Wp), 8 inversores Huawei SUN2000-330KTL-H1 (p.51-52)"
  - "Batería seleccionada: 2.000 kWh Huawei LUNA2000, por equilibrio rentabilidad/durabilidad frente a 200 y 4.500 kWh (p.46-51)"
  - "Resultado económico final: CAPEX 2.372.000 €, VAN 4.481.881,96 €, TIR 15,76 %, LCOE 0,0393 €/kWh, payback 5,75 años (p.74-76, p.82)"
  - "Resultado energético final: 4.150,8 MWh/año, autoconsumo 87,5 %, autosuficiencia 77 %, PR 70,61 % (p.68-70)"
---

# Instalación fotovoltaica para autoconsumo en centro logístico de almacenaje (Amazon MAD9) (Fernandes Alves, 2025)

> **⚠️ NOTA DE NO-CITABILIDAD:** este documento es un TFM de otro autor (Diego Fernandes Alves, Máster ERMA, curso 2024/2025, UPM), tutorizado por el mismo tutor que Mario Carrión (Julio Amador Guerra). **No es fuente académica citable** en el TFM de Mario. Sirve únicamente como referencia de estructura, metodología, criterios de dimensionado de almacenamiento y formato esperado por el tribunal ERMA — por ser el trabajo más cercano en temática y tutor disponible entre los TFM de referencia (autoconsumo fotovoltaico industrial de gran escala con almacenamiento en baterías, sin excedentes, en media tensión).

TFM de autoconsumo fotovoltaico sin excedentes para el centro logístico Amazon MAD9 (Alcalá de Henares, Madrid): 2,71 MWp (4.928 módulos JA Solar 550 Wp), 8 inversores Huawei SUN2000-330KTL-H1, almacenamiento de 2.000 kWh (Huawei LUNA2000), conexión en MT (20 kV). Compara 24 configuraciones simuladas en PVsyst v8.0.13 (módulos/inversores × 3 capacidades de batería) y selecciona la batería de 2.000 kWh por criterio técnico-económico, incluyendo un método propio de estimación de degradación de baterías por ciclos equivalentes.

## Resumen de referencia (no citable)

El resumen técnico exhaustivo ya generado por `bibliotecario-pdf` (skill `resumen-tecnico`) — con ecuaciones, tablas y datos por página preservados — vive en el vault como [[instalacion-fotovoltaica-centro-logistico-mad9]] (`conocimiento fotovoltaico/Referencia/instalacion-fotovoltaica-centro-logistico-mad9.md`). El propio resumen incluye su propia nota de no-citabilidad en el cuerpo. **Ningún agente debe citar este documento como fuente académica** — ni el resumen ni esta página — al redactar el TFM de Mario (regla 10 de `CLAUDE.md`).

## Uso en el TFM (solo como referencia de metodología/formato)

- Cap. 3 (emplazamiento y consumo): metodología de comparación de bases de datos meteorológicas (Meteonorm/NASA/PVGIS) replicable.
- Cap. 4 (tipología de autoconsumo y tramitación): ejemplo de codificación CNMC 31-A y esquema de medida tipo A para instalación sin excedentes en MT.
- Cap. 6 (diseño e ingeniería FV): metodología de comparación de variantes módulos/inversores × capacidad de batería; diagrama de pérdidas PVsyst con desglose por almacenamiento AC-coupling.
- Cap. 7 (almacenamiento — núcleo del TFM de Mario): **aportación más valiosa**. Método propio de degradación de baterías por ciclos equivalentes (ecuación $Ciclos_t = Ciclos_{t-1}\cdot(1+\delta)^{t-1}$) y criterio de selección de capacidad basado en durabilidad, no solo rentabilidad estática.
- Cap. 8 (análisis económico): estructura de presupuesto y ecuaciones de VAN/TIR/LCOE, validación cruzada preliminar vs. detallado.

## Advertencias de uso

1. **No citar en ningún momento como fuente académica.** Es un TFM de otro estudiante, no revisado por pares, no publicado. Solo válido como referencia interna de metodología, estructura y orden de magnitud de resultados.
2. Discrepancia sin resolver en la fuente: el ratio DC/AC se cita como 1,13 (diseño de strings, apdo. 3.3.2) y como ≈1,03 (potencia prevista, apdo. 3.4). No usar ninguno de los dos valores sin verificar directamente en el PDF original.
3. No se localizó en el texto extraído la ficha técnica completa (Voc, Isc, coeficientes de temperatura) del módulo JA Solar JAM72D30-550-MB.
4. Anexo I (planos EPLAN) y Anexo IV (cálculos Caneco BT) verificados como existentes pero no extraídos en detalle numérico (salida de software repetitiva por circuito).

## Relacionado

- [[instalacion-fotovoltaica-centro-logistico-mad9]] — resumen técnico completo (no citable, solo referencia interna)
