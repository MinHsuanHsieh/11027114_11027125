import requests
import spotify_accesstoken
from Search_all.search_album import search_album, search_albumtrack
from Search_all.search_similarartists import search_similarartists
from pymongo import MongoClient
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
            album_id = lastest_album['id']
            album_tracks = search_albumtrack(album_id)
            client = MongoClient('mongodb://localhost:27017/')
            # 選擇資料庫
            db1 = client['spotify_data']
            # 選擇集合（collection）
            collection1 = db1['albums']
            document = {
                'artist name': artist_name,
                'lastest album': lastest_album,
                'album tracks': album_tracks
            }
            
            if collection1.find_one({'artist name': artist_name}): 
                collection1.update_one(
                    {'artist name': artist_name},
                    {'$set': {
                        'lastest album': lastest_album
                    }}
                )
            else:
                collection1.insert_one(document)
            
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