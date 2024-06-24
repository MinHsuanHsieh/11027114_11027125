import requests
import spotify_accesstoken
from Search_all.search_album import search_album
from Search_all.search_similarartists import search_similarartists
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

        if data['artists']['items']:
            # Get the first result
            item = data['artists']['items'][0]

            # Extract the 'spotify' url, track name, and artist name from the first result
            artist_name = item['name']
            id = item['id']
            spotify_url = item['external_urls']['spotify']
            geners = item['genres']
            image = item['images'][0]['url'] if item['images'] else None
            popularity = item['popularity']
            
            similar_artists = search_similarartists(id)
            lastest_album = search_album(id)
            #print(f"Artist Name: {artist_name}, Spotify URL: {spotify_url}, Geners: {geners}, Images: {image}, Popularity: {popularity}, Similar Artists: {similar_artists}, Lastest Album: {lastest_album}")
            return {
                'artist name': artist_name,
                'spotify url': spotify_url,
                'geners': geners,
                'images': image,
                'popularity': popularity,
                'similar artists': similar_artists,
                'lastest album': lastest_album
            }
        
        else:
            return None