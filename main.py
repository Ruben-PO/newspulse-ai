from core.scraper import fetch_tech_news
from core.processor import analyze_sentiment
import pandas as pd

def run_engine():
    print("🚀 Iniciando NewsPulse-AI...")
    
    # 1. Extracción
    print("🔍 Extrayendo noticias de Hacker News...")
    news = fetch_tech_news()
    
    # 2. Procesamiento
    print("🧠 Analizando tendencias con IA...")
    data = analyze_sentiment(news)
    
    # 3. Guardado
    df = pd.DataFrame(data)
    df.to_csv("data/reporte_diario.csv", index=False)
    print("✅ Reporte generado en data/reporte_diario.csv")
    print(df)

if __name__ == "__main__":
    run_engine()