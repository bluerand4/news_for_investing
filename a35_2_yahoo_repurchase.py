#%%
from import_basics import *
from bs4 import BeautifulSoup
ticker='QCOM'
#%%
from import_mongo import *
#%%
def repurchase_ratio_analysis(ticker):
    url=f'https://finance.yahoo.com/quote/{ticker}/cash-flow'

    # url = f'https://finance.yahoo.com/quote/{ticker}/profile/'
    headers = {"User-Agent": "insomnia/8.4.2"}

    # Make a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with class 'hello_there'
    #//tr[@class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "]
    class1="D(tbr) fi-row Bgc($hoverBgColor):h"
    div_content = soup.find_all('div', class_=class1)
    div_content

    div_content
    for item in div_content:
        
        if 'repurchase' in item.text.lower():
            print("item.text.lower(): ",item.text.lower())
            print('here 1')
            break
    try:
        repurchase_total=float(item.find_all('span')[1].text.replace(',',''))
        repurchase_total=abs(repurchase_total)

        market_cap,industry, short_description,company_name,PE=get_stock_details(ticker)
        market_cap=market_cap*1000000
        market_cap
        repurchase_ratio=repurchase_total/market_cap
        print("market_cap: ",market_cap)

        dict1=dict(ticker=ticker,repurchase_ratio=repurchase_ratio,market_cap=market_cap,industry=industry, short_description=short_description,company_name=company_name,PE=PE)
    except:
        dict1=dict(ticker=ticker,repurchase_ratio=0,market_cap=0,industry=0, short_description=0,company_name=0,PE=0)


    
    return dict1

def finviz_df(ticker):

    url = "https://finviz.com/quote.ashx"

    querystring = {"t":ticker,"p":"d"}

    payload = ""
    headers = {
        "cookie": "chartsTheme=dark; notice-newsletter=show",
        "User-Agent": "insomnia/8.4.2"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # print(response.text)


    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.text
    text

    '''
    class="js-snapshot-table snapshot-table2 screener_snapshot-table-body"
    '''

    div_content = soup.find_all('tr', class_="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) ")
    div_content

    class_name = "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)".replace(" ", ".").replace("(", "\(").replace(")", "\)")

    # Find all tr elements with the specified class
    #//td[@data-test="PE_RATIO-value"]
    elements = soup.find_all('tr', class_=class_name)
    elements


    #//table[@class="snapshot-table2 screener_snapshot-table-body"]
    # table = soup.find_all('table')
    # table=soup.find_all('table', class_="snapshot-table2 screener_snapshot-table-body")
    table=soup.find_all('table', class_="js-snapshot-table snapshot-table2 screener_snapshot-table-body")
    print("\n>> len(table)= ", len(table))
    table



    soup2 = BeautifulSoup(str(table[0]), 'html.parser').find_all('tr')
    # print("\n>> len(soup2)= ", len(soup2))

    soup2


    list1=[]
    list2=[]
    sum1=0
    for i in range(len(soup2)):
        cells=soup2[i].find_all('td')
        cells
        for ii,cell in enumerate(cells):
            # print("cell.text: ",cell.text)
            if type(cell.text)==type('text'):
                text1=cell.text
                # text1=text1.replace('/','divided by').replace('.','_')
            if ii%2==0:
                list1.append(text1)
            else:
                list2.append(text1)

        sum1+=1

    list2

    de=pd.DataFrame(list2).T
    de

    de.columns=list1
    de

    # dividend_rate=float(de['Dividend TTM'][0].split(' ')[1].replace('(','').replace('%)',''))
    # dividend_rate=dividend_rate/100
    # dividend_rate


    # short_interest=de['Short Float / Ratio'][0]
    # Beta=de['Beta'][0]
    # insider_owned=de['Insider Own'][0]
    # insider_trade=de['Insider Trans'][0]
    # institut_owned=de['Inst Own'][0]
    # institut_trade=de['Inst Trans'][0]
    # quick_ratio=de['Quick Ratio'][0]
    # Beta
    # dict1=dict(short_interest=short_interest,
    #             Beta=Beta,
    #             insider_owned=insider_owned,
    #             insider_trade=insider_trade,
    #             institut_owned=institut_owned,
    #             institut_trade=institut_trade,
    #             quick_ratio=quick_ratio,
    #             )
    de.columns = [col.replace('.', '_') for col in de.columns]

    de['ticker']=ticker
    columns = list(de.columns)

    columns.remove('ticker')
    columns.insert(0, 'ticker')

    dn = de[columns]
    dn
    return dn
# %%

stock_list11000=stock_list_11000()
stock_list11000
ticker='QCOM'
# %%

#%%
#%%    print("\n>> len(stock_list11000)= ", len(stock_list11000))

#%%
i
#%%
for i,ticker in enumerate(stock_list11000):
    if i <3148:
        continue
    time.sleep(10)
    # dn=finviz_df(ticker)
    try:
        dict1=repurchase_ratio_analysis(ticker)
        dict1

        if dict1['market_cap']==0:
            print(i,'not stock',ticker)
            continue





        dn1=pd.DataFrame.from_dict(dict1,orient='index').T
        dn1

        dn=finviz_df(ticker)
        dn

        dt=dn.merge(dn1,how='outer',on='ticker')
        dt
        target_column='ticker'


        mongo_update_insert_one('stock','finviz_v1',dt,target_column)
        print(i,"ticker: ",ticker)
    except Exception as e:
        content=f'{i}_{ticker}_{e}'
        print1(content,filename='error_finviz_v1')
        
# %%
