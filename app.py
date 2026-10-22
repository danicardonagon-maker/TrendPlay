import streamlit as st
import datos
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="TrendPlay", page_icon="🎮", layout="wide")


@st.cache_data
def cargar_datos():
    """Prepara la tabla de juegos una sola vez y la guarda en memoria.
    Así la app no repite la limpieza cada vez que el usuario hace clic."""
    return datos.preparar_datos()


st.title("🎮 TrendPlay")
st.caption("Analítica con datos de Steam para decidir qué juego comprar")

with st.spinner("Cargando datos de Steam... (la primera vez tarda un poco)"):
    df = cargar_datos()

# Las 4 pestañas del mockup
inicio, para_ti, buscar, cuando = st.tabs(
    ["Inicio", "Para ti", "Buscar juego", "¿Cuándo comprar?"]
)

with inicio:
    st.subheader("¿Vale la pena jugarlo?")
    st.write(
        "Analizamos las reseñas de miles de juegos de Steam para ayudarte "
        "a encontrar los que más le gustan a la gente."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Juegos analizados", f"{len(df):,}".replace(",", "."))
    col2.metric("Aprobación promedio", f"{df['approval_rate'].mean():.1f}%")
    col3.metric("Géneros distintos", df["genre"].nunique())

with para_ti:
    st.subheader("Motor de recomendaciones")
    st.write(
        "Elige lo que te gusta y te mostramos los juegos mejor valorados "
        "por la comunidad de Steam."
    )

    # Lista de géneros, del más común al menos común
    generos = df["genre"].value_counts().index.tolist()

    col_a, col_b = st.columns(2)

    with col_a:
        generos_elegidos = st.multiselect(
            "Géneros que te gustan",
            options=generos,
            default=generos[:2],
        )

    with col_b:
        aprobacion_min = st.slider(
            "Aprobación mínima (%)",
            min_value=50,
            max_value=100,
            value=75,
            step=5,
        )
        resenas_min = st.select_slider(
            "Popularidad mínima (número de reseñas)",
            options=[10, 100, 1000, 10000, 100000],
            value=1000,
            format_func=lambda x: f"{x:,}".replace(",", "."),
        )

    # Resumen de lo que eligió el usuario (con comas entre géneros y punto en los miles)
    texto_generos = ", ".join(generos_elegidos) if generos_elegidos else "ningún género"
    texto_resenas = f"{resenas_min:,}".replace(",", ".")
    st.caption(
        f"Elegiste: {texto_generos} · aprobación desde {aprobacion_min}% · "
        f"al menos {texto_resenas} reseñas"
    )

    if not generos_elegidos:
        st.info("Elige al menos un género para ver recomendaciones.")
    else:
        # Filtrar según lo que eligió el usuario
        recomendados = df[
            (df["genre"].isin(generos_elegidos))
            & (df["approval_rate"] >= aprobacion_min)
            & (df["total_reviews"] >= resenas_min)
        ]

        # Ordenar: primero más aprobación; si empatan, más reseñas
        recomendados = recomendados.sort_values(
            ["approval_rate", "total_reviews"], ascending=False
        )

        if recomendados.empty:
            st.warning(
                "No encontramos juegos con esos filtros. "
                "Prueba bajando la aprobación mínima o la popularidad."
            )
        else:
            st.success(
                f"Encontramos {len(recomendados)} juegos. "
                "Estos son los 10 mejor valorados:"
            )
            top = recomendados.head(10)
            columnas = st.columns(2)

            for i, (_, juego) in enumerate(top.iterrows()):
                # Reparte las tarjetas: una a la izquierda, otra a la derecha
                with columnas[i % 2]:
                    with st.container(border=True):
                        aprob = juego["approval_rate"]

                        # Veredicto calculado según la aprobación
                        if aprob >= 95:
                            etiqueta = "🟢 **MUY RECOMENDADO**"
                        elif aprob >= 85:
                            etiqueta = "🟡 **RECOMENDADO**"
                        else:
                            etiqueta = "🟠 **CON RESERVAS**"

                        st.subheader(juego["name"], anchor=False)

                        detalle = f"{juego['genre']} · {int(juego['year'])}"
                        if "developer" in juego.index and pd.notna(juego["developer"]):
                            detalle += f" · {juego['developer']}"
                        st.caption(detalle)

                        st.markdown(etiqueta)

                        resenas = f"{int(juego['total_reviews']):,}".replace(",", ".")
                        precio = juego["precio_usd"] if "precio_usd" in juego.index else None
                        if pd.notna(precio) and precio > 0:
                            texto_precio = f"${precio:.2f} USD"
                        else:
                            texto_precio = "Sin dato"

                        st.write(
                            f"Aprobación: **{aprob:.1f}%** · "
                            f"Reseñas: **{resenas}** · "
                            f"Precio: **{texto_precio}**"
                        )

with buscar:
    st.write("Aquí irá la ficha de cada juego.")

with cuando:
    st.write("Aquí irá el calendario de ofertas.")