import pandas as pd


df = {

'nome':['Ana','Pedro','José','Carlos'],
'idade':[35,50,12,25],
'email':['ana@gmail.com','pedro@gmail.com','jose@gmail.com','carlos@gmail.com'],
    
}

data = pd.DataFrame(df)

data.to_csv('dado.csv', index=False )
data.to_excel('dados2.xlsx', index=False)
data.to_json('dado3.json')
data.to_html('index.html')
data.to_string('dados.py')
data.to_dict()
print(data.to_markdown())
data.to_

print(data)