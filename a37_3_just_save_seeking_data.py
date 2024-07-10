#%%
from import_basics import *
import textwrap
from import_mongo import * 

import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

from openai import OpenAI
client = OpenAI()

# def youtube_seek_alpha_v1():
#%%

#%%
def save_seeking_alpha_analyst_reports():
    #%%
    ticker_list=mongo_get_one_off('news','additional_stocks_v2')
    ticker_list
    #%%

    print("\n>> len(ticker_list)= ", len(ticker_list))

    if ticker_list==['']:
        return print('done')
    #%%

    # ticker_list=['DSGX','CDNA','CB','JXN','ETN','VRT']
    # ticker='DSGX'
    #%%

    #%%
    for ticker in ticker_list:
        try:
            driver=open_driver()
            '''
            pip install --upgrade undetected-chromedriver
            '''
            # How to upgrade the Chrome undetected driver PIP install


            # df2=mongo_get_df('screenshot','us_stock_max2_max1')

            # stock_list=df2['tradingview_link'].values.tolist()
            # stock_list

            # ticker='ZS'
            exchange=find_exchange(ticker)
            link=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange}%3A{ticker}'


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
                try:
                    button.click()
                except:
                    pass
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
            time.sleep(5)




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
            to_folder='data/image/seek_alpha_tradingview_v1'
            if not os.path.exists(to_folder): os.makedirs(to_folder)
            filename=f'{ticker}.png'
            fullpath_tradingview=os.path.join(to_folder,filename)
            driver.save_screenshot(fullpath_tradingview)

            # driver.save_screenshot(f'/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/{folder_name}/{i}_{ticker}.png')
            # print(i,ticker)



            time.sleep(10)
            driver.quit()
            time.sleep(5)


            # p2
            driver=open_driver()
            time.sleep(5)
            url1=f'https://seekingalpha.com/symbol/{ticker}/analysis'
            driver.get(url1)

            time.sleep(10)

            sections = driver.find_elements(By.TAG_NAME, 'section')
            sections

            section=sections[0]


            articles=section.find_elements(By.TAG_NAME,'article')
            # for item in articles:
                # print(item.text)

            # item.text


            # Initialize lists to store data
            h3_texts = []
            div_texts = []
            span_texts = []
            a_texts = []
            link_text=[]
            # Loop through each article and extract the desired data
            for article in articles:
                # Extract h3 text
                h3 = article.find_element(By.CSS_SELECTOR, 'h3')
                h3_texts.append(h3.text)
                link1 = article.find_element(By.CSS_SELECTOR, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('href')
                link1
                link_text.append(link1)

                # Extract div text
                div = article.find_elements(By.CSS_SELECTOR, 'div')[-1]
                div_texts.append(div.text)
                
                # Extract span text
                span = article.find_elements(By.CSS_SELECTOR, 'span')[-1]
                span_texts.append(span.text)
                
                # Extract a text
                a = article.find_elements(By.CSS_SELECTOR, 'a')[-1]
                a_texts.append(a.text)
                


            # Create a DataFrame
            df = pd.DataFrame({
                'title': h3_texts,
                'direction': div_texts,
                'date': span_texts,
                'comment': a_texts,
                'link':link_text
            })
            df


            # Convert 'date' column to datetime format
            # current_year = datetime.now().year
            # date_obj

            # First attempt with the first format
            for i in range(len(df)):
                date=df['date'][i]
                comment=df['comment'][i]
                date1=0
                try:
                    try:
                        if '.' in date:
                            date1=pd.to_datetime(date, format='%a, %b. %d').replace(year=datetime.now().year)
                        else:
                            date1=pd.to_datetime(date, format='%a, %b %d').replace(year=datetime.now().year)
                    except:
                        if '.' in date:
                            date1=pd.to_datetime(date, format='%a, %b. %d, %Y')
                        else:
                            date1=pd.to_datetime(date, format='%a, %b %d, %Y')
                except:
                    pass
                df.loc[i,'date']=date1
                if 'Comments' not in comment:
                    df.loc[i,'comment']=0
                # data=df['data'][i]
                # data=df['data'][i]
            df['comment'] = df['comment'].str.extract('(\d+)')
            df['comment'] = df['comment'].fillna(0).astype(int)
            df

            df1=df[:10]
            df1
            df1=df1.sort_values(by='comment',ascending=False)
            df1

            df1=reset_index(df1)
            df1
            try:
                do=mongo_get_df('seeking_alpha','analyst_report_v1')
                do_titles=do['title'].values.tolist()
            except:
                do_titles=[]
            
            iii=0
            for iii in range(len(df1)):
                # time.sleep(5)
                title=df1['title'][iii]
                if title in do_titles:
                    print('duplicate!!',ticker,iii)
                    continue
                driver.get(df1['link'][iii])

                time.sleep(30)
                sections = driver.find_elements(By.TAG_NAME, 'section')
                sections

                section=sections[0]
                text1=section.text

                text1=text1.split('This article was written by')[0]

                # print("\n>> len(text1)= ", len(text1))



                img_=[]
                for item in section.find_elements(By.TAG_NAME,'img'):
                    img_.append(item.get_attribute('src'))

                img_=img_[1:-1]
                img_



                text1

                title=section.find_element(By.TAG_NAME,'h1').text
                title


                dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
                dn

                csv_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
                dn=pd.DataFrame.from_dict(dict(ticker=ticker,title=title,text=text1,img=img_),orient='index').T
                mongo_update_insert_one('seeking_alpha','analyst_report_v1',dn,'title')
            driver.quit()
        except Exception as e:
            print('error...',ticker,e)