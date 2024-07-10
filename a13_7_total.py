#%%
from import_stocks import *
stock_list='AJG,IR,WRB,LDOS,CE,GLOB,APG,AMR,WDFC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK'
# stock_list='WDFC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK'
# stock_list='WDFC'
# stock_list='PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK'
# stock_list='AJG,IR,WRB,LDOS,CE,GLOB,APG,AMR,WFDC,PGTI,AFYA,ROVR,HCI,TIPT,CVRX,ML,LWAY,HRTG,QUIK,'
stock_list='VRNS,GLOB,COR,IR,WRB,LII,LDOS,ENSG,OBDC,AIR,PGTI,HCI,CVRX,ML,LWAY,HRTG,GHM'
stock_list='WMT,DOCN,SHOP'
stock_list='PANW,MELI,RACE,CAH,GRMN,BRO,ROKU,AFRM,WING,NEU,AVAV,CDRE,CWCO,AVAH,DERM,CXDO'
stock_list='KGC,KTOS,NET,DCBO,NU,DAKT,DDOG,CRWD,ZS,NOW,SKWD,GLOB,VRNS'
stock_list='INTU,MELI,CDNS,WDAY,DLR,PINS,BR,AKAM,FFIV,GWRE,RBC,INFA,QLYS,BRZE,STNE,VRNS,VERX,RPD,LRN,ROVR,SEMR'
stock_list='CRM,EQIX,WDAY,PH,APH,CRH,COR,CNC,IT,URI,WAB,IRM,PTC,WRB,IOT,LDOS,PATH,ESTC,STN'
stock_list='CYBR,APG,WIX,BRZE,STNE'
stock_list='COST,DHI,LEN,FERG,FAST,IT,PHM,PTC,HII,STN,COKE,CERE,MTH,PCVX,KRC,KBH,NUVL,FSS,ACLX,CBAY,AFYA,MBIN,RXST,HCI,MBWM,FUSN,SUPV,SMLR,SGC,SMID'
stock_list='FI,ANET,TT,DHI,LEN,FERG,RCL,IR,DB,NVR,PHM,PTC,VRT,WSO,AER,NTNX,BLD,ITT,SKX,SSD,CNM,OBDC,NEU,CADE,IBP,BLKB,KBH,FSS,FTAI,HLNE,MHO,OFG,MBIN,WINA,IRON,SRRK,RXST,ASPN,QCRH,GRC,HOV,BITF,GNE,AAOI'
with open('data/stock_list.txt','w') as f:
    f.write(stock_list)
    # f.write('wow')    
    
#%%
import a18_startup_news
print(' done 14212')
#%%
import a11_2_wsj_make_videos
print(' done 321')
#%%
import a13_2_tradingview_screenshot
print(' done 1')


#%%
import a13_3_2_save_audio_only_no_talk
print('herer 2')
#%%
import a13_4_save_videos
print('herer 13  4')
#%%
import a13_5_combine_and_upload
print('here 13 5')

#%%

#%%
#%%
# from datetime import datetime,timedelta
# import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
# import numpy as np
# import pandas as pd
# from pytz import timezone
# import matplotlib.pyplot as plt



# to_folder=f'/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/news_video/'
# filepath=os.listdir('data/youtube2')
# item=sorted(filepath)[-1]
# from_folder='data/youtube2/'
# import shutil

# # from_folder='/Volumes/A1/2_ibkr/19_data_collection/7_dz/1_sql_cleanup/2_y/'
# # to_folder='/Users/{getpass.getuser()}/Library/CloudStorage/GoogleDrive-ryan.ichun9@gmail.com/My Drive/ibkr/9 practicce/feature1/7_dz/1_sql_cleanup/2_y/'

# shutil.copy(from_folder+item, to_folder+item)
#%%


timedelta1=0
timedelta2=100
today1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1)).strftime("%Y-%m-%d"))
today2=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta1))).timestamp()
past1=((datetime.now(timezone('US/Eastern'))-timedelta(timedelta2)).strftime("%Y-%m-%d"))
past2=datetime.strptime('20210218', "%Y%m%d").timestamp()

# youtube_upload(video_title='news '+today1,description='news '+today1)
#%%
youtube_upload_folder('data/youtube2/')
#%%
remove_files('data/youtube1')
remove_files('data/youtube2')
remove_files('data/youtube3')
# %%
