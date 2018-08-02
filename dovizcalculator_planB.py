import json
from urllib.request import urlopen

istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")

with urlopen("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz = istenen_doviz,doviz2 = ikinci_doviz)) as sterlingRequest:
    dovizSource = sterlingRequest.read()

dovizData = json.loads(dovizSource)

def getdovizName():
    dovizName = dovizData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
    print(dovizSource)
    return dovizName

def dovizCalculate():

    result = dovizName.get(2) - dovizName.get(3)
    return result

