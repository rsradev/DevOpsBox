import boto3

# Initialize interfaces
s3Client = boto3.client('s3')
s3Resource = boto3.resource('s3')

# Create byte string to send to our bucket
putMessage = b'Hi! I came from Boto3!'

# put_object
response = s3Client.put_object(
    Body = putMessage,
    Bucket = 'radi-demo',
    Key = 'boto3put.txt'
)

print(response)

# copy
toCopy = {
    'Bucket': 'radi-demo',
    'Key': 'boto3put.txt'
}

s3Resource.meta.client.copy(toCopy, 'radi-demo', 'boto3copy.txt')

# copy_object
response = s3Client.copy_object(
    Bucket = 'radi-demo',
    CopySource = '/radi-demo/boto3put.txt',
    Key = 'boto3copyobject.txt'
)

print(response)

# upload_file
boto3Upload = 'boto3upload.txt'

s3Resource.meta.client.upload_file(boto3Upload, 'radi-demo', boto3Upload)

# upload_fileobj
with open(boto3Upload, 'rb') as fileObj:
    response = s3Client.upload_fileobj(fileObj, 'radi-demo', 'boto3uploadobj.txt')
    print(response)

'''
response = s3Client.put_bucket_accelerate_configuration(
    Bucket='radi-demo',
    AccelerateConfiguration={
        'Status': 'Enabled'
    }
)
print(response)
'''