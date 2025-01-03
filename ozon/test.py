import requests

client_id = '1898519'
api_key = '7441b4a6-0424-48a3-bb95-f28a20e678a2'

url = "https://api-seller.ozon.ru/v1/report/warehouse/stock"

headers = {
    'Api-Key': api_key,
    'Client-Id': client_id
}

json = {
    "WarehouseId": ['1020001804381000'],
    "details": []
}

response = requests.post(url, headers=headers, json=json)

data = response.json()
print(data)

