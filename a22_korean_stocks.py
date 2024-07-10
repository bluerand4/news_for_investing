#%%
from import_korean import *
import pandas as pd
import ccxt
#import ccxtpro
#import asyncio
from datetime import datetime
from copy import deepcopy
import threading
import time
from copy import deepcopy
import numpy as np
import matplotlib_inline
import openpyxl
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import date, timedelta
import requests

name_of_script="a7_upbit_kr"

time_lag = 3600 #3600 = 1 hr
time_lag_historical= 900 # 900 is 15min
#tickers_a2=["DOGE"]

tickers_a2={"WAXP": {"quantity": 1, "currency":"KRW"}
            #"BTC": {"quantity": 0.00001, "currency":"KRW"},
            
            
            #LUNA": {"quantity": 1, "currency":"BTC"}
           
            }
kosdaq=kosdaq_mc_list_500(page_number=60)
#%%

kospi=kospi_mc_list_500(80)

#%%
kospi.extend(kosdaq)
#%%
from import_mongo import *
dn=pd.DataFrame(['247540'])
dn.columns=['ticker']
dn
#%%
mongo_update_insert_one('stock','korean_slope',dn,'ticker')
#%%
dk=mongo_get_df('stock','korean_slope')
dk
#%%
print("\n>> len(kosdaq)= ", len(kosdaq))
print("\n>> len(kospi)= ", len(kospi))
#%%

#%%
kospi
#%%
kosdaq
#%%
# def naver_finance(time3):

invested=50_000

today1=date.today()
today1=today1.strftime('%A')
today1

Date=datetime.now()
T1=str(Date).split(".")[0]
Date=str(Date).split(" ")[0]
T2=T1.split(" ")[0]
T3=T1.split(" ")[1]

#2 

#3 인기검색

url = "https://finance.naver.com/sise/lastsearch2.naver"

payload = ""
headers = {
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; nx_ssl=2; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; naver_stock_codeList=028300%7C096530%7C; page_uid=hQO+SwprvmZssSm9dmwssssssHZ-410937; NID_SES=AAABpvahNico2THI6ZJb0dAnDSq45fliZZh/zv/BDZ6HuAvDns7LxBfFTZOiIGVpzf1vQO2+sJW8EkeKsR3YDOLf4uHofnWS3pb2HlJPmZQUL+207qDnRd72gVXew8BVgqkZf0fPwwRtLKCAnHLwxovqUHIIe1ldwOyOgCml5D5GymhKv8iASoWGfaQ8o5wT11/laVQjbBLLhKHXUj9YWtBhwrw2HfJHezZWsLKDU+FQqcWF5bF2hjh7+jN+WIyxakI3m8lrwXirTiCPfE77d7Y7via9LN+herFKhYIR07dDfhVGR0r0B2zUBNSP4JENhXaUQiIOHHy3xZjLzHRluVpoEmLdTIhveZZNGv8U3OfI/bamz9fBb7BsRVfkvLA63Oxu38DISrQgHJmqmkbd03+CkYy4+On0S58zJxKKeUhL1b0tC6f1XdycpoTp9DU9KlEiI7Qf8izBtrDB/QB1mo1fAMd94TQwwTR7wYTeELzD5fsoKwtKUCr/ODk0gqEIlQqUuRVpILhm6ZHiEOR0F7mW2ko3lOxJNg3G0jGKzH8ny5OH3eCQzmCClTYvNuEE5dtvPA==; JSESSIONID=246FFD1ABA79DD1EDD3319AE8DB61455",
    "authority": "finance.naver.com",
    "cache-control": "max-age=0",
    #"sec-ch-ua": "" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://finance.naver.com/",
    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
}

response = requests.request("GET", url, data=payload, headers=headers)
data=response.text

data2= data.split("hidden name=returnUrl value")[1].split("<div id=")[1]
data3=(data2.split('</a>'))
list1=[]
for item in data3:
    try:
        save1=item.split('tltle">')[1]
        
    except:
        continue
    else:
        list1.append(save1)
list1
#%%
# 2 상한가
url = "https://finance.naver.com/sise/sise_upper.naver"

