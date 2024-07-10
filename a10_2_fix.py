#%%

import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)

from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

from import_stocks import *
#%%
tickers=['ZS','NET','CRWD','NOW','NU','KTOS','DDOG','DCBO','CLS','QLYS','PCAR','MLM','GRMN','PTC','FDS','DKNG','AKAM','VRT','MANH','NTNX','GWRE','FIX','ENSG','OBDC','GPI']

ticker=tickers[2]
ticker='NOW'
list1=[]
# for ticker in tickers:
# try:
ticker='MS'
do=financials(ticker)
do#%%
#%%
do.columns
#%%


#%%

target_name='revenues'
column_list=do.columns
for name in column_list:
    if target_name in name:
        print(name)

for name in column_list:
    if target_name in name:
        print(name)
        break
#%%

#%%

#%%
df=do[name].reset_index()
import webbrowser

# HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Quarterly Values Plot</title>
<style>
    body {text-align: center;}
</style>
</head>
<body>
    <img src="quarterly_values_plot.png" alt="Quarterly Values Plot">
</body>
</html>
"""

# Saving the plot as an image
plt.figure(figsize=(30, 18))
plt.plot(df['index'], df[name], '-o')  # Line plot with dots at data points
for i, value in enumerate(df[name]):
    value_in_billions = value / 1e9  # Convert to billions
    plt.text(df['index'][i], value, f"{value_in_billions}B", va='bottom', ha='center')



# for i, value in enumerate(df[name]):
    # plt.text(df['index'][i], value, f"{value:.2e}", va='bottom', ha='center')
plt.xlabel(name)
plt.ylabel('Value')
plt.title(name)
plt.xticks(rotation=45)
plt.tight_layout()
plot_filename = "mydata/quarterly_values_plot.png"
plt.savefig(plot_filename)
plt.close()

# Saving the HTML content to a file
html_filename = "mydata/quarterly_values.html"
with open(html_filename, "w") as html_file:
    html_file.write(html_content)

# Open the HTML file in the default web browser
html_filename=os.path.join(os.getcwd(),html_filename)
webbrowser.open_new_tab(f"file://{html_filename}")

html_filename
#%%


#%%
#%%
#%%
numbers = remove_outliers(numbers)
min1=min(numbers)
max1=max(numbers)
numbers2=[(item -min1)/(max1-min1) for item in numbers]
numbers2

# for item in do.columns:
#     if 'gross' in item:
#         print("item: ",item)

slope1,intercept=regression(numbers)
slope1

slope2,intercept=regression(numbers2)
slope2








per,mc,div=get_pe_mc_div(ticker)
per
if per =='nan':
    score=slope2/1000*100000
else:
    score=slope2/per*100000

score
list1.append((ticker,score,slope2,per,mc,div))
    # except Exception as e:
        # print( 0 ,' = >>> some error = ',e)
    
# %%
dg=pd.DataFrame(list1)
dg
dg=dg.sort_values(by=2,ascending=False)
dg
# %%
per
# %%

for item in do.columns:
    if 'revenue' in item:
        print("item: ",item)
# %%
do.columns
# %%
per,mc,div=get_pe_mc_div('VRT')
per
# %%


ticker='DKNG'
#%%
revslope,inslope,do=draw_slope(ticker)
revslope=round(revslope*1000,1)
inslope=round(inslope*1000,1)
#%%
import requests
from bs4 import BeautifulSoup
import requests
ticker='WMT'




