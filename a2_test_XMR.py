#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
import getpass,sys,socket
# add path for the libraryfrom t10_stock import *
from t23_total import *
sys.path.pop(-1)
import pytz


#%%

model_name='win3_XMR_ATT_MU2_2023-05-27-1548_95-72-1768.pt'
model_name='linux1_IOST_CNN_v3_2023-06-01-1803_115-116-527.pt'
model_name='linux1_NEO_ATT_MU2_2023-06-01-2304_78-94-1875.pt'
model_name='linux1_LTC_CNN_v3_2023-06-04-1554_123-161-1976.pt'
# model_name='winp3_WAVES_CNN_v2_2023-05-23-1503_118-126-436.pt' #WAVES	1.0	winp3_WAVES_CNN_v2_2023-05-23-1503_118-126-436.pt	BUY	10.0	0.0	11.0	0.0
# model_name='winp3_WAVES_CNN_v2_2023-05-23-1503_118-126-436.pt' # 1.0	    winp3_WAVES_CNN_v2_2023-05-23-1503_118-126-436.pt	BUY	8.0	0.0	11.0	0.0	2023-05-24_0729
# model_name='winp3_WAVES_CNN_v2_2023-05-23-1532_180-143-2482.pt' # winp3_WAVES_CNN_v2_2023-05-23-1532_180-143-2482.pt	BUY	8.0	0.0	13.0	1.0	2023-05-24_2304
# volatility,SIGNAL,LENGTH,FEATURE_N,SIGNAL0,FEATURE_LIST=find_best_v3(model_name)
SIGNAL='OMEGA_1.0876__WINDOW1_1765__WINDOW2_714__RO_0.6358__THRESHOLD1_2.7584'
volatility=0.013664033
#%%
LENGTH=600
SIGNAL0='Close'
FEATURE_LIST=FEATURE_LIST=['Close2','Open2','High2','Low2',"Volume2",'Volume_minmax','close_SMA200','close_SMA50','close_SMA1000','close_SMA2000']
# print(volatility,SIGNAL,LENGTH,FEATURE_N,SIGNAL0,FEATURE_LIST)
#%%

# ticker1 = 'WAVES'
ticker1=model_name.split('_')[1]
side= 'SELL'
print("Ticker name:", ticker1)

ticker_ccxt=f'{ticker1}/USDT'
# df=generate_df_ccxt_v2(ticker1,'5',past_days=25)
minute1='5m'
df=generate_df_bi_v1(ticker1,minute1,past_days=10,DATE=True,delay=0)
# %%
# p1 bring parameters

# p2 make signal

# p3 make win loss

# ticker1 = 'WAVES'\


# p2 make your bol first and signal cross
SIGNAL_DICT={}
for item2 in SIGNAL.split('__'):
    key1=item2.split('_')[0]
    value1=float(item2.split('_')[1])
    SIGNAL_DICT[key1]=value1
    globals()[key1]=value1
# def bol_signal(df,target_column,BOLLINGER,num_std):

# p3 make signal
WINDOW1=int(WINDOW1)
WINDOW2=int(WINDOW2)
mean1=df['Volume'].mean()
df['Volume_plus_1']=df['Volume']+OMEGA*mean1
df['Volume2'] = df['Volume_plus_1'].pct_change()

df['Close2_SMA50'] = df["Close2"].rolling(min_periods=1, window=WINDOW1).mean()
df['Close2_SMA50_std'] = df["Close2"].rolling(min_periods=1, window=WINDOW1).std()

df['Volume2_SMA50'] = df["Volume2"].rolling(min_periods=1, window=WINDOW2).mean()
df['Volume2_SMA50_std'] = df["Volume2"].rolling(min_periods=1, window=WINDOW2).std()

# p3

df['cross1']=''
df['cross2']=''
quantity=1

# p3 signal cross

signal_list=[]
max_window=max(WINDOW1,WINDOW2)
for i in range(max_window,len(df)):
    Close2=df['Close2'][i]
    Close2_SMA50=df['Close2_SMA50'][i] 
    Close2_SMA50_std=df['Close2_SMA50_std'][i] 
    Volume2=df['Volume2'][i]
    Volume2_SMA50=df['Volume2_SMA50'][i] 
    Volume2_SMA50_std=df['Volume2_SMA50_std'][i] 
    TILDA=RO*abs((Close2-Close2_SMA50)/(Close2_SMA50_std))+ (1-RO)*abs((Volume2-Volume2_SMA50)/(Volume2_SMA50_std))
    if TILDA> THRESHOLD1:
        timestamp1=df['Timestamp'][i]
        dt2=datetime.fromtimestamp(timestamp1,tz=pytz.timezone("Asia/Seoul"))
        string1=datetime.strftime(dt2 ,"%Y-%m-%d %H:%M:%S")

        signal_list.append((0,LENGTH,i,timestamp1,df[SIGNAL0][i],df['Volume'][i],quantity,string1))
        df.loc[i,'cross2']='marked'

