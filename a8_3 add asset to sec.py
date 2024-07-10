#%%
from import_stocks import *
#%%

def prepared_df(ticker,minute1,limit1,past1,today1):
    df=polygon_v3(ticker,minute1,limit1,past1,today1)
    df['Date']=[datetime.fromtimestamp(item,tz=pytz.timezone("US/Eastern")) for item in df['Timestamp']]
    df=feature_engineering(df)    
    return df


def download_10k(ticker):
    dl.get("10-K", ticker, limit=1)
    time.sleep(3)
    folder=f'sec-edgar-filings/{ticker}'
    sub2=os.listdir(folder)[0]
    sub3=os.listdir(os.path.join(folder,sub2))[0]
    txt1=os.listdir(os.path.join(folder,sub2,sub3))[0]
    path1=os.path.join(folder,sub2,sub3,txt1)
    with open(path1,'r') as file:
        data=file.read()
    return data

def get_data_from_10k(ticker,data):
    TARGET_NAME='>business<'.lower()

    # TARGET_NAME='ITEM 7.'
    split_list=data.lower().split(TARGET_NAME)
    if len(split_list)>3:
        splited_list=data.lower().split(TARGET_NAME)[1].split('\n')[:20]
    else:
        splited_list=data.lower().split(TARGET_NAME)[-1].split('\n')[:20]
    print("\n>> len(splited_list)= ", len(splited_list))

    text1="".join(splited_list)




    cleaned_text = re.sub('<[^>]+>', '', text1)[:4000]

    print("\n>> len(cleaned_text)= ", len(cleaned_text))


    url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
    response=requests.get(url)
    
    json1=response.json()
    stock_name=json1['results']['name']
    stock_name

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based which products/services this company make. why is it better than competitors. what kind of customers will buy and why"
    define='Does it include business description of the company, what products this company sells, and why customers buy from them?'
    answer1=gpt_answer(define,cleaned_text)
    answer1

    
    # TARGET_NAME='>risk factors<'
    TARGET_NAME='item 1a.'
    TARGET_NAME=TARGET_NAME.lower()
    split_list=data.lower().split(TARGET_NAME)
    cleaned_text=split_list[-1]
    cleaned_text = re.sub('<[^>]+>', '', cleaned_text)[:4000]

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based on what are important events that happened for the company. If it has any financial numbers or other numbers, give me summary with the numbers."
    define='Does it include risk factors for this company?'
    answer2=gpt_answer(define,cleaned_text)
    answer2



    TARGET_NAME='DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERA'
    TARGET_NAME=TARGET_NAME.lower()
    split_list=data.lower().split(TARGET_NAME)
    cleaned_text=split_list[-1].split('overview')[-1]
    cleaned_text = re.sub('<[^>]+>', '', cleaned_text)[:4000]

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based on what are important events that happened for the company. If it has any financial numbers or other numbers, give me summary with the numbers."
    define='Does it include good news or bad news for the company?'
    answer3=gpt_answer(define,cleaned_text)
    answer3
    return answer1,answer2,answer3

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
            df=prepared_df(ticker,minute1,limit1,past1,today1)

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
