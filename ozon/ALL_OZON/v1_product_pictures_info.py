import requests
import main_header
import json

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v1/product/pictures/info'


headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "product_id": [
    "1544645217"
  ]
}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))

