#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)
from torch.optim.lr_scheduler import StepLR
import torch,os,time
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.distributed import init_process_group, destroy_process_group
from torch.utils.data import DataLoader, TensorDataset
from multiprocessing import Pool, cpu_count
import torch.multiprocessing as mp
import torch.distributed as dist
from torch.utils.data.distributed import DistributedSampler
from torch.nn.parallel import DistributedDataParallel as DDP
import pytz
from pytz import timezone
if torch.backends.mps.is_available():
    device='mps'
elif torch.cuda.is_available():
    device='cuda'
else:
    device="cpu"

DEVICE=device

def random_seed(m):
    random.seed(m)
    torch.manual_seed(m)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(m)
        torch.cuda.manual_seed_all(m)
    np.random.seed(m)
random_seed(1)

def weekly_ohlcv(ticker,rolling_n=10,z_score=1.5):
    timedelta1=0
    timedelta2=365*5
    today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
    today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
    past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
    past2=datetime.strptime('20210218', "%Y%m%d").timestamp()
    today1

    url=f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{past1}/{today1}?adjusted=true&sort=asc&limit=50000&apiKey={polygon_api_key}'
    response=requests.get(url)

    json1=response.json()
    df=pd.DataFrame(json1['results'])
    df

    df['t']=df['t']/1000
    dlist=[]
    for i in range(len(df)):
        timestamp1=df['t'][i]
        dt2=datetime.fromtimestamp(timestamp1,tz=pytz.timezone("US/Eastern"))
        # string1=datetime.strftime(dt2 ,"%Y-%m-%d %H:%M:%S")
        string1=datetime.strftime(dt2 ,"%Y-%m-%d")
        string1
        # df.loc[i,'d']=string1
        dlist.append(string1)
    df['d']=dlist
    df



    df


    df=df.rename(columns={"o":"Open"})
    df=df.rename(columns={"h":"High"})
    df=df.rename(columns={"l":"Low"})
    df=df.rename(columns={"c":"Close"})
    df=df.rename(columns={"v":"Volume"})
    df=df.rename(columns={"t":"Timestamp"})

    # tradingview_complex(df,blue_marker='mark')

    # import pandas as pd

    # Assuming df is your existing DataFrame with a datetime index
    # For example:
    # df = pd.DataFrame({
    #     'Open': [...],
    #     'High': [...],
    #     'Low': [...],
    #     'Close': [...],
    #     'Volume': [...]
    # })
    # df.index = pd.to_datetime([...])  # Replace [...] with your datetime data

    # Resample to weekly bars





    df['d'] = pd.to_datetime(df['d'])

    df.set_index('d', inplace=True)


    dfw = pd.DataFrame({
        'Open': df['Open'].resample('W').first(),
        'High': df['High'].resample('W').max(),
        'Low': df['Low'].resample('W').min(),
        'Close': df['Close'].resample('W').last(),
        'Volume': df['Volume'].resample('W').sum()
    })
    dfw

    dfw

    dfw['rolling_mean'] = dfw['Close'].rolling(window=rolling_n).mean()
    dfw['rolling_std'] = dfw['Close'].rolling(window=rolling_n).std()

    dfw['up'] = dfw['rolling_mean'] + z_score * dfw['rolling_std']
    dfw['down'] = dfw['rolling_mean'] - z_score * dfw['rolling_std']
    dfw

    dfw['down']=dfw['down'].shift(1)
    dfw['up']=dfw['up'].shift(1)
    dfw


    dfw=reset_index(dfw)
    dfw=dfw.loc[rolling_n+1:]
    dfw=reset_index(dfw)
    dfw

    dfw['mark']=''
    timestamps=[]
    for i in range(len(dfw)):
        down=dfw['down'][i]
        c=dfw['Close'][i]
        d=dfw['d'][i]
        timestamp1=int(d.timestamp())
        timestamps.append(timestamp1)
        if c<down:
            dfw.loc[i,'mark']='yes'
            # print('here',i)


    dfw['Timestamp']=timestamps



    stop_loss_price=dfw['down'][len(dfw)-1]

    return dfw,stop_loss_price
