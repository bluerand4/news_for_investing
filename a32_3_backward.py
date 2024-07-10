#%%
from import_all import *

path1='/Users/imac1/Documents/data/stock/bottoming_stock.csv'
df=read_excel(path1)
# %%
df
df=df.sort_values(by='ratio1',ascending=True)
df
# %%
# open_excel(df)
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
#%%
for i in range(len(df))[:100]:
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
# %%
#%%
#%%
#%%
    #%%
from import_all import *

# %%

# mongo_collection_names('stock')
#%%
dp=mongo_get_df('stock','polygon_stocks')
dp
#%%

#%%
df_mongo=mongo_get_df('stock','comparison')
df_mongo
# %%
df_mongo=df_mongo.sort_values(by='revslope',ascending=False)
df_mongo[:20]
# %%
df_mongo
#%%
df2 = df_mongo[df_mongo['inslope'] >= 15]
df2 = df2[df2['inslope2'] >= 15]
df2 = df2[df2['revslope'] >= 15]
df2 = df2[df2['revslope2'] >= 15]
df2

#%%

df2 = df2[df2['inslope'] <= 499]
df2 = df2[df2['inslope2'] <= 499]
df2 = df2[df2['revslope'] <= 499]
df2 = df2[df2['revslope2'] <= 499]
df2
# %%
df2
# %%
tradingview_slope=mongo_get_df('stock','tradingview_slope')
tradingview_slope
#%%

#%%
PER="Price to earnings Ratio (TTM)"
DIV='Dividend yield (indicated)'
tradingview_slope[PER]


df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2 = df2[df2['revenue1'] >= 0]
df2 = df2[df2['revenue2'] >= 0]
df2 = df2[df2['net_income1'] >= 0]
df2 = df2[df2['net_income2'] >= 0]
df2 = df2[df2['fcf1'] >= 0]
df2 = df2[df2['fcf2,'] >= 0]
df2=df2.sort_values(by=PER,ascending=True)
df3=df2[:50][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
df3
#%%

list2=df3['ticker'][0:20].values.tolist()
','.join(list2)
#%%

'ESEA,PSHG,TNK,GSL,TRMD,CVI,PETZ,DINO,GM,CEIX,SDRL,GECC,MHUA,FCAP,MVO,OI,BSVN,SLVM,WLFC,BOSC,HE,RWAY,BVFL'
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%####################################################
#

tradingview_slope
#%%
# df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2=tradingview_slope
df2 = df2[df2['revenue1'] >= 15]
df2 = df2[df2['revenue2'] >= 15]
# df2 = df2[df2['net_income1'] >= 15]
# df2 = df2[df2['net_income2'] >= 15]
df2 = df2[df2['fcf1'] >= 15]
df2 = df2[df2['fcf2,'] >= 15]
df2 = df2[df2['revenue1'] <= 499]
df2 = df2[df2['revenue2'] <= 499]
# df2 = df2[df2['net_income1'] <= 499]
# df2 = df2[df2['net_income2'] <= 499]
df2 = df2[df2['fcf1'] <= 499]
df2 = df2[df2['fcf2,'] <= 499]

df2=df2.sort_values(by='fcf2,',ascending=False)
df2
#%%
ticker_list2=df2['ticker'].values.tolist()
# %%
df[df['ticker']=='AAPL'].index[0]

#%%

# for i in range(len(df))[:100]:
for ticker in ticker_list2:
    # data=df['data'][i]
    # data=df['data'][i]
    # data=df['data'][i]
    try:
        # ticker=df['ticker'][i]
        i=df[df['ticker']==ticker].index[0]

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
    except Exception as e:
        print('error',ticker,e)
    print("ticker: ",ticker,i)
# %%
df
# %%
df_total=df2.merge(df,how='outer',on='ticker')
df_total
# %%
open_excel(df_total)
#%%
df_copy=df_total[['ticker','ratio1','revenue1','revenue1','net_income1','net_income2','dividend1','dividend','fcf1','fcf2,']][:50]
# %%
df_total

df_copy = df_copy[df_copy['ratio1'] < 0.6]
df_copy=reset_index(df_copy)
df_copy
# %%
df_total[df_total['ticker']=='TSLA']
# %%

df_copy['sic_description']=''
df_copy['type']=''
df_copy['primary_exchange']=''
df_copy['name']=''
df_copy['market_cap']=0
for i in range(len(df_copy))[:]:
    # data=df_copy['data'][i]
    # data=df_copy['data'][i]
    # data=df_copy['data'][i]
    try:
        ticker=df_copy['ticker'][i]

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
        df_copy.loc[i,'sic_description']=sic_description
        df_copy.loc[i,'type']=type
        df_copy.loc[i,'primary_exchange']=primary_exchange
        df_copy.loc[i,'name']=name
        df_copy.loc[i,'market_cap']=market_cap
    except:
        print('error',ticker)
    print("ticker: ",ticker,i)

# %%
df_copy
df_copy2 = df_copy[df_copy['market_cap'] > 100000000]
df_copy2=reset_index(df_copy2)
df_copy2

# %%
