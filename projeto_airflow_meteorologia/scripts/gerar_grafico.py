import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/dados_unificados.csv')
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['AnoMes'] = df['Data'].dt.to_period('M')
df_temp = df[['AnoMes', 'TEMPERATURA MAXIMA (°C)', 'TEMPERATURA MINIMA (°C)']].dropna()
media = df_temp.groupby('AnoMes').mean(numeric_only=True)

plt.figure(figsize=(12,6))
media.plot(y=['TEMPERATURA MAXIMA (°C)', 'TEMPERATURA MINIMA (°C)'], ax=plt.gca())
plt.title('Evolução da Temperatura')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('data/grafico_temperatura.png')