payload = ""
headers = {
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; nx_ssl=2; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; naver_stock_codeList=028300%7C096530%7C; page_uid=hQO+SwprvmZssSm9dmwssssssHZ-410937; NID_SES=AAABr7eEYjKrz9FesGWSUhCBLQa3UxolTqqWhjlI02lLSCCtDCw5ZQaKr/La6ToOQ1otqw+YLtEVSDf7rCxmk7TR8TeBRYqZUa1vFT6gntu4YyEPwViuE61gDm9fK9f0OfZUE9I/EsHbKEmPMHdpul0VQmpLT9zHYJ6TZ0bR4onrEmAQyg8HvFDktJBOOiA1YOs49tJRzad35znA/DpLLfUS+UR5nG/06MCaPo2siNY3oNAgnOiFRlQ68FGW5vBMoGU9auUYHm4QFFnzi0w+ScvlETzOybnhKSPYdaJuNV3HUcJacnos5aERcEb3nSw3kdrjLXgUtiLHzQHiqFrYac2zTMoFKykBxkv9gdPr2t1LCIjrpPJ3ozvu1IXUd/N7w9jWQ7eeL8+eYzxzqblCwQM++El21D1Ar8wJsHPVya+1WoZQKxfqakmDgBTrRCtvMl766VbxNAqlAT3U7QClXIZfWIfy/obfMIKHk2GnF/8P/Qr/yKVvvfF84MGfCVS2x43WYc5h8ngIYL78vbsQuf2tDEw+CNssiuXCzyDJ6mbsR6G8IH0+WoWW7HMK4wHvyPD1sQ==; JSESSIONID=FC51FE7EB831043B131ECC5F0083134A",
    "authority": "finance.naver.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    #"sec-ch-ua": "" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "referer": "https://finance.naver.com/sise/sise_rise.naver?sosok=1",
    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
}

response = requests.request("GET", url, data=payload, headers=headers)

data=response.text

data2=data.split("/item/main.naver?code=")
list2=[]
for item in data2[1:]:
    try:
        data3=item.split("</a></td>")
    except:
        pass
    else:
        list2.append(data3[0].split('">'))

#3 상승

url = "https://finance.naver.com/sise/sise_rise.naver"

querystring = {"sosok":"1"}

