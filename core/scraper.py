import requests
from bs4 import BeautifulSoup

def fetch_tech_news():
    # Usaremos un sitio de noticias como ejemplo
    url = "https://news.ycombinator.com/" 
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscamos los títulos de las noticias
        titles = [span.text for span in soup.select(".titleline > a")]
        return titles[:10]  # Devolvemos solo los 10 primeros
    except Exception as e:
        print(f"Error al extraer noticias: {e}")
        return []