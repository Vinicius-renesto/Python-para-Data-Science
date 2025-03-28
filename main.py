import moda as m 
import statistics

# import mediana 

vendas = [15., 1213., 556., 150., 85.]

def verificar_dados():
    print('Verificar moda: ')
    modas =m.moda(vendas)
    print(modas)
    print('Verificar variância: ')
    # print(mediana(vendas))  

verificar_dados()

