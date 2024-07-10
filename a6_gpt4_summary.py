#%%
import openai

from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


import yfinance as yf

from newsapi import NewsApiClient
newsapi_org='{newsapi_org}'

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
company_name='MSFT'
news=fetch_news_for_query(newsapi_org, query=company_name)
news=str(news)
news
#%%
def get_stock_details(ticker):
    stock = yf.Ticker(ticker)
    
    # Info is a dictionary containing various details about the stock
    info = stock.info
    
    market_cap = stock.info.get('marketCap')
    market_cap=round(market_cap/1000000000,2)
    industry = info.get('industry', 'N/A')
    short_description = info.get('longBusinessSummary', 'N/A')

    return market_cap,industry, short_description
get_stock_details('AAPL')
#%%

secapi='{secapi}'
from sec_api import ExtractorApi

extractorApi = ExtractorApi(secapi)
def pprint(text, line_length=100):
  words = text.split(' ')
  lines = []
  current_line = ''
  for word in words:
    if len(current_line + ' ' + word) <= line_length:
      current_line += ' ' + word
    else:
      lines.append(current_line.strip())
      current_line = word
  if current_line:
    lines.append(current_line.strip())
  print('\n'.join(lines))
# URL of Tesla's 10-K filing
filing_10_k_url = 'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm'
#%%
link_to_10k
#%%
# extract text section "Item 1 - Business" from 10-K
item_1_text = extractorApi.get_section(filing_10_k_url, '1', 'text')

print('Extracted Item 1 (Text)')
print('-----------------------')
pprint(item_1_text[0:1500])

#%%
from sec_api import ExtractorApi
from sec_api import QueryApi
queryApi = QueryApi(api_key=secapi)

query = {
  "query": { "query_string": { 
      "query": "ticker:TSLA",
  } },
  "from": "0",
  "size": "100",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

response = queryApi.get_filings(query)
import pandas as pd

metadata = pd.DataFrame.from_records(response['filings'])
#%%
metadata[metadata['formType']=='10-K']['linkToTxt'].values
metadata[metadata['formType']=='10-K']['linkToHtml'].values

link_to_10k=metadata[metadata['formType']=='10-K']['linkToFilingDetails'].values[0]
link_to_10k
#%%

#%%
item_1_text = extractorApi.get_section(link_to_10k, '1', 'text')
item_1_text
#%%
queryApi = QueryApi(secapi)

# construct query to search for Apple's (AAPL) latest 10-K filing
query = {
  "query": { "query_string": { "query": "ticker:AAPL AND formType:\"10-K\"" } },
  "sort": [{ "filedAt": { "order": "desc" } }],
  "from": "0",
  "size": "1",
  "source": ["url"]
}

# execute the query
filings = queryApi.get_filings(query)
#%%

#%%
# check if we got a result
if filings.get("total", {}).get("value", 0) > 0:
    # get the URL of the latest 10-K form
    filing_10_k_url = filings["hits"]["hits"][0]["_source"]["url"]

    # extract text section "Item 1 - Business" from 10-K
    item_1_text = extractorApi.get_section(filing_10_k_url, '1', 'text')

    print('Extracted Item 1 (Text) for AAPL')
    print('-----------------------')
    pprint(item_1_text[0:1500])
else:
    print("No 10-K filings found for AAPL")
#%%
ticker='MSFT'
stock = yf.Ticker(ticker)

# Info is a dictionary containing various details about the stock
info = stock.info

market_cap = stock.info.get('marketCap')
market_cap=round(market_cap/1000000000,2)
industry = info.get('industry', 'N/A')
short_description = info.get('longBusinessSummary', 'N/A')
#%%
short_description='SYNAPY Inc. this company'
company_name = short_description.split('.')[0]
company_name
#%%
short_description
#%%
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

define='summarize it: '
content='''
[("'I would rather clock out eternally': This Gen Z TikToker quit her office job and proclaimed she's happier struggling to pay bills than being a ‘corporate drone’ — here's why", 'Do the Zoomers have a point?'), ('Usher to headline the 2024 Super Bowl Halftime Show', 'This morning, the NFL confirmed that Usher will be the headlining performer for the Apple Music Super Bowl Halftime Show at Super Bowl LVIII next February in Las Vegas, capping off… not a single second of speculation? There’s usually a bit more hype for this …'), ('Enter The World Of Gen-Z Fragrance With Givaudan', 'If you’ve scrolled through your TikTok recently, there’s a high chance you’ve come across #perfumetok, the new Gen-Z-driven wave of content that’s elevating ni…'), ('Gen Z’s Social Media Dependency Is A Bridge, Not Barrier, For Advisors', 'For those wondering what the future of financial advising might hold for Gen Z, new data might offer some hope.'), ('The Best Stoner Movies: ‘Inherent Vice,’ ‘The Beach Bum,’ and More Films to Help You Blaze On', 'Whether it\'s April 20 or you just need to chill out, these 22 movies from "Dazed and Confused" to "Smiley Face" are perfect for sinking into the couch.')]
'''
message_list3=[{"role": "system", "content" : define},
            {"role": "user", "content" : content},
            
            ]
#%%
completion = openai.ChatCompletion.create(model="gpt-4" , #"gpt-3.5-turbo", 
            messages = message_list3)
completion=completion['choices'][0]['message']['content']
print("completion: ",completion)