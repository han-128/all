import requests
import json

def a(currency = "USD", coin = "BTC"):
    print(f"{coin} PRICE: {str(json.loads(requests.get(f'https://api.bittrex.com/api/v1.1/public/getticker?market={currency}-{coin}').text)['result']['Ask'])} {currency}")

a("EUR", "ETH")
a("EUR")
a(coin = "ETH")
a(currency = "EUR")
