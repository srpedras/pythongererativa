import numpy as np
import time
from pyfirmata import Arduino, util

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


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
time.sleep(1)

leitura=[]
rotulos=np.array([])

for i in range(100):
    leitura01=sensor01.read()
    leitura02 = sensor02.read()
    valor01 = int(leitura01 * 1023)
    valor02 = int(leitura02 * 1023)
    if((valor01>=0 and valor01<=525)or(valor02>=0 and valor02<=590)):
        rotulos=np.append(rotulos,0)
    else:
        rotulos = np.append(rotulos, 1)
    leitura.append([valor01,valor02])
    time.sleep(0.5)
Dados=np.array(leitura)
print(f"Dados = {Dados}")
print(f"Rótulos = {rotulos}")

Dados_treino,Dados_teste,Rotulos_Treino,Rotulos_teste=train_test_split(Dados,rotulos,test_size=0.25,random_state=42)
modelo=RandomForestClassifier()
modelo.fit(Dados_treino,Rotulos_Treino)

Previsao_Rotulo=modelo.predict(Dados_teste)
Acuracia=accuracy_score(Rotulos_teste,Previsao_Rotulo)

if Acuracia > 0.80:
    print("O modelo está com uma boa precisão, o que significa que ele é eficaz em prever se os carros serão aprovados ou reprovados.")
else:
    print("O modelo precisa de mais dados ou ajustes para melhorar a sua precisão.")

joblib.dump(modelo,'modelo_rf.pkl')



