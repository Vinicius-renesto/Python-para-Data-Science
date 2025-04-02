import funcoes as fc 
# ampliude: 

# produtos 
dicionario_notas = {
'Camiseta de marca' : [150],
'Calça jeans' : [ 250],
'Tênis esportivo' : [400],
'Bolsa feminina' : [350],
'Relógio de pulso' : [500],
'Óculos de sol' : [300],
'Jaqueta de couro' : [600],
'Vestido casual' : [280],
'Carteira de couro' : [200],
'Perfume importado' : [450],
'Smartphone' : [3.000],
'Notebook' : [4.500],
'Smartwatch' : [1.000],
'Headset Bluetooth' : [350],
'Câmera digital' : [2.500],
'Caixa de som portátil' : [400],
'Carregador portátil' : [200],
'Tablet' : [1.800],
'Mouse sem fio' : [150],
'Capinha de celular' : [80],
'Kit de maquiagem' : [250],
'Creme hidratante' : [120],
'Shampoo e condicionador premium' : [100],
'Esmalte importado' : [50],
'Aparelho de barbear elétrico' : [350],
'Livro best-seller' : [80],
'Jogo de tabuleiro' : [200],
'Boneco colecionável': [150],
'Videogame' : [4.000],
'Bolsa de grife' : [2.000]
}

valor = []
v1  = []
total_valor  = []
for etiquetas, n in dicionario_notas.items():
        for x1 in n:
            total_valor.append(x1)


print(total_valor)
soma = sum(total_valor)
print('Total os valores dos produtos: ', soma)

# amplitude  = max(frequencia) - min(frequencia)
def display():
    print('Media de todos os produtos :')
    
    media = fc.media(total_valor)
    print(media)
    
    print('Mediana total de notas:')
    mediana = fc.mediana(total_valor)
    print(mediana)
    
    
    print('Moda total de notas:')
    moda = fc.moda(total_valor)
    print(moda)
    
    
    print('Amplitude total de notas: ')

    amplitude = fc.amplitude(total_valor)
    print(amplitude)
  
    print('***' * 30)
     
    print('Variância total: ')

    variancia_total = fc.variancia(total_valor)
    print('Variância total', variancia_total)

    print('***'*30)

    print('Desvio padrão')
    
    d_total = fc.desvio_padrao(total_valor)
    print('DesvioTotal: ', d_total)


   
    
    
