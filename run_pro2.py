#%%
from import_major import *


# driver=open_driver()
#%%
import pytz
print('start')
from a37_3_just_save_seeking_data import *
save_seeking_alpha_analyst_reports()
from a37_2_loop_seek_alpha import *
# youtube_seek_alpha_v1()
timezone1 = pytz.timezone('US/Eastern')
make_google_drive_stock_v1()
make_google_drive_stock_v2()
make_google_drive_stock_v4()

from a30_2_save_ohlcv_5000 import *

from a30_3_save_ohlcv_polygon import *




while True:
    # print((datetime.now().strftime("%H:%M:%S")))
    time.sleep(1)
    
    #between 7pm to 11:59pm
    if 1900<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<1910:
            
        make_google_drive_stock_v1()
        make_google_drive_stock_v2()
        make_google_drive_stock_v4()

        try:
            print('''> try: youtube_seek_alpha_v1()''',datetime.now())
            youtube_seek_alpha_v1()
        except Exception as e:
            print('''>> error: youtube_seek_alpha_v1(): ''',e,datetime.now())


        try:
            print('''> try: save_seeking_alpha_analyst_reports()''',datetime.now())
            save_seeking_alpha_analyst_reports()
        except Exception as e:
            print('''>> error: save_seeking_alpha_analyst_reports(): ''',e,datetime.now())
        
        try:
            print('''> try: save_csv_daily_tradingview_ohlcv()''',datetime.now())
            save_csv_daily_tradingview_ohlcv()
        except Exception as e:
            print('''>> error: save_csv_daily_tradingview_ohlcv(): ''',e,datetime.now())

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
        # print('execute here')
        pass
    # execute once every minute
    if int(datetime.now().strftime("%S"))==1 or int(datetime.now().strftime("%S"))==2 : 
        pass
    # execute once every 2 min
    if int(datetime.now().strftime("%M"))%2==0 and int(datetime.now().strftime("%S"))==1:
        pass
    # execute once every hour
       
    # execute once everyday
    if (datetime.now().strftime("%H%M%S"))=='182559' : 
        pass