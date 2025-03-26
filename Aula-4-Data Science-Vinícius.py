# Desafio 1

# Cadastrar
lista_cadastro = []
lista_opcoes =[]
depositar = 0
lista_opcoes.append(depositar)
sacar = 1 
lista_opcoes.append(sacar)
ver_saldo = 2 
lista_opcoes.append(ver_saldo)

email_usuario = input('qual seu email ?')
senha_usuario = input('qual seu senha ?')
lista_cadastro.append (email_usuario)
lista_cadastro.append (senha_usuario)
print('seu email é',email_usuario,'e sua senha é',senha_usuario)
login = 0 
while login >= 0 :
       if login <= 3 :
        email_usuario = input('qual seu email ?')
       if email_usuario == lista_cadastro[0] :
         print('correto')
       else :
          print('verifique seu email')
          break
       senha_usuario = input('qual seu senha ?')   
       if senha_usuario == lista_cadastro[1] :
         print('correto')
       else :
          print('verifique sua senha')
          break
       saldo = int(input('Qual é o saldo da sua conta bancaria ? '))
       print(saldo)
       opcoes = input('Escolha dentre essas tres opções ID0( depositar), 1(sacar), 2(ver saldo da conta)')
       if opcoes == '0' :
          soma = int(input('Qual o valor que você deseja depositar ? '))
          print (soma + saldo )
       elif opcoes == '1': 
          sub = int(input('Qual o valor que você deseja sacar ? '))
          print (sub - saldo )
       elif opcoes == '2':
          print('Seu saldo é de', saldo)
       break
else :
   print('Tente novamente mais tarde')

# Desafio 2

