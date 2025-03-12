from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import numpy as np
import time
from pyfirmata import Arduino, util

#Colocar a porta de conexão do Arduino:
porta='COM9'

#Conexão com a placa do Arduino
placa=Arduino(porta)

#Processo de Leitura de Forma Assíncrona
it=util.Iterator(placa)
it.start()

#Definindo os pinos onde os sensores estão ligados no Arduino
sensor01=placa.get_pin('a:0:i')
sensor02=placa.get_pin('a:1:i')

#Inicializando o vetor de armazenamento de dados
Dados=np.array([])
Rotulos=np.array([])

for i in range(5):
    leitura01=sensor01.read()
    leitura02=sensor02.read()

    if leitura01 is not None and leitura02 is not None:

        valor01=int(leitura01*1023)
        valor02=int(leitura02*1023)
        if (valor01<=200 or valor01>=300)or(valor02<=200 or valor02>=300):
            Rotulos=np.append(Rotulos,0)
        else:
            Rotulos = np.append(Rotulos, 1)
            

        #novo_valor=np.array([valor01,valor02])
        Dados=np.append(Dados,[valor01,valor02], axis=0)


    time.sleep(1)
print(f'Dados:{Dados}')
print(f'Rotulos:{Rotulos}')
'''
X_train, X_test, y_train, y_test = train_test_split(Dados, Rotulos, test_size=0.25, random_state=42)


# Treinar um modelo Random Forest para prever se o carro será aprovado ou reprovado
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Fazer previsões sobre os carros de teste
y_pred = model.predict(X_test)

# Avaliar a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)
'''