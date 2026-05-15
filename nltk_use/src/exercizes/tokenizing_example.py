import nltk 
from nltk.tokenize import word_tokenize

def tokenize_example(text):
    nltk.download('punkt')

    tokens = word_tokenize(text)

    print(tokens)

if __name__ == "__main__":
    text = input("Qual texto gostaria de tokenizar? ")
    tokenize_example(text)
