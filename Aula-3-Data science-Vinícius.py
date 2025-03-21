# desafio 1
# cadastrar-se


dados_usuarios ={}
print('Seja bem vindo, cadastr-se: ')

login = input('Login: ')
senha = input('Senha : ')
nome  = input('Nome: ')

dados_usuarios['senha'] = login
dados_usuarios['login'] = senha
dados_usuarios['nome']  = nome

print(dados_usuarios)
login_usuario = input('Login: ')
senha_usuario = input('Senha: ')

carrinho = []

if senha_usuario in dados_usuarios['login']  and login_usuario in dados_usuarios['senha']:
    print('Seja bem vindo:  ', dados_usuarios['nome'])
    lista_prod = []
    fones = 219.90
    lista_prod.append(fones)
    celular = 5399.90
    lista_prod.append(celular)
    tenis = 479.90
    lista_prod.append(tenis)
    escolha =  int(input('Escolha o produto a partir do ID 0(fones), 1(celular), 2(tenis)'))
    carrinho.append(lista_prod[escolha])
    escolha1 = input('deseja continuar escolhendo ? ')
    if escolha1 == 'sim':
        soma = int(input('quantas compras deseja comprar ? ') )
        for escolha in range(soma):
             escolha =  int(input('Escolha o produto a partir do ID 0,1,2'))
             carrinho.append(lista_prod[escolha])
             somas = sum(carrinho)
        print('O total de sua compra foi de', somas)     
        pagamento = float(input('Qual o valor que vc deseja atribuir ao pagamento ? '))
        if pagamento > somas:
            sub = somas - pagamento 
            print('aqui esta seu troco ',sub)
        elif pagamento == somas :
            print('Obrigado pela compra')
        elif pagamento < somas :
            sub1 = somas - pagamento 
            print('esta faltando ',sub1)
        else :
            print('devolva sua compra')
    else : 
        print('Ok, iermos finalizar sua compra')
        print('O total de sua compra foi de', lista_prod[escolha])
        pagamento = float(input('Qual o valor que vc deseja atribuir ao pagamento ? '))
        if pagamento > escolha :
            sub = ( lista_prod[escolha] - pagamento)
            print('aqui esta seu troco ',sub)
        elif pagamento == pagamento == escolha :
            print('Obrigado pela compra')
        elif pagamento > escolha :
            sub1 = lista_prod[escolha] - pagamento 
            print('esta faltando ',sub1)
        else :
            print('devolva sua compra')

else :
    print('obrigado pela sua visita')


# desafio 2

