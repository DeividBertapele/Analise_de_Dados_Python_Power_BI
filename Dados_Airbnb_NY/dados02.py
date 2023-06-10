
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Coletar dados para ler uma planilha de dados
df = pd.read_csv(r'AB_NYC_2019.csv')

df.info()


# Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?

# 1- vamos selecionar as colunas
room_type = df.loc[:, "room_type"]

# 2- Valores distintos
room_type_unique = np.unique(room_type)

print("As categorias são: {}".format(room_type_unique))


## Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?

# 1- vamos selecionar as colunas
host_id = df.loc[:, "host_id"]

# 2- Valores distintos
host_unique = np.unique(host_id)
len(host_unique)


# Como é a variação do preços dos imóveis em NY?

# 1- vamos selecionar as colunas
price = df.loc[:, "price"]

# 2- Valor do desvio padrão
desvio_padrao = np.std(price)
print("Os preços estão disperson em U${:.2f} em torno da média".format(
    desvio_padrao))


# Existem mais imóveis baratos ou caros?

# 1- Selecionar a coluna price e filtrar linhas
linhas = df.loc[:, "price"] < 1250
print(linhas)
price = df.loc[linhas, "price"]
print(price)


# 2 - Desenhar o histograma
plt.hist(price, bins=12)
print("Existem mais de 20.000 imóveis com valor de aluguel.")


# Qual a distribuição do número de Reviews? Existem imóveis com muitos e outro com poucos reviews?

# 1- Selecionar a coluna price e filtrar linhas
linhas = df.loc[:, 'number_of_reviews'] < 500
number_reviews = df.loc[linhas, 'number_of_reviews']

# Histograma
plt.hist(price, bins=12)
print("Existem mais de 30.000 imóveis com valor de aluguel.")
