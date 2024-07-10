import boto3
import pandas as pd

def dynamo_set_df(table_name, unique_column_name, df):
    # Create a Boto3 client for DynamoDB
    dynamodb = boto3.resource('dynamodb')

    # Access your table
    table = dynamodb.Table(table_name)

    # Iterate over DataFrame and upsert items
    for index, row in df.iterrows():
        item = row.to_dict()
        table.put_item(Item=item)

    # Fetch all items to find ones to delete
    response = table.scan()
    items_in_table = {item[unique_column_name] for item in response['Items']}
    
    # Find items that are not in DataFrame
    items_to_delete = items_in_table - set(df[unique_column_name])

    # Delete items that are not in DataFrame
    with table.batch_writer() as batch:
        for item_to_delete in items_to_delete:
            batch.delete_item(Key={unique_column_name: item_to_delete})

# Usage example
# dynamodb_set_df('your_table_name', 'your_unique_column_name', your_dataframe)
import boto3
import pandas as pd

def dynamo_get_df(table_name):
    # Create a Boto3 client for DynamoDB
    dynamodb = boto3.resource('dynamodb')

    # Access your table
    table = dynamodb.Table(table_name)

    # Fetch all items from the table
    response = table.scan()
    items = response['Items']

    # While loop to handle pagination if the dataset is large
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response['Items'])

    # Convert the items to a DataFrame
    df = pd.DataFrame(items)
    return df

# Usage example
# df = dynamo_get_df('your_table_name')
