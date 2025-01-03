import requests
import main_header
import json

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v2/posting/fbo/list'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
}

jjson = {
  "dir": "ASC",
  "filter": {
    "since": "2024-07-03T08:00:00Z",
    "status": "",
    "to": "2024-08-03T08:00:00Z"
  },
  "limit": 100,
  "offset": 0,
  "translit": False,
  "with": {
    "analytics_data": False,
    "financial_data": False
  }
}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))

with open("main.json", "w") as f:
    d = {"my_key": data}
    json.dump(d, f, indent=4)

f.close

Name_Offer_id_H = d['my_key']['result']

Name_Offer_id = []

for i in Name_Offer_id_H:
    if (i['products'][0]['name']) not in Name_Offer_id:
      Name_Offer_id.append(i['products'][0]['name']) 
      Name_Offer_id.append(i['products'][0]['offer_id'])

print(Name_Offer_id)

