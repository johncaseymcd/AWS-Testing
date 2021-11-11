import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    destination_bucket = 'nps26-new-receiver'
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key_file_name = event['Records'][0]['s3']['object']['key']
    
    copy_source_object = {'Bucket': source_bucket, 'Key': key_file_name}
    
    s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket, Key=key_file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Nick!')
    }