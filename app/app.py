import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# --------------------------------------------------
# Configuración
# --------------------------------------------------

st.set_page_config(
    page_title="Análisis inmobiliario RM",
    page_icon="🏠",
    layout="wide"
)


# --------------------------------------------------
# Rutas de datos
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_MARZO = (
    BASE_DIR
    / "data"
    / "processed"
    / "precios_casas_rm_limpio.csv"
)

RUTA_JULIO = (
    BASE_DIR
    / "data"
    / "processed"
    / "propiedades_web_scrape_limpio.csv"
)


# --------------------------------------------------
# Carga de datos
# --------------------------------------------------

@st.cache_data
def cargar_datos():

    df_marzo = pd.read_csv(RUTA_MARZO)
    df_julio = pd.read_csv(RUTA_JULIO)

    return df_marzo, df_julio


df_marzo, df_julio = cargar_datos()


# --------------------------------------------------
# Encabezado
# --------------------------------------------------

st.title("Análisis y visualización de precios de viviendas usadas")

st.write(
    "Análisis de propiedades de la Región Metropolitana "
    "a partir de datos recopilados en marzo y julio de 2023."
)

st.divider()


# --------------------------------------------------
# Indicadores generales
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Propiedades — marzo",
        f"{len(df_marzo):,}"
    )

with col2:
    st.metric(
        "Propiedades — julio",
        f"{len(df_julio):,}"
    )

with col3:
    st.metric(
        "Precio mediano — marzo",
        f"{df_marzo['Price_UF'].median():,.0f} UF"
    )

with col4:
    st.metric(
        "Precio mediano — julio",
        f"{df_julio['Price_UF'].median():,.0f} UF"
    )

comunas = sorted(
    set(df_marzo["Comuna"].dropna())
    | set(df_julio["Comuna"].dropna())
)

comuna_seleccionada = st.selectbox(
    "Filtrar análisis por comuna:",
    ["Todas las comunas"] + comunas
)

if comuna_seleccionada == "Todas las comunas":
    df_marzo_filtrado = df_marzo.copy()
    df_julio_filtrado = df_julio.copy()
else:
    df_marzo_filtrado = df_marzo[
        df_marzo["Comuna"] == comuna_seleccionada
    ].copy()

    df_julio_filtrado = df_julio[
        df_julio["Comuna"] == comuna_seleccionada
    ].copy()

st.divider()


# --------------------------------------------------
# Precio por comuna
# --------------------------------------------------

st.header("Precio mediano por comuna")

st.write(
    "Comparación del precio mediano de las viviendas usadas "
    "entre marzo y julio de 2023."
)


def resumen_por_comuna(df):

    resumen = (
        df.groupby("Comuna")
        .agg(
            Propiedades=("Price_UF", "count"),
            Precio_mediano_UF=("Price_UF", "median")
        )
        .reset_index()
    )

    # Solo comunas con suficiente cantidad de observaciones
    resumen = resumen[
        resumen["Propiedades"] >= 30
    ]

    return resumen


resumen_marzo = resumen_por_comuna(df_marzo)
resumen_julio = resumen_por_comuna(df_julio)


comparacion = resumen_marzo[
    ["Comuna", "Precio_mediano_UF"]
].merge(
    resumen_julio[
        ["Comuna", "Precio_mediano_UF"]
    ],
    on="Comuna",
    suffixes=("_marzo", "_julio")
)

comparacion = comparacion.sort_values(
    "Precio_mediano_UF_marzo"
)


# --------------------------------------------------
# Gráfico
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 7))

y = range(len(comparacion))
ancho = 0.35

ax.barh(
    [i - ancho / 2 for i in y],
    comparacion["Precio_mediano_UF_marzo"],
    height=ancho,
    label="Marzo 2023"
)

ax.barh(
    [i + ancho / 2 for i in y],
    comparacion["Precio_mediano_UF_julio"],
    height=ancho,
    label="Julio 2023"
)

ax.set_yticks(y)
ax.set_yticklabels(comparacion["Comuna"])

ax.set_xlabel("Precio mediano (UF)")
ax.set_ylabel("Comuna")

ax.legend()
ax.grid(axis="x", alpha=0.3)

fig.tight_layout()

st.pyplot(fig)

st.divider()

st.header("Superficie construida y precio")

st.write(
    "Relación entre la superficie construida y el precio de las "
    "viviendas usadas en marzo y julio de 2023."
)

