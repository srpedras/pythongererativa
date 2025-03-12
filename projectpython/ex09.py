import numpy as np
import time
from pyfirmata import Arduino, util
import joblib
modelo=joblib.load('modelo_rf.pkl')
porta='COM9'
placa=Arduino(porta)
it=util.Iterator(placa)
it.start()
sensor01=placa.get_pin('a:0:i')
sensor02=placa.get_pin('a:1:i')
time.sleep(1)
leitura=[]
rotulos=np.array([])

def LerDados():
    leitura01 = sensor01.read()
    leitura02 = sensor02.read()
    valor01 = int(leitura01 * 1023)
    valor02 = int(leitura02 * 1023)
    print(f"Iluminação: {valor02}. Potenciometro: {valor01}")
    return np.array([valor01,valor02])

def PreverDados():
    dados=LerDados()
    previsao=modelo.predict([dados])
    print(f"Previsão: {previsao[0]}")

while True:
    PreverDados()
    time.sleep(1)


