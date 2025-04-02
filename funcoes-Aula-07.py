import statistics
from collections import Counter

def amplitude(lista):
    menor = min(lista)
    maior =  max(lista)
    amplitude  =  maior - menor
    return amplitude 

def variancia(lista):
    variancia_  =  statistics.variance(lista)
    return variancia_

def desvio_padrao(lista):
    desvio  =  statistics.stdev(lista)
    return desvio   

def moda(lista):
    Frequencia = [1, 2, 3, 6, 4]
    contagem = Counter(Frequencia)
    moda = contagem.most_common(1)
    if moda[0][1] > 1:
        print(f"A moda é: {moda[0][0]}")
    else:
        print('Moda : '"Não há moda, não tem nenhum número repetitivo")
    return moda       
        
def media(lista):
    media  =  statistics.mode(lista)
    return media  


def mediana(lista):
    Frequencia2 = [200,300,500,700,900,400,600]
    n = Frequencia2.sort()
    mediana = statistics.mode(lista)
    print(f"Média: {media}")
    return mediana