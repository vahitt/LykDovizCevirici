import json
import requests


class Doviz():
    url = ""
    requests_session = requests.session()
    def __init__(self,url):

        self.url = url

    def getRequest(self):

        raw_data = self.request_session.get(self.url).content
        dovizData = json.loads(raw_data)
        print(dovizData)


istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")

doviz = Doviz("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz=istenen_doviz, doviz2=ikinci_doviz))
doviz.getRequest()