'''import requests
from bs4 import BeautifulSoup

link = 'https://tabelatest.netlify.app/'
dados = requests.get(link)
sopa = BeautifulSoup(dados.text, 'html.parser')

lista = []
for n in sopa.find_all('tr')[1:]:
    for i in n.find_all('td')[3]:
        lista.append(i)
        con = set(lista)
print(con)

#email = [linha.find_all('td')[3].text for linha in sopa.find_all('tr')[1:]]

#print(email)
'''

import requests
from bs4 import BeautifulSoup

link = 'https://gratuitos.netlify.app'
dados = requests.get(link)
sopa = BeautifulSoup(dados.text, 'html.parser')

lista_Cursos = [linha.find('th').text for linha in sopa.find_all('tr')[3:]]
print(lista_Cursos)

lista_Datas = [linha.find('td').text for linha in sopa.find_all('tr')[3:]]
print(lista_Datas)
