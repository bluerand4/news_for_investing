#%%
from import_all import *


# %%

mongo_collection_names('stock')
#%%
dp=mongo_get_df('stock','polygon_stocks')
dp
#%%

#%%
df=mongo_get_df('stock','comparison')
df
# %%
df=df.sort_values(by='revslope',ascending=False)
df[:20]
# %%
df
#%%
df2 = df[df['inslope'] >= 15]
df2 = df2[df2['inslope2'] >= 15]
df2 = df2[df2['revslope'] >= 15]
df2 = df2[df2['revslope2'] >= 15]
df2

#%%

df2 = df2[df2['inslope'] <= 499]
df2 = df2[df2['inslope2'] <= 499]
df2 = df2[df2['revslope'] <= 499]
df2 = df2[df2['revslope2'] <= 499]
df2
# %%
df2
# %%
tradingview_slope=mongo_get_df('stock','tradingview_slope')
tradingview_slope
#%%

#%%

#%%
PER="Price to earnings Ratio (TTM)"
DIV='Dividend yield (indicated)'
tradingview_slope[PER]


df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2 = df2[df2['revenue1'] >= 0]
df2 = df2[df2['revenue2'] >= 0]
df2 = df2[df2['net_income1'] >= 0]
df2 = df2[df2['net_income2'] >= 0]
df2 = df2[df2['fcf1'] >= 0]
df2 = df2[df2['fcf2,'] >= 0]
df2=df2.sort_values(by=PER,ascending=True)
df3=df2[:50][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
df3
#%%

list2=df3['ticker'][0:20].values.tolist()
','.join(list2)
#%%

'ESEA,PSHG,TNK,GSL,TRMD,CVI,PETZ,DINO,GM,CEIX,SDRL,GECC,MHUA,FCAP,MVO,OI,BSVN,SLVM,WLFC,BOSC,HE,RWAY,BVFL'
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%####################################################
# #

# for i in range(len(df)):
#     data=df['data'][i]
#     data=df['data'][i]
#     data=df['data'][i]

tradingview_slope
#%%
# df2 = tradingview_slope[tradingview_slope[PER] > 0]
df2=tradingview_slope
df2 = df2[df2['revenue1'] >= 15]
df2 = df2[df2['revenue2'] >= 15]
# df2 = df2[df2['net_income1'] >= 15]
# df2 = df2[df2['net_income2'] >= 15]
df2 = df2[df2['fcf1'] >= 15]
df2 = df2[df2['fcf2,'] >= 10]
df2 = df2[df2['revenue1'] <= 499]
df2 = df2[df2['revenue2'] <= 499]
# df2 = df2[df2['net_income1'] <= 499]
# df2 = df2[df2['net_income2'] <= 499]
df2 = df2[df2['fcf1'] <= 499]
df2 = df2[df2['fcf2,'] <= 499]

# df2=df2.sort_values(by='fcf2,',ascending=False)
df2
#%%
df2=reset_index(df2)
df2_copy=copy.deepcopy(df2)

df2_copy['mc']=0
df2_copy['revenue']=0
df2_copy['rm_ratio']=0
df2_copy['free_cash']=0
df2_copy['fm_ratio']=0
for i in range(len(df2_copy)):
    ticker=df2_copy['ticker'][i]
    
    marc=df2[df2['ticker']==ticker]['Market capitalization'].values[0]
    rev1=df2[df2['ticker']==ticker]['revenue'].values[0]
    rev1=ast.literal_eval(rev1)
    rev1=rev1[-4:]
    rev1=sum(rev1)
    fcf1=df2[df2['ticker']==ticker]['fcf'].values[0]
    fcf1=ast.literal_eval(fcf1)
    fcf1=fcf1[-4:]
    fcf1=sum(fcf1)
    
    
    df2_copy.loc[i,'mc']=marc
    df2_copy.loc[i,'revenue']=rev1
    df2_copy.loc[i,'free_cash']=fcf1
    ratio=rev1/marc
    df2_copy.loc[i,'rm_ratio']=ratio
    ratio=fcf1/marc
    df2_copy.loc[i,'fm_ratio']=ratio



LAMBDA=0.5
df2_copy['rm_fm']=LAMBDA*df2_copy['rm_ratio']+(1-LAMBDA)*3*df2_copy['fm_ratio']
df2_copy=df2_copy.sort_values(by='rm_fm',ascending=False)
df2_copy
#%%


#%%
#%%
#%%

#%%
df3=df2_copy[['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV,'Market capitalization','revenue','free_cash','rm_ratio','fm_ratio','mc','rm_fm']]
df_2=df[['ticker','industry','sector']]
df3=df3.merge(df_2,how='outer',on='ticker')
df3=df3[df3['sector']=='Technology']
df3=reset_index(df3)
df3
df3['how_many_days']=1000
# df3=df3[:50]
df3
#%%
df3 = df3.dropna(subset=['rm_fm'])
df3
#%%


for i in range(len(df3))[:]:
    ticker=df3['ticker'][i]
    try:
        days=how_many_days_ago_max_above(ticker)
    except:
        days=3000
    df3.loc[i,'how_many_days']=days
    print("ticker: ",ticker,days)
#%%

#%%
df3
df3=df3.sort_values(by='how_many_days',ascending=True)
df3
#%%
df3=reset_index(df3)
df3

    

#%%



#%%
df4 = df3[df3['how_many_days'] <= 60]




#%%
df4=df4.sort_values(by='rm_fm',ascending=False)
df4=reset_index(df4)
df4[['ticker','fcf1','fcf2,','rm_ratio','fm_ratio','industry',PER,'rm_fm']]
#%%
# open_excel(df3)
#%%
df4[['ticker','rm_fm','fcf1','fcf2,','rm_ratio','fm_ratio','industry',PER,'how_many_days']]
#%%

#%%
tradingview_slope[tradingview_slope['ticker']=='TIPT'][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
#%%
df4.columns
#%%
df4 = df4[df4['fm_ratio'] >= 0.001]
df4=reset_index(df4)
df5=copy.deepcopy(df4)
df5['fm_rm_fcf']=0
for i in range(len(df5)):
    ticker=df5['ticker'][i]
    fcf1_=df5['fcf1'][i]
    fcf2_=df5['fcf2,'][i]
    revenue2=df5['revenue2'][i]


    marc=df2[df2['ticker']==ticker]['Market capitalization'].values[0]
    rev1=df2[df2['ticker']==ticker]['revenue'].values[0]
    try:
        rev1=ast.literal_eval(rev1)
        rev1=rev1[-4:]
        rev1=sum(rev1)
    except:
        rev1=int(rev1)
    
    
    fcf1=df2[df2['ticker']==ticker]['fcf'].values[0]
    fcf1=ast.literal_eval(fcf1)
    fcf1=fcf1[-4:]
    fcf1=sum(fcf1)
    
    
    # df5.loc[i,'mc']=marc
    # df5.loc[i,'revenue']=rev1
    # df5.loc[i,'free_cash']=fcf1
    rm_ratio=rev1/marc
    # df5.loc[i,'rm_ratio']=ratio
    fm_ratio=fcf1/marc
    fcf1_=fcf1_/1000
    fcf2_=fcf2_/1000
    revenue2=revenue2/1000
    fm_rm_fcf=0.9*fm_ratio+0.3*fcf2_+0.4*revenue2

    df5.loc[i,'fm_rm_fcf']=fm_rm_fcf



#%%
df5
df5=df5.sort_values(by='fm_rm_fcf',ascending=False)
df5=reset_index(df5)
df5[['ticker','fcf1','fcf2,','rm_ratio','fm_ratio','industry',PER,'rm_fm']]
df5[['ticker','fm_rm_fcf','fcf1','fcf2,','rm_ratio','fm_ratio','industry',PER,'how_many_days']]

#%%



#%%
#%%
#%%
#%%####################################################
#

#%%
df.columns
#%%
df_2=df[['ticker','industry','sector']]
df4=df3.merge(df_2,how='outer',on='ticker')[:50]
df4
#%%
final=df4[df4['sector']=='Technology']
final
# %%

list2=df2[df2['ticker']=='EPRT']['fcf'].values[0]
list2=ast.literal_eval(list2)
list2
#%%

tradingview_slope[tradingview_slope['ticker']=='NVDA'][['ticker','revenue1','revenue2','net_income1','net_income2','fcf1','fcf2,',PER,DIV]]
# %%
list3=list2[-8:]
# %%
import matplotlib.pyplot as plt

plt.plot(list3)
plt.show()
# %%

def regression(numbers,normalize=False):
    if normalize:
        # numbers = remove_outliers(numbers,85,5)
        min1=min(numbers)
        max1=max(numbers)
        numbers=[(item -min1)/(max1-min1) for item in numbers]
    numbers = [x for x in numbers if not math.isnan(x)]
    # Generating the same number of points as the list of numbers for the x-axis
    x = list(range(len(numbers)))
    y = numbers

    # Calculating the sum of x, y, x*y and x^2
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(len(x))])
    sum_xx = sum([i**2 for i in x])

    # Number of data points
    N = len(x)

    # Calculating slope (m) and intercept (b)
    slope = (N * sum_xy - sum_x * sum_y) / (N * sum_xx - sum_x**2)
    intercept = (sum_y - slope * sum_x) / N

    # Generating the regression line
    regression_line = [slope * xi + intercept for xi in x]

    # Plotting the points and the regression line
    # plt.scatter(x, y, color='blue', label='Data Points')
    # plt.plot(x, regression_line, color='red', label='Regression Line')

    # # Annotating the slope
    # plt.text(1, 4, f'Slope: {slope:.2f}', fontsize=12)

    # # Adding labels and title
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.title('Linear Regression Line')
    # plt.legend()

    # # Showing the plot
    # plt.show()
    return slope,intercept


def remove_outliers(data,THRESHOLD=25,THRESHOLD2=1.5):
    q1 = np.percentile(data, int(THRESHOLD))
    q3 = np.percentile(data, int(100-THRESHOLD))
    iqr = q3 - q1

    lower_bound = q1 - THRESHOLD2 * iqr
    upper_bound = q3 + THRESHOLD2 * iqr

    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]
    return filtered_data

slope1,_=regression(list3,normalize=True)
print("slope1: ",slope1)
# %%
