"""
estilo.py — Decoración retro/arcade de TrendPlay.
Colores y fuentes tomados del mockup del equipo.
"""
import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&family=Inter:wght@400;600;700&display=swap');

:root {
  --verde: #00FF87;
  --azul: #00D4FF;
  --dorado: #FFD700;
  --rosa: #FF4A9B;
  --fondo: #080810;
  --panel: #0D1B2A;
  --borde: #1E3A5F;
  --texto: #E8EDF5;
  --gris: #8899AA;
}

/* Fondo con cuadrícula tipo arcade */
.stApp {
  background-color: var(--fondo);
  background-image:
    linear-gradient(rgba(0, 212, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 212, 255, 0.05) 1px, transparent 1px);
  background-size: 40px 40px;
}

/* Texto normal */
.stMarkdown p, label { font-family: 'Inter', sans-serif; }

/* Títulos de sección y nombres de juegos: letra de consola con brillo */
h3 {
  font-family: 'VT323', monospace !important;
  font-size: 2.1rem !important;
  color: var(--azul) !important;
  text-shadow: 0 0 8px rgba(0, 212, 255, 0.6);
  letter-spacing: 1px;
}
h4 {
  font-family: 'VT323', monospace !important;
  font-size: 1.7rem !important;
  color: var(--dorado) !important;
}

/* Pestañas como botones de menú de videojuego */
.stTabs [data-baseweb="tab-list"] {
  gap: 8px;
  border-bottom: 2px solid var(--borde);
}
.stTabs [data-baseweb="tab"] {
  background: var(--panel);
  border: 1px solid var(--borde);
  border-radius: 8px 8px 0 0;
  padding: 10px 16px;
}
.stTabs [data-baseweb="tab"] p {
  font-family: 'Press Start 2P', monospace !important;
  font-size: 0.6rem !important;
  color: var(--gris);
}
.stTabs [aria-selected="true"] {
  background: var(--verde) !important;
  box-shadow: 0 0 14px var(--verde);
}
.stTabs [aria-selected="true"] p { color: var(--fondo) !important; }

/* Números grandes como marcador de puntaje */
[data-testid="stMetric"] {
  background: var(--panel);
  border: 1px solid var(--borde);
  border-radius: 10px;
  padding: 14px 18px;
  box-shadow: 0 0 14px rgba(0, 255, 135, 0.08);
}
[data-testid="stMetricLabel"] p {
  font-family: 'Press Start 2P', monospace !important;
  font-size: 0.5rem !important;
  color: var(--gris) !important;
  letter-spacing: 1px;
}
[data-testid="stMetricValue"] {
  font-family: 'VT323', monospace !important;
  font-size: 2.6rem !important;
  color: var(--verde) !important;
  text-shadow: 0 0 10px rgba(0, 255, 135, 0.7);
}

/* Tarjetas: brillan al pasar el mouse */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: rgba(13, 27, 42, 0.85);
  transition: box-shadow 0.2s, transform 0.2s;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
  box-shadow: 0 0 18px rgba(0, 212, 255, 0.35);
  transform: translateY(-2px);
}

/* Géneros elegidos en rosa */
[data-baseweb="tag"] { background: var(--rosa) !important; }

/* Banner del título */
.tp-banner {
  text-align: center;
  padding: 28px 16px 22px;
  margin-bottom: 18px;
  border: 2px solid var(--borde);
  border-radius: 14px;
  background: linear-gradient(135deg, #0D1B2A 0%, #13284A 50%, #0D1B2A 100%);
  box-shadow: 0 0 25px rgba(0, 212, 255, 0.15), inset 0 0 40px rgba(0, 255, 135, 0.05);
}
.tp-sub {
  font-family: 'Press Start 2P', monospace;
  font-size: 0.6rem;
  color: var(--dorado);
  letter-spacing: 2px;
  animation: parpadeo 1.2s steps(2, start) infinite;
}
.tp-logo {
  font-family: 'Press Start 2P', monospace;
  font-size: clamp(1.6rem, 6vw, 3.2rem);
  color: var(--verde);
  text-shadow: 0 0 10px var(--verde), 4px 4px 0 #003D22;
  margin: 14px 0;
}
.tp-logo span {
  color: var(--rosa);
  text-shadow: 0 0 10px var(--rosa), 4px 4px 0 #4A0F2C;
}
.tp-tag {
  font-family: 'VT323', monospace;
  font-size: 1.4rem;
  color: var(--texto);
}
@keyframes parpadeo { to { visibility: hidden; } }
</style>
"""

BANNER = """
<div class="tp-banner">
<div class="tp-sub">▶ PLAYER 1 · PRESS START</div>
<div class="tp-logo">TREND<span>PLAY</span></div>
<div class="tp-tag">Analítica con datos de Steam para decidir qué juego comprar</div>
</div>
"""


def aplicar_estilo():
    """Carga las fuentes y los colores retro en toda la app."""
    st.markdown(CSS, unsafe_allow_html=True)


def banner():
    """Muestra el título grande estilo arcade."""
    st.markdown(BANNER, unsafe_allow_html=True)