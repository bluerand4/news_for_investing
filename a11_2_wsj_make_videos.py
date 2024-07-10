#%%
import getpass,sys,socket
# add path for the libraryfrom import_basics import *
sys.path.pop(-1)
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import TextClip
from moviepy.video.tools.subtitles import SubtitlesClip

from youtube_data import *
from ai_moderator import *
from utils import *
from dataframe_stuff import *
from make_credentials import *
from spreadsheet import *

from pathlib import Path
from openai import OpenAI

def audio_download(name_prefix,input1):
    speech_file_path = f"data/audios/main_news/{name_prefix}.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=input1
    )

    response.stream_to_file(speech_file_path)
# %%
# f'https://www.google.com/search?q={search}&tbm=isch'
ii=0

def save_news_images(list1):
    
    search_list=[item for item in list1 if len(item)>10]
    search_list

    for ii in range(len(search_list)):
        time.sleep(1)
        print("ii: ",ii)
        search=search_list[ii]
        driver.get(f'https://www.bing.com/images/search?q={search}&form=HDRSC3')


        ming=driver.find_elements(By.XPATH,'//img[@class="mimg"]')
        ming

        ming

        # ming
        # imgs=driver.find_elements(By.TAG_NAME,'img')
        # imgs
        for iii,item in enumerate(ming[:5]):
            print("iii: ",iii)
            content=item.get_attribute('src')
            content

            # image_url = 'https://example.com/image.jpg'

            # Send an HTTP GET request to the image URL
            response = requests.get(content)

            folder_name='data/news_images'
            name=search[:20]+f" {iii}"
            local_file_path = f'{folder_name}/{name}.png'

            # Check if the request was successful (HTTP status code 200)
            if response.status_code == 200:
                # Get the content of the response (the image data)
                image_data = response.content
                
                # Specify the local file path where you want to save the image
                # local_file_path = 'data/temp.jpg'
                
                # Open a local file in binary write mode and write the image data to it
                with open(local_file_path, 'wb') as file:
                    file.write(image_data)

    for ii in range(len(search_list)):
        # time.sleep(1)
        search=search_list[ii]
        name_prefix=search[:20]
        audio_download(name_prefix,search)
        print(ii)
    return search_list


# data:image/jpeg;base64,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

# with open(local_file_path, 'wb') as file:
#     #identify image to be captured
#     #write file
#     file.write(content.screenshot_as_png)
#     print(f"Image downloaded and saved to {local_file_path}")

import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Directory containing the images and audio file



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
    
    
        

def remove_files(folder1):
    for file in os.listdir(folder1):
        file_path = os.path.join(folder1, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")

def make_final_video(search_list,name):
    # video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Add the file paths of your video files
    video_files=os.listdir('data/youtube1')
    video_files=['data/youtube1/'+item for item in video_files]
    video_files


    new_list=[]
    for item in search_list:
        for video3 in video_files:
            item=item[:20]
            if item in video3:
                new_list.append(video3)
                print('good!')
    
    video_clips=[]
    for file in new_list:
        video_clips.append(VideoFileClip(file).resize(newsize=(1920, 1080)) )
    video_clips

    # video_clips = [VideoFileClip(file).resize(newsize=(1920, 1080)) for file in video_files]
    # video_clips

    # from moviepy.editor import VideoFileClip, VideoFileClipList
    # final_video = VideoFileClipList(video_clips).concatenate()
    final_video = concatenate_videoclips(video_clips)


    import moviepy.editor as mpe
    # final_video = mpe.concatenate(video_clips)

    # Write the concatenated video to a file
    # concat_clip.write_videofile("concatenated_video.mp4")

    final_video.write_videofile(f"data/youtube3/{name}.mp4", codec="libx264", fps=30)
    # video_clip.write_videofile(output_video_file, codec="libx264", fps=30)
    for clip in video_clips:
        clip.close()
    final_video.close()

    # video_audio(wjslist)
    # Iterate through the files and remove them
    
    # remove_files('data/youtube1')
    # remove_files('data/youtube1')
    # remove_files('data/audios')
    # remove_files('data/news_images')

def youtube_upload(video_title,description):
    youtuber = YoutuberDummyParameters()


    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)   


    
    timedelta1=0
    timedelta2=100
    today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
    today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
    past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
    past2=datetime.strptime('20210218', "%Y%m%d").timestamp()


    title= f'{today1}_{video_title}_news'
    file_name='data/youtube3/final.mp4'
    request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
        "categoryId": '22',
        "description": description,
        "title": title,
        "tags": 'news'
        },
        "status": {
        "privacyStatus": 'public'
        }
    },
    
    # TODO: For this request to work, you must replace "YOUR_FILE"
    # with a pointer to the actual file you are uploading.
    media_body=googleapiclient.http.MediaFileUpload(file_name,chunksize=-1, resumable=True)
    )


    # output= AuxMakeYoutubeRequest(request)


    request.next_chunk()


