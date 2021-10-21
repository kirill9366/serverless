import boto3
from botocore.exceptions import ClientError


def create_todo_table(dynamodb):
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE',
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def create_task(table, title):
    response = table.put_item(
        Item={
            'title': title,
        }
    )
    return response


def get_task(table, title):
    try:
        response = table.get_item(Key={'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def update_task(table, title):
    response = table.update_item(
        Key={
            'title': title
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def delete_task(table, title):
    try:
        response = table.delete_item(
            Key={
                'title': title
            },
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response
