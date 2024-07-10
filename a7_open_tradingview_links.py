#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

import webbrowser

links=['https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ARACE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ATT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAFL', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AWELL', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ANU', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACOR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AIT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACAH', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AGRMN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=BATS%3ACBOE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ALDOS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ARBA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AGDDY', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AMORN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACHE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ASWN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACYBR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWFRD', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AINFA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AQLYS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ANEWR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABRBR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AESAB', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ASUN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AMOG.A', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AFG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ALOPE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AMOG.B', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABSM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAGO', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AESMT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAEO', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AANF', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AKNF', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AKAI', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AAGYS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAROC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AATGE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AGVA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHNI', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACNXN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWINA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AGIII', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYAM%3ANHC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ATHR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AOLMA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AALPN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AWSR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AGAIN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ANBN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYAM%3ANCL', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AALTO', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ATRHC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AEPIX', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AFSTR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHRTG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AHCMA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWRAP', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYAM%3AQFTA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ANRAC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AESOA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AOXUS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AYHGJ', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ADUNE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACPBI', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABFX', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ANOVV']
links="['1','2']"
# links=input('lists = ')
import pyperclip
links=pyperclip.paste()
links = ast.literal_eval(links)
sum1=0
for item in links:
    webbrowser.open(item)
    sum1+=1
    if sum1>50:
        while True:
            if input('next')=='next':
                print('here 2')
                break
            print('here 1')
        sum1=0