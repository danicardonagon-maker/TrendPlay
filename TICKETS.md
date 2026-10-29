# TICKETS — TrendPlay

Estados: ⬜ pendiente · 🟨 en curso · ✅ hecho · ❌ descartado
Regla: no hay ticket 2 sin ticket 1 corriendo. Un ticket = un commit.

## Construcción 1/3 y 2/3

| ID | Tarea | Criterio de aceptación | Responsable | Estado |
|----|-------|------------------------|-------------|--------|
| T-01 | Crear app.py con título y 4 pestañas vacías | `streamlit run app.py` abre y se ven las 4 pestañas | Juan David | ✅ |
| T-02 | requirements.txt, .gitignore y publicar en Community Cloud | El link abre en el celular y está en README.md | Juan David | ✅ |
| T-03 | Pasar la limpieza del notebook a datos.py | Al importar datos.py se puede generar la tabla limpia sin errores | Daniela Cardona | ✅ |
| T-04 | Crear preparar_datos.py que guarde data/juegos_limpios.csv | Descartado: los archivos pesan menos de 100 MB y la caché ya hace que la app cargue rápido | Daniela Cardona | ❌ |
| T-05 | Cargar los datos en la app (con caché) | Inicio muestra "N juegos analizados" calculado, no escrito a mano | Miguel Roa | ✅ |
| T-06 | Pestaña Para ti: controles de géneros, aprobación mínima y popularidad mínima | Los controles aparecen y se pueden mover | Miguel Roa | ✅ |
| T-07 | Lógica del recomendador: filtrar y ordenar juegos | Al cambiar la aprobación o la popularidad cambia la lista de juegos | Juan David | ✅ |
| T-08 | Mostrar cada juego recomendado como tarjeta | Cada tarjeta muestra nombre, género, precio y aprobación | Daniela Cardona | ✅ |

## Construcción 3/3

| ID | Tarea | Criterio de aceptación | Responsable | Estado |
|----|-------|------------------------|-------------|--------|
| T-09 | Pestaña Buscar juego: ficha de un juego | Al escribir un nombre se ven aprobación, reseñas, dueños, jugadores y precio | Miguel Roa | ✅ |
| T-10 | Comparar el juego contra el promedio de su género | La ficha dice si está por encima o por debajo del promedio y a qué porcentaje supera | Juan David | ✅ |
| T-11 | Inicio: gráfica de aprobación promedio por género (antes: mapa de calor género × precio) | Las barras salen ordenadas y solo con géneros de al menos 30 juegos. Se cambió porque solo 67 juegos tienen precio | Daniela Cardona | ✅ |
| T-12 | Manejo de datos raros en la app | Sin géneros, sin resultados, texto vacío, una letra o símbolos: la app avisa y no se cae | Miguel Roa | ✅ |
| T-13 | Entrenar modelo de aprobación | Descartado: el modelo dependía del precio, que viene vacío en el 99% de los juegos; preferimos no mostrar predicciones poco confiables | Juan David | ❌ |
| T-14 | Pestaña Predicción | Descartado: depende del T-13 | Daniela Cardona | ❌ |
| T-15 | Pestaña ¿Cuándo comprar?: calendario de ofertas de Steam | Muestra la próxima temporada calculada con la fecha de hoy, el calendario y una nota de que es información general | Miguel Roa | ✅ |
| T-16 | Documento de errores con datos raros (docs/errores.md) | Lista de pruebas con campo vacío, cero, letras y los 8 casos | Todos | ✅ |
| T-17 | Colores y estilo parecidos al mockup | La app se parece visualmente al mockup | Juan David | ⬜ Opcional |

## Arreglos de los 8 casos (sesión 13)

| ID | Tarea | Criterio de aceptación | Responsable | Estado |
|----|-------|------------------------|-------------|--------|
| T-18 | Validar archivos al leerlos: archivo inexistente, vacío, solo encabezado o con columnas faltantes | Cada caso muestra un mensaje claro en vez de caerse (casos 6 y 7) | Juan David | ✅ |
| T-19 | Descartar reseñas negativas o con letras | Esos juegos no entran a la tabla final (casos 3 y 5) | Juan David | ✅ |
| T-20 | Script probar_casos.py que rompe la app con los 8 casos | Al correrlo, ningún caso dice "FALLA" | Juan David | ✅ |

Nota: T-18, T-19 y T-20 se subieron juntos en el commit "Sesion 13: 8 casos de datos raros".