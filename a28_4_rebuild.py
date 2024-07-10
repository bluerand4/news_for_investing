#%%

from import_all import *

from selenium import webdriver
from PIL import Image
# import pytesseract
#%%
list1=base_list_read('tradingview_screenshot_stocks')
list1
#%%
len(list1)
#%%


#%%
# Setup WebDriver (make sure chromedriver is in your PATH)
driver = open_driver_loop()
#%%

mongo_collection_names('stock')
#%%
ticker='AAPL'
dt=mongo_get_df('stock','comparison')
dt
#%%
#%%
# def run(ticker):

#%%
ds=mongo_get_df('stock','tradingview_slope')
ds
#%%

tickers=dt['ticker'].values.tolist()
len(tickers)
filename='tradingview_screenshot_stocks'

# tickers=list_read('tradingview','screenshot_list_US')
#%%
len(tickers)
#%%

#%%
target_column='ticker'
total_list=tickers

undone_items=[]
do_list=ds[target_column].values.tolist()
undone_items=list_minus(total_list,do_list)
print("\n>> len(undone_items)= ", len(undone_items))
print("\n>> len(total_list)= ", len(total_list))
undone_items

#%%
done_stocks=os.listdir('data/crops')
done_stocks
done_=[]
for item in done_stocks:
    stock=item.split('_')[0]
    done_.append(stock)
done_
#%%

done_=list(set(done_))
done_
#%%
undone_items=list_minus(total_list,done_)
print("\n>> len(undone_items)= ", len(undone_items))
print("\n>> len(total_list)= ", len(total_list))
print("\n>> len(done_)= ", len(done_))

#%%

def run(ticker):

    print("ticker: ",ticker)

    exchange=find_exchange_v2(ticker)
    exchange

    driver.get(f'https://www.tradingview.com/chart/q0QCLsTJ/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located
    


    try:
        time.sleep(3)
        alert = driver.switch_to.alert
        alert.accept()

        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    time.sleep(20)
    # Locate the canvas element
    canvas = driver.find_elements(By.TAG_NAME,'canvas')
    canvas
    canvase=driver.find_elements(By.XPATH,'//canvas[@aria-hidden="true"]')

    pt.moveTo(124,153)

    time.sleep(1)
    canvas=canvase[5]

    # Get the location and size of the canvas element
    location = canvas.location
    size = canvas.size

    # Take a screenshot of the entire page
    driver.save_screenshot('data/page_image.png')

    # Open the screenshot and crop it to the canvas area
    # x, y = location['x'], location['y']+500

    row=[]
    row.append(ticker)


    HOW_MANY=27
    # list1=[(56,404+365*0),(56,404+365*1),(56,404+365*2),(56,404+365*3),(56,404+365*4),(56,404+365*5)]
    list1=[]
    HORI=430
    VERTI=115
    BLOCK=90
    width=2640
    height=20
    node1=0
    node2=0
    node3=1450
    node4=75
    for how_i in range(HOW_MANY):
        list1.append((HORI,VERTI+BLOCK*how_i))
    print("list1: ",list1)


    i=0
    for i in range(len(list1)):
        x,y=list1[i]

        # x, y = location['x'], location['y']

        # width, height = size['width'], size['height']
        
        image = Image.open('data/page_image.png')
        canvas_image = image.crop((x+node1, y+node2, x + width+node3, y + height+node4))
        # canvas_image = image.crop((x, y, x + width+1400, y + height+120))
        canvas_image.save(f'data/crops/{ticker}_{i}.png')
        # canvas_image.show()

        

for ticker in undone_items:
    try:
        print('''> try: run(ticker)''',datetime.now())
        run(ticker)
    except Exception as e:
        print('''>> error: run(ticker): ''',e,datetime.now())

    # canvas_image.show()

        
# %%
