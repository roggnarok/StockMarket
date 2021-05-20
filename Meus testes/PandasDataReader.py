import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime
import requests_cache

expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
start = datetime.datetime(2021, 5, 1)
end = datetime.datetime(2021, 5, 19)
ticker_usuario = input("Digite o código da ação: ")
ticker_usuario = ticker_usuario + ".SA"             # Para ações do IBOV é necessário add '.SA'.
ticker = ticker_usuario.upper()                     # Converte tudo em maiúscula. 

# Recebe os dados e armazena na variável papel. 
papel = web.DataReader(ticker, 'yahoo', start, end, session=session)
papel = round(papel, 2) # Arredonda para 2 casas decimais.

# Mostra as informações sobre a tabela, nomes de colunas e tipos de variáveis.
print(papel.info())

print(
f'As 5 primeiras linhas da tabela:\n'
f'{papel.head()}'
)

print(
f'As informações de determinado dia:\n'
f'{papel.loc["2021-5-19"]}'
)

papel_vol = papel.Volume
print(f'O volume de {ticker} foi\n{papel_vol}')
