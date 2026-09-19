---
name: project-superficies-3d-variantes
description: "Superficies canónicas de V1a/V1b/V2 medidas por Mario sobre el 3D de PVsyst (19/09/2026): 578,91 / 2.756,88 / 3.536 m² → 57,9 / 304,6 / 716,3 kWp. Sustituyen a las de catastro/KMZ. Dos ambigüedades abiertas: patios de V1b y pendiente del lucernario"
metadata:
  type: project
---

Recálculo hecho el 19/09/2026. Documento completo:
`Memoria/analisis/recalculo-superficies-3d-pvsyst.md`; script reproducible:
`Memoria/analisis/scripts/recalc_superficies_3d.py` (reutiliza `solar.py` + la carga canónica de
8.760 h). **No rehacer este cálculo desde cero: correr el script.**

## Cifras de trabajo (lectura conservadora A)

| Variante | Superficie 3D | kWp | E_PV | A_PV | C_D (3.832) | C_D (3.467, geotermia) |
| --- | --- | --- | --- | --- | --- | --- |
| V1a BIPV lucernario | 578,9109 m² | **57,9** | 92,6 MWh | 100 % | **2,42 %** | 2,67 % |
| V1b cubierta | 2.756,8828 m² brutos | **304,56** | 491,0 MWh | 100 % | **12,81 %** | 14,16 % |
| V1 total | — | **362,5** | 583,7 MWh | 100 % | **15,23 %** | 16,83 % |
| V2 marquesinas | 3.536 m² | **716,28** | 1.173,7 MWh | 98,6 % | **30,20 %** | 32,43 % |
| V1 + V2 | — | 1.078,7 | 1.757,4 MWh | 81,9 % | **37,56 %** | 38,81 % |

Criterios aplicados (sin cambios respecto a la guía): V1a = sup × 0,80 vidrio activo × 125 Wp/m²
(VLT 20 %); V1b = (sup − 408 patios) × 0,70 × 0,82 × 226,7 W/m²; V2 = huella × 0,90 × 226,7.
Strings de 12 módulos REC Alpha Pure-RX 470 Wp, redondeo a la baja.

## Las dos ambigüedades que hay que cerrar con Mario

1. **¿Los 2.756,88 m² de V1b descuentan los dos patios interiores (408 m²)?** Si NO (lectura A,
   la adoptada): 304,56 kWp. Si SÍ (lectura B): 355,32 kWp y C_D 14,95 %. Se eligió A porque el
   forjado implícito (2.348,9 m²) queda a +5,3 % de catastro, coherente con el sesgo global del
   modelo 3D (+7,2 %); la lectura B exigiría +23,6 %, inexplicable. **Nunca tomar los 2.756,88 m²
   como superficie neta de módulo** — daría 512,5 kWp, que es el error a evitar.
2. **Pendiente y geometría del lucernario.** 578,91 / 472 = 1,2265 = 1/cos(35,4°). O el lucernario
   tiene ~35° y no los 5° supuestos, o el polígono incluye perfilería. Horquilla de producción de
   V1a: **−15,2 % (a dos aguas con faldón norte) a +10,5 % (plano único 35°/−30°)**.

## Dos hallazgos laterales que cambian texto ya escrito

- **El ratio DC/AC de V1b deja de ser un problema.** Con 304,56 kWp son 54 strings entre 3 Huawei
  SUN2000-100KTL-M2 = 18 exactos por inversor, ratio **1,015** (antes 0,96 con 287,6 kWp). Cierra
  el punto abierto n.º 3 de `guia-diseno-pvsyst.md`.
- **V2 ya no es «excedente testimonial».** Pico 529 kW contra 437 kW de carga: 16,5 MWh vertidos
  en 559 h sin geotermia, **49,5 MWh en 957 h con geotermia (4,2 % de la producción)**. Sigue sin
  justificar batería (+0,36 / +1,21 pp de techo; bastarían 0,16–0,38 MWh para vertido cero), pero
  **ya no se puede escribir que V2 nunca vierte**: el antivertido recorta producción real y eso hay
  que declararlo en el capítulo de resultados.

**Cómo aplicar:** cualquier cifra de 47 / 290 / 680 kWp o de 472 / 1.562 / 3.332 m² está obsoleta.
Avisos de vigencia ya añadidos al principio de `estimacion-preliminar-variantes.md` y en la sección
0bis de `guia-diseno-pvsyst.md`; los cuerpos de ambos documentos aún contienen las cifras viejas y
hay que rehacerlos cuando se cierre la ambigüedad n.º 1. Ninguna conclusión estratégica se cae: V2
sigue siendo la mejor variante, V1a sigue siendo marginal en energía (justificación arquitectónica,
no energética) y la barrera del 50,5 % sin almacenamiento sigue intacta.
