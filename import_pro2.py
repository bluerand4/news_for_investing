#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

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



def save_images(search_list,audio_folder='data/news_audios/',random_voices=False):
    search_list=[item.replace('-','').replace('\n','') for item in search_list]
    search_list=[item for item in search_list if len(item)>2]

    for ii in range(len(search_list)):
        try:
            search=search_list[ii]
            url = "https://www.bing.com/images/search"

            querystring = {"q":search,"qs":"n","form":"QBIR","sp":"-1","lq":"0","pq":search,"sc":"0-385","cvid":"8315BDF4778F4D79B9BEE404E2235FCD","ghsh":"0","ghacc":"0","first":"1"}

            payload = ""
            headers = {
                "cookie": "MUID=187D6415C7756594386277C8C6556400; MUIDB=187D6415C7756594386277C8C6556400; _EDGE_S=F%3D1%26SID%3D0217789F30A1631932186B42318162D7; _EDGE_V=1; MMCASM=ID%3D4B7BB4EC8C0242ADA2B01CE7EAD8A518; SRCHD=AF%3DQBIR; SRCHUID=V%3D2%26GUID%3DCC81D6DC8DF1492892505589E1146896%26dmnchg%3D1; SRCHUSR=DOB%3D20231204; SRCHHPGUSR=SRCHLANG%3Dko%26IG%3DE6A3BF77318E480DB48AB9506B0C4CB5; _SS=SID%3D0217789F30A1631932186B42318162D7",
                "User-Agent": "insomnia/8.4.2"
            }

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

            # print(response.text)
            
            soup = BeautifulSoup(str(response.text), 'html.parser')
            text = soup.text
            text
            div_content = soup.find_all('img', class_="mimg")
            
            for iii,item in enumerate(div_content[:5]):

                img_link=div_content[iii]['src']

                response = requests.get(img_link)
                response

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
                time.sleep(1)
            print('done ',item)
            time.sleep(3)
        except Exception as e:
            print( 0 ,' = >>> some error = ',e)
    
    

    for ii in range(len(search_list)):
        # time.sleep(1)
        search=search_list[ii]
        name_prefix=search[:20]
        audio_download_v3(name_prefix,search,audio_folder,random_voices)
        print(ii)
    return search_list
