#%%
from import_stocks import *
# %%
driver = open_driver()
# %%

tickers=read_stock_list()
#%%
ticker=tickers[1]
company_name=generate_company_name(ticker)
print("company_name: ",company_name)
print("ticker: ",ticker)
#%%
# if 'Class A' in company_name:
#     company_name=company_name.split(' Class A')[0]
company_name=company_name.replace('Class A','')
company_name=company_name.replace('Common Stock','')
print("company_name: ",company_name)
#%%
news_list=[]
#%%
question_list=[f'{company_name} is about what?',
f'which industry is {company_name} in ?',
f'who are competitors of {company_name}?']


search=f'what is the product name of {company_name}'
url=f'https://www.google.com/search?q={search}'
driver.get(url)
ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
answers=''
for item in ulist:
    answers=answers+item.text
print("answers: ",answers)
if len(answers)==0:
    print('more')
    answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    print("answers: ",answers)
QnA=search +"?  " + answers
answers2=copy.deepcopy(answers)
print("QnA: ",QnA)
news_list.append(QnA)
#%%


search=f'what do they sell from {company_name}'
url=f'https://www.google.com/search?q={search}'
driver.get(url)
ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
answers=''
for item in ulist:
    answers=answers+item.text
print("answers: ",answers)
if len(answers)==0:
    print('more')
    answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    print("answers: ",answers)
QnA=search +"?  " + answers
print("QnA: ",QnA)
news_list.append(QnA)
#%%
# QnA=search +" " + answers
# news_list.append(QnA)
#%%
per,mc,div,company_description=yahoo_company(ticker)
company_description
#%%
#%%
productname_element=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
productname_element
# model_name='gpt-4-0613'
# response=functional_enum(productname_element+company_description,f'what is product or services',f'ex. Iphone16, Amazon Prime Membership',None,model_name=model_name)
# response
# #%%
# response.choices[0].message
# #%%
# product_name=json.loads(response.choices[0].message.function_call.arguments)['search_term']
# product_name
# content=product_name
# content
# #%%
content=company_description+productname_element
define=f'what is name of product of company {company_name}. write less than 10 words answer'
product_name=gpt_answer(content,define)
product_name
# yesorno=functional_enum(content,'do you think this name is name of a product?','return yes or no',enums=['yes','no'],model_name=model_name)
# yesorno=json.loads(yesorno.choices[0].message.function_call.arguments)['search_term']
# yesorno

#%%

if len(product_name)==0 or company_name in product_name or 'investor' in product_name or 'sorry' in product_name.lower() or 'not' in product_name.lower():
    product_name='product'
print("product_name: ",product_name)
#%%

search=f'what does {product_name} from {company_name} do'
url=f'https://www.google.com/search?q={search}'
driver.get(url)
ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
answers=''
for item in ulist:
    answers=answers+item.text
print("answers: ",answers)
if len(answers)==0:
    print('more')
    answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    print("answers: ",answers)
QnA=search +"?  " + answers
print("QnA: ",QnA)
news_list.append(QnA)



#%%
search=f'why {product_name} of {company_name} so special'
url=f'https://www.google.com/search?q={search}'
driver.get(url)
ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
answers=''
for item in ulist:
    answers=answers+item.text
print("answers: ",answers)
if len(answers)==0:
    print('more')
    answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    print("answers: ",answers)
QnA=search +"?  " + answers
print("QnA: ",QnA)
news_list.append(QnA)
#%%
search=f'review of {product_name} of {company_name}'
url=f'https://www.google.com/search?q={search}'
driver.get(url)
ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
answers=''
for item in ulist:
    answers=answers+item.text
print("answers: ",answers)
if len(answers)==0:
    print('more')
    answers=driver.find_element(By.XPATH,'//div[@class="kb0PBd cvP2Ce"]').text
    print("answers: ",answers)

QnA=search +"?  " + answers
print("QnA: ",QnA)
news_list.append(QnA)
#%%

#%%
for search in question_list:
    url=f'https://www.google.com/search?q={search}'
    driver.get(url)
    ulist=driver.find_elements(By.XPATH,'//span[@class="hgKElc"]')
    answers=''
    for item in ulist:
        print(item.text)
        answers=answers+item.text

    QnA=search +" " + answers
    QnA

    news_list.append(QnA)
# %%
QnA
# %%
total_news=''
tickerdot = '.'.join(ticker[i] for i in range(len(ticker)))
tickerdot
#%%
item
#%%
for item in news_list:
    new_sentence=item.replace(company_name,f"{company_name} (ticker. {tickerdot}.)")
    total_news=total_news+new_sentence
total_news
#%%

# %%
print("\n>> len(total_news)= ", len(total_news))
#%%
answer3=gpt_answer(total_news,f"summarize in great details in question and answer format. and mention the company name '{company_name}' as '{tickerdot}' ")
answer3
print("\n>> len(answer3)= ", len(answer3))
#%%
answer3
# %%
timestamp1=str(int(datetime.now().timestamp()))
name_prefix=timestamp1
content=answer3
audio_download_v2(folder=ticker,name_prefix=name_prefix,input1=content,role='man2')
# %%

answer3
# %%
print("\n>> len(total_news)= ", len(total_news))

# %%
answer4=total_news.replace('\n','')
# %%