from PIL import Image, ImageDraw, ImageFont
def make_text_image(text,filepath):
    width = 400  # Adjust the width of the image
    height = 400  # Adjust the height of the image
    background_color = (255, 255, 255)  # RGB color (white in this example)

    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype("path_to_font_file.ttf", font_size)  # Replace with your font file path
    # OR
    font = ImageFont.load_default()  # Use a default font
    # text = "Hello, World!"  # Replace with your desired text
    text_color = (0, 0, 0)  # RGB color (black in this example)
    text_position = (50, 50)  # (x, y) coordinates of the text
    draw.text(text_position, text, fill=text_color, font=font)
    image.save(filepath)  # Specify the desired image format (e.g., PNG, JPEG)
    image.close()
import openai
from moviepy.editor import VideoFileClip, ImageSequenceClip
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key


from twilio.rest import Client
import yagmail
from datetime import datetime,timedelta
import pandas as pd
# Your Account SID from twilio.com/console
account_sid = "{account_sid_twilio}"
auth_token  = "{auth_token_twilio}"
client = Client(account_sid, auth_token)
sender='{id_yagmail}'
#receiver='bluerand3@gmail.com'
email1=sender
passw1='{password_yagmail}'
passw1='{password_yagmail}'
yag = yagmail.SMTP(user=sender,password=passw1)
content1='1'
subject1='1'
def send_email(to_email,title,content):
    yag.send(to=to_email,subject=title,contents=content)


import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key



import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key

from openai import OpenAI
client = OpenAI()

def gpt_answer(content,define):
    try:

        message_list3=[{"role": "system", "content" : define},
                    {"role": "user", "content" : str(content)},    
                    ]
        completion = client.chat.completions.create(model="gpt-3.5-turbo" , #"gpt-3.5-turbo", 
                    messages = message_list3)
        completion=completion.choices[0].message.content

    except Exception as e:
        completion='>> error = time out for gpt...'+str(e)
    return completion
# define='summarize based on why the stock is going up.'
# summary=gpt_answer(content,define)
# summary


def find_repeated_substrings(word_list, min_length=2, min_repeats=3):
    substring_counts = Counter()

    # Iterate over each word
    for word in word_list:
        length = len(word)
        # Generate substrings for each word
        for start in range(length):
            for end in range(start + min_length, length + 1):
                substring = word[start:end]
                substring_counts[substring] += 1

    # Filter based on minimum repeats
    return {sub: count for sub, count in substring_counts.items() if count >= min_repeats}

# Sample list of words
# words = ['이미스머리띠', '샤넬머리띠', '티아라', '명품머리띠', '산리오머리띠', '벨벳머리띠', '고양이머리띠', '왕관', '밴드', '눈']

# Find repeated substrings
# repeated_substrs = find_repeated_substrings(keyword_list, min_length=2, min_repeats=3)
# repeated_substrs

def find_longest_repeated_substrings(word_list, min_length=2, min_repeats=3):
    substring_counts = Counter()

    # Iterate over each word
    for word in word_list:
        length = len(word)
        # Generate substrings for each word
        for start in range(length):
            for end in range(start + min_length, length + 1):
                substring = word[start:end]
                substring_counts[substring] += 1

    # Filter and find the longest repeated substring
    repeated_substrs = {sub: count for sub, count in substring_counts.items() if count >= min_repeats}
    longest_substring = max(repeated_substrs, key=lambda x: (repeated_substrs[x], len(x)), default=None)

    return longest_substring

from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pickle
import time 
import pandas as pd
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import requests
import os
import re
from collections import Counter
# Create download folder if not exist
# Specify the folder name you want to create
folder_name = "taobao_download"
# Check if the folder already exists, and if not, create it
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")
else:
    print(f"Folder '{folder_name}' already exists.")

