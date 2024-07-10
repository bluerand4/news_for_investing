#%%
from import_basics import *
from import_stocks2 import *


def convert_percentage_to_decimal(value):
    try:
        if isinstance(value, str) and value.endswith('%'):
            return float(value.rstrip('%')) * 0.01
        return value
    except ValueError:
        return value
# %%
def stock_analysis_com_update_financials_5000():

    driver=open_driver()
    driver
    # %%
    ticker='AAPL'

    # stock_list=stock_list_5000()
    # stock_list

    #%%

    # mongo_collection_names('stock')

    #%%
    de=mongo_get_df('stock','polygon_total_stock_info')
    de
    #%%
    stock_list=de[de['type']=='CS']['ticker'].values.tolist()
    print("\n>> len(stock_list)= ", len(stock_list))

    #%%
    for ticker in stock_list:
        do=pd.DataFrame()
        # driver=open_driver_loop()


        ticker_lower=ticker.lower()
        # url1=f'https://stockanalysis.com/stocks/{ticker_lower}/financials/?p=quarterly'
        # driver.get(url1)
        # url1=f'https://stockanalysis.com/stocks/{ticker_lower}/financials/cash-flow-statement/?p=quarterly'
        # driver.get(url1)

        # #%%
        # url1=f'https://stockanalysis.com/stocks/{ticker_lower}/financials/ratios/?p=quarterly'
        # driver.get(url1)


        # %%
        financial_list=['','balance-sheet/','cash-flow-statement/','ratios/']
        for financial in financial_list:
            try:
                url1=f'https://stockanalysis.com/stocks/{ticker_lower}/financials/{financial}?p=quarterly'
                driver.get(url1)

                time.sleep(3)
                # driver.

                tbody = driver.find_element(By.TAG_NAME, 'tbody')
                tbody

                thead = driver.find_element(By.TAG_NAME, 'thead')

                rows = thead.find_elements(By.TAG_NAME, 'tr')

                # Initialize a list to store the table data
                column_data = []

                # Iterate through each row and extract td elements
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, 'th')
                    cell_data = [cell.text for cell in cells]
                    column_data.append(cell_data)
                column_data


                rows = tbody.find_elements(By.TAG_NAME, 'tr')

                # Initialize a list to store the table data
                table_data = []

                # Iterate through each row and extract td elements
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    cell_data = [cell.text for cell in cells]
                    table_data.append(cell_data)


                df = pd.DataFrame(table_data)
                df


                # Apply the function to the entire DataFrame
                df = df.applymap(convert_percentage_to_decimal)
                df

                df.columns=column_data
                df


                do = pd.concat([do, df], ignore_index=True)
                do

                do
                time.sleep(3)
            except:
                pass
        #%%
        if len(do)>1:

            # %%
            do = do[do.columns.drop(list(do.filter(regex='\+')))]
            do
            # %%
            # do=copy.deepcopy(do)
            #%%
            do.columns = [' '.join(col).strip() for col in do.columns.values]
            do
            #%%
            filename=f'{ticker}_quarter.csv'
            path1=f'/Users/ryanchun1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/10_stock_analysis_com/{filename}'
            do.to_csv(path1)
            # %%
            mongo_set_df('stock_analysis_com',ticker,'Quarter Ended',do)

    # %%
    driver.quit()




#%%
    
import getpass
getpass.getuser()
#%%

