#%%
from import_all import *

path1='/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/9 practicce/7_feature_extraction/4_version/11_tradingview_alarm/data/max200_v2.txt'
path1
# %%
with open(path1,'r') as f:
    data1=f.readlines()
data1

# %%
data1=ast.literal_eval(data1)

for ticker in data1:
    break
ticker
#%%

exchange=find_exchange_v2(ticker)
exchange

driver.get(f'https://www.tradingview.com/chart/q0QCLsTJ/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located

