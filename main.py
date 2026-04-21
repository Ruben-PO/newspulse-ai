def run_engine():
    print("🚀 Iniciando NewsPulse-AI...")
    
    try:
        # 1. Extracción
        print("🔍 Extrayendo noticias de Hacker News...")
        news = fetch_tech_news()
        
        if not news:
            print("⚠️ No se encontraron noticias. Revisa tu conexión a internet.")
            return
        
        # 2. Procesamiento
        print("🧠 Analizando tendencias con IA...")
        data = analyze_sentiment(news)
        
        # 3. Guardado
        df = pd.DataFrame(data)
        df.to_csv("data/reporte_diario.csv", index=False)
        print("✅ Reporte generado en data/reporte_diario.csv")
        print(df)

    except Exception as e:
        print(f"❌ ¡Ups! Algo salió mal: {e}")

if __name__ == "__main__":
    run_engine()
