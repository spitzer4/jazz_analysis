from google.cloud import storage

def initialize_gcs_client():
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
