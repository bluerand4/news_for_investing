#%%
from import_major import *
import numpy

'''

1. run for update stock analysis.com occasionally for 5000 stocks financials

'''





import pytz

timezone1 = pytz.timezone('US/Eastern')
print('start')
while True:
    # print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    if (datetime.now(timezone('US/Eastern')).strftime("%A"))=='Sunday':
        if datetime.now(timezone1).strftime("%H%M%S") == '062559':        
            try:
                print('''> try: stock_analysis_com_update_financials_5000()''',datetime.now())
                stock_analysis_com_update_financials_5000()
                print('done --> stock_analysis_com_update_financials_5000')
            except Exception as e:
                print('''>> error: stock_analysis_com_update_financials_5000(): ''',e,datetime.now())



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



while True:
    # Getting the current time in US Eastern Time Zone
    now_eastern = datetime.now(timezone1).strftime("%H:%M:%S")
    print(now_eastern)
    time.sleep(1)

    # Execute once everyday at 06:25:59 AM Eastern Time
    if datetime.now(timezone1).strftime("%H%M%S") == '062559':
        pass

    # Execute once every hour
    HR = 1
    if int(datetime.now(timezone1).strftime("%H")) % HR == 0 and int(datetime.now(timezone1).strftime("%M")) == 0:
        # Your hourly code here
        pass

    # Execute once every minute
    MI = 1
    if int(datetime.now(timezone1).strftime("%M")) % MI == 0 and int(datetime.now(timezone1).strftime("%S")) == 1:
        # Your minutely code here
        pass