# coding=utf-8
from pymongo import MongoClient

def get_artist_info(artist_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['spotify_data']
    collection = db['artists']

    result = collection.find_one({'name': artist_name})

    if result:
        popularity = result['popularity']
        album = result['albums']
        latest_album = album[0] if album else None
        return f"The latest album of {artist_name} is {latest_album['album_name']}." + "\n" + artist_name + "'s popularity is: " + str(popularity)

    else:
        return f"Failed to find artist: {artist_name}"

if __name__ == "__main__":
    artist_name = 'artist_name'  # 叫盢 '美嘿' 蠢传稱璶琩高美嘿
    print(get_artist_info(artist_name))

