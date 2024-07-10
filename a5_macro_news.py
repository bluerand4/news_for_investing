#%%
from datetime import datetime,timedelta
import sys,os,copy,ast,socket,random,math,webbrowser,getpass,time,shutil
import numpy as np
import pandas as pd
from pytz import timezone
import matplotlib.pyplot as plt

links=['https://www.investing.com/economic-calendar/interest-rate-decision-168',
'https://www.investing.com/economic-calendar/services-pmi-1062',
'https://www.investing.com/economic-calendar/manufacturing-pmi-829',
'https://tradingeconomics.com/china/manufacturing-pmi',
'https://tradingeconomics.com/united-states/building-permits',
'https://ycharts.com/indicators/us_building_permits',
'https://ycharts.com/indicators/housing_starts',
'http://www.sca.isr.umich.edu/',
'https://ycharts.com/indicators/moodys_seasoned_aaa_corporate_bond_yield',
'https://www.wsj.com/market-data/bonds',
'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm',
'https://fred.stlouisfed.org/series/TOTALSA',
'https://fred.stlouisfed.org/series/UNRATE',
'https://tradingeconomics.com/united-states/current-account',
'https://www.investing.com/economic-calendar/cftc-copper-speculative-positions-1620',
'https://tradingeconomics.com/united-states/capital-flows',
'https://tradingeconomics.com/united-states/tourist-arrivals',
'https://tradingeconomics.com/united-states/gdp-growth-annual',
'https://tradingeconomics.com/united-states/wage-growth',
'https://tradingeconomics.com/united-states/core-inflation-rate',
'https://tradingeconomics.com/united-states/banks-balance-sheet',
'https://tradingeconomics.com/united-states/central-bank-balance-sheet',
'https://tradingeconomics.com/united-states/money-supply-m2',
'https://www.bea.gov/data/intl-trade-investment/international-transactions#:~:text=The%20U.S.%20current%20account%20deficit,quarter%20deficit%20was%20%24161.4%20billion.',
'https://www.eia.gov/naturalgas/weekly/',
'https://www.aaii.com/sentimentsurvey']

for item in links:
    webbrowser.open(item)