#%%
from sec_api import ExtractorApi
from sec_api import QueryApi
import requests
secapi='{secapi}'
queryApi = QueryApi(secapi)
extractorApi = ExtractorApi(secapi)
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
filings
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
    print(item_1_text[0:1500])
else:
    print("No 10-K filings found for AAPL")
# %%
from sec_api import FullTextSearchApi

fullTextSearchApi = FullTextSearchApi(api_key=secapi)
fullTextSearchApi
query = {
  "query": '"LPCN 1154"',
  "formTypes": ['8-K', '10-Q'],
  "startDate": '2020-01-01',
  "endDate": '2022-01-01',
}

response = fullTextSearchApi.get_filings(query)
response["filings"][0:4]


#%%
#%%
ticker='CAH'
#%%

url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'

response=requests.get(url)
#%%
json1=response.json()
cik1=json1['results']['cik']
cik1
#%%
# header={"Authorization":secapi,}
query={
  "query": ticker,
  "ciks": [cik1],

  "formTypes": ["10-K"]
  
}
response=requests.post(f'https://api.sec-api.io/full-text-search?token={secapi}',json=query)
response
# %%
text=response.json()
text
# %%
# %%
for item in text['filings']:
    if item['description']=='10-K':
        url1=item['filingUrl']
        break
#%%
url1# %%

# %%
'https://api.sec-api.io/extractor'

response=requests.get(f'https://api.sec-api.io/extractor?token={secapi}&item=1&url={url1}&type=text')
response

# %%
text2=response.json()
text2

# %%
print(response.text)
# %%


for 