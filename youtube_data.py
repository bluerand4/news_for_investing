"""
    This is  for getting some data from youtube using youtubedata API
"""

import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

from utils import *



class YoutuberDummyParameters():
    def __init__(self, user_name="me"):
        # Some dummy parameters for initial development
        self.user_name = user_name
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.DEVELOPER_KEY = "{developer_key_youtube}"
        self.client_secrets_file = "CLIENT.json"
        self.scopes = ["https://www.googleapis.com/auth/youtube.force-ssl", 
                       "https://www.googleapis.com/auth/userinfo.email",
                       "openid"]
        self.creds = None

    def YoutubeExtractor(self, local_api=True):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        self._oauthlibInsecureTransport()

        # For using personal API key uses local_api = True,
        # for clients use local_api = False
        if local_api:
            return self._youtubeExtractorLocal()
        else:
            return self._youtubeExtractorClient()
        
    def _youtubeExtractorLocal(self):
        # create an API client, uses personal API key
        api_service_name = self.api_service_name
        api_version = self.api_version
        DEVELOPER_KEY = self.DEVELOPER_KEY
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)
        return youtube

    def generateUserProfileInfo(self):
        creds = self.creds
        if creds:
            try:
                userinfo = googleapiclient.discovery.build('oauth2', 'v2', credentials=creds)
                return userinfo
            except Exception as err:
                print("no possible to get userinfo")
                return None
        else:
            print("no credentials to generate userinfo")
            return None    
                
    def _youtubeExtractorClient(self):
        # Get credentials and create an API client, uses Oauth2 key
        creds = self.creds
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.user_name+'_token.pickle'):
            with open(self.user_name+'_token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            print("\n\n##########################")
            print("Requesting New Credentials")
            print("##########################\n\n")
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.user_name+'_token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        print("\n\n##########################")
        print(" the credentials ")
        print(creds.to_json())
        print("##########################\n\n")
        self.creds = creds

        youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials=creds)
        return youtube

    def _oauthlibInsecureTransport(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"        



def GetMyPlaylistsList(youtube, **kwargs):
    """
    This example retrieves playlists created in the authorized user's YouTube channel. 
    It uses the mine request parameter to indicate that the API should only return playlists
    owned by the user authorizing the request.
    """
    request = youtube.playlists().list(
        part = "snippet,contentDetails",
        mine = True, 
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetAPlaylistsList(youtube, channelId, **kwargs):
    """
    This example retrieves playlists owned by the YouTube channel that
    the request's channelId parameter identifies.
    """
    request = youtube.playlists().list(
        part = "snippet,contentDetails",
        channelId = channelId, 
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetMyChannelsList(youtube, **kwargs):
    """
    This example retrieves the channel data for the authorized user's YouTube channel. 
    It uses the mine request parameter to indicate that the API should only return
    channels owned by the user authorizing the request.
    """
    request = youtube.channels().list(
        part = "snippet,contentDetails,statistics",
        mine = True, 
        **kwargs
    )
    return AuxMakeYoutubeRequest(request) 

def GetAChannelsList(youtube, channelID, **kwargs):
    """
    This example retrieves channel data for the GoogleDevelopers YouTube channel. 
    It uses the id request parameter to identify the channel by its YouTube channel ID.
    """
    request = youtube.channels().list(
        part = "snippet,contentDetails,statistics",
        id = channelID, 
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetAPlaylistItemsList(youtube, playlistId, **kwargs):
    """
    This example retrieves the list of videos in a specified playlist. 
    The request's playlistId parameter identifies the playlist.
    """
    request = youtube.playlistItems().list(
        part = "snippet, contentDetails",
        playlistId = playlistId, 
        **kwargs
    )
    response = request.execute() 
    return response   

def GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs):
    """
    This example retrieves all comment threads associated with a particular video.
    The request's videoId parameter identifies the video.
    """
    
    request = youtube.commentThreads().list(
        part = "snippet,replies",
        videoId = videoId,
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetCommentThreadsListbyChannelID(youtube, channelId, **kwargs):
    """
    This example retrieves all comment threads about the specified channel.
    The request's channelId parameter identifies the channel.
    The response does not include comments left on videos that the channel uploaded.
    """
    request = youtube.commentThreads().list(
        part = "snippet,replies",
        channelId = channelId,
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs):
    """
    This example retrieves all comment threads associated with a particular channel. 
    The response could include comments about the channel or about the channel's videos. 
    The request's allThreadsRelatedToChannelId parameter identifies the channel.
    """
    request = youtube.commentThreads().list(
        part = "snippet,replies",
        allThreadsRelatedToChannelId = channelId, 
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)

def GetCommentThreadsListbyModerationStatus(youtube, channelId, moderationStatus, **kwargs):
    """
    This example retrieves all comment threads associated with a particular channel.
    The response could include comments about the channel or about the channel's videos.
    moderationStatus limit the returned comment threads to a particular moderation state.
    """
    request = youtube.commentThreads().list(
        part = "snippet,replies",
        allThreadsRelatedToChannelId = channelId,
        moderationStatus = moderationStatus,
        **kwargs
    )
    return AuxMakeYoutubeRequest(request)



def CommentDelete(youtube, commentId):
    """
    This example deletes the specified comment. 
    You must use the id parameter to specify a comment ID for the code sample to work.
    """
    request = youtube.comments().delete(
        id = commentId
    )
    return AuxMakeYoutubeRequest(request)

def CommentSetModerationStatus(youtube, commentId, moderationStatus="heldForReview"):
    """
    This example sets the moderation status of one or more comments to heldForReview 
    You can also set the moderation status to published or rejected or likelySpam.
    """
    request = youtube.comments().setModerationStatus(
        id = commentId,
        moderationStatus = moderationStatus
    )
    return AuxMakeYoutubeRequest(request)

def CommentMarkAsSpam(youtube, commentId):
    """
    This example marks the specified comment as spam. 
    You must use the id parameter to specify a comment ID for the code sample to work.
    """
    request = youtube.comments().markAsSpam(
        id = commentId
    )
    return AuxMakeYoutubeRequest(request)



def AuxMakeYoutubeRequest(request):
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        return HandleError(e.error_details[0]["reason"])
    return response

def AuxGetPlaylistVideosList(playlist_response):
    """
    Gets the playlist videos from a 
    youtube.playlistItems().list() response object
    """
    playlist_videos = []
    for item in playlist_response['items']:
        playlist_video = PlaylistVideo()
        playlist_video.playlist_id = item["snippet"]["playlistId"], 
        playlist_video.channel_id = item["snippet"]["channelId"],
        playlist_video.video_id = item["contentDetails"]["videoId"]
        
        playlist_videos.append(playlist_video)
    return playlist_videos

def AuxGetChannelRelatedPlaylists(channellist_response):
    """
    Gets the ID of the playlist that contains the
    channel's uploaded videos from a 
    youtube.channels().list() response object
    """
    channelplaylists = ChannelPlaylists()
    channelplaylists.channel_id = channellist_response['items'][0]['id']
    channelplaylists.channel_uploads = [channellist_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']]
    return channelplaylists

def AuxGetCommentThreadsCommentsList(commentthreads_response):
    """
    Get the comments from a 
    youtube.commentThreads().list() response object
    """
    commentthreads_comments = []
    for item in commentthreads_response["items"]:
        to_video_id = item["snippet"].get("videoId")
        to_channel_id = item["snippet"]["channelId"]
        comment = AuxParseCommentInfo(item["snippet"]["topLevelComment"])
        comment.to_video_id = to_video_id
        comment.to_channel_id = to_channel_id
        comment.is_response = False
        commentthreads_comments.append(comment)

        if "replies" in item:
            for subitem in item["replies"]["comments"]:
                comment = AuxParseCommentInfo(subitem)
                comment.to_video_id = to_video_id
                comment.to_channel_id = to_channel_id
                comment.is_response = True
                commentthreads_comments.append(comment)
    return commentthreads_comments

def AuxCommentsModeration(youtube, comments, moderationStatus, allowedAuthors=[]):
    """
    Sets the moderationStatus of a list of comments that do not belong to a list
    of allowed authors
    """
    for comment in comments:
        if comment.comment_author_id not in allowedAuthors:
            CommentSetModerationStatus(youtube, comment.comment_id, moderationStatus)
    return None

def AuxParseCommentInfo(comment_response):
    """
    Parse information in a comment
    """
    comment = Comment()
    comment.comment_id = comment_response["id"]
    comment.comment_text = comment_response["snippet"]["textDisplay"]
    comment.comment_author_id = comment_response["snippet"]["authorChannelId"]["value"]
    comment.like_count = comment_response["snippet"]["likeCount"]
    comment.updatedAt = comment_response["snippet"]["updatedAt"]
    return comment
