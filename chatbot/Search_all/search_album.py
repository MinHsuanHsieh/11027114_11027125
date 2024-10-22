import requests
import spotify_accesstoken
def search_album(id):
    access_token = spotify_accesstoken.get_access_token()

    # 使用訪問令牌訪問 Spotify Web API
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # 搜索項目，替換 'id' 為你的搜索關鍵字
    SEARCH_URL = f'https://api.spotify.com/v1/artists/{id}/albums?order=release_date&limit=1'
    response = requests.get(SEARCH_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            item = data['items'][0]
            lastest_album = []
            album_info = {
                'name': item['name'],
                'id': item['id'],
                'spotify_url': item['external_urls']['spotify'],
                'image': item['images'][0]['url'] if item['images'] else None
            }
            lastest_album.append(album_info)
            return lastest_album
        else:
            return 'No album found'
        
def search_albumtrack(id):
    access_token = spotify_accesstoken.get_access_token()

    # 使用訪問令牌訪問 Spotify Web API
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    SEARCH_URL = f'https://api.spotify.com/v1/albums/{id}/tracks'
    response = requests.get(SEARCH_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        track = []
        if data['items']:
            for item in data['items']:
                track_info = {
                    'name': item['name'],
                    'id': item['id'],
                }
                
                track.append(track_info)
                
            return track
        else:
            return 'No track found'
            
#search_albumtrack('4aawyAB9vmqN3uQ7FjRGTy')
                
                
    