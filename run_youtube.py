#%%
#%%
from import_stocks2 import *
from import_tradingview import *
# #%%
# youtuber = YoutuberDummyParameters()
#%%
# generate_total_news()
# max200_email_NSE_india()
# max200_email_NSE_india(eq.get_symbols_list(),'MAX India NSE - ')

try:
    bool_news_generate=check_mongo_new_tickers()
    bool_news_generate
except:
    bool_news_generate=False

if bool_news_generate:
    print('start bool news')
    generate_tradingview_screenshots()
    generate_tradingview_audio()
    generate_tradingview_video()
    combine_video('stocks_news_')
    youtube_upload_and_remove()
    print('done')
#%%/Users/mac1/Documents/2_code/t6_trading_news/a19_pro2.py
while True:
    print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)

    # execute once everyday
    if (datetime.now(timezone('US/Eastern')).strftime("%H%M%S"))=='172559' : 
        
        generate_total_news()
        # max200_email_NSE_india()
        # max200_email_NSE_india(eq.get_symbols_list(),'MAX India NSE - ')
        
        try:
            bool_news_generate=check_mongo_new_tickers()
            bool_news_generate
        except:
            bool_news_generate=False

        if bool_news_generate:
            print('start bool news')
            generate_tradingview_screenshots()
            generate_tradingview_audio()
            generate_tradingview_video()
            combine_video('stocks_news_')
            youtube_upload_and_remove()
            print('done')

        country_list=['us_stock_close2_max1','us_stock_max2_max1','india_stock_close2_max1']
        for country in country_list:
            try:
                print('''> try: collect_screenshots(country)''',datetime.now())
                collect_screenshots(country)
            except Exception as e:
                print('''>> error: collect_screenshots(country): ''',e,datetime.now())


        if (datetime.now(timezone('US/Central')).strftime("%A"))=='Sunday':
            mongo_update_polygon_stocks()
    
    # execute once HR hour
    HR = 1  
    if int(datetime.now().strftime("%H")) % HR == 0 and int(datetime.now().strftime("%M")) == 0:
        pass

    # execute once MI min
    MI=1
    if int(datetime.now().strftime("%M"))%MI==0 and int(datetime.now().strftime("%S"))==1:
        pass
    
#%%

while True:
    print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    
    #between 7pm to 11:59pm
    if 1900<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<2359:
        pass
    # eastern us market hour:
    if 930<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<1600 :
        if (datetime.now(timezone('US/Eastern')).strftime("%A"))!='Sunday' and (datetime.now(timezone('US/Eastern')).strftime("%A"))!='Saturday':
        # everry 15min :
            pass
    # central US market hours open
    central_market=1
    if (datetime.now(timezone('US/Central')).strftime("%A"))=='Saturday':
        central_market=0
    elif (datetime.now(timezone('US/Central')).strftime("%A"))=='Sunday':
        if int(datetime.strftime(datetime.now(timezone('US/Central')) ,"%H%M"))<1655 :
            central_market=0
    elif (datetime.now(timezone('US/Central')).strftime("%A"))=='Friday':
        if 1805<int(datetime.strftime(datetime.now(timezone('US/Central')) ,"%H%M")) :
            central_market=0
    if central_market==1:
        print('execute here')

    # execute once every minute
    if int(datetime.now().strftime("%S"))==1 or int(datetime.now().strftime("%S"))==2 : 
        pass
    # execute once every 2 min
    if int(datetime.now().strftime("%M"))%2==0 and int(datetime.now().strftime("%S"))==1:
        pass
    # execute once every hour
    if (datetime.now().strftime("%M%S"))=='1553' : 
        try:
            main1()
        except:
            pass
    # execute once everyday
    if (datetime.now().strftime("%H%M%S"))=='182559' : 
        pass
#%%
#%%
#%%
#%%
#%%
#%%
#%%##############################################
#p2 
