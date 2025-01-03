import requests
import json

f = open("application/main.json")
data = json.load(f)
print(data)

client_id = '1898519'
api_key = '7441b4a6-0424-48a3-bb95-f28a20e678a2'
warehouseid = '[1020001804381000]'
details = "[00125]"

url = 'https://api-seller.ozon.ru/v1/report/warehouse/stock'

print()

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
    'Content-Type': 'application/json'
}


response = requests.post(url, headers=headers)

data = response.json()
print(data)