def screenshot_simple_generate_max200(stock_list,folder_name):
    path1=f'data/{folder_name}'

    remove_files(path1)
    path1=f'/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/{folder_name}'
    remove_files(path1)
    # %%

    # path1='/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/9 practicce/7_feature_extraction/4_version/11_tradingview_alarm/data/max200_v2.txt'
    # path1
    # %%
    # with open(path1,'r') as f:
        # data1=f.readlines()
    # data1
    #%%
    # stock_list=data1[0].split(',')
    # %%


    # df0=mongo_get_df('screenshot','us_stock_close2_max1')
    #%%
    # df0['tradingview_link'].values.tolist()
    #%%
    # df=mongo_get_df('screenshot','us_stock_max2_max1')
    #%%
    # df['tradingview_link'][0]
    #%%
    driver=open_driver_loop()
    # data1=ast.literal_eval(data1)
    #%%
    #%%
    for i,link in enumerate(stock_list):
        try:
            link


            # exchange=find_exchange_v2(ticker)
            # exchange
            ticker=link.split('%3A')[1]
            # driver.get(f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located
            driver.get(link)
            time.sleep(10)


            button=driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]')

            if 'dropped' in button.find_element(By.TAG_NAME,'span').get_attribute('class'):
                # print('down now')
                pass
            else:
                button.click()
                # print('up now')
                pass
            time.sleep(1)
            # titles=driver.find_elements(By.XPATH,'//span[@class="title-cXDWtdxq itemTitle-KSzJG6_A"]')
            # infos=driver.find_elements(By.XPATH,'//span[@class="data-cXDWtdxq"]')

            try:
                time.sleep(3)
                alert = driver.switch_to.alert
                alert.accept()

                alert = driver.switch_to.alert
                alert.accept()
            except:
                pass
            time.sleep(10)




            # canvas = driver.find_elements(By.TAG_NAME,'canvas')
            # canvas
            # canvase=driver.find_elements(By.XPATH,'//canvas[@aria-hidden="true"]')



            time.sleep(3)
            pt.moveTo(124,153)

            time.sleep(1)
            # canvas=canvase[5]

            # Get the location and size of the canvas element
            # location = canvas.location
            # size = canvas.size

            # Take a screenshot of the entire page
            
            driver.save_screenshot(f'data/{folder_name}/{i}_{ticker}.png')

            driver.save_screenshot(f'/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/{folder_name}/{i}_{ticker}.png')
            print(i,ticker)
        except Exception as e:
            print(ticker,e)
    # %%


    driver.quit()
# %%

def stock_v4():
    print('he22')
    folder1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v2'
    data=os.listdir(folder1)
    tickers=[]
    for item in data:
        stock=item.split('_')[1].replace('.png','')
        tickers.append(stock)
    tickers


    dtt=mongo_get_df('stock','tradingview_slope')
    dtt

    dtt.columns


    list1=[]
    # ticker='AAPL'
    for ticker in tickers:
        try:
            revenue1=dtt[dtt['ticker']==ticker]['revenue1'].values[0]
            list1.append((ticker,revenue1))
        except:
            pass

    dn=pd.DataFrame(list1)
    dn.columns=['ticker','revenue']
    dn
    dn=dn.sort_values(by='revenue',ascending=False)
    dn=reset_index(dn)
    dn



    from_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v2/'

    to_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/stock_v4/'

    remove_everything(to_folder)

    from_stocks=os.listdir(from_folder)
    for i in range(len(dn)):
        ticker=dn['ticker'][i]
        for item in from_stocks:
            if ticker in item:
                break
        if os.path.isfile(from_folder+item):
            shutil.copy(from_folder+item, to_folder+f'{i}_'+item)
            print(item, 'done 12 ',i,len(folder1))



def make_google_drive_stock_v2():

    try:
        df2=mongo_get_df('screenshot','us_stock_max2_max1')
        #%%
        stock_list=df2['tradingview_link'].values.tolist()

        print('''> try: screenshot_simple_generate_max200()''',datetime.now())
        screenshot_simple_generate_max200(stock_list,'stock_v2')
    except Exception as e:
        print('''>> error: screenshot_simple_generate_max200(): ''',e,datetime.now())

def make_google_drive_stock_v1():


    
    try:
        df0=mongo_get_df('screenshot','us_stock_close2_max1')
        #%%
        stock_list=df0['tradingview_link'].values.tolist()

        print('''> try: screenshot_simple_generate_max200()''',datetime.now())
        screenshot_simple_generate_max200(stock_list,'stock_v1')
    except Exception as e:
        print('''>> error: screenshot_simple_generate_max200(): ''',e,datetime.now())

def make_google_drive_stock_v4():

        try:
            print('''> try: stock_v4()''',datetime.now())
            stock_v4()
        except Exception as e:
            print('''>> error: stock_v4(): ''',e,datetime.now())
