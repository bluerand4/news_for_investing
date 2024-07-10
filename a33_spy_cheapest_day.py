#%%
from import_all import *
fullname=generate_fullname_tradingview('SPY')
df=tradingview_simple(fullname,'1D')
df
# %%
df[['Date','Open']]
# %%
t1=df['Date'][0]
# %%
dt1=datetime.fromtimestamp(t1,tz=pytz.timezone("US/Eastern"))
dt1
#%%
string1=datetime.strftime(t1 ,"%A")
string1
#%%
df['Day']=''
df['week_of_year']=''
for i in range(len(df)):
    Date=df['Date'][i]
    # data=df['data'][i]
    # data=df['data'][i]
    string1=datetime.strftime(Date ,"%A")
    df.loc[i,'Day']=string1
    week_of_year = Date.isocalendar()[1]
    df.loc[i,'week_of_year']=week_of_year
    

#%%
df[['Date','Open','Day','week_of_year']]
#%%
new_week=0
dict1={}
min_day=[]
prev_week=888
list1=[]
for i in range(len(df)):
    
    week_of_year=df['week_of_year'][i]
    Date=df['Date'][i]
    Open=df['Open'][i]
    Day=df['Day'][i]
    if new_week ==0:
        new_week=week_of_year
        dict1[Day]=Open
    elif week_of_year!=prev_week:
        print('update needed',dict1)
        min_value = min(dict1.values())
        min_day = [day for day, price in dict1.items() if price == min_value]
        min_day
        list1.append(min_day[0])
        new_week=week_of_year
        
        dict1={}
        dict1[Day]=Open
    
    else:
        dict1[Day]=Open
    prev_week=new_week

#%%
print("\n>> len(list1)= ", len(list1))

# %%
print("\n>> len(df)= ", len(df))

# %%
most_common_string = Counter(list1).most_common()
most_common_string
# %%
Counter(list1)
# %%
list1
# %%
