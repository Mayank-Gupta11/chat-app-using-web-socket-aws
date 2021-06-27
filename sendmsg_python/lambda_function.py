import json
import boto3
import os
import time

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    
    #time.sleep(300) # applying 5min sleep
    
    # TODO implement
    message="null"
    
    try:
        message = json.loads(event['body'])['message']
    except Exception as e:
        message=event['body']
    
    paginator = dynamodb.get_paginator('scan')
    
    connectionIds = []

    apigatewaymanagementapi = boto3.client('apigatewaymanagementapi', 
    endpoint_url = "https://" + event["requestContext"]["domainName"] + "/" + event["requestContext"]["stage"])

    # Retrieve all connectionIds from the database
    for page in paginator.paginate(TableName='chat'):
        connectionIds.extend(page['Items'])

    # Emit the recieved message to all the connected devices
    print(connectionIds)
    
    for connectionId in connectionIds:
        apigatewaymanagementapi.post_to_connection(
            Data=message,
            ConnectionId=connectionId['connectionid']['S']
        )
		
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
