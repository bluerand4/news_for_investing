#%%
# add path for the libraries.     from t_mini import * 
import t_mini_basics as basics
import t_mini_examine as examine
import t_mini_pnl as pnl
import t_mini_model as model
from t_mini_tradingview import *
sys.path.pop(-1)
import json
import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)

#%%

from moviepy.editor import VideoFileClip

def get_video_length(filename):
    with VideoFileClip(filename) as video:
        return video.duration

from twilio.rest import Client
import yagmail
from datetime import datetime,timedelta
import pandas as pd
# Your Account SID from twilio.com/console

newsapi_org='{newsapi_org}'

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



import yfinance as yf

import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

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

def save_images(search_list,audio_folder='data/news_audios/',random_voices=False):
    search_list=[item.replace('-','').replace('\n','') for item in search_list]
    search_list=[item for item in search_list if len(item)>2]

    for ii in range(len(search_list)):
        try:
            search=search_list[ii]
            url = "https://www.bing.com/images/search"

            querystring = {"q":search,"qs":"n","form":"QBIR","sp":"-1","lq":"0","pq":search,"sc":"0-385","cvid":"8315BDF4778F4D79B9BEE404E2235FCD","ghsh":"0","ghacc":"0","first":"1"}

            payload = ""
            headers = {
                "cookie": "MUID=187D6415C7756594386277C8C6556400; MUIDB=187D6415C7756594386277C8C6556400; _EDGE_S=F%3D1%26SID%3D0217789F30A1631932186B42318162D7; _EDGE_V=1; MMCASM=ID%3D4B7BB4EC8C0242ADA2B01CE7EAD8A518; SRCHD=AF%3DQBIR; SRCHUID=V%3D2%26GUID%3DCC81D6DC8DF1492892505589E1146896%26dmnchg%3D1; SRCHUSR=DOB%3D20231204; SRCHHPGUSR=SRCHLANG%3Dko%26IG%3DE6A3BF77318E480DB48AB9506B0C4CB5; _SS=SID%3D0217789F30A1631932186B42318162D7",
                "User-Agent": "insomnia/8.4.2"
            }

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

            # print(response.text)
            
            soup = BeautifulSoup(str(response.text), 'html.parser')
            text = soup.text
            text
            div_content = soup.find_all('img', class_="mimg")
            
            for iii,item in enumerate(div_content[:5]):

                img_link=div_content[iii]['src']

                response = requests.get(img_link)
                response

                folder_name='data/news_images'
                name=search[:20]+f" {iii}"
                local_file_path = f'{folder_name}/{name}.png'

                # Check if the request was successful (HTTP status code 200)
                if response.status_code == 200:
                    # Get the content of the response (the image data)
                    image_data = response.content
                    
                    # Specify the local file path where you want to save the image
                    # local_file_path = 'data/temp.jpg'
                    
                    # Open a local file in binary write mode and write the image data to it
                    with open(local_file_path, 'wb') as file:
                        file.write(image_data)
                time.sleep(1)
            print('done ',item)
            time.sleep(3)
        except Exception as e:
            print( 0 ,' = >>> some error = ',e)
    
    

    for ii in range(len(search_list)):
        # time.sleep(1)
        search=search_list[ii]
        name_prefix=search[:20]
        audio_download_v3(name_prefix,search,audio_folder,random_voices)
        print(ii)
    return search_list

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
def functional_enum2():

    messages = [{"role": "user", "content": productname_element}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "yes_or_no",
                "description": "do you think this name is name of a product?",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "return yes or no",
                        },
                        # "unit": {"type": "string", "enum": ["yes", "no"]},
                        "unit": {"type": "string"},
                    },
                    "required": ["search_term"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response

    response.choices[0].message

def functional_enum(content,main_description,description,enums,model_name='gpt-3.5-turbo-1106'):

    response = openai_client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": content}],
    functions=[
        {
            "name": "functional_enum",
            "description": main_description,
            "parameters": {
                "type": "object",
                "properties": {
                    "search_term": {
                        "type": "string",
                        "description": description 
                        

                    }
                    
                },
                "required": ["search_term"],
            },
        }
    ],
    # function_call="auto",
    function_call={'name':'functional_enum'}
    )

    print("response: ",response)

    return response
#%%
dl = Downloader("eontech", "bluerand3@gmail.com")
dl

def get_nasdaq_insider(ticker):

    for _ in range(3):
        try:
            driver=open_driver()
            break
        except Exception as e:
            driver.quit()
            print( 0 ,' = >>> some error = ',e)
    

    
    url = f"https://www.nasdaq.com/market-activity/stocks/{ticker}/insider-activity"




    driver.get(url)

    short_interest_nasdaq=driver.find_elements(By.XPATH,'//div[@class="insider-activity__table-container"]')[1].find_elements(By.TAG_NAME,'td')
    month12=short_interest_nasdaq[-1].text
    month3=short_interest_nasdaq[-2].text

    month3=convert_to_integer(month3)
    month12=convert_to_integer(month12)
    month12

    print("month12: ",month12)

    driver.quit()
    time.sleep(3)
    try:
        driver.quit()
    except Exception as e:
        print( 0 ,' = >>> some error = ',e)
    
def get_insider_short_interest(ticker):
    
    month3,month12=insider_barchart(ticker)


    #https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
    import requests,json
    url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'

    response=requests.get(url)

    json1=response.json()
    total_outstanding_shares=json1['results']['share_class_shares_outstanding']
    total_outstanding_shares


    month3_1=str(round(month3/total_outstanding_shares*100,2))+"%"
    month12_1=str(round(month12/total_outstanding_shares*100,2))+"%"
    print("month3_1: ",month3_1)
    recent_price=get_recent_price(ticker)
    recent_price

    d1,mc,d3=get_pe_mc_div(ticker)




    month3_2=str(round((recent_price*month3)/(mc*1000000000)*100,2))+"%"
    month12_2=str(round((recent_price*month12)/(mc*1000000000)*100,2))+"%"
    print("month12_2: ",month12_2)


    
    dict1=get_short_interests(ticker)
    string1=''
    for key,value in dict1.items():
        string1=string1+key
        string1=string1+'\n'
        string1=string1+value
        string1=string1+'\n'
    
    
    dict2=dict(
        month3_1=month3_1 + "vs"+month3_2,
        
        month12_1=month12_1+"vs"+month12_2
    )
    for key,value in dict2.items():
        string1=string1+key
        string1=string1+'\n'
        string1=string1+value
        string1=string1+'\n'
    

    return string1
def convert_to_integer(s):
    # Check for negative numbers represented by parentheses
    is_negative = '(' in s and ')' in s

    # Remove commas and parentheses
    s = s.replace(',', '').replace('(', '').replace(')', '')

    # Convert to integer
    num = int(s)

    # Apply negative sign if needed
    if is_negative:
        num = -num

    return num
def get_recent_price(ticker):
    import requests,json

    url=f'https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}?apiKey={polygon_api_key}'


    # url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
    response=requests.get(url)

    json1=response.json()
    # print(json1)
    # stock_name=json1['results']['name']
    recent_price=json1['ticker']['min']['c']
    return recent_price

import requests
from bs4 import BeautifulSoup


