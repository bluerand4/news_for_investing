from import_mongo import *
from import_google import *
from import_korean import *
from import_tradingview import *
from import_basics import *

def regression_v2(numbers,normalize=False):
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

    return slope,intercept
def how_many_days_ago_max_above(ticker):
    fullname=generate_fullname_tradingview(ticker)
    dwww=tradingview_simple(fullname,'1D')
    dwww

    dwww['above_max200']=''

    dwww=feature_engineering(dwww)
    dwww

    dwww.columns

    for i in range(1,len(dwww)):
        Close=dwww['Close'][i]
        Open=dwww['Open'][i]
        High=dwww['High'][i]
        Low=dwww['Low'][i]
        Volume=dwww['Volume'][i]
        Timestamp=dwww['Timestamp'][i]
        max200=dwww['MAX200'][i]
        max200_1=dwww['MAX200'][i-1]



        if dwww['High'][i]>dwww['MAX200'][i-1]:
            dwww.loc[i,'above_max200']='yes'

    dwww['above_max200'][-50:]
    for i in reversed(range(1,len(dwww))):
        above_max200=dwww['above_max200'][i]
        if above_max200=='yes':
            # print(i)
            break

    how_many_days_ago_max=len(dwww)-1-i
    print("how_many_days_ago_max: ",how_many_days_ago_max)
    return how_many_days_ago_max