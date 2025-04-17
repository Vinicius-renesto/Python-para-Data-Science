import pandas as pd
import matplotlib.pyplot as plt

# Criar uma Series
data = pd.Series([1, 3, 5, 7, 9])

# Criar um DataFrame
data = {'Nome': ['Ana', 'Bob', 'Catarina', 'Daniel'],
        'Idade': [23, 35, 45, 27],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}
df = pd.DataFrame(data)
print(df)

df.to_csv('dados.csv')

# 2 leitura de Dados de Arquivos
# 3 Visualização de Dados
# 4 eleção e Indexação
# 5 Filtragem de Dados
# 6. Manipulação de Dados

