#建立一個mbti音樂資料庫分成16個類別
#每個類別有一個list，裡面放入該類別的歌曲
from pymongo import MongoClient

def add_song_to_mbtidb(mbti):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    target_collection = db['mbti_song']
    source_collection = db['predict_result']

    #mbti_list = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
    #for mbti in mbti_list:
    result = source_collection.find({'MBTI': mbti})
    songs = []
    seen_tracks = set()
    
    # 取得目標資料庫中已經存在的歌曲
    existing_songs = target_collection.find_one({'MBTI': mbti})
    if existing_songs:
        for song in existing_songs.get('songs', []):
            seen_tracks.add(song['spotify url'])

    for doc in result:
        if 'song' in doc:
            for song in doc['song']['tracks']:
                track_id = song['spotify url']
                if track_id not in seen_tracks:
                    seen_tracks.add(track_id)
                    songs.append({
                        'track name': song['track name'],
                        'artist name': song['artist name'],
                        'spotify url': song['spotify url'],
                        'image': song['image']
                    })
    if songs:
        formatted_songs = {'tracks': songs}
        if target_collection.find_one({'MBTI': mbti}):
            target_collection.update_one({'MBTI': mbti}, {'$set': {'songs': songs}})
        else:
            target_collection.insert_one({'MBTI': mbti, 'songs': songs})

        print(f"成功將 MBTI 類型為 {mbti} 的歌曲資料存進目標資料庫。")
    else:
        print(f"沒有找到 MBTI 類型為 {mbti} 的歌曲資料。")
