import TrackFeatures
from pymongo import MongoClient
import data_transfer
from scoring_file_v_2_0_0 import init, run
def Mbti_predict( line_id ):

    # 建立連線
    client = MongoClient('mongodb://localhost:27017/')

    # 選擇資料庫
    db1 = client['spotify']

    # 選擇集合（collection）
    collection1 = db1['users']
    
    track_features = []
    
    line_user = collection1.find_one({'line_user_id': line_id})
    
    for track in line_user['top_tracks']:
        track_id = track['id']
        track_name = track['name']
        data = TrackFeatures.Track_Audio_Features(track_id, track_name)
        track_features.append(data)
    
    data_sample = data_transfer.get_data_sample(track_features)
    return data_sample
    
def runmodel( data_sample ):
    prediction = run(data_sample['Inputs'], data_sample['GlobalParameters'])
    return prediction['Results'][0]
    