# mediana 
def mediana():
 Frequencia1 = [1.5,6.8,9.7,10.6]
 Frequencia1.sort()
 Tamanho = len(Frequencia1)
 mediana = (Frequencia1[Tamanho//2]
           if Tamanho % 2 != 0  
           else (Frequencia1[Tamanho//2 - 1] + Frequencia1[Tamanho//2]) / 2)
 print(f"Mediana: {mediana}")

mediana()
