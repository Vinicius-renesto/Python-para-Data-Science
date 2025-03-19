print('olá seja bem-vindo')
lista_cadastro = []
email_usuario = input('qual é seu login') 
senha_usuario = input('qual é sua senha')
lista_cadastro.append(email_usuario)
lista_cadastro.append(senha_usuario)
lista_notas =[]
for notas in range(3):
  notas = float(input('qual sua nota ? '))
  lista_notas.append (notas)
  nota =  sum(lista_notas)
resultado = nota/len(lista_notas)
if resultado >= 7 :
    print('você foi aprovado com',resultado)
elif resultado <= 6.9 and 5:
    print('você está de recuperação',resultado)
elif resultado <= 4.9 :
    print('você foi reprovado',resultado)


# Mesma coisa que o de cima, forma diferente 
print('olá seja bem-vindo')
lista_cadastro = []
email_usuario = input('qual é seu login') 
senha_usuario = input('qual é sua senha')
lista_cadastro.append(email_usuario)
lista_cadastro.append(senha_usuario)
lista_notas =[]
notas = float(input('qual sua maior nota ? '))
lista_notas.append(notas)
notas1 = float(input('qual sua menor nota ? '))
lista_notas.append(notas1)
notas2 = float(input('qual sua nota mediana ? '))  
lista_notas.append(notas2)
resultado = (lista_notas[0] + lista_notas[1] + lista_notas[2]) / 3
print(' Sua media foi de',resultado)
print('sua maior nota foi de',lista_notas[0])
print('sua menor nota foi de',lista_notas[1])



print('vamos fazer uma calculadora de IMC')
peso = float(input('qual seu peso ? '))
altura = float(input('qual é sua altura ? '))
calculadora = peso / ( altura ** 2)
print(calculadora <= 18.5 ,'abaixo do peso')
print(calculadora > 18.5 and calculadora < 24.9 ,'sobrepeso')
print(calculadora > 25 and calculadora < 29.9,'sobrepeso')
print(calculadora > 30 and calculadora < 34.9,'obesidade grau 1')
print(calculadora > 35 and calculadora <39.9,'obesidade grau 2')
print(calculadora >= 40 ,'obesidade grau 3


