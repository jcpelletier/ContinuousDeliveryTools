import sys
import os
import boto3
from botocore.exceptions import NoCredentialsError

def append_to_s3_file(bucket_name, object_key, region, data):
    session = boto3.session.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                                    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                                    region_name=region)
    s3 = session.resource('s3')
    obj = s3.Object(bucket_name, object_key)

    # Try to read the existing content
    try:
        file_content = obj.get()['Body'].read().decode('utf-8')
    except s3.meta.client.exceptions.NoSuchKey:
        file_content = ""

    # Append new data
    file_content += f"\n{data}"

    # Write back to S3
    obj.put(Body=file_content.encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python PushFileToS3.py <bucketName> <objectKey> <region>")
        sys.exit(1)

    bucketName = sys.argv[1]
    objectKey = sys.argv[2]
    region = sys.argv[3]

    # Example data to append, customize as needed
    new_data = "New log data here"

    try:
        append_to_s3_file(bucketName, objectKey, region, new_data)
        print("Data appended successfully.")
    except NoCredentialsError:
        print("Error: AWS credentials not found.")