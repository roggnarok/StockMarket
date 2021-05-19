import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime
import requests_cache

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
start = datetime.datetime(2021, 5, 1)
end = datetime.datetime(2021, 5, 19)
guar3 = web.DataReader("GUAR3.SA", 'yahoo', start, end, session=session)
hype3 = web.DataReader("HYPE3.SA", 'yahoo', start, end, session=session)
itub4 = web.DataReader("ITUB4.SA", 'yahoo', start, end, session=session)
bbas3 = web.DataReader("BBAS3.SA", 'yahoo', start, end, session=session)


#Testes
print(guar3.loc['2021-5-19'])
guar3_vol = guar3.Volume
print(f'O volume de Guar3 foi\n{guar3_vol}')

#print(len(guar3_vol))
#print(itub4.all)
#print(itub4.head(6))
