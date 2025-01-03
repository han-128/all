import requests
import main_header
import json




client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v3/posting/fbs/list'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "dir": "ASC",
  "filter": {
    "delivery_method_id": [
      "1893206"
    ],
    "since": "2024-07-01T00:00:00Z",
    "to": "2024-08-01T00:00:00Z",
    "warehouse_id": [
      "1020001804381000"
    ]
  },
  "limit": 1000,
  "offset": 0,
  "with": {
    "analytics_data": True,
    "barcodes": True,
    "financial_data": True,
    "translit": True
  }
}




response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))


with open("main.json", "w") as f:
    d = {"my_key": data}
    json.dump(d, f, indent=4)