payload = ""
headers = {
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; nx_ssl=2; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; naver_stock_codeList=028300%7C096530%7C; page_uid=hQO+SwprvmZssSm9dmwssssssHZ-410937; NID_SES=AAABroDy3uKzIdIYj3/zMeS1bERSbB/EUMXARmrHyNYVCOz7WiRQP9JQTDhbW3TsP68vOEuuIbaOUdKZax1rFpbtFJLtDcDu067UyYYHJ790syGJOrrpVPCTi3srXCW916UiFzF6AlfpbQdADHw6vjdFxpRQMMmZ4ir8ihpbJICJ+Vko/zqZH3GoEYkV13HhLQcRDN/Jj5Rl9hPw2JObSfWuqNqfhYGEdfMgveiHfTEGBm/pBDSI8f7Obh/oPkUHc6tJstTVC5NtXH8xmJUg/tEtIpi1qrzJ1G5lByzd/Rlafu5ffuguuN8X9/C2eFsPlsyXWosOFYuFEm1rHc660zIGMeSP/cUjAD7hJId0l+3b3+zgd3hlzpxXU3u7Tq4waVxaNIP8RMdTlvrzHbEDseFfNO9a0D3N+73d7jTo7TPJhMx9VVMYoAtHwn7zpyz/RyS6rQDENmFcNMbvVaa3T20Wet13wJed5LPisPcqhm1q2iTdJfRR07s5iN0MOOPDGYu7bG2hIgUWzYVEiW6zLoTeBDnI44xAo0vpgnM9/Yd/8A5p/KkBFQUZdtX0TlporClHJQ==; JSESSIONID=A705F7C71BE4C3BA1A07637D04254CE3",
    "authority": "finance.naver.com",
    #"sec-ch-ua": "" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://finance.naver.com/sise/sise_rise.naver",
    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data=response.text
data2=data.split("/item/main.naver?code=")
list3=[]
for item in data2[1:]:
    try:
        data3=item.split("</a></td>")
    except:
        pass
    else:
        data4=data3[0].split('">')
        data5=data4[0].split('"')[0]
        list3.append((data5,data4[1]))

#4 외국인 순매수 상위

url = "https://finance.naver.com/sise/sise_deal_rank_iframe.naver"

querystring = {"sosok":"01","investor_gubun":"9000","type":"buy"}

payload = ""
headers = {
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; nx_ssl=2; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; naver_stock_codeList=028300%7C096530%7C; page_uid=hQO+SwprvmZssSm9dmwssssssHZ-410937; NID_SES=AAABqHAkZ1mlZHsS3d9xVdbrtuD5bhsMouHADOxJRYgYB9Gnexm4kpf7P889tRZJPbJhoweIessGw2Et4HsxB3lXtiTlu51vOAkJ/hg+8OE839+saMibir2O5yx2LNLW3rHi5HK+Qf1crFklsqjjDNMuazkMbcfU2Ny+29kLUWiA/L56cJPsS0RZqbD0IIaZ5Txyi92OZ5VMqJ+eIQysJr+J+I3gnoP57xYHutzdYxOFis5N10qvxvO84+OqyK2ud4tUMyLb5ijC2WsKhJ+sWl0zxDgwSwccwLwF7e87Zlpirrhp/nUI16qvAyu+FHTe8G9R7YRROmieOh0A958E1dF+Q/2oddcIb7fUJ+4BtUrVQb1bzwu2D8YaEVJcy7dJmd0/DQ+mMeDRrmuo4EjHHOn9tOEBAjTd/0aXos04UiFJPsmxUQM7D9AmX6LjZKdLAQhEIcwJCauho4BLafI++To95V+5z2HyLaaZh9+p+rcoROZoUq80X5z510xgJvdA6U6lc5ZqwC9th+2KcTQxpArOmCn2u9g7lGPalr04t52H5U6Ck5UlTS0/pRIs6edKHS81XQ==; JSESSIONID=C853571E610AA68421A79B0730FB19B9",
    "authority": "finance.naver.com",
    #"sec-ch-ua": "" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "iframe",
    "referer": "https://finance.naver.com/sise/sise_deal_rank.naver?sosok=01&investor_gubun=9000",
    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data=response.text
data2=data.split('/item/main.naver?code=')[1:]
list4=[]
for item in data2:
    try:
        data3=item.split("</a></p></td>")
    except:
        pass
    else:
        data4=data3[0].split('"')[0]
        data5=data3[0].split(">")[1]
        list4.append((data4,data5))
#%%
# 10 export
#%%
#%%
# else:
# print("b8 naver finance-time not passed")

#%%
        # %%

        # %%
# naver_finance(0)
# %%
# %%


kosdaq_list=kosdaq_mc_list_500()
print("\n>> len(kosdaq_list)= ", len(kosdaq_list))


#%%

kospi_list=kospi_mc_list_500()

#%%print("\n>> len(kospi_list)= ", len(kospi_list))
print("\n>> len(kospi_list)= ", len(kospi_list))


#%%
ticker=kospi_list[2][0]
ticker
#%%
def kosdaq_historical_datalist(kosdaq_mc_list):
    for i in range(1,510):
        ticker=kosdaq_mc_list[i][2]

        list3=[]

        pagenumber1_list=5
        for pagenumber1 in range(1, pagenumber1_list):
            
            try:
                name1=ticker.split("_")[0]
                url = "https://finance.naver.com/item/sise_day.naver"

                querystring = {"code":"{}".format(ticker.split("_")[1]),"page":"{}".format(pagenumber1)}

                payload = ""
                headers = {
                    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; nx_ssl=2; page_uid=hlojslp0J1sssCXP+shssssssrd-315361; naver_stock_codeList=053050%7C066570%7C056090%7C218150%7C004105%7C004100%7C169330%7C005930%7C028300%7C096530%7C; NID_SES=AAABrFnq6ZE6kMRdmeRCnpUa0HQafTxUMto7pa0CKatJwsWS+p26D8A0o3ZGCKM2zERdPsfqAI2b6Lw0zyfTmphCC/qdRAjnPV2joantnFUoSDv+uEfmjvC8uWUIqUB3kjfp/GIihmDaQNBhcXZD2dcJ6CN10XS2DaS7ntbEDfq68d2MU8IMtL394CrFW7C+eGg2LSnB5Ly0DbeusRXtQlv1DLpsM017Xdf2/kXIVngle5og3lhVoggjUIqbGIQL3xXqJYyKboyYIhYppO8dboJz+4i8cAOUhWXU4nd3D3QAB7TBtGN9wkp841FX+A0RbIgxZ+qUHFs7d2h7mYd8macZYsESofRPF/Vd86pB4JsDNVPPOrKRNcyPXNSNCqmpxcoH1j2v9ZBFR5Ast8xbeQ7kcZJwSgFAKX+1k4obAqrnmugz9pNBEFaCGJI0AKYDtOhLXXkUjv9aXy8fjHA8MQOMOa63soBlxc4DyCtS7qG9uealqpnd16bgpjKtGcFtaeXAyMorkh8COTh7/QCgHgO9PSojG0NyG5y4Zh0celn5I3+TPcWJYSGK8LYsqeXW3aljFQ==; JSESSIONID=32A4B119EE5B0ABC94B5DF8FA36557FF",
                    "authority": "finance.naver.com",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "macOS",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "iframe",
                    "referer": "https://finance.naver.com/item/sise_day.naver?code=053050",
                    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
                }

                response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
                data=response.text
                eachrow=data.split('<span class="tah p10 gray03">')[1:]
                for each in eachrow:
                    date=each.split("</span>")[0]
                    data5=each.split('num"><span class="tah p11">')
                    # for item in data5:
                    #     if "</span>\n\t\t\t</td>" in item:
                    #         print(item)
                    #         data5.remove(item)

                    # print(data2)
                    date=data5[0].split("</span></td>")[0].replace(".","")
                    close=int(data5[1].split("</span></td>")[0].replace(",",""))    
                    open=int(data5[2].split("</span></td>")[0].replace(",",""))        
                    high=int(data5[3].split("</span></td>")[0].replace(",",""))
                    low=int(data5[4].split("</span></td>")[0].replace(",",""))
                    volume=int(data5[5].split("</span></td>")[0].replace(",",""))

                    list3.append((date,close,open,high,low,volume))
            except:
                pass

        list4=list(dict.fromkeys(list3))

    return list4

list4=kosdaq_historical_datalist(kospi_list)
list4
#%%
print("\n>> len(list4)= ", len(list4[0]))

#%%

#%%
def kospi_list_get_historical_data_naver():
    for i in range(len(kospi_mc_list)):
        list3=[]
        ticker=kospi_mc_list[i]

        pagenumber1_list=5
        for pagenumber1 in range(1, pagenumber1_list):
            
            try:
                name1=ticker.split("_")[0]
                url = "https://finance.naver.com/item/sise_day.naver"

                querystring = {"code":"{}".format(ticker.split("_")[1]),"page":"{}".format(pagenumber1)}

                payload = ""
                headers = {
                    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; nx_ssl=2; page_uid=hlojslp0J1sssCXP+shssssssrd-315361; naver_stock_codeList=053050%7C066570%7C056090%7C218150%7C004105%7C004100%7C169330%7C005930%7C028300%7C096530%7C; NID_SES=AAABrFnq6ZE6kMRdmeRCnpUa0HQafTxUMto7pa0CKatJwsWS+p26D8A0o3ZGCKM2zERdPsfqAI2b6Lw0zyfTmphCC/qdRAjnPV2joantnFUoSDv+uEfmjvC8uWUIqUB3kjfp/GIihmDaQNBhcXZD2dcJ6CN10XS2DaS7ntbEDfq68d2MU8IMtL394CrFW7C+eGg2LSnB5Ly0DbeusRXtQlv1DLpsM017Xdf2/kXIVngle5og3lhVoggjUIqbGIQL3xXqJYyKboyYIhYppO8dboJz+4i8cAOUhWXU4nd3D3QAB7TBtGN9wkp841FX+A0RbIgxZ+qUHFs7d2h7mYd8macZYsESofRPF/Vd86pB4JsDNVPPOrKRNcyPXNSNCqmpxcoH1j2v9ZBFR5Ast8xbeQ7kcZJwSgFAKX+1k4obAqrnmugz9pNBEFaCGJI0AKYDtOhLXXkUjv9aXy8fjHA8MQOMOa63soBlxc4DyCtS7qG9uealqpnd16bgpjKtGcFtaeXAyMorkh8COTh7/QCgHgO9PSojG0NyG5y4Zh0celn5I3+TPcWJYSGK8LYsqeXW3aljFQ==; JSESSIONID=32A4B119EE5B0ABC94B5DF8FA36557FF",
                    "authority": "finance.naver.com",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "macOS",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "iframe",
                    "referer": "https://finance.naver.com/item/sise_day.naver?code=053050",
                    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
                }

                response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
                data=response.text
                eachrow=data.split('<span class="tah p10 gray03">')[1:]
                for each in eachrow:
                    date=each.split("</span>")[0]
                    data5=each.split('num"><span class="tah p11">')
                    # for item in data5:
                    #     if "</span>\n\t\t\t</td>" in item:
                    #         print(item)
                    #         data5.remove(item)

                    for data2 in data5:
                        # print(data2)
                        date=data5[0].split("</span></td>")[0].replace(".","")
                        close=int(data5[1].split("</span></td>")[0].replace(",",""))    
                        open=int(data5[2].split("</span></td>")[0].replace(",",""))        
                        high=int(data5[3].split("</span></td>")[0].replace(",",""))
                        low=int(data5[4].split("</span></td>")[0].replace(",",""))
                        volume=int(data5[5].split("</span></td>")[0].replace(",",""))

                        list3.append((date,close,open,high,low,volume))
            except:
                pass
        list4=list(dict.fromkeys(list3))

        try:
            df2=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(ticker),index_col=0)
            #df2=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/temp/{}_v1.xlsx".format(ticker),index_col=0)
        except:
            df1=pd.DataFrame(list4)
            df=df1.rename(columns={0:"Date",1:"Close",2:"Open",3:"High",4:"Low",5:"Volume"})
            df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
            df=df.sort_values(by="Date")
            df=df.reset_index()
            df1=df.drop(columns=["index"])
            df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(ticker))
            #df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/temp/{}_v1.xlsx".format(ticker))
        else:
            df1=pd.DataFrame(list4)
            df=df1.rename(columns={0:"Date",1:"Close",2:"Open",3:"High",4:"Low",5:"Volume"})
            df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
            df=df.sort_values(by="Date")
            df=df.reset_index()
            df1=df.drop(columns=["index"])
            df1=df2.append(df1)
            df1=df1.drop_duplicates(["Date"],keep="last")
            df=df1.reset_index()
            df1=df.drop(columns=["index"])
            df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(ticker))



