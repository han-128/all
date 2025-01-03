import requests
import main_header
import json

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v1/product/info/stocks-by-warehouse/fbs'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "sku": ['1544235256','1544627989','1544644427','1544641126','1544645048',
    '1544645217','1615430448','1615424674','1601993373','1617845824','1618948878',
    '1618949886','1620966944','1622712259'
]
}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))
