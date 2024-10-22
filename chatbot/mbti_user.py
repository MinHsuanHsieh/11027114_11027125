#存user id and mbti and 喜歡藝人的曲風 and 喜歡的前十首歌曲的資料
import TrackFeatures
from pymongo import MongoClient
# 建立連線
client = MongoClient('mongodb://localhost:27017/')

# 選擇資料庫
db1 = client['spotify']

# 選擇集合（collection）
collection1 = db1['users']

db2 = client['line_bot']
collection2 = db2['mbti']

db3 = client['line_bot']
collection3 = db3['users_mbti']
# 查詢所有資料
for user in collection1.find():
    track_features = []
    artist_genres = []
    line_id = user['line_user_id']
    print(line_id)
    usermbti = collection2.find_one({"user_id": line_id})
    if usermbti is None:
        print('No MBTI data found')
    else:
        mbti = usermbti['mbti']
        print(mbti)
        # 取得藝人的 genres
    for artist in user['top_artists']:
        artist_genres.append(artist['genres'])
        #print('Artist Genres:', artist_genres)
    
    # 取得每首歌的 id 和名字
    for track in user['top_tracks']:
        track_id = track['id']
        track_name = track['name']
        data = TrackFeatures.Track_Audio_Features(track_id, track_name)
        track_features.append(data)
    #print(data)
    
    alldata = {
        'line_id': line_id,
        'mbti': mbti,
        'artist_genres': artist_genres,
        'track_features': track_features
    }

    collection3.insert_one(alldata)