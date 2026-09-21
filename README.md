# NewsPulse-AI

Sistema automatizado en **Python** para el seguimiento y análisis de tendencias tecnológicas.

## ¿Qué hace este proyecto?
* **Web Scraping:** Extrae los últimos titulares de *Hacker News*.
* **Análisis de sentimiento (NLP):** Clasifica cada titular como Positivo, Neutro o Negativo con la librería `TextBlob` (basada en léxico, no en deep learning).
* **Data Logging:** Genera un reporte automático en formato `.csv` en la carpeta `/data` con los hallazgos del día.

## Tecnologías utilizadas
* **Lenguaje:** Python 3.12
* **Librerías:**
    * `Pandas` (Gestión de datos)
    * `BeautifulSoup4` (Extracción web)
    * `TextBlob` (Procesamiento de lenguaje natural)
    * `Requests` (Peticiones HTTP)

## Estructura del Proyecto
* `/core`: Lógica principal (scraper y procesador).
* `/data`: Almacenamiento de reportes generados.
* `main.py`: Punto de entrada del programa.

## Cómo ejecutarlo

1. Clona el repositorio: `git clone https://github.com/Ruben-PO/newspulse-ai.git` y entra en la carpeta con `cd newspulse-ai`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el programa: `python main.py`
4. Revisa el resultado en `/data`, donde se genera un `.csv` con los titulares extraídos y su sentimiento asociado.

## Ejemplo de salida

Extracto real de `data/reporte_diario.csv`:

```csv
noticia,sentimiento
ClickHouse acquires Langfuse,Neutro
The 600-year-old origins of the word 'hello',Neutro
US electricity demand surged in 2025 – solar handled 61% of it,Neutro
```

## Limitaciones

`TextBlob` está pensado para inglés y puntúa por palabras sueltas, así que la mayoría de titulares técnicos salen como *Neutro*. Está bien para un primer prototipo; el siguiente paso sería probar un modelo más fino (por ejemplo, uno de Hugging Face) y comparar resultados.

## Licencia

Este proyecto está bajo la licencia MIT — consulta el archivo [LICENSE](LICENSE) para más detalles.
