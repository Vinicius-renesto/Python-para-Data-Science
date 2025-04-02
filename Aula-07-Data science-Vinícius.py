import funcoes as fc

# ampliude: 


dicionario_salario = {
   'empresa1' : [2500, 2800, 3000, 9500, 12000],
    'empresa2' : [5000, 5200, 5300, 5400, 5500],
    'empresa3' : [1000, 2000, 8000, 15000, 20000],
    'empresa4' : [3500, 4000, 4200, 4300, 6000],
    'empresa5' : [1200, 1500, 1800, 2500, 10000],
}

salarios = []
v  = []
total_salario  = []
for etiquetas, s in dicionario_salario.items():
        for x in s:
            total_salario.append(x)


print(total_salario)
soma = sum(total_salario)
print('Total de salarios de todas as empresas: ', soma)

lista_empresa1 = [x for x in dicionario_salario['empresa1']]
lista_empresa2 = [x for x in dicionario_salario['empresa2']]
lista_empresa3 = [x for x in dicionario_salario['empresa3']]
lista_empresa4 = [x for x in dicionario_salario['empresa4']]
lista_empresa5 = [x for x in dicionario_salario['empresa5']]

# amplitude  = max(frequencia) - min(frequencia)
def display():
    print('Media de todos os alunos:')
    
    media = fc.media(total_salario)
    print(media)
    
    print('aluno 1')
    media_empresa1  =  fc.media(lista_empresa1)
    print( media_empresa1)
    
    print('aluno 2')
    media_empresa2  =  fc.media(lista_empresa2)
    print( media_empresa2)
    
    print('aluno 3')
    media_empresa3  =  fc.media(lista_empresa3)
    print( media_empresa3)
    
    print('aluno 4')
    media_empresa4  =  fc.media(lista_empresa4)
    print( media_empresa4)
    
    print('aluno 5')
    media_empresa5  =  fc.media(lista_empresa5)
    print( media_empresa5)
    
    print('Mediana total de notas:')
    mediana = fc.mediana(total_salario)
    print(mediana)
    
    print('Mediana de cada aluno:')
    
    print('aluno 1')
    mediana_empresa1   =  fc.mediana(lista_empresa1)
    print( mediana_empresa1)
    
    print('aluno 2')
    mediana_empresa2  =  fc.mediana(lista_empresa2)
    print( mediana_empresa2)
    
    print('aluno 3')
    mediana_empresa3  =  fc.mediana(lista_empresa3)
    print( mediana_empresa3)
    
    print('aluno 4')
    mediana_empresa4  =  fc.mediana(lista_empresa4)
    print( mediana_empresa4)
    
    print('aluno 5')
    mediana_empresa5  =  fc.mediana(lista_empresa5)
    print( mediana_empresa5)
    
    print('Moda total de notas:')
    moda = fc.moda(total_salario)
    print(moda)
    
    print('Moda de cada aluno:')
    
    print('aluno 1')
    moda_empresa1  =  fc.moda(lista_empresa1)
    print( moda_empresa1)
    
    print('aluno 2')
    moda_empresa2  =  fc.moda(lista_empresa2)
    print( moda_empresa2)
    
    print('aluno 3')
    moda_empresa3  =  fc.moda(lista_empresa3)
    print( moda_empresa3)
    
    print('aluno 4')
    moda_empresa4  =  fc.moda(lista_empresa4)
    print( moda_empresa4)
    
    print('aluno 5')
    moda_empresa5  =  fc.moda(lista_empresa5)
    print( moda_empresa5)
    
    print('Amplitude total de salarios: ')

    amplitude = fc.amplitude(total_salario)
    print(amplitude)

    print('Amplitude por mês:')

    print('empresa 1')
    amplitude_empresa1  =  fc.amplitude(lista_empresa1)
    print(amplitude_empresa1)

    print('empresa 2')
    amplitude_empresa2 =  fc.amplitude(lista_empresa2)
    print(amplitude_empresa2)

    print('empresa 3') 
    amplitude_empresa3 =  fc.amplitude(lista_empresa3)
    print(amplitude_empresa3)
    
    print('empresa 4') 
    amplitude_empresa4 =  fc.amplitude(lista_empresa4)
    print(amplitude_empresa4)
    
    print('empresa 5') 
    amplitude_empresa5 =  fc.amplitude(lista_empresa5)
    print(amplitude_empresa5)

    print('***' * 30)
     
    print('Variância total: ')

    variancia_total = fc.variancia(total_salario)
    print('Variância total', variancia_total)


    print('empresa 1')
    v_j =  fc.variancia(lista_empresa1)
    print('Variância: ', v_j)

    print('empresa 2')
    v_j =  fc.variancia(lista_empresa2)
    print('Variância: ', v_j)

    print('empresa 3')
    v_j =  fc.variancia(lista_empresa3)
    print('Variância: ', v_j)
    
    print('empresa 4')
    v_j =  fc.variancia(lista_empresa4)
    print('Variância: ', v_j)
    
    print('empresa 5')
    v_j =  fc.variancia(lista_empresa5)
    print('Variância: ', v_j)

    print('***'*30)

    print('Desvio padrão')
    
    d_total = fc.desvio_padrao(total_salario)
    print('DesvioTotal: ', d_total)


    print('Desvio totais')


    d_empresa1 =  fc.desvio_padrao(lista_empresa1)
    d_empresa2 =  fc.desvio_padrao(lista_empresa2)
    d_empresa3 =  fc.desvio_padrao(lista_empresa3)
    d_empresa4 =  fc.desvio_padrao(lista_empresa4)
    d_empresa5 =  fc.desvio_padrao(lista_empresa5)
    
    print(f'''

    empresa 1 - {d_empresa1}
    empresa 2 - {d_empresa2}
    empresa 3 - {d_empresa3}
    empresa 4 - {d_empresa4}
    empresa 5 - {d_empresa5}


''')