def insider_barchart(ticker):
    url = f"https://www.barchart.com/stocks/quotes/{ticker}/insider-trades"

    payload = ""
    headers = {
        "cookie": "laravel_token=eyJpdiI6InI4TVBINVl1Z295bTJrY3hwNk1STHc9PSIsInZhbHVlIjoiN2JpbGNraFV5OEJKUFVDY1VNdThTRVh2aVBSRVlBT2pQNnJ3bXZ3bWxsSjczdHpvWWtNT28zODl4SnRoVzdhRWZ0ZDRNczV2TWxYT1V3dG1hdDdjeUhZOHJFK3BTZ2tYa0tDV2RGNDE1bGxGYkdDSUlJVWF5TkM3dmZJVDFpcXVNbys0OG44OXYwczN1SkFEVTYwWTdiS3BYUHBkZVgvUEJPNUtUYmNqc2FRL2E0Q0dKNGVZdjAwV21sZXdUOXNaK3R5aWNrQ2tsSjhHcHdPQUtia0UxSnhwQnR4T2ZzTVk4TG81cXdmaDYrVXlCaC9LM1AxL3ViUEFQNEVDUFBPdkM4YXRSYldzTGFWNmV1bWpEZlBSUHZNeUp3Y0xLNWFaeDVjNlhUdjU2VnJzbFNobWNBa1ZGLzhxSEJVUDRKSnEiLCJtYWMiOiIwMGJlMmRjMzU2NmJiNjI4ZDE4MWE5MDMxZjRhMWQ5YTlkZmNhYzJhOWRjZmEyNWExOWEwM2QwMWFhMWE2NDUxIn0%253D; XSRF-TOKEN=eyJpdiI6Ino5OTAyWEs0TTZYSXdiTVZjZTRiT1E9PSIsInZhbHVlIjoiMU8zZ0IwbW43QzMwTldES3NSU2pEVUh0T3lFZTFodmEybm9xS01WaERla0Zaam5WOXFTS2J2MDkyUFU1aUkrdFlvNUJxRVQ2YjJCR3dHcWlrSlE4RDBLNytXdXBrOFY5Nzh0bWF2Y2tMTmtXbHFlVmNESkptL3FyZDAwWUcyRmkiLCJtYWMiOiJlODVhMWU2ZmE1ZTJiMDUwNzcwM2MxZTAxYTdjMzY0OGQ0NTU3M2U0MzkwNjQzY2U0YzI4YWQwZDJlNmJkZTllIn0%253D; laravel_session=eyJpdiI6ImV3ZEpZRU9mRlBKak93VkpSV2NyOGc9PSIsInZhbHVlIjoiYnNrUmVzMDdsMG0yL0RsNGlNTFQxVDZPbGlYNGtrVGFyN3FOaUxEU3hRSEN1cy81Nk53L2hjb0lMNmVKMjFOTXFFOVc5UnN2bWpkelBTTnRId0hXOWxHSGY2SjJldkNGNTc2YUpiblJYWnoxNHdxOENlMUxCMWYrM0hjbUhUSG8iLCJtYWMiOiJlZDhjNzkzMTc2MTg4MWNiOWFmOGE0YmRhZDdiYjI5MDdhYWY4YWJlOGFhNGYxMGY4YzQyM2U1M2IxNWFkOTA2In0%253D; market=eyJpdiI6InpubVVJZ0h3NWxnV1JxSFRrTFllK2c9PSIsInZhbHVlIjoiekdJZ0g4bkpielF3cWliMHA5cGJnL05pRkJCa0txSUhHOXFyRzRSSmtMWW1saFlNMGhlM1NIcHdVWldJZXN6aiIsIm1hYyI6IjFkMWI0OTVlODYxYWI2Y2MzNWY1YzdkNjk3NzBjNWUzNDZkMTY5ODYwNDM3ZTJhYzI2YjEwZGYwNWVkYmYyMjQifQ%253D%253D",
        "User-Agent": "insomnia/8.4.2"
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.text
    # //div[@class="trades-shares"]
    div_content = soup.find_all('div', class_="trades-shares")


    bought3=int(div_content[0].text.replace(' Shares','').replace(',',''))
    sold3=int(div_content[1].text.replace(' Shares','').replace(',',''))
    net3=bought3-sold3
    print("net3: ",net3)

    bought12=int(div_content[4].text.replace(' Shares','').replace(',',''))
    sold12=int(div_content[5].text.replace(' Shares','').replace(',',''))
    net12=bought12-sold12
    print("net12: ",net12)
    return net3,net12
def get_short_interests(ticker):
    url = "https://finviz.com/quote.ashx"

    querystring = {"t":ticker,"p":"d"}

    payload = ""
    headers = {
        "cookie": "chartsTheme=dark; notice-newsletter=show",
        "User-Agent": "insomnia/8.4.2"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # print(response.text)


    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.text

    div_content = soup.find_all('tr', class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
    div_content

    class_name = "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)".replace(" ", ".").replace("(", "\(").replace(")", "\)")

    # Find all tr elements with the specified class
    #//td[@data-test="PE_RATIO-value"]
    elements = soup.find_all('tr', class_=class_name)
    elements


    #//table[@class="snapshot-table2 screener_snapshot-table-body"]
    # table = soup.find_all('table')
    table=soup.find_all('table', class_="snapshot-table2 screener_snapshot-table-body")
    # print("\n>> len(table)= ", len(table))




    soup2 = BeautifulSoup(str(table[0]), 'html.parser').find_all('tr')
    # print("\n>> len(soup2)= ", len(soup2))

    soup2


    list1=[]
    list2=[]
    sum1=0
    for i in range(len(soup2)):
        cells=soup2[i].find_all('td')
        cells
        for ii,cell in enumerate(cells):
            print("cell.text: ",cell.text)
            if ii%2==0:
                list1.append(cell.text)
            else:
                list2.append(cell.text)

        sum1+=1

    list2

    de=pd.DataFrame(list2).T
    de

    de.columns=list1
    de

    short_interest=de['Short Float / Ratio'][0]
    Beta=de['Beta'][0]
    insider_owned=de['Insider Own'][0]
    insider_trade=de['Insider Trans'][0]
    institut_owned=de['Inst Own'][0]
    institut_trade=de['Inst Trans'][0]
    quick_ratio=de['Quick Ratio'][0]
    Beta
    dict1=dict(short_interest=short_interest,
               Beta=Beta,
               insider_owned=insider_owned,
               insider_trade=insider_trade,
               institut_owned=institut_owned,
               institut_trade=institut_trade,
               quick_ratio=quick_ratio,
               )
    return dict1
import requests
from bs4 import BeautifulSoup
import re

def yahoo_company(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('tr', class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
    div_content

    class_name = "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)".replace(" ", ".").replace("(", "\(").replace(")", "\)")

    # Find all tr elements with the specified class
    #//td[@data-test="PE_RATIO-value"]
    elements = soup.find_all('tr', class_=class_name)
    elements

    def find_value(datatest):
        pe_ratio_element = soup.find('td', {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-test': datatest})
        text1=pe_ratio_element.text
        print("text1: ",text1)
        if "B" in text1:
            text1=text1.replace('B','')
            text1=float(text1)
        elif "T" in text1:
            text1=text1.replace('T','')
            text1=float(text1)*1000
        
        elif "M" in text1:
            text1=text1.replace('M','')
            text1=float(text1)/1000
        elif "N/A" in text1:
            return 'nan'
        elif "%" in text1:

            # Regular expression pattern to find text inside parentheses
            pattern = r"\((.*?)\)"

            # Use re.findall to find all matches
            matches = re.findall(pattern, text1)
            return matches
        
        else:
            text1=float(text1)

        return    text1

    per=find_value('PE_RATIO-value')
    per

    mc=find_value("MARKET_CAP-value")
    mc
    div=find_value("DIVIDEND_AND_YIELD-value")
    div



    url = f'https://finance.yahoo.com/quote/{ticker}/profile/'
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('p', class_="Mt(15px) Lh(1.6)")
    div_content

    soup = BeautifulSoup(str(div_content[0]), 'html.parser')
    company_description = soup.text
    company_description

    return per,mc,div,company_description

def yahoo_company_v2(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('tr', class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
    div_content

    class_name = "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)".replace(" ", ".").replace("(", "\(").replace(")", "\)")

    # Find all tr elements with the specified class
    #//td[@data-test="PE_RATIO-value"]
    elements = soup.find_all('tr', class_=class_name)
    elements

    def find_value(datatest):
        pe_ratio_element = soup.find('td', {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-test': datatest})
        text1=pe_ratio_element.text
        print("text1: ",text1)
        if "B" in text1:
            text1=text1.replace('B','')
            text1=float(text1)
        elif "T" in text1:
            text1=text1.replace('T','')
            text1=float(text1)*1000
        
        elif "M" in text1:
            text1=text1.replace('M','')
            text1=float(text1)/1000
        elif "N/A" in text1:
            return 'nan'
        elif "%" in text1:

            # Regular expression pattern to find text inside parentheses
            pattern = r"\((.*?)\)"

            # Use re.findall to find all matches
            matches = re.findall(pattern, text1)
            return matches
        
        else:
            text1=float(text1)

        return    text1

    per=find_value('PE_RATIO-value')
    per

    mc=find_value("MARKET_CAP-value")
    mc
    div=find_value("DIVIDEND_AND_YIELD-value")
    div


    company_description,sector,industry=yahoo_profile(ticker)
    revenue1,insider=yahoo_statistics(ticker)
    mc_rev=mc/revenue1
    return per,mc,div,company_description,revenue1,insider,mc_rev,sector,industry

def yahoo_statistics(ticker):

    url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('tr', class_="Bxz(bb) H(36px) BdY Bdc($seperatorColor)")
    div_content
    for item in div_content:
        if 'revenue' in item.text.lower():
            print('here 1')
            break

    item.text

    item


    soup1 = BeautifulSoup(str(item), 'html.parser')
    soup1

    text1 = soup1.find_all('td')[-1].text
    text1
    if "B" in text1:
        text1=text1.replace('B','')
        text1=float(text1)
    elif "T" in text1:
        text1=text1.replace('T','')
        text1=float(text1)*1000

    elif "M" in text1:
        text1=text1.replace('M','')
        text1=float(text1)/1000
    elif "N/A" in text1:
        text1= 'nan'
    text1
    revenue1=text1

    #//tr[@class="Bxz(bb) H(36px) BdB Bdbc($seperatorColor) "]
    div_content = soup.find_all('tr', class_="Bxz(bb) H(36px) BdB Bdbc($seperatorColor)")
    div_content
    for item in div_content:
        if 'insider' in item.text.lower():
            print('here 1')
            break

    item.text

    item


    soup2 = BeautifulSoup(str(item), 'html.parser')
    soup2

    insider_percentage = soup2.find_all('td')[-1].text
    return revenue1,insider_percentage

def yahoo_profile(ticker):

    url = f'https://finance.yahoo.com/quote/{ticker}/profile/'
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('p', class_="Mt(15px) Lh(1.6)")
    div_content

    soup2 = BeautifulSoup(str(div_content[0]), 'html.parser')
    company_description = soup2.text
    company_description

    profiles = soup.find_all('span', class_="Fw(600)")
    # profiles_=[]
    # sector=''
    # industry=''
    # for item in profiles:
    #     word=item.text.lower()
    #     if 'sector' in word:
    #         sector=word
    #     elif 'industry' in word:
    #         industry=word
    sector=profiles[1].text
    sector
    industry=profiles[2].text
    industry

    return company_description,sector,industry
# def gpt_answer(define,question):
#     try:
        

#         content=question
#         message_list3=[{"role": "system", "content" : define},
#                     {"role": "user", "content" : str(content)},    
#                     ]
#         completion = openai.ChatCompletion.create(model="gpt-3.5-turbo" , #"gpt-3.5-turbo", 
#                     messages = message_list3)['choices'][0]['message']['content']
#     except Exception as e:
#         completion='>> error = time out for gpt...'+str(e)
#     return completion

def get_stock_details(ticker):
    market_cap,industry, short_description,company_name,PE=0,0,0,0,0
    try:
        stock = yf.Ticker(ticker)
        
        # Info is a dictionary containing various details about the stock
        info = stock.info
        
        market_cap = stock.info.get('marketCap')
        market_cap=round(market_cap/1000000000,2)
        industry = info.get('industry', 'N/A')
        short_description = info.get('longBusinessSummary', 'N/A')
        company_name = short_description.split('.')[0]
        company_name
        PE = info.get('trailingPE')
    except Exception as e:
        print('error here 13: ',ticker,e)
        try:

            endpoint=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
            response = requests.get(endpoint)
            # Raise an error if the request failed
            response.raise_for_status()
            # Parse the JSON result
            data = response.json()

            json_data=data['results']

            new_row = pd.DataFrame(json_data, index=[0])
            short_description=new_row['description'][0]
            market_cap=new_row['market_cap'][0]
            market_cap=round(market_cap/1000000000,2)
            company_name=new_row['name'][0]
        except Exception as e:
            print('double error ',ticker,e)
            
    return market_cap,industry, short_description,company_name,PE

from newsapi import NewsApiClient

def fetch_news_for_query(api_key, query, language='en', page_size=5):
    newsapi = NewsApiClient(api_key=api_key)

    # Search for articles with the given query
    articles = newsapi.get_everything(q=query,
                                      language=language,
                                      sort_by="relevancy",  # Sort by relevancy to the query
                                      page_size=page_size)

    articles_list = articles.get('articles')
    if not articles_list:
        print("No news found!")
        return
    list1=[]
    for article in articles_list:
        title = article.get('title')
        description = article.get('description')
        print(f"Title: {title}")
        # print(f"Description: {description}\n")
        list1.append((title,description))
    return list1

def check_20_assets_sma200_above():

    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    dw

    de=total.read_excel(f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/list_of_assets.xlsx')
    de=total.reset_index(de)
    de


    fullname_list=[]
    webname_list=[]
    for i in range(len(de)):
        webname=str(de['web_name'][i])
        if 'symbol' in webname:
            webname=webname.split('=')[1]
            ticker2=webname.split("%")
            part2=ticker2[1].replace("3A","")
            if len(ticker2)>2:
                
                fullname=ticker2[0]+":"+part2+"!"
            else:
                fullname=ticker2[0]+":"+part2
            fullname
            webname_list.append(webname)
            fullname_list.append(fullname)
            print(fullname)
            print(' ')


    list5=[]
    minute1='1D'
    for fullname in fullname_list:
        try:
            df=tradingview1(fullname,minute1)
            df
            while True:

                tot=len(df)-1
                print(fullname,'  ',df['Date'][tot])

                date2=df['Date'][tot]
                date2

                if 'nan' in str(date2).lower() or 'nat' in str(date2).lower():
                    print('drop last row')
                    df = df.iloc[:-1 , :]
                else:
                    break


        
            link_symbol=fullname.replace(":","%3A").replace("!","%21")
            link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
            link_symbol
        
            
            tot=len(df)-1
            print(fullname,'  ',df['Date'][tot])
            print(' ')
            for i in range(10):
                close1=df['Close'][tot-i]
                sma200=df['SMA200'][tot-i]
                close1_2=df['Close'][tot-i-1]
                sma200_2=df['SMA200'][tot-i-1]
                date1=df['Date'][tot-i]
                if close1>sma200:
                    if close1_2<sma200_2:
                        print(i)
                        print(date1)
                        print('close > sma200')
                        list5.append((fullname,date1,close1,sma200,'above',f'{fullname}_{date1}'))
                if close1<sma200:
                    if close1_2>sma200_2:
                        print(' ============')
                        print(i)
                        print(df['Date'][tot-i])
                        print('close < sma200')
                        list5.append((fullname,date1,close1,sma200,'below',f'{fullname}_{date1}'))
                        print(' ----')  
        except Exception as e:
            print(e)
            send_email(sender,f'error - {fullname}',f'{fullname},{e}')



    if len(list5)>0:
    
        dw2=pd.DataFrame(list5)
        dw2.columns=['fullname','date','close','sma200','direction','fullname_date']
        dw2

        dw3=dw2[~dw2['fullname_date'].isin(dw['fullname_date'])]
        dw3=total.reset_index(dw3)
        dw3
        if len(dw3)>0:
        
            for i in range(len(dw3)):
                above1=str(dw3['direction'][i])
                
                fullname=str(dw3['fullname'][i])
                date1=str(dw3['date'][i])
                close1=str(dw3['close'][i])
                sma200=str(dw3['sma200'][i])
                fullname_date=str(dw3['fullname_date'][i])
                ticker=fullname.split(':')[1].replace("1!","")
                link_symbol=fullname.replace(":","%3A").replace("!","%21")
                link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
                
                if 'above' in above1:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
                else:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
    
        print('start = saving dw to csv')
        dw=pd.concat((dw,dw2),axis=0)
        dw=dw.drop_duplicates(keep="last",subset='fullname_date')
        dw=total.reset_index(dw)
        
        dw.to_csv(alarm1)
        dw
        print('success = saving dw to csv')
def seven_days_alarm():
    print('seven days - alarm check')
    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    
    for item in list(set(dw['fullname'].values)):


        string1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['date'][-1:].values[0]
        above1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['direction'][-1:].values[0]
        fullname=item
        datetime1=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=7)
        link_symbol=fullname.replace(":","%3A").replace("!","%21")
        link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'

        days_7=datetime.strftime(datetime1 ,"%Y-%m-%d")
        

        today1=(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d"))
        if today1==days_7:
            send_email(email1,title=f't2: {item} has been 7 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 7 days passed..')

        datetime2=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=14)
        days_14=datetime.strftime(datetime2 ,"%Y-%m-%d")
        if today1==days_14:
            send_email(email1,title=f't3: {item} has been 14 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 14 days passed..')



def futures_expiration_email():
    day1=3
    path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/2 futures expiration definition/win2_IBKR_Futures2.csv'
    da=total.read_csv(path1)
    da=total.reset_index(da)
    da
    for i in range(len(da)):
        expiry1=str(da['expiry'][i])
        symbol=da['symbol'][i]
        sectype=da['sectype'][i]
        exch=da['exch'][i]
        local=da['local'][i]
        all1=str(da.iloc[i])
        date1=datetime.strptime(expiry1, "%Y%m%d")
        date2=date1-timedelta(days=day1)

        date2=datetime.strftime(date2 ,"%Y-%m-%d")
        date2
        timedelta1=0
        timedelta2=100
        today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
        today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
        past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
        past2=datetime.strptime('20210218', "%Y%m%d").timestamp()

        if today1==date2:
            print(i,symbol,sectype,expiry1,exch,local)
            send_email(email1,title=f'futures expiration: {symbol} will be expired in {day1} days.',content=f'{symbol}_{sectype}_{expiry1}_{exch}_{local}')




def find_exchange(ticker):


    df1=pd.read_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx",index_col=0)
    exchange1=0
    for i in range(len(df1)):
        if ticker == df1['ticker'][i]:
            exchange1=df1['Exchange'][i]
            #print("existing ticker exchange",ticker)
    if exchange1==0:
        print("not existing exchange info : ", ticker)
        
        url = "https://ycharts.com/companies/{}".format(ticker)
        payload = ""
        headers = {
            "cookie": "ycsessionid=2qz3d4y9pia7lsirwduwfoqsy68lxo0u; _ga=GA1.2.635129160.1644138754; _gid=GA1.2.916019816.1644138754; __gads=ID=93bc25b5583902a4-22af5cc377d00013:T=1644138753:S=ALNI_MZo9l0xXkE31mqmewQtnKQnTUUD5Q; __hstc=69688216.203ddbd23f614854901d1b6290dd0cc4.1644138757373.1644138757373.1644138757373.1; hubspotutk=203ddbd23f614854901d1b6290dd0cc4; __hssrc=1; _fbp=fb.1.1644138757715.487408360; _gcl_au=1.1.38652961.1644138758; quickflowsSingleSecurityCookieName=%7B%22displaySecurityId%22%3A%22AAPL%22%2C%22securityId%22%3A%22AAPL%22%7D; messagesUtk=a7090410a7a24598b5f7b00924eb45a1; page_view_ctr=3; __hssc=69688216.3.1644138757373",
            "authority": "ycharts.com",
            "cache-control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "macOS",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://www.google.com/",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        data=response.text
        exchange1=data.split("&nbsp;|&nbsp;")[1].split("\n")[1].replace(" ","")

        print("scrape ychart", ticker, exchange1)
        dictionary={"ticker":[ticker],"Exchange":[exchange1]}

        df=pd.DataFrame.from_dict(dictionary)
        df1=df1.append(df)
        df=df1.append(df)
        df=df.drop_duplicates(keep="last",subset="ticker")
        df=df.reset_index()
        df=df.drop(columns=["index"])
        df.to_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx")
    return exchange1


def read_excel(path):
    if 'csv' in path:
        df=pd.read_csv(path,index_col=0)
    else:
        df=pd.read_excel(path,index_col=0)
    if 'index' in df.columns:
        df=df.drop(columns=["index"])
    if 'level_0' in df.columns:
        df=df.drop(columns=["level_0"])
    if 'Unnamed: 0' in df.columns:
        df=df.drop(columns=['Unnamed: 0'])    
    return df

def common_stock_list_v1_5000_polygon_real_time():
    if 'win' in socket.gethostname():
        socket_path='G:/My Drive/'
        csv2='G:/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    else:
        socket_path=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/'
        csv2=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    # csv2=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/6 IBKR/polygon_list.csv'
    # da=total.read_csv(csv2)
    da=read_excel(csv2)
    da
    da=da.sort_values(by='market_cap',ascending=False)
    da
    da['mc1']=[int(item/1000000) for item in da['market_cap'].values]
    common_stock_list_v1=da['Ticker'].values.tolist()
    return common_stock_list_v1


from datetime import datetime,timedelta
import requests
import pandas as pd

def feature_engineering(df):
    df['Close1']=df["Close"].shift(periods=1)

    df['SMA10'] = df["Close"].rolling(min_periods=1, window=10).mean()
    df['SMA20'] = df["Close"].rolling(min_periods=1, window=20).mean()
    df['SMA50'] = df["Close"].rolling(min_periods=1, window=50).mean()
    df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
    df['SMA300'] = df["Close"].rolling(min_periods=1, window=300).mean()
    df['SMA500'] = df["Close"].rolling(min_periods=1, window=500).mean()
    df['SMA100'] = df["Close"].rolling(min_periods=1, window=100).mean()
    df['SMA1000'] = df["Close"].rolling(min_periods=1, window=1000).mean()
    df['SMA2000'] = df["Close"].rolling(min_periods=1, window=2000).mean()

    df["MAX50"] = df["High"].rolling(min_periods=1, window=50).max()
    df["MAX100"] = df["High"].rolling(min_periods=1, window=100).max()
    df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()

    df["MIN50"] = df["Low"].rolling(min_periods=1, window=50).min()
    df["MIN100"] = df["Low"].rolling(min_periods=1, window=100).min()
    df["MIN200"] = df["Low"].rolling(min_periods=1, window=200).min()
    

    df['Close2'] = df['Close'].pct_change()
    df['High2'] = df['High'].pct_change()
    df['Low2'] = df['Low'].pct_change()
    df['Open2'] = df['Open'].pct_change()
    df['Volume2'] = df['Volume'].pct_change()
    return df

def polygon_v3(ticker,minute1,limit1,past1,today1):
    link5='https://api.polygon.io/v2/aggs/ticker/{}/range/{}/day/{}/{}?adjusted=true&sort=asc&limit={}&apiKey={polygon_api_key}'.format(ticker,minute1,past1,today1,limit1)
    data3=requests.get(link5).json()

    df4=pd.DataFrame.from_dict(data3['results'])
    df4
    # columns2=['Volume','vol_weighted_price','Open','Close','High','Low','Timestamp','#_transactions']
    df4=df4.rename(columns={'c':'Close','h':'High','l':'Low','o':'Open','v':'Volume','t':'Timestamp'})
    # df4.columns=columns2
    df4['Timestamp']=df4['Timestamp']/1000
    df4=df4[['Timestamp','Open','High','Low','Close','Volume']]
    return df4

def generate_company_name(ticker):
    
    endpoint=f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}"
    # Make the request
    response = requests.get(endpoint)

    # Raise an error if the request failed
    response.raise_for_status()

    # Parse the JSON result
    data = response.json()
    data
    print("data: ",data)

    company_name=data['results']['name']
    print("company_name: ",company_name)
    return company_name

def stock_list_11000():
    endpoint='https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?apiKey={polygon_api_key}'
    response = requests.get(endpoint)
    # Raise an error if the request failed
    response.raise_for_status()
    # Parse the JSON result
    data = response.json()
    data
    df_total=pd.DataFrame(data['tickers'])
    df_day = pd.DataFrame(data['tickers'])['day'].apply(pd.Series)
    df_day
    df_total = pd.concat([df_total, df_day], axis=1)
    df_total
    df_total['trade_volume']=df_total['v']*df_total['c']
    df_total
    df_total=df_total.sort_values(by='trade_volume',ascending=False)
    df_total=reset_index(df_total)
    stock_list=df_total['ticker'].values.tolist()
    return stock_list


from datetime import datetime,timedelta
import requests
import pandas as pd

def stock_list_5000():
    endpoint='https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?apiKey={polygon_api_key}'
    response = requests.get(endpoint)
    # Raise an error if the request failed
    response.raise_for_status()
    # Parse the JSON result
    data = response.json()
    data
    df_total=pd.DataFrame(data['tickers'])
    df_day = pd.DataFrame(data['tickers'])['day'].apply(pd.Series)
    df_day
    df_total = pd.concat([df_total, df_day], axis=1)
    df_total
    df_total['trade_volume']=df_total['v']*df_total['c']
    df_total
    df_total=df_total.sort_values(by='trade_volume',ascending=False)
    df_total=reset_index(df_total)
    stock_list=df_total['ticker'].values.tolist()
    
    df=pd.DataFrame()
    


    i=0
    for i in range(len(stock_list)):
        try:
            ticker=stock_list[i]
            endpoint=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
            response = requests.get(endpoint)
            # Raise an error if the request failed
            response.raise_for_status()
            # Parse the JSON result
            data = response.json()
            
            json_data=data['results']
            
            new_row = pd.DataFrame(json_data, index=[0])

            # Append the new row to the DataFrame
            df = pd.concat([df, new_row], ignore_index=True)
            df
        except Exception as e:
            print(ticker,i,e)

    
    df1=df[df['type']=='CS']
    # [['ticker','market_cap','primary_exchange']]

    df1=df1.sort_values(by='market_cap',ascending=False)

    df1=reset_index(df1)
    df1
    stock_list=df1['ticker'].values.tolist()
    return stock_list
def feature_engineering(df):
    df['Close1']=df["Close"].shift(periods=1)

    df['SMA10'] = df["Close"].rolling(min_periods=1, window=10).mean()
    df['SMA20'] = df["Close"].rolling(min_periods=1, window=20).mean()
    df['SMA50'] = df["Close"].rolling(min_periods=1, window=50).mean()
    df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
    df['SMA300'] = df["Close"].rolling(min_periods=1, window=300).mean()
    df['SMA500'] = df["Close"].rolling(min_periods=1, window=500).mean()
    df['SMA100'] = df["Close"].rolling(min_periods=1, window=100).mean()
    df['SMA1000'] = df["Close"].rolling(min_periods=1, window=1000).mean()
    df['SMA2000'] = df["Close"].rolling(min_periods=1, window=2000).mean()

    df["MAX50"] = df["High"].rolling(min_periods=1, window=50).max()
    df["MAX100"] = df["High"].rolling(min_periods=1, window=100).max()
    df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()

    df["MIN50"] = df["Low"].rolling(min_periods=1, window=50).min()
    df["MIN100"] = df["Low"].rolling(min_periods=1, window=100).min()
    df["MIN200"] = df["Low"].rolling(min_periods=1, window=200).min()
    

    df['Close2'] = df['Close'].pct_change()
    df['High2'] = df['High'].pct_change()
    df['Low2'] = df['Low'].pct_change()
    df['Open2'] = df['Open'].pct_change()
    df['Volume2'] = df['Volume'].pct_change()
    return df




#%%
import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

from youtube_data import *
from ai_moderator import *
from utils import *
from dataframe_stuff import *
from make_credentials import *
from spreadsheet import *

from pathlib import Path
from openai import OpenAI
def audio_download_v3(name_prefix,input1,audio_folder,random_voices=False):
    speech_file_path = f"{audio_folder}{name_prefix}.mp3"
    actor_list=['echo','onyx','alloy','nova']
    actors = {
        'man1': 'echo',
        'man2': 'fable',
        'man3': 'onyx',
        'woman1': 'alloy',
        'woman2': 'nova',
        'woman3': 'shimmer'
    }
    actor='alloy'
    if random_voices:
        actor=actor_list[random.randint(0,3)]
    response = client.audio.speech.create(
    model="tts-1",
    voice=actor,
    input=input1
    )

    response.stream_to_file(speech_file_path)

def audio_download(name_prefix,input1):
    speech_file_path = f"data/audios/{name_prefix}.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=input1
    )

    response.stream_to_file(speech_file_path)
# %%
# f'https://www.google.com/search?q={search}&tbm=isch'
ii=0

def save_news_images(list1,driver):
    
    search_list=[item for item in list1 if len(item)>10]
    search_list

    for ii in range(len(search_list)):
        time.sleep(1)
        search=search_list[ii]
        driver.get(f'https://www.bing.com/images/search?q={search}&form=HDRSC3')


        ming=driver.find_elements(By.XPATH,'//img[@class="mimg"]')
        ming

        ming

        # ming
        # imgs=driver.find_elements(By.TAG_NAME,'img')
        # imgs
        for iii,item in enumerate(ming[:5]):
            content=item.get_attribute('src')
            content

            # image_url = 'https://example.com/image.jpg'

            # Send an HTTP GET request to the image URL
            response = requests.get(content)

            folder_name='data/news_images'
            name=search[:20]+f" {iii}"
            local_file_path = f'{folder_name}/{name}.png'

            # Check if the request was successful (HTTP status code 200)
            if response.status_code == 200:
                # Get the content of the response (the image data)
                image_data = response.content
                
                # Specify the local file path where you want to save the image
                # local_file_path = 'data/temp.jpg'
                
                # Open a local file in binary write mode and write the image data to it
                with open(local_file_path, 'wb') as file:
                    file.write(image_data)

    for ii in range(len(search_list)):
        # time.sleep(1)
        search=search_list[ii]
        name_prefix=search[:20]
        audio_download(name_prefix,search)
        print(ii)
    return search_list


# data:image/jpeg;base64,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

# with open(local_file_path, 'wb') as file:
#     #identify image to be captured
#     #write file
#     file.write(content.screenshot_as_png)
#     print(f"Image downloaded and saved to {local_file_path}")

import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Directory containing the images and audio file
def make_video(audio_folder,image_folder,image_name_prefix,image_files):

    # List of image filenames (change these to match your file names)
    imagelist=os.listdir(image_folder)
    imagelist=[item for item in imagelist if image_name_prefix in item]
    # image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

    # Audio file name (change this to match your audio file)
    audio_file = audio_folder+ f"{image_name_prefix}.mp3"

    # Video output file name
    output_video_file = f"data/youtube2/{image_name_prefix}.mp4"

    # Frame rate (number of frames per second)
    
    # Duration of each image in seconds
    
    

    # Load the audio file
    audio = AudioFileClip(audio_folder + audio_file)
    audio=audio.volumex(1.3)
    frame_rate = 30
    
    audio_duration = audio.duration
    each_length=audio_duration/len(imagelist)
    image_duration = int(each_length)
    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (audio.fps * 2, audio.fps * 2))

    # Loop through the images and add them to the video
    for image_file in image_files:
        image = cv2.imread(image_folder + image_file)
        for _ in range(int(audio.fps * image_duration)):
            video_writer.write(image)

    # Release the video writer
    video_writer.release()

    # Combine the video with the audio
    final_video = VideoFileClip(output_video_file)
    final_video = final_video.set_audio(audio)

    # Write the final video to a file
    final_video.write_videofile(output_video_file, codec="libx264")

    # Clean up temporary files
    final_video.close()

def read_stock_list():
    with open('data/stock_list.txt','r') as f:
        tickers=f.readline()
    tickers=tickers.split(',')
    return tickers

def audio_download_v2(folder='AAPL',name_prefix='a1',input1='news',role='man1'):
    path=f"data/audios/{folder}"
    if not os.path.exists(path):
        os.makedirs(path)
   
    actors = {
        'man1': 'echo',
        'man2': 'fable',
        'man3': 'onyx',
        'woman1': 'alloy',
        'woman2': 'nova',
        'woman3': 'shimmer'
    }

    speech_file_path = f"data/audios/{folder}/{name_prefix}.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice=actors[role],
    input=input1
    )

    response.stream_to_file(speech_file_path)
    return speech_file_path

def make_inter_videos(search_list):
    for ii in range(len(search_list))[0:]:
        try:
            search=search_list[ii]
            image_name_prefix=search[:20]


            image_name_prefix

            

            imagelist=os.listdir(image_folder)
            imagelist

            image_name_prefix

            imagelist=[image_folder+item for item in imagelist if image_name_prefix in item]
            imagelist

            image_files=imagelist
            if len(imagelist)==0:
                filepath=image_folder+image_name_prefix+'.png'
                make_text_image(search,filepath)
                imagelist=[filepath]


            # image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

            # Audio file name (change this to match your audio file)
            audio_file = f"{image_name_prefix}.mp3"
            audio_file

            # fps=24
            # Video output file name
            output_video_file = f"data/youtube1/{image_name_prefix}.mp4"

            audio_clip = AudioFileClip(audio_folder + audio_file)
            frame_rate = 1
            audio_duration = audio_clip.duration
            each_length=audio_duration/len(imagelist)
            image_duration = max(3,int(each_length))

            duration=image_duration
            image_clips = [ImageSequenceClip([img], durations=[duration]) for img in image_files]
            # from moviepy.editor import ImageSequenceClip, VideoFileClip, concatenate_videoclips
            # Concatenate the image clips to create the final video
            video_clip = concatenate_videoclips(image_clips, method="compose")
            video_clip = video_clip.set_duration(audio_duration).set_audio(audio_clip)
            # Write the final video to a file using H.264 codec
            # video_clip.write_videofile(output_video_file, codec="libx264")

            # Write the final video to a file
            # final_video.write_videofile("output_with_subtitles.mp4", codec="libx264", fps=video_clip.fps)
            video_clip.write_videofile(output_video_file.replace('-',''), codec="libx264", fps=frame_rate)  # Adjust the fps value as needed
            # Clean up
            video_clip.close()
            print("ii: ",ii)
        except Exception as e:
            print( 0 ,' = >>> some error = ',e)
    
        

def make_final_video(search_list):
    # video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Add the file paths of your video files
    video_files=os.listdir('data/youtube2')
    video_files=['data/youtube2/'+item for item in video_files]
    video_files


    new_list=[]
    for item in search_list:
        for video3 in video_files:
            item=item[:20]
            if item in video3:
                new_list.append(video3)
                print('good!')
    
    video_clips=[]
    for file in new_list:
        video_clips.append(VideoFileClip(file).resize(newsize=(1920, 1080)) )
    video_clips

    # video_clips = [VideoFileClip(file).resize(newsize=(1920, 1080)) for file in video_files]
    # video_clips

    # from moviepy.editor import VideoFileClip, VideoFileClipList
    # final_video = VideoFileClipList(video_clips).concatenate()
    final_video = concatenate_videoclips(video_clips)


    import moviepy.editor as mpe
    # final_video = mpe.concatenate(video_clips)

    # Write the concatenated video to a file
    # concat_clip.write_videofile("concatenated_video.mp4")

    final_video.write_videofile("data/youtube3/final.mp4", codec="libx264", fps=30)
    # video_clip.write_videofile(output_video_file, codec="libx264", fps=30)
    for clip in video_clips:
        clip.close()
    final_video.close()

    # video_audio(wjslist)
    # Iterate through the files and remove them
    
    remove_files('data/youtube2')
    # remove_files('data/youtube2')
    remove_files('data/audios')
    remove_files('data/news_images')

def youtube_upload(video_title,description):
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   


    
    timedelta1=0
    timedelta2=100
    today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
    today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
    past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
    past2=datetime.strptime('20210218', "%Y%m%d").timestamp()


    title= f'{today1}_{video_title}_news'
    filename=os.listdir('data/youtube2')[-1]
    file_name=f'data/youtube2/{filename}'
    request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
        "categoryId": '22',
        "description": description,
        "title": title,
        "tags": 'news'
        },
        "status": {
        "privacyStatus": 'public'
        }
    },
    
    # TODO: For this request to work, you must replace "YOUR_FILE"
    # with a pointer to the actual file you are uploading.
    media_body=googleapiclient.http.MediaFileUpload(file_name,chunksize=-1, resumable=True)
    )


    # output= AuxMakeYoutubeRequest(request)


    request.next_chunk()


import requests
from bs4 import BeautifulSoup
import re

def get_pe_mc_div(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    div_content = soup.find_all('tr', class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
    div_content

    class_name = "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)".replace(" ", ".").replace("(", "\(").replace(")", "\)")

    # Find all tr elements with the specified class
    #//td[@data-test="PE_RATIO-value"]
    elements = soup.find_all('tr', class_=class_name)
    elements

    def find_value(datatest):
        pe_ratio_element = soup.find('td', {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-test': datatest})
        text1=pe_ratio_element.text
        print("text1: ",text1)
        if "B" in text1:
            text1=text1.replace('B','')
            text1=float(text1)
        elif "T" in text1:
            text1=text1.replace('T','')
            text1=float(text1)*1000
        
        elif "M" in text1:
            text1=text1.replace('M','')
            text1=float(text1)/1000
        elif "N/A" in text1:
            return 'nan'
        elif "%" in text1:

            # Regular expression pattern to find text inside parentheses
            pattern = r"\((.*?)\)"

            # Use re.findall to find all matches
            matches = re.findall(pattern, text1)
            return matches
        
        else:
            text1=float(text1)

        return    text1

    per=find_value('PE_RATIO-value')
    per

    mc=find_value("MARKET_CAP-value")
    mc
    div=find_value("DIVIDEND_AND_YIELD-value")
    div
    return per,mc,div
def remove_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data

# Example usage
import numpy as np
import matplotlib.pyplot as plt

# List of numbers
# numbers = [1, 2, 3, 4, 5]
def regression(numbers):
    numbers = [x for x in numbers if not math.isnan(x)]
    # Generating the same number of points as the list of numbers for the x-axis
    x = list(range(len(numbers)))
    y = numbers

    # Calculating the sum of x, y, x*y and x^2
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_xx = sum([i**2 for i in x])

    # Number of data points
    N = len(x)

    # Calculating slope (m) and intercept (b)
    slope = (N * sum_xy - sum_x * sum_y) / (N * sum_xx - sum_x**2)
    intercept = (sum_y - slope * sum_x) / N

    # Generating the regression line
    regression_line = [slope * xi + intercept for xi in x]

    # Plotting the points and the regression line
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, regression_line, color='red', label='Regression Line')

    # Annotating the slope
    plt.text(1, 4, f'Slope: {slope:.2f}', fontsize=12)

    # Adding labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Line')
    plt.legend()

    # Showing the plot
    plt.show()
    return slope,intercept
import requests,json

def financials(ticker):
    url=f'https://api.polygon.io/vX/reference/financials?ticker={ticker}&timeframe=quarterly&limit=100&apiKey={polygon_api_key}'

    
    # url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
    response=requests.get(url)

    json1=response.json()
    json1

    stock_name=json1['results']
    stock_name

    df=pd.DataFrame(stock_name)
    df


    total_columns=[]
    do=pd.DataFrame()
    for i in range(len(df)):
        columns1=[]
        rows1=[]
        id=df['id'][i].split(":")[1]+'_'+df['id'][i].split(":")[2]
        # df['financials'][i]['balance_sheet']


        for main_key in df['financials'][i].keys():
            # for item in df['financials'][i][main_key]:


            for key,values in df['financials'][i][main_key].items():
                value=values['value']  
                rows1.append(value)  
                columns1.append(key)
                    

        dt=pd.DataFrame(rows1).T
        # dt=dt.set_index(0).T
        # dt=dt.set_index(0)
        # dt=dt.T
        dt.columns=columns1
        # dt=reset_index(dt)
        dt=dt.rename(index={0: id})
        # dt.set_index(id)

        # do=pd.concat([do,dt])
        do = pd.concat([do, dt])
        # do=reset_index(do)
        total_columns.extend(columns1)

    do = do.iloc[::-1]
    return do

def draw_slope(ticker):
    try:
        do=financials(ticker)
        column_target='revenues'
        # column_target='gross_profit'
        # for item in do.columns:
        #     if 'gross' in item:
        #         print("item: ",item)


        numbers=do[column_target].dropna().values.tolist()
        numbers = remove_outliers(numbers)
        min1=min(numbers)
        max1=max(numbers)
        numbers2=[(item -min1)/(max1-min1) for item in numbers]
        numbers2
        slope1,intercept=regression(numbers)
        rev_slope,intercept=regression(numbers2)
        

        column_target='net_income_loss'
        numbers=do[column_target].dropna().values.tolist()
        numbers = remove_outliers(numbers)
        min1=min(numbers)
        max1=max(numbers)
        numbers2=[(item -min1)/(max1-min1) for item in numbers]
        numbers2
        slope1,intercept=regression(numbers)
        income_slope,intercept=regression(numbers2)
        

    except:
        print("\n>> len(do)= ", len(do))

        return 0,0,do
    return rev_slope,income_slope,do

def generate_qna_audio(ticker,driver,filename):
    company_name=generate_company_name(ticker)
    print("company_name: ",company_name)
    print("ticker: ",ticker)

    company_name=company_name.replace('Class A','')
    company_name=company_name.replace('Common Stock','')
    print("company_name: ",company_name)

    news_list=[]


    search=f'what is the product name of {company_name}'
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        answers=answers+item.text
    print("answers: ",answers)
    if len(answers)==0:
        print('more')
        answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
        print("answers: ",answers)
    QnA=search +"?  " + answers
    answers2=copy.deepcopy(answers)
    print("QnA: ",QnA)
    news_list.append(QnA)

    search=f'what do they sell from {company_name}'
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        answers=answers+item.text
    print("answers: ",answers)
    if len(answers)==0:
        print('more')
        answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
        print("answers: ",answers)
    QnA=search +"?  " + answers
    print("QnA: ",QnA)
    news_list.append(QnA)

    per,mc,div,company_description=yahoo_company(ticker)
    company_description


    productname_element=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    productname_element
    # 
    content=company_description+productname_element
    define=f'what is name of product of company {company_name}. write less than 10 words answer'
    product_name=gpt_answer(content,define)
    product_name



    if len(product_name)==0 or company_name in product_name or 'investor' in product_name or 'sorry' in product_name.lower() or 'not' in product_name.lower():
        product_name='product'
    print("product_name: ",product_name)


    search=f'what does {product_name} from {company_name} do'
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        answers=answers+item.text
    print("answers: ",answers)
    if len(answers)==0:
        print('more')
        answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
        print("answers: ",answers)
    QnA=search +"?  " + answers
    print("QnA: ",QnA)
    news_list.append(QnA)




    search=f'why {product_name} of {company_name} so special'
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        answers=answers+item.text
    print("answers: ",answers)
    if len(answers)==0:
        print('more')
        answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
        print("answers: ",answers)
    QnA=search +"?  " + answers
    print("QnA: ",QnA)
    news_list.append(QnA)

    search=f'review of {product_name} of {company_name}'
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        answers=answers+item.text
    print("answers: ",answers)
    if len(answers)==0:
        print('more')
        answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
        print("answers: ",answers)

    QnA=search +"?  " + answers
    print("QnA: ",QnA)
    news_list.append(QnA)

    #f'{company_name} is about what?', f'which industry is {company_name} in ?',
    question_list=[
    f'who are competitors of {company_name}?']


    for search in question_list:
        url=f'https://www.google.com/search?q={search}'
        driver.get(url)
        ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
        answers=''
        for item in ulist:
            print(item.text)
            answers=answers+item.text

        QnA=search +" " + answers
        QnA

        news_list.append(QnA)

    QnA
    # 
    # total_news=''
    # tickerdot = '.'.join(ticker[i] for i in range(len(ticker)))
    # tickerdot

    # item

    # for item in news_list:
    #     new_sentence=item.replace(company_name,f"{company_name} (ticker. {tickerdot}.)")
    #     total_news=total_news+new_sentence
    # total_news


    # 
    # print("\n>> len(total_news)= ", len(total_news))

    answer3=gpt_answer(str(news_list),f"summarize in great details in question and answer format.")
    answer3
    print("\n>> len(answer3)= ", len(answer3))

    answer3

    # timestamp1=str(int(datetime.now().timestamp()))
    # name_prefix='b'+timestamp1
    content=answer3
    audio_download_v2(folder=ticker,name_prefix=filename,input1=content,role='man3')
    answer3


def seconds_to_srt_time_format(seconds):
    return str(timedelta(seconds=seconds)).replace('.', ',')

def generate_srt(sentences, total_duration):
    num_sentences = len(sentences)
    duration_per_sentence = total_duration / num_sentences
    srt_entries = []

    for index, sentence in enumerate(sentences):
        start_time = index * duration_per_sentence
        end_time = start_time + duration_per_sentence
        srt_entries.append({
            "index": index + 1,
            "start": seconds_to_srt_time_format(start_time),
            "end": seconds_to_srt_time_format(end_time),
            "text": sentence
        })

    return srt_entries

def write_srt_file(srt_entries, filename):
    with open(filename, 'w') as file:
        for entry in srt_entries:
            file.write(f"{entry['index']}\n")
            file.write(f"{entry['start']} --> {entry['end']}\n")
            file.write(f"{entry['text']}\n\n")



def upload_youtube_v2(folder1,filename):
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   



    timedelta1=0
    timedelta2=100
    today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
    today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
    past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
    past2=datetime.strptime('20210218', "%Y%m%d").timestamp()



    file_list=os.listdir(folder1)
    # for filename in file_list:

    file_name=folder1+filename
    description=filename.split('.')[0]
    title= f'{today1}_{description}_news'
    request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
        "categoryId": '22',
        "description": description,
        "title": title,
        "tags": 'news'
        },
        "status": {
        "privacyStatus": 'public'
        }
    },

    # TODO: For this request to work, you must replace "YOUR_FILE"
    # with a pointer to the actual file you are uploading.
    media_body=googleapiclient.http.MediaFileUpload(file_name,chunksize=-1, resumable=True)
    )


    # output= AuxMakeYoutubeRequest(request)


    data=request.next_chunk()
    return data

def remove_files(folder1):
    for file in os.listdir(folder1):
        file_path = os.path.join(folder1, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")
def upload_subtitle(video_id,subtitle_fullpath):
    # Assume `service` is your authenticated YouTube API client
    # Assume `video_id` is the ID of the uploaded video
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   

    # Prepare the request body for the caption
    caption_body = {
        'snippet': {
            'videoId': video_id,
            'language': 'en',  # Language of the subtitles
            'name': 'English Subtitles',  # Name of the subtitle track
            'isDraft': False
        }
    }

    # Path to your subtitle file

    # Create the media file upload object
    media_body = MediaFileUpload(subtitle_fullpath, mimetype='text/plain', resumable=True)

    # Insert the captions
    caption_insert_request = youtube.captions().insert(
        part='snippet',
        body=caption_body,
        media_body=media_body
    )

    # Execute the request
    caption_response = caption_insert_request.execute()

    # Optionally, check the response for success
    print(caption_response)

def youtube_upload_folder(folder1):
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   


    
    timedelta1=0
    timedelta2=100
    today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
    today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
    past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
    past2=datetime.strptime('20210218', "%Y%m%d").timestamp()


    
    file_list=os.listdir(folder1)
    for filename in file_list:
        file_name=folder1+filename
        description=filename.split('.')[0]
        title= f'{today1}_{description}_news'
        request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
            "categoryId": '22',
            "description": description,
            "title": title,
            "tags": 'news'
            },
            "status": {
            "privacyStatus": 'public'
            }
        },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        # with a pointer to the actual file you are uploading.
        media_body=googleapiclient.http.MediaFileUpload(file_name,chunksize=-1, resumable=True)
        )


        # output= AuxMakeYoutubeRequest(request)


        request.next_chunk()

from PIL import Image, ImageDraw, ImageFont
def make_text_image(text,filepath):
    width = 400  # Adjust the width of the image
    height = 400  # Adjust the height of the image
    background_color = (255, 255, 255)  # RGB color (white in this example)

    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype("path_to_font_file.ttf", font_size)  # Replace with your font file path
    # OR
    font = ImageFont.load_default()  # Use a default font
    # text = "Hello, World!"  # Replace with your desired text
    text_color = (0, 0, 0)  # RGB color (black in this example)
    text_position = (50, 50)  # (x, y) coordinates of the text
    draw.text(text_position, text, fill=text_color, font=font)
    image.save(filepath)  # Specify the desired image format (e.g., PNG, JPEG)
    image.close()
import openai
from moviepy.editor import VideoFileClip, ImageSequenceClip
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key


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


import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key



import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

from openai import OpenAI
client = OpenAI()

def gpt_answer(content,define):
    try:

        message_list3=[{"role": "system", "content" : define},
                    {"role": "user", "content" : str(content)},    
                    ]
        completion = client.chat.completions.create(model="gpt-3.5-turbo" , #"gpt-3.5-turbo", 
                    messages = message_list3)
        completion=completion.choices[0].message.content

    except Exception as e:
        completion='>> error = time out for gpt...'+str(e)
    return completion
# define='summarize based on why the stock is going up.'
# summary=gpt_answer(content,define)
# summary


def find_repeated_substrings(word_list, min_length=2, min_repeats=3):
    substring_counts = Counter()

    # Iterate over each word
    for word in word_list:
        length = len(word)
        # Generate substrings for each word
        for start in range(length):
            for end in range(start + min_length, length + 1):
                substring = word[start:end]
                substring_counts[substring] += 1

    # Filter based on minimum repeats
    return {sub: count for sub, count in substring_counts.items() if count >= min_repeats}

# Sample list of words
# words = ['이미스머리띠', '샤넬머리띠', '티아라', '명품머리띠', '산리오머리띠', '벨벳머리띠', '고양이머리띠', '왕관', '밴드', '눈']

# Find repeated substrings
# repeated_substrs = find_repeated_substrings(keyword_list, min_length=2, min_repeats=3)
# repeated_substrs

def find_longest_repeated_substrings(word_list, min_length=2, min_repeats=3):
    substring_counts = Counter()

    # Iterate over each word
    for word in word_list:
        length = len(word)
        # Generate substrings for each word
        for start in range(length):
            for end in range(start + min_length, length + 1):
                substring = word[start:end]
                substring_counts[substring] += 1

    # Filter and find the longest repeated substring
    repeated_substrs = {sub: count for sub, count in substring_counts.items() if count >= min_repeats}
    longest_substring = max(repeated_substrs, key=lambda x: (repeated_substrs[x], len(x)), default=None)

    return longest_substring

from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pickle
import time 
import pandas as pd
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import requests
import os
import re
from collections import Counter
# Create download folder if not exist
# Specify the folder name you want to create
folder_name = "taobao_download"
# Check if the folder already exists, and if not, create it
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

# Open web browse
def open_driver():
    options = uc.ChromeOptions()
    # Creates a new instance of the ChromeOptions class to configure various options for the Chrome web browser.
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    # we are setting the profile.default_content_setting_values.notifications preference to 2. This will disable all notifications in the Chrome web browser.
    options.add_experimental_option("prefs",prefs)
    # # Adds the preferences that we created in the previous line to the ChromeOptions instance.
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")  # fatal
    options.add_argument('--no-sandbox')
    options.headless = False
    # Add a Random User Agent
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument("user-agent=%s" % user_agent) 
    # Option to set the user data directory, you should add your user data path
    # options.add_argument(r'--user-data-dir=C:\Users\Ahmed Farid\AppData\Local\Google\Chrome\User Data\Profile 1')
    
    options.add_argument(f'--user-data-dir=/Users/{getpass.getuser()}/Library/Application Support/Google/Chrome/Default')
    # This will disable the sandbox for the Chrome web browser. This may be necessary if you are running the Chrome web browser on a remote machine.
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # Creates a new instance of the Chrome web browser using the ChromeDriverManager class and the options instance that we created earlier.
    driver.maximize_window()
    # Maximizes the window for the Chrome web browser.
    print('Driver opened correctly!')
    # Prints a message to the console indicating that the Chrome web browser was opened successfully.
    return driver
# Open driver


import re

def find_exchange(ticker):
    
    try:

        df1=pd.read_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx",index_col=0)
        exchange1=0
        for i in range(len(df1)):
            if ticker == df1['ticker'][i]:
                exchange1=df1['Exchange'][i]
                #print("existing ticker exchange",ticker)
        if exchange1==0:
            print("not existing exchange info : ", ticker)
            
            url = "https://ycharts.com/companies/{}".format(ticker)
            payload = ""
            headers = {
                "cookie": "ycsessionid=2qz3d4y9pia7lsirwduwfoqsy68lxo0u; _ga=GA1.2.635129160.1644138754; _gid=GA1.2.916019816.1644138754; __gads=ID=93bc25b5583902a4-22af5cc377d00013:T=1644138753:S=ALNI_MZo9l0xXkE31mqmewQtnKQnTUUD5Q; __hstc=69688216.203ddbd23f614854901d1b6290dd0cc4.1644138757373.1644138757373.1644138757373.1; hubspotutk=203ddbd23f614854901d1b6290dd0cc4; __hssrc=1; _fbp=fb.1.1644138757715.487408360; _gcl_au=1.1.38652961.1644138758; quickflowsSingleSecurityCookieName=%7B%22displaySecurityId%22%3A%22AAPL%22%2C%22securityId%22%3A%22AAPL%22%7D; messagesUtk=a7090410a7a24598b5f7b00924eb45a1; page_view_ctr=3; __hssc=69688216.3.1644138757373",
                "authority": "ycharts.com",
                "cache-control": "max-age=0",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "cross-site",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "referer": "https://www.google.com/",
                "accept-language": "en-US,en;q=0.9,ko;q=0.8"
            }
            response = requests.request("GET", url, data=payload, headers=headers)
            data=response.text
            exchange1=data.split("&nbsp;|&nbsp;")[1].split("\n")[1].replace(" ","")

            print("scrape ychart", ticker, exchange1)
            dictionary={"ticker":[ticker],"Exchange":[exchange1]}

            df=pd.DataFrame.from_dict(dictionary)
            df1=df1.append(df)
            df=df1.append(df)
            df=df.drop_duplicates(keep="last",subset="ticker")
            df=df.reset_index()
            df=df.drop(columns=["index"])
            df.to_excel(f"/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/4 exchange list/exchange list.xlsx")
    except:
        exchange1='NASDAQ'    
    return exchange1