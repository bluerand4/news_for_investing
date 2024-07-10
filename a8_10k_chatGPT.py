#%%
from import_all import *
from import_sec import *

#%%
ticker='MEDP'
#%%
tickers=['TEAM','CDRE','BRZE','SKWD','ML','PANW']
sum1=0
for ticker in tickers:

    download_10k(ticker)

    '/Users/ryanchun1/Documents/2_coding/t7_2_trade_news/sec-edgar-filings/AAPL/10-K/0000320193-23-000106'

    folder=f'sec-edgar-filings/{ticker}'
    sub2=os.listdir(folder)[0]
    sub3=os.listdir(os.path.join(folder,sub2))[0]
    txt1=os.listdir(os.path.join(folder,sub2,sub3))[0]
    path1=os.path.join(folder,sub2,sub3,txt1)
    path1

    with open(path1,'r') as file:
        data=file.read()
    data

    TARGET_NAME='>business<'.lower()

    # TARGET_NAME='ITEM 7.'
    split_list=data.lower().split(TARGET_NAME)
    if len(split_list)>3:
        splited_list=data.lower().split(TARGET_NAME)[1].split('\n')[:20]
    else:
        splited_list=data.lower().split(TARGET_NAME)[-1].split('\n')[:20]
    print("\n>> len(splited_list)= ", len(splited_list))

    text1="".join(splited_list)
    text2=re.sub('<[^>]+>', '', text1)



    # webbrowser.open('')

    
    # os.system("open /System/Applications/Google Chrome.app")



    BLOCK=30000

    webbrowser.open('https://chat.openai.com/?model=gpt-4')

    time.sleep(5)

    data2=yahoo_company_v2(ticker)
    data2

    company_name=generate_company_name(ticker)

    os.system("open /Applications/Google\ Chrome.app")
    init=f'''
    this is summary of {company_name} with ticker symbol {ticker}.
    {data2}

    tell me about this company and prospect
    '''
    pyperclip.copy(init)
    with pt.hold(['command']):
        time.sleep(0.2)
        pt.press('v')
        time.sleep(0.1)
    time.sleep(2)
    pt.press('enter')
    time.sleep(2)
    pt.press('enter')
    time.sleep(2)
    pt.press('enter')
    sum1+=1
    if sum1>10:
        time.sleep(60*60*2)
        sum1=0
    time.sleep(60*3)
    with pt.hold(['command']):
        time.sleep(0.2)
        pt.press('r')
        time.sleep(0.1)
    time.sleep(5)

    ii_=len(text2)//BLOCK

    for i in range(ii_):
        os.system("open /Applications/Google\ Chrome.app")
        BLOCK=30000
        cleaned_text = text2[0+i*BLOCK:BLOCK+i*BLOCK]
        cleaned_text=cleaned_text+'\n\n summarize in great detail'
        print("\n>> len(cleaned_text)= ", len(cleaned_text))
        time.sleep(3)
        pyperclip.copy(cleaned_text)
        with pt.hold(['command']):
            time.sleep(0.2)
            pt.press('v')
            time.sleep(0.1)
        time.sleep(2)
        pt.press('enter')
        time.sleep(2)
        pt.press('enter')
        time.sleep(2)
        pt.press('enter')
        
        time.sleep(60*3)
        with pt.hold(['command']):
            time.sleep(0.2)
            pt.press('r')
            time.sleep(0.1)
        time.sleep(5)
        sum1+=1
        if sum1>10:
            time.sleep(60*60*2)
            sum1=0
