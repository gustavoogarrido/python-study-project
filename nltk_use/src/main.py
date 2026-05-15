from exercizes.comment_window import run_comment_window
from exercizes.sentiment_comment_window import run_sentiment_comment_window
from exercizes.tokenizing_example import tokenize_example
from exercizes.w_translation import run_analisys


EXERCIZES = [
    {
        "function": tokenize_example,
        "input_message": "Qual texto gostaria de tokenizar? ",
    },
    {
        "function": run_analisys,
        "input_message": "Qual texto gostaria de fazer a análise de sentimentos? ",
    },
    {
        "function": run_comment_window,
    },
    {
        "function": run_sentiment_comment_window,
    },
]


def get_exercize_name(exercize):
    return exercize["function"].__module__.split(".")[-1]


def main():
    exercizes_options = [
        f"{index}- {get_exercize_name(exercize)}"
        for index, exercize in enumerate(EXERCIZES, start=1)
    ]
    menu_text = "Exercícios disponíveis:\n" + "\n".join(exercizes_options)

    print(menu_text)
    decision = input("Qual exercicio voce quer rodar? (1, 2...)? ")

    try:
        selected_exercize = EXERCIZES[int(decision) - 1]
    except (ValueError, IndexError):
        print("Exercício inválido")
        return

    if "input_message" in selected_exercize:
        text = input(selected_exercize["input_message"])
        selected_exercize["function"](text)
    else:
        selected_exercize["function"]()


if __name__ == "__main__":
    main()
