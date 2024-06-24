import numpy as np
from pymongo import MongoClient
import pandas as pd

def get_data_sample( track_features ):
    flattened_data = []
    key_counts = {str(i) + '_count': 0 for i in range(12)}  # 初始化 key 計數器
    for track in track_features:
        audio_features = track['audio_features'][0]
        audio_features['track_name'] = track['track_name']
        flattened_data.append(audio_features)

        # 計算每個 key 的出現次數
        key_value = audio_features.get('key')
        if key_value is not None and 0 <= key_value <= 11:
            key_counts[str(key_value) + '_count'] += 1
    # 轉換為 DataFrame
    df = pd.DataFrame(flattened_data)
    # 現在你可以對 df 進行處理，例如計算平均值和標準差
    # 計算每個特徵的平均值和標準差
    df = df.select_dtypes(include=[np.number])
    mean_values = df.mean()
    std_values = df.std()
    for key, count in key_counts.items():
            df[key] = count
    # 創建一個新的 DataFrame，其中包含每個特徵的平均值和標準差
    data_sample = {
        'Inputs': {
            'data': pd.DataFrame({
                "danceability_mean": [mean_values["danceability"]],
                "danceability_stdev": [std_values["danceability"]],
                "energy_mean": [mean_values["energy"]],
                "energy_stdev": [std_values["energy"]],
                "loudness_mean": [mean_values["loudness"]],
                "loudness_stdev": [std_values["loudness"]],
                "mode_mean": [mean_values["mode"]],
                "mode_stdev": [std_values["mode"]],
                "speechiness_mean": [mean_values["speechiness"]],
                "speechiness_stdev": [std_values["speechiness"]],
                "acousticness_mean": [mean_values["acousticness"]],
                "acousticness_stdev": [std_values["acousticness"]],
                "liveness_mean": [mean_values["liveness"]],
                "liveness_stdev": [std_values["liveness"]],
                "valence_mean": [mean_values["valence"]],
                "valence_stdev": [std_values["valence"]],
                "tempo_mean": [mean_values["tempo"]],
                "tempo_stdev": [std_values["tempo"]],
                "instrumentalness_mean": [mean_values["instrumentalness"]],
                "instrumentalness_stdev": [std_values["instrumentalness"]],
                "0_count": [key_counts["0_count"]],
                "1_count": [key_counts["1_count"]],
                "2_count": [key_counts["2_count"]],
                "3_count": [key_counts["3_count"]],
                "4_count": [key_counts["4_count"]],
                "5_count": [key_counts["5_count"]],
                "6_count": [key_counts["6_count"]],
                "7_count": [key_counts["7_count"]],
                "8_count": [key_counts["8_count"]],
                "9_count": [key_counts["9_count"]],
                "10_count": [key_counts["10_count"]],
                "11_count": [key_counts["11_count"]]
                # ... 其他特徵
            })
        },
        'GlobalParameters': {"method": "predict"}
    }

    return data_sample