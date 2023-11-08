# <h1 align=center> **Proyecto de Telecomunicaciones - Data Analytics** </h1>

## **Descripción del problema**

## Introducción

El proyecto está orientado en un análisis realizado sobre la situación de las telecomunicaciones en Argentina, con un enfoque particular en el acceso a Internet. Este estudio abarca el período comprendido entre los años 2014 y 2022, centrándose en aspectos como las tasas de conectividad, las velocidades de Internet y la relación entre ambas variables. El objetivo es llevar a cabo un examen detallado de la situación en varias provincias para obtener una comprensión más profunda de la temática.

## Datos

A continuación se presenta los datasets proporcionados para el desarrollo del proyecto:

+ Internet_Penetracion.xlsx:
    El dataset contiene los accesos a internet fijo por cada 100 hogares y 100 habitantes a nivel nacional y provincial.

+ Accesos bandas.xlsx:
    El dataset contiene los registros de accesos a internet fijo por banda ancha y dial-up a nivel nacional y provincial.

+ Internet_Accesos-por-tecnología.xlsx:
    El dataset contiene los accesos a internet por tipo de tecnología (ADSL, Cablemodem, Fibra Óptica, Wireless, Otros) a nivel nacional y provincial.

+ historico_velocidad_internet.xlsx:
    El dataset contiene registros sobre la velocidad media de bajada a nivel nacional y provincial.

+ Internet_Accesos-por-velocidad.xlsx:
    El dataset contiene datos sobre las velocidades del internet y por rangos a nivel nacional.

+ Internet_Accesos-por-velocidad_provincias:
    El dataset contiene datos sobre los rangos de velocidad a nivel provincial (Este dataset fue extraido por medio de una API).

+ Internet_Ingresos.xlsx:
    El dataset contiene datos sobre los ingresos de internet fijo a nivel nacional.

+ Internet-Accesos-por-velocidad_por_loc.xlsx:
    El dataset contiene datos sobre las velocidades del internet por localidad.

+ Internet-Accesos-por-tecno_por_loc.xlsx:
    El dataset contiene los accesos a internet por tipo de tecnología (ADSL, Cablemodem, Fibra óptica, Wireless, Otros, Wimax, Satelital), a nivel localidad.

+ mapa_conectividad.xlsx:
    El dataset contiene datos sobre las tecnologías utilizadas por localidad y datos demográficos y geográficos de las localidades.

## Desarrollo del Proyecto

### 1. Extracción, Transformación y Carga (ETL):

A partir de los 10 datasets iniciales, se realizó un proceso de transformación de los datasets, pasando los registros a dataframes separándolos por nacionales, provinciales y locales.

De los dataframes resultantes se llevó a cabo un análisis preliminar de las variables, así como el tratamiento correspondiente a los registros nulos y duplicados. Se seleccionaron aquellos dataframes para realizar un análisis más extenso.

### 2. Análisis exploratorio de datos (EDA):

Se realizó un análisis independiente de los dataframes seleccionados, en total fueron seis (6) dataframes. Para cada uno de ellos se crearon gráficas de acorde a los registros que contenían y se analizaron los registros anómalos (outliers).

#### Accesos Internet Fijo Nacional

<img src='./images/Accesos Internet Fijo (Hogares-Habitantes).png'></img>

El gráfico de lineas de accesos a internet fijo por cada 100 hogares, muestra como los registros se comportan a lo largo del tiempo, en este caso cada trimestre. Se puede ver que siguen una tendencia ascendente a lo largo de los años, se observa que desde el 2014 al 2022, se incremento aproximadamente la mitad de los accesos desde el 2014. Así mismo existe, un punto de inflexión en el ultimo trimestre del 2019 y el primer trimestre del 2020, esto principalmente se debe a la pandemia, por lo cual los accesos se vieron disminuidos durante esa época.

#### Accesos Internet Fijo Provincial

<img src='./images/Accesos por provincia (Hogares).png'></img>

El gráfico de boxplot que representa los accesos por cada 100 hogares, organizados por provincias, revela patrones interesantes en la distribución de los datos. En particular, la Capital Federal se destaca con valores significativamente más altos, reflejando la densidad demográfica característica de esta, lo que justifica que estos valores no sean considerados como atípicos. Asimismo, varias provincias, como Catamarca, Córdoba, Jujuy, La Pampa, La Rioja, San Luis, Santiago del Estero y Tierra del Fuego, muestran una variabilidad notable, como se evidencia por la amplitud de las cajas y los bigotes en el gráfico. Esto refleja el crecimiento acelerado que estas provincias han experimentado en el acceso a Internet en comparación con otras regiones, y a pesar de esta variabilidad, no se observan valores atípicos, ya que los datos permanecen dentro de los límites establecidos.

