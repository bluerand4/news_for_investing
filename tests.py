#%%
from youtube_data import *
from ai_moderator import *
from utils import *
from dataframe_stuff import *
from make_credentials import *
from spreadsheet import *

# Tests part of the youtube_data.py code using clients permission
def testYoutubeDataAPI():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)    
    
    # get the client's channel info
    channellist_response = GetMyChannelsList(youtube)
 
    # get the channels asociated playlists
    channel_relatedPlaylists = AuxGetChannelRelatedPlaylists(channellist_response)

    # get a playlist items by playlist id
    playlist_response = GetAPlaylistItemsList(youtube, channel_relatedPlaylists.channel_uploads[0])

    # get the playlist videos
    playlist_videos = AuxGetPlaylistVideosList(playlist_response)

    # get the commentthreads by video id
    kwargs = {"textFormat":"plainText"}
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs)

    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)

    # set the moderationStatus in the comments that are not form the allowed authors
    allowedAuthors = [channel_relatedPlaylists.channel_id] # the channel owner is an allowed author
    moderationStatus = "heldForReview"
    AuxCommentsModeration(youtube, commentthreads_comments, moderationStatus=moderationStatus, allowedAuthors=allowedAuthors)    

    # get all the comments with a given moderationStatus
    commentthreads_response_moderated = GetCommentThreadsListbyModerationStatus(youtube, channel_relatedPlaylists.channel_id, moderationStatus=moderationStatus)
    return commentthreads_response_moderated

testYoutubeDataAPI()
#%%


# Tests the AIModerator with madeup comments
def testAIModerator():
    textdata = [
        "don't you want to buy the new cellphone? do you really want to miss this opportunity? I do not think so, give me a call, yes?",
        "this is a hate comment",
        "do you think you should kill you? do you think I hate you?",
        "and hate comment?",
        "and spam comment?",
        "can i add a comment?",
        "can you give information about this place",
        "this is a neutral comment",
        "Tree in a house",
        "I think you should kill you, I hate you", 
        "buy the new cellphone do not miss the opportunity send a message to us",
    ]   

    comments = []
    for comment_text in textdata:
        comment = Comment()
        comment.comment_text = comment_text
        comment.comment_author_id = "1"

        comments.append(comment)

    commentdescriptions = GetOpenAICommentDescription(comments, "gpt-4") 

    for comment in commentdescriptions:
        print("\n\n")
        print(comment.comment_text)
        print(comment.comment_flagged)
        print(comment.comment_description)

    return commentdescriptions

testAIModerator()
#%%


# Test to get all the comments from a not owned video using pageToken
def testGetAllCommentsfromVideo():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=True) 
    videoId = "F2D4q4JYkRI"   
    kwargs = {"textFormat":"plainText"}
    #comments = get_video_comments(youtube, videoId)

    # get the commentthreads by video id
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)
    
    
    while commentthreads_response:
        if 'nextPageToken' in commentthreads_response:
            #kwargs = {}
            kwargs['pageToken'] = commentthreads_response['nextPageToken']
            # get the commentthreads by video id
            commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
            # get the comments of a thread
            more_comments = AuxGetCommentThreadsCommentsList(commentthreads_response) 
            commentthreads_comments.extend(more_comments)         
        else:
            break    

    return commentthreads_comments

testGetAllCommentsfromVideo()
#%%


# Test to get all the comments from a non existent video
def testYoutubeErrors():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=True) 
    videoId = "F2D4q4JYkRI212"   
    kwargs = {"textFormat":"plainText"}
    #comments = get_video_comments(youtube, videoId)

    # get the commentthreads by video id
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
    if isinstance(commentthreads_response, type(None)):
        return
    
    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)
    
    
    while commentthreads_response:
        if 'nextPageToken' in commentthreads_response:
            #kwargs = {}
            kwargs['pageToken'] = commentthreads_response['nextPageToken']
            # get the commentthreads by video id
            commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
            if isinstance(commentthreads_response, type(None)):
                return
            # get the comments of a thread
            more_comments = AuxGetCommentThreadsCommentsList(commentthreads_response) 
            commentthreads_comments.extend(more_comments)         
        else:
            break    

    return commentthreads_comments    

testYoutubeErrors()

#%%

def testOpenAIErrors():
    textdata = [
        "I think you should kill you, I hate you",
        "this is a neutral comment",
        "buy the new cellphone do not miss the opportunity send a message to us",
        "can you give information about this place"
    ]   

    comments = []
    for comment_text in textdata:
        #comment = Comment()
        #comment.comment_text = comment_text
        #comment.comment_author_id = "1"

        comments.append(comment_text)

    try:
        commentdescriptions = GetOpenAICommentDescription(comments)    
    except Exception as e:
        print(e)
        return None

    return commentdescriptions
    
