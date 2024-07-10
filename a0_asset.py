#%%
# add path for the libraries.     from t_mini import * 
import t_mini_basics as basics
import t_mini_examine as examine
import t_mini_pnl as pnl
import t_mini_model as model
from t_mini_tradingview import *
sys.path.pop(-1)
import json
import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)

#%%
from twilio.rest import Client
import yagmail
from datetime import datetime,timedelta
import pandas as pd
# Your Account SID from twilio.com/console

newsapi_org='{newsapi_org}'

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



import yfinance as yf

import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

def gpt_answer(define,question):
    try:
        

        content=question
        message_list3=[{"role": "system", "content" : define},
                    {"role": "user", "content" : str(content)},    
                    ]
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo" , #"gpt-3.5-turbo", 
                    messages = message_list3)['choices'][0]['message']['content']
    except Exception as e:
        completion='>> error = time out for gpt...'+str(e)
    return completion

def get_stock_details(ticker):
    market_cap,industry, short_description,company_name,PE=0,0,0,0,0
    try:
        stock = yf.Ticker(ticker)
        
        # Info is a dictionary containing various details about the stock
        info = stock.info
        
        market_cap = stock.info.get('marketCap')
        market_cap=round(market_cap/1000000000,2)
        industry = info.get('industry', 'N/A')
        short_description = info.get('longBusinessSummary', 'N/A')
        company_name = short_description.split('.')[0]
        company_name
        PE = info.get('trailingPE')
    except Exception as e:
        print('error here 13: ',ticker,e)
        try:

            endpoint=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
            response = requests.get(endpoint)
            # Raise an error if the request failed
            response.raise_for_status()
            # Parse the JSON result
            data = response.json()

            json_data=data['results']

            new_row = pd.DataFrame(json_data, index=[0])
            short_description=new_row['description'][0]
            market_cap=new_row['market_cap'][0]
            market_cap=round(market_cap/1000000000,2)
            company_name=new_row['name'][0]
        except Exception as e:
            print('double error ',ticker,e)
            
    return market_cap,industry, short_description,company_name,PE

from newsapi import NewsApiClient

def fetch_news_for_query(api_key, query, language='en', page_size=5):
    newsapi = NewsApiClient(api_key=api_key)

    # Search for articles with the given query
    articles = newsapi.get_everything(q=query,
                                      language=language,
                                      sort_by="relevancy",  # Sort by relevancy to the query
                                      page_size=page_size)

    articles_list = articles.get('articles')
    if not articles_list:
        print("No news found!")
        return
    list1=[]
    for article in articles_list:
        title = article.get('title')
        description = article.get('description')
        print(f"Title: {title}")
        # print(f"Description: {description}\n")
        list1.append((title,description))
    return list1

def check_20_assets_sma200_above():

    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    dw

    de=total.read_excel(f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/list_of_assets.xlsx')
    de=total.reset_index(de)
    de


    fullname_list=[]
    webname_list=[]
    for i in range(len(de)):
        webname=str(de['web_name'][i])
        if 'symbol' in webname:
            webname=webname.split('=')[1]
            ticker2=webname.split("%")
            part2=ticker2[1].replace("3A","")
            if len(ticker2)>2:
                
                fullname=ticker2[0]+":"+part2+"!"
            else:
                fullname=ticker2[0]+":"+part2
            fullname
            webname_list.append(webname)
            fullname_list.append(fullname)
            print(fullname)
            print(' ')


    list5=[]
    minute1='1D'
    for fullname in fullname_list:
        try:
            df=tradingview1(fullname,minute1)
            df
            while True:

                tot=len(df)-1
                print(fullname,'  ',df['Date'][tot])

                date2=df['Date'][tot]
                date2

                if 'nan' in str(date2).lower() or 'nat' in str(date2).lower():
                    print('drop last row')
                    df = df.iloc[:-1 , :]
                else:
                    break


        
            link_symbol=fullname.replace(":","%3A").replace("!","%21")
            link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
            link_symbol
        
            
            tot=len(df)-1
            print(fullname,'  ',df['Date'][tot])
            print(' ')
            for i in range(10):
                close1=df['Close'][tot-i]
                sma200=df['SMA200'][tot-i]
                close1_2=df['Close'][tot-i-1]
                sma200_2=df['SMA200'][tot-i-1]
                date1=df['Date'][tot-i]
                if close1>sma200:
                    if close1_2<sma200_2:
                        print(i)
                        print(date1)
                        print('close > sma200')
                        list5.append((fullname,date1,close1,sma200,'above',f'{fullname}_{date1}'))
                if close1<sma200:
                    if close1_2>sma200_2:
                        print(' ============')
                        print(i)
                        print(df['Date'][tot-i])
                        print('close < sma200')
                        list5.append((fullname,date1,close1,sma200,'below',f'{fullname}_{date1}'))
                        print(' ----')  
        except Exception as e:
            print(e)
            send_email(sender,f'error - {fullname}',f'{fullname},{e}')



    if len(list5)>0:
    
        dw2=pd.DataFrame(list5)
        dw2.columns=['fullname','date','close','sma200','direction','fullname_date']
        dw2

        dw3=dw2[~dw2['fullname_date'].isin(dw['fullname_date'])]
        dw3=total.reset_index(dw3)
        dw3
        if len(dw3)>0:
        
            for i in range(len(dw3)):
                above1=str(dw3['direction'][i])
                
                fullname=str(dw3['fullname'][i])
                date1=str(dw3['date'][i])
                close1=str(dw3['close'][i])
                sma200=str(dw3['sma200'][i])
                fullname_date=str(dw3['fullname_date'][i])
                ticker=fullname.split(':')[1].replace("1!","")
                link_symbol=fullname.replace(":","%3A").replace("!","%21")
                link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
                
                if 'above' in above1:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
                else:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
    
        print('start = saving dw to csv')
        dw=pd.concat((dw,dw2),axis=0)
        dw=dw.drop_duplicates(keep="last",subset='fullname_date')
        dw=total.reset_index(dw)
        
        dw.to_csv(alarm1)
        dw
        print('success = saving dw to csv')
def seven_days_alarm():
    print('seven days - alarm check')
    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    
    for item in list(set(dw['fullname'].values)):


        string1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['date'][-1:].values[0]
        above1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['direction'][-1:].values[0]
        fullname=item
        datetime1=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=7)
        link_symbol=fullname.replace(":","%3A").replace("!","%21")
        link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'

        days_7=datetime.strftime(datetime1 ,"%Y-%m-%d")
        

        today1=(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d"))
        if today1==days_7:
            send_email(email1,title=f't2: {item} has been 7 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 7 days passed..')

        datetime2=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=14)
        days_14=datetime.strftime(datetime2 ,"%Y-%m-%d")
        if today1==days_14:
            send_email(email1,title=f't3: {item} has been 14 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 14 days passed..')



