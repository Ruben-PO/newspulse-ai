from textblob import TextBlob

def analyze_sentiment(titles):
    results = []
    for title in titles:
        analysis = TextBlob(title)
        # La polaridad va de -1 (negativo) a 1 (positivo)
        sentiment = "Positivo" if analysis.sentiment.polarity > 0 else "Negativo" if analysis.sentiment.polarity < 0 else "Neutro"
        results.append({"noticia": title, "sentimiento": sentiment})
    return results