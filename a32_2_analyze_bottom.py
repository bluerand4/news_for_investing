#%%
from import_all import *

path1='/Users/imac1/Documents/data/stock/bottoming_stock.csv'
df=read_excel(path1)
# %%
df
df=df.sort_values(by='ratio1',ascending=False)
df
# %%
open_excel(df)
# %%
#https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
import requests,json
ticker='AAPL'
# %%
df=reset_index(df)
# %%
df

df['sic_description']=''
df['type']=''
df['primary_exchange']=''
df['name']=''
df['market_cap']=0

for i in range(len(df)):
    # data=df['data'][i]
    # data=df['data'][i]
    # data=df['data'][i]
    try:
        ticker=df['ticker'][i]

        url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
        response=requests.get(url)

        json1=response.json()
        stock_name=json1['results']['name']
        stock_name
        
        json1
        
        data1=json1['results']
        sic_description=data1['sic_description']
        type=data1['type']
        primary_exchange=data1['primary_exchange']
        name=data1['name']
        market_cap=data1['market_cap']
        df.loc[i,'sic_description']=sic_description
        df.loc[i,'type']=type
        df.loc[i,'primary_exchange']=primary_exchange
        df.loc[i,'name']=name
        df.loc[i,'market_cap']=market_cap
    except:
        print('error',ticker)
    print("ticker: ",ticker,i)
    #
