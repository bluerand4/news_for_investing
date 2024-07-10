#%%
from import_all import *

# %%
stock_list_5000
#%%
stock_list=stock_list_11000()
print("\n>> len(stock_list)= ", len(stock_list))

# %%
for ticker in stock_list:
    try:
        fullname=generate_fullname_tradingview(ticker)
        df=tradingview_simple(fullname,'1D')
        df
        # %%
        all_time_high=max(df['High'].values.tolist())
        # %%
        current_price=df['Close'][-1:].values[0]
        # %%
        ratio1=current_price/all_time_high
        # %%
        dn=pd.DataFrame.from_dict(dict(ticker=ticker,ratio1=ratio1,current_price=current_price,all_time_high=all_time_high),orient='index').T
        dn
        #%%
        print("ticker: ",ticker,ratio1,current_price,all_time_high)
        csv_update_insert_one('stock','bottoming_stock',dn,'ticker')
    # %%
    except:
        print('error:',ticker)