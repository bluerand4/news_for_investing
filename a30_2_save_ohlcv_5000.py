#%%
from import_basics import *
#%%

from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
# from nsedt import equity as eq
from datetime import date
from import_basics import *
from websocket import create_connection
import json,string,re

from twilio.rest import Client
import yagmail
from datetime import datetime,timedelta
import pandas as pd
# Your Account SID from twilio.com/console
account_sid = "{account_sid_twilio}"
auth_token  = "{auth_token_twilio}"
client = Client(account_sid, auth_token)
sender='{id_yagmail}'
#receiver='bluerand3@gmail.com'
email1=sender
passw1='{password_yagmail}'
passw1='{password_yagmail}'
yag = yagmail.SMTP(user=sender,password=passw1)
content1='1'
subject1='1'
def send_email(to_email,title,content):
    yag.send(to=to_email,subject=title,contents=content)

def datainput(func,paramList):
    #func="set_auth_token"
    #paramList=["unauthorized_user_token"]
    data1=json.dumps({"m":func,"p":paramList}, separators=(',', ':'))
    data1
    data2="~m~" + str(len(data1)) + "~m~" + data1
    return data2



# if 'winp' in socket.gethostname():
#     path3='G:/내 드라이브/'
#     path7=f'G:/내 드라이브/ibkr/1_total_data/7 scrape/2 tradingview scrape/daily_update'
def save_tradingview_df_in_gdrive(fullname1,minute1,df):
    if 'win' in socket.gethostname():
        csv1='G:/My Drive/ibkr/10_chrome_data/1_bayesian_results/v1_model_data.xlsx'
        path7=f'G:/My Drive/ibkr/1_total_data/7 scrape/2 tradingview scrape/daily_update'
    else:
        path3=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/'

        path7=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/7 scrape/2 tradingview scrape/daily_update'

    
    try:
        df1=pd.read_csv(f"{path7}/{fullname1}_{minute1}.csv",index_col=0)
    except:
        # df=create_SMA200(df)

        df.to_csv(f"{path7}/{fullname1}_{minute1}.csv")
    else:
        # df=df1.append(df)
        # new_df=pd.DataFrame(list6).transpose()
        df=pd.concat((df1,df),axis=0)

        df=df.drop_duplicates(keep="last",subset="Timestamp")
        df=df.sort_values(by='Timestamp')
        df=df.reset_index()
        if "index" in df.columns:
            df=df.drop(columns=["index"])
        if "level_0" in df.columns:
            df=df.drop(columns=["level_0"])
        # df=create_SMA200(df)

        
        df.to_csv(f"{path7}/{fullname1}_{minute1}.csv")

