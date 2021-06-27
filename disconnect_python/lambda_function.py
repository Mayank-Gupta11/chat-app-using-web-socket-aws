import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    
    connectionId = event['requestContext']['connectionId']

    # Delete connectionId from the database
    dynamodb.delete_item(TableName='chat', Key={'connectionid': {'S': connectionId}})

    #return {}
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
