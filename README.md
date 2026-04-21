# 🚀 NewsPulse-AI

Sistema automatizado en **Python** para el seguimiento y análisis de tendencias tecnológicas.

## 🛠️ ¿Qué hace este proyecto?
* **Web Scraping:** Extrae los últimos titulares de *Hacker News*.
* **Inteligencia Artificial (NLP):** Analiza el sentimiento de cada noticia (Positivo/Neutro/Negativo) usando la librería `TextBlob`.
* **Data Logging:** Genera un reporte automático en formato `.csv` en la carpeta `/data` con los hallazgos del día.

## 📦 Tecnologías utilizadas
* **Lenguaje:** Python 3.12
* **Librerías:** * `Pandas` (Gestión de datos)
    * `BeautifulSoup4` (Extracción web)
    * `TextBlob` (Procesamiento de lenguaje natural)
    * `Requests` (Peticiones HTTP)

## 📂 Estructura del Proyecto
* `/core`: Lógica principal (scraper y procesador).
* `/data`: Almacenamiento de reportes generados.
* `main.py`: Punto de entrada del programa.

## 🚀 Cómo ejecutarlo
1. **Instala las dependencias:** ```bash
   pip install -r requirements.txt
