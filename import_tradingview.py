#%%
from import_mongo import *
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
from nsedt import equity as eq
from datetime import date

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


def feature_engineering(df):
    df['Close1']=df["Close"].shift(periods=1)

    df['SMA10'] = df["Close"].rolling(min_periods=1, window=10).mean()
    df['SMA20'] = df["Close"].rolling(min_periods=1, window=20).mean()
    df['SMA50'] = df["Close"].rolling(min_periods=1, window=50).mean()
    df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
    df['SMA300'] = df["Close"].rolling(min_periods=1, window=300).mean()
    df['SMA500'] = df["Close"].rolling(min_periods=1, window=500).mean()
    df['SMA100'] = df["Close"].rolling(min_periods=1, window=100).mean()
    df['SMA1000'] = df["Close"].rolling(min_periods=1, window=1000).mean()
    df['SMA2000'] = df["Close"].rolling(min_periods=1, window=2000).mean()

    df["MAX50"] = df["High"].rolling(min_periods=1, window=50).max()
    df["MAX100"] = df["High"].rolling(min_periods=1, window=100).max()
    df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()

    df["MIN50"] = df["Low"].rolling(min_periods=1, window=50).min()
    df["MIN100"] = df["Low"].rolling(min_periods=1, window=100).min()
    df["MIN200"] = df["Low"].rolling(min_periods=1, window=200).min()
    

    df['Close2'] = df['Close'].pct_change()
    df['High2'] = df['High'].pct_change()
    df['Low2'] = df['Low'].pct_change()
    df['Open2'] = df['Open'].pct_change()
    df['Volume2'] = df['Volume'].pct_change()
    return df

def max200_email_NSE_india(stock_list,title):
    # stock_list=common_stock_list_v1_5000_polygon_real_time()
    print("max200 started")
    # stock_list=stock_list_11000()
    # stock_list=stock_list_5000()
    
    stock_list

    ticker_=[]
    content_=[]

    limit1=2000
    minute1='1'
    beta2=0
    past1=datetime.strftime(datetime.now()-timedelta(2000) ,"%Y-%m-%d")
    today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
    print(past1,today1)
    tradingview_links=[]
    ticker='AAPL'
    for ii,ticker in enumerate(stock_list):
        time.sleep(5)
        try:
            print("ticker: ",ticker,ii,len(stock_list))
            # for ticker in polygon_list:
            # df=polygon_v3(ticker,minute1,limit1,past1,today1)
            
            fullname=f'NSE:{ticker}'
            df=tradingview_simple(fullname,minute1)
            # df['Date']=[datetime.fromtimestamp(item,tz=pytz.timezone("US/Eastern")) for item in df['Timestamp']]
            df



            df=feature_engineering(df)
            close1=df['Close'][len(df)-1]
            max1=df['MAX200'][len(df)-2]
            print(close1,max1)
            # print(df)
            if df['Close'][len(df)-1]>df['MAX200'][len(df)-2]:
                print('yes max200 crossed',ticker,ii)
                content_.append('\n')
                # content_.append(ticker)
                # MC,industry, description,company_name,PE_ratio = get_stock_details(ticker)
                
                # description_summary=gpt_answer("summarize what they do? why customers buying from them? why their products are better than other competitors?",description)
                content_.append('_____________________________________________________')
                # content_.append(f'ticker: {ticker} \nMC: ${MC}B / \nPE: {round(PE_ratio,3)} / \n\nindustry:{industry} / \n\n>description: {description} \n\n>summary: {description_summary}')
                # company_name= generate_company_name(ticker)
                # news=fetch_news_for_query(newsapi_org, query=f'{company_name}',page_size=10)
                # news=fetch_news_for_query(newsapi_org, query=f'{ticker} stock',page_size=10)
                news=str(news)
                # define=f'summarize based on why the {company_name} stock is going up.'
                # news=gpt_answer(define,news)
                try:
                    # exchange1=find_exchange(ticker)
                    exchange1='NSE'
                    ticker_.append(ticker)
                    
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'

                    content_.append(content)
                    tradingview_links.append(content)
                    content_.append(news)
                except:
                    pass
        except Exception as e:
            print('error : ',ticker,e)
    content_


    # Your Account SID from twilio.com/console
    account_sid = "{account_sid_twilio}"
    # Your Auth Token from twilio.com/console
    auth_token  = "{auth_token_twilio}"

    client = Client(account_sid, auth_token)

    sender='{id_yagmail}'
    #receiver='bluerand3@gmail.com'
    receiver=sender
    passw1='{password_yagmail}'
    passw1='{password_yagmail}'

    yag = yagmail.SMTP(user=sender,password=passw1)

    content__=" \n ".join(content_)
    content__

    ticker__=" ".join(ticker_)
    ticker__
    subject_=f'{title}_{ticker__}'
    content__=str(tradingview_links)+content__
    yag.send(to=sender,subject=subject_,contents=content__)
    
    print('end - send email... v1')

list1=['us_stock_close2_max1','us_stock_max2_max1','india_stock_close2_max1']
country='us_stock_close2_max1'

