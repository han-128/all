import requests
import main_header

client_id = main_header.client_id
api_key = main_header.api_key
warehouseid = main_header.warehouseid 

url = 'https://api-seller.ozon.ru/v1/report/info'

headers = {
    'Client-Id': client_id,
    'Api-Key': api_key,
    'Content-Type': 'application/json'
}

jjson = {
  "code": "REPORT_seller_products_1898519_1722510377_24f992ed-873e-48fd-bb66-6ea886d054e6"

}

response = requests.post(url, headers=headers, json=jjson)

data = response.json()
print(data)
