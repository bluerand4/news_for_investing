
#%%
subtitles=[]

subtitles1=[item for item in search.split('.') if len(item)>3]
subtitles1
duration_subtitle=int(video_clip.duration/len(subtitles1))
start_time=0
for item in subtitles1:
    subtitles.append(((start_time,start_time+duration_subtitle),item))
    start_time+=duration_subtitle
#%%
subtitles
#%%
subtitles_clips = []

for text, start_time in subtitles:
    text_clip = TextClip(text, fontsize=24, color='white', bg_color='black')
    # text_clip = TextClip(text, fontsize=24, color='white', bg_color='black')
    # text_clip = text_clip.set_position(('center', 'bottom')).set_start(start_time).set_duration(duration_subtitle)  # Adjust duration as needed
    subtitles_clips.append(text_clip)
#%%
subtitles_clips = []

for (start_time,text )  in subtitles:
    text_clip = TextClip(text, fontsize=24, color='white', bg_color='black')
    text_clip = text_clip.set_position(('center', 'bottom')).set_start(start_time).set_duration(duration_subtitle)
    subtitles_clips.append(text_clip)

#%%
subtitles_clips
#%%
subtitles_clip = SubtitlesClip(subtitles_clips)
# subtitles_clip = subtitles_clip.set_audio(audio_clip)
#%%
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
subtitles = SubtitlesClip("somet.srt", generator)


# final_video = video_clip.set_audio(None).set_duration(subtitles_clip.duration)
# final_video = final_video.set_audio(audio_clip)
# final_video = final_video.set_duration(subtitles_clip.duration)
# final_video = final_video.set_audio(audio_clip)
# final_video = final_video.set_duration(subtitles_clip.duration)
# final_video = final_video.overlay(subtitles_clip)
#%%
# subtitles_clip = subtitles_clip.set_audio(audio_clip)

# Overlay subtitles onto the video
# final_video = video_clip.set_audio(None)
# final_video = final_video.set_duration(subtitles_clip.duration)
# final_video = final_video.set_audio(audio_clip)
final_video = final_video.overlay(subtitles_clip)