testOpenAIErrors()    
#%%

# Tests part of the youtube_data.py code using clients permission
def testYoutubeModeratorIntegration():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)    
    
    # get the client's channel info
    channellist_response = GetMyChannelsList(youtube)
 
    # get the channels asociated playlists
    channel_relatedPlaylists = AuxGetChannelRelatedPlaylists(channellist_response)

    # get a playlist items by playlist id
    playlist_response = GetAPlaylistItemsList(youtube, channel_relatedPlaylists.channel_uploads[0])

    # get the playlist videos
    playlist_videos = AuxGetPlaylistVideosList(playlist_response)

    # get the commentthreads by video id
    kwargs = {"textFormat":"plainText"}
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs)

    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)

    comment_moderated = GetOpenAICommentDescription(commentthreads_comments, "gpt-4")
    
    comment_todo = []
    for comment in comment_moderated:
        if comment.comment_flagged:                     # uses OPENAI API Moderation https://platform.openai.com/docs/guides/moderation
            comment_todo.append(comment)
        if comment.comment_description["hate"]=="yes":  # uses OPENAI API functional call https://platform.openai.com/docs/guides/gpt/function-calling
            comment_todo.append(comment)
        if comment.comment_description["spam"]=="yes":  # uses OPENAI API functional call https://platform.openai.com/docs/guides/gpt/function-calling
            comment_todo.append(comment)

    # set the moderationStatus in the comments that are not form the allowed authors
    allowedAuthors = [channel_relatedPlaylists.channel_id] # the channel owner is an allowed author
    moderationStatus = "heldForReview"
    AuxCommentsModeration(youtube, comment_todo, moderationStatus=moderationStatus, allowedAuthors=allowedAuthors)    

    # get all the comments with a given moderationStatus
    commentthreads_response_moderated = GetCommentThreadsListbyModerationStatus(youtube, channel_relatedPlaylists.channel_id, moderationStatus=moderationStatus)
    commentthreads_response_moderated_comments = AuxGetCommentThreadsCommentsList(commentthreads_response_moderated)
    for comment in commentthreads_response_moderated_comments:
        print("\n\n")
        print(comment.comment_text)

    return commentthreads_response_moderated

testYoutubeModeratorIntegration()
#%%

# Test to get all the comments from a not owned and convert to dataframe
def testGetCommentsDataFramefromVideo():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=True) 
    videoId = "bYqS5TGiji4" #"F2D4q4JYkRI"   
    kwargs = {"textFormat":"plainText"}
    #comments = get_video_comments(youtube, videoId)

    # get the commentthreads by video id
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)
    
    
    while commentthreads_response:
        if 'nextPageToken' in commentthreads_response:
            #kwargs = {}
            kwargs['pageToken'] = commentthreads_response['nextPageToken']
            # get the commentthreads by video id
            commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
            # get the comments of a thread
            more_comments = AuxGetCommentThreadsCommentsList(commentthreads_response) 
            commentthreads_comments.extend(more_comments)         
        else:
            break    

    df = AuxGetCommentsDataFrame(commentthreads_comments)    
    return df

testGetCommentsDataFramefromVideo()
#%%


# Test to get all the comments from a channelId in DB
def testGetCommentsfromDB(createdBy):
    # Make youtube parameters                                                     
    youtube = make_youtube(createdBy)

    # get the client's channel info
    channellist_response = GetMyChannelsList(youtube)
 
    # get the channels asociated playlists
    channel_relatedPlaylists = AuxGetChannelRelatedPlaylists(channellist_response)

    # get a playlist items by playlist id
    playlist_response = GetAPlaylistItemsList(youtube, channel_relatedPlaylists.channel_uploads[0])

    # get the playlist videos
    playlist_videos = AuxGetPlaylistVideosList(playlist_response)

    # get the commentthreads by video id
    kwargs = {"textFormat":"plainText"}
    commentthreads_response = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs)

    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)

    comment_moderated = GetOpenAICommentDescription(commentthreads_comments, "gpt-4")
    
    comment_todo = []
    for comment in comment_moderated:
        if comment.comment_flagged:                     # uses OPENAI API Moderation https://platform.openai.com/docs/guides/moderation
            comment_todo.append(comment)
        if comment.comment_description["hate"]=="yes":  # uses OPENAI API functional call https://platform.openai.com/docs/guides/gpt/function-calling
            comment_todo.append(comment)
        if comment.comment_description["spam"]=="yes":  # uses OPENAI API functional call https://platform.openai.com/docs/guides/gpt/function-calling
            comment_todo.append(comment)

    # set the moderationStatus in the comments that are not form the allowed authors
    allowedAuthors = [channel_relatedPlaylists.channel_id] # the channel owner is an allowed author
    moderationStatus = "heldForReview"
    AuxCommentsModeration(youtube, comment_todo, moderationStatus=moderationStatus, allowedAuthors=allowedAuthors)    

    # get all the comments with a given moderationStatus
    commentthreads_response_moderated = GetCommentThreadsListbyModerationStatus(youtube, channel_relatedPlaylists.channel_id, moderationStatus=moderationStatus)
    commentthreads_response_moderated_comments = AuxGetCommentThreadsCommentsList(commentthreads_response_moderated)
    for comment in commentthreads_response_moderated_comments:
        print("\n\n")
        print(comment.comment_text)

    return commentthreads_response_moderated




