import json
import requests
from pprint import pprint

class Doviz():
    
    
    
    def __init__(self):
        self.api_url = "https://exchangeratesapi.io/api/latest?base={}"
        self.requests_session = requests.session()
        
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
        base = "TRY"
        dolar = self.api_url.format("USD")
        euro = self.api_url.format("EUR")
        sterlin = self.api_url.format("GBP")
        
       
        self.getRequest(dolar,base)
        dolar_data = self.deger
        self.getRequest(sterlin,base)
        sterlin_data = self.deger
        self.getRequest(euro,base)
        euro_data = self.deger
        
        print("\nDolar : {}\nEuro : {}\nSterlin : {}".format(dolar_data,euro_data,sterlin_data))
        
        return self.__init__()

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
        
        url = self.api_url.format(birinci_doviz.upper())
        
        self.getRequest(url,ikinci_doviz.upper())
        print("{tarihli} tarihi itibariyle {ilkpara} {ilkbirim} ----->{ikinicipara} {ikinicibirim} değerindedir.".format(tarihli=self.tarih,ilkpara=float(miktar),ilkbirim=birinci_doviz,ikinicipara= float(self.deger) * miktar,ikinicibirim=ikinci_doviz))
    
    def getRequest(self,url,base=None):
        self.url = url
        self.base = base
        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data)

        if self.url.split("=")[1].split("&")[0] == "FX_WEEKLY":
            print(dovizData)
        else:
            self.deger=dovizData.get("rates").get(self.base)
            self.tarih=dovizData.get('date')


doviz=Doviz()




