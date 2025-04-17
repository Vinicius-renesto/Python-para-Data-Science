import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')
print(dados)

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(dados['Nome'], dados['Idade'], color='red', width=0.4, label='Idade')
ax1.set_ylabel('Idade', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.set_xlabel('Nome')

ax2 = ax1.twinx()
ax2.plot(dados['Nome'], dados['Cidade'], 'b-o', label='Cidade')
ax2.set_ylabel('Cidade', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

ax1.set_title('Idade (barras) e Cidade (linha) por Nome')
fig.tight_layout()
plt.show()
print()

x = 'idade'
print(x)
idades = dados['Idade']
print(idades)
print()

y = 'Filtragem'
print(y)
filtro = dados[dados['Idade']<30]
print(filtro)
print()

z = 'Manipulação de dados'
print(z)
df = dados.drop('Cidade', axis=1)
print(df)


