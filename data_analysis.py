import os
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from google.cloud import storage

def analyze_jazz_data():
    """Cloud Function to analyze jazz data from GCS and store the visualization."""
    # Initialize GCS client
    bucket_name = 'spotify_data_bucket1'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    # Download raw data
    blob = bucket.blob('jazz_analysis/raw_jazz_data.csv')
    raw_data = blob.download_as_string().decode('utf-8')
    jazz_df = pd.read_csv(StringIO(raw_data))
    
    # Data processing
    jazz_df['release_date'] = pd.to_datetime(jazz_df['release_date'])
    jazz_df['year'] = jazz_df['release_date'].dt.year
    avg_popularity_by_year = jazz_df.groupby('year')['popularity'].mean().reset_index()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(avg_popularity_by_year['year'], avg_popularity_by_year['popularity'], marker='o')
    plt.title('Average Popularity of Jazz Music Over Time')
    plt.xlabel('Year')
    plt.ylabel('Popularity')
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot to bytes
    from io import BytesIO
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    
    # Upload plot to GCS
    blob = bucket.blob('jazz_analysis/jazz_popularity_trend.png')
    blob.upload_from_string(img_buffer.read(), content_type='image/png')
    
    return 'Jazz data analyzed and visualization uploaded to GCS.', 200

if __name__ == "__main__":
    analyze_jazz_data()
