import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import tkinter as tk


link = 'https://bea3853.github.io/site/'
dados = requests.get(link)
sopa = BeautifulSoup(dados.text, 'html.parser')
dado = sopa.find_all('span')
dado2 = sopa.find_all('h2', class_='nome')


def extrair_nome():
    global nome 
    nome = []
    for n in dado2:
        i =  n.text
        nome.append(i)
        print(nome)
        nomes.config(text = nome) 
        return nomes

def extrai_valor():
    nome = []
    for n in dado2:
        i =  n.text
        nome.append(i)
        print(nome)
        nomes.config(text = nome) 
       
    l = []
    for i in dado:
        l.append(i.text)
        l = [valor.replace('R$','').strip() for valor in l]
        l.sort()
        print(l)
        valores.config(text= l)
        d = [float(i) for i in l]
        plt.bar(nome,d)
        plt.show() 


 
      
        

janela = tk.Tk()





btn_valores = tk.Button(janela, text='clique', command=extrai_valor)
btn_valores.pack()
btn_nomes = tk.Button(janela, text='clique', command=extrair_nome)
btn_nomes.pack()

valores = tk.Label(janela)
valores.pack()



nomes = tk.Label(janela)
nomes.pack()

janela.mainloop()