# Open web browse
def open_driver():
    options = uc.ChromeOptions()
    # Creates a new instance of the ChromeOptions class to configure various options for the Chrome web browser.
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    # we are setting the profile.default_content_setting_values.notifications preference to 2. This will disable all notifications in the Chrome web browser.
    options.add_experimental_option("prefs",prefs)
    # # Adds the preferences that we created in the previous line to the ChromeOptions instance.
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")  # fatal
    options.add_argument('--no-sandbox')
    options.headless = False
    # Add a Random User Agent
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument("user-agent=%s" % user_agent) 
    # Option to set the user data directory, you should add your user data path
    # options.add_argument(r'--user-data-dir=C:\Users\Ahmed Farid\AppData\Local\Google\Chrome\User Data\Profile 1')
    
    options.add_argument(f'--user-data-dir=/Users/{getpass.getuser()}/Library/Application Support/Google/Chrome/Default')
    # This will disable the sandbox for the Chrome web browser. This may be necessary if you are running the Chrome web browser on a remote machine.
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # Creates a new instance of the Chrome web browser using the ChromeDriverManager class and the options instance that we created earlier.
    driver.maximize_window()
    # Maximizes the window for the Chrome web browser.
    print('Driver opened correctly!')
    # Prints a message to the console indicating that the Chrome web browser was opened successfully.
    return driver
# Open driver


import re

def scroll_down(driver, num_scrolling):
    # Finds the body element of the web page.
    body = driver.find_element(By.TAG_NAME, 'body')
    # Iterates over the `num_scrolling` argument and scrolls down the page by one page each time.
    for i in range(num_scrolling):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
    return
def extract_number(text):
    
    match = re.search(r'\((\d+)\)', text)
    if match:
        return int(match.group(1))
    else:
        return int(0)
    


from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,re
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


#%%
# driver.quit()
#%%

driver=open_driver()
# %%
url='https://www.biospace.com/news/'
response=requests.get(url)
response
driver.get(url)
# # %%
# time.sleep(10)
# #%%
# xbutton=driver.find_elements(By.XPATH,'//div[@id="interactive-close-button"]')
# xbutton=driver.find_element(By.XPATH,'//div[@class="button-container"]')
# xbutton
# #%%
# for item in xbutton:
#     try:
#         item.click()
#     except Exception as e:
#         print( 0 ,' = >>> some error = ',e)
    
#     time.sleep(1)


#%%
list2=[]
ulist1=driver.find_elements(By.XPATH,'//li[@class="cf block lister__item lister__item--article"]')
for item in ulist1[0:10]:
    list2.append(item.text)
    print("item.text: ",item.text)
#%%
list2
#%%
list1=[]
for item in list2:
    define='summarize with this format. [company name] has a good(or bad) news. Their drug [drug_name] is... \n However, if no specific company name is present, just summarize. explain medical terms.'
    print('start ')
    summary=gpt_answer(item,define)
    list1.append(summary)
    list1.append('\n\n')
    print('summary: ',summary)
timedelta1=0
timedelta2=100
today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
past2=datetime.strptime('20210218', "%Y%m%d").timestamp()
#%%
send_email('{id_yagmail}',f'biospace news {today1}',' '.join([item for item in list1]))
# %%

driver.get('https://www.wsj.com/')
# time.sleep(5)
try:
    headline=driver.find_element(By.XPATH,'//div[@layout="MEDIUM-TOPPER-SUMMARY"]')
    headline1=headline.text
    print("headline1: ",headline1)
except:
    headline=' '
    headline1=headline

try:
    semimain=driver.find_element(By.XPATH,'//div[@class="style--column--1p190TxH style--column-top--3Nm75EtS style--column-8--2_beVGlu style--border-left--1FbHaAV_ "]')
    


    columns=driver.find_element(By.XPATH,'//div[@class="style--column--1p190TxH style--column-top--3Nm75EtS style--column-4--2Ng-GQLy "]')
    

    submain=semimain.text+"\n Next news: "+columns.text
    print("submain: ",submain)
except:
    print('here')
    ulist3=driver.find_element(By.XPATH,'//div[@layout="LS-VISUAL-ELEVEN"]')
    submain=ulist3.text
    print("submain: ",submain)
#%%
define='with each point bulletpointed, summarize with this format. "[subject] has a good(or bad) news. Their [product/service] is...". However, if no specific subject like company, person, country is present, just summarize.'
news="Headline today:"+headline1+"\n\n"+"Next news: "+submain
print("news: ",news)
summary1=gpt_answer(news,define)
print("summary1: ",summary1)
#%%

