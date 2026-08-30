# Análisis del mercado inmobiliario de la Región Metropolitana

## Integrantes

- German Echeverri
- [Integrante 2]
- [Integrante 3]
- [Integrante 4]
- [Integrante 5]
- [Integrante 6]

## Descripción del proyecto

Este proyecto busca analizar el mercado inmobiliario de la Región Metropolitana de Chile a partir de datos de propiedades publicados durante 2023.

El objetivo es estudiar cómo se relacionan los precios de las propiedades con sus características y ubicación, identificando diferencias entre comunas y patrones que puedan ser representados mediante visualizaciones.

## Problemática

El mercado inmobiliario presenta importantes diferencias de precios dependiendo de la ubicación y las características de cada propiedad. Sin embargo, la gran cantidad de publicaciones disponibles dificulta identificar visualmente estos patrones.

## Motivación

El análisis de estos datos puede permitir comprender mejor las diferencias existentes entre comunas y explorar qué características de las propiedades están asociadas a variaciones en sus precios.

## Pregunta inicial

¿Cómo se relaciona el precio de las propiedades con sus características y ubicación en las comunas de la Región Metropolitana, a partir de los datos recopilados en 2023?

## Alcance

El análisis se enfocará inicialmente en propiedades de la Región Metropolitana presentes en los datasets disponibles.

Se estudiarán principalmente:

- Precio de las propiedades.
- Comuna y ubicación.
- Superficie construida.
- Superficie total.
- Número de dormitorios.
- Número de baños.
- Número de estacionamientos.

El análisis se centrará en los datos recopilados durante 2023 y no contempla inicialmente la predicción de precios futuros.

## Datasets

### Precios Casas RM

- Archivo: `2023-03-08 Precios Casas RM.csv`
- Registros: 7.779
- Cobertura: Región Metropolitana
- Comunas: 51

### Propiedades Web Scrape

- Archivo: `2023-07-18 Propiedades Web Scrape.csv`
- Registros: 9.291
- Cobertura: Región Metropolitana
- Comunas: 52

### Variables principales

- `Price_CLP`: precio en pesos chilenos.
- `Price_UF`: precio en UF.
- `Price_USD`: precio en dólares.
- `Comuna`: comuna de la propiedad.
- `Ubicacion`: ubicación registrada.
- `Dorms`: cantidad de dormitorios.
- `Baths`: cantidad de baños.
- `Built Area`: superficie construida.
- `Total Area`: superficie total.
- `Parking`: cantidad de estacionamientos.
- `id`: identificador de la publicación.
- `Realtor`: corredor o agencia inmobiliaria.

## Estructura del repositorio

```text
proyecto-inmobiliario/
│
├── data/
│   ├── 2023-03-08 Precios Casas RM.csv
│   └── 2023-07-18 Propiedades Web Scrape.csv
│
├── notebooks/
│   └── exploracion.ipynb
│
└── README.md