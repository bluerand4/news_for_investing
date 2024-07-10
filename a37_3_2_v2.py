#%%
from import_basics import *
import textwrap
from import_mongo import * 

import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

from openai import OpenAI
client = OpenAI()

# def youtube_seek_alpha_v1():
#%%

#%%
ticker_list=['CB']

# %%
mongo_set_df('seeking_alpha','analyst_report_v1','title',dn)
# %%
dn
# %%
dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
dn
# %%
mongo_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
# %%
for item in driver.find_elements(By.TAG_NAME,'div'):
    print(item.text)
# %%
driver.find_elements(By.XPATH,'//p[@id="tWHuOezkjAhuSrk"]')
# %%
driver.find_element(By.XPATH,'//p[@class="czsybYoLdoOQhfH"]')
# %%

for iii in range(len(df1)):
    if iii<3:
        continue
    # time.sleep(5)
    title=df1['title'][iii]
    if title in do_titles:
        print('duplicate!!',ticker,iii)
        continue
    driver.get(df1['link'][iii])

    time.sleep(10)
    sections = driver.find_elements(By.TAG_NAME, 'section')
    sections

    section=sections[0]
    text1=section.text

    text1=text1.split('This article was written by')[0]

    # print("\n>> len(text1)= ", len(text1))



    img_=[]
    for item in section.find_elements(By.TAG_NAME,'img'):
        img_.append(item.get_attribute('src'))

    img_=img_[1:-1]
    img_



    text1

    title=section.find_element(By.TAG_NAME,'h1').text
    title


    dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
    dn

    csv_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
    dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
    mongo_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
#%%
sections = driver.find_elements(By.TAG_NAME, 'section')
sections

section=sections[0]
text1=section.text

text1=text1.split('This article was written by')[0]

# print("\n>> len(text1)= ", len(text1))



img_=[]
for item in section.find_elements(By.TAG_NAME,'img'):
    img_.append(item.get_attribute('src'))

img_=img_[1:-1]
img_



text1

title=section.find_element(By.TAG_NAME,'h1').text
title


dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
dn

csv_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
mongo_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
# %%
#%%
driver.quit()
# %%
