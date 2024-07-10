#%%
from import_all import *
#%%
tickers='ESEA,PSHG,TNK,GSL,TRMD,CVI,PETZ,DINO,GM,CEIX,SDRL,GECC,MHUA,FCAP,MVO,OI,BSVN,SLVM,WLFC,BOSC,HE,RWAY,BVFL'
tickers=tickers.split(',')
df=tradingview_simple('ESEA','1W')
df
#%%

def feature_engineering(df):
    df['Close1']=df["Close"].shift(periods=1)

    df['Close5'] = df["Close"].rolling(min_periods=1, window=5).mean()
    df['Close10'] = df["Close"].rolling(min_periods=1, window=10).mean()
    df['SMA50'] = df["Close"].rolling(min_periods=1, window=50).mean()
    df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
    df['SMA300'] = df["Close"].rolling(min_periods=1, window=300).mean()
    df['SMA500'] = df["Close"].rolling(min_periods=1, window=500).mean()
    df['SMA100'] = df["Close"].rolling(min_periods=1, window=100).mean()
    df['SMA1000'] = df["Close"].rolling(min_periods=1, window=1000).mean()
    df['SMA2000'] = df["Close"].rolling(min_periods=1, window=2000).mean()

    df["High5"] = df["High"].rolling(min_periods=1, window=5).max()
    df["High10"] = df["High"].rolling(min_periods=1, window=10).max()
    df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()

    df["Low5"] = df["Low"].rolling(min_periods=1, window=5).min()
    df["Low10"] = df["Low"].rolling(min_periods=1, window=10).min()
    df["MIN200"] = df["Low"].rolling(min_periods=1, window=200).min()
    

    df['Close2'] = df['Close'].pct_change()
    df['High2'] = df['High'].pct_change()
    df['Low2'] = df['Low'].pct_change()
    df['Open2'] = df['Open'].pct_change()
    df['Volume2'] = df['Volume'].pct_change()

    # p2 getting 'down2' value from 'low' and 2sd away from 'low'
    ROLLING_N=10
    df['Low5_mean'] = df['Low'].rolling(window=ROLLING_N).mean()
    df['Low5_sd'] = df['Low'].rolling(window=ROLLING_N).std()
    z_score=2
    df['up1'] = df['High'] + z_score * df['Low5_sd']
    df['down1'] = df['Low'] - z_score * df['Low5_sd']
    df
    df['down1']=df['down1'].shift(1)
    df['up1']=df['up1'].shift(1)
    
    return df
df=feature_engineering(df)
df1=df.dropna()
df1=reset_index(df1)

#%%
sum1=0
for i in range(len(df1)):
    
    down1=df1['down1'][i]
    Low=df1['Low'][i]
    Close=df1['Close'][i]
    if down1>Low:
        print('i',i,sum1)
        sum1+=1
#%%

# %%
df1[['Low','down1']]
# %%
# %%
# add path for the libraries.     from t3_temp import *
sys.path.pop(-1)

tradingview_complex(df1,blue_line='Close',red_line='Low',gray_line='down1')
# %%
