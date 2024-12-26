import requests
import spotify_accesstoken
def search_similarartists(id):
     # 用你的 Spotify 應用的 Client ID 和 Client Secret 替換這些值
    access_token = spotify_accesstoken.get_access_token()

    # 使用訪問令牌訪問 Spotify Web API
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # 搜索項目，替換 'keyword' 為你的搜索關鍵字
    SEARCH_URL = f'https://api.spotify.com/v1/artists/{id}/related-artists'
    response = requests.get(SEARCH_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data['artists']:
            item = data['artists']
            similar_artists = []
            for artist in item[:10]:
                artist_info = {
                    'name': artist['name'],
                    'spotify_url': artist['external_urls']['spotify'],
                    'image': artist['images'][0]['url'] if artist['images'] else None
                }
                similar_artists.append(artist_info)
            return similar_artists
        else:
            return None