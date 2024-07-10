from youtube_data import *
from ai_moderator import *
from utils import *
from dataframe_stuff import *
from make_credentials import *
from spreadsheet import *

# make youtuber parameters
youtuber = YoutuberDummyParameters()
youtube = youtuber.YoutubeExtractor(local_api=False)    
channellist_response = GetMyChannelsList(youtube)

###############
channel_relatedPlaylists = AuxGetChannelRelatedPlaylists(channellist_response)
playlist_response = GetAPlaylistItemsList(youtube, channel_relatedPlaylists.channel_uploads[0])
playlist_videos = AuxGetPlaylistVideosList(playlist_response)
kwargs = {"textFormat":"plainText"}
commentthreads_response_1 = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs)

print(len(commentthreads_response_1["items"]))
#####
kwargs_ = {"textFormat":"plainText", "order":"relevance"}
commentthreads_response_1_ = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs_)

print(len(commentthreads_response_1_["items"]))
#####
channelId = channellist_response["items"][0]["id"] 
commentthreads_response_2 = GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs)

print(len(commentthreads_response_2["items"]))
####
commentthreads_response_2_ = GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs_)

print(len(commentthreads_response_2_["items"]))

###########3
###########
###########


youtuber = YoutuberDummyParameters()
youtube = youtuber.YoutubeExtractor(local_api=True)    

#############
channelId = "UCRdl6XLjYhP7I40PB-1fhqQ"
kwargs = {"textFormat":"plainText"}
channel = GetAChannelsList(youtube, channelId)
playlist = GetAPlaylistsList(youtube, channelId)
playlist_response = GetAPlaylistItemsList(youtube, playlist["items"][0]["id"]) 
commentthreads_response_3 = GetCommentThreadsListbyVideoID(youtube, playlist_response["items"][0]["contentDetails"]["videoId"], **kwargs)

print(len(commentthreads_response_3["items"]))


#############
commentthreads_response_4 = GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs)

print(len(commentthreads_response_4["items"]))
