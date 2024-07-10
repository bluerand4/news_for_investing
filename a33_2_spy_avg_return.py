#%%
from import_all import *
fullname=generate_fullname_tradingview('SPY')
df=tradingview_simple(fullname,'1D')
df
# %%
year=2004

dict1={}
Close0=df['Close'][0]
df['Day']=''
df['week_of_year']=''
for i in range(len(df)):
    Date=df['Date'][i]
    Close=df['Close'][i]
    # data=df['data'][i]
    string1=datetime.strftime(Date ,"%A")
    df.loc[i,'Day']=string1
    week_of_year = Date.isocalendar()[1]
    df.loc[i,'week_of_year']=week_of_year
    year1=Date.isocalendar()[0]
    Close
    if year!= year1:
        year=copy.deepcopy(year1)
        return1=Close/Close0
        value1=return1-1
        value1=round(value1,3)
        dict1[year]=value1
        Close0=copy.deepcopy(Close)
        
# %%
dict1
#%%
np.average(list(dict1.values())[:])

# %%
#%%
from import_all import *
fullname=generate_fullname_tradingview('XLK')
df=tradingview_simple(fullname,'1D')
df
# %%
year=2004

dict1={}
Close0=df['Close'][0]
df['Day']=''
df['week_of_year']=''
for i in range(len(df)):
    Date=df['Date'][i]
    Close=df['Close'][i]
    # data=df['data'][i]
    string1=datetime.strftime(Date ,"%A")
    df.loc[i,'Day']=string1
    week_of_year = Date.isocalendar()[1]
    df.loc[i,'week_of_year']=week_of_year
    year1=Date.isocalendar()[0]
    Close
    if year!= year1:
        year=copy.deepcopy(year1)
        return1=Close/Close0
        value1=return1-1
        value1=round(value1,3)
        dict1[year]=value1
        Close0=copy.deepcopy(Close)
        
# %%
dict1
#%%
back=3
print('last years',back)
np.average(list(dict1.values())[-back:])
#%%
back=5
print('last years',back)
np.average(list(dict1.values())[-back:])

# %%
back=10
print('last years',back)
np.average(list(dict1.values())[-back:])

# %%
back=20
print('last years',back)
np.average(list(dict1.values())[-back:])

# %%
