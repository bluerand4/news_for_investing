#%%
from import_stocks2 import *

youtuber = YoutuberDummyParameters()


# prepare the extractor for client
youtube = youtuber.YoutubeExtractor(local_api=False)   

#%%

timedelta1=0
timedelta2=100
today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
past2=datetime.strptime('20210218', "%Y%m%d").timestamp()


title= f'{today1}_{video_title}_news'
filename=os.listdir('data/youtube2')[-1]
file_name=f'data/youtube2/{filename}'
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


#%%
from moviepy.editor import concatenate_audioclips, ImageClip, AudioFileClip
from moviepy.editor import ImageClip, AudioFileClip

video_title='today_news'
description=video_title
filepath=os.listdir('data/youtube2')
filepath
#%%
filepath=sorted(filepath)[-1]
filepath='data/youtube2/'+'final_1701279722.mp4'
filepath
#%%
# youtube_upload(video_title,description,filepath)
# %%
folder1='data/youtube2/'
youtuber = YoutuberDummyParameters()


# prepare the extractor for client
youtube = youtuber.YoutubeExtractor(local_api=False)   



timedelta1=0
timedelta2=100
today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d %M%S"))
today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d %M%S"))
past2=datetime.strptime('20210218', "%Y%m%d").timestamp()



file_list=os.listdir(folder1)
file_list
#%%
# for filename in file_list:
filename='main_news_1701694485.mp4'
file_name=folder1+filename
description=filename.split('.')[0]
title= f'{today1}_{description}_news'
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
# %%
