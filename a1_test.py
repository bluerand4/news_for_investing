#%%
from youtube_data import *
from ai_moderator import *
from utils import *
from dataframe_stuff import *
from make_credentials import *
from spreadsheet import *

from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

dummy=YoutuberDummyParameters()
# %%
dummy.client_secrets_file="data/client_secret.json"
# %%
import env
# %%
dummy.DEVELOPER_KEY=env.secret
# %%
# Initialize your YoutuberDummyParameters
# dummy = YoutuberDummyParameters()

# Create a YouTube client object
youtube = dummy.YoutubeExtractor(local_api=True)  # Use local_api=False for OAuth2
youtube
#%%
# Get your channel's details
channel_response = GetMyChannelsList(youtube)
channel_response
#%%
channel_id = channel_response['items'][0]['id']
channel_id
#%%
# Fetch comments from your channel
comments = []
next_page_token = None

while True:
    response = GetCommentThreadsListbyChannelID(youtube, channel_id, pageToken=next_page_token)
    comments.extend(response['items'])

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

# Now, `comments` contains all comment threads from your channel


#%%


# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.delete
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import env
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "data/client_secret.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
credentials
#%%
credentials=env.api_key
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)
#%%
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "data/client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.comments().delete(
        id="YOUR_COMMENT_ID"
    )
    request.execute()

if __name__ == "__main__":
    main()


#%%
# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

# def main():
    # Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = env.api_key

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)
#%%
request = youtube.comments().list(
    part="snippet",
    # parentId="UgzDE2tasfmrYLyNkGt4AaABAg"
    parentId="topLevelCommentId"
    
)
response = request.execute()

print(response)

# %%
'wow' in str(response)
# %%
# youtube = googleapiclient.discovery.build(
#     api_service_name, api_version, credentials=DEVELOPER_KEY)

request = youtube.channels().list(
    part="id",
    mine=True
)
response = request.execute()

channel_id = response['items'][0]['id']
print(channel_id)

# %%
request = youtube.channels().list(
    part="id",
    forUsername="Rand Green"  # Replace with the actual username
)
response = request.execute()
response
#%%
channel_id = response['items'][0]['id']
print(channel_id)

# %%
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load client secrets
client_secrets_file = 'data/client_secret.json'
scopes = ['https://www.googleapis.com/auth/youtube.readonly']

# Get credentials and create an API client
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

# Call the API
request = youtube.channels().list(part="id", mine=True)
response = request.execute()
print(response)

# %%

request = youtube.channels().list(
        part = "snippet,contentDetails,statistics",
        mine = True, 
        
    )
response = request.execute()
response
# %%
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load client secrets
client_secrets_file = 'data/client_secret.json'
scopes = ['https://www.googleapis.com/auth/youtube.readonly']

# Get credentials and create an API client
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

# Make an authorized request
request = youtube.channels().list(part='snippet,contentDetails,statistics', mine=True)
response = request.execute()

print(response)

# %%