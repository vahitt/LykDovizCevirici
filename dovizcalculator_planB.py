import json
import requests

istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz = istenen_doviz,doviz2 = ikinci_doviz)

request_session = requests.session()

raw_data = request_session.get(url).content

dovizData = json.loads(raw_data)

print(dovizData)