#%%
#kospi_list_get_historical_data_naver()




#%%
import pandas as pd
kospi_mc_list_1000=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/3 kospi kosdaq list/mc_kospi_list_v2.xlsx",index_col=0)
kospi_mc_list_1000=kospi_mc_list_1000[0:500]
kospi_mc_list_1000
kospi_mc_list=kospi_mc_list_1000[2].to_list()
len(kospi_mc_list)
# %%

#%%
def kospi_historical_single_stock(ticker):
    
    
    
    kospi_mc_list_1000=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/3 kospi kosdaq list/mc_kospi_list_v2.xlsx",index_col=0)
    kospi_mc_list_1000=kospi_mc_list_1000[0:500]
    kospi_mc_list_1000
    kospi_mc_list=kospi_mc_list_1000[2].to_list()
    len(kospi_mc_list)
    code1=kospi_mc_list_1000[kospi_mc_list_1000[0]==ticker][1].values[0]
    nameandcode="{}_{}".format(ticker,code1)


    list3=[]

    pagenumber1_list=10
    for pagenumber1 in range(1, pagenumber1_list):
        
        try:
            url = "https://finance.naver.com/item/sise_day.naver"

            querystring = {"code":"{}".format(code1),"page":"{}".format(pagenumber1)}

            payload = ""
            headers = {
                "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; nx_ssl=2; page_uid=hlojslp0J1sssCXP+shssssssrd-315361; naver_stock_codeList=053050%7C066570%7C056090%7C218150%7C004105%7C004100%7C169330%7C005930%7C028300%7C096530%7C; NID_SES=AAABrFnq6ZE6kMRdmeRCnpUa0HQafTxUMto7pa0CKatJwsWS+p26D8A0o3ZGCKM2zERdPsfqAI2b6Lw0zyfTmphCC/qdRAjnPV2joantnFUoSDv+uEfmjvC8uWUIqUB3kjfp/GIihmDaQNBhcXZD2dcJ6CN10XS2DaS7ntbEDfq68d2MU8IMtL394CrFW7C+eGg2LSnB5Ly0DbeusRXtQlv1DLpsM017Xdf2/kXIVngle5og3lhVoggjUIqbGIQL3xXqJYyKboyYIhYppO8dboJz+4i8cAOUhWXU4nd3D3QAB7TBtGN9wkp841FX+A0RbIgxZ+qUHFs7d2h7mYd8macZYsESofRPF/Vd86pB4JsDNVPPOrKRNcyPXNSNCqmpxcoH1j2v9ZBFR5Ast8xbeQ7kcZJwSgFAKX+1k4obAqrnmugz9pNBEFaCGJI0AKYDtOhLXXkUjv9aXy8fjHA8MQOMOa63soBlxc4DyCtS7qG9uealqpnd16bgpjKtGcFtaeXAyMorkh8COTh7/QCgHgO9PSojG0NyG5y4Zh0celn5I3+TPcWJYSGK8LYsqeXW3aljFQ==; JSESSIONID=32A4B119EE5B0ABC94B5DF8FA36557FF",
                "authority": "finance.naver.com",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "macOS",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "iframe",
                "referer": "https://finance.naver.com/item/sise_day.naver?code=053050",
                "accept-language": "en-US,en;q=0.9,ko;q=0.8"
            }

            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
            data=response.text
            eachrow=data.split('<span class="tah p10 gray03">')[1:]
            for each in eachrow:
                date=each.split("</span>")[0]
                data5=each.split('num"><span class="tah p11">')
                # for item in data5:
                #     if "</span>\n\t\t\t</td>" in item:
                #         print(item)
                #         data5.remove(item)

                # print(data2)
                date=data5[0].split("</span></td>")[0].replace(".","")
                close=int(data5[1].split("</span></td>")[0].replace(",",""))    
                open=int(data5[2].split("</span></td>")[0].replace(",",""))        
                high=int(data5[3].split("</span></td>")[0].replace(",",""))
                low=int(data5[4].split("</span></td>")[0].replace(",",""))
                volume=int(data5[5].split("</span></td>")[0].replace(",",""))

                list3.append((date,close,open,high,low,volume))
        except:
            pass
    list4=list(dict.fromkeys(list3))

    # df1=pd.DataFrame(list4)
    # df=df1.rename(columns={0:"Date",1:"Close",2:"Open",3:"High",4:"Low",5:"Volume"})
    # df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
    # df=df.sort_values(by="Date")
    # df=df.reset_index()
    # df1=df.drop(columns=["index"])
    # df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(ticker))

    try:
        df2=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(nameandcode),index_col=0)
    except:
        df1=pd.DataFrame(list4)
        df=df1.rename(columns={0:"Date",1:"Close",2:"Open",3:"High",4:"Low",5:"Volume"})
        df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
        df=df.sort_values(by="Date")
        df=df.reset_index()
        df1=df.drop(columns=["index"])
        df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(nameandcode))
    else:
        df1=pd.DataFrame(list4)
        df=df1.rename(columns={0:"Date",1:"Close",2:"Open",3:"High",4:"Low",5:"Volume"})
        df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
        df=df.sort_values(by="Date")
        df=df.reset_index()
        df1=df.drop(columns=["index"])
        df1=df2.append(df1)
        df1=df1.drop_duplicates(["Date"],keep="last")
        df=df1.reset_index()
        df1=df.drop(columns=["index"])
        df1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}_v1.xlsx".format(nameandcode))

