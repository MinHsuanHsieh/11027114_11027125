import requests
def get_access_token():
    
    # 用你的 Spotify 應用的 Client ID 和 Client Secret 替換這些值
    CLIENT_ID = '777f43889e4643c1928a8a338de98082'
    CLIENT_SECRET = '078fc9716eaf484b97f867f9875272b3'

    # 獲取訪問令牌
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # 將響應轉換為 JSON
    auth_response_data = auth_response.json()

    # 保存訪問令牌
    access_token = auth_response_data['access_token']
    return access_token