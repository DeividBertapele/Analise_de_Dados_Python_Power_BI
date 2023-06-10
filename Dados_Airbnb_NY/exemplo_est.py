import numpy as np
from matplotlib import pyplot as plt


## Exemplos do Desvio Padrão e Hisotgrama:
dados = [8, 9, 4, 2, 2]

# Desvio padrão
desvio_padrao = np.std(dados)
print("O desvio padrão é: {}".format(desvio_padrao))

# Histograma
plt.hist( dados, bins='doane')