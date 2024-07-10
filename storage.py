
def check_20_assets_sma200_above():

    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    dw

    de=total.read_excel(f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/list_of_assets.xlsx')
    de=total.reset_index(de)
    de


    fullname_list=[]
    webname_list=[]
    for i in range(len(de)):
        webname=str(de['web_name'][i])
        if 'symbol' in webname:
            webname=webname.split('=')[1]
            ticker2=webname.split("%")
            part2=ticker2[1].replace("3A","")
            if len(ticker2)>2:
                
                fullname=ticker2[0]+":"+part2+"!"
            else:
                fullname=ticker2[0]+":"+part2
            fullname
            webname_list.append(webname)
            fullname_list.append(fullname)
            print(fullname)
            print(' ')


    list5=[]
    minute1='1D'
    for fullname in fullname_list:
        try:
            df=tradingview1(fullname,minute1)
            df
            while True:

                tot=len(df)-1
                print(fullname,'  ',df['Date'][tot])

                date2=df['Date'][tot]
                date2

                if 'nan' in str(date2).lower() or 'nat' in str(date2).lower():
                    print('drop last row')
                    df = df.iloc[:-1 , :]
                else:
                    break


        
            link_symbol=fullname.replace(":","%3A").replace("!","%21")
            link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
            link_symbol
        
            
            tot=len(df)-1
            print(fullname,'  ',df['Date'][tot])
            print(' ')
            for i in range(10):
                close1=df['Close'][tot-i]
                sma200=df['SMA200'][tot-i]
                close1_2=df['Close'][tot-i-1]
                sma200_2=df['SMA200'][tot-i-1]
                date1=df['Date'][tot-i]
                if close1>sma200:
                    if close1_2<sma200_2:
                        print(i)
                        print(date1)
                        print('close > sma200')
                        list5.append((fullname,date1,close1,sma200,'above',f'{fullname}_{date1}'))
                if close1<sma200:
                    if close1_2>sma200_2:
                        print(' ============')
                        print(i)
                        print(df['Date'][tot-i])
                        print('close < sma200')
                        list5.append((fullname,date1,close1,sma200,'below',f'{fullname}_{date1}'))
                        print(' ----')  
        except Exception as e:
            print(e)
            send_email(sender,f'error - {fullname}',f'{fullname},{e}')



    if len(list5)>0:
    
        dw2=pd.DataFrame(list5)
        dw2.columns=['fullname','date','close','sma200','direction','fullname_date']
        dw2

        dw3=dw2[~dw2['fullname_date'].isin(dw['fullname_date'])]
        dw3=total.reset_index(dw3)
        dw3
        if len(dw3)>0:
        
            for i in range(len(dw3)):
                above1=str(dw3['direction'][i])
                
                fullname=str(dw3['fullname'][i])
                date1=str(dw3['date'][i])
                close1=str(dw3['close'][i])
                sma200=str(dw3['sma200'][i])
                fullname_date=str(dw3['fullname_date'][i])
                ticker=fullname.split(':')[1].replace("1!","")
                link_symbol=fullname.replace(":","%3A").replace("!","%21")
                link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'
                
                if 'above' in above1:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
                else:
                    print('start - send email... ',i)
                    send_email(email1,title=f't: {ticker} is {above1} SMA200. {fullname_date}',content=f'{fullname}  .\n 2. close = {close1} \n 3. sma200= {sma200}   \n 4. {link1}    \n 5. {date1}   \n 6.    ')
                    print('success ')
                    print(' ')
    
        print('start = saving dw to csv')
        dw=pd.concat((dw,dw2),axis=0)
        dw=dw.drop_duplicates(keep="last",subset='fullname_date')
        dw=total.reset_index(dw)
        
        dw.to_csv(alarm1)
        dw
        print('success = saving dw to csv')

def seven_days_alarm():
    print('seven days - alarm check')
    alarm1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/1_total_data/1 US stocks/8_tradingview/20_assets_sma200_alarm.csv'
    dw=total.read_csv(alarm1)
    dw=total.reset_index(dw)
    
    for item in list(set(dw['fullname'].values)):


        string1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['date'][-1:].values[0]
        above1=dw[dw['fullname']==item].sort_values(by='date').reset_index()['direction'][-1:].values[0]
        fullname=item
        datetime1=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=7)
        link_symbol=fullname.replace(":","%3A").replace("!","%21")
        link1=f'https://www.tradingview.com/chart/tMeJexox/?symbol={link_symbol}'

        days_7=datetime.strftime(datetime1 ,"%Y-%m-%d")
        

        today1=(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d"))
        if today1==days_7:
            send_email(email1,title=f't2: {item} has been 7 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 7 days passed..')

        datetime2=datetime.strptime(string1, "%Y-%m-%d %H:%M:%S")+timedelta(days=14)
        days_14=datetime.strftime(datetime2 ,"%Y-%m-%d")
        if today1==days_14:
            send_email(email1,title=f't3: {item} has been 14 days {above1} SMA200.',content=f'{item}    \n 4. {link1}     \n 6.    ')
            print(item,' - 14 days passed..')



def futures_expiration_email():
    day1=3
    path1=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/2 import data/IBKR/2 futures expiration definition/win2_IBKR_Futures2.csv'
    da=total.read_csv(path1)
    da=total.reset_index(da)
    da
    for i in range(len(da)):
        expiry1=str(da['expiry'][i])
        symbol=da['symbol'][i]
        sectype=da['sectype'][i]
        exch=da['exch'][i]
        local=da['local'][i]
        all1=str(da.iloc[i])
        date1=datetime.strptime(expiry1, "%Y%m%d")
        date2=date1-timedelta(days=day1)

        date2=datetime.strftime(date2 ,"%Y-%m-%d")
        date2
        timedelta1=0
        timedelta2=100
        today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
        today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
        past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
        past2=datetime.strptime('20210218', "%Y%m%d").timestamp()

        if today1==date2:
            print(i,symbol,sectype,expiry1,exch,local)
            send_email(email1,title=f'futures expiration: {symbol} will be expired in {day1} days.',content=f'{symbol}_{sectype}_{expiry1}_{exch}_{local}')



def make_inter_videos(search_list):
    for ii in range(len(search_list))[0:]:
        try:
            search=search_list[ii]
            image_name_prefix=search[:20]


            image_name_prefix

            

            imagelist=os.listdir(image_folder)
            imagelist

            image_name_prefix

            imagelist=[image_folder+item for item in imagelist if image_name_prefix in item]
            imagelist

            image_files=imagelist
            if len(imagelist)==0:
                filepath=image_folder+image_name_prefix+'.png'
                make_text_image(search,filepath)
                imagelist=[filepath]


            # image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

            # Audio file name (change this to match your audio file)
            audio_file = f"{image_name_prefix}.mp3"
            audio_file

            # fps=24
            # Video output file name
            output_video_file = f"data/youtube1/{image_name_prefix}.mp4"

            audio_clip = AudioFileClip(audio_folder + audio_file)
            frame_rate = 1
            audio_duration = audio_clip.duration
            each_length=audio_duration/len(imagelist)
            image_duration = max(3,int(each_length))

            duration=image_duration
            image_clips = [ImageSequenceClip([img], durations=[duration]) for img in image_files]
            # from moviepy.editor import ImageSequenceClip, VideoFileClip, concatenate_videoclips
            # Concatenate the image clips to create the final video
            video_clip = concatenate_videoclips(image_clips, method="compose")
            video_clip = video_clip.set_duration(audio_duration).set_audio(audio_clip)
            # Write the final video to a file using H.264 codec
            # video_clip.write_videofile(output_video_file, codec="libx264")

            # Write the final video to a file
            # final_video.write_videofile("output_with_subtitles.mp4", codec="libx264", fps=video_clip.fps)
            video_clip.write_videofile(output_video_file.replace('-',''), codec="libx264", fps=frame_rate)  # Adjust the fps value as needed
            # Clean up
            video_clip.close()
            print("ii: ",ii)
        except Exception as e:
            print( 0 ,' = >>> some error = ',e)
    
        

def upload_subtitle(video_id,subtitle_fullpath):
    # Assume `service` is your authenticated YouTube API client
    # Assume `video_id` is the ID of the uploaded video
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   

    # Prepare the request body for the caption
    caption_body = {
        'snippet': {
            'videoId': video_id,
            'language': 'en',  # Language of the subtitles
            'name': 'English Subtitles',  # Name of the subtitle track
            'isDraft': False
        }
    }

    # Path to your subtitle file

    # Create the media file upload object
    media_body = MediaFileUpload(subtitle_fullpath, mimetype='text/plain', resumable=True)

    # Insert the captions
    caption_insert_request = youtube.captions().insert(
        part='snippet',
        body=caption_body,
        media_body=media_body
    )

    # Execute the request
    caption_response = caption_insert_request.execute()

    # Optionally, check the response for success
    print(caption_response)



def functional_enum2():

    messages = [{"role": "user", "content": productname_element}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "yes_or_no",
                "description": "do you think this name is name of a product?",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {
                            "type": "string",
                            "description": "return yes or no",
                        },
                        # "unit": {"type": "string", "enum": ["yes", "no"]},
                        "unit": {"type": "string"},
                    },
                    "required": ["search_term"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response

    response.choices[0].message


# %%

ds=ds.sort_values(by='fcf1',ascending=False)
ds[:20]
#%%
data=ds['net_income'][0]
data=ast.literal_eval(data)
data
#%%
ds_past=copy.deepcopy(ds)
# %%
ds_past

#%%
dd
# %%

ticker='AAPL'
print("ticker: ",ticker)
exchange=find_exchange(ticker)
driver.get(f'https://www.tradingview.com/chart/q0QCLsTJ/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located
# time.sleep(10)

# %%
#%%

for ticker in tickers[0:50]:
    
    print("ticker: ",ticker)
    exchange=find_exchange(ticker)
    driver.get(f'https://www.tradingview.com/chart/q0QCLsTJ/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located
    time.sleep(10)


    button=driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]')

    if 'dropped' in button.find_element(By.TAG_NAME,'span').get_attribute('class'):
        print('down now')
    else:
        button.click()
        print('up now')
    time.sleep(1)
    titles=driver.find_elements(By.XPATH,'//span[@class="title-cXDWtdxq itemTitle-KSzJG6_A"]')
    infos=driver.find_elements(By.XPATH,'//span[@class="data-cXDWtdxq"]')

    dict1={}
    dict1['ticker']=ticker
    for title,item in zip(titles,infos):
        title=title.text
        item=item.text
        if item.endswith('B'):
            item=item.replace('B','')
            item=float(item)
            item=item*1000000
        elif item.endswith('M'):
            item=item.replace('M','')
            item=float(item)
            item=item*1000
        elif item.endswith('T'):
            item=item.replace('T','')
            item=float(item)
            item=item*1000000000
        elif item.endswith('K'):
            item=item.replace('K','')
            item=float(item)
            
        elif item.endswith('%'):
            item=item.replace('%','')
            item=float(item)
        
        else:
            try:
                item=float(item)
            except:
                item=float(0)
        dict1[title]=item
        
        print("item: ",title,item)
    dict1




    dd=pd.DataFrame.from_dict(dict1,orient='index').T
    dd

    mongo_update_insert_one('stock','tradingview_slope',dd,'ticker',UPSERT=True,IGNORE=False)

# %%
    

# %%

#%%
def max200_email():
    # stock_list=common_stock_list_v1_5000_polygon_real_time()
    print("max200 started")
    # stock_list=stock_list_11000()
    stock_list=stock_list_5000()
    stock_list

    ticker_=[]
    content_=[]

    limit1=2000
    minute1='1'
    beta2=0
    past1=datetime.strftime(datetime.now()-timedelta(2000) ,"%Y-%m-%d")
    today1=datetime.strftime(datetime.now()-timedelta(beta2) ,"%Y-%m-%d")
    print(past1,today1)

    ticker='AAPL'
    for ii,ticker in enumerate(stock_list):
        try:
            print("ticker: ",ticker,ii)
            # for ticker in polygon_list:
            df=prepared_df(ticker,minute1,limit1,past1,today1)

            if df['Close'][len(df)-1]>df['MAX200'][len(df)-2]:
                print('yes max200 crossed',ticker,ii)
                content_.append('\n')
                # content_.append(ticker)
                MC,industry, description,company_name,PE_ratio = get_stock_details(ticker)
                
                description_summary=gpt_answer("summarize what they do? why customers buying from them? why their products are better than other competitors?",description)
                content_.append('_____________________________________________________')
                content_.append(f'{ticker} \nMC: ${MC}B / \nPE: {round(PE_ratio,3)} / \nindustry:{industry} / \n>description: {description} \n>summary: {description_summary}')
                company_name= generate_company_name(ticker)
                news=fetch_news_for_query(newsapi_org, query=f'{company_name}',page_size=10)
                # news=fetch_news_for_query(newsapi_org, query=f'{ticker} stock',page_size=10)
                news=str(news)
                define=f'summarize based on why the {company_name} stock is going up.'
                news=gpt_answer(define,news)
                try:
                    exchange1=find_exchange(ticker)
                    
                    ticker_.append(ticker)
                    
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'

                    content_.append(content)
                    content_.append(news)
                except:
                    ticker_.append(ticker)
                    exchange1='NASDAQ'
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'            
                    content_.append(content)
                    content_.append(news)
                    exchange1='NYSE'
                    content=f'https://www.tradingview.com/chart/tMeJexox/?symbol={exchange1}%3A{ticker}'
                    content_.append(content)
        except Exception as e:
            print('error : ',ticker,e)
    content_


    # Your Account SID from twilio.com/console
    account_sid = "{account_sid_twilio}"
    # Your Auth Token from twilio.com/console
    auth_token  = "{auth_token_twilio}"

    client = Client(account_sid, auth_token)

    sender='{id_yagmail}'
    #receiver='bluerand3@gmail.com'
    receiver=sender
    passw1='{password_yagmail}'
    passw1='{password_yagmail}'

    yag = yagmail.SMTP(user=sender,password=passw1)

    content__=" \n ".join(content_)
    content__

    ticker__=" ".join(ticker_)
    ticker__
    subject_=f'MAX200_{ticker__}'
    yag.send(to=sender,subject=subject_,contents=content__)
    
    print('end - send email... v1')



#%%
from import_all import *

# %%

mongo_collection_names('stock')
#%%
dp=mongo_get_df('stock','polygon_stocks')
dp
#%%

#%%
df=mongo_get_df('stock','comparison')
df
# %%
df=df.sort_values(by='revslope',ascending=False)
df[:20]
# %%
df
#%%
df2 = df[df['inslope'] >= 15]
df2 = df2[df2['inslope2'] >= 15]
df2 = df2[df2['revslope'] >= 15]
df2 = df2[df2['revslope2'] >= 15]
df2

#%%

df2 = df2[df2['inslope'] <= 499]
df2 = df2[df2['inslope2'] <= 499]
df2 = df2[df2['revslope'] <= 499]
df2 = df2[df2['revslope2'] <= 499]
df2
# %%
df2
# %%
tradingview_slope=mongo_get_df('stock','tradingview_slope')
tradingview_slope
#%%

#%%
PER="Price to earnings Ratio (TTM)"
DIV='Dividend yield (indicated)'
tradingview_slope[PER]


df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2 = df2[df2['revenue1'] >= 0]
df2 = df2[df2['revenue2'] >= 0]
df2 = df2[df2['net_income1'] >= 0]
df2 = df2[df2['net_income2'] >= 0]
df2 = df2[df2['fcf1'] >= 0]
df2 = df2[df2['fcf2,'] >= 0]
df2=df2.sort_values(by=PER,ascending=True)
df3=df2[:50][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
df3
#%%

list2=df3['ticker'][0:20].values.tolist()
','.join(list2)
#%%

'ESEA,PSHG,TNK,GSL,TRMD,CVI,PETZ,DINO,GM,CEIX,SDRL,GECC,MHUA,FCAP,MVO,OI,BSVN,SLVM,WLFC,BOSC,HE,RWAY,BVFL'

#%%
df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2 = df2[df2['revenue1'] >= 15]
df2 = df2[df2['revenue2'] >= 15]
df2 = df2[df2['net_income1'] >= 15]
df2 = df2[df2['net_income2'] >= 15]
df2 = df2[df2['fcf1'] >= 15]
df2 = df2[df2['fcf2,'] >= 15]
df2 = df2[df2['revenue1'] <= 499]
df2 = df2[df2['revenue2'] <= 499]
df2 = df2[df2['net_income1'] <= 499]
df2 = df2[df2['net_income2'] <= 499]
df2 = df2[df2['fcf1'] <= 499]
df2 = df2[df2['fcf2,'] <= 499]

df2=df2.sort_values(by='fcf2,',ascending=False)
df2
#%%
df3=df2[:50][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
df3=reset_index(df3)
df3
df3['how_many_days']=1000
#%%
ticker='LTHM'
import requests,json
url=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
response=requests.get(url)

json1=response.json()
json1
#%%
stock_name=json1['results']

exchange1=stock_name['primary_exchange']
exchange1
#%%
find_exchange_v2(ticker)
#%%

#%%

ticker='CPNG'
#%%
for i in range(len(df3))[20:]:
    ticker=df3['ticker'][i]
    try:
        days=how_many_days_ago_max_above(ticker)
    except:
        days=3000
    df3.loc[i,'how_many_days']=days
    print("ticker: ",ticker,days)
#%%

#%%
df3
df3=df3.sort_values(by='how_many_days',ascending=True)
df3
#%%
df.columns
#%%
df_2=df[['ticker','industry','sector']]
df4=df3.merge(df_2,how='outer',on='ticker')[:50]
df4
#%%
df4[df4['sector']=='Technology']
# %%

list2=df2[df2['ticker']=='EPRT']['fcf'].values[0]
list2=ast.literal_eval(list2)
list2
# %%
list3=list2[-8:]
# %%
import matplotlib.pyplot as plt

plt.plot(list3)
plt.show()
# %%

def regression(numbers,normalize=False):
    if normalize:
        # numbers = remove_outliers(numbers,85,5)
        min1=min(numbers)
        max1=max(numbers)
        numbers=[(item -min1)/(max1-min1) for item in numbers]
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


def remove_outliers(data,THRESHOLD=25,THRESHOLD2=1.5):
    q1 = np.percentile(data, int(THRESHOLD))
    q3 = np.percentile(data, int(100-THRESHOLD))
    iqr = q3 - q1

    lower_bound = q1 - THRESHOLD2 * iqr
    upper_bound = q3 + THRESHOLD2 * iqr

    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data

slope1,_=regression(list3,normalize=True)
print("slope1: ",slope1)
# %%



actors[index1]
# %%

# %%
print("\n>> len(summary)= ", len(summary))

# %%
# import torch
# from TTS.api import TTS

# # Get device
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # List available 🐸TTS models
# print(TTS().list_models())

# # Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# # Run TTS
# # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# # Text to speech list of amplitude values as output
# wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
# # Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
# #%%
# import torch
# from TTS.api import TTS

# # Get device
# device = "cuda" if torch.cuda.is_available() else "cpu"
# device
# #%%
# print(TTS().list_models())
# #%%
# # Initialize the TTS model

# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)

# #%%
# tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False).to(device)

# #%%
# # Define the text you want to convert to speech
# text = summary[:500]

# # Convert text to speech and save it to a file
# tts.tts_to_file(text=text, file_path="data/output.wav")

# print("Speech synthesis completed. The audio has been saved to 'output.wav'.")

# # %%