# Tests getting user info using clients permission
def testUserinfoDataAPI():
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=False)    
    
    # get the client's channel info
    userinfo_service = youtuber.generateUserProfileInfo()

    if userinfo_service:
        userinfo = userinfo_service.userinfo().get().execute()
    else:
        userinfo = None
    
    userinfo

testUserinfoDataAPI()


#%%

def testMakeSpreadSheet():
    results = make_plans_users_aggregation()
    a = []
    for result in results:
        a.append(result["createdBy"])
        
        createdBy = a[-1]
    
        # Make youtube parameters                                                     
        youtube = make_youtube(createdBy)

        # get the client's channel info
        channellist_response = GetMyChannelsList(youtube)
     
        # get the channels asociated playlists
        channel_relatedPlaylists = AuxGetChannelRelatedPlaylists(channellist_response)

        # get a playlist items by playlist id
        playlist_response = GetAPlaylistItemsList(youtube, channel_relatedPlaylists.channel_uploads[0])

        # get the playlist videos
        playlist_videos = AuxGetPlaylistVideosList(playlist_response)

        kwargs = {"textFormat":"plainText"}
        # get the commentthreads by video id
        commentthreads_response = GetCommentThreadsListbyVideoID(youtube, playlist_videos[0].video_id, **kwargs)

        # get the comments of a thread
        commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)

        while commentthreads_response:
            if 'nextPageToken' in commentthreads_response:
                #kwargs = {}
                kwargs['pageToken'] = commentthreads_response['nextPageToken']
                # get the commentthreads by video id
                commentthreads_response = GetCommentThreadsListbyVideoID(youtube, videoId, **kwargs)
                # get the comments of a thread
                more_comments = AuxGetCommentThreadsCommentsList(commentthreads_response) 
                commentthreads_comments.extend(more_comments)         
            else:
                break    

        # get the dataframe from the commentthreads
        df = AuxGetCommentsDataFrame(commentthreads_comments) 

        # add columns to dataframe
        questions = ["delete_comment", "answer_comment"]
        reasons_to_delete = ["delete_hate", "delete_sexual", "delete_other"]
        reasons_to_answer = ["answer_good", "answer_help", "answer_other"]
        prefix = "_is_complete"
        reasons = {"delete_comment":reasons_to_delete, "answer_comment":reasons_to_answer}
        for question in questions:
            df[question] = -1
            for reason_i in reasons[question]:
               df[reason_i] = -1
            df[question+"_is_complete"] = -1
        # user email
        user_email = "gabriel.diaz.iturry@gmail.com"

        # make spreadsheet
        auxCreateExampleSpreadsheet(df, reasons, prefix, user_email)


def testEmbeddingComments():
    """
    TODO needs to be finished!!
    """
    # make youtuber parameters
    youtuber = YoutuberDummyParameters()
    
    # prepare the extractor for client
    youtube = youtuber.YoutubeExtractor(local_api=True) 

    # get the commentthreads by video id
    channelId = "UC8ENHE5xdFSwx71u3fDH5Xw" 
    maxlen = 100
    kwargs = {"textFormat":"plainText"} 

    # get the commentthreads by channel id
    commentthreads_response = GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs)
    # get the comments of a thread
    commentthreads_comments = AuxGetCommentThreadsCommentsList(commentthreads_response)
    
    
    while commentthreads_response:
        if 'nextPageToken' in commentthreads_response:
            #kwargs = {}
            kwargs['pageToken'] = commentthreads_response['nextPageToken']
            # get the commentthreads by video id
            commentthreads_response = GetCommentThreadsListbyChannelID_all(youtube, channelId, **kwargs)
            # get the comments of a thread
            more_comments = AuxGetCommentThreadsCommentsList(commentthreads_response) 
            commentthreads_comments.extend(more_comments)         
            if len(commentthreads_comments) > maxlen:
                break
        else:
            break    

    df = AuxGetCommentsDataFrame(commentthreads_comments, short=False)    
    return df
