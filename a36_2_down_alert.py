#%%

from import_basics import *
from import_mongo import *
# %%
# path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/6 twilio/stock_alert.xlsx'
# path1='/Users/ryanchun1/Downloads/stock_alert.xlsx'
# df=read_excel(path1)
# df=reset_index(df)
# df=df[:13][['ticker','alert_price']]
# df
# %%
# mongo_update_insert_one('stock','alert_stock_above',df,'ticker')
#%%
# mongo_set_df('stock','alert_stock_above','ticker',df)
# %%
# dw=mongo_get_df('stock','alert_stock_above')
# dw
# %%
# dw
# %%
ticker=input('Down NVDA ====== ')
price=float(input('price = '))

dn=pd.DataFrame([ticker,price]).T
dn.columns=['ticker','alert_price']
dn
# %%
dw=mongo_update_insert_one('stock','alert_stock_below',dn,'ticker')
print(dw)
# %%