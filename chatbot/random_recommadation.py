#在mbti_song裡隨機推薦歌

from pymongo import MongoClient
import random
def random_recommendation():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    collection = db['mbti_song']
    
    # 使用聚合框架隨機選取三首歌曲
    pipeline = [
        {"$unwind": "$songs"},
        {"$sample": {"size": 3}}
    ]
    
    result = list(collection.aggregate(pipeline))
    
    # 提取歌曲資料和 MBTI 類型
    recommendations = [
        {
            "mbti": doc['MBTI'],
            "track name": doc['songs']['track name'],
            "artist name": doc['songs']['artist name'],
            "spotify url": doc['songs']['spotify url'],
            "image": doc['songs']['image']
        }
        for doc in result
    ]
    
    return recommendations

def hasmbti_recommendation(mbti, user_song):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    collection = db['mbti_song']
    all_songs = collection.find_one({'MBTI': mbti})
    
    if not all_songs or 'songs' not in all_songs:
        return random_recommendation()

    user_song_urls = []
    for song in user_song['tracks']:
        user_song_urls.append(song['spotify url'])
    
    # 過濾掉與 user_songs 中任何歌曲相同的歌曲
    filtered_songs = [song for song in all_songs['songs'] if song['spotify url'] not in user_song_urls]
    
    # 如果過濾後的歌曲少於三首，返回所有過濾後的歌曲
    if len(filtered_songs) < 3:
        additional_songs_needed = 3 - len(filtered_songs)
        unique_mbti_songs = {}
    
    while len(unique_mbti_songs) < additional_songs_needed:
        other_songs_pipeline = [
            {"$unwind": "$songs"},
            {"$sample": {"size": additional_songs_needed * 2}}  # 多取一些以便過濾重複的 MBTI 類別
        ]
        additional_songs = list(collection.aggregate(other_songs_pipeline))
        
        for doc in additional_songs:
            mbti = doc['MBTI']
            if mbti not in unique_mbti_songs:
                unique_mbti_songs[mbti] = {
                    "mbti": mbti,
                    "track name": doc['songs']['track name'],
                    "artist name": doc['songs']['artist name'],
                    "spotify url": doc['songs']['spotify url'],
                    "image": doc['songs']['image']
                }
            if len(unique_mbti_songs) >= additional_songs_needed:
                break

        additional_songs = list(unique_mbti_songs.values())
        filtered_songs.extend(additional_songs)
        
        return filtered_songs
    
    # 隨機選取三首歌曲
    recommendations = random.sample(filtered_songs, 3)
    
    return recommendations
    
# 測試範例
#print(random_recommendation())