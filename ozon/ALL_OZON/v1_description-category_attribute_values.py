import requests
import main_header
import json

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v1/description-category/attribute/values'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "attribute_id": 85,
  "description_category_id": 17054869,
  "language": "DEFAULT",
  "last_value_id": 0,
  "limit": 100,
  "type_id": 97311
}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))
