from a31_2_save_stock_analy_com import *


update_stock_analysis_com_5000_v1()
while True:
    print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    if (datetime.now(timezone('US/Eastern')).strftime("%A"))=='Sunday' :
        if  1100<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<1105:
            try:
                print('''> try: update_stock_analysis_com_5000_v1()''',datetime.now())
                update_stock_analysis_com_5000_v1()
            except Exception as e:
                print('''>> error: update_stock_analysis_com_5000_v1(): ''',e,datetime.now())


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
        pass
    # execute once every minute
    if int(datetime.now().strftime("%S"))==1 or int(datetime.now().strftime("%S"))==2 : 
        pass
    # execute once every 2 min
    if int(datetime.now().strftime("%M"))%2==0 and int(datetime.now().strftime("%S"))==1:
        pass