def futures_expiration_email():
    day1=3
    path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/2 futures expiration definition/win2_IBKR_Futures2.csv'
    da=total.read_csv(path1)
    da=total.reset_index(da)
    da
    for i in range(len(da)):
        expiry1=str(da['expiry'][i])
        symbol=da['symbol'][i]
        sectype=da['sectype'][i]
        exch=da['exch'][i]
        local=da['local'][i]
        all1=str(da.iloc[i])
        date1=datetime.strptime(expiry1, "%Y%m%d")
        date2=date1-timedelta(days=day1)

        date2=datetime.strftime(date2 ,"%Y-%m-%d")
        date2
        timedelta1=0
        timedelta2=100
        today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
        today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
        past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
        past2=datetime.strptime('20210218', "%Y%m%d").timestamp()

        if today1==date2:
            print(i,symbol,sectype,expiry1,exch,local)
            send_email(email1,title=f'futures expiration: {symbol} will be expired in {day1} days.',content=f'{symbol}_{sectype}_{expiry1}_{exch}_{local}')




def find_exchange(ticker):


    df1=pd.read_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx",index_col=0)
    exchange1=0
    for i in range(len(df1)):
        if ticker == df1['ticker'][i]:
            exchange1=df1['Exchange'][i]
            #print("existing ticker exchange",ticker)
    if exchange1==0:
        print("not existing exchange info : ", ticker)
        
        url = "https://ycharts.com/companies/{}".format(ticker)
        payload = ""
        headers = {
            "cookie": "ycsessionid=2qz3d4y9pia7lsirwduwfoqsy68lxo0u; _ga=GA1.2.635129160.1644138754; _gid=GA1.2.916019816.1644138754; __gads=ID=93bc25b5583902a4-22af5cc377d00013:T=1644138753:S=ALNI_MZo9l0xXkE31mqmewQtnKQnTUUD5Q; __hstc=69688216.203ddbd23f614854901d1b6290dd0cc4.1644138757373.1644138757373.1644138757373.1; hubspotutk=203ddbd23f614854901d1b6290dd0cc4; __hssrc=1; _fbp=fb.1.1644138757715.487408360; _gcl_au=1.1.38652961.1644138758; quickflowsSingleSecurityCookieName=%7B%22displaySecurityId%22%3A%22AAPL%22%2C%22securityId%22%3A%22AAPL%22%7D; messagesUtk=a7090410a7a24598b5f7b00924eb45a1; page_view_ctr=3; __hssc=69688216.3.1644138757373",
            "authority": "ycharts.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://www.google.com/",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        data=response.text
        exchange1=data.split("&nbsp;|&nbsp;")[1].split("\n")[1].replace(" ","")

        print("scrape ychart", ticker, exchange1)
        dictionary={"ticker":[ticker],"Exchange":[exchange1]}

        df=pd.DataFrame.from_dict(dictionary)
        df1=df1.append(df)
        df=df1.append(df)
        df=df.drop_duplicates(keep="last",subset="ticker")
        df=df.reset_index()
        df=df.drop(columns=["index"])
        df.to_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx")
    return exchange1


def read_excel(path):
    if 'csv' in path:
        df=pd.read_csv(path,index_col=0)
    else:
        df=pd.read_excel(path,index_col=0)
    if 'index' in df.columns:
        df=df.drop(columns=["index"])
    if 'level_0' in df.columns:
        df=df.drop(columns=["level_0"])
    if 'Unnamed: 0' in df.columns:
        df=df.drop(columns=['Unnamed: 0'])    
    return df

def common_stock_list_v1_5000_polygon_real_time():
    if 'win' in socket.gethostname():
        socket_path='G:/My Drive/'
        csv2='G:/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    else:
        socket_path=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/'
        csv2=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    # csv2=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    # da=total.read_csv(csv2)
    da=read_excel(csv2)
    da
    da=da.sort_values(by='market_cap',ascending=False)
    da
    da['mc1']=[int(item/1000000) for item in da['market_cap'].values]
    common_stock_list_v1=da['Ticker'].values.tolist()
    return common_stock_list_v1


from datetime import datetime,timedelta
import requests
import pandas as pd

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

def generate_company_name(ticker):
    
    endpoint=f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}"
    # Make the request
    response = requests.get(endpoint)

    # Raise an error if the request failed
    response.raise_for_status()

    # Parse the JSON result
    data = response.json()
    data
    print("data: ",data)

    company_name=data['results']['name'].split('.')[0]
    print("company_name: ",company_name)
    return company_name

