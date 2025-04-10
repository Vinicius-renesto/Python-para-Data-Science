import pandas as pd
import numpy as np

vendas = [1000, 2000, 3000, 50000, 9000, 7000, 8000]
vendedor = ['CARLOS','FERNANDO','MARIA','MARTA','ELOYSA','CARMEM','PABLO']

data = pd.DataFrame({
'Vendas': vendas,
'Vendedor':vendedor},
)
print(data)

data.to_csv('dado2.csv', index=True)
print('Ação realizada')


