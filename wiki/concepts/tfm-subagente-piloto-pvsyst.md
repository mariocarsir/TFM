---
type: concept
title: "Subagente: piloto-pvsyst"
created: 2026-08-15
updated: 2026-08-15
status: developing
tags:
  - concept
  - tfm
  - subagent
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[tfm-subagentes]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
---

# piloto-pvsyst

Modelo: opus. Definido en `.claude/agents/piloto-pvsyst.md`.

Sabe manejar la interfaz de PVsyst (versión 8.1.5, con conocimiento de la evolución desde v6) y leer sus resultados. No decide ingeniería: esa parte sigue siendo de [[tfm-subagente-ingeniero-dominio]].

## Ámbitos que cubre

- Navegación de la interfaz: en qué pestaña/menú/botón está cada acción, en qué orden se rellenan los pasos de un proyecto.
- Lectura de capturas de pantalla guardadas en `conocimiento fotovoltaico/Capturas/` (formato `AAAA-MM-DD_HHMM.png`) — siempre responde sobre la de timestamp más reciente, nunca asume cuál es sin comprobar la fecha del nombre.
- Validación de resultados de simulación: si un Performance Ratio, gráfica de pérdidas o aviso de PVsyst tiene sentido, y por qué.
- Guía por pasos del diseño completo: genera `conocimiento fotovoltaico/Referencia/guia-diseno-pvsyst.md`, con cada paso justificado para que Mario la audite y la vaya tachando.

## Cuándo se delega

Cualquier duda de **cómo** usar PVsyst (dónde clickar, qué significa una pantalla o un resultado). Nunca para decidir **qué** valor de ingeniería usar — eso es [[tfm-subagente-ingeniero-dominio]].

## Fuente de verdad

`conocimiento fotovoltaico/Manuales PVsyst/` (14 manuales oficiales v6/v7/v8) primero, `conocimiento fotovoltaico/Referencia/` después. Si una duda de interfaz no está cubierta por ningún manual, lo dice explícitamente en vez de responder de memoria del modelo sobre el software.

## Relación con otros agentes

Cuando una pregunta mezcla "cómo lo configuro" con "qué valor debería poner", lo señala en vez de decidir el valor — el hilo principal consulta entonces a [[tfm-subagente-ingeniero-dominio]] para la parte de criterio de ingeniería. Los subagentes no se invocan directamente entre sí.
