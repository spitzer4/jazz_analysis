from get_data import main as generate
from gcs_utils import upload_to_gcs, download_from_gcs

def main():
	# Run the data generation
	generate()

	# Upload the generated data to GCS
	upload_to_gcs('spotify_data_bucket1', 'data/raw_jazz_data.csv', 'jazz_analysis/raw_jazz_data.csv')