# %%
kospi_historical_single_stock("KODEX 200")

# %%
import os

def five_consecutive_days_up_korean_stocks():
    list1=[]
    list2=[]
    for file in os.listdir('/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history'):
        # read excel
        try:
            df=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}".format(file),index_col=0)
            ticker=file.split("_v1.")[0]
            try:
                if df["Close"][-1:].values[0] >df["Close"][-2:-1].values[0]  and df["Close"][-2:-1].values[0] >df["Close"][-3:-2].values[0] :
                    if df["Close"][-3:-2].values[0] >df["Close"][-4:-3].values[0]  and df["Close"][-4:-3].values[0] >df["Close"][-5:-4].values[0] :
                        if df["Close"][-5:-4].values[0] >df["Close"][-6:-5].values[0]  and df["Close"][-6:-5].values[0] >df["Close"][-7:-6].values[0] :
                            list2.append((ticker,df["Close"][-1:].values[0] ,df["Close"][-2:-1].values[0] ,df["Close"][-1:].values[0] /df["Close"][-5:-4].values[0] ))
                        else:    
                            list1.append((ticker,df["Close"][-1:].values[0] ,df["Close"][-2:-1].values[0] ,df["Close"][-1:].values[0] /df["Close"][-5:-4].values[0] ))

            except Exception as e:
                print(ticker ,e)
        except:
            print(ticker,file)

    df2=pd.DataFrame(list1)
    df2=df2.sort_values(by=3,ascending=False)
    df2=df2.reset_index()

    df2.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/4 korean stock analysis/5_consecutive_high.xlsx")

    dt2=pd.DataFrame(list2)
    dt2=dt2.sort_values(by=3,ascending=False)
    dt2=dt2.reset_index()
    dt2.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/4 korean stock analysis/7_consecutive_high.xlsx")

