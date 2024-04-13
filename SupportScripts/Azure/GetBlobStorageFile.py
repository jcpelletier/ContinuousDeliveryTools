import sys
import logging
from azure.storage.blob import BlobServiceClient, BlobClient

def download_blob():
    # Correct the argument check to account for 4 arguments plus the script name
    if len(sys.argv) != 5:
        logging.error("Usage: python script.py <connection_string> <container_name> <blob_name> <local_file_path>")
        sys.exit(1)
    
    # Correct the indices for sys.argv to properly unpack the arguments
    _, connection_string, container_name, blob_name, local_file_path = sys.argv
    
    try:
        # Create a BlobServiceClient to interact with the Blob service
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Create a BlobClient to interact with a specific blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        print(f"Downloading blob '{blob_name}' from container '{container_name}'...")
        
        # Download the blob to a local file
        with open(local_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        
        print(f"Blob '{blob_name}' downloaded to '{local_file_path}'.")
    except Exception as ex:
        print('Exception:')
        print(ex)

# Call the function with the specifics
download_blob()
