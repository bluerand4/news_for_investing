from a30_2_save_ohlcv_5000 import *


from a30_3_save_ohlcv_polygon import *

while True:

    save_csv_polygon_1d()

    save_csv_polygon_1m()
    save_csv_daily_tradingview_ohlcv()

    time.sleep(60*60*24)