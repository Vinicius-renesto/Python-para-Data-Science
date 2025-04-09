import matplotlib.pyplot  as plt
import numpy as np
import pandas as pd
 

'''x = [1,2,4,6,8]
y = ['a','b','c','d','e']

plt.bar(x,y)
plt.title('Barras')
plt.show()

# linhas

plt.plot(x,y)
plt.title('Linhas')
plt.show()

# pizzas

plt.pie(x,labels=y)
plt.show()

# dispersão 

y =[1,6,9,89,3]
plt.scatter(x,y,marker='o')
plt.show()

# histograma

plt.hist(x,bins=7)
plt.show()'''

x = np.linspace(0,10,100)
y = np.sin(x)

# Plotar o grafico de linha 

'''plt.plot(x, y, color = 'blue', linestyle = '--', label = 'sin(x)')
plt.title('Grafico de linhas')
plt.xlabel('Tempo em dias')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()'''


# ----------

# Grafico de barras-

'''i = ['maça','melancia','banana','amora','amexa']
n = [25, 30, 12, 15, 20]
plt.bar(i, n, color = ['green', 'red', 'yellow', 'blue', 'purple'])

plt.show()
'''


'''dados = pd.read_csv('teste.csv')
x = dados [ 'nome' ]
y = dados [ 'Idade' ]
df = pd.DataFrame (dados)
print(df)

plt.plot(x ,y)
plt.show()
'''




'''
x = np.random.rand(50) * 100
y = x * 0 + np.random.rand(50) * 10

df2 = pd.DataFrame(x)
df = pd.DataFrame(y)
print(df)

plt.scatter(x, y, color = 'purple')
plt.show()


plt.hist(x, bins = 10, edgecolor = 'red')

plt.show()'''