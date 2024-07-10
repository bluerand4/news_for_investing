#%%
from import_stocks2 import *
# %%
import boto3
#%%
dc=mongo_get_df('stock','comparison')
dc
# %%
dc.columns
#%%
dc2=dc[['mc','revenue1','industry','ticker','mc_rev','per','sector','inslope','inslope2','revslope','revslope2','month12_1','month12_2','month3_1','month3_2','insider','insider_owned']]
# %%
dc2=dc2.sort_values(by='inslope2',ascending=False)
dc2
# %%
dc2=dc2.sort_values(by='revslope2',ascending=False)
dc2

# %%
dc2=dc2.sort_values(by='revslope2',ascending=False)
dc2
#%%
dc3 = dc2[dc2['inslope2'] >= 30]
dc3 = dc3[dc3['revslope2'] >= 30]
dc3 = dc3[dc3['revslope2'] <= 499]
dc3 = dc3[dc3['inslope2'] <= 499]
# %%
dc3=dc3.sort_values(by='revslope2',ascending=False)
dc3

# %%
dc3=dc3.sort_values(by='inslope2',ascending=False)
dc3

# %%
dc
# %%
