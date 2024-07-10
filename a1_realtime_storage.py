#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


{add_path_for library}from t1_import_total import *

import getpass,sys,socket
# add path for the libraryfrom t10_stock import *
sys.path.pop(-1)


folder1='/Volumes/A1/2_ibkr/trash/4_realtime_storage/'
list1=os.listdir(folder1)
list1
# %% /Users/macpro1/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/a1_realtime_storage.py
list1.sort()
# %%
list1
# %%
ticker1='LTC'
side='SELL'
list2=[]
for item in list1:
    if '.csv' in item and '2023' in item:
        df=read_excel(folder1+item)
        item3=df[(df['ticker1']==ticker1) & (df['side']==side)].values.tolist()
        print(item3)
        if len(item3)!=0:
            list2.append(item3[0])
#%%
list2
#%%
for ii,item in enumerate(list2):
    try:
        if 'OMEGA' in item[9]:
            break
    except:
        pass

list2=list2[ii:]
#%%
dt=pd.DataFrame(list2)
dt
# %%
open_excel(dt)
# %%
