"""
probar_casos.py — Rompe TrendPlay a propósito con los 8 casos de la clase.

Crea archivos de prueba pequeños con 3 juegos inventados, los daña de distintas
formas, corre la limpieza de datos.py con cada uno y muestra qué pasó.
No toca los datos reales de la carpeta data.
"""
import os
import shutil

import pandas as pd

import datos

CARPETA = "pruebas_tmp"


def base():
    """Tres juegos inventados y válidos. Cada caso los daña un poco."""
    games = pd.DataFrame({
        "app_id": [1, 2, 3],
        "name": ["Juego A", "Juego B", "Juego C"],
        "release_date": ["2020-01-15", "2021-06-10", "2022-09-30"],
        "type": ["game", "game", "game"],
    })
    reviews = pd.DataFrame({
        "app_id": [1, 2, 3],
        "positive": [90, 50, 30],
        "negative": [10, 50, 5],
    })
    steamspy = pd.DataFrame({
        "app_id": [1, 2, 3],
        "owners_range": ["10,000 .. 20,000", "20,000 .. 50,000", "0 .. 20,000"],
        "concurrent_users_yesterday": [100, 50, 10],
        "price": [999, 0, 499],
        "initial_price": [999, 0, 499],
        "discount": [0, 0, 0],
    })
    genres = pd.DataFrame({
        "app_id": [1, 2, 3],
        "genre": ["Action", "Adventure", "Indie"],
    })
    return games, reviews, steamspy, genres


def probar(numero, nombre, games, reviews, steamspy, genres, texto_reviews=None):
    """Guarda los archivos de prueba, corre la limpieza y dice qué pasó."""
    os.makedirs(CARPETA, exist_ok=True)
    datos.RUTA_GAMES = f"{CARPETA}/games.csv"
    datos.RUTA_REVIEWS = f"{CARPETA}/reviews.csv"
    datos.RUTA_STEAMSPY = f"{CARPETA}/steamspy_insights.csv"
    datos.RUTA_GENRES = f"{CARPETA}/genres.csv"

    games.to_csv(datos.RUTA_GAMES, index=False)
    steamspy.to_csv(datos.RUTA_STEAMSPY, index=False)
    genres.to_csv(datos.RUTA_GENRES, index=False)

    # Para los casos de archivo vacío escribimos el texto tal cual
    if texto_reviews is not None:
        with open(datos.RUTA_REVIEWS, "w", encoding="utf-8") as f:
            f.write(texto_reviews)
    else:
        reviews.to_csv(datos.RUTA_REVIEWS, index=False)

    try:
        df = datos.preparar_datos()
        juegos = ", ".join(df["name"].tolist())
        print(f"Caso {numero} - {nombre}\n   -> La app sigue funcionando con {len(df)} juego(s): {juegos}\n")
    except ValueError as error:
        print(f"Caso {numero} - {nombre}\n   -> ATRAPADO con mensaje claro: {error}\n")
    except Exception as error:
        print(f"Caso {numero} - {nombre}\n   -> FALLA, error no controlado: {type(error).__name__}: {error}\n")


if __name__ == "__main__":
    print("=== Rompiendo TrendPlay a propósito: 8 casos ===\n")

    # 1. Vacío: al Juego B le borramos las reseñas positivas
    g, r, s, ge = base()
    r.loc[1, "positive"] = None
    probar(1, "Vacío (Juego B sin reseñas positivas)", g, r, s, ge)

    # 2. Cero: Juego B con 0 reseñas
    g, r, s, ge = base()
    r.loc[1, ["positive", "negative"]] = 0
    probar(2, "Cero (Juego B con 0 reseñas)", g, r, s, ge)

    # 3. Negativo: Juego B con -50 reseñas positivas
    g, r, s, ge = base()
    r.loc[1, "positive"] = -50
    probar(3, "Negativo (Juego B con -50 reseñas positivas)", g, r, s, ge)

    # 4. Borde: Juego A con 10 reseñas justas (entra), Juego B con 9 (no entra),
    #    Juego C lanzado en 2025 (fuera del rango 2000-2024)
    g, r, s, ge = base()
    r.loc[0, ["positive", "negative"]] = [7, 3]
    r.loc[1, ["positive", "negative"]] = [6, 3]
    g.loc[2, "release_date"] = "2025-03-01"
    probar(4, "Borde (10 reseñas sí, 9 no, año 2025 no)", g, r, s, ge)

    # 5. Tipo equivocado: letras donde va un número
    g, r, s, ge = base()
    r["positive"] = r["positive"].astype(object)
    r.loc[1, "positive"] = "abc"
    s.loc[2, "owners_range"] = "muchos"
    probar(5, "Tipo equivocado (letras en reseñas y en dueños)", g, r, s, ge)

    # 6. Columna faltante: el archivo de reseñas sin la columna positive
    g, r, s, ge = base()
    probar(6, "Columna faltante (reviews sin 'positive')", g, r.drop(columns=["positive"]), s, ge)

    # 7a. Archivo con solo el encabezado
    g, r, s, ge = base()
    probar(7, "Archivo vacío (reviews solo con encabezado)", g, r, s, ge,
           texto_reviews="app_id,positive,negative\n")

    # 7b. Archivo completamente vacío
    g, r, s, ge = base()
    probar(7, "Archivo vacío (reviews sin nada, ni encabezado)", g, r, s, ge, texto_reviews="")

    # 8. Archivo de una sola fila
    g, r, s, ge = base()
    probar(8, "Una sola fila en cada archivo", g.iloc[:1], r.iloc[:1], s.iloc[:1], ge.iloc[:1])

    shutil.rmtree(CARPETA, ignore_errors=True)
    print("Listo. Los archivos de prueba se borraron; los datos reales no se tocaron.")