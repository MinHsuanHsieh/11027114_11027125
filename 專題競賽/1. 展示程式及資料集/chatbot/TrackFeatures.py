import spotify_accesstoken
import requests
def Track_Audio_Features(track_id, track_name):
    access_token = spotify_accesstoken.get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # 搜索項目，替換 'keyword' 為你的搜索關鍵字
    SEARCH_URL = 'https://api.spotify.com/v1/audio-features?ids=' + track_id

    # Send the GET request to the Spotify API
    response = requests.get(SEARCH_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        data['track_name'] = track_name
        return data
    