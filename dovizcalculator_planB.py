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
        birinci_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
        ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")
        miktar = float(input("Ne kadar bu birimden paranız var:"))

        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(
                doviz=birinci_doviz, doviz2=ikinci_doviz)

        self.getRequest(url)
        print("{tarihli} tarihi itibariyle {ilkpara} {ilkbirim} ----->{ikinicipara} {ikinicibirim} değerindedir.".format(tarihli=self.tarih,ilkpara=float(miktar),ilkbirim=birinci_doviz,ikinicipara= float(self.deger) * miktar,ikinicibirim=ikinci_doviz))
    
    def getRequest(self,url):
        self.url = url
        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data)
        #TARIH VE DEGER CEKILECEK
        degerler = dovizData.get('Realtime Currency Exchange Rate')
        self.tarih=degerler.get('6. Last Refreshed')
        self.deger=degerler.get('5. Exchange Rate')

doviz=Doviz()