"""
This presents some utils used in the other scripts
"""


"""
Dummy classes used for consistency
"""
class Comment():
    def __init__(self):
        self.comment_author_id = None
        self.comment_id = None
        self.comment_text = None
        self.comment_flagged = None
        self.comment_description = None
        self.is_response = None
        self.like_count = None
        self.to_video_id = None
        self.to_channel_id = None
        self.updatedAt = None

class PlaylistVideo():
    def __init__(self):
        self.playlist_id = None
        self.channel_id = None
        self.video_id = None

class ChannelPlaylists():
    def __init__(self):
        self.channel_id = None
        self.channel_uploads = None        


"""
    Error handling
"""        
def HandleError(stringi):
    print("This error ", stringi)
    return None