five_consecutive_days_up_korean_stocks()
# %%
list_newhigh=[]
def korean_newhigh_stocks():
    koreanlist2=[]
    list1=[]
    list2=[]
    for file in os.listdir('/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history'):
        # read excel
        try:
            df=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}".format(file),index_col=0)
            ticker=file.split("_v1.")[0]
            df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()
            df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()

            try:
                if df["Close"][-1:].values[0]> df["MAX200"][-2:-1].values[0]:
                    list_newhigh.append((ticker,df["Close"][-1:].values[0],df["MAX200"][-1:].values[0],df["Close"][-1:].values[0]/df["MAX200"][-1:].values[0]))
                if str(df["Close"][-1:].values[0]) in "nan":
                    if df["Close"][-2:-1].values[0]> df["MAX200"][-3:-2].values[0]:
                        list_newhigh.append((ticker,df["Close"][-2:-1].values[0],df["MAX200"][-2:-1].values[0],df["Close"][-2:-1].values[0]/df["MAX200"][-2:-1].values[0]))
            except Exception as e:
                print(ticker ,e)
            
            
            try:
                
                
                
            
                                    
                if str(df["Close"][-1:].values[0]) in "nan":
                    if df["Close"][-2:-1].values[0]> df["SMA200"][-2:-1].values[0] and df["Close"][-3:-2].values[0]< df["SMA200"][-3:-2].values[0]:
                        
                        koreanlist2.append((ticker,df["Close"][-2:-1].values[0],df["Close"][-3:-2].values[0],df["Close"][-2:-1].values[0]/df["Close"][-3:-2].values[0],df["SMA200"][-2:-1].values[0]))
                    elif df["Close"][-2:-1].values[0]> df["SMA200"][-2:-1].values[0] and df["Close"][-4:-3].values[0]< df["SMA200"][-4:-3].values[0]:
                        
                        koreanlist2.append((ticker,df["Close"][-2:-1].values[0],df["Close"][-4:-3].values[0],df["Close"][-2:-1].values[0]/df["Close"][-4:-3].values[0],df["SMA200"][-2:-1].values[0]))

                else:
                    if df["Close"][-1:].values[0]> df["SMA200"][-1:].values[0] and df["Close"][-2:-1].values[0]< df["SMA200"][-2:-1].values[0]:
                        
                        koreanlist2.append((ticker,df["Close"][-1:].values[0],df["Close"][-2:-1].values[0],df["Close"][-1:].values[0]/df["Close"][-2:-1].values[0],df["SMA200"][-1:].values[0]))
                    elif df["Close"][-1:].values[0]> df["SMA200"][-1:].values[0] and df["Close"][-3:-2].values[0]< df["SMA200"][-3:-2].values[0]:
                        
                        koreanlist2.append((ticker,df["Close"][-1:].values[0],df["Close"][-2:-1].values[0],df["Close"][-1:].values[0]/df["Close"][-2:-1].values[0],df["SMA200"][-1:].values[0]))

                
                
                
            except:
                pass
                
                
                
                
                
                
            
        except:
            print(ticker,file)

    if len(list_newhigh)<1:
        pass
    else:
        dc1=pd.DataFrame(list_newhigh)
        dc1=dc1.sort_values(by=3,ascending=False)
        dc1=dc1.reset_index()
        dc1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/4 korean stock analysis/korean_stocks_newhigh.xlsx")

    if len(koreanlist2)<1:
        pass
    else:
        dd1=pd.DataFrame(koreanlist2)
        dd1=dd1.sort_values(by=3,ascending=False)
        dd1=dd1.reset_index()
        dc1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/4 korean stock analysis/korean_stocks_sma200.xlsx")