# %%
signal_list
# %%
# for i in range(len(df1)):
pnl_list,df=win_loss(signal_list,df,volatility,LENGTH,mode=SIGNAL0)
signal_list,pnl_list=clean_up_none(signal_list,pnl_list)
# outcome,length,buyindex,sellindex,buystamp,sellstamp,pnl
pnl_list2=np.array(pnl_list)
buyindex_list=pnl_list2[:,2].astype(int)
buyindex_list
print("volatility: ",volatility)
print("\n>> len(signal_list)= ", len(signal_list))
LENGTH=pnl_list[0][1]
LENGTH

#%%
pnl_list
#%%
list3=[df.iloc[i-LENGTH+1:i+1][FEATURE_LIST].values.tolist() for i in buyindex_list]
# list3
# print("\n>> len(list3)= ", len(list3))

x_array=torch.tensor(list3,dtype=torch.float)
y_true_list=[0 if item=='loss' else 1 for item in pnl_list2[:,0]]
y_true_array=torch.tensor(y_true_list,dtype=torch.long)
print('x array shape: ',x_array.shape)
print("\n>> y_true_array.shape= ", y_true_array.shape)
X_5000=x_array #.numpy()
Y_5000=y_true_array #.numpy()

#%%
X_5000=X_5000.to(DEVICE)
Y_5000=Y_5000.to(DEVICE)

#%%
model = torch.load(MODEL_FOLDER+model_name,map_location=DEVICE)
#%%
CHOSEN_EPOCH=0
TOTAL=0
# model,TOTAL,mcc,tp,fp,tn,fn=run_this_many_times(model,CHOSEN_EPOCH,TOTAL,X_5000,Y_5000)
# y_hat=model(X)
# model,acc,mcc,confusion=acc_test_v2(model,X,Y)
model.eval()
XXX=X_5000
YYY=Y_5000
y_hat=model(XXX) 
y_hat

y_hat=torch.argmax(y_hat,dim=1)
y_hat

acc=float(sum(YYY==y_hat))/len(YYY)
# mcc = matthews_corrcoef(YYY.cpu().numpy(), y_hat.cpu().numpy())
mcc=0
confusion =confusion_matrix(YYY.cpu().numpy(),y_hat.cpu().numpy()).ravel()

model.train()
# try:
tn, fp, fn, tp =confusion.ravel()
#%%
print(tp,fp,tn,fn)

#%%

# %%

df['buy_signal']=''
df['sell_signal']=''
df['sell_win']=''
df['sell_lose']=''
df['buy_win']=''
df['buy_lose']=''

for ii, (a,b,c,d,e,f,g) in enumerate(pnl_list):
    y_predicted=y_hat[ii].item()
    
    if a =='loss':

        df.loc[c,'sell_signal']='marked'
        if y_predicted==0:
            df.loc[d,'sell_win']='marked'
        else:
            df.loc[d,'sell_lose']='marked'
    elif a=='win':
        df.loc[c,'buy_signal']='marked'
        if y_predicted==1:
            df.loc[d,'buy_win']='marked'
        else:
            df.loc[d,'buy_lose']='marked'
# %%

KOREA1=True
INFO1=f'{ticker1} - {volatility} _ {SIGNAL}, {SIGNAL0} '

tradingview_complex_v3(df,ALPHA=9,INFO1=INFO1,blue_marker='buy_signal',greenup_marker='buy_win',redup_marker='buy_lose',red_line='SMA200')
#%%
tradingview_complex_v3(df,ALPHA=9,INFO1=INFO1,blue_marker='sell_signal',greendown_marker='sell_win',reddown_marker='sell_lose',red_line='SMA200')
# %%
y_hat
# %%
YYY
# %%
new_pnl_list=[]
for (win, length, i1,i2,time1,time2,pnl),predict,true1 in zip(pnl_list,y_hat,YYY):
    
    dt2=datetime.fromtimestamp(time1,tz=pytz.timezone("Asia/Seoul"))
    string1=datetime.strftime(dt2 ,"%Y-%m-%d %H:%M:%S")
    dt2=datetime.fromtimestamp(time2,tz=pytz.timezone("Asia/Seoul"))
    string2=datetime.strftime(dt2 ,"%Y-%m-%d %H:%M:%S")
    new_pnl_list.append((true1.item(),predict.item(),string1,string2,time1,time2))
