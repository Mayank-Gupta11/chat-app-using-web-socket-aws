import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    connectionId = event['requestContext']['connectionId']

    # Insert the connectionId of the connected device to the database
    dynamodb.put_item(TableName='chat', Item={'connectionid': {'S': connectionId}})

    #return {}
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
