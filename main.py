import asyncio
from googletrans import Translator

file = input("Enter file name: ")

with open(file+'.txt', 'r', encoding='utf-8') as f:
    raw_text = f.read()

translator = Translator()


async def main():
    original_language = input("Enter language: ")

    language = await translator.detect(raw_text)
    translation = await translator.translate(raw_text, src=language.lang, dest=original_language)
    print(translation.text)

if __name__ == "__main__":
    asyncio.run(main())
