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

#%%


print("ticker: ",ticker)

exchange=find_exchange_v2(ticker)
exchange
#%%
driver.get(f'https://www.tradingview.com/chart/q0QCLsTJ/?symbol={exchange}%3A{ticker}')  # URL where the canvas is located
time.sleep(10)

#%%
button=driver.find_element(By.XPATH,'//button[@class="button-vll9ujXF button-KSzJG6_A"]')
#%%
if 'dropped' in button.find_element(By.TAG_NAME,'span').get_attribute('class'):
    print('down now')
else:
    button.click()
    print('up now')
time.sleep(1)
#%%
titles=driver.find_elements(By.XPATH,'//span[@class="title-cXDWtdxq itemTitle-KSzJG6_A"]')
infos=driver.find_elements(By.XPATH,'//span[@class="data-cXDWtdxq"]')
#%%
dict1={}
dict1['ticker']=ticker
for title,item in zip(titles,infos):
    title=title.text
    item=item.text
    if item.endswith('B'):
        item=item.replace('B','')
        item=float(item)
        item=item*1000000
    elif item.endswith('M'):
        item=item.replace('M','')
        item=float(item)
        item=item*1000
    elif item.endswith('T'):
        item=item.replace('T','')
        item=float(item)
        item=item*1000000000
    elif item.endswith('K'):
        item=item.replace('K','')
        item=float(item)
        
    elif item.endswith('%'):
        item=item.replace('%','')
        item=float(item)
    
    else:
        try:
            item=float(item)
        except:
            item=float(0)
    dict1[title]=item
    
    print("item: ",title,item)
dict1
#%%



dd=pd.DataFrame.from_dict(dict1,orient='index').T
dd
#%%

# Locate the canvas element
canvas = driver.find_elements(By.TAG_NAME,'canvas')
canvas
canvase=driver.find_elements(By.XPATH,'//canvas[@aria-hidden="true"]')
#%%
pt.moveTo(60,200)
time.sleep(1)
canvas=canvase[5]

# Get the location and size of the canvas element
location = canvas.location
size = canvas.size

# Take a screenshot of the entire page
driver.save_screenshot('data/page_image.png')
#%%
# Open the screenshot and crop it to the canvas area
# x, y = location['x'], location['y']+500

row=[]
row.append(ticker)


HOW_MANY=27
# list1=[(56,404+365*0),(56,404+365*1),(56,404+365*2),(56,404+365*3),(56,404+365*4),(56,404+365*5)]
list1=[]
HORI=250
VERTI=115
BLOCK=90
width=2640
height=20
node1=0
node2=0
node3=1650
node4=75
for how_i in range(HOW_MANY):
    list1.append((HORI,VERTI+BLOCK*how_i))
print("list1: ",list1)


i=0
for i in range(len(list1))[:]:
    x,y=list1[i]

    # x, y = location['x'], location['y']

    # width, height = size['width'], size['height']
    
    image = Image.open('data/page_image.png')
    canvas_image = image.crop((x+node1, y+node2, x + width+node3, y + height+node4))
    # canvas_image = image.crop((x, y, x + width+1400, y + height+120))
    canvas_image.save(f'data/canvas_image_{i}.png')
    # canvas_image.show()

    

canvas_image.show()
#%%
    
#%%

for i in range(len(list1)):
    x,y=list1[i]

    # x, y = location['x'], location['y']

    # width, height = size['width'], size['height']
    
    image = Image.open('data/page_image.png')
    canvas_image = image.crop((x+node1, y+node2, x + width+node3, y + height+node4))
    # canvas_image = image.crop((x, y, x + width+1400, y + height+120))
    canvas_image.save('data/canvas_image.png')
    # canvas_image.show()

    size


    # Clean up
    




    # def detect_text(path):

    """Detects text in the file."""
    path='data/canvas_image.png'
    total_text=image2text(path)


    total_text=total_text.split('\n')
    print("total_text: ",total_text)
    
    
    try:
        numbers=[]
        for text in total_text:
            # text=item.description
            print("text: ",text)
            # print(f'\n"{item.description}"')
            if text.startswith('$') and text:
                print("text: ",text)
                # found_numbers = re.findall(r'\d+\.\d+', text)
                found_numbers = re.findall(r'-?\d+\.\d+', text)
                print("found_numbers: ",found_numbers)
                if found_numbers == '' or found_numbers==None or len(found_numbers)==0:
                    found_numbers='0'
                if text.endswith('B'):
                    found_numbers=float(found_numbers[0])*1000000
                elif text.endswith('M'):
                    found_numbers=float(found_numbers[0])*1000
                numbers.append(found_numbers)
        numbers
    except:
        numbers=[]
        define='''reformat each element so that the list looks like "['$10.516B', '$7.796B', '$9.014B', '$17.891B',...]"'''
        for _ in range(3):
            try:
                print('''> try: summary=gpt_answer_v2(str(total_text),define)''',datetime.now())
                summary=gpt_answer_v2(str(total_text),define)
                
                summary
                list2=ast.literal_eval(summary)
                list2
                for text in list2:
                    # found_numbers = re.findall(r'\d+\.\d+', text)
                    found_numbers = re.findall(r'-?\d+\.\d+', text)

                    if found_numbers == '' or found_numbers==None or len(found_numbers)==0:
                        found_numbers='0'
                    print("found_numbers: ",found_numbers)
                    if text.endswith('B'):
                        
                        found_numbers=float(found_numbers[0])*1000000
                    elif text.endswith('M'):
                        found_numbers=float(found_numbers[0])*1000
                    numbers.append(found_numbers)
                break
            except Exception as e:
                time.sleep(1)
                print('''>> error: summary=gpt_answer_v2(str(total_text),define): ''',e,datetime.now())

    row.append(str(numbers))

