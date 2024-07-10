#%%
from import_stocks2 import *
from import_dynamo import *
endpoint='https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?apiKey={polygon_api_key}'
response = requests.get(endpoint)
# Raise an error if the request failed
response.raise_for_status()
# Parse the JSON result
data = response.json()
data
df_total=pd.DataFrame(data['tickers'])
df_day = pd.DataFrame(data['tickers'])['day'].apply(pd.Series)
df_day
df_total = pd.concat([df_total, df_day], axis=1)
df_total
df_total['trade_volume']=df_total['v']*df_total['c']
df_total
df_total=df_total.sort_values(by='trade_volume',ascending=False)
df_total=reset_index(df_total)
stock_list=df_total['ticker'].values.tolist()

df=pd.DataFrame(stock_list)
df.columns=['ticker']
df
#%%

dynamo_set_df('test','ticker',df)
# %%
import boto3

# Specify the AWS region
region_name = 'us-east-1'  # Replace eith your region

# Create a Boto3 client for DynamoDB
dynamodb = boto3.resource('dynamodb', region_name=region_name)

# Access your table (replace 'your_table_name' with the actual table name)
table = dynamodb.Table('test')

# Example: Putting an item
#%%
item=df.to_dict('records')
#%%
# item = {'yourPrimaryKey': 'value', 'anotherAttribute': 'value'}
table.put_item(Item=item[0])

# %%
