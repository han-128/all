import requests
import main_header

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v1/report/warehouse/stock'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "language": "DEFAULT",
  "warehouseId": [
    "1020001804381000"
  ]
}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(data)
