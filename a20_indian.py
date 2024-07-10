#%%
from import_tradingview import *




#%%
ticker='TCS'
start_date = date(2023, 1, 1)
end_date = date(2023, 1, 10)
print(eq.get_price(start_date, end_date, symbol=ticker))
start_date = "01-05-2023"
end_date = "03-05-2023"
print(eq.get_corpinfo(start_date, end_date, symbol=ticker))
print(eq.get_event(start_date, end_date))
print(eq.get_event())
print(eq.get_marketstatus())
print(eq.get_marketstatus(response_type="json"))
print(eq.get_companyinfo(symbol=ticker))
print(eq.get_companyinfo(symbol=ticker, response_type="json"))
print(eq.get_chartdata(symbol=ticker))
print(eq.get_symbols_list()) #print the list of symbols used by NSE for equities
print(eq.get_asm_list(asm_type = "shortterm"))

# %%

price_now=eq.get_price(start_date, end_date, symbol=ticker)
print("price_now: ",price_now)
stock_list=eq.get_symbols_list()
stock_list

#%%
price_now
# %%
print("\n>> len(stock_list)= ", len(stock_list))

# %%
asm_list=eq.get_asm_list(asm_type = "shortterm")
print("\n>> len(asm_list)= ", len(asm_list))

# %%

# %%fullname
fullname='NSE:MRF'
minute1='1D'
df=tradingview_simple(fullname,minute1)
# %%
df
# %%


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


# %%
title='MAX India NSE - '
stock_list=eq.get_symbols_list()

max200_email_NSE_india(stock_list,title)
# %%
