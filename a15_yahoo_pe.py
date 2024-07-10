#%%
import requests

url = "https://finance.yahoo.com/quote/TSLA"

querystring = {"p":"TSLA"}

payload = ""
headers = {"User-Agent": "insomnia/8.4.2"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
# %%
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
ticker='HCI'
per,mc,div,company_description=yahoo_company(ticker)
company_description
# %%
ticker='HCI'
#%%

#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


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

short_description
# %%
