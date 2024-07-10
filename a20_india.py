#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


from nsepy import get_history
from datetime import date
data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
data[['Close']].plot()
#%%
from datetime import date
from nsepy import get_history
# Stock futures (Similarly for index futures, set index = True)
stock_fut = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        futures=True,
                        expiry_date=date(2015,1,29))
stock_fut
# %%
