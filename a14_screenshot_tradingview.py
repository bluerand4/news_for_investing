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
    speech_file_path = f"data/audios/{name_prefix}.mp3"
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
        search=search_list[ii]
        driver.get(f'https://www.bing.com/images/search?q={search}&form=HDRSC3')


        ming=driver.find_elements(By.XPATH,'//img[@class="mimg"]')
        ming

        ming

        # ming
        # imgs=driver.find_elements(By.TAG_NAME,'img')
        # imgs
        for iii,item in enumerate(ming[:5]):
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


# data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAGQAZAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQADBgIBB//EADgQAAIBAwMBBgQEBAYDAAAAAAECAwAEEQUSITEGEyJBUWEUcYGRMqGx0RVC4fBScsHC0vEjJDP/xAAaAQACAwEBAAAAAAAAAAAAAAABAgMEBQAG/8QAJREAAgIBAwQCAwEAAAAAAAAAAAECEQMEEiETMUFRIjJSYYEF/9oADAMBAAIRAxEAPwDTNVbEiu81w/SvTIzzgvioHJNVsa8BwaehbC8+GqJagk4qp5OeaCRzYPNQUvWmLYIpfOMH2qeBFIpUnPFWrmq04ar1UsadiI9TrRUOc1UseOtERrUcmSRQSORXldKpxxUqIkORJXu8GqWqovg9aNAsvk6ZFU7qneZGCa5JFGgNnYbFcSHJrwkVwzU1AbLM4WhLiiRIMYqiTxGjEWQOlFxY4oZ5YIRmWRV+tLb/ALQQWgKsyoR13Hn7VHl1OOHdkmPBOXZGiO0DJIA9Saol1a1t/CCXf0FY86zNqVrI9mHnlWdIVXpktnj8vWhP4Pr1+oSdu5WSMFUVS2STjoOB9TWZl17fEeC5HTxj9uTaRarcXS95E6ouSNoAOK8ofRbH+GafHbyGQtkse9A3cn2JxUqo88vyLKxxr6jVpc1S7igjcZ6EVw09ekUDFcwszYPWve/4pe0oPnXPf4p9om8Na4OanxChSXIA88ml7zg1kdV1C8aXUMOyxw8I3oSwH71X1OZYIp13JMMOq6s2N3rVrbIW37h69BSyTWrq5u/h7aCVyH2t3aeEeIA5J+dU9mLG3u9PtzfF5mkIAyM7j3hOCT7VpdKvYIEuLdNtu3idpHAKvlx4R78Hz8xWJm1uWbqzShghGqRm4dB13V0kmimSC23FRtPiIyAOp9x5+fT0ZW+gaK1zdXWsMxYuQgB4G0ovOTj19athe6ZII0lkIVU8CDGCO7z9fCR19KZQ6BqF5I0sNhIQWYiR0I6kHqflVNzZPsk0C2kllatBLaIWiguXJGBt8IfkeXlmqrztNeXluyIGlPwjKqrlyOvPAwOvrWhteyd5Kkjztbwq7lmLOOpznpn1NXfwbR7J40vNat8f4EI8P5/6UrkvI+xexNaSPdRGS7UCTcRhuOPlmpT1peyMR2fF3Jx5qrY/JalL1EOkj4jBcSW08UlvMyMAAxOWDH0+RxW4Eokt45t6lXCncDwSfSkJ0KzTdBd3tvGzOQoBUEDBzweeoPn5+fFNtO0O+mit7GzfbsmBdANwwMHcW44J+nTFbmn1XSTb7GTlwOSDI7m3ihljlh3yyLiN842EHJOPPjIoNpDuxmt9D2P0z4UNdmSSYDLOHKjPsPSgtE7KaZey6h8Q0rG3uDDGyuR4MK33ycE+1Wl/oYlb5KMsUpcGQt1luJBHChdznCgZPSho9NsWaczxvIs7hnGRjg5HnX0RuyGhq5ihv5Y5yONs3iFZjtHo9x2fkR3XvreSVV70cbAc9ev9fboYs+p02oXybSRPpo5MbqKts70yz0p4o1hs7yUjcoCtHGg2kZGSfVh96dadbZtprix7PWzKjOpkuLhnxtyDxgjyo/QNKRtGhMNy9uGjYvgKxUuQzEN8x60SkaTLPHY6zDJK6OoVHxgsxbPhPJyaw543fDNFaleQPPaGHSnmt2tbWFYC4EFmOcLnqT1+lMItE1eWBDdazdyrgHCOsWB8lXp9aXa3rUlvPHonespuIGjIaMjCkNnaehGOK0Ecl4UjlMltgeIEpIP9+Kj6UmrGlqIp0JNN7LJeWUc91iZ/Fu7+aQ8hiOi/KiI+zcFvqllG0FvseKXKRR5B/CRwxP3pjawwW8cXxZASFHBkVjhw2TggHj+lJ9N1hNR1+P4W1RYIWnRUb+cb8fIfhoLE3YHqIpJ33HxsNOjJj2BSvBBKj8g1SrL7X9Hs7gxT/DRsB0kCgn7/AFH0qUNkvCH6kfZjI+wlkreOZigP4Qo4+tEz32j9l4O6gi5J5C4JYj3PX/SpqerajPGYtP0+dHxy0yMB+QOfyrG3XZntBcyGeZ0eQ/5xgeg8PSrGSUkviuSgoSfD7H0LStWttWsHmt8oB4WV+Np+lL+ylwpGtx4wy3rNjzIKr+xoDspbTaXp93bakHSZ23IQjsrDGMZ29aXWsOtad2hudSsLYy2czZKlXBkXA5Hh4Oc4/rXRlParXIrg9zokMOlNq15HrUyW16szPHOxZe8jPQqc9Rz+VPdR1TS20Ca2n1GC8KxEAlvE5xx08846VJ/4Jqqg39jdo6/ySWr4B+2PtQd9onZ97KdLK2kE5jbu/wD13Hixxjw+tM7ppMC33yg63u407DGW4D7fhVLrE5DEEDoc5Bx70vtNELJb3dquozM+1483YaNQf8W45PB9K9ZLiTsdDp8FvM15LBGjI0TgJwM5OKF7OjtFoZEc9v39p5qGbcvyyBUabU1a8ElTcGkNO089t8To8EsobUIpslV58BGGyfL+lF9qoln0iyd9SFhbg4Zmj3qSRxu4PpikGv6TY6oTqWlTSW18f/J3ckLpubrzleD7/rTLS9TlhsBYdpLMGKQbS0amRD8wBkUXKUri/wCHRi4SUkuBDb2lxfxLbw9q7d4txCI1qsy5HsAcGnXY2Ix6/HaMw72BDE4EezJx12+WQc0x02x0LSZHu9P7yWQAslvGd3PoB5Uq7OXE79p5b/UjHBNLMzsmT4QF2qBkcnp9qlgoxT55ojyucttx4vwVXHYu61C/vrmSNQHupdgYZ8O44/evac6h2h1wXTjT9Lga2H4GlYhmHrgdPlUplrpJUgPQW75PnMWo3e3c92kW3hlaVs+w45oU6/d5aJ76dBuIDAnHHoTzUS9kt0Cw2BlVwO7cAIFyB5n++BihZ72QZWWIAYG2QMWJ569Oc4zk/wDWAky80/YS2sTCVR8bcs+OV7wj9DVY7RXSdLq42jpi4bI+WDQVuFJk3PGp6J4+VPTy49akMp7qTKI7nIyFyQc8/OmoTn2Noe0N83hM07ufMXb7sfLNXDVLyZy4urjDeRkxt9cc+vtSaaZ/DM0rSDIYNtAHr0GOf3q5nkaZHVg285IG3PXjg+fln86VxGuXsZR3mpxKSJ5mCjkh28h6Zr0avqRjAF1cna3Vpnz9gaBs7pLcKjrjaNyqy/hJ6DBzxXTTRyT7khETB87g2FyeeR9f1oJNHW/YRFr91zvursc5DCZyo+xouO8vbjw2upyvz/LO+4D5E/3zSi4uAykKuDt/EpOCAfpUaKAJmS4uFZOpUgnJOf2Nc0db9j5r+9t5HWe9vQACSWlYbf79PPFWDUyY1P8AF76ZiRjbPIMcY9fcUptNXhVlQ96p4G9wCVz7nrXKyeMCSOR1cgLgqNx9MfSkqQbHcWsyIu17++jI8jcyf8qlL4gkG9AIn8R/+qkEe3lxUpa/YbYNcQx7sbeFQuPt09hwOlZ7UlEckKrnxpuPPTxHgDpj2qVKmwnSCLWBBahiCxO8nPnjn9QK5iPdRQyR+FpkO4ge7Yx8sVKlSeWBkhy8mxmPORu8+AMfrVqvgRkgMDjKnODlsZPmTxUqVzAgzULeMSSRpuUBXbIbnwnA5PypQZm3sBgFTjcvBON3Pz5qVKEOxwbYSG6tQ74VgSMr/lz+v6miNLbvsO/Lcj2ODjJHQ1KlJMKK1JImjP4IyQF8sAN+uwZ9ea4kja3mk7maVGikIRg/I61KlOgF8WqXMe+PKEI5UEryfnipUqVG4oJ//9k=

