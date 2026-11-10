# Cómo llenar ENTREGA.md

`ENTREGA.md` es un índice de su proyecto, no un documento nuevo que haya que redactar. Sirve para que quien abra su repositorio encuentre en un minuto cada pieza del trabajo del semestre. Se llena en cuatro pasos:

1. **Copien la plantilla** a la raíz del repositorio con el nombre `ENTREGA.md` y escriban la URL de la app.
2. **Tabla 1 (archivos):** abran cada archivo en GitHub y comprueben que existe y que dice lo que la tabla indica. Marquen ✅ si está completo, ⚠️ si está parcial o ❌ si no está. Si no es ✅, escriban en "Nota" una línea de por qué.
3. **Tabla 2 (artefactos metodológicos):** en "Dónde está", pongan el enlace al archivo del repositorio o el nombre de la sección del Reporte 4 donde aparece (por ejemplo, "Reporte 4, sección 3" o `docs/flujo_app.md`). Si el artefacto no existe, déjenlo en blanco y escriban una nota; es mejor un vacío honesto que un enlace que no lleva a nada.
4. **Revisión final (miércoles 11):** otro integrante, que no la llenó, abre cada enlace y comprueba que lleva a lo que dice. Después se reproducen las mismas dos tablas como anexo del Reporte 4.

Reglas: lo que marquen debe coincidir con el estado real del repositorio, y la columna opcional "Cómo alimentó la siguiente etapa" es una sola línea, no un párrafo.

---

Copien todo lo que sigue a la raíz de su repositorio como `ENTREGA.md`:

---

# Checklist de entrega final — [Nombre del proyecto]

URL de la app: [url]
Etiqueta de la versión entregada: final-12nov

## 1. Archivos del procedimiento

Estado: ✅ completo · ⚠️ parcial (explicar) · ❌ no está (explicar)

| Archivo | Semana | Qué contiene | Estado | Nota |
|---|---|---|---|---|
| README.md | S11, S14 | URL, propósito, cómo correr en local, ejemplo, enlace al datafolio | | |
| app.py | S12–S14 | Interfaz en Streamlit; manejo de entradas inválidas; aviso de uso | | |
| pipeline.py | S10, S13 | Funciones reutilizables, modelo de referencia, main(), random_state, RANGOS | | |
| entrenar.py | S10–S11 | Entrena y guarda el modelo fuera de la app | | |
| modelo/ | S10–S11 | Modelo guardado (joblib) | | |
| datos/ | S11 | Solo datos publicables (o README dice de dónde obtenerlos) | | |
| notebooks/eda.ipynb | S6–S8 | EDA: auditoría, visuales, pruebas estadísticas | | |
| docs/funcionalidades.md | S11 | Actualizado a la app que existe hoy | | |
| docs/flujo_app.md + docs/capturas/ | S16 | Páginas reales, diagrama de flujo, decisiones de diseño (qué se muestra y qué no, y por qué) | | |
| TICKETS.md | S11–S15 | Al día: estados, responsables, MVP y "fuera del MVP" | | |
| requirements.txt | S11–S12 | Librerías con versiones fijas | | |
| .gitignore | S12 | Incluye .streamlit/secrets.toml | | |
| datafolio.pdf | S15–S16 | La página visual del datafolio | | |
| Etiquetas de Git | S14–S15 | estable-29oct y final-12nov | | |

## 2. Artefactos metodológicos

| Artefacto | Semana | Dónde está (archivo o sección del Reporte 4) | Cómo alimentó la siguiente etapa (opcional, una línea) |
|---|---|---|---|
| Big Idea inicial y actualizada | S3, S15 | | |
| Descomposición del alcance (Top-Down / Bottom-Up) | S3 | | |
| Auditoría de datos en cuatro frentes | S5 | | |
| Hallazgos del EDA y pruebas estadísticas | S6–S8 | | |
| Frase de método y enfoque elegido | S9 | | |
| Modelo de referencia y su resultado | S9–S10 | | |
| Supuestos del método y casos en que no debe usarse | S10 | | |
| Mockup y decisiones de diseño (qué se muestra y qué no, y por qué) | S10–S11 | | |
| Lista de errores y resultado de los ocho casos | S12–S13 | | |
| RANGOS y su fuente | S13 | | |
| Checklist MVP y tarjeta de prueba | S14 | | |
| Cuenta de impacto (cuatro pasos, rango) | S14 | | |
| Aviso de uso responsable | S14 | | |
| Flujo real de la app y decisiones de diseño | S16 | | |
