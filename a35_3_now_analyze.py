#%%
from import_basics import *
from bs4 import BeautifulSoup
ticker='QCOM'
#%%
from import_mongo import *
# %%
df=mongo_get_df('stock','finviz_v1')
df
# %%
for item in df.columns:
    if 'price' in item.lower():
        print(item)
        data1=df[item][0]
        print("data1: ",data1)
# %%
# for item in 
df['div_ratio']=0
for i in range(len(df)):
    price_now=df['Price'][i]
    div=df['Dividend TTM'][i]
    try:
        div2=div.split(' ')[1].replace('(','').replace('%)','')
        div2=float(div2)
        price_now=float(price_now)
        # div_ratio=div2/price_now
        div_ratio=div2/100
        print(i,"dat1: ",div_ratio)
        df.loc[i,'div_ratio']=div_ratio
    except:
        pass
#%%
df[df['ticker']=='EC'][['ticker','Dividend TTM','Price']]
#%%
df['div_ratio']
#%%
df['repurchase_ratio']
#%%
df['sum_ratio']=df['div_ratio']+df['repurchase_ratio']
#%%
df['sum_ratio']
#%%
df1=df.sort_values(by='sum_ratio',ascending=False)
df1=reset_index(df1)
df2=df1[['ticker','sum_ratio','div_ratio','repurchase_ratio']]
#%%

'''
IBKR margin rate: 
6.83%

'''
margin_rate=0.0683
df3=df2[df2['sum_ratio']>margin_rate]
mongo_set_df('stock','finviz_v1_div_buyback','ticker',df3)

#%%
open_excel(df2)
#%%
# df1=df.sort_values(by='div_ratio',ascending=False)
# df1=reset_index(df1)
# df2=df1[['ticker','sum_ratio','div_ratio','repurchase_ratio']]


# # %%
# with open('test.txt','a+') as f:
#     f.write(str(df.columns))
# # %%
# df.columns.tolist()
# %%

#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%####################################################
#

ticker='EC'

url=f'https://finance.yahoo.com/quote/{ticker}/cash-flow'

# url = f'https://finance.yahoo.com/quote/{ticker}/profile/'
headers = {"User-Agent": "insomnia/8.4.2"}

# Make a request to the URL
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with class 'hello_there'
#//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
class1="D(tbr) fi-row Bgc($hoverBgColor):h"
div_content = soup.find_all('div', class_=class1)
div_content

div_content
for item in div_content:
    
    if 'repurchase' in item.text.lower():
        print("item.text.lower(): ",item.text.lower())
        print('here 1')
        break

    repurchase_total=float(item.find_all('span')[1].text.replace(',',''))
    repurchase_total=abs(repurchase_total)

    market_cap,industry, short_description,company_name,PE=get_stock_details(ticker)
    market_cap=market_cap*1000000
    market_cap
    repurchase_ratio=repurchase_total/market_cap
    print("market_cap: ",market_cap)

# %%
repurchase_total
#%%
4.8+2.85+2.62
# %%
