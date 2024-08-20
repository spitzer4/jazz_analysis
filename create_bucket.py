import os
from google.cloud import storage

# Create an environment variable for the service key configuration
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

# Create a storage client
storage_client = storage.Client()

print(storage_client)

# Create a new bucket
bucket_name = 'spotify_data_bucket1'
bucket = storage_client.bucket(bucket_name=bucket_name)
bucket = storage_client.create_bucket(bucket)