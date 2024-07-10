#%%
from import_basics import *
# import textwrap
from import_mongo import * 

# import openai,getpass,os
# path1=f'{path_to_openai_api}'
# with open(path1,'r') as f:
#     key=f.readline()
# os.environ["OPENAI_API_KEY"] = key
# openai.api_key = key

# from openai import OpenAI
# client = OpenAI()

# ticker_list=['DSGX','CDNA','CB','JXN','ETN','VRT']
# interested_list=
ticker_list=input('MSFT,TSLA,AAPL = ')
mongo_set_one_off('news','additional_stocks_v2',ticker_list)
#%%
print('success')
