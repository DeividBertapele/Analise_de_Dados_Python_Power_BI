
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Coletar dados para ler uma planilha de dados
df = pd.read_csv(r'AB_NYC_2019.csv')

df.info()


# Calcular a média de todos os valores de aluguel da cidade de Nova York:

# 1- vamos selecionar as colunas
price = df.loc[:, "price"]

# 2 - vamos calcular a média
valor_medio = np.mean(price)

# 3 - Mostrar os valores da média
print("o valor médio é: U${:.2f}".format(valor_medio))


# Contar todos os nomes distintos que aparecem na coluna região:

# 1- Vamos selecionar a coluna região
region = df.loc[:, "neighbourhood_group"]

# 2 - Podemos contar os valores distintos
region_unique = pd.unique(region)
print(region_unique)


# Encontrar o valor máximo e mínimo da coluna que contém os valores dos aluguéis:

# 1- Selecionar as colunas do price
price = df.loc[:, "price"]

# 2- Podemos encontrar o valor máximo e mínimo
val_max = np.max(price)
val_min = np.min(price)

# 3- Mostrar os valores máximos e mínimos
print("o valor máximo é: U${}".format(val_max))
print("o valor mínimo é: U${}".format(val_min))
