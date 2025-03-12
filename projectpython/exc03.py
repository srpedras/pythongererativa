import spacy
# Execute o comando python -m spacy download pt_core_news_sm
# Carregar o modelo de linguagem em português
nlp = spacy.load('pt_core_news_sm')

# Texto para análise
text = "Eu adoro estudar sobre Inteligência Artificial!"

# Processar o texto com o spaCy
doc = nlp(text)

# Mapeamento das siglas de POS para explicações em português
pos_map = {
    'ADJ': 'Adjetivo',
    'ADP': 'Preposição',
    'ADV': 'Advérbio',
    'AUX': 'Verbo auxiliar',
    'CCONJ': 'Conjunção coordenativa',
    'DET': 'Determinante',
    'INTJ': 'Interjeição',
    'NOUN': 'Substantivo',
    'NUM': 'Número',
    'PART': 'Partícula',
    'PRON': 'Pronome',
    'PROPN': 'Substantivo próprio',
    'PUNCT': 'Pontuação',
    'SCONJ': 'Conjunção subordinativa',
    'SYM': 'Símbolo',
    'VERB': 'Verbo',
    'X': 'Outro'
}

# Exibir tokens (palavras) no texto e suas respectivas categorias gramaticais
for token in doc:
    pos_explicado = pos_map.get(token.pos_, 'Categoria desconhecida')
    print(f'{token.text} -> {pos_explicado}')
