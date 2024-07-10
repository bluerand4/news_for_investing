#%%

print('start')
from import_stocks2 import *

# get_insider_short_interest(ticker)


# ticker='MEDP'


# # %%
# tickers = "DERM,AFRM,AFRM,CRWD,ZS,NET,QLYS,NOW,ANET,MBIN,MBIN,SKWD,TEAM,BRZE,ML,AVAH,ZS,ML,AVAH,SRRK,IRON,CDRE,MBIN,ANET,AFRM,PHM,STNE,SKWD,BRZE,TEAM,IBP,CADE,CNM,NET,NET,SNAP,VRT,ML,CADE,MBIN"
# tickers='SRRK,IRON,CDRE,MBIN,ANET,AFRM,PHM,STNE,SKWD,BRZE,TEAM,IBP,CADE,CNM,NET,NET,SNAP,VRT,ML,CADE,MBIN'
# tickers=tickers.split(',')
# tickers=list(set(tickers))
# tickers
# #%%
# #%%
# for ticker in tickers:
#     insert_mongo_stock_comparison(ticker)
# # %%
# ticker='QLYS'
# insert_mongo_stock_comparison(ticker)
# # %%
# common_stock_list_v1_5000_polygon_real_time()
# #%%
from import_tradingview import *
tickers=polygon_stock_list_5000_realtime()
for ticker in tickers:
    time.sleep(10)
    try:
        print('''> try: insert_mongo_stock_comparison(ticker)''',datetime.now())
        insert_mongo_stock_comparison(ticker)
    except Exception as e:
        print('''>> error: insert_mongo_stock_comparison(ticker): ''',e,datetime.now())

