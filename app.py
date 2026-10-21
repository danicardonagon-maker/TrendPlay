import streamlit as st

# Configuración de la página: título de la pestaña del navegador, ícono y ancho
st.set_page_config(page_title="TrendPlay", page_icon="🎮", layout="wide")

st.title("🎮 TrendPlay")
st.caption("Analítica con datos de Steam para decidir qué juego comprar")

# Las 4 pestañas del mockup
inicio, para_ti, buscar, cuando = st.tabs(
    ["Inicio", "Para ti", "Buscar juego", "¿Cuándo comprar?"]
)

with inicio:
    st.write("Aquí irá el resumen con datos reales.")

with para_ti:
    st.write("Aquí irá el recomendador.")

with buscar:
    st.write("Aquí irá la ficha de cada juego.")

with cuando:
    st.write("Aquí irá el calendario de ofertas.")