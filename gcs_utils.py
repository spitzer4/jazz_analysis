import os
from google.cloud import storage

def initialize_gcs_client():
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'
	storage_client = storage.Client()
	return storage_client

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
	storage_client = initialize_gcs_client()
	bucket = storage_client.bucket(bucket_name=bucket_name)
	blob = bucket.blob(destination_blob_name)
	blob.upload_from_filename(source_file_name)
	print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

def download_from_gcs(bucket_name, source_blob_name, destination_file_name):
	storage_client = initialize_gcs_client()
	bucket = storage_client.bucket(bucket_name=bucket_name)
	blob = bucket.blob(source_blob_name)
	blob.download_to_filename(destination_file_name)
	print(f"File {source_blob_name} has been downloaded from bucket {bucket_name} to {destination_file_name}.")

if __name__ == "__main__":
	initialize_gcs_client()
	upload_to_gcs('spotify_data_bucket1', 'data/raw_jazz_data.csv', 'jazz_analysis/raw_jazz_data.csv')