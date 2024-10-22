import TrackFeatures
from pymongo import MongoClient
import data_transfer
import scoring_file_v_2_0_0
#預測專輯的MBTI

def predict( ):

    # 建立連線
    client = MongoClient('mongodb://localhost:27017/')

    # 選擇資料庫
    db1 = client['spotify_data']

    # 選擇集合（collection）
    collection1 = db1['albums']
    
    track_features = []
    # 獲取集合中的所有文件
    albums = collection1.find()

    # 遍歷每一筆資料
    for album in albums:
        for track in album.get('album tracks', []):
            track_id = track['id']
            track_name = track['name']
            data = TrackFeatures.Track_Audio_Features(track_id, track_name)
             # 確保 audio_features 存在且不是 None
            if data and 'audio_features' in data and data['audio_features']:
                track_features.append(data)
            
        data_sample = data_transfer.get_data_sample(track_features)
        prediction = scoring_file_v_2_0_0.run(data_sample['Inputs'], data_sample['GlobalParameters'])
        print( "16 classification : " + prediction['Results'][0])
        MBTI = prediction['Results'][0]
        
        print( "MBTI : " + MBTI)
        collection1.update_one(
            {'artist name': album['artist name']},
            {'$set': {'MBTI': MBTI}}
        )


scoring_file_v_2_0_0.init()
predict()