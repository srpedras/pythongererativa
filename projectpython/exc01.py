#processamento de linguagem natural

'''
    Bibliotecas nltk e space faz varias coisas entrar com os dados de um texto e chutar o restante, faz analise
    sintatica.


'''

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

text="i like cofee in diner"

sia = SentimentIntensityAnalyzer()

sentiment=sia.polarity_scores(text)

print(sentiment)