row[1:] 

slopes1=[]
slopes1.append(ticker)
for numbers in row[1:]:
    numbers=ast.literal_eval(numbers)
    # numbers=[float(item[0]) for item in numbers if isinstance(item, list) elif isinstance(obj, float) item]
    
    
    try:
        print('''> try: slope1,intercept=regression(numbers)''',datetime.now())
        numbers = [float(item[0]) if isinstance(item, list) else float(item) for item in numbers]
        slope1,intercept=regression(numbers,normalize=True)
    except Exception as e:
        slope1=0
        print('''>> error: slope1,intercept=regression(numbers): ''',e,datetime.now())

    slope1=slope1*1000
    slope1=round(slope1,2)
    slopes1.append(slope1)
    slopes1.append(str(numbers))
for numbers in row[1:]:
    numbers=ast.literal_eval(numbers)
    try:
        numbers = [float(item[0]) if isinstance(item, list) else float(item) for item in numbers]
        print('''> try: slope1,intercept=regression(numbers[-8:])''',datetime.now())
        slope1,intercept=regression(numbers[-8:],normalize=True)
    except Exception as e:
        print('''>> error: slope1,intercept=regression(numbers[-8:]): ''',e,datetime.now())
        slope1=0
    slope1=slope1*1000
    slope1=round(slope1,2)
    slopes1.append(slope1)
slopes1
print("slopes1: ",slopes1) 

numbers=row[1]
numbers=ast.literal_eval(numbers)
numbers

dn=pd.DataFrame(slopes1).T
dn#%

dn.columns=['ticker','revenue1','revenue','gross_profit1','gross_profit','net_income1','net_income','dividend1','dividend','fcf1','fcf','cogs1','cogs','revenue2','gross_profit2','net_income2','dividend2','fcf2,','cogs2']
print("dn: ",dn)

dn=dd.merge(dn,how='outer',on='ticker')

# mongo_insert(dn,'ticker','stock','tradingview_slope')
mongo_update_insert_one('stock','tradingview_slope',dn,'ticker')
#%%
for ticker in undone_items:
    if 1600<int(datetime.strftime(datetime.now(timezone('US/Eastern')) ,"%H%M"))<2000 :
        pass
    else:
        try:
            print('''> try: run(ticker)''',datetime.now())
            run(ticker)
        except Exception as e:
            time.sleep(30)
            print('''>> error: run(ticker): ''',e,datetime.now())

# %%
# mongo_set_df('stock','tradingview_slope','ticker',dn)
#%%
#%%
print("\n>> len(tickers)= ", len(tickers))

# %%

ds=mongo_get_df('stock','tradingview_slope')
ds

# %%


ds2=ds[['ticker','revenue1','revenue2','net_income1','net_income2']]
ds2 = ds2[ds2['revenue1'] >= 30]
ds2 = ds2[ds2['revenue2'] >= 30]
ds2 = ds2[ds2['net_income1'] >= 30]
ds2 = ds2[ds2['net_income2'] >= 30]
ds2=ds2.sort_values(by='revenue2',ascending=False)
ds2[:20]
# %%
ticker='AAPL'
endpoint=f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={polygon_api_key}'
response = requests.get(endpoint)
# Raise an error if the request failed
response.raise_for_status()
# Parse the JSON result
data = response.json()

json_data=data['results']

new_row = pd.DataFrame(json_data, index=[0])
new_row['primary_exchange']
# %%
new_row.columns
# %%
find_exchange_v2('AIRI')
# %%
