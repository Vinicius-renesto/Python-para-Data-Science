
from collections import Counter
import statistics

def moda():
 Frequencia = [1, 2, 3, 6, 4]
 Frequencia.sort()
 contagem = Counter(Frequencia)
 moda = contagem.most_common(1)
 if moda[0][1] > 1:
    print(f"A moda é: {moda[0][0]}")
 else:
    print('Moda : '"Não há moda, não tem nenhum número repetitivo")
