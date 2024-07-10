#%%
from import_all import *

# %%

mongo_collection_names('comparison')
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
df=mongo_get_df('stock','tradingview_slope')
#%%
data1=ast.literal_eval(df['revenue'][0])
data1
# %%
import matplotlib.pyplot as plt

plt.plot(data1)
plt.show()
# %%
regression()
#%%
if True:
    numbers = remove_outliers(data1)
    min1=min(numbers)
    max1=max(numbers)
    numbers=[(item -min1)/(max1-min1) for item in numbers]
numbers = [x for x in numbers if not math.isnan(x)]
numbers
#%%
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
slope
# %%
round(slope*1000,2)
# %%
