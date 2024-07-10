from utils import *
import pandas as pd

def AuxGetCommentsDataFrame(commentthreads_comments, short=True):
    """
    Converts a list of Comments() to a DataFrame
    it parses the dates of style "2023-09-01T00:00:00Z"
    """
    df = pd.DataFrame([comment.__dict__ for comment in commentthreads_comments])
    if short:
        df = df[["comment_id", "comment_text"]]
    else:    
        df["updatedAt"] = pd.to_datetime(df["updatedAt"])
    return df
    
