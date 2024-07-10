from import_stocks2 import *
from sec_edgar_downloader import Downloader
dl = Downloader("eontech", "bluerand3@gmail.com")


def download_10k(ticker):
    dl.get("10-K", ticker, limit=1)
    time.sleep(3)
    folder=f'sec-edgar-filings/{ticker}'
    sub2=os.listdir(folder)[0]
    sub3=os.listdir(os.path.join(folder,sub2))[0]
    txt1=os.listdir(os.path.join(folder,sub2,sub3))[0]
    path1=os.path.join(folder,sub2,sub3,txt1)
    with open(path1,'r') as file:
        data=file.read()
    return data


def prepared_df(ticker,minute1,limit1,past1,today1):
    df=polygon_v3(ticker,minute1,limit1,past1,today1)
    df['Date']=[datetime.fromtimestamp(item,tz=pytz.timezone("US/Eastern")) for item in df['Timestamp']]
    df=feature_engineering(df)    
    return df

def get_data_from_10k(ticker,data):
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
    return answer1,answer2,answer3
