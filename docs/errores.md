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