# with open(local_file_path, 'wb') as file:
#     #identify image to be captured
#     #write file
#     file.write(content.screenshot_as_png)
#     print(f"Image downloaded and saved to {local_file_path}")

import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Directory containing the images and audio file
def make_video(audio_folder,image_folder,image_name_prefix):

    # List of image filenames (change these to match your file names)
    imagelist=os.listdir(image_folder)
    imagelist=[item for item in imagelist if image_name_prefix in item]
    # image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

    # Audio file name (change this to match your audio file)
    audio_file = audio_folder+ f"{image_name_prefix}.mp3"

    # Video output file name
    output_video_file = f"data/youtube2/{image_name_prefix}.mp4"

    # Frame rate (number of frames per second)
    
    # Duration of each image in seconds
    
    

    # Load the audio file
    audio = AudioFileClip(audio_folder + audio_file)
    audio=audio.volumex(1.3)
    frame_rate = 30
    
    audio_duration = audio.duration
    each_length=audio_duration/len(imagelist)
    image_duration = int(each_length)
    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (audio.fps * 2, audio.fps * 2))

    # Loop through the images and add them to the video
    for image_file in image_files:
        image = cv2.imread(image_folder + image_file)
        for _ in range(int(audio.fps * image_duration)):
            video_writer.write(image)

    # Release the video writer
    video_writer.release()

    # Combine the video with the audio
    final_video = VideoFileClip(output_video_file)
    final_video = final_video.set_audio(audio)

    # Write the final video to a file
    final_video.write_videofile(output_video_file, codec="libx264")

    # Clean up temporary files
    final_video.close()


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
            output_video_file = f"data/youtube2/{image_name_prefix}.mp4"

            audio_clip = AudioFileClip(audio_folder + audio_file)
            frame_rate = 30
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
            video_clip.write_videofile(output_video_file.replace('-',''), codec="libx264", fps=30)  # Adjust the fps value as needed
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

def make_final_video(search_list):
    # video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Add the file paths of your video files
    video_files=os.listdir('data/youtube2')
    video_files=['data/youtube2/'+item for item in video_files]
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

    final_video.write_videofile("data/youtube3/final.mp4", codec="libx264", fps=30)
    # video_clip.write_videofile(output_video_file, codec="libx264", fps=30)
    for clip in video_clips:
        clip.close()
    final_video.close()

    # video_audio(wjslist)
    # Iterate through the files and remove them
    
    remove_files('data/youtube2')
    # remove_files('data/youtube2')
    remove_files('data/audios')
    remove_files('data/news_images')

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

import re


driver=open_driver()
# %%

#%%
import pyautogui as pt

screenshots=[]
list1=['https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AV', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AADBE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AACN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AIBM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AUBER', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACB', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABSX', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AMELI', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACMG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AKKR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAJG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ADELL', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHLT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACOR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AFICO', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHWM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ATW', 'https://www.tradingview.com/chart/tMeJexox/?symbol=BATS%3ACBOE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AAKAM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AL', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AGDDY', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AMORN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACASY', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ANTNX', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWING', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHRB', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABRBR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AENSG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AENLC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ACNM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AOBDC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AFG', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AMOG.A', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AVRNS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABNRE.A', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAMR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWDFC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AHCC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ALRN', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AAIR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AATGE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AIDYA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AAFYA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AMBC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACLBT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AFOR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ABVH', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AFRGE', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ADAKT', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ACVRX', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ASPOK', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AJAKK', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AWEYS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AGASS', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3AGHM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ARNAC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AQUIK', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AHCMA', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ASMID', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AFINW', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AIZM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3ANCAC', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AFONR', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AAPXI', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYAM%3AMYO', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NASDAQ%3AITRM', 'https://www.tradingview.com/chart/tMeJexox/?symbol=NYSE%3ASWKHL']
for ii,item in enumerate(list1):
    if ii==0:
        for _ in range(3):
            try:
                driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]').click()
                break
            except:
                time.sleep(2)
                pass
    
    # if ii<10:
    #     continue
    driver.get(item)
    
    pt.press('enter')
    time.sleep(5)
    ticker=item.split('3A')[-1]
    
    # driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]').click()

    screenshot_path=f'data/tradingview_images/{ticker}.png'

    driver.save_screenshot(screenshot_path)
    screenshots.append(screenshot_path)


