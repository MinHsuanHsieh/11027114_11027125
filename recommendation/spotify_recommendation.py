import requests
import spotify_accesstoken
def spotift_recommendation():
    access_token = spotify_accesstoken.get_access_token()

    # 使用訪問令牌訪問 Spotify Web API
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    recommend_URL = 'https://api.spotify.com/v1/recommendations'
    
    