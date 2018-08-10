#!/usr/bin/python3
import json
import requests
import logging
from collections import OrderedDict

class Doviz():

    def __init__(self):
        self.api_url = "https://www.alphavantage.co/query?function=FX_INTRADAY&" \
        "from_symbol={}&to_symbol={}&interval=1min&apikey=5Y57NAHCNN1GRX1O"

        self.monthly_url ="https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={}&" \
             "to_symbol={}&apikey=5Y57NAHCNN1GRX1O"
        self.requests_session = requests.session()

        format_ = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
        logging.basicConfig(filename="warnings.log", format=format_, level=logging.INFO)

        secim = input("""
        1 - TL -> USD EURO STERLIN GOSTER
        2 - TOPLU CEVIR
        3 - AYLIK DEGER DEGISIMI
        seciminiz:
        """)

        if secim.isnumeric():
            secim = int(secim)
        else:
            print("Lutfen gecerli bir secim yapiniz")
            return self.__init__()

        if secim == 1:
            return self.trDeger()
        elif secim == 2:
            return self.topluCevir()
        elif secim == 3:
            return  self.showMonthly()
        else:
            print("Lutfen gecerli bir secim yapiniz")
            logging.warning("Hatali menu girdisi")
            return self.__init__()

    def trDeger(self):
        base = "TRY"
        dolar = self.api_url.format("USD", base)
        euro = self.api_url.format("EUR", base)
        sterlin = self.api_url.format("GBP", base)


        def getter(*args):
                for i in args:
                  self.getRequest(i,base)
                  yield self.deger
        generator = getter(dolar,euro,sterlin)

        print("\nDolar : {}\nEuro : {}\nSterlin : {}".format(next(generator),next(generator),next(generator)))

        return self.__init__()

    def showMonthly(self):
        hangi_dovizden = input("Degisim hangi para birimine gore baz alinacak:")
        hangi_dovize = input("Karsiligini gostermek istediginiz birimi giriniz:")
        url = self.monthly_url.format(hangi_dovizden,hangi_dovize)

        try:
            self.getRequest(url)
        except:
            print("Hatali birim girisi ya da zaman asimi")
            logging.warning("Hatali birim girisi ya da zaman asimi")
            return self.__init__()

        try:
            for keys in self.monthly_data.keys():
                print("Tarih: {}   Kapanis: {}".format(keys,self.monthly_data.get(keys).get('4. close')))

        except:
            print("Aylik data cekilirken hata")
            logging.warning("Aylik data cekilirken hata")

        return self.__init__()

    def topluCevir(self):
        birinci_doviz = input("Hangi doviz turunu girmek istiyorsunuz:")
        ikinci_doviz = input("Hangi parabirimine gore gormek istiyorsunuz:")
        miktar = float(input("Ne kadar bu birimden paranız var:"))

        url = self.api_url.format(birinci_doviz.upper(),ikinci_doviz.upper())

        try:
            self.getRequest(url)
        except:
            print("Hatali birim girisi ya da zaman asimi")
            logging.warning("Hatali birim girisi ya da zaman asimi")
            return self.__init__()

        print("\n{tarihli} tarihi itibariyle\n{ilkpara} {ilkbirim} {ikinicipara} {ikinicibirim} degerindedir.".format(tarihli=self.tarih,ilkpara=float(miktar),ilkbirim=birinci_doviz,ikinicipara= float(self.deger) * miktar,ikinicibirim=ikinci_doviz))

        return self.__init__()

    def getRequest(self,url,base=None):
        self.url = url
        self.base = base


        raw_data = self.requests_session.get(self.url).content
        dovizData = json.loads(raw_data.decode('utf-8'),object_pairs_hook=OrderedDict)

        if self.url.split("=")[1].split("&")[0] == "FX_MONTHLY":
            self.monthly_data = dovizData.get("Time Series FX (Monthly)")
            logging.info("Aylik data istendi")
        else:
            self.deger=dovizData.get("Time Series FX (1min)")
            f_key = list(self.deger)[0]
            self.deger = self.deger.get(f_key).get("4. close")

            self.tarih=dovizData.get("Meta Data").get("4. Last Refreshed").split(' ')[0]
            logging.info("Ceviri datasi istendi")

doviz=Doviz()
