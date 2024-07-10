#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil,requests,subprocess
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt


def kosdaq_mc_list_500(page_number=20):

    

    list1=[]
    list2=[]
    for page1 in range(1,page_number):

        url = "https://finance.naver.com/sise/sise_market_sum.naver"

        querystring = {"sosok":"1","page":"{}".format(page1)}

        payload = ""
        headers = {
            "cookie": "NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=LW5SFGDED2OV6; ASID=6c02c773000001758c0bce1e0000006a; NID_JKL=dgq30fAoLFclJayIEIlXv7cvEPMB1ExKZ0RQJWTB3xQ=; NID_AUT=5LQvMVlbnEkzplcT8LWXI/bUFi8dY9GXDmHroSd3msgp47qbBWz469GZ17qhTPVX; _ga=GA1.2.23033451.1609657664; _ga_4BKHBFKFK0=GS1.1.1628482401.4.0.1628482401.60; summary_item_type=recent; BMR=s=1643190542512&r=https%3A%2F%2Fm.blog.naver.com%2Fpunch833%2F221019264036&r2=https%3A%2F%2Fwww.google.com%2F; nx_ssl=2; page_uid=hlojslp0J1sssCXP+shssssssrd-315361; naver_stock_codeList=053050%7C066570%7C056090%7C218150%7C004105%7C004100%7C169330%7C005930%7C028300%7C096530%7C; NID_SES=AAABqA6T11qWUUJyEwPe8ZasyIQXLiMU+rZpQ9reIeoMCmzLPgOkOtgG5uANOrlfalxH3tPgjB2X1P8tHrF7vm6rJfMMSz0GqzmHcv6b4v50/ftXmuUnaV3Tjcxw75M/3Q2zSMEQ5ohy9okQ6+eEsYBRMqvAsbaM45qoLJ6Jw2vpECSTTZY4YmO2DnACd9C2ZEKP+PnQhHN14RJJAn7UcozHJ4KcOfet4ZKW/EpKCWdpgZD/DUurWQqM/9k4nb6X572+3w3qC5PZ3Ov4Uv7ZgtBnrXspKbMwDxyCbHv7NVryWfFfWScednx8J17BGVZU3nJFGy6337bj9chVmPcCN3RKKUYi0ecJve+r46hfmz8Lp1C1dmAXZ+SvD8xDr+kr5u5xejk3BhiBitYfNUcJtPq2hn1VHxQEGSYegItFwLWgD361IegOzBT+E6En+UIrNZ8SZ6V7TwtoTP6x3GxioywyFe1KsQnPHAd0Q4U2Aozy0EIhsIR/VRMa2B6JoYHP3EMJHYQhJtpYqABcvt5/+YwoMBTj9j8AyJ3sfjUx4sG+bTppUUD1JEKg9RIN1Lq70fVsxw==; JSESSIONID=FAB0E43BED9CB05732BCA4F244798E08",
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
            "referer": "https://finance.naver.com/sise/sise_market_sum.naver?sosok=1",
            "accept-language": "en-US,en;q=0.9,ko;q=0.8"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        data=response.text
        data1=data.split('/item/main.naver?code=')

        for item in data1:
            data2=item.split("</a></td>")[0]
            list1.append(data2)

        for i in range(len(list1)):
            try:
                code1=list1[i].split(" ")[0].replace('"',"")
                code1
                
                name1=list1[i].split('"tltle">')[1]
                name1
                nameandcode="{}_{}".format(name1,code1)
                list2.append((name1,code1,nameandcode))
            except:
                pass
    # korean_list=list(set(list2))
            
    list3=[]
    for item in list2:
        if item not in list3:
            
            list3.append(item)

    return list3

def kospi_mc_list_500(until_page=20):
    


    list1=[]
    list2=[]
    for page1 in range(1,until_page):


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

        data

        data1=data.split('/item/main.naver?code=')

        for item in data1:
            data2=item.split("</a></td>")[0]
            list1.append(data2)

        for i in range(len(list1)):
            try:
                code1=list1[i].split(" ")[0].replace('"',"")
                code1
        
                name1=list1[i].split('"tltle">')[1]
                name1

                nameandcode="{}_{}".format(name1,code1)
                list2.append((name1,code1,nameandcode))

            except:
                pass
    # return list(set(list2))
    list3=[]
    for item in list2:
        if item not in list3:
            
            list3.append(item)

    return list3
