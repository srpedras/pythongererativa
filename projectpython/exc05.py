import numpy as np
import time
from pyfirmata import Arduino, util

# colocar a porta de conexão do Arduino:
porta = 'COM8'

# conexão com a placa do Arduino
placa = Arduino(porta)

# Processo de leitura de forma Assicrona
it=util.Iterator(placa)
it.start()

# Definindo os pinos onde os sensores estão ligados no Arduino
sensor01 = placa.get_pin('a:0:i')
sensor02 = placa.get_pin('a:1:i')

# Iniciando o vetor de armazenamento de dados
Dados=np.array({})

try:
    while True:
        leitura01 = sensor01.read()
        leitura02 = sensor02.read()
        if leitura01 is not None and leitura02 is not None:
            valor1=int(leitura01*1023)
            valor2=int(leitura02*1023)

            novo_valor=np.array({valor1,valor2})
            Dados=np.append(Dados, novo_valor, axis=0)
            print(f'Valor 01:{valor1}: Valor 02:{valor2}.')
            print(f'Dados:{Dados}')
        time.sleep(5)
except KeyboardInterrupt:
    print('Programa Finalizado')
    placa.exit()