fig, ax = plt.subplots(figsize=(10, 6))

df_marzo_grafico = df_marzo_filtrado[
    df_marzo_filtrado["Built Area"].notna() &
    (df_marzo_filtrado["Built Area"] <= 1000)
].copy()

df_julio_grafico = df_julio_filtrado[
    df_julio_filtrado["Built Area"].notna() &
    (df_julio_filtrado["Built Area"] <= 1000)
].copy()

ax.scatter(
    df_marzo_grafico["Built Area"],
    df_marzo_grafico["Price_UF"],
    alpha=0.25,
    label="Marzo 2023"
)

ax.scatter(
    df_julio_grafico["Built Area"],
    df_julio_grafico["Price_UF"],
    alpha=0.25,
    label="Julio 2023"
)

ax.set_xlabel("Superficie construida (m²)")
ax.set_ylabel("Precio (UF)")
ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()

st.pyplot(fig)

st.divider()

st.header("Características de la vivienda y precio")

st.write(
    "Comparación del precio mediano según distintas características "
    "de las viviendas."
)

opciones = {
    "Dormitorios": "Dorms",
    "Baños": "Baths",
    "Estacionamientos": "Parking"
}

caracteristica_nombre = st.selectbox(
    "Selecciona una característica:",
    list(opciones.keys())
)

caracteristica = opciones[caracteristica_nombre]

df_marzo_caracteristica = df_marzo_filtrado[
    df_marzo_filtrado[caracteristica].between(1, 7)
].copy()

df_julio_caracteristica = df_julio_filtrado[
    df_julio_filtrado[caracteristica].between(1, 7)
].copy()

resumen_marzo = (
    df_marzo_caracteristica
    .groupby(caracteristica)["Price_UF"]
    .median()
    .reset_index()
)

resumen_julio = (
    df_julio_caracteristica
    .groupby(caracteristica)["Price_UF"]
    .median()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    resumen_marzo[caracteristica],
    resumen_marzo["Price_UF"],
    marker="o",
    label="Marzo 2023"
)

ax.plot(
    resumen_julio[caracteristica],
    resumen_julio["Price_UF"],
    marker="o",
    label="Julio 2023"
)

ax.set_xlabel(caracteristica_nombre)
ax.set_ylabel("Precio mediano (UF)")
ax.set_title(
    f"Precio mediano según cantidad de {caracteristica_nombre.lower()}"
)

ax.set_xticks(range(1, 8))
ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()

st.pyplot(fig)

st.divider()

st.header("Cambios de precios entre marzo y julio")

st.write(
    "Comparación de los precios publicados para propiedades "
    "identificadas en ambos conjuntos de datos."
)


columnas_temporales = [
    "id",
    "Price_UF",
    "Comuna"
]

comparacion_temporal = df_marzo[
    columnas_temporales
].merge(
    df_julio[
        columnas_temporales
    ],
    on="id",
    suffixes=("_marzo", "_julio")
)

comparacion_temporal["Cambio_UF"] = (
    comparacion_temporal["Price_UF_julio"]
    - comparacion_temporal["Price_UF_marzo"]
)


def clasificar_cambio(cambio):

    if cambio > 0:
        return "Aumentó"
    elif cambio < 0:
        return "Disminuyó"
    else:
        return "Sin cambio"


comparacion_temporal["Tipo_cambio"] = (
    comparacion_temporal["Cambio_UF"]
    .apply(clasificar_cambio)
)

resumen_cambios = (
    comparacion_temporal["Tipo_cambio"]
    .value_counts()
    .reindex(
        ["Disminuyó", "Sin cambio", "Aumentó"],
        fill_value=0
    )
    .reset_index()
)

resumen_cambios.columns = [
    "Tipo de cambio",
    "Propiedades"
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Disminuyeron",
        f"{resumen_cambios.loc[0, 'Propiedades']:,}"
    )

with col2:
    st.metric(
        "Sin cambio",
        f"{resumen_cambios.loc[1, 'Propiedades']:,}"
    )

with col3:
    st.metric(
        "Aumentaron",
        f"{resumen_cambios.loc[2, 'Propiedades']:,}"
    )

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    resumen_cambios["Tipo de cambio"],
    resumen_cambios["Propiedades"]
)

ax.set_xlabel("Cambio del precio publicado")
ax.set_ylabel("Cantidad de propiedades")

ax.grid(axis="y", alpha=0.3)

fig.tight_layout()

st.pyplot(fig)

