import pandas as pd
import matplotlib.pyplot as plt

# Carregar o DataFrame a partir do CSV
dados = pd.read_csv('dado.csv')

# Exibir os dados para conferirmos
print(dados)

# Gráfico 1: Gráfico de Barras (Lucros e Vendas)
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(dados['Mês'], dados['Lucros'], color='red', width=0.4, label='Lucros')
ax1.set_ylabel('Lucros', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.set_xlabel('Mês')

ax2 = ax1.twinx()
ax2.plot(dados['Mês'], dados['Vendas'], 'b-o', label='Vendas')
ax2.set_ylabel('Vendas', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

ax1.set_title('Lucros (barras) e Vendas (linha) por Mês')
fig.tight_layout()
plt.show()

# Gráfico 2: Gráfico de Linha (Lucros e Vendas ao longo do tempo)
plt.figure(figsize=(10, 6))
plt.plot(dados['Mês'], dados['Lucros'], 'r-o', label='Lucros')
plt.plot(dados['Mês'], dados['Vendas'], 'b-o', label='Vendas')
plt.xlabel('Mês')
plt.ylabel('Valores')
plt.title('Lucros e Vendas ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 3: Gráfico de Pizza (Distribuição de Vendas e Lucros por Mês)
plt.figure(figsize=(8, 6))
# Plotando a distribuição dos lucros
plt.pie(dados['Lucros'], labels=dados['Mês'], autopct='%1.1f%%', colors=plt.cm.Reds(range(len(dados['Mês']))))
plt.title('Distribuição dos Lucros por Mês')
plt.show()

# Gráfico 4: Gráfico de Dispersão (Relação entre Lucros e Vendas)
plt.figure(figsize=(10, 6))
plt.scatter(dados['Lucros'], dados['Vendas'], color='purple')
plt.xlabel('Lucros')
plt.ylabel('Vendas')
plt.title('Relação entre Lucros e Vendas')
plt.show()
