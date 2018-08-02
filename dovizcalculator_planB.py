"""
import json
import requests

istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")

data = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O'.format(doviz = istenen_doviz))

codeco = data.content.decode ("UTF-8")

suggests_json = codeco.split("Realtime Currency Exchange Rate")[0:]

suggests = json.loads(codeco)

for i in suggests:
    print(i)
"""


import json
from urllib.request import urlopen

istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")

with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency=TRY&apikey=5Y57NAHCNN1GRX1O".format(doviz = istenen_doviz)) as sterlingRequest:
    sterlingSource = sterlingRequest.read()

sterlingData = json.loads(sterlingSource)

def getSterlingName():
    sterlingName = sterlingData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    print(sterlingSource)
    return sterlingName


getSterlingName()