# %%
new_pnl_list[-10:]
# %%
volatility
# %%
signal_list[-5:]
# %%
pnl_list[-10:]
# %%
"""
...
 (0, 600, 6998, 1685312100, 154.9, 470.921, 1, '2023-05-29 07:15:00'),
 (0, 600, 7010, 1685315700, 154.8, 755.664, 1, '2023-05-29 08:15:00'),
 (0, 600, 7073, 1685334600, 155.6, 707.452, 1, '2023-05-29 13:30:00'),
 (0, 600, 7096, 1685341500, 154.3, 1378.075, 1, '2023-05-29 15:25:00'),
 (0, 600, 7097, 1685341800, 153.7, 3562.732, 1, '2023-05-29 15:30:00')]
"""
#%%
close1=154.67
up1=close1*(1+volatility)
down1=close1*(1-volatility)
print(close1,up1,down1)
# %%

#%%
#%%
#%%
iii=3
paths=['/Users/macpro1/Documents/3_temp/1/v4_NEO_SELL_v2_20230615_111002.csv',
    '/Users/macpro1/Documents/3_temp/1/v4_NEO_SELL_v2_20230615_112503.csv',
    '/Users/macpro1/Documents/3_temp/1/v4_NEO_SELL_v2_20230615_124002.csv',
    '/Users/macpro1/Documents/3_temp/1/v4_NEO_SELL_v2_20230615_132502.csv'
       
       
       ]
df=read_excel(paths[iii])
df=df.dropna()
df=df.drop_duplicates(keep="last",subset='Date')
df=df.sort_values(by='Timestamp',ascending=True)
df=reset_index(df)
df=clean_negative_data(df)
df=feature_engineering_v1_essential(df)
df=feature_engineering_v2(df)
df=df.dropna()
df=reset_index(df)
df
# %%

# p3 make signal
WINDOW1=int(WINDOW1)
WINDOW2=int(WINDOW2)
mean1=df['Volume'].mean()
df['Volume_plus_1']=df['Volume']+OMEGA*mean1
df['Volume2'] = df['Volume_plus_1'].pct_change()

df['Close2_SMA50'] = df["Close2"].rolling(min_periods=1, window=WINDOW1).mean()
df['Close2_SMA50_std'] = df["Close2"].rolling(min_periods=1, window=WINDOW1).std()

df['Volume2_SMA50'] = df["Volume2"].rolling(min_periods=1, window=WINDOW2).mean()
df['Volume2_SMA50_std'] = df["Volume2"].rolling(min_periods=1, window=WINDOW2).std()

# p3

df['cross1']=''
df['cross2']=''
quantity=1

# p3 signal cross

signal_list=[]
max_window=max(WINDOW1,WINDOW2)
for i in range(max_window,len(df)):
    Close2=df['Close2'][i]
    Close2_SMA50=df['Close2_SMA50'][i] 
    Close2_SMA50_std=df['Close2_SMA50_std'][i] 
    Volume2=df['Volume2'][i]
    Volume2_SMA50=df['Volume2_SMA50'][i] 
    Volume2_SMA50_std=df['Volume2_SMA50_std'][i] 
    TILDA=RO*abs((Close2-Close2_SMA50)/(Close2_SMA50_std))+ (1-RO)*abs((Volume2-Volume2_SMA50)/(Volume2_SMA50_std))
    if TILDA> THRESHOLD1:
        timestamp1=df['Timestamp'][i]
        dt2=datetime.fromtimestamp(timestamp1,tz=pytz.timezone("Asia/Seoul"))
        string1=datetime.strftime(dt2 ,"%Y-%m-%d %H:%M:%S")

        signal_list.append((0,LENGTH,i,timestamp1,df[SIGNAL0][i],df['Volume'][i],quantity,string1))
        df.loc[i,'cross2']='marked'
#%%
df['buy_signal']=''
df['sell_signal']=''
df['sell_win']=''
df['sell_lose']=''
df['buy_win']=''
df['buy_lose']=''

for ii, (a,b,c,d,e,f,g,h) in enumerate(signal_list):
    # y_predicted=y_hat[ii].item()
    # if a =='loss':

    df.loc[c,'sell_signal']='marked'
        # if y_predicted==0:
        #     df.loc[d,'sell_win']='marked'
        # else:
        # df.loc[d,'sell_lose']='marked'
    # elif a=='win':
        # df.loc[c,'buy_signal']='marked'
        # if y_predicted==1:
        #     df.loc[d,'buy_win']='marked'
        # else:
        # df.loc[d,'buy_lose']='marked'

tradingview_complex_v3(df,ALPHA=9,INFO1=INFO1,blue_marker='sell_signal',greendown_marker='sell_win',reddown_marker='sell_lose',red_line='SMA200')

# %%



model_name='linux1_LTC_CNN_v3_2023-06-04-1554_123-161-1976.pt'