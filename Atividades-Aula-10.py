import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
import statistics 

'''# Exercício 1

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)


def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)


def varianca1(lista):
    if len(lista) > 1:
        return statistics.variance(lista)
    else:
        return 0 

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')


def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
    return media  # Agora retorna a média calculada
 

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

def handle(lista, salarios):
    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)

handle(empresa1, empresa1)  
handle(empresa2, empresa2)   
handle(empresa3, empresa3) 
handle(empresa4, empresa4)

# Agora, as médias são corretamente armazenadas nas variáveis
media_empresa1 = media1(empresa1)
media_empresa2 = media1(empresa2)
media_empresa3 = media1(empresa3)
media_empresa4 = media1(empresa4)

medias = [media_empresa1, media_empresa2, media_empresa3, media_empresa4]

empresas = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']

# Gráfico de barras
plt.bar(empresas, medias, color='purple')
plt.title('Cargos e Salarios das Empresas')
plt.xlabel('Cargos')
plt.ylabel('Salarios')
plt.show()


enter=input('enter para sair')


# Exercício 2
x = [2021,2022,2023,2024,2025,2026] # Ano
y = [10000,2000,30000,10000,5000,20000] # Vendas

plt.plot(x, y)
plt.show()

# Exercício 3

x_barras = [10,5,8,9,10,5,4] # Medias de José
y_barras = ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto'] # Meses

plt.bar(x_barras,y_barras)
plt.show()'''

# Exercício 4



root = tk.Tk()
root.title('Gerar Grafico')
root.geometry('2050x1700')

text_1 = tk.Label(root, text = 'Insira um dado :')
text_1.grid(row=0,column=1,padx=5,pady=5)

entry_dados = tk.Entry(root,width = 10)
entry_dados.grid(row=0,column=2,padx=5,pady=5)

entry_dados1 = tk.Entry(root,width = 10)
entry_dados1.grid(row=0,column=3,padx=5,pady=5)

entry_dados2 = tk.Entry(root,width = 10)
entry_dados2.grid(row=0,column=4,padx=5,pady=5)

media_label = tk.Label(root, text = 'X')
media_label.grid(row=3,column=1,padx=5,pady=5)

moda_label = tk.Label(root, text = 'X')
moda_label.grid(row=4,column=1,padx=5,pady=5)

mediana_label = tk.Label(root, text = 'X')
mediana_label.grid(row=5,column=1,padx=5,pady=5)

btn = tk.Button(root, text = 'Gerar')
btn.grid(row=7,column=1,padx=5,pady=5)




root.mainloop()