def stock_list_11000():
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
    return stock_list

def stock_list_5000():
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
def max200_email():
    # stock_list=common_stock_list_v1_5000_polygon_real_time()
    print("max200 started")
    # stock_list=stock_list_11000()
    stock_list=stock_list_5000()
    stock_list

    ticker_=[]
    content_=[]

    limit1=2000
    minute1='1'
    beta2=0
    past1=datetime.strftime(datetime.now()-timedelta(2000) ,"%Y-%m-%d")
    today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
    print(past1,today1)

    ticker='AAPL'
    for ii,ticker in enumerate(stock_list):
        try:
            print("ticker: ",ticker,ii)
            # for ticker in polygon_list:
            df=polygon_v3(ticker,minute1,limit1,past1,today1)
            df
            df['Date']=[datetime.fromtimestamp(item,tz=pytz.timezone("US/Eastern")) for item in df['Timestamp']]
            df



            df=feature_engineering(df)

            if df['Close'][len(df)-1]>df['MAX200'][len(df)-2]:
                print('yes max200 crossed',ticker,ii)
                content_.append('\n')
                # content_.append(ticker)
                MC,industry, description,company_name,PE_ratio = get_stock_details(ticker)
                
                description_summary=gpt_answer("summarize what they do? why customers buying from them? why their products are better than other competitors?",description)
                content_.append('_____________________________________________________')
                content_.append(f'{ticker} \nMC: ${MC}B / \nPE: {round(PE_ratio,3)} / \nindustry:{industry} / \n>description: {description} \n>summary: {description_summary}')
                company_name= generate_company_name(ticker)
                news=fetch_news_for_query(newsapi_org, query=f'{company_name}',page_size=10)
                # news=fetch_news_for_query(newsapi_org, query=f'{ticker} stock',page_size=10)
                news=str(news)
                define=f'summarize based on why the {company_name} stock is going up.'
                news=gpt_answer(define,news)
                try:
                    exchange1=find_exchange(ticker)
                    
                    ticker_.append(ticker)
                    
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'

                    content_.append(content)
                    content_.append(news)
                except:
                    ticker_.append(ticker)
                    exchange1='NASDAQ'
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'            
                    content_.append(content)
                    content_.append(news)
                    exchange1='NYSE'
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'
                    content_.append(content)
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
    subject_=f'MAX200_{ticker__}'
    yag.send(to=sender,subject=subject_,contents=content__)
    
    print('end - send email... v1')



# try:
#     max200_email()
# except Exception as e:
#     print('exception for masx200',e)
    
# check_20_assets_sma200_above()
# seven_days_alarm()
while True:
    # print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    # execute once every minute
    #between 7pm to 11:59pm
    if 1900<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<2359:
        pass
    # eastern us market hour:
    if 930<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<1600 :
        if (datetime.now(timezone('US/Eastern')).strftime("%A"))!='Sunday' and (datetime.now(timezone('US/Eastern')).strftime("%A"))!='Saturday':
        # everry 15min :
            if (datetime.now().strftime("%M%S"))=='0001' or (datetime.now().strftime("%M%S"))=='1501' or (datetime.now().strftime("%M%S"))=='3001' or (datetime.now().strftime("%M%S"))=='4501': 
                pass
    if int(datetime.now().strftime("%S"))==1 or int(datetime.now().strftime("%S"))==2 : 
        pass
        try:
            pass
        except:
            pass
    # execute once every hour
    if (datetime.now().strftime("%M%S"))=='1553' : 
        pass
    # execute once everyday
    if (datetime.now().strftime("%H%M%S"))=='142559' : 
        try:
            check_20_assets_sma200_above()
        except:
            print('some error for check_20_assets_sma200_above()')

        try:
            seven_days_alarm()
        except:
            print('some error for seven_days_alarm()')

        try:
            futures_expiration_email()
        except:
            print('some error for futures_expiration_email()')

        try:
            max200_email()
        except Exception as e:
            print('exception for masx200',e)
            
# %%
