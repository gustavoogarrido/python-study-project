import tkinter as tk
from tkinter import messagebox


def run_comment_window():
    def confirmar_comentario():
        comentario = caixa_texto.get("1.0", "end-1c")
        messagebox.showinfo(
            "Comentario Confirmado",
            f"Obrigado pelo seu comentario:\n{comentario}",
        )

    try:
        janela = tk.Tk()
    except tk.TclError as error:
        print("Nao foi possivel abrir a janela grafica.")
        print("Se estiver rodando no Docker, verifique se o DISPLAY esta configurado.")
        print(f"Erro original: {error}")
        return

    janela.title("TecSentimentos")

    titulo = tk.Label(janela, text="TecSentimentos", font=("Helvetica", 16))
    titulo.pack()

    mensagem = tk.Label(janela, text="Sua opiniao e importante para nos")
    mensagem.pack()

    caixa_texto = tk.Text(janela, height=5, width=50)
    caixa_texto.pack()

    botao_confirmar = tk.Button(
        janela,
        text="Confirmar",
        command=confirmar_comentario,
    )
    botao_confirmar.pack()

    janela.mainloop()


if __name__ == "__main__":
    run_comment_window()
