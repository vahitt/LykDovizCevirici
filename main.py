# -*- coding: utf-8 -*-
import requests
import json

url = "https://www.biletall.com/Default.aspx/KaraKalkisGetir2"

session_request = requests.session()
header = {'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.biletall.com/',
'Content-Type': 'application/json; charset=utf-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '42',
'Cookie': '_gcl_aw=GCL.1527586892.Cj0KCQjw9LPYBRDSARIsAHL7J5l17rQ8bSyHqmw0t-YzV2P5BBlNwr_QFd6kaitemgI1Cjqs0cdzk0oaAgeaEALw_wcB; _ga=GA1.2.1211182984.1527586892; _gac_UA-6216713-2=1.1527586892.Cj0KCQjw9LPYBRDSARIsAHL7J5l17rQ8bSyHqmw0t-YzV2P5BBlNwr_QFd6kaitemgI1Cjqs0cdzk0oaAgeaEALw_wcB; _ym_uid=1527586892692183300; SL_C_23361dd035530_KEY=17148d8a0d5c2c1b9954e73fbb1b4b2047684dce; LangDemoCookie=LangCode=tr-TR; OtobusAramaYeni=%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Bolu%22%2C%22VarisAd%22%3A%22Ankara%20(A%C5%9Fti)%22%2C%22KalkisId%22%3A245%2C%22VarisId%22%3A84%2C%22GidisTarihi%22%3A%222018-08-04T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-08-02T08%3A41%3A53.690Z%22%7D; OtobusAramalar1=%5B%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Bolu%22%2C%22VarisAd%22%3A%22Ankara%20(A%C5%9Fti)%22%2C%22KalkisId%22%3A245%2C%22VarisId%22%3A84%2C%22GidisTarihi%22%3A%222018-08-04T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-08-02T08%3A41%3A53.690Z%22%7D%2C%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Bolu%22%2C%22VarisAd%22%3A%22Yozgat%22%2C%22KalkisId%22%3A245%2C%22VarisId%22%3A1238%2C%22GidisTarihi%22%3A%222018-08-04T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-07-30T20%3A51%3A00.772Z%22%7D%2C%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Bolu%22%2C%22VarisAd%22%3A%22Yerk%C3%B6y%22%2C%22KalkisId%22%3A245%2C%22VarisId%22%3A1236%2C%22GidisTarihi%22%3A%222018-08-05T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-07-30T20%3A50%3A21.259Z%22%7D%2C%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Bolu%22%2C%22VarisAd%22%3A%22Gebze%22%2C%22KalkisId%22%3A245%2C%22VarisId%22%3A777%2C%22GidisTarihi%22%3A%222018-08-05T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-07-30T20%3A48%3A54.956Z%22%7D%2C%7B%22BiletTipi%22%3A%22Otobus%22%2C%22KalkisAd%22%3A%22Gebze%22%2C%22VarisAd%22%3A%22Yerk%C3%B6y%22%2C%22KalkisId%22%3A777%2C%22VarisId%22%3A1236%2C%22GidisTarihi%22%3A%222018-08-05T00%3A00%3A00.000Z%22%2C%22DonusTarihi%22%3A%222018-08-07T00%3A00%3A00.000Z%22%2C%22GidisDonusMu%22%3Afalse%2C%22OlusturmaTarihi%22%3A%222018-07-30T20%3A50%3A41.323Z%22%7D%5D; _gid=GA1.2.907120955.1533194257; ASP.NET_SessionId=fgbofmryfafx53cycnagvxo0',
'Connection': 'keep-alive'}
#session_request.headers = {'content-type': 'application/json; charset=utf-8','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
body = {'term':'an','benzerlikUygulansinMi':'true'}

data = session_request.post(url,headers = header,json=body)

print(data.json())