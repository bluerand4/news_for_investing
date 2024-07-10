#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests
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


# %%
# dl.get("8-K", "GNE")
# dl.get("10-K", 'METC', limit=1)
# %%\
list1=[]

path = f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news"
os.chdir(path)
#%%

tickers=input('TSLA,AAPL,MSFT')
# tickers.split(',')
# tickers='CTAS,TT,RSG,CAH,FICO,TW,MANH,FCN,PSN,OBDC,CWCO'
ticker_list = [ticker.strip() for ticker in tickers.split(',')]

ticker='BRBR'
for ticker in ticker_list:
    print("ticker: ",ticker,'generate 10k...')
    dl.get("10-K", ticker, limit=1)
    time.sleep(1)
time.sleep(5)
#%%
def generate_10k_summary(ticker):
    print("ticker: ",ticker)

    folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/{ticker}'
    dl.get("10-K", ticker, limit=1)
    
    time.sleep(5)
    if os.path.isdir(folder):
        dl.get("10-K", ticker, limit=1)
    else:
        dl.get("10-K", ticker, limit=1)
        time.sleep(5)



    


    sub2=os.listdir(folder)[0]
    sub3=os.listdir(os.path.join(folder,sub2))[0]
    txt1=os.listdir(os.path.join(folder,sub2,sub3))[0]
    path1=os.path.join(folder,sub2,sub3,txt1)

    while not os.path.isfile(path1):
        print("Waiting for download to complete...",path1)
        time.sleep(1)  # Check every 5 seconds

    # path1='/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/TSLA/10-K/0000950170-23-001409/full-submission.txt'
    # path1="/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/MSFT/10-K/0000950170-23-035122/full-submission.txt"
    with open(path1,'r') as file:
        data=file.read()
    # data = re.sub('<[^>]+>', '', data)

    # TARGET_NAME='ITEM 1.'.lower()

    TARGET_NAME='>business<'.lower()

    # TARGET_NAME='ITEM 7.'
    split_list=data.lower().split(TARGET_NAME)
    if len(split_list)>3:
        splited_list=data.lower().split(TARGET_NAME)[1].split('\n')[:20]
    else:
        splited_list=data.lower().split(TARGET_NAME)[-1].split('\n')[:20]
    print("\n>> len(splited_list)= ", len(splited_list))

    text1="".join(splited_list)




    cleaned_text = re.sub('<[^>]+>', '', text1)[:4000]

    print("\n>> len(cleaned_text)= ", len(cleaned_text))


    url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
    response=requests.get(url)
    
    json1=response.json()
    stock_name=json1['results']['name']
    stock_name

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based which products/services this company make. why is it better than competitors. what kind of customers will buy and why"
    define='Does it include business description of the company, what products this company sells, and why customers buy from them?'
    answer1=gpt_answer(define,cleaned_text)
    answer1

    
    # TARGET_NAME='>risk factors<'
    TARGET_NAME='item 1a.'
    TARGET_NAME=TARGET_NAME.lower()
    split_list=data.lower().split(TARGET_NAME)
    cleaned_text=split_list[-1]
    cleaned_text = re.sub('<[^>]+>', '', cleaned_text)[:4000]

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based on what are important events that happened for the company. If it has any financial numbers or other numbers, give me summary with the numbers."
    define='Does it include risk factors for this company?'
    answer2=gpt_answer(define,cleaned_text)
    answer2



    TARGET_NAME='DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERA'
    TARGET_NAME=TARGET_NAME.lower()
    split_list=data.lower().split(TARGET_NAME)
    cleaned_text=split_list[-1].split('overview')[-1]
    cleaned_text = re.sub('<[^>]+>', '', cleaned_text)[:4000]

    cleaned_text="the company is "+stock_name+". "+cleaned_text

    # define="summarize based on what are important events that happened for the company. If it has any financial numbers or other numbers, give me summary with the numbers."
    define='Does it include good news or bad news for the company?'
    answer3=gpt_answer(define,cleaned_text)
    answer3


    list1.append(ticker)
    list1.append(f"#1 - description: {answer1}")
    list1.append('\n\n')
    list1.append(f"#2 - risk factors: {answer2}")
    list1.append('\n\n')
    list1.append(f"#3 - financial: {answer3}")
    list1.append('\n\n')
    list1.append('-----------------------------------')
    list1.append('\n\n')

    # os.remove(folder)
    folder_10k = Path(folder+"/10-K")
    if folder_10k.exists():
        # Recursively delete the folder and all its contents
        shutil.rmtree(folder_10k)
for ticker in ticker_list:
    try:
        generate_10k_summary(ticker)
    except Exception as e:
        print( 0 ,' = >>> some error = ',e)
    
list1.append('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

send_email('{id_yagmail}',"10k info: "+str(", ".join(ticker_list))," ".join([item for item in list1]))

# conda activate feature1
# cd "/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/"
# python3 "a8_sec gov api.py"
#%%
dl.get("10-K", "PSN", limit=1)
# %%
path3=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/data/full-submission.txt'
path3=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/CTAS/10-K/0000723254-23-000025/full-submission.txt'
with open(path3,'r') as file:
    data=file.read()

data = re.sub('<[^>]+>', '', data)

#%%
TARGET_NAME='DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERA'
TARGET_NAME=TARGET_NAME.lower()
split_list=data.lower().split(TARGET_NAME)
cleaned_text=split_list[-1].split('overview')[1][:4000]
# %%
path4=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t6_trading_news/sec-edgar-filings/CTAS/10-K/0000723254-23-000025/full-submission.txt'
with open(path4,'r') as file:
    data=file.read()
data = re.sub('<[^>]+>', '', data)


TARGET_NAME='DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERA'
TARGET_NAME=TARGET_NAME.lower()
split_list=data.lower().split(TARGET_NAME)
print("\n>> len(split_list)= ", len(split_list))
#%%
new1=split_list[-1].split('overview')
print("\n>> len(new1)= ", len(new1))
#%%
split_list[-1][:1000]
#%%
cleaned_text=split_list[-1].split('overview')[1][:4000]


cleaned_text="the company is "+'stock_name'+". "+cleaned_text

# %%
