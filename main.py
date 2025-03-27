
# Exercício 1


def medias () :
 lista_valor = []
 quantidades = int(input('Me fala a quantidade de número vai ter ? '))
 for media in range(quantidades):
    media = int(input('Qual é o valor ? '))
    lista_valor.append(media)
    soma = sum(lista_valor)
 resultado = soma / len(lista_valor)
 print('Sua media será de', resultado)
    
medias ()

# Exercício 2


def IMC (): 
    peso = int(input('Qual seu peso ? '))
    altura = float(input('Qual sua altura ? '))
    IMC = peso / (altura ** 2)
    if IMC > 18.50: 
        print( IMC, 'Abaixo do peso')
    elif IMC >= 18.50 and IMC <= 24.99:
        print(IMC, 'Peso normal')
    elif IMC >= 25.00 and IMC <= 29.99:
        print(IMC, 'Sobrepeso')
    elif IMC >= 30.00 and IMC <= 34.99:
          print(IMC, 'Obesidade grau I')
    elif IMC >= 35.00 and IMC <= 39.99:
        print(IMC, 'Obesidade grau II')
    elif IMC >= 40.00:
        print(IMC, 'Obesidade grau III')

IMC ()

# Exercício 3

import random 

def adv ():
    aleatorio = random.randint(1, 30)
    print('você terá 3 chances ! ')
    for tentativa in range(3):
        tentativa = int(input('Qual o número que você chuta ? '))
        if tentativa == aleatorio:
            print('Parabéns você acertou ')
            break
        elif tentativa != aleatorio :
            print('Tente novamente ')
        else :
            print('Você perdeu')
            break
            
adv()
