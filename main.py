import requests

response = requests.get('https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd?rapidapi-key=ab6bd7d3d4mshe406166b4af7b82p1f6ed0jsneae683ad9ad2')

BTC = response.json()

print(BTC['data']['coin']['name'])