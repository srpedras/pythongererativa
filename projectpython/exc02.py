import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('punkt')

text="Eu adoro aprender sobre inteligência artificial!"

tokens=word_tokenize(text)

print(tokens)