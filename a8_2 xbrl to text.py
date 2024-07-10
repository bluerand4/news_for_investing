#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
from pathlib import Path

from sec_edgar_downloader import Downloader
import re
import openai,getpass,os
from openai import OpenAI

path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key
openai_client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=key,
)


from twilio.rest import Client
import yagmail
from datetime import datetime,timedelta
import pandas as pd
# Your Account SID from twilio.com/console
account_sid = "{account_sid_twilio}"
auth_token  = "{auth_token_twilio}"
client = Client(account_sid, auth_token)
sender='{id_yagmail}'
#receiver='bluerand3@gmail.com'
email1=sender
passw1='{password_yagmail}'
passw1='{password_yagmail}'
yag = yagmail.SMTP(user=sender,password=passw1)
content1='1'
subject1='1'
def send_email(to_email,title,content):
    yag.send(to=to_email,subject=title,contents=content)

def gpt_answer(define,content):
    response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": define},
        {"role": "user", "content": content}
    ]
    )
    
    return response.choices[0].message.content
# %%
# %%

#%% 
dl = Downloader("eontech", "bluerand3@gmail.com")
dl

tickers='CTAS,TT,RSG,CAH,FICO,TW,MANH,FCN,PSN,OBDC,CWCO'
ticker_list = [ticker.strip() for ticker in tickers.split(',')]

ticker='BRBR'
for ticker in ticker_list:
    print("ticker: ",ticker,'generate 10k...')
    dl.get("10-K", ticker, limit=1)
    time.sleep(1)
# dl.get("10-K", 'TW', limit=1)
#%%
path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/full-submission.txt'


with open(path1,'r') as file:
        data=file.read()

TARGET_NAME='ITEM 1'.lower()


#%%
cleaned_text = re.sub('<[^>]+>', '', data)
cleaned_text
# %%
len(cleaned_text)
# %%
with open("data/temp.txt",'a+') as file:
        file.write(cleaned_text)

# %%
path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/TW/10-K/0001758730-23-000047/full-submission.txt'
with open(path1,'r') as file:
    data=file.read()

TARGET_NAME='ITEM 1. business'.lower()


# TARGET_NAME='ITEM 7.'
split_list=data.lower().split(TARGET_NAME)
split_list
#%%
len(split_list)
#%%
if len(split_list)>3:
    splited_list=data.lower().split(TARGET_NAME)[1].split('\n')[:20]
else:
    splited_list=data.lower().split(TARGET_NAME)[-1].split('\n')[:20]
print("\n>> len(splited_list)= ", len(splited_list))

text1="".join(splited_list)



cleaned_text = re.sub('<[^>]+>', '', text1)[:4000]
cleaned_text
#%%
print("\n>> len(cleaned_text)= ", len(cleaned_text))



define="summarize based which products/services this company make. why is it better than competitors. what kind of customers will buy and why"
answer1=gpt_answer(define,cleaned_text)
answer1



TARGET_NAME='ITEM 7. mana'.lower()


split_list=data.lower().split(TARGET_NAME)
if len(split_list)>3:
    splited_list=data.lower().split(TARGET_NAME)[2].split('\n')[:20]
else:
    splited_list=data.lower().split(TARGET_NAME)[-1].split('\n')[:20]
text1="".join(splited_list)


cleaned_text = re.sub('<[^>]+>', '', text1)[:4000]
cleaned_text

define="summarize based on what are important events that happened for the company. If it has any financial numbers or other numbers, give me summary with the numbers."
answer2=gpt_answer(define,cleaned_text)
answer2


# %%
cleaned_text



#%%
path1=f'{path_to_openai_api}'
path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/data/temp.txt'
with open(path1,'r') as f:
    text1=f.read()

cleaned_text = re.sub('<[^>]+>', '', text1)[:4000]
cleaned_text

# %%
