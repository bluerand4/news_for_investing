#%%
from import_basics import *
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


from pymongo import MongoClient

def mongo_set_df(database_name,collection_name,unique_column_name,df):
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
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
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
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
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
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

    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
    connection_string = "{mongo_link}"
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

    query = {target_column: target_value}
    new_values = {"$set": dict1}

    # Update the document
    # collection.update_one(query, new_values)

    collection.update_one(query, new_values, upsert=UPSERT)

    documents = collection.find()
    do = pd.DataFrame(list(documents))
    return do




def list_collections():
    return mongo_collection_names('list')



def list_save(database,filename,list1):

    dn=pd.DataFrame([str(list1)])
    dn.columns=['column1']
    dn
    
    mongo_set_df('list',f"{database}__{filename}",'column1',dn)
def list_read(database,filename):
    do=mongo_get_df('list',f'{database}__{filename}')
    data=do['column1'][0]
    data=ast.literal_eval(data)
    return data

import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)
#%%
print('he11')
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

# from import_stocks import *

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
    # plt.scatter(x, y, color='blue', label='Data Points')
    # plt.plot(x, regression_line, color='red', label='Regression Line')

    # # Annotating the slope
    # plt.text(1, 4, f'Slope: {slope:.2f}', fontsize=12)

    # # Adding labels and title
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.title('Linear Regression Line')
    # plt.legend()

    # # Showing the plot
    # plt.show()
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

#%%
# mongo_collection_names('stock')

#%%
# dtt=mongo_get_df('stock','tradingview_slope')

print('he22')
folder1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v2'
data=os.listdir(folder1)
tickers=[]
for item in data:
    stock=item.split('_')[1].replace('.png','')
    tickers.append(stock)
tickers
#%%
#%%
dtt=mongo_get_df('stock','tradingview_slope')
dtt
#%%
dtt.columns
#%%

list1=[]
ticker='AAPL'
for ticker in tickers:
    try:
        revenue1=dtt[dtt['ticker']==ticker]['revenue1'].values[0]
        list1.append((ticker,revenue1))
    except:
        pass
#%%
dn=pd.DataFrame(list1)
dn.columns=['ticker','revenue']
dn
dn=dn.sort_values(by='revenue',ascending=False)
dn=reset_index(dn)
dn
#%%


from_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v2/'

to_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v3_revenue_order/'
#%%
def remove_everything(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Error deleting {item_path}: {str(e)}")


def remove_files(folder1):
    for file in os.listdir(folder1):
        file_path = os.path.join(folder1, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")
remove_everything(to_folder)
#%%
from_stocks=os.listdir(from_folder)
for i in range(len(dn)):
    ticker=dn['ticker'][i]
    for item in from_stocks:
        if ticker in item:
            break
    if os.path.isfile(from_folder+item):
        shutil.copy(from_folder+item, to_folder+f'{i}_'+item)
        print(item, 'done 12 ',i,len(folder1))
#%%
'''

/Users/ryanchun1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v3_revenue_order/

'''
#%%
#%%
import shutil
def copy_paste(from_folder,to_folder):
    folder1=os.listdir(from_folder)
    print("\n>> len(folder1)= ", len(folder1))
    if not os.path.exists(to_folder):
        os.makedirs(to_folder)
    for i,item in enumerate(folder1):
        if os.path.isfile(from_folder+item):
            shutil.copy(from_folder+item, to_folder+item)
            print(item, 'done 12 ',i,len(folder1))


#%%
# #%%
# ticker=tickers[0]











# do=financials(ticker)


# column_target='revenues'
# column_target='gross_profit'
# column_target='net_income_loss'




