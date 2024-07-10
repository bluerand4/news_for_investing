#%%
from import_stocks2 import *
# generate_tradingview_audio()
generate_tradingview_video()
combine_video('stocks_news_')
youtube_upload_and_remove()
#%%
while True:
    time.sleep(5)
    bool_news_generate=check_mongo_new_tickers()
    bool_news_generate


    if bool_news_generate:
        print('start bool news')
        generate_tradingview_screenshots()
        generate_tradingview_audio()
        generate_tradingview_video()
        combine_video('stocks_news_')
        youtube_upload_and_remove()
        print('done')
    else:
        print('none')

# %%
print('done')
# %%
