
import requests
import pandas as pd
import json

df = pd. read_csv("./data/bill_of_materials.csv", sep = ",")
df['json'] = df.apply(lambda x: x.to_json(), axis=1)


url = 'https://us-central1-testeengenharia.cloudfunctions.net/ingestionTerraform'

headers = {'content-type': 'application/json'}

qtdeRegistros = 0

for index,row in df.iterrows():    
    value = row['json']
    body = json.dumps({"billmaterials": value})
    r = requests.post(url, data = body, headers=headers )
    qtdeRegistros = qtdeRegistros + 1
    print ('Foram enviados {0} registros '.format(qtdeRegistros))
    