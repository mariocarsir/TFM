# Diseño del autoconsumo fotovoltaico para el CPD

El tiempo no acompaña y quiero que me ayudes con el diseño del autoconsumo fotovoltaico para el CPD. Para ponerte en contexto necesito que analices la documentación de la carpeta "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Documentacion de apoyo\Trabajo Autoconsumo CPD" (parte de esta documentación ya fue revisada previamente). En esta carpeta está el trabajo académico realizado para superar el Módulo 6: Autoconsumo Fotovoltaico del Máster ERMA. En ese trabajo se realizó prácticamente lo mismo que se pretende en el TFM (aunque en el TFM se profundizará más, se incluirá el estudio económico y se compararán más variantes de diseño). La presentación en dicha carpeta resume brevemente el trabajo realizado; para detalles más técnicos está el informe de PV Syst; la otra presentación es una guía metodológica para realizar el trabajo. Es necesario también revisar la carpeta "C:\Users\Usuario\OneDrive - Universidad Politécnica de Madrid\Escritorio\Claudio\TFM\Datos\Consumo CPD", que contiene los datos de consumo mensual y horario del CPD. En los datos mensuales se observa que solo hay registro de 11 meses, porque al momento de solicitar los datos diciembre de 2025 aún no había concluido.

Como se puede ver en la documentación, el trabajo anterior no obtuvo resultados muy favorables por dos motivos principales:

1. La cantidad de paneles instalables en la cubierta era mínima en comparación con el alto consumo constante 24/7 del CPD (y eso que el trabajo anterior solo intentaba cubrir el consumo de refrigeración; cubrir el consumo total no tenía viabilidad alguna con paneles FV en cubierta).
2. La zona de instalación no era propiamente la cubierta, sino una especie de tragaluz, lo que restringe el tipo de paneles utilizables.

Estructura de los ficheros de consumo mensual (ejemplo de referencia: 06_2025.xlsx):

- Columna B: PUE del CPD
- Columna C: Consumo general en kWh
- Columna F: Potencia general en kW
- Columnas restantes de consumo y potencia: lado A y lado B (IT). NOTA: la suma de A+B no es igual al general, ya que el general incluye refrigeración y servicios auxiliares.
- Columnas de temperatura y humedad: no relevantes para este análisis en esta fase.
- Filas 8645–8658 (al final del fichero): resumen estadístico con consumo máximo, mínimo, rango y promedio.
- Los datos tienen resolución de 5 minutos durante un mes completo.

Respecto a los ficheros de consumo horario: se desconoce con exactitud qué cambia respecto a los ficheros mensuales. Se solicita que los analices e indiques qué diferencias o información adicional aportan.

Las tres variantes de diseño a desarrollar son las siguientes:

1. Instalar paneles fotovoltaicos transparentes (BIPV) en la zona del tragaluz de la cubierta, y eliminar los sistemas de refrigeración de la cubierta para instalar paneles convencionales en esa área, sustituyendo el air-cooling por refrigeración geotérmica.
2. Instalar paneles de forma similar al tragaluz (integración arquitectónica o sobre marquesinas) en el parking adyacente al CPD.
3. Instalar una planta fotovoltaica tipo utility en suelo, identificando una superficie de terreno cercana al CPD suficientemente amplia.

Datos geométricos de referencia conocidos:

- Superficie del tragaluz: 472 m² (catastro) / 614 m² (Google Earth)
- Superficie total de cubierta: 3.111 m² (catastro) / 3.070 m² (Google Earth)

Solicitud concreta:
A partir del contexto proporcionado por la documentación revisada, se requiere una estimación aproximada (margen de error aceptable: 5–8%) de:

- La superficie que ocuparía cada variante (en m² o ha).
- El porcentaje del consumo global del CPD que cubriría cada variante.
- Para la variante 3 (planta en suelo): la superficie necesaria (en m² o ha) para cubrir el 100% del consumo, o al menos el 80%.

IMPORTANTE: No se requiere precisión extrema, pero las estimaciones deben ser técnicamente coherentes y útiles. Un rango como "entre 1 y 20.000 ha" no es aceptable. Si se necesita algún dato adicional para realizar las estimaciones, no dudes en solicitarlo.