display()

# Qual empresa escolheria?
# Escollheria  Empresa 2

# Porquê?
#Escolhi a Empresa 2 porque ela tem a menor amplitude, variância e desvio padrão, o que significa que os salários são mais estáveis

# O que você entendeu do desvio padrão, média, moda, mediana, amplitude,  variância dessa empresa? 
#A Empresa 2 oferece salários estáveis, com pouca variação 

# Desafio 2

import funcoes as fc
# ampliude: 


dicionario_notas = {
   'aluno 1' : [10, 8, 6, 10, 9],
    'aluno 2' : [10, 2, 4, 8, 9],
    'aluno 3' : [10, 0, 4, 9, 9],
    'aluno 4' : [9, 10, 9, 3, 7],
    'aluno 5' : [0, 0, 0, 0, 0],
}

notas = []
v1  = []
total_notas  = []
for etiquetas, n in dicionario_notas.items():
        for x1 in n:
            total_notas.append(x1)


print(total_notas)
soma = sum(total_notas)
print('Total de notas dos alunos: ', soma)

lista_aluno1 = [x for x in dicionario_notas['aluno 1']]
lista_aluno2 = [x for x in dicionario_notas['aluno 2']]
lista_aluno3 = [x for x in dicionario_notas['aluno 3']]
lista_aluno4 = [x for x in dicionario_notas['aluno 4']]
lista_aluno5 = [x for x in dicionario_notas['aluno 5']]