En contraste, las demás provincias muestran una variabilidad menos marcada y han experimentado un aumento constante en sus valores a lo largo de los años. Sin embargo, se identifican dos excepciones: Mendoza y Neuquén, donde se encuentran valores que se extienden más allá de los bigotes en el gráfico. No obstante, un análisis más detenido revela que estos valores atípicos se deben al crecimiento acelerado en los accesos en los trimestres más recientes, lo que los excluye de la categoría de valores anómalos.

<img src='./images/Accesos por provincia (Habitantes).png'></img>

El gráfico boxplot que muestra los accesos por cada 100 habitantes, agrupados por provincias, revela importantes diferencias en la distribución de los datos. En particular, la Capital Federal destaca con valores sustancialmente más altos debido a su densa población, lo que justifica que estos valores se mantengan dentro de los límites y no sean considerados como valores atípicos. Por otro lado, varias provincias, como Catamarca, Chubut, Córdoba, Jujuy, La Pampa, La Rioja, San Luis, Santiago del Estero y Tierra del Fuego, muestran una variabilidad notoria, evidenciada por cajas y bigotes amplios, lo cual refleja su crecimiento acelerado en el acceso a Internet en comparación con otras provincias. A pesar de esta variabilidad, no se observan valores atípicos, ya que los datos siguen dentro de los límites establecidos.

En contraste, las demás provincias exhiben una variabilidad menos pronunciada y han experimentado un crecimiento constante en sus valores a lo largo de los años. Sin embargo, se identifican tres excepciones: la Capital Federal, Mendoza y Neuquén, donde se encuentran valores que se extienden más allá de los bigotes. Sin embargo, al analizar más a fondo, se observa que estos valores atípicos se deben al crecimiento acelerado en los accesos en los trimestres más recientes, lo que no los clasifica como valores anómalos.

#### Accesos Tecnología Nacional

<img src='./images/Conexiones tecnologia.png'></img>

El gráfico de líneas representa la evolución de los accesos por tecnología a lo largo del tiempo, desde el 2014 al 2022. Se visualiza una tendencia que destaca el pronunciado aumento en las conexiones de 'Cablemodem' durante el período, más que duplicando su cantidad desde 2014 hasta 2021. Sin embargo, en 2022, se observa una estabilización en esta tendencia de crecimiento. De manera similar, la conexión 'Fibra óptica' mostró un aumento constante, especialmente a partir de 2018, convirtiéndose en la segunda opción más utilizada. En contraste, las conexiones 'Wireless' y 'Otros' mantuvieron tendencias relativamente estables durante el período. En cambio la única tendencia que decreció fue las conexiones 'ADSL', que pasó de ser la más utilizada a ocupar el tercer lugar, debido al crecimiento de 'Cablemodem' y 'Fibra óptica'.

#### Accesos Tecnología Provincial

<img src='./images/Conexiones por tipo.png'></img>

El gráfico de barras apiladas ilustra las cantidades totales de conexiones de Internet en las provincias argentinas durante el último trimestre de 2022, organizadas por el tipo de conexión. Se destaca una marcada disparidad en la cantidad total de conexiones entre las provincias más pobladas, como 'Buenos Aires', 'Capital Federal', 'Córdoba' y 'Santa Fe', en comparación con las demás regiones. Esto se atribuye principalmente a las diferencias demográficas que caracterizan a estas provincias. En las áreas más densamente pobladas, las conexiones 'Cablemodem' prevalecen como la opción más utilizada, seguidas de cerca por 'ADSL', mientras que las conexiones de fibra óptica y otros tipos son minoritarias. En contraste, en provincias menos pobladas, como 'San Luis', donde la topografía y la geografía inciden en la disponibilidad de servicios, las conexiones 'Wireless' son la elección predominante. Estas diferencias demográficas y geográficas conducen a una variación en la distribución de tipos de conexión a Internet en todo el país.

#### Rangos Velocidades Provincial

<img src='./images/Conexiones velocidad.png'></img>