korean_newhigh_stocks()

# %%

volume_peak1=[time.monotonic()]
def volume_peak(time1):
    if time.monotonic()-volume_peak1[0]>(time1):
        volume_peak1[0]=time.monotonic()
        

        list3=[]


        koreanlist2=[]
        list1=[]
        list2=[]
        for file in os.listdir('/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history'):
            # read excel
            try:
                df=pd.read_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/2 naver stock price history/{}".format(file),index_col=0)
                ticker=file.split("_v1.")[0]
                df["MAX200"] = df["High"].rolling(min_periods=1, window=200).max()
                df['SMA200'] = df["Close"].rolling(min_periods=1, window=200).mean()
                df['VOL200'] = df["Volume"].rolling(min_periods=1, window=200).mean()
            except:
                pass
            else:
                try:
                                        
                    if str(df["Volume"][-1:].values[0]) in "nan":
                        if df["VOL200"][-2:-1].values[0]> df["Volume"][-2:-1].values[0]*5:

                            list3.append((ticker,df["Volume"][-2:-1].values[0],df["Volume"][-3:-2].values[0],df["Volume"][-2:-1].values[0]/df["VOL200"][-3:-2].values[0],df["VOL200"][-2:-1].values[0]))

                    else:
                        if df["VOL200"][-1:].values[0]> df["Volume"][-1:].values[0]*5: 

                            list3.append((ticker,df["Volume"][-1:].values[0],df["Volume"][-2:-1].values[0],df["Volume"][-1:].values[0]/df["VOL200"][-2:-1].values[0],df["VOL200"][-1:].values[0]))
                except Exception as e:
                    print(ticker , e)
        if len(list3)<1:
            pass
        else:
            dc1=pd.DataFrame(list3)
            dc1=dc1.sort_values(by=3,ascending=False)
            dc1=dc1.reset_index()
            dc1.to_excel("/Volumes/GoogleDrive/My Drive/ibkr/1_total_data/3 korean stocks/4 korean stock analysis/korean_stocks_vol200.xlsx")
