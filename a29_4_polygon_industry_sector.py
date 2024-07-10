#%%
from import_all import *

# %%
#https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
import requests,json
ticker='ML'
url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
response=requests.get(url)

json1=response.json()
stock_name=json1['results']['name']
stock_name
# %%
json1['results']
# %%
