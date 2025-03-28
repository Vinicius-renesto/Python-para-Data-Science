
# Moda


from collections import Counter
Frequencia = [1, 2, 3, 6, 4]
contagem = Counter(Frequencia)
moda = contagem.most_common(1)
if moda[0][1] > 1:
    print(f"A moda é: {moda[0][0]}")
else:
    print('Moda : '"Não há moda, não tem nenhum número repetitivo")


# mediana 

Frequencia1 = [1.5,6.8,9.7,10.6]
Frequencia1.sort()
Tamanho = len(Frequencia1)
mediana = (Frequencia1[Tamanho//2]
           if Tamanho % 2 != 0  
           else (Frequencia1[Tamanho//2 - 1] + Frequencia1[Tamanho//2]) / 2)
print(f"Mediana: {mediana}")


# media 

Frequencia2 = [200,300,500,700,900,400,600]
n = Frequencia2.sort()
media = sum(Frequencia2) / len(Frequencia2)
print(f"Média: {media}")

