#%%
from import_stocks2 import *
from import_basics import *
from datetime import datetime,timedelta
import requests
import pandas as pd

def polygon_v3(ticker,minute1,limit1,past1,today1):
    link5='https://api.polygon.io/v2/aggs/ticker/{}/range/{}/day/{}/{}?adjusted=true&sort=asc&limit={}&apiKey={polygon_api_key}'.format(ticker,minute1,past1,today1,limit1)
    data3=requests.get(link5).json()

    df4=pd.DataFrame.from_dict(data3['results'])
    df4
    # columns2=['Volume','vol_weighted_price','Open','Close','High','Low','Timestamp','#_transactions']
    df4=df4.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','v':'Volume','t':'Timestamp'})
    # df4.columns=columns2
    df4['Timestamp']=df4['Timestamp']/1000
    df4=df4[['Timestamp','Open','High','Low','Close','Volume']]
    return df4

# ticker='AAPL'
# limit1=5000
# minute1='1'
# beta2=0
# past1=datetime.strftime(datetime.now()-timedelta(5000) ,"%Y-%m-%d")
# today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
# print(past1,today1)

# # for ticker in polygon_list:
# df=polygon_v3(ticker,minute1,limit1,past1,today1)
# df
# # %%
# df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')
# df
# # %%

# df['Date'] = pd.to_datetime(df['Timestamp'], unit='s').dt.date
# df
# # %%
# ticker='AAPL'
def save_csv_polygon_1d():
    stock_list=stock_list_5000_v2()
    for ticker in stock_list:
        limit1=5000
        minute1='1'
        beta2=0
        BLOCK=100
        beta1=BLOCK
        #%%
        try:
            do=pd.DataFrame()
            for i in range(int(3*30000)):
                past1=datetime.strftime(datetime.now()-timedelta(beta1) ,"%Y-%m-%d")
                today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
                beta1+=BLOCK
                beta2+=BLOCK
                link5='https://api.polygon.io/v2/aggs/ticker/{}/range/{}/day/{}/{}?adjusted=true&sort=asc&limit={}&apiKey={polygon_api_key}'.format(ticker,minute1,past1,today1,limit1)
                data3=requests.get(link5).json()

                df4=pd.DataFrame.from_dict(data3['results'])
                df4
                do=pd.concat([do,df4])
                # break
        except:
            pass
        # %%
        do=do.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','v':'Volume','t':'Timestamp'})
        # do.columns=columns2
        do['Timestamp']=do['Timestamp']/1000
        do=do[['Timestamp','Open','High','Low','Close','Volume']]
        do['Date'] = pd.to_datetime(do['Timestamp'], unit='s').dt.date
        do
        do=do.sort_values(by='Timestamp',ascending=True)
        do
        #%%
        do=reset_index(do)
        do

        # %%
        do=do.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','v':'Volume','t':'Timestamp'})
        # do.columns=columns2
        do['Timestamp']=do['Timestamp']/1000
        do=do[['Timestamp','Open','High','Low','Close','Volume']]
        do['Date'] = pd.to_datetime(do['Timestamp'], unit='s').dt.date
        do

        # %%
        csv_update_insert_one('polygon_v1_1D',ticker,do,'Date')
        # %%
        print("ticker: ",ticker)


#%%
def save_csv_polygon_1m():
    stock_list=stock_list_5000_v2()
    for ticker in stock_list:

        limit1=50000
        minute1='1'
        Interval='minute'
        beta2=0
        BLOCK=1
        beta1=BLOCK
        try:
            do=pd.DataFrame()
            for i in range(int(3*30000)):
                past1=datetime.strftime(datetime.now()-timedelta(beta1) ,"%Y-%m-%d")
                today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
                beta1+=BLOCK
                beta2+=BLOCK
                link5='https://api.polygon.io/v2/aggs/ticker/{}/range/{}/minute/{}/{}?adjusted=true&sort=asc&limit={}&apiKey={polygon_api_key}'.format(ticker,minute1,past1,today1,limit1)
                data3=requests.get(link5).json()

                df4=pd.DataFrame.from_dict(data3['results'])
                df4
                do=pd.concat([do,df4])
                
        except:
            pass
        do
        # %%
        do=do.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','v':'Volume','t':'Timestamp'})
        # do.columns=columns2
        do['Timestamp']=do['Timestamp']/1000
        do=do[['Timestamp','Open','High','Low','Close','Volume']]
        do['Date'] = pd.to_datetime(do['Timestamp'], unit='s')
        do
        # %%

        do=do.sort_values(by='Timestamp',ascending=True)
        do
        #%%
        do=reset_index(do)
        do
        csv_update_insert_one('polygon_v1_1M',ticker,do,'Date')
        print("ticker: ",ticker)


try:
    print('''> try: save_csv_polygon_1d()''',datetime.now())
    save_csv_polygon_1d()
except Exception as e:
    print('''>> error: save_csv_polygon_1d(): ''',e,datetime.now())


try:
    print('''> try: save_csv_polygon_1m()''',datetime.now())
    save_csv_polygon_1m()
except Exception as e:
    print('''>> error: save_csv_polygon_1m(): ''',e,datetime.now())
