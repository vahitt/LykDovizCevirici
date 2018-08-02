import json
import requests


class Doviz():
    url = ""
    requests_session = ""
    def __init__(self,url,requests_session):

        self.url = url
        self.requests_session = requests_session
    def getRequest(self):

        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data)
        print(dovizData)


istenen_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")

doviz = Doviz("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz=istenen_doviz, doviz2=ikinci_doviz),requests.session())
doviz.getRequest()