import csv
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

import nltk
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer


CSV_FILE = Path(__file__).resolve().parents[1] / "dados_sentimentos.csv"


def run_sentiment_comment_window():
    nltk.download("vader_lexicon")
    analisador_sentimento = SentimentIntensityAnalyzer()

    def salvar_e_analisar_comentario():
        comentario = caixa_texto.get("1.0", "end-1c").strip()

        if not comentario:
            messagebox.showwarning(
                "Comentario vazio",
                "Digite um comentario antes de confirmar.",
            )
            return

        translator = Translator()
        comentario_ingles = translator.translate(
            comentario,
            src="pt",
            dest="en",
        ).text

        sentimento = analisador_sentimento.polarity_scores(comentario_ingles)

        if sentimento["compound"] >= 0.05:
            resultado = "Positivo"
        elif sentimento["compound"] <= -0.05:
            resultado = "Negativo"
        else:
            resultado = "Neutro"

        arquivo_existe = CSV_FILE.exists()

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)

            if not arquivo_existe:
                escritor_csv.writerow(["comentario", "sentimento"])

            escritor_csv.writerow([comentario, resultado])

        messagebox.showinfo(
            "Analise de Sentimentos",
            f"Comentario: {comentario}\nResultado: {resultado}",
        )

    try:
        janela = tk.Tk()
    except tk.TclError as error:
        print("Nao foi possivel abrir a janela grafica.")
        print("Se estiver rodando no Docker, verifique se o DISPLAY esta configurado.")
        print(f"Erro original: {error}")
        return

    janela.title("TecSentimentos")

    mensagem = tk.Label(janela, text="Sua opiniao e importante para nos")
    mensagem.pack()

    caixa_texto = tk.Text(janela, height=5, width=50)
    caixa_texto.pack()

    botao_confirmar = tk.Button(
        janela,
        text="Confirmar",
        command=salvar_e_analisar_comentario,
    )
    botao_confirmar.pack()

    janela.mainloop()


if __name__ == "__main__":
    run_sentiment_comment_window()
