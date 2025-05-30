import pandas as pd
import os

caminho = 'data'
arquivos = [os.path.join(caminho, f) for f in os.listdir(caminho) if f.endswith('.csv')]

df = pd.concat([pd.read_csv(f, sep=';', encoding='latin1') for f in arquivos], ignore_index=True)
df.to_csv('data/dados_unificados.csv', index=False)