#%%

bullet=gpt_answer(summary1,'number each point into bullet points with short titles')

# wjslist=bullet.split('\n')
#%%
wjslist=summary1.split('\n')
wjslist
#%%
wjslist=[item.replace('-','').replace('\n','') for item in wjslist]
wjslist=[item for item in wjslist if len(item)>2]
wjslist
#%%


driver.get('https://www.wsj.com/economy?mod=nav_top_section')

economy_para=driver.find_element(By.XPATH,'//div[@class="css-11vqdys"]').text
economy_para
#%%
define='with each point bulletpointed, summarize with this format. "[subject] has a good(or bad) news. Their [product/service] is...". However, if no specific subject like company, person, country is present, just summarize.'
economy_summary=gpt_answer(economy_para,define)

#%%
driver.get('https://www.wsj.com/finance?mod=nav_top_section')

finance_para=driver.find_element(By.XPATH,'//div[@class="css-11vqdys"]').text
finance_para
define='with each point bulletpointed, summarize with this format. "[subject] has a good(or bad) news. Their [product/service] is...". However, if no specific subject like company, person, country is present, just summarize.'
finance_summary=gpt_answer(finance_para,define)
finance_summary
#%%

send_email('{id_yagmail}',f'wsj news {today1}',summary1)
# %%


economy_list=[item for item in economy_summary.split('\n') if len(item)>10]
economy_list
#%%
finance_list=[item for item in finance_summary.split('\n') if len(item)>10]
finance_list

# driver.quit()
# driver=open_driver()
# %%
# summary1.split('\n')


#%%
wjslist

#%% #################################

client = OpenAI()
audio_folder='data/audios/main_news/'
image_folder='data/news_images/'
#%%
# def video_audio(search_list):
search_list=save_news_images(wjslist)
make_inter_videos(search_list)
make_final_video(search_list,'wsj1')
# description='news'
# video_title='others'
# # youtube_upload(video_title,description)

#%%

search_list=save_news_images(economy_list)
make_inter_videos(search_list)
make_final_video(search_list,'wsj2')

search_list=save_news_images(finance_list)
make_inter_videos(search_list)
make_final_video(search_list,'wsj3')


#%%
bio_list=[item for item in list1 if len(item)>5]
search_list=save_news_images(bio_list)

image_folder='data/news_images/'
make_inter_videos(search_list)
print('done 1')

make_final_video(search_list,'bio1')
# description='news'
# video_title='bio'
# print('done 2')
# youtube_upload(video_title,description)
#%%
list1=os.listdir('data/youtube3')
list1=sorted(list1)
list1=[item for item in list1 if item.endswith('.mp4')]
list1
# %%
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_clips=[]
for item in list1:
    video_clip=VideoFileClip(f'data/youtube3/{item}')
    video_clips.append(video_clip)
timestamp1=str(int(datetime.now().timestamp()))
video_clip = concatenate_videoclips(video_clips, method="compose")
video_clip.write_videofile(f'data/youtube2/main_news_{timestamp1}.mp4', fps=1)

#%%



#%%
to_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/news_video/'
from_folder='data/youtube2/'
filepath=os.listdir(from_folder)
filepath
#%%
for item in filepath:


    import shutil

    # from_folder='/Volumes/A1/2_ibkr/19_data_collection/7_dz/1_sql_cleanup/2_y/'
    # to_folder='/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/9 practicce/feature1/7_dz/1_sql_cleanup/2_y/'

    shutil.copy(from_folder+item, to_folder+item)
    print("item: ",item)
#%%
# driver.get('https://www.youtube.com/channel/UCnZe7kuOZqQLCkEnoMEnjow')
# driver.find_element(By.XPATH,'//button[@aria-label="Create"]').click()
# #%%
# driver.find_element(By.XPATH,'//div[@id="primary-text-container"]').click()


# #%%
# driver.find_element(By.XPATH,'//ytcp-button[@id="select-files-button"]').click()
# #%%
# import pyautogui as pt

# with pt.hold(['command','shift']):
#     time.sleep(0.2)
#     pt.press('g')
#     time.sleep(0.1)

#%%
#%%
driver.quit()
#%%
def remove_files(folder1):
    for file in os.listdir(folder1):
        file_path = os.path.join(folder1, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {str(e)}")
remove_files('data/youtube1')
remove_files('data/youtube3')
remove_files('data/news_images')

# %%
