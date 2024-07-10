#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


# %%
obj1=1
dict1=dict(obj1=obj1)
dict1
# %%
import torch
X=torch.tensor(1)
y_hat0=torch.tensor([1,2,3])
y_hat=torch.tensor([1,2,3])
SIDE='hi'
RSIDE=1
TRUSTED_SIDE2=[1,2,3]

def print11(filename,*content):
    if not os.path.exists('7_print1'):
        os.makedirs('7_print1')

    with open(f'7_print1/{filename}.txt', 'a') as f:
        # Write to file
        f.write(f'{str(content)} <- {datetime.now()} -> \n')
ticker1='BTC'
side='BUY'
keys='X,y_hat0,y_hat,SIDE,RSIDE,TRUSTED_SIDE2'.split(',')
values=X,y_hat0,y_hat,SIDE,RSIDE,TRUSTED_SIDE2
list2=zip(keys,values)
for key,value in list2:
    try:
        print11(f'v4_{ticker1}_{side}_y_hat',str({key:value}))
    except:
        pass
# %%

# %%
