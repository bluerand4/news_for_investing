#%%
from import_basics import *
from import_stocks2 import *
def update_stock_analysis_com_5000_v1():
    def convert_percentage_to_decimal(value):
        try:
            if isinstance(value, str) and value.endswith('%'):
                return float(value.rstrip('%')) * 0.01
            return value
        except ValueError:
            return value
    # %%


    # %%
    #%%
    de=mongo_get_df('stock','polygon_total_stock_info')
    de
    de=de.sort_values(by='market_cap',ascending=False)
    de=reset_index(de)

    #%%
    stock_list=de[de['type']=='CS']['ticker'].values.tolist()
    print("\n>> len(stock_list)= ", len(stock_list))

    #%%
    for ii,ticker in enumerate(stock_list[:]):
        try:
            driver=open_driver()
            driver
        
            print(ii,"ticker: ",ticker)
            # break
            do=pd.DataFrame()
            # driver=open_driver_loop()


            ticker_lower=ticker.lower()


            financial_list=['','balance-sheet/','cash-flow-statement/','ratios/']
            for financial in financial_list:
                try:
                    url1=f'https://stockanalysis.com/stocks/{ticker_lower}/financials/{financial}?p=quarterly'
                    driver.get(url1)

                    time.sleep(10)
                    # driver.
                    try:
                        driver.find_element(By.XPATH,'//button[@class="absolute right-0 top-0 m-2 sm:right-1 sm:top-1"]').click()
                        time.sleep(2)
                    except:
                        pass
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

                    print(len(do))
                except Exception as e:
                    print('error ',ticker,e)
            driver.quit()
        except Exception as e:
            
            
            print('error v2',ticker,e)
            driver.quit()
            print('quit success',ticker)


        if len(do)>1:

            do = do[do.columns.drop(list(do.filter(regex='\+')))]
            do

            # do=copy.deepcopy(do)

            do.columns = [' '.join(col).strip() for col in do.columns.values]
            do

            filename=f'{ticker}_quarter.csv'
            path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/10_stock_analysis_com/{filename}'
            do.to_csv(path1)
            print('saved,',ticker,ii)
            # mongo_set_df('stock_analysis_com',ticker,'Quarter Ended',do)
            
    # %%
    # %%
    do=pd.DataFrame()
    #%%
    for ii,ticker in enumerate(stock_list[:]):
        print(ii,"ticker: ",ticker)
        # break
        # do=pd.DataFrame()
        # driver=open_driver_loop()

        filename=f'{ticker}_quarter.csv'
        try:
            ticker_lower=ticker.lower()
            path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/10_stock_analysis_com/{filename}'
            dx=read_excel(path1)
            # print("\n>> len(dx)= ", len(dx))
            for i in range(len(dx)):
                name1=dx['Quarter Ended'][i]
                name1=ticker+'-'+name1
                dx.loc[i,'Quarter Ended']=name1
            do=pd.concat((dx,do),axis=0)
            do=reset_index(do)

        except Exception as e:
            print('fail ,',ticker)
        
    # %%


    filename='total_v1.csv'
    do.to_csv(f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/10_stock_analysis_com/{filename}')
    #%%
    mongo_set_df('stock_analysis_com','total_v1','Quarter Ended',do)
    # %%
    path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/10_stock_analysis_com/'

    print(len(os.listdir(path1))  )
# %%
    driver.quit()
# update_stock_analysis_com_5000_v1()

