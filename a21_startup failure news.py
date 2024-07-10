#%%
from import_stocks2 import *
api_key=newsapi_org
query='startup failure news'
data=fetch_news_for_query(api_key, query, language='en', page_size=5)
data
# %%
import requests

# Replace 'YOUR_API_KEY' with your actual API key from newsapi.org
# api_key = 'YOUR_API_KEY'
url = 'https://newsapi.org/v2/everything'

# Define the search parameters
parameters = {
    'q': 'startup failure',  # Query for news stories about startup failure
    'apiKey': api_key,
    'language': 'en',
    'sortBy': 'relevancy',  # You can sort by 'publishedAt', 'relevancy', or 'popularity'
}

# Make the request
response = requests.get(url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON to get the articles
    articles = response.json().get('articles')
    for article in articles:
        print(article['title'], article['url'])
else:
    print("Failed to fetch news: ", response.status_code)

# %%
data=articles[0]
data
# %%
url=data['url']

# %%

import requests

url = "https://www.businessinsider.com/failure-museum-vc-norwest-venture-partners-startups-sean-jacobsohn"

payload = ""
headers = {"User-Agent": "insomnia/8.5.0"}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
# %%
import re

def remove_angle_bracket_strings(text):
    # Regular expression pattern to match strings within angle brackets
    pattern = r'<[^>]*>'
    
    # Replacing the matched strings with an empty string
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

# Example usage
original_text = remove_angle_bracket_strings(response.text)
original_text
# %%<!DOCTYPE html>\n<html lang="
text2=original_text.replace('\n','')
# %%
pattern = r'{[^>]*}'
    
# Replacing the matched strings with an empty string
text3 = re.sub(pattern, '', text2)
# %%
text3
# %%
