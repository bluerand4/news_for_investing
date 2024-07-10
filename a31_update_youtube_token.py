#%%
from import_all import *

# %%
os.remove('me_token.pickle')
# %%
youtuber = YoutuberDummyParameters()
# %%
youtube = youtuber.YoutubeExtractor(local_api=False)   
# %%
