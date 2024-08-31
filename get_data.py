import os
import pandas as pd
import spotipy

# Initialize Spotify API client
def initialize_spotify_client():
    client_id = os.environ.get('SPOTIPY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
    auth_manager = spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return spotipy_object

def search_jazz_albums(sp):
    results = sp.search(q='jazz', type='album')
    albums = results['albums']['items']
    
    jazz_data = []
    for album in jazz_albums:
        album_id = album['id']
        album_name = album['name']
        album_data = sp.album(album_id)
        release_date = album_data['release_date']
        popularity = album_data['popularity']

        jazz_data.append({
			'album_name': album_name,
			'popularity': popularity,
			'release_date': release_date
		})
        
    return pd.DataFrame(jazz_data)
    
def save_data(jazz_df):
    jazz_df.to_csv('data/raw_jazz_data.csv', index=False)
    
def main():
    sp = initialize_spotify_client()
    jazz_df = search_jazz_albums(sp)
    save_data(jazz_df)

if __name__ == "__main__":
    main()