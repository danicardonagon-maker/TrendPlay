
import numpy as np
import pandas as pd

# Dónde están los archivos (dentro de la carpeta data)
RUTA_GAMES = "data/games.csv"
RUTA_REVIEWS = "data/reviews.csv"
RUTA_STEAMSPY = "data/steamspy_insights.csv"
RUTA_GENRES = "data/genres.csv"


def _arreglar_app_id(df):
    """Deja app_id como número entero en todas las tablas,
    para que se puedan unir sin problemas."""
    df = df.copy()
    df["app_id"] = pd.to_numeric(df["app_id"], errors="coerce")
    df = df.dropna(subset=["app_id"])
    df["app_id"] = df["app_id"].astype(int)
    return df


def leer_archivos():
    """PASO 1: leer los 4 archivos."""
    opts = dict(engine="python", on_bad_lines="skip", na_values=["\\N"])
    games_df = _arreglar_app_id(pd.read_csv(RUTA_GAMES, **opts))
    reviews_df = _arreglar_app_id(pd.read_csv(RUTA_REVIEWS, **opts))
    steamspy_df = _arreglar_app_id(pd.read_csv(RUTA_STEAMSPY, **opts))
    genres_df = _arreglar_app_id(pd.read_csv(RUTA_GENRES, **opts))
    return games_df, reviews_df, steamspy_df, genres_df


def _columna_fecha(games_df):
    return "date_release" if "date_release" in games_df.columns else "release_date"


def limpiar_datos_nulos(games_df, reviews_df, steamspy_df):
    """PASO 2: quitar filas vacías en las columnas que usamos."""
    col_fecha = _columna_fecha(games_df)
    games_df = games_df.dropna(subset=[col_fecha]).copy()
    reviews_df = reviews_df.dropna(subset=["positive", "negative"]).copy()
    steamspy_df = steamspy_df.dropna(subset=["owners_range"]).copy()
    return games_df, reviews_df, steamspy_df


def calcular_aprobacion(games_df, reviews_df):
    """PASO 3: calcular approval_rate y aplicar los filtros de calidad."""
    reviews_df = reviews_df.copy()
    reviews_df["positive"] = pd.to_numeric(reviews_df["positive"], errors="coerce")
    reviews_df["negative"] = pd.to_numeric(reviews_df["negative"], errors="coerce")
    reviews_df["total_reviews"] = reviews_df["positive"] + reviews_df["negative"]

    # Mínimo 10 reseñas para que el porcentaje sea confiable
    reviews_df = reviews_df[reviews_df["total_reviews"] >= 10].copy()
    reviews_df["approval_rate"] = reviews_df["positive"] / reviews_df["total_reviews"] * 100

    # Fechas válidas entre 2000 y 2024
    col_fecha = _columna_fecha(games_df)
    games_df = games_df.copy()
    games_df[col_fecha] = pd.to_datetime(games_df[col_fecha], errors="coerce")
    games_df = games_df.dropna(subset=[col_fecha])
    games_df["year"] = games_df[col_fecha].dt.year
    games_df = games_df[(games_df["year"] >= 2000) & (games_df["year"] <= 2024)].copy()

    # Solo juegos (no DLC ni demos)
    if "app_type" in games_df.columns:
        games_df = games_df[games_df["app_type"] == "game"].copy()
    elif "type" in games_df.columns:
        games_df = games_df[games_df["type"] == "game"].copy()

    # Precio
    col_precio = next((c for c in ["price_final", "price", "Price"] if c in games_df.columns), None)
    if col_precio:
        games_df[col_precio] = pd.to_numeric(games_df[col_precio], errors="coerce")
        games_df = games_df[(games_df[col_precio] >= 0) & (games_df[col_precio] <= 20000)].copy()
        games_df = games_df.rename(columns={col_precio: "price_final"})

    df = pd.merge(
        games_df,
        reviews_df[["app_id", "approval_rate", "total_reviews"]],
        on="app_id",
        how="inner",
    )
    return df


def parsear_owners(steamspy_df):
    """PASO 4: convertir '10,000 .. 20,000' en un número (15000)."""

    def punto_medio(texto):
        try:
            partes = str(texto).replace(",", "").split("..")
            return (int(partes[0].strip()) + int(partes[1].strip())) / 2
        except Exception:
            return np.nan

    steamspy_df = steamspy_df.copy()
    steamspy_df["owners_mid"] = steamspy_df["owners_range"].apply(punto_medio)
    if "concurrent_users_yesterday" in steamspy_df.columns:
        steamspy_df["concurrent_users_yesterday"] = pd.to_numeric(
            steamspy_df["concurrent_users_yesterday"], errors="coerce"
        )
    return steamspy_df


def fusionar(juegos_df, steamspy_df, genres_df):
    """PASO 5: unir juegos + SteamSpy (dueños, jugadores, precio) + primer género."""
    posibles = ["app_id", "owners_mid", "concurrent_users_yesterday",
                "price", "initial_price", "discount", "developer", "publisher"]
    cols_spy = [c for c in posibles if c in steamspy_df.columns]
    # Evita columnas repetidas si games.csv ya trae alguna con el mismo nombre
    cols_spy = [c for c in cols_spy if c == "app_id" or c not in juegos_df.columns]

    df = pd.merge(juegos_df, steamspy_df[cols_spy].drop_duplicates("app_id"),
                  on="app_id", how="left")

    # SteamSpy guarda el precio en centavos: 999 = 9.99 dólares
    for col in ["price", "initial_price", "discount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "price" in df.columns:
        df["price"] = df["price"] / 100
    if "initial_price" in df.columns:
        df["initial_price"] = df["initial_price"] / 100

    df = df.rename(columns={
        "price": "precio_usd",
        "initial_price": "precio_original_usd",
        "discount": "descuento_pct",
    })

    if "genre" in genres_df.columns:
        primer_genero = genres_df.groupby("app_id")["genre"].first().reset_index()
        df = pd.merge(df, primer_genero, on="app_id", how="left")

    return df


def preparar_datos():
    """Hace todos los pasos en orden y devuelve la tabla final lista para la app."""
    games_df, reviews_df, steamspy_df, genres_df = leer_archivos()
    games_df, reviews_df, steamspy_df = limpiar_datos_nulos(games_df, reviews_df, steamspy_df)
    juegos_df = calcular_aprobacion(games_df, reviews_df)
    steamspy_df = parsear_owners(steamspy_df)
    return fusionar(juegos_df, steamspy_df, genres_df)