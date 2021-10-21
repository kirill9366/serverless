import boto3

import json

# locale imports
from database import todo

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": context
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def create_task(event, context):
    table = dynamodb.Table('Movies')
    body = todo.create_task(table, event["pathParameters"]["title"])
    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
