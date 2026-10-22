import streamlit as st
import datos

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
    st.write("Aquí irá el recomendador.")

with buscar:
    st.write("Aquí irá la ficha de cada juego.")

with cuando:
    st.write("Aquí irá el calendario de ofertas.")