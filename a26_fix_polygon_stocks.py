#%%
from import_stocks2 import *
# %%
from import_tradingview import *
#%%
polygon_stock_list_5000_realtime

#%%
endpoint='https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?apiKey={polygon_api_key}'
response = requests.get(endpoint)
# Raise an error if the request failed
response.raise_for_status()
# Parse the JSON result
data = response.json()
data
df_total=pd.DataFrame(data['tickers'])
df_day = pd.DataFrame(data['tickers'])['day'].apply(pd.Series)
df_day
df_total = pd.concat([df_total, df_day], axis=1)
df_total
df_total['trade_volume']=df_total['v']*df_total['c']
df_total
df_total=df_total.sort_values(by='trade_volume',ascending=False)
df_total=reset_index(df_total)
stock_list=df_total['ticker'].values.tolist()



# %%
stock_list
# %%
df_total
# %%
df_total=df_total.sort_values(by='todaysChangePerc',ascending=False)
df_total=reset_index(df_total)
df_total[:10]
#%%
df_total[-10:]
#%% todaysChange
stock_list.extend('NEWWWW')
df=pd.DataFrame(stock_list)
df.columns=['ticker']
df
# %%
# %%

mongo_set_df('stock','polygon_stocks','ticker',df)
# %%
mongo_insert
#%%
dg=mongo_get_df('stock','polygon_stocks')
dg
# %%
