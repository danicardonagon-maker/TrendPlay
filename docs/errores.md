# Lista de errores con datos raros — TrendPlay

Probamos la app con entradas raras para ver si se cae o si responde bien.
También documentamos los problemas que encontramos en los datos de origen.

## 1. Pruebas en la app (pestaña Para ti)

| # | Prueba | Qué debería pasar | Resultado obtenido |
|---|--------|-------------------|--------------------|
| 1 | Quitar todos los géneros (campo vacío) | Aviso azul: "Elige al menos un género" y no se cae | FUNCIONO COMO SE ESPERABA|
| 2 | Aprobación mínima en 100% | Muestra solo juegos con 100% o un aviso de que no hay resultados | FUNCIONO COMO SE ESPERABA|
| 3 | Aprobación 100% y popularidad 100.000 reseñas (filtros imposibles) | Aviso amarillo: "No encontramos juegos con esos filtros" | FUNCIONO COMO SE ESPERABA |
| 4 | Popularidad mínima en el valor más bajo (10 reseñas) | Muestra muchos juegos, la app no se pone lenta | FUNCIONO COMO SE ESPERABA|
| 5 | Elegir un género con muy pocos juegos | Muestra los pocos que hay o el aviso de sin resultados | FUNCIONO COMO SE ESPERABA |
| 6 | Cambiar los filtros muchas veces seguidas y rápido | La app responde sin volver a cargar los datos desde cero | FUNCIONO COMO SE ESPERABA |
| 7 | Escribir letras donde va un número | No aplica: los controles son barras y listas, el usuario no puede escribir texto. Se probará en la pestaña Buscar juego (T-09) | No aplica por diseño |

## 2. Problemas encontrados en los datos de origen

| # | Dato raro | Cómo lo detectamos | Qué hicimos |
|---|-----------|--------------------|-------------|
| 1 | La columna `price_overview` de games.csv está vacía (`\N`) en todos los juegos | Contamos los juegos con precio: 0 de 12.299 | Buscamos el precio en steamspy_insights.csv |
| 2 | En SteamSpy el precio viene en centavos (999 = 9,99 USD) | Revisamos las primeras filas del archivo | Dividimos entre 100 para pasarlo a dólares |
| 3 | Aun así, solo 67 juegos tienen precio mayor a 0 | Conteo de precios mayores a cero | Quitamos el filtro de presupuesto y lo cambiamos por popularidad mínima |
| 4 | 11.140 juegos (90%) aparecen como gratis (`is_free` = 1) | Conteo por `is_free`; en Steam real los gratis son minoría | Lo reportamos como limitación de la fuente de datos |
| 5 | La lista de recomendados incluye muchos prólogos y demos | Al revisar los resultados del recomendador | Lo reportamos como característica de los datos; se puede filtrar en una mejora futura |
| 6 | Juegos con muy pocas reseñas dan porcentajes extremos (por ejemplo 100% con 2 reseñas) | Regla del análisis inicial | Se exigen al menos 10 reseñas por juego |
| 7 | Fechas inválidas o fuera de rango | Conversión de fechas en la limpieza | Solo se usan juegos lanzados entre 2000 y 2024 |
| 8 | El número de dueños viene como texto ("10,000 .. 20,000") | Revisión de steamspy_insights.csv | Se convierte al punto medio del rango (15.000) |
| 9 | Los identificadores de juego (`app_id`) no siempre tenían el mismo tipo en los 4 archivos | Al unir las tablas | Se convierten todos a número entero antes de unir |


## 3. Rompan su propia app: 8 casos (sesión 13)

Probamos la limpieza de datos con archivos dañados a propósito usando `probar_casos.py`
(3 juegos inventados, sin tocar los datos reales). Para correrlo: `python probar_casos.py`.

| # | Caso | Cómo lo probamos | Qué hace la app | Tipo de respuesta |
|---|------|------------------|-----------------|-------------------|
| 1 | Vacío | Juego B sin reseñas positivas | Descarta el Juego B y sigue con 2 juegos. En la pantalla, si el usuario no elige géneros, sale un aviso | Validar y atrapar |
| 2 | Cero | Juego B con 0 reseñas | Descarta el Juego B (se exigen al menos 10 reseñas). Las barras no dejan elegir 0 | Validar e impedir |
| 3 | Negativo | Juego B con -50 reseñas positivas | Descarta el Juego B: una cantidad de reseñas no puede ser negativa | Validar |
| 4 | Extremo y borde | Juego A con 10 reseñas justas, Juego B con 9, Juego C de 2025 | Solo queda el Juego A: 10 reseñas sí entra, 9 no, y 2025 está fuera del rango 2000-2024. Con aprobación 100% y 100.000 reseñas sale el aviso de "sin resultados" | Validar y atrapar |
| 5 | Tipo o unidad equivocados | Letras ("abc") en reseñas y ("muchos") en dueños | Descarta el juego con letras en reseñas; los dueños con letras quedan como "sin dato". El precio venía en centavos y se convierte a dólares. El usuario no puede escribir texto en los controles | Validar e impedir |
| 6 | Columna faltante | Archivo de reseñas sin la columna `positive` | Mensaje claro: "Al archivo reviews.csv le faltan columnas: positive" | Atrapar |
| 7 | Archivo vacío | Reseñas solo con encabezado, y reseñas sin nada | Mensaje claro para cada caso: "solo tiene encabezado" y "está completamente vacío" | Atrapar |
| 8 | Archivo de una sola fila | Cada archivo con un solo juego | Sigue funcionando con 1 juego. La app no usa desviación estándar ni gráficas de tendencia que se rompan con una fila | Funciona sin cambios |

En ningún caso la app se cae ni muestra datos falsos sin avisar.