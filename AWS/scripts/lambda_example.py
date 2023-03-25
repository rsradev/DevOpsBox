import boto3
import json

def get_data():
    s3_bucket = 'random-users-data-554323931716'
    
    data = []
    
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(
            Bucket = s3_bucket
        )['Contents']
        
    s3_keys = []
    for object in objects:
        if object['Key'].startswith('users_'):
            s3_keys.append(object['Key'])
            
    for key in s3_keys:
        object = s3.get_object(
            Bucket = s3_bucket,
            Key = key
        )
             
        
        data += json.loads(object['Body'].read())
    
    return data
  
def handler(event, context):
    # Call the "get_data" function and return appropriately formatted results.
    return {'isBase64Encoded': False,'statusCode': 200,'body': json.dumps(get_data()), 'headers': {"Access-Control-Allow-Origin": "*"}}