En el gráfico de barras apiladas que representa las cantidades totales de conexiones de Internet fijo por provincia para el último trimestre del 2022, se destaca una tendencia clara. Las provincias con una mayor densidad poblacional, como 'Buenos Aires', 'Capital Federal', 'Córdoba' y 'Santa Fe', exhiben una mayor cantidad de conexiones de Internet fijo. Sin embargo, lo que varía significativamente es la distribución de velocidades. En 'Buenos Aires', 'Córdoba' y 'Santa Fe', predominan las conexiones de velocidad moderada, seguidas por conexiones de velocidad alta y baja. 'Capital Federal' es la excepción, ya que presenta una cantidad similar de accesos con velocidades altas y moderadas. En contraste, provincias como 'La Pampa', 'San Juan', 'Santa Cruz' y 'Tierra del Fuego' tienen escasez de conexiones de alta velocidad, principalmente debido a factores demográficos y geográficos que dificultan la implementación de redes de alta velocidad.

Se puede resaltar la influencia de la demografía y la geografía en la distribución de velocidades de Internet fijo en las provincias argentinas. Las áreas densamente pobladas muestran una mayor diversidad en velocidades, mientras que las provincias con poblaciones más dispersas tienden a depender en su mayoría de conexiones de velocidad baja.

#### Conectividad Internet Localidades (Densidad Poblacional)

<img src='./images/Poblacion por Provincia.png'></img>

El gráfico de barras muestra la población de las localidades en cada provincia, y se observa una tendencia coherente con los gráficos anteriores. Las provincias más densamente pobladas, como 'Buenos Aires', 'Capital Federal', 'Córdoba' y 'Santa Fe', presentan una mayor cantidad total de accesos a Internet en comparación con las provincias menos densamente pobladas. Esta relación entre densidad poblacional y accesos a Internet se repite, destacando la influencia de la densidad poblacional en la conectividad en estas provincias en comparación con las que tienen menos habitantes.

Por otro lado, las provincias menos pobladas, como 'Tierra del Fuego', 'Catamarca', 'San Luis' y 'Santa Cruz', confirman lo que se ha observado en gráficos anteriores, donde a pesar de contar con una cantidad significativa de accesos a Internet, las velocidades de descarga son más bajas. Esta relación entre densidad poblacional y calidad de la conectividad se refleja en estas provincias con menos habitantes, donde la disponibilidad de accesos no necesariamente se traduce en velocidades más altas.

### 3.  KPI's:

+ Aumento de accesos internet:
    Aumentar en un 2% el acceso al servicio de internet trimestralmente, por cada 100 hogares.

+ Aumento de conexiones de Fibra Óptica:
    Aumentar en un 6% las conexiones de fibra óptica a nivel nacional para el próximo trimestre.

### 4. Dashboard:

El dashboard del análisis fue creado en Power Bi y fue diseñado de manera intuitiva e interactiva para el seguimiento y análisis de los datos más relevantes.

El dashboard contiene la siguiente estructura:

+ Presentación del Informe:
    Se proporciona una introducción general del informe

+ Accesos a Internet Fijo:
    Se presenta las datos históricos de los accesos a internet fijo a nivel nacional y provincial, así como la densidad poblacional.

+ Accesos a Internet por tecnología y velocidad:
    Se presenta las datos históricos de los accesos a internet por tipo de tecnología y rangos de velocidad, tanto a nivel nacional como provincial.

+ Key Performance Indicators (KPI's):
    Se muestran los KPI's establecidos, y la tasa de cumplimiento de los mismos a lo largo de los años.

+ Conclusiones:
    Se presenta conclusiones y recomendaciones asociadas al estudio realizado, haciendo un enfoque en los puntos de mejora para alcanzar los objetivos establecidos en los KPI's.

### 5. Conclusión:

Se ha observado un notable aumento en el acceso a Internet en los últimos años, impulsado por una demanda en constante crecimiento. Este aumento en la demanda ha generado la necesidad de velocidades de conexión más rápidas para satisfacer las necesidades del mundo moderno. En este contexto, la elección de tecnologías que favorezcan este desarrollo es clara, y la fibra óptica no solo ha experimentado un crecimiento evidente, sino que se presenta como una opción eficaz. La fibra óptica se destaca en entornos urbanos o densamente poblados, mientras que las conexiones inalámbricas son ideales para áreas rurales que también experimentan un aumento en la demanda de servicios de Internet.