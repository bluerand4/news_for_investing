#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from import_stocks import *
import openai,getpass,os
path1=f'{path_to_openai_api}'
with open(path1,'r') as f:
    key=f.readline()
os.environ["OPENAI_API_KEY"] = key
openai.api_key = key
from googleapiclient.http import MediaFileUpload
from openai import OpenAI
client = OpenAI()

def make_inter_videos_v2(search_list,image_folder,audio_folder):
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

def make_final_video_v2(search_list,name):
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
#%%
page_list=['startups','artificial-intelligence','venture','apps']
page_list=['apps']
for page_name in page_list:

    # url = "https://techcrunch.com/category/artificial-intelligence/"
    url = f"https://techcrunch.com/category/{page_name}/"

    payload = ""
    headers = {"User-Agent": "insomnia/8.4.2"}

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)


    soup = BeautifulSoup(str(response.text), 'html.parser')
    text = soup.text
    text
    # div_content = soup.find_all('div', class_="river river--category river--subscription-enabled")
    div_content = soup.find_all('div', class_="content")
    print("\n>> len(div_content)= ", len(div_content))

    news=div_content[1].text.replace('\n','').replace('\t','')
    print("\n>> len(news)= ", len(news))

    import re
    # pattern = r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}\b'
    pattern = r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2},\s\d{4}'
    # Find all matches
    dates = list(set(re.findall(pattern, news)))
    dates

    list1=[]
    for item in news.split(dates[0]):
        if len(dates)==1:
            list1.append(item)
        else:
            for item2 in item.split(dates[1]):
                list1.append(item2)
    news2=list1[:10]


    define='bulletpoint each point and summarize based on [company name] has good or bad news. and explain why. if no specific [company_name] is mentioned, then just summarize'
    summary=gpt_answer(news2,define)

    new_list=summary.split('\n')
    new_list



    new_list=save_images(new_list,random_voices=True)
    new_list

    image_folder='data/news_images/'
    audio_folder='data/news_audios/'
    make_inter_videos_v2(new_list,image_folder,audio_folder)

    make_final_video_v2(new_list,page_name)

    filename=f'{page_name}.mp4'
    folder1='data/youtube3/'
    duration=get_video_length(f'data/youtube3/{filename}')

    subtitle_fullpath=f'data/subtitles/{page_name}.srt'

    srt_entries = generate_srt(new_list, duration)
    write_srt_file(srt_entries, subtitle_fullpath)

    print("SRT file created successfully.")

    # youtube_upload_folder('data/youtube2/')
    # data=upload_youtube_v2(folder1,filename)

    # video_id=data[1]['id']
    # video_id
    

    # upload_subtitle(video_id,subtitle_fullpath)
    

# %%