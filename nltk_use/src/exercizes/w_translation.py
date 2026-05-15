import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator


def run_analisys(text):
    # Baixa modelo
    nltk.download('vader_lexicon')

    # Objeto de analise de sentimento, com a definição do texto a ser analisado
    analisador_sentimento = SentimentIntensityAnalyzer()
    text_sample = text

    # Traduz o texto para inglês para melhorar a tokenização
    translator = Translator()
    texto_ingles = translator.translate(text_sample, src='pt', dest='en')

    # Realiza a análise de sentimento
    sentimento = analisador_sentimento.polarity_scores(texto_ingles.text)

    resultado = ""

    if sentimento['compound'] >= 0.05:
        resultado = "Sentimento positivo"
    elif sentimento['compound'] <= -0.05:
        resultado = "Sentimento negativo"
    else:
        resultado = "Sentimento neutro"

    print(f'sentimento={sentimento}')
    print(f'resultado={resultado}')


if __name__ == "__main__":
    run_analisys("Eu gostei muito desse exemplo")
