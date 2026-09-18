# 🚀 NewsPulse-AI

Sistema automatizado en **Python** para el seguimiento y análisis de tendencias tecnológicas.

## 🛠️ ¿Qué hace este proyecto?
* **Web Scraping:** Extrae los últimos titulares de *Hacker News*.
* **Inteligencia Artificial (NLP):** Analiza el sentimiento de cada noticia (Positivo/Neutro/Negativo) usando la librería `TextBlob`.
* **Data Logging:** Genera un reporte automático en formato `.csv` en la carpeta `/data` con los hallazgos del día.

## 📦 Tecnologías utilizadas
* **Lenguaje:** Python 3.12
* **Librerías:**
    * `Pandas` (Gestión de datos)
    * `BeautifulSoup4` (Extracción web)
    * `TextBlob` (Procesamiento de lenguaje natural)
    * `Requests` (Peticiones HTTP)

## 📂 Estructura del Proyecto
* `/core`: Lógica principal (scraper y procesador).
* `/data`: Almacenamiento de reportes generados.
* `main.py`: Punto de entrada del programa.

## 🚀 Cómo ejecutarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Ruben-PO/newspulse-ai.git
   cd newspulse-ai

2. Instala las dependencias:
pip install -r requirements.txt
3. Ejecuta el programa:
python main.py
4. Revisa el resultado en /data, donde se genera un .csv con los titulares extraídos y su sentimiento asociado.

📄 Licencia

Este proyecto está bajo la licencia MIT — consulta el archivo LICENSE para más detalles.
