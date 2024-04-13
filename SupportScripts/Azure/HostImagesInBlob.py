import os
import sys
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings

if len(sys.argv) < 5:
    print("Usage: python script.py <connection_string> <container_name> <directory_path> <output_file>")
    sys.exit(1)

# Assign arguments to variables
connect_str = sys.argv[1]
container_name = sys.argv[2]
directory_path = sys.argv[3]
output_file = sys.argv[4]

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Function to upload file to Azure Blob with content type
def upload_file_to_blob(file_path):
    file_name = os.path.basename(file_path)
    blob_client = container_client.get_blob_client(file_name)
    with open(file_path, "rb") as data:
        # Specify the content type for PNG images
        content_settings = ContentSettings(content_type='image/png')
        blob_client.upload_blob(data, overwrite=True, content_settings=content_settings)
    return f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{file_name}"

# Scan directory for .png files and upload them
urls = []
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            print(f"Uploading {file_path}...")
            url = upload_file_to_blob(file_path)
            urls.append(url)

# Write URLs to a file
with open(output_file, 'w') as f:
    for url in urls:
        f.write(url + '\n')

print("Upload complete. URLs written to", output_file)
