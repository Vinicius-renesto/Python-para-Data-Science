import sqlite3 
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox

conexao = sqlite3.connect('Banco.db')          
cursor = conexao.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, 
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
        )                     
''')

conexao.commit()

def inserir_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()
    
    if nome and idade and cidade:
        
        cursor.execute('''
        INSERT INTO pessoas(nome, idade, cidade)
        VALUES(?, ?, ?)               
    ''',(nome, int(idade), cidade))
        conexao.commit()
        messagebox.showinfo('Ok', 'Dados inseridos')
        entrada_cidade.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_nome.delete(0, tk.END)
        
    else:
        messagebox.showerror('Erro','Ocorreu um erro')
    


def exibir_grafico():
    cursor.execute('SELECT nome, idade FROM pessoas')
    dados = cursor.fetchall()
    if dados:
        nomes = [dado[0] for dado in dados]
        idade = [dado[1] for dado in dados]
        plt.figure(figsize=(10,5))
        plt.bar(nomes, idade, color = 'red')
        plt.show()
    else:
        messagebox.showerror('Erro','Ocorreu um erro')   

janela = tk.Tk()

janela.title('DADOS')

tk.Label(janela, text= 'Nome').grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text= 'Idade').grid(row=1, column=0, padx=5, pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text= 'Cidade').grid(row=2, column=0, padx=5, pady=5)
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=2, column=1, padx=10, pady=5)

btn_inserir = tk.Button(janela, text='Inserir',  command= inserir_dados)
btn_inserir.grid(row=3, column=1, padx=10, pady=5)

btn_grafico = tk.Button(janela, text='Gerar grafico', command= exibir_grafico)
btn_grafico.grid(row=4, column=1, padx=10, pady=5)

janela.mainloop()