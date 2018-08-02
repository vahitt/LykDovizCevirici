import json
import requests


class Doviz():
    requests_session = requests.session()
    
    def __init__(self):
        secim = input("""
        1 - TL -> USD EURO STERLIN GOSTER
        2 - DEGER CEVIR
        3 - TOPLU CEVIR 
        
        seciminiz:             
        """)
        
        if secim.isnumeric():
            secim = int(secim)
        else:
            print("Lutfen gecerli bir secim yapiniz")
            return self.__init__()
        
        if secim == 1:
            return self.tr_deger()
        elif secim == 2:
            return self.cevir()
        elif secim == 3:
            return self.toplu_cevir()
        else:
            print("Lutfen gecerli bir secim yapiniz")
            return self.__init__()
    
    def tr_deger(self):
        dolar = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='usd', doviz2='try')
        sterlin = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='gbp', doviz2='try')
        euro ="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='eur', doviz2='try')
        pass
    
    def cevir(self):
        pass
    
    def toplu_cevir(self):
        pass
    
    def getRequest(self,url):
        self.url = url
        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data)
        #TARIH VE DEGER CEKILECEK