import json
def tradingview_simple(fullname,minute1):

    if "CME" in fullname or "CBOT" in fullname or "COMEX" in fullname or "NYMEX" in fullname:
        extended_or_regular="regular"
    else:
        extended_or_regular="extended"


    headers = json.dumps({'Origin': 'https://data.tradingview.com'})
    connector=create_connection('wss://data.tradingview.com/socket.io/websocket',headers=headers)
    stringLength=12
    letters = string.ascii_lowercase
    random_string= ''.join(random.choice(letters) for i in range(stringLength))
    session= "qs_" +random_string

    stringLength=12
    letters = string.ascii_lowercase
    random_string= ''.join(random.choice(letters) for i in range(stringLength))
    chart_session= "cs_" +random_string
    #chart_session= "cs_" +"ZHlTeGX28izS"
    #ZHlTeGX28izS

    #connector.send(datainput('set_auth_token',["eyJhbGciOiJSUzUxMiIsImtpZCI6IkdaeFUiLCJ0eXAiOiJKV1QifQ.eyJ1c2VyX2lkIjoxMjgyNzE5MywiZXhwIjoxNjQ3OTM2MDQ2LCJpYXQiOjE2NDc5MjE2NDYsInBsYW4iOiJwcm9fcHJlbWl1bSIsImV4dF9ob3VycyI6MSwicGVybSI6ImNib3RfbWluaSxjbWUsY21lLWZ1bGwsY29tZXgsbnltZXgsbnlzZSxueW1leF9taW5pLGNtZV9taW5pLGNib3QsbmFzZGFxLGNvbWV4X21pbmksa3J4X3N0b2NrcyIsInN0dWR5X3Blcm0iOiJ0di12b2x1bWVieXByaWNlLHR2LXByb3N0dWRpZXMiLCJtYXhfc3R1ZGllcyI6MjUsIm1heF9mdW5kYW1lbnRhbHMiOjAsIm1heF9jaGFydHMiOjgsIm1heF9hY3RpdmVfYWxlcnRzIjo0MDAsIm1heF9zdHVkeV9vbl9zdHVkeSI6MjR9.ps5_xiYSdN_1FQnC1C98KwtTE3vHMRA0hDyHnCXbg3cyP0RHT6P4O4EBIGCeW-ZsrWkLrCdVN5ZJTgH9jfG9IaSviiDhkhS8rh6iFvqPS-NZ5rdcJ8--tbSLMcLcSHxfonrMO6BXB_yAh3fDePaWFFmJoaDh7D9_-iLgDC_jtoI"]))
    connector.send(datainput('set_auth_token',['unauthorized_user_token']))
    connector.send(datainput("chart_create_session",[chart_session, ""]))
    connector.send(datainput('quote_create_session',[session]))
    #connector.send(datainput('quote_set_fields',[session,"ch","chp","current_session","description","local_description","language","exchange","fractional","is_tradable","lp","lp_time","minmov","minmove2","original_name","pricescale","pro_name","short_name","type","update_mode","volume","currency_code","rchp","rtc"]))
    connector.send(datainput('quote_set_fields',[session,"short_name","pro_name","logoid","currency-logoid","base-currency-logoid","symbol-primaryname","type"]))
    "qs_pzepkyh89H2l"
    connector.send(datainput('quote_add_symbols',[session, fullname, "={\"symbol\":"+"\"{}\"".format(fullname) + ",\"currency-id\":\"USD\",\"adjustment\":\"splits\"}"]))

    connector.send(datainput('quote_fast_symbols',[session,fullname]))
    #connector.send(datainput('resolve_symbol',[chart_session,"sds_sym_1","={\"symbol\":"+"\"{}\"".format(fullname) +",\"adjustment\":\"splits\",\"session\":\"extended\"}"]))
    #connector.send(datainput('resolve_symbol',[chart_session,"sds_sym_1","={\"symbol\":"+"\"{}\"".format(fullname) +",\"adjustment\":\"splits\",\"session\":\"regular\"}"]))
    connector.send(datainput('resolve_symbol',[chart_session,"symbol_1","={\"symbol\":"+"\"{}\"".format(fullname) +",\"adjustment\":\"splits\",\"session\":" +"\"{}\"".format(extended_or_regular)+"}"]))
    connector.send(datainput('create_series',[chart_session, "s1", "s1", "symbol_1", minute1, 5000]))
    time1=[time.monotonic()]
    while True:
        #time.sleep(1)
        list1=[]
        result = connector.recv()
        list2=""+result+'\n'
        
        list1.append(result)
        #print(result)
        #print("helo##############################")

        if len(result)>10000:
            break
        elif len(result)==0:
            break
        else:
            
            if time.monotonic()-time1[0]>(60):
                print(fullname, "error here5")
                break

            else:
                continue
    result1=list1[0]
    a1=""+result1+'\n'
    out= re.search('"s":\[(.+?)\}\]', a1).group(1)
    x=out.split(',{\"')

    list4=[]

    for i in range(len(x)):


        xi=x[i]
        xi

        xi2= re.split('\[|:|,|\]', xi)
        

        index1= int(xi2[1])
        index1

        date2=xi2[4]
        date2

        date1=datetime.fromtimestamp(float(date2)).strftime("%Y/%m/%d, %H:%M:%S")
                
        date1=datetime.strptime(date1, "%Y/%m/%d, %H:%M:%S")
        date1

        list3=[index1,date1,float(xi2[5]), float(xi2[6]), float(xi2[7]), float(xi2[8]), float(xi2[9]),float(date2)]
        list3

        list4.append(list3)
        list4

    df=pd.DataFrame(list4)
    df.rename(columns={0:"Index",1:'Date',2:"Open",3:"High",4:"Low",5:"Close",6:"Volume",7:"Timestamp"}, inplace=True)


    df = df.drop('Index', axis=1)
    df

    while True:
        tot=len(df)-1
        date2=df['Date'][tot]
        date2
        if 'nan' in str(date2).lower() or 'nat' in str(date2).lower():
            print('drop last row')
            df = df.iloc[:-1 , :]
        else:
            break

    return df


def weekly_df(df,DATE_Column='d'):
    




    df[DATE_Column] = pd.to_datetime(df[DATE_Column])

    df.set_index(DATE_Column, inplace=True)


    dfw = pd.DataFrame({
        'Open': df['Open'].resample('W').first(),
        'High': df['High'].resample('W').max(),
        'Low': df['Low'].resample('W').min(),
        'Close': df['Close'].resample('W').last(),
        'Volume': df['Volume'].resample('W').sum(),
        'Timestamp': df['Timestamp'].resample('W').first()
    })
    dfw


    # p3 reset
    dfw=reset_index(dfw)
    
    return dfw

# %%
#%%
from import_stocks2 import *
def save_csv_daily_tradingview_ohlcv():
    stock_list=stock_list_5000_v2()
    print("\n>> len(stock_list)= ", len(stock_list))
    #%%

    ticker='AAPL'
    for ii,ticker in enumerate(stock_list[:]):
        try:
            fullname=generate_fullname_tradingview(ticker)
            
            df=tradingview_simple(fullname,minute1='1D')
            df
            
            csv_update_insert_one('tradingview_v1',ticker,df,'Date')
            print(ii,ticker)
        except Exception as e:
            print('erororororor,',ticker,e)
    #%%