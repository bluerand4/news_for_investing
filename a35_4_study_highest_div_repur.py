#%%
from import_basics import *
from bs4 import BeautifulSoup
from import_mongo import *

# %%
df=mongo_get_df('stock','finviz_v1_div_buyback')
#%%


tradingview_slope=mongo_get_df('stock','tradingview_slope')
tradingview_slope
#%%
dt_slope=copy.deepcopy(tradingview_slope)
    
for i_slope in range(len(dt_slope)):
    list4=dt_slope['fcf'][i_slope]
    list4=ast.literal_eval(list4)
    list4
    fcf1,intercept=regression_v2(list4,normalize=True)
    fcf2,intercept=regression_v2(list4[-8:],normalize=True)
    fcf2
    
    list4=dt_slope['revenue'][i_slope]
    list4=ast.literal_eval(list4)
    revenue1,intercept=regression_v2(list4,normalize=True)
    revenue2,intercept=regression_v2(list4[-8:],normalize=True)

    list4=dt_slope['net_income'][i_slope]
    list4=ast.literal_eval(list4)
    net_income1,intercept=regression_v2(list4,normalize=True)
    net_income2,intercept=regression_v2(list4[-8:],normalize=True)


    dt_slope.loc[i_slope,'fcf1']=fcf1
    dt_slope.loc[i_slope,'fcf2,']=fcf2
    dt_slope.loc[i_slope,'revenue1']=revenue1
    dt_slope.loc[i_slope,'revenue2']=revenue2
    dt_slope.loc[i_slope,'net_income1']=net_income1
    dt_slope.loc[i_slope,'net_income2']=net_income2

df2=dt_slope
df2 = df2[df2['revenue1'] >= 5]
df2 = df2[df2['revenue2'] >= 5]
# df2 = df2[df2['net_income1'] >= 5]
# df2 = df2[df2['net_income2'] >= 5]
df2 = df2[df2['fcf1'] >= 5]
df2 = df2[df2['fcf2,'] >= 5]
df2 = df2[df2['revenue1'] <= 499]
df2 = df2[df2['revenue2'] <= 499]
# df2 = df2[df2['net_income1'] <= 499]
# df2 = df2[df2['net_income2'] <= 499]
df2 = df2[df2['fcf1'] <= 499]
df2 = df2[df2['fcf2,'] <= 499]

# df2=df2.sort_values(by='fcf2,',ascending=False)
df2
#%%
df2=reset_index(df2)
df2_copy=copy.deepcopy(df2)

df2_copy['mc']=0
df2_copy['revenue']=0
df2_copy['rm_ratio']=0
df2_copy['free_cash']=0
df2_copy['fm_ratio']=0
for i in range(len(df2_copy)):
    ticker=df2_copy['ticker'][i]
    
    marc=df2[df2['ticker']==ticker]['Market capitalization'].values[0]
    rev1=df2[df2['ticker']==ticker]['revenue'].values[0]
    rev1=ast.literal_eval(rev1)
    rev1=rev1[-4:]
    rev1=sum(rev1)
    fcf1=df2[df2['ticker']==ticker]['fcf'].values[0]
    fcf1=ast.literal_eval(fcf1)
    fcf1=fcf1[-4:]
    fcf1=sum(fcf1)
    
    
    df2_copy.loc[i,'mc']=marc
    df2_copy.loc[i,'revenue']=rev1
    df2_copy.loc[i,'free_cash']=fcf1
    ratio=rev1/marc
    df2_copy.loc[i,'rm_ratio']=ratio
    ratio=fcf1/marc
    df2_copy.loc[i,'fm_ratio']=ratio



LAMBDA=0.5
df2_copy['rm_fm']=LAMBDA*df2_copy['rm_ratio']+(1-LAMBDA)*3*df2_copy['fm_ratio']
df2_copy=df2_copy.sort_values(by='rm_fm',ascending=False)
df2_copy
# %%
df3=df2_copy[['ticker','rm_fm','rm_ratio','fm_ratio']]
# %%
dt=df3.merge(df,how='outer',on='ticker')
dt
# %%
# Filter rows where 'RM' and 'dividend' are not null and 'MAN' is null
# filtered_df = df[(df['rm_fm'].notnull()) & (df['dividend'].notnull()) & (df['MAN'].isnull())]
# Filter rows where 'RM' and 'dividend' are not NaN
filtered_df = dt[dt['rm_fm'].notna() & dt['sum_ratio'].notna()]
filtered_df
filtered_df['rm_fm_div_repur']=filtered_df['rm_fm']+filtered_df['sum_ratio']
filtered_df=filtered_df.sort_values(by='rm_fm_div_repur',ascending=False)
filtered_df=reset_index(filtered_df)
filtered_df
#%%

mongo_set_df('stock','finviz_v1_div_buyback_rm_fm','ticker',filtered_df)
