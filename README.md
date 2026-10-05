Análisis y visualización de precios de viviendas usadas en la Región Metropolitana
-

Integrantes: 

-Francisco Javier Angel.

-German Echeverri.

-Rodrigo Plaza.

-Constanza Venegas.

Descripción
-

El mercado de viviendas usadas en la Región Metropolitana presenta diferencias de precios entre las distintas comunas y propiedades. Sin embargo, observar los precios de manera aislada no permite identificar fácilmente cómo se distribuyen territorialmente ni qué características presentan las viviendas de mayor y menor costo.

Este proyecto busca analizar y visualizar los precios de viviendas usadas de la Región Metropolitana, considerando su comuna y características como superficie construida, superficie total, cantidad de dormitorios, baños y estacionamientos.

Motivación
-
La motivación del proyecto surge de la necesidad de comprender las diferencias existentes en los precios de las viviendas usadas dentro de la Región Metropolitana.

A través de la visualización de datos se busca facilitar la comparación entre comunas e identificar patrones que permitan observar qué características están presentes en las viviendas de mayor y menor costo.

Pregunta inicial
-
¿Cómo varían los precios de las viviendas usadas entre las comunas de la Región Metropolitana y qué características de las viviendas se asocian a precios más altos o más bajos?

Alcance
-
El proyecto estudiará la distribución de los precios de las viviendas usadas en las distintas comunas de la Región Metropolitana, utilizando como unidad de observación cada propiedad registrada en los datasets disponibles. El análisis se centrará en identificar diferencias territoriales en los precios y explorar su relación con características de las viviendas, principalmente superficie construida, superficie total, cantidad de dormitorios, baños y estacionamientos.

El período de análisis estará determinado por las fechas de los datasets utilizados, correspondientes a marzo y julio de 2023. El estudio se limitará a las propiedades registradas en dichos conjuntos de datos y no busca representar la totalidad del mercado inmobiliario de la Región Metropolitana.

Quedarán fuera del alcance factores que no se encuentran disponibles en los datos, como condiciones de financiamiento, antigüedad de la propiedad, estado de conservación, características del barrio o evolución histórica de los precios. Asimismo, el análisis buscará identificar patrones y asociaciones, pero no establecer relaciones causales entre las características de una vivienda y su precio.

Fuente de los datasets
-

Se utilizarán dos datasets proporcionados para el proyecto:

https://www.kaggle.com/datasets/luisfelipetn/valor-casas-usadas-chile-rm-08032023

2023-03-08 Precios Casas RM.csv

2023-07-18 Propiedades Web Scrape.csv

Los datasets contienen registros de propiedades ubicadas en distintas comunas de la Región Metropolitana.

Breve descripción de los datos
-
Los datasets contienen información de viviendas y sus principales características. Cada registro representa una propiedad y cuenta con variables relacionadas con su precio, ubicación y atributos físicos.

Las principales variables disponibles son:
-
Variable	     |          Descripción

Price_CLP	     |          Precio de la vivienda en pesos chilenos

Price_UF	     |          Precio de la vivienda expresado en UF

Price_USD	     |          Precio de la vivienda expresado en dólares

Comuna	       |          Comuna donde se encuentra la propiedad

Ubicacion	     |          Ubicación o referencia de la propiedad

Dorms	         |          Cantidad de dormitorios

Baths	         |          Cantidad de baños

Built Area	   |          Superficie construida de la vivienda

Total Area	   |          Superficie total del terreno o propiedad

Parking	       |          Cantidad de estacionamientos

id	           |          Identificador de la propiedad

Realtor	       |          Corredora o agente asociado a la publicación, cuando está disponible

El primer dataset contiene 7.779 registros, mientras que el segundo contiene 9.291 registros, para un total de 17.070 registros antes de cualquier proceso de limpieza, validación o eliminación de duplicados.

Instrucciones de ejecucion:
Paso 1: Instalar Streamlit usando python -m
En lugar de llamar a streamlit directamente, ejecuta la instalación a través de la carpeta oficial de Python:

PowerShell
python -m pip install streamlit pandas plotly
(Si usas Python 3 con otro comando, también puedes probar con py -m pip install streamlit pandas plotly).

Paso 2: Ejecutar la aplicación usando python -m
Una vez terminada la instalación, ejecuta el servidor de Streamlit anteponiendo python -m:

PowerShell
python -m streamlit run app.py
