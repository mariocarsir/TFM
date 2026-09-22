---
name: project-superficies-3d-variantes
description: "Geometría CERRADA de V1a/V1b/V2 (19/09/2026): 578,91 m² horizontal / 2.756,88 m² ya neto de patios / 3.536 m² → 57,89 / 338,40 / 716,28 kWp y C_D 2,33 / 14,24 / 30,20 %. Sustituye a catastro y KMZ. El limitante de V1b ya no es la superficie, son las entradas DC del inversor"
metadata:
  type: project
---

Geometría cerrada el 19/09/2026 con las respuestas de Mario a las cuatro preguntas abiertas.
Documento completo: `Memoria/analisis/recalculo-superficies-3d-pvsyst.md` (revisión 2); script
reproducible: `Memoria/analisis/scripts/recalc_superficies_3d.py` (reutiliza `solar.py` + la carga
canónica de 8.760 h). **No rehacer este cálculo desde cero: correr el script.**

## Cifras de trabajo

| Variante | Superficie 3D | kWp | E_PV | kWh/kWp | A_PV | C_D (3.832) | C_D (3.467, geotermia) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1a BIPV lucernario | 578,9109 m², **horizontal** | **57,89** | 89,2 MWh | 1.540 | 100 % | **2,33 %** | 2,57 % |
| V1b cubierta | 2.756,8828 m² | **338,40** | 545,6 MWh | 1.612 | 100 % | **14,24 %** | 15,74 % |
| V1 total | — | **396,3** | 634,8 MWh | 1.602 | 100 % | **16,56 %** | 18,31 % |
| V2 marquesinas | 3.536 m² | **716,28** | 1.173,7 MWh | 1.639 | 98,6 % | **30,20 %** | 32,43 % |
| V1 + V2 | — | **1.112,6** | 1.808,5 MWh | 1.625 | **80,4 %** | **37,94 %** | 39,13 % |

Criterios: V1a = sup × 0,80 vidrio activo × 125 Wp/m² (VLT 20 %); V1b = sup × 0,70 × 0,82 ×
226,7 W/m² **sin restar patios** (ya están fuera); V2 = huella × 0,90 × 226,7. Strings de 12
módulos REC Alpha Pure-RX 470 Wp, redondeo a la baja.

## Las cuatro respuestas de Mario que cierran la geometría

1. **El lucernario es horizontal (0°), plano único.** Cae la hipótesis de ~35° que la revisión 1
   dedujo de 578,9109/472 = 1/cos(35,4°): era casualidad aritmética. Cae también la de 5° de
   catastro. Al ser horizontal, superficie desarrollada = proyección en planta.
2. **Ninguna superficie lleva márgenes descontados**: son la superficie máxima ideal. Los factores
   0,80 / 0,70 / 0,82 / 0,90 se aplican desde cero.
3. **Los patios ya están fuera de los 2.756,88 m²**: Mario midió polígonos de tejado por sección
   sobre la planta en H, no un rectángulo envolvente. Verificado en las capturas (los patios están
   modelados como huecos pasantes). **Nunca tomar los 2.756,88 m² como superficie neta de módulo**
   — daría 512 kWp, que es el error a evitar.
4. **Fuente de la geometría: catastro a escala 1:1 trazado a mano en el editor 3D de PVsyst.** No
   hay importación de CAD. Declararlo en la fase 1.4 de ERMA, junto con la desviación de +7,2 %
   frente a catastro (+23,6 % en el forjado).

## Tres hallazgos que cambian texto ya escrito

- **El limitante de V1b cambia de naturaleza: ya no es la superficie, son las entradas DC.** La
  superficie da 358,74 kWp = 63 strings, pero 63 entre 3 Huawei SUN2000-100KTL-M2 son 21 por
  inversor y el equipo tiene ~20 entradas (10 MPPT × 2). Se adopta **60 strings (3 × 20) = 720
  módulos = 338,40 kWp, ratio DC/AC 1,128** (el 1,13 del trabajo previo). El viejo problema del
  ratio 0,96 desaparece. **Pendiente de verificar el n.º de entradas con el datasheet de Huawei**:
  si admitiese más, V1b sube a 355,32 kWp y C_D 14,95 %.
- **V1a produce menos que antes, no más.** Al ser horizontal, GlobInc baja de 1.857,7 a
  1.785,6 kWh/m² (−3,9 %) y la productividad de 1.600 a 1.540 kWh/kWp: **es la superficie que peor
  rinde del proyecto**. Un argumento más para no justificar el BIPV por energía.
- **V1 + V2 vierte 354,6 MWh en 2.147 h y el A_PV cae al 80,4 %.** Es el primer escenario donde la
  batería tiene algo real que hacer sin llegar a la planta en suelo. V2 sola vierte 16,5 MWh en
  559 h (49,5 MWh en 957 h con geotermia): sigue sin justificar batería (+0,36 pp), pero **ya no
  se puede escribir que V2 nunca vierte**.

## Abierto a propósito

- **Reparto de strings de V2: 126 o 127.** Mario lo difirió expresamente («conforme avancemos en
  PVsyst veremos»). 127 → 716,28 kWp, 7 inversores con reparto no uniforme (127 es primo), ratio
  1,023, C_D 30,20 %. 126 (7 × 18) → 710,64 kWp, ratio 1,015, C_D 30,01 %. Diferencia: 0,19 pp.
  **No forzar la decisión.**
- **Errata a corregir antes de simular:** el proyecto `TFM_DataCenter.PRJ` tiene cargado
  `Carrasqueira_MN82.SIT` (Meteonorm 8.2, **Portugal**), heredado de una plantilla. Y la escena 3D
  está dibujada pero sin campos FV asignados (`PV Fields (0)`, `Active area 0.00 m²`).

**Cómo aplicar:** cualquier cifra de 47 / 290 / 680 kWp, de 472 / 1.562 / 3.332 m², o las
intermedias de la revisión 1 (57,9 / 304,56 / 362,5 kWp, C_D 2,42 / 12,81 / 15,23 %) está obsoleta.
`guia-diseno-pvsyst.md` (rev.2) y `estimacion-preliminar-variantes.md` (rev.3) ya están reescritos.
Ninguna conclusión estratégica se cae: V2 sigue siendo la mejor variante, V1a sigue siendo marginal
en energía y la barrera del 50,5 % sin almacenamiento sigue intacta.
