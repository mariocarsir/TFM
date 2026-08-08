# Registro de hallazgos de auditoría

Tabla viva del meta-flujo del proyecto. La mantiene la skill `/auditor`: la lee en la Fase 0
antes de analizar nada y la actualiza en la Fase 4.

Los ID son correlativos y **nunca se reutilizan**, ni siquiera si el hallazgo queda obsoleto.

## Estados

| Estado | Significado | Efecto en la siguiente auditoría |
| --- | --- | --- |
| `pendiente` | Propuesto, todavía sin resolver | **Reaparece**, indicando su antigüedad en número de auditorías |
| `aplicado` | Ejecutado, con hash de commit en la Nota | No reaparece. Si el síntoma vuelve, se abre un hallazgo nuevo etiquetado "regresión de AUD-NNN" |
| `rechazado` | Mario dijo que no. El motivo va siempre en la Nota | **No se vuelve a proponer nunca** |
| `obsoleto` | Dejó de aplicar porque el proyecto cambió | No reaparece |

## Hallazgos

| ID | Hallazgo | Eje | Severidad | Estado | Fecha | Nota |
| --- | --- | --- | --- | --- | --- | --- |

## Historial de auditorías

Permite calcular la antigüedad de los hallazgos `pendiente`.

| Fecha | Ámbito | Informe | Hallazgos | Aplicados |
| --- | --- | --- | --- | --- |