from import_stocks2 import *
def collect_screenshots(country):
    # di=mongo_get_df('screenshot','india_stock_close2_max1')
    # di=mongo_get_df('screenshot','us_stock_max2_max1')
    di=mongo_get_df('screenshot',country)


    driver=open_driver()

    folder=country
    folder1=f'data/screenshots/{folder}/'
    # folder1=f'/Users/mac1/Documents/a1_data/{folder}'
    if not os.path.exists(folder1):
        os.makedirs(folder1)


    i=0
    links=di['tradingview_link'].values.tolist()
    tradingview_link=di['tradingview_link'][i]
    ticker=None
    driver.get(tradingview_link)
    for _ in range(3):
        try:
            print('''> try: driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]').click()''',datetime.now())
            driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]').click()
            break
        except Exception as e:
            time.sleep(5)
            print('''>> error: driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]').click(): ''',e,datetime.now())
    if ticker==None:
        ticker=str(int(datetime.now().timestamp()))

    filename=ticker+'.png'
    relapath=f'data/screenshots/{folder}/{filename}'
    
    # relapath=f'/Users/mac1/Documents/a1_data/{folder}/{filename}'
    time.sleep(5)
    for _ in range(3):
        try:
            print('''> try: driver.save_screenshot(relapath)''',datetime.now())
            driver.save_screenshot(relapath)
            break
        except Exception as e:
            time.sleep(5)
            print('''>> error: driver.save_screenshot(relapath): ''',e,datetime.now())


    for link in links[1:]:
        ticker=None
        driver.get(link)
        try:
            time.sleep(3)
            alert = driver.switch_to.alert
            alert.accept()

            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass
        
        if ticker==None:
            ticker=str(int(datetime.now().timestamp()))

        filename=ticker+'.png'
        relapath=f'data/screenshots/{folder}/{filename}'
        # relapath=f'/Users/mac1/Documents/a1_data/{folder}/{filename}'
        time.sleep(1)

        for _ in range(3):
            try:
                print('''> try: driver.save_screenshot(relapath)''',datetime.now())
                driver.save_screenshot(relapath)
                break
            except Exception as e:
                time.sleep(5)
                print('''>> error: driver.save_screenshot(relapath): ''',e,datetime.now())

        # driver.get('https://www.google.com/')


    # driver.get(link) 
    driver.get('https://www.google.com/')
    try:
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()

        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    driver.quit()


    s3_upload(folder1, country)
    to_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/daily_download/{country}'
    if not os.path.exists(to_folder):
        os.makedirs(to_folder)

    remove_files(to_folder)    
    copy_paste(folder1,to_folder)
    
    remove_files(folder1)




def polygon_stock_list_5000_realtime():
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
    
    df=pd.DataFrame()
    


    i=0
    for i in range(len(stock_list)):
        try:
            ticker=stock_list[i]
            print('ticker: ',ticker)
            endpoint=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
            response = requests.get(endpoint)
            # Raise an error if the request failed
            response.raise_for_status()
            # Parse the JSON result
            data = response.json()
            
            json_data=data['results']
            
            new_row = pd.DataFrame(json_data, index=[0])

            # Append the new row to the DataFrame
            df = pd.concat([df, new_row], ignore_index=True)
            df
        except Exception as e:
            print(ticker,i,e)

    
    df1=df[df['type']=='CS']
    # [['ticker','market_cap','primary_exchange']]

    df1=df1.sort_values(by='market_cap',ascending=False)

    df1=reset_index(df1)
    df1
    stock_list=df1['ticker'].values.tolist()
    return stock_list



def mongo_update_polygon_stocks():
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
    stock_list



    #%%
    # stock_list.remove('AAPL')
    # stock_list.remove('MSFT')
    # stock_list.remove('NVDA')
    # stock_list.remove('TSLA')
    #%%
    do=mongo_get_df('stock','polygon_stocks')

    dn=pd.DataFrame(stock_list)
    dn.columns=['ticker']
    dn

    #%%
    set_do = set(do['ticker'])
    set_dn = set(dn['ticker'])

    # Find new values (present in dn but not in do)
    new_values = set_dn - set_do

    # Find no longer existing values (present in do but not in dn)
    no_longer_existing = set_do - set_dn

    # Convert the sets to lists (if needed)
    new_values_list = list(new_values)
    no_longer_existing_list = list(no_longer_existing)

    print("New values:", new_values_list)
    print("No longer existing:", no_longer_existing_list)

    #%%
    new_values_list
    #%%
    dnn = df_total[df_total['ticker'].isin(new_values_list)]
    dnn

    # %%


    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient['stock']

    # Access a collection in the database
    collection = db['polygon_stocks']


    #%%
    for ticker in no_longer_existing:
        result = collection.delete_many({'ticker': ticker})
        print("result: ",result)
    if len(dnn)>0:
        mongo_insert(dnn,'ticker','stock','polygon_stocks')




def find_exchange_v2(ticker):


    url = f"https://finance.yahoo.com/quote/{ticker}"

    querystring = {"p":ticker}

    payload = ""
    headers = {"User-Agent": "insomnia/8.5.0"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # print(response.text)
    # //div[@class="C($tertiaryColor) Fz(12px)"]
    TAG='div'
    class_name = "C($tertiaryColor) Fz(12px)"

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.text

    elements = soup.find_all(TAG, class_=class_name)
    exchange_info=elements[0].find('span').text
    exchange_info=exchange_info.lower()

    exchange='NYSE'
    if exchange_info.startswith('nasdaq'):
        exchange='NASDAQ'
    elif exchange_info.startswith('nyse'):
        exchange='NYSE'
    return exchange


def find_exchange_v3(ticker):
    print("ticker: ",ticker)
    #https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
    import requests,json
    url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
    response=requests.get(url)

    json1=response.json()
    stock_name=json1['results']

    exchange1=stock_name['primary_exchange']
    exchange1

    if exchange1=='XNAS':
        exchange='NASDAQ'
    elif exchange1=='XNYS':
        exchange='NYSE'
    else:
        exchange='AMEX'
    return exchange
#%%
def generate_fullname_tradingview(ticker):
    try:
        exchange=find_exchange_v3(ticker)
    except:
        exchange=find_exchange_v2(ticker)
    return f'{exchange}:{ticker}'
