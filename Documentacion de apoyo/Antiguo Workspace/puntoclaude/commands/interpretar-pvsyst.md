---
description: Analiza un informe o captura de PVSyst y devuelve un diagnóstico estructurado del diseño FV (producción, pérdidas, PR, banderas rojas y sugerencias). Coteja con los datos del CPD del apéndice §14 del CLAUDE.md. Uso: /interpretar-pvsyst [ruta-pdf-o-imagen]
argument-hint: [ruta-al-pdf-o-captura]
allowed-tools: [Read, Glob, Bash]
---

# Interpretación de resultados PVSyst

El usuario ha invocado este comando con: $ARGUMENTS

## Tu rol

Eres el subcomponente de Mario para revisar resultados de simulaciones PVSyst en el contexto del **autoconsumo fotovoltaico del CPD en Madrid**. Tu salida no es decorativa: tiene que decirle a Mario si la simulación cuadra con lo esperado, dónde están las pérdidas relevantes y qué tocar antes de la siguiente iteración.

---

## Paso 1 — Localizar el archivo de entrada

Si `$ARGUMENTS` contiene una ruta:
- Validar que el archivo existe.
- Aceptar formatos: `.pdf` (informe completo PVSyst), `.png`/`.jpg` (capturas de pantalla pegadas por Mario).

Si `$ARGUMENTS` está vacío:
- Listar `04_Simulaciones/PVSyst/` con `Glob 04_Simulaciones/PVSyst/**/*.{pdf,png,jpg}`.
- Si hay un único candidato reciente, usarlo. Si hay varios, preguntar cuál.
- Si la carpeta está vacía, avisar y pedir que Mario adjunte la captura o exporte el informe.

---

## Paso 2 — Lectura del archivo

- **PDF**: usar `Read` indicando rango de páginas (PVSyst suele exportar 8-15 páginas). Las páginas más relevantes son normalmente:
  - Página 1: ficha resumen con `Yr`, `Ya`, `PR`, producción específica.
  - Página de pérdidas: diagrama Sankey o tabla con pérdidas por concepto.
  - Página de configuración: módulos, inversores, MPPT, orientación e inclinación.
- **Imagen**: la captura ya viene visible en el contexto; léela como tal.

---

## Paso 3 — Extracción estructurada

Rellena este esquema con los valores que encuentres. Si un dato falta, pon `n/d`.

### A. Configuración del sistema
- Potencia nominal del campo FV (kWp)
- Modelo, potencia y nº de módulos
- Modelo, potencia y nº de inversores
- Configuración: módulos por string, strings por MPPT, MPPT por inversor
- Orientación (acimut) e inclinación (tilt)
- Tipo de instalación: tejado, marquesina, suelo, BIPV

### B. Recurso y meteorología
- Irradiación horizontal anual GHI (kWh/m²·año)
- Irradiación sobre el plano POA (kWh/m²·año)
- Fuente de datos meteo (Meteonorm 8.x, PVGIS-SARAH, etc.)

### C. Producción
- Energía anual `E_array` o `E_grid` (MWh/año)
- Producción específica `Yf` (kWh/kWp·año)
- Performance Ratio `PR` (%)
- Factor de capacidad implícito = `Yf / 8760`

### D. Pérdidas (en % o kWh/kWp·año)
- Sombras cercanas + lejanas
- IAM (incidencia angular)
- Soiling (suciedad)
- Temperatura
- Mismatch
- Ohmica DC + AC
- Pérdida en inversor
- Indisponibilidad

### E. Autoconsumo (si la simulación lo incluye)
- Energía autoconsumida (MWh/año)
- Energía vertida a red (MWh/año)
- Tasa de autoconsumo (%) = autoconsumida / producida
- Tasa de autosuficiencia (%) = autoconsumida / consumida

---

## Paso 4 — Diagnóstico

Compara los valores extraídos con los rangos esperados para una instalación FV en Madrid orientada a sur y con inclinación 25-35°:

| Magnitud | Rango esperado Madrid | Bandera roja si… |
|---|---|---|
| POA anual | 1.900-2.100 kWh/m²·año | < 1.700 (orientación mala) o > 2.200 (overfit) |
| Yf | 1.500-1.700 kWh/kWp·año | < 1.300 o > 1.800 |
| PR | 78-84% | < 74% o > 88% |
| Pérdida por sombras | 1-4% | > 8% → revisar layout |
| Pérdida por temperatura | 7-10% | > 12% → ventilación insuficiente |
| Mismatch | 1-2% | > 3% → strings mal balanceados |
| Pérdidas DC ohmicas | 0,8-1,5% | > 2,5% → secciones de cable insuficientes |
| Pérdidas en inversor | 2-3% | > 4% → infradimensionado o curva mala |

### Cotejo con el CPD (apéndice §14 del CLAUDE.md)
- Consumo CPD: ~3.778 MWh/año
- Refrigeración: ~1.242 MWh/año
- Marquesinas FV parking (3.150 m²): ~990 MWh/año brutos previstos

→ Comparar `E_grid` de PVSyst con esos ~990 MWh/año. Desviaciones > 10% merecen revisión del prediseño.

→ Calcular cobertura sobre total y sobre refrigeración:
- Cobertura total = `E_grid` / 3.778
- Cobertura refrigeración = `E_grid` / 1.242

---

## Paso 5 — Reporte estructurado

Devolver a Mario un bloque con esta estructura:

```
INTERPRETACIÓN PVSYST — <archivo>
=====================================

CONFIGURACIÓN
  - Potencia nominal:  XXX kWp
  - Módulos:           N × <modelo> (<W>)
  - Inversores:        N × <modelo> (<kW>)
  - Orientación:       acimut X°, tilt Y°

PRODUCCIÓN
  - Energía anual:     X.XXX MWh/año
  - Yf:                X.XXX kWh/kWp
  - PR:                XX,X %
  - GHI / POA:         XXX / XXX kWh/m²

PÉRDIDAS RELEVANTES
  - Sombras:           X,X %
  - Temperatura:       X,X %
  - Inversor:          X,X %
  - Otras notables:    ...

DIAGNÓSTICO
  ✓ <punto que sale en rango>
  ⚠ <punto en límite>
  ✗ <punto fuera de rango — explicar por qué>

COBERTURA CPD (vs. apéndice §14)
  - Sobre consumo total:    XX,X %
  - Sobre refrigeración:    XX,X %
  - Desviación vs. estimación prediseño (~990 MWh): ±X,X %

SUGERENCIAS PARA LA SIGUIENTE ITERACIÓN
  1. <acción concreta — qué tocar en PVSyst y para qué>
  2. <…>
```

---

## Paso 6 — Reglas operativas

- No inventes datos. Si un valor no aparece en el informe, déjalo como `n/d` y no lo metas en cálculos.
- Las recomendaciones tienen que ser concretas: "subir tilt a 30°", "cambiar Cable DC de 4 mm² a 6 mm²", "reorganizar strings 12/13 para reducir mismatch". Nada de generalidades.
- Si Mario ha pasado una captura que no es suficiente para llegar al diagnóstico completo, pídele explícitamente la página de pérdidas y la de configuración.
- No reescribas la simulación: solo interpretas. Si hay que tocar parámetros, dilo en sugerencias.

---

## Ejemplos de uso

```
/interpretar-pvsyst
/interpretar-pvsyst 04_Simulaciones/PVSyst/v1_marquesinas_parking.pdf
/interpretar-pvsyst 04_Simulaciones/PVSyst/Capturas/perdidas_v3.png
```
