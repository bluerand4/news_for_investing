#%%
from import_stocks2 import *
# %%
import pyperclip
tickers=pyperclip.paste()

# %%
tickers
# %%
unique_column_name='tickers'
database_name='news'
collection_name='additional_stocks'
# df=mongo_get_df(database_name,collection_name)
# df
#%%

dt=mongo_get_df(database_name,collection_name)
dt
#%%
if dt['status'][0]=='new':
    print('not made yet.. pass, come back tomorrow.')
else:

    df=pd.DataFrame([tickers,'new']).T
    df.columns=['tickers','status']
    df
    #%%

    # time.sleep(10)
    # %%

    if df['status'][0]=='new':
        print('start update')
        mongo_set_df(database_name,collection_name,unique_column_name,df)
        print('success - set here')
        
    # %%
print('done')
time.sleep(10)
for _ in range(3):
    a=1+2

# time.sleep(10)
#%%
