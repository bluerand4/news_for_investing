#%%
from import_basics import *
from import_stocks2 import *

de=mongo_get_df('stock','polygon_total_stock_info')
de
#%%
stock_list=de[de['type']=='CS']['ticker'].values.tolist()
print("\n>> len(stock_list)= ", len(stock_list))
#%%
de.columns
# %%
de=de.sort_values(by='market_cap',ascending=False)
de=reset_index(de)
de
# %%
stock_list=de[de['type']=='CS']['ticker'].values.tolist()
stock_list
# %%
