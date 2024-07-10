#%%
from import_stocks2 import *
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


def list_collections():
    return mongo_collection_names('list')


#%%

def list_save(database,filename,list1):

    dn=pd.DataFrame([str(list1)])
    dn.columns=['column1']
    dn
    
    mongo_set_df('list',f"{database}__{filename}",'column1',dn)
#%%
def list_read(database,filename):
    do=mongo_get_df('list',f'{database}__{filename}')
    data=do['column1'][0]
    data=ast.literal_eval(data)
    return data
def mongo_set_one_off(database,collection,list1):

    if type([])==type(list1):
        list1=','.join(list1)
    list1
    status='new'
    dn=pd.DataFrame.from_dict(dict(tickers=list1,status=status),orient='index').T
    dn

    mongo_set_df(database,collection,'tickers',dn)

def mongo_get_one_off(database,collection):
    dq=mongo_get_df(database,collection)
    ticker_list=dq['tickers'][0]
    ticker_list=ticker_list.split(',')

    dn=pd.DataFrame(['','old']).T
    dn.columns=['tickers','status']
    dn
    mongo_set_df(database,collection,'tickers',dn)
    if ticker_list==['']:
        ticker_list=[]
    return ticker_list
from pymongo import MongoClient

def mongo_set_df(database_name,collection_name,unique_column_name,df):
    
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Access a collection in the database
    collection = db[collection_name]

    for index, row in df.iterrows():
        # Construct the query and new values
        query = {unique_column_name: row[unique_column_name]}
        new_values = {"$set": row.to_dict()}
        collection.update_one(query, new_values, upsert=True)
    tickers_in_df = set(df[unique_column_name])
    collection.delete_many({unique_column_name: {"$nin": list(tickers_in_df)}})

def mongo_get_df(database_name,collection_name):
    
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Access a collection in the database
    collection = db[collection_name]

    documents = collection.find()
    df = pd.DataFrame(list(documents))
    return    df

def mongo_insert(df,no_dup_column,database_name,collection_name):
    
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Access a collection in the database
    collection = db[collection_name]
    
    documents = collection.find()
    do = pd.DataFrame(list(documents))
    values=do[no_dup_column].values.tolist()


    data=df.to_dict('records')
    data

    values

    new_dict=[]
    for item in data:
        if item[no_dup_column] in values:
            pass
        else:
            new_dict.append(item)
    new_dict
    if len(new_dict)>0:
        collection.insert_many(new_dict)
    documents = collection.find()
    df = pd.DataFrame(list(documents))
    return    df

def mongo_replace(index,target_column,new_value,database_name,collection_name):

    
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Access a collection in the database
    collection = db[collection_name]

    documents = collection.find()
    do = pd.DataFrame(list(documents))
    do

    
    document_id=do['_id'][index]

    # document_id = ObjectId(document_id)

    # Update the document
    collection.update_one({'_id': document_id}, {'$set': {target_column: new_value}})





def mongo_collection_names(database_name):
    # Your connection string (make sure to replace with your actual credentials and cluster URL)
    connection_string = "{mongo_link}"

    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Get a list of collection names
    collection_names = db.list_collection_names()
    
    return collection_names



def mongo_update_insert_one(database_name,collection_name,dn,target_column,UPSERT=True,IGNORE=False):
    connection_string = "{mongo_link}"
    #ryaneontech1:mongodbpw
    {mongo_id}
    # Create a connection using MongoClient
    mongoClient = MongoClient(connection_string)

    # Access your database
    db = mongoClient[database_name]

    # Access a collection in the database
    collection = db[collection_name]



    data=dn.to_dict('records')
    dict1=data[0]
    dict1
    #%%
    #%%
    # dict2 = {k: v for k, v in dict1.items() if not (k == 'ticker' and v == 'AAPL')}
    # dict2
    remove_list=[target_column]
    if IGNORE:
        ignore_list=list_minus(list(do.columns),list(dn.columns))
        for item2 in ignore_list:
            remove_list.append(item2)

    
    for key in remove_list:
        if key in dict1:
            del dict1[key]
    dict1
    target_value=dn[target_column][0]
    #%%
    query = {target_column: target_value}
    new_values = {"$set": dict1}

    # Update the document
    # collection.update_one(query, new_values)

    collection.update_one(query, new_values, upsert=UPSERT)
    #%%
    documents = collection.find()
    do = pd.DataFrame(list(documents))
    return do
    # %%



def insert_mongo_stock_comparison(ticker):
    per,mc,div,company_description,revenue1,insider,mc_rev,sector,industry=yahoo_company_v2(ticker.split('_')[-1])

    try:
        revslope,inslope,do,revslope2,inslope2=draw_slope(ticker)
        revslope=round(revslope*1000,1)
        inslope=round(inslope*1000,1)
        revslope2=round(revslope2*1000,1)
        inslope2=round(inslope2*1000,1)
    except:
        revslope=0
        inslope=0
        revslope2=0
        inslope2=0
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
        string1=string1+f"{key}: {value}"+'\n'
        # string1=string1+key
        # string1=string1+'\n'
        # string1=string1+value
        # string1=string1+'\n'


    dict2=dict(
        month3_1=month3_1 + "vs"+month3_2,
        
        month12_1=month12_1+"vs"+month12_2
    )
    for key,value in dict2.items():
        string1=string1+f"{key}: {value}"+'\n'
        # string1=string1+'\n'
        # string1=string1+value
    short_interest=dict1['short_interest'],
    Beta=dict1['Beta'],
    insider_owned=dict1['insider_owned'],
    insider_trade=dict1['insider_trade'],
    institut_owned=dict1['institut_owned'],
    institut_trade=dict1['institut_trade'],
    quick_ratio=dict1['quick_ratio'],

    total_dict=dict(ticker=ticker,per=per,mc=mc,div=div,revenue1=revenue1,insider=insider,mc_rev=mc_rev,sector=sector,industry=industry,revslope=revslope,
    inslope=inslope,
    revslope2=revslope2,
    inslope2=inslope2,
    month3_1=month3_1,
    month3_2=month3_2,
    month12_1=month12_1,
    month12_2=month12_2,
    short_interest=short_interest,
    Beta=Beta,
    insider_owned=insider_owned,
    insider_trade=insider_trade,
    institut_owned=institut_owned,
    institut_trade=institut_trade,
    quick_ratio=quick_ratio)

    total_dict

    df=pd.DataFrame.from_dict(total_dict)
    df

    # mongo_set_df('stock','comparison','ticker',df)

    mongo_insert(df,'ticker','stock','comparison')

    # dc=mongo_get_df('stock','comparison')
    # dc
