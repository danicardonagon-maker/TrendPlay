# TICKETS — TrendPlay

Estados: ⬜ pendiente · 🟨 en curso · ✅ hecho
Regla: no hay ticket 2 sin ticket 1 corriendo. Un ticket = un commit.

## Para el 22 de octubre

| ID | Tarea | Criterio de aceptación | Responsable | Estado |
|----|-------|------------------------|-------------|--------|
| T-01 | Crear app.py con título y 4 pestañas vacías | `streamlit run app.py` abre y se ven las 4 pestañas | Juan David | ✅ |
| T-02 | requirements.txt, .gitignore y publicar en Community Cloud | El link abre en el celular y está en README.md | Juan David | ✅ |
| T-03 | Pasar la limpieza del notebook a datos.py | Al importar datos.py se puede generar la tabla limpia sin errores | Daniela Cardona | ✅ |
| T-04 | Crear preparar_datos.py que guarde data/juegos_limpios.csv | El archivo existe y pesa menos de 100 MB | Daniela Cardona | ✅ |
| T-05 | Cargar los datos en la app (con caché) | Inicio muestra "N juegos analizados" calculado, no escrito a mano | Miguel Roa | ✅ |
| T-06 | Pestaña Para ti: controles de géneros, aprobación mínima y popularidad mínima | Los controles aparecen y se pueden mover | Miguel Roa | ✅ |
| T-07 | Lógica del recomendador: filtrar y ordenar juegos | Al cambiar la aprobación o la popularidad cambia la lista de juegos | Juan David | ⬜ |
| T-08 | Mostrar cada juego recomendado como tarjeta | Cada tarjeta muestra nombre, género, precio y aprobación | Daniela Cardona | ⬜ |

## Después del 22 de octubre

| ID | Tarea | Criterio de aceptación | Responsable | Estado |
|----|-------|------------------------|-------------|--------|
| T-09 | Pestaña Buscar juego: ficha de un juego | Al escribir un nombre se ven aprobación, precio, dueños y jugadores | Miguel Roa | ⬜ |
| T-10 | Comparar el juego contra el promedio de su género | La ficha dice si está por encima o por debajo del promedio | Juan David | ⬜ |
| T-11 | Inicio: métricas reales y mapa de calor género × precio | El mapa de calor reparte bien los juegos en los rangos de precio | Daniela Cardona | ⬜ |
| T-12 | Manejo de datos raros en la app | Sin géneros elegidos o búsqueda sin resultados, la app avisa y no se cae | Miguel Roa | ⬜ |
| T-13 | Entrenar modelo de aprobación y guardarlo en modelo/modelo.joblib | Su error (RMSE) es menor que el del modelo de referencia | Juan David | ⬜ |
| T-14 | Pestaña Predicción: el usuario da género, precio y año y recibe aprobación predicha | El número cambia al cambiar los datos de entrada | Daniela Cardona | ⬜ |
| T-15 | Pestaña ¿Cuándo comprar?: calendario de ofertas de Steam | Se ve el calendario con una nota de que es información general | Miguel Roa | ⬜ |
| T-16 | Documento de errores con datos raros (docs/errores.md) | Lista de pruebas con campo vacío, cero y letras donde va número | Todos | ⬜ |
| T-17 | Colores y estilo parecidos al mockup | La app se parece visualmente al mockup | Juan David | ⬜ |