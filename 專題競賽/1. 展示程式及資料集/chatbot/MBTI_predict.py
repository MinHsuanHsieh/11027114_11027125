import TrackFeatures
from pymongo import MongoClient
import data_transfer
import scoring_file_v_2_0_0
import search_tracks
from MBTI_feature import mbti_feature

def Mbti_predict( line_id ):

    # 建立連線
    client = MongoClient('mongodb://localhost:27017/')

    # 選擇資料庫
    db1 = client['spotify']

    # 選擇集合（collection）
    collection1 = db1['users']
    
    track_features = []
    ten_songs = []
    line_user = collection1.find_one({'line_user_id': line_id})
    
    if line_user is None or line_user['top_tracks'] == []:
        return None, None
    for track in line_user['top_tracks']:
        track_id = track['id']
        track_name = track['name']
        artistname = track['artists'][0]['name']
        data = TrackFeatures.Track_Audio_Features(track_id, track_name)
        search_result = search_tracks.Search_spotify(track_name, search_type='track')
        for result in search_result['tracks']:
            if result['artist name'] == artistname:
                ten_songs.append(result)
                break
        track_features.append(data)
    ten_songs = {
        'tracks': ten_songs[:10]
    }
    data_sample = data_transfer.get_data_sample(track_features)
    return data_sample, ten_songs
    
def runmodel( data_sample ):
    prediction = scoring_file_v_2_0_0.run(data_sample['Inputs'], data_sample['GlobalParameters'])
    print( "16 classification : " + prediction['Results'][0])
    MBTI = prediction['Results'][0]
    return MBTI

def run( user_id ):
    data_sample, ten_songs = Mbti_predict( user_id )
    if data_sample is None:
        return None, None

    MBTI = runmodel(data_sample)
    mbti = mbti_feature( MBTI )
    return mbti, ten_songs
