import requests
import spotify_accesstoken
def Search_spotify(search_keyword, search_type):
    
    access_token = spotify_accesstoken.get_access_token()

    # 使用訪問令牌訪問 Spotify Web API
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # 搜索項目，替換 'keyword' 為你的搜索關鍵字
    SEARCH_URL = 'https://api.spotify.com/v1/search'

    # Send the GET request to the Spotify API
    response = requests.get(SEARCH_URL, headers=headers, params={'q': search_keyword, 'type': search_type})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Check if there are any results
        if data['tracks']['items']:
            # Get the first result
            item = data['tracks']['items']
            alltracks = []
            for track in item[:5]:
                track_info = {
                    'track name': track['name'],
                    'artist name': track['artists'][0]['name'],
                    'spotify url': track['external_urls']['spotify'],
                    'image': track['album']['images'][0]['url'] if track['album']['images'] else None
                }
                alltracks.append(track_info)
            # Extract the 'spotify' url, track name, and artist name from the first result
            return {
                'tracks': alltracks
            }
            
            
        
        else:
            return None
