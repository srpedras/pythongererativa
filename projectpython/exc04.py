from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Exemplo com dados fictícios, com base na indústria automobilística
# X = [potência do motor, peso da carroceria]
X = [[150, 1200], [180, 1300], [200, 1400], [170, 1250]]  # Atributos de carros
y = [0, 1, 0, 1]  # Rótulos (0 = reprovado, 1 = aprovado no controle de qualidade)

# Dividir os dados em treino e teste (75% para treino, 25% para teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Treinar um modelo Random Forest para prever se o carro será aprovado ou reprovado
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Fazer previsões sobre os carros de teste
y_pred = model.predict(X_test)

# Avaliar a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia:.2f}")

# Interpretação do resultado
if acuracia > 0.80:
    print("O modelo está com uma boa precisão, o que significa que ele é eficaz em prever se os carros serão aprovados ou reprovados.")
else:
    print("O modelo precisa de mais dados ou ajustes para melhorar a sua precisão.")


