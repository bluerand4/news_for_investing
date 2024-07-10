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
# %%
# from import_major import *


def youtube_seek_alpha_v1():
    #%%
    dq=mongo_get_df('news','additional_stocks')

    dq
    #%%
    ticker_list=dq['tickers'][0]
    ticker_list=ticker_list.split(',')
    ticker_list
    print(ticker_list)

    if ticker_list==['']:
        return print('done')

    #%%
    for ticker in ticker_list:
        try:
            driver=open_driver()
            '''
            pip install --upgrade undetected-chromedriver
            '''
            # How to upgrade the Chrome undetected driver PIP install
            #%%
            # df2=mongo_get_df('screenshot','us_stock_max2_max1')
            #%%
            # stock_list=df2['tradingview_link'].values.tolist()
            # stock_list

            # ticker='ZS'
            exchange=find_exchange(ticker)
            link=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange}%3A{ticker}'
            #%%

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
            to_folder='data/image/seek_alpha_tradingview_v1'
            if not os.path.exists(to_folder): os.makedirs(to_folder)
            filename=f'{ticker}.png'
            fullpath_tradingview=os.path.join(to_folder,filename)
            driver.save_screenshot(fullpath_tradingview)

            # driver.save_screenshot(f'/Users/mac1/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/9_daily/{folder_name}/{i}_{ticker}.png')
            # print(i,ticker)

            # %%

            time.sleep(10)
            driver.quit()
            time.sleep(5)
            driver=open_driver()
            time.sleep(5)
            url1=f'https://seekingalpha.com/symbol/{ticker}/analysis'
            driver.get(url1)
            #%%
            time.sleep(10)
            sections = driver.find_elements(By.TAG_NAME, 'section')
            sections
            # %%
            section=sections[0]

            #%%
            articles=section.find_elements(By.TAG_NAME,'article')
            # for item in articles:
                # print(item.text)
            # %%
            # item.text
            # %%

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
                

            #%%
            # Create a DataFrame
            df = pd.DataFrame({
                'title': h3_texts,
                'direction': div_texts,
                'date': span_texts,
                'comment': a_texts,
                'link':link_text
            })
            df
            # %%

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
            # %%
            df1=df[:10]
            df1
            df1=df1.sort_values(by='comment',ascending=False)
            df1
            # %%
            time.sleep(5)
            driver.get(df1['link'][0])
            # %%
            time.sleep(10)
            sections = driver.find_elements(By.TAG_NAME, 'section')
            sections
            # %%
            section=sections[0]
            text1=section.text
            # %%
            text1=text1.split('This article was written by')[0]
            # %%
            print("\n>> len(text1)= ", len(text1))

            # %%


            def gpt_answer(content,define):
                try:

                    message_list3=[{"role": "system", "content" : define},
                                {"role": "user", "content" : str(content)},    
                                ]
                    completion = client.chat.completions.create(model="gpt-4o" , #"gpt-3.5-turbo", 
                                messages = message_list3)
                    completion=completion.choices[0].message.content

                except Exception as e:
                    completion='>> error = time out for gpt...'+str(e)
                return completion
            define='summarize in details.'
            summary=gpt_answer(text1,define)
            summary
            # %%
            print("\n>> len(summary)= ", len(summary))

            # %%

            # print(textwrap.fill(summary, width=70))
            # %%

            actors = {
                'man1': 'echo',
                # 'man2': 'fable',
                'man3': 'onyx',
                'woman1': 'alloy',
                'woman2': 'nova',
                'woman3': 'shimmer'
            }
            index1=random.randint(0,len(actors)-1)
            # index1=1
            #%%
            # speech_file_path = f"data/audios/{folder}/{name_prefix}.mp3"
            to_folder='data/audio/youtube_news_v1'
            if not os.path.exists(to_folder): os.makedirs(to_folder)
            
            filename=f'{ticker}_seek_alpha.mp3'
            fullpath=os.path.join(to_folder,filename)
            response = client.audio.speech.create(
            model="tts-1",
            voice=list(actors.values())[index1],
            input=summary[:]
            )

            response.stream_to_file(fullpath)
            # %%
            img_=[]
            for item in section.find_elements(By.TAG_NAME,'img'):
                img_.append(item.get_attribute('src'))
            # %%
            img_=img_[1:-1]
            # %%
            import moviepy.editor as mp
            import requests
            from PIL import Image
            from io import BytesIO

            # List of image URLs
            # img_ = [
            #     "https://example.com/image1.png",
            #     "https://example.com/image2.png",
            #     "https://example.com/image3.png",
            #     # Add more image URLs as needed
            # ]

            local_img = Image.open(fullpath_tradingview)
            if local_img.mode != 'RGB':
                local_img = local_img.convert('RGB')


            images = [local_img]
            for url in img_:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                images.append(img)

            frame_size = (1920, 1080)  # Example frame size, adjust as needed

            # Duration of the audio file
            # fullpath = "path/to/your/audio.mp3"
            audio = mp.AudioFileClip(fullpath)
            audio_duration = audio.duration

            # Calculate the duration each image should be displayed
            img_duration = audio_duration / len(images)

            # Create a list of video clips from the images
            image_clips = []
            for img in images:
                # Convert the PIL image to an ImageClip
                img = np.array(img)

                img_clip = mp.ImageClip(img)
                
                # Set the duration for each clip
                img_clip = img_clip.resize(newsize=frame_size)
                
                img_clip = img_clip.set_duration(img_duration)


                img_clip=img_clip.set_fps(24)
                image_clips.append(img_clip)

            # Concatenate all image clips into one video clip
            video = mp.concatenate_videoclips(image_clips, method="compose")

            # Set the audio of the video
            video = video.set_audio(audio)

            # Save the video to a file
            to_folder_video='data/video/seek_alpha_v1'
            if not os.path.exists(to_folder_video): os.makedirs(to_folder_video)
            output_file = f"{ticker}_{datetime.now().timestamp()}_video.mp4"
            fullpath_video=os.path.join(to_folder_video,output_file)
            #%%
            print('start - video')
            video.write_videofile(fullpath_video, codec="libx264", audio_codec="aac",fps=24)

            print(f"Video created successfully: {fullpath_video}")
            time.sleep(30)
            # %%
            type(images[0])
            # %%


            #%%
            driver.get('https://studio.youtube.com/channel/UCnZe7kuOZqQLCkEnoMEnjow')
            chrome_window_x = 5  # Example X coordinate
            chrome_window_y = 5  # Example Y coordinate
            time.sleep(5)
            # Move the mouse cursor to the Chrome window and click
            # pt.moveTo(chrome_window_x, chrome_window_y)
            # pt.click()


            driver.find_elements(By.XPATH,'//ytcp-button[@class="style-scope ytcp-header"]')[1].click()
            time.sleep(2)

            # //tp-yt-paper-item[@class="tp-yt-paper-item  selectable-item style-scope ytcp-text-menu style-scope ytcp-text-menu"]

            driver.find_element(By.XPATH,'//tp-yt-paper-item[@class="tp-yt-paper-item  selectable-item style-scope ytcp-text-menu style-scope ytcp-text-menu"]').click()
            time.sleep(2)

            driver.find_element(By.XPATH,'//ytcp-button[@id="select-files-button"]').click()
            time.sleep(2)
            time.sleep(3)

            with pt.hold(['command','shift']):
                time.sleep(0.2)
                pt.press('g')
                time.sleep(0.1)

            time.sleep(3)
            import pyperclip
            pyperclip.copy(os.path.join(os.getcwd(),fullpath_video))

            time.sleep(2)
            with pt.hold(['command']):
                time.sleep(0.2)
                pt.press('v')
                time.sleep(0.1)


            time.sleep(1)
            pt.press('enter')
            time.sleep(1)

            pt.press('enter')
            time.sleep(30)
            #%%
            time.sleep(3)
            final_title3=f'{ticker} _{datetime.now()} video'

            title=driver.find_element(By.XPATH,'//div[@class="style-scope ytcp-social-suggestions-textbox"]')
            title


            title=driver.find_elements(By.XPATH,'//ytcp-social-suggestion-input[@class="fill-height style-scope ytcp-social-suggestions-textbox"]')[0]
            title.click()
            title.text

            time.sleep(3)
            with pt.hold(['command']):
                time.sleep(0.2)
                pt.press('a')
                time.sleep(0.1)

            pyperclip.copy(final_title3)
            # title.send_keys(final_title3)
            with pt.hold(['command']):
                time.sleep(0.2)
                pt.press('v')
                time.sleep(0.1)

            time.sleep(1)

            pt.press('tab')
            time.sleep(1)

            pt.press('tab')


            description=f'''
            {ticker}_{datetime.now()}

            '''
            pyperclip.copy(description)
            # title.send_keys(final_title3)
            with pt.hold(['command']):
                time.sleep(0.2)
                pt.press('v')
                time.sleep(0.1)

            time.sleep(1)

            pt.press('tab')
            time.sleep(1)

            pt.press('tab')


            time.sleep(3)
            for item in driver.find_elements(By.XPATH,'//div[@class="style-scope tp-yt-paper-radio-button"]'):
                print(item.text)
                if '아동용이 아닙니다' in item.text or 'not made for kids' in item.text:
                    item.click()

            time.sleep(3)
            for item in driver.find_elements(By.XPATH,'//div[@class="label style-scope ytcp-button"]'):
                if '다음' in item.text or 'next' in item.text.lower() :
                    try:
                        print('''> try: item.click()''',datetime.now())
                        item.click()
                    except Exception as e:
                        print('''>> error: item.click(): ''',e,datetime.now())


            time.sleep(3)
            for item in driver.find_elements(By.XPATH,'//div[@class="label style-scope ytcp-button"]'):
                if '다음' in item.text or 'next' in item.text.lower() :
                    try:
                        print('''> try: item.click()''',datetime.now())
                        item.click()
                    except Exception as e:
                        print('''>> error: item.click(): ''',e,datetime.now())

            time.sleep(3)
            for item in driver.find_elements(By.XPATH,'//div[@class="label style-scope ytcp-button"]'):
                if '다음' in item.text or 'next' in item.text.lower() :
                    try:
                        print('''> try: item.click()''',datetime.now())
                        item.click()
                    except Exception as e:
                        print('''>> error: item.click(): ''',e,datetime.now())


            time.sleep(2)
            for item in driver.find_elements(By.XPATH,'//div[@class="style-scope tp-yt-paper-radio-button"]'):
                if '공개' in item.text and '비공개' not in item.text and '일부 공개' not in item.text:
                    print(item.text)
                    item.click()
                elif 'Public' in item.text and 'Private' not in item.text and 'Unlisted' not in item.text:
                    print(item.text)
                    item.click()

            time.sleep(2)
            for item in driver.find_elements(By.XPATH,'//div[@class="label style-scope ytcp-button"]'):
                if '게시' in item.text or 'PUBLISH' in item.text:
                    try:
                        print('''> try: item.click()''',datetime.now())
                        item.click()
                    except Exception as e:
                        print('''>> error: item.click(): ''',e,datetime.now())



            # youtube_link=driver.find_element(By.XPATH,'//a[@class="style-scope ytcp-video-share-dialog"]').text
            # youtube_link
            # %%


            time.sleep(30)
            driver.quit()


        except Exception as e:
            print('error -r ',ticker,e)
        # %%
    dn=pd.DataFrame(['','old']).T
    dn.columns=['tickers','status']
    dn
    mongo_set_df('news','additional_stocks','tickers',dn)