# amplitude  = max(frequencia) - min(frequencia)
def display():
    print('Media de todos os alunos:')
    
    media = fc.media(total_notas)
    print(media)
    
    print('aluno 1')
    media_aluno1  =  fc.media(lista_aluno1)
    print( media_aluno1)
    
    print('aluno 2')
    media_aluno2  =  fc.media(lista_aluno2)
    print( media_aluno2)
    
    print('aluno 3')
    media_aluno3  =  fc.media(lista_aluno3)
    print( media_aluno3)
    
    print('aluno 4')
    media_aluno4  =  fc.media(lista_aluno4)
    print( media_aluno4)
    
    print('aluno 5')
    media_aluno5  =  fc.media(lista_aluno5)
    print( media_aluno5)
    
    print('Mediana total de notas:')
    mediana = fc.mediana(total_notas)
    print(mediana)
    
    print('Mediana de cada aluno:')
    
    print('aluno 1')
    mediana_aluno1  =  fc.mediana(lista_aluno1)
    print( mediana_aluno1)
    
    print('aluno 2')
    mediana_aluno2  =  fc.mediana(lista_aluno2)
    print( mediana_aluno2)
    
    print('aluno 3')
    mediana_aluno3  =  fc.mediana(lista_aluno3)
    print( mediana_aluno3)
    
    print('aluno 4')
    mediana_aluno4  =  fc.mediana(lista_aluno4)
    print( mediana_aluno4)
    
    print('aluno 5')
    mediana_aluno5  =  fc.mediana(lista_aluno5)
    print( mediana_aluno5)
    
    print('Moda total de notas:')
    moda = fc.moda(total_notas)
    print(moda)
    
    print('Moda de cada aluno:')
    
    print('aluno 1')
    moda_aluno1  =  fc.moda(lista_aluno1)
    print( moda_aluno1)
    
    print('aluno 2')
    moda_aluno2  =  fc.moda(lista_aluno2)
    print( moda_aluno2)
    
    print('aluno 3')
    moda_aluno3  =  fc.moda(lista_aluno3)
    print( moda_aluno3)
    
    print('aluno 4')
    moda_aluno4  =  fc.moda(lista_aluno4)
    print( moda_aluno4)
    
    print('aluno 5')
    moda_aluno5  =  fc.moda(lista_aluno5)
    print( moda_aluno5)
    
    print('Amplitude total de notas: ')

    amplitude = fc.amplitude(total_notas)
    print(amplitude)

    print('Amplitude por mês:')

    print('aluno 1')
    amplitude_aluno1  =  fc.amplitude(lista_aluno1)
    print(amplitude_aluno1)

    print('aluno 2')
    amplitude_aluno2 =  fc.amplitude(lista_aluno2)
    print(amplitude_aluno2)

    print('aluno 3') 
    amplitude_aluno3 =  fc.amplitude(lista_aluno3)
    print(amplitude_aluno3)
    
    print('aluno 4') 
    amplitude_aluno4 =  fc.amplitude(lista_aluno4)
    print(amplitude_aluno4)
    
    print('aluno 5') 
    amplitude_aluno5 =  fc.amplitude(lista_aluno5)
    print(amplitude_aluno5)

    print('***' * 30)
     
    print('Variância total: ')

    variancia_total = fc.variancia(total_notas)
    print('Variância total', variancia_total)


    print('aluno 1')
    v_j =  fc.variancia(lista_aluno1)
    print('Variância: ', v_j)

    print('aluno 2')
    v_j =  fc.variancia(lista_aluno2)
    print('Variância: ', v_j)

    print('aluno 3')
    v_j =  fc.variancia(lista_aluno3)
    print('Variância: ', v_j)
    
    print('aluno 4')
    v_j =  fc.variancia(lista_aluno4)
    print('Variância: ', v_j)
    
    print('aluno 5')
    v_j =  fc.variancia(lista_aluno5)
    print('Variância: ', v_j)

    print('***'*30)

    print('Desvio padrão')
    
    d_total = fc.desvio_padrao(total_notas)
    print('DesvioTotal: ', d_total)


    print('Desvios totais ')


    d_aluno1 =  fc.desvio_padrao(lista_aluno1)
    d_aluno2 =  fc.desvio_padrao(lista_aluno2)
    d_aluno3 =  fc.desvio_padrao(lista_aluno3)
    d_aluno4 =  fc.desvio_padrao(lista_aluno4)
    d_aluno5 =  fc.desvio_padrao(lista_aluno5)
    
    print(f'''

    aluno 1 - {d_aluno1}
    aluno 2 - {d_aluno2}
    aluno 3 - {d_aluno3}
    aluno 4 - {d_aluno4}
    aluno 5 - {d_aluno5}


''')
    print('Maior nota:')
    maior_nota = max(total_notas)
    print(maior_nota)
    
    print('Menor nota:')
    menor_nota = min(total_notas)
    print(menor_nota)
    
    

display()
