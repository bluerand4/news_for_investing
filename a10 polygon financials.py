#%%

import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)

from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

from import_stocks import *
#%%
tickers=['ZS','NET','CRWD','NOW','NU','KTOS','DDOG','DCBO','CLS','QLYS','PCAR','MLM','GRMN','PTC','FDS','DKNG','AKAM','VRT','MANH','NTNX','GWRE','FIX','ENSG','OBDC','GPI']

ticker=tickers[2]
ticker='NOW'
list1=[]
for ticker in tickers:
    try:
        do=financials(ticker)


        column_target='revenues'
        # column_target='gross_profit'
        # column_target='net_income_loss'

        numbers=do[column_target].dropna().values.tolist()
        numbers = remove_outliers(numbers)
        min1=min(numbers)
        max1=max(numbers)
        numbers2=[(item -min1)/(max1-min1) for item in numbers]
        numbers2

        # for item in do.columns:
        #     if 'gross' in item:
        #         print("item: ",item)

        slope1,intercept=regression(numbers)
        slope1

        slope2,intercept=regression(numbers2)
        slope2








        per,mc,div=get_pe_mc_div(ticker)
        per
        if per =='nan':
            score=slope2/1000*100000
        else:
            score=slope2/per*100000

        score
        list1.append((ticker,score,slope2,per,mc,div))
    except Exception as e:
        print( 0 ,' = >>> some error = ',e)
    
# %%
dg=pd.DataFrame(list1)
dg
dg=dg.sort_values(by=2,ascending=False)
dg
# %%
per
# %%

for item in do.columns:
    if 'revenue' in item:
        print("item: ",item)
# %%
do.columns
# %%
per,mc,div=get_pe_mc_div('VRT')
per
# %%


ticker='DKNG'
#%%
revslope,inslope,do=draw_slope(ticker)
revslope=round(revslope*1000,1)
inslope=round(inslope*1000,1)
#%%
import requests
from bs4 import BeautifulSoup
import requests
ticker='WMT'