volume_peak(0)
# %%

page1=0
url = "https://finance.naver.com/sise/sise_market_sum.naver"

querystring = {"page":"{}".format(page1)}

payload = ""
headers = {
    "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; nx_ssl=2; page_uid=hlojslp0J1sssCXP+shssssssrd-315361; naver_stock_codeList=053050%7C066570%7C056090%7C218150%7C004105%7C004100%7C169330%7C005930%7C028300%7C096530%7C; NID_SES=AAABqA6T11qWUUJyEwPe8ZasyIQXLiMU+rZpQ9reIeoMCmzLPgOkOtgG5uANOrlfalxH3tPgjB2X1P8tHrF7vm6rJfMMSz0GqzmHcv6b4v50/ftXmuUnaV3Tjcxw75M/3Q2zSMEQ5ohy9okQ6+eEsYBRMqvAsbaM45qoLJ6Jw2vpECSTTZY4YmO2DnACd9C2ZEKP+PnQhHN14RJJAn7UcozHJ4KcOfet4ZKW/EpKCWdpgZD/DUurWQqM/9k4nb6X572+3w3qC5PZ3Ov4Uv7ZgtBnrXspKbMwDxyCbHv7NVryWfFfWScednx8J17BGVZU3nJFGy6337bj9chVmPcCN3RKKUYi0ecJve+r46hfmz8Lp1C1dmAXZ+SvD8xDr+kr5u5xejk3BhiBitYfNUcJtPq2hn1VHxQEGSYegItFwLWgD361IegOzBT+E6En+UIrNZ8SZ6V7TwtoTP6x3GxioywyFe1KsQnPHAd0Q4U2Aozy0EIhsIR/VRMa2B6JoYHP3EMJHYQhJtpYqABcvt5/+YwoMBTj9j8AyJ3sfjUx4sG+bTppUUD1JEKg9RIN1Lq70fVsxw==; JSESSIONID=E2CA54E942CD15DC5E712D9FF25094AD",
    "authority": "finance.naver.com",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://finance.naver.com/sise/sise_market_sum.naver",
    "accept-language": "en-US,en;q=0.9,ko;q=0.8"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data=response.text


//td[@class="no"]