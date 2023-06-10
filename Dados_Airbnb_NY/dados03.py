
import pandas as pd
from matplotlib import pyplot as plt
import folium

# Coletar dados para ler uma planilha de dados
df = pd.read_csv(r'AB_NYC_2019.csv')
df.info()


# 1- Selecionando as linhas e colunas
colunas = ['price', 'neighbourhood_group', 'latitude', 'longitude']
colunas_groupby = ['neighbourhood_group']

print(colunas_groupby)

# 2- Criando os segmentos
df_plot = df.loc[:, colunas].groupby(colunas_groupby).max().reset_index()
print(df_plot)


# Gráficos
f = folium.Figure(width=1024, height=768)

map = folium.Map(
    location=[
        df_plot['latitude'].mean(),
        df_plot['longitude'].mean(),
    ],
    zoom_start=12,
    control_scale=True
)

# Adicionando os pinos nos mapas

for index, location_info in df_plot.iterrows():
    folium.Marker([
        location_info['latitude'],
        location_info['longitude']
    ], popup=location_info['neighbourhood_group']).add_to(map)

map