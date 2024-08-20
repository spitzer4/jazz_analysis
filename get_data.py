import os
import spotipy

auth_manager = spotipy.SpotifyClientCredentials(client_id=os.environ.get('SPOTIPY_CLIENT_ID'), client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'))
spotipy_object = spotipy.Spotify(auth_manager=auth_manager)

def search_jazz_albums():
    results = spotipy_object.search(q='jazz', type='album', limit=50)
    albums = results['albums']['items']
    return albums

# jazz_playlists = search_jazz_playlists()
jazz_albums = search_jazz_albums()

def get_album_popularity(album_id):
    album = spotipy_object.album(album_id)
    return album['popularity'], album['release_date']

# Extracting track popularity and release date from jazz albums
jazz_data = []
for album in jazz_albums:
    album_id = album['id']
    album_name = album['name']
    popularity, release_date = get_album_popularity(album_id)
    jazz_data.append({
        'album_name': album_name,
        'popularity': popularity,
        'release_date': release_date
    })
    
print(jazz_data)