---
type: concept
title: "Subagente: ingeniero-dominio"
created: 2026-08-13
updated: 2026-08-13
status: developing
tags:
  - concept
  - tfm
  - subagent
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-subagentes]]"
  - "[[tfm-subagente-piloto-pvsyst]]"
  - "[[tfm-subagente-analista-economico]]"
  - "[[tfm-subagente-redactor-humanizador]]"
---

# ingeniero-dominio

Modelo: opus. Definido en `.claude/agents/ingeniero-dominio.md`.

Es el núcleo técnico del TFM: apoyo para una instalación fotovoltaica con almacenamiento para autoconsumo en un CPD (carga crítica 24/7, con SAIs y restricciones de redundancia). Es el único agente configurado con el modelo más capaz (opus), reflejando que es el centro de gravedad técnico del trabajo.

## Ámbitos que cubre

- Dimensionado del generador FV: módulos, inversores, strings, ratio DC/AC, sombras, orientación/inclinación, restricciones estructurales.
- Simulación PVsyst: diagrama de pérdidas, Performance Ratio, producción P50/P90, elección de base meteorológica.
- Almacenamiento: tecnología de baterías, dimensionado ligado al consumo crítico, estrategia de carga/descarga por periodos tarifarios, degradación.
- Autoconsumo y autosuficiencia: grado con y sin batería, comparativa de escenarios.
- Tramitación: modalidad de autoconsumo, procedimiento de legalización, plazos orientativos.

## Cuándo se delega

Para cualquier cálculo o decisión de ingeniería de los capítulos 6 y 7 de la memoria.

## Reglas clave

- La criticidad del CPD (carga 24/7, redundancia, SAIs) es el elemento diferencial de este TFM frente a los de referencia (Manuel Arcas, Andrea Barrios); condiciona el dimensionado de baterías y no se trata como detalle menor.
- Cualquier cifra de producción, pérdidas o dimensionado debe venir del informe PVsyst real de Mario, no de valores típicos de la industria salvo hipótesis explícita a validar.
- Contrasta cualquier decisión contra los dos TFM de referencia (`Documentacion de apoyo/Ejemplos TFM/`) cuando exista precedente.

## Relación con otros agentes

Comparte el capítulo 7 (estrategia de carga/descarga) con [[tfm-subagente-analista-economico]]: este agente decide la estrategia técnica, el analista económico la modela hora a hora en Excel. Ambos alimentan de cifras canónicas a [[tfm-subagente-redactor-humanizador]].

Se apoya en [[tfm-subagente-piloto-pvsyst]] para todo lo operativo del software (dónde clickar, cómo leer una pantalla o un resultado) — este agente aporta el criterio de ingeniería (qué valor usar y por qué), no el manejo de la interfaz.
