import json
from idlelib.multicall import r


def bit(symbol="USD"):
    url = "https://blockchain.info/ticker"
    a = r.unloper(url)
    b = json.load(a)
    if symbol in b:
        print(f"exchange reta {b[symbol]['last']} {symbol}")
