import requests
import main_header
import json

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v3/posting/fbs/unfulfilled/list'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "dir": "ASC",
  "filter": {
    "cutoff_from": "2024-04-01T14:15:22Z",
    "cutoff_to": "2024-08-01T10:15:22Z",
    "delivery_method_id": ['1893206'],
    "warehouse_id": ['1020001804381000']
  },
  "limit": 100,
  "offset": 0,

}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))
