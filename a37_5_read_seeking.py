#%%
from import_basics import *
# import textwrap
from import_mongo import * 

'''

pip install --upgrade undetected-chromedriver selenium webdriver-manager


'''
driver=open_driver()

driver.get('https://www.seekingalpha.com/')
#%%
sections = driver.find_elements(By.TAG_NAME, 'section')
sections
print("\n>> len(sections)= ", len(sections))

section=sections[0]
text1=section.text

text1=text1.split('This article was written by')[0]


pyperclip.copy(text1+'\n\nsummarize in detail')
# %%

#%%
# get all the news first.
section=driver.find_element(By.XPATH,'//div[@class="col-start-2 col-end-4"]')
section
articles=section.find_elements(By.TAG_NAME,'section')
# articles=section.get_attribute('article')
print("\n>> len(articles)= ", len(articles))
#%%
# all news summarize. can be very long
sections=driver.find_elements(By.XPATH,'//div[@class="flex flex-col flex-wrap print:block"]')
# sections=driver.find_elements(By.XPATH,'//div[@class="pb-24 px-safe-offset-18 md:pb-20 md:px-safe-offset-24"]')

section=sections[0]
articles=section.find_elements(By.TAG_NAME,'article')
# articles=section.get_attribute('article')
print("\n>> len(articles)= ", len(articles))

#%%
# summarize only 10 each
news=[]
iii=0
for iii in range(10):
    article=articles.pop(0)

    news.append(article.text)
    news.append(f'\n\n#{iii}.**summarize above\n\n')
print("\n>> len(articles)= ", len(articles))

news=' '.join(news)
print("\n>> len(news)= ", len(news))
pyperclip.copy(news+'\n\nsummarize in great details')
#%%

# all news summarize. can be very long
sections=driver.find_elements(By.XPATH,'//div[@class="flex flex-col flex-wrap print:block"]')
# sections=driver.find_elements(By.XPATH,'//div[@class="pb-24 px-safe-offset-18 md:pb-20 md:px-safe-offset-24"]')

section=sections[0]
articles=section.find_elements(By.TAG_NAME,'article')
# articles=section.get_attribute('article')
print("\n>> len(articles)= ", len(articles))

news=[]
iii=0
for iii in range(len(articles)):
    article=articles[iii]
    news.append(article.text)
    news.append('\n')

news=' '.join(news)
print("\n>> len(news)= ", len(news))

pyperclip.copy(news+'\n\nsummarize in great details')


#%%
news=[]
iii=0
for iii in range(int(len(articles)/2),len(articles)):
    article=articles[iii]
    news.append(article.text)
    news.append('\n')

news=' '.join(news)
print("\n>> len(news)= ", len(news))
pyperclip.copy(news+'\n\nsummarize in great details')
#%%
text1=pyperclip.paste()
print("\n>> len(text1)= ", len(text1))
#%%

text2=text1[15000:25000]
pyperclip.copy(text2 +'\n\nsummarize in detail')
# %%
driver.quit()
# %%
