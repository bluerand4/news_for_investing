#%%
from import_basics import *
from bs4 import BeautifulSoup
from import_mongo import *
ticker='GS'
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

#%%

stock_list_v2=stock_list_5000()
#%%
ticker='GS'
dn=finviz_df(ticker)
dn
# mongo_collection_names('stock')
#%%
common_stock_list_v1_5000_polygon_real_time()
#%%
stock_list11000=stock_list_11000()
stock_list11000
#%%
print("\n>> len(stock_list11000)= ", len(stock_list11000))

#%%
#%%
for i,ticker in enumerate(stock_list11000):
    time.sleep(10)
    dn=finviz_df(ticker)
    target_column='ticker'


    mongo_update_insert_one('stock','finviz_v1',dn,target_column)
    print(i,"ticker: ",ticker)
# %%

# %%
