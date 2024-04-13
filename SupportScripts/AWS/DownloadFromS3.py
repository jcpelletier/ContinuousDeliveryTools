import sys
import boto3
from botocore.exceptions import NoCredentialsError

def download_file_from_s3(bucket_name, object_name, file_name):
    """
    Download a file from an S3 bucket using IAM roles or AWS CLI configured credentials.

    :param bucket_name: The name of the S3 bucket
    :param object_name: S3 object name
    :param file_name: Local file name to save the downloaded content
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        s3.download_file(bucket_name, object_name, file_name)
        print(f"File {file_name} downloaded successfully.")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <BUCKET_NAME> <OBJECT_NAME> <FILE_NAME>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    object_name = sys.argv[2]
    file_name = sys.argv[3]

    download_file_from_s3(bucket_name, object_name, file_name)
