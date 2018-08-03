import json
import requests
from pprint import pprint

class Doviz():
    requests_session = requests.session()

    def __init__(self):
        secim = input("""
        1 - TL -> USD EURO STERLIN GOSTER
        2 - DEGER CEVIR
        3 - TOPLU CEVIR 
        4 - HAFTALIK PARA BİRİMİNİN KARSILIGINI GOSTER
        seciminiz:             
        """)

        if secim.isnumeric():
            secim = int(secim)
        else:
            pprint("Lutfen gecerli bir secim yapiniz")
            return self.__init__()
        
        if secim == 1:
            return self.tr_deger()
        elif secim == 2:
            return self.cevir()
        elif secim == 3:
            return self.toplu_cevir()
        elif secim == 4:
            hangi_dovizden = input("Hangi dovizin karsılığını görmek istiyorusunuz:")
            hangi_dovize = input("Karsılığını gostermek istediğiniz dövizi giriniz:")
            return  self.showWeek(hangi_dovizden,hangi_dovize)
        else:
            pprint("Lutfen gecerli bir secim yapiniz")
            return self.__init__()
    
    def tr_deger(self):
        dolar = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='usd', doviz2='try')
        sterlin = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='gbp', doviz2='try')
        euro ="https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency={doviz2}&apikey=5Y57NAHCNN1GRX1O".format(doviz='eur', doviz2='try')
        print("1TL karsılıkları\n")

        for i in range(3):
            if(i == 0):
                self.getRequest(dolar)
                dolar_data = self.deger
                print("USD->{usd}\n" .format(usd =dolar_data) )
            elif(i==1):
                 self.getRequest(sterlin)
                 sterlin_data = self.deger
                 print("GBP->{gbp}\n".format(gbp = sterlin_data))
            elif(i == 2):
                 self.getRequest(euro)
                 euro_data = self.deger
                 print("EURO->{euro}\n".format(euro=euro_data))

    def cevir(self):
        pass
    def showWeek(self,h_dovizden,h_dovize):
        url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol={hangi_dovizden}&to_symbol" \
              "={hangi_dovize}&apikey=5Y57NAHCNN1GRX1O".format(hangi_dovizden = h_dovizden,hangi_dovize=h_dovize)
        self.getRequest(url)
    def toplu_cevir(self):
        birinci_doviz = input("Hangi döviz türünü girmek istiyorsunuz:")
        ikinci_doviz = input("Hangi parabirimine göre görmek istiyorsunuz:")
        miktar = float(input("Ne kadar bu birimden paranız var:"))

        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={doviz}&to_currency=" \
              "{doviz2}&apikey=5Y57NAHCNN1GRX1O".format( doviz=birinci_doviz, doviz2=ikinci_doviz)

        self.getRequest(url)
        print("{tarihli} tarihi itibariyle {ilkpara} {ilkbirim} ----->{ikinicipara} {ikinicibirim} değerindedir.".format(tarihli=self.tarih,ilkpara=float(miktar),ilkbirim=birinci_doviz,ikinicipara= float(self.deger) * miktar,ikinicibirim=ikinci_doviz))
    
    def getRequest(self,url):
        self.url = url
        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data)

        if self.url.split("=")[1].split("&")[0] == "FX_WEEKLY":
            print(dovizData)
        else:
            #TARIH VE DEGER CEKILECEK
            degerler = dovizData.get('Realtime Currency Exchange Rate')
            self.tarih=degerler.get('6. Last Refreshed')
            self.deger=degerler.get('5. Exchange Rate')


doviz=Doviz()




