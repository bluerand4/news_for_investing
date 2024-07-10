
#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


from google.cloud import vision
from google.cloud import translate_v2 as gt
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryaneontech1@gmail.com/My Drive/t1_code/t1_authentification/twilio-call-v1-a7cee1c9cc7f.json'

def image2text(path):
    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
    return texts[0].description