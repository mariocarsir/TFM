---
type: concept
title: "AUD-018 — El flujo de PVsyst sigue sin ejercitarse"
created: 2026-08-21
updated: 2026-08-21
status: developing
tags:
  - concept
  - tfm
  - auditoria
  - hallazgo
  - pendiente
domain: "Flujo de trabajo TFM"
complexity: intermediate
related:
  - "[[registro-auditorias]]"
  - "[[tfm-skill-auditor]]"
  - "[[tfm-subagente-piloto-pvsyst]]"
  - "[[aud-002-pipeline-sin-ejercitar]]"
  - "[[tfm-subagente-ingeniero-dominio]]"
---

# AUD-018 — El flujo de PVsyst sigue sin ejercitarse

| | |
| --- | --- |
| **Estado** | Pendiente — Se dejó para más adelante, a propósito. |
| **Fecha** | 2026-08-21 |
| **Eje** | Doctrina/realidad |
| **Severidad** | Bloqueante |
| **Commit** | sin commit |

## El problema que trataba de resolver

PVsyst es el núcleo técnico del TFM: de ahí salen las cifras de la simulación fotovoltaica. Pero nunca se ha usado. `Datos/PVsyst/` sigue sin informes y el subagente [[tfm-subagente-piloto-pvsyst]] no se ha invocado ni una vez.

## La decisión que se planteó

Ninguna acción inmediata. Queda anotado para reevaluarlo en cuanto exista la primera simulación.

## La decisión que se adoptó

Abierto como hallazgo propio el 21/08/2026, al cerrar la mitad bibliográfica de [[aud-002-pipeline-sin-ejercitar]].

## Detalle

**Por qué existe esta ficha.** Es la mitad superviviente de [[aud-002-pipeline-sin-ejercitar]]. Ese hallazgo agrupaba dos procesos sin probar: el bibliográfico y el de PVsyst. El primero se ejercitó cuatro veces con éxito, así que el hallazgo original se cerró — pero cerrarlo entero habría dado por buena la parte de PVsyst **sin haberla probado nunca**, que es exactamente el error que denunciaba. De ahí la separación.

**Por qué es bloqueante.** No porque haya nada roto, sino por lo que está en juego. Toda la memoria del TFM se apoya en los resultados de la simulación, y ese camino no se ha recorrido ni una vez. La experiencia del pipeline bibliográfico es el argumento más fuerte: cuando por fin se usó de verdad, aparecieron **seis hallazgos** que nadie había visto sobre el papel. No hay motivo para pensar que PVsyst será distinto.

**Qué lo cerrará.** La primera simulación real. En cuanto exista un informe en `Datos/PVsyst/`, este hallazgo se reevalúa: o se cierra como obsoleto, o destapa sus propios problemas — que es justamente para lo que sirve.

## Relacionado

- [[registro-auditorias]] — el registro completo de auditorías
- [[tfm-skill-auditor]] — la skill que produjo este hallazgo
