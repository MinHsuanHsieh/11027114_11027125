from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# 連接MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['line_bot']
collection = db['users_mbti']

# 提取數據
data = list(collection.find({}))

# 將數據轉換為Pandas DataFrame
df = pd.DataFrame(data)

# 處理嵌套的數據
def unpack_track_features(track_features):
    if track_features and 'audio_features' in track_features[0]:
        return {key: track_features[0]['audio_features'][0][key] for key in track_features[0]['audio_features'][0]}
    return {}

# 展開音樂特徵
df['unpacked_features'] = df['track_features'].apply(unpack_track_features)
df_features = df['unpacked_features'].apply(pd.Series)

# 合併數據
df_final = pd.concat([df.drop(['unpacked_features', 'track_features'], axis=1), df_features], axis=1)

# 清理嵌套列表
def flatten_list(data_list):
    if isinstance(data_list, list):
        return [item for sublist in data_list for item in (sublist if isinstance(sublist, list) else [sublist])]
    return data_list

df_final['artist_genres'] = df_final['artist_genres'].apply(flatten_list)

# 重置索引
df_final = df_final.reset_index(drop=True)

# 可視化MBTI類型與舞動性的關係並保存圖像
plt.figure(figsize=(14, 7))
sns.barplot(data=df_final, x='mbti', y='danceability')
plt.title('Danceability by MBTI Type')
plt.xticks(rotation=45)
plt.savefig('/home/cynthia/chat_bot/database/danceability_by_mbti.png')  # 指定保存路徑
plt.close()

# 可視化MBTI類型與能量的關係並保存圖像
plt.figure(figsize=(14, 7))
sns.boxplot(data=df_final, x='mbti', y='energy')
plt.title('Energy by MBTI Type')
plt.xticks(rotation=45)
plt.savefig('/home/cynthia/chat_bot/database/energy_by_mbti.png')  # 指定保存路徑
plt.close()

# 處理和可視化音樂類型與MBTI類型的關係並保存圖像
df_final = df_final.dropna(subset=['artist_genres'])  # 確保沒有NA值
df_final = df_final.explode('artist_genres')
music_genres = df_final['artist_genres'].value_counts().nlargest(10).index.tolist()
df_top_genres = df_final[df_final['artist_genres'].isin(music_genres)]

plt.figure(figsize=(14, 7))
sns.countplot(data=df_top_genres, x='artist_genres', hue='mbti', palette='viridis')
plt.title('Top Music Genres by MBTI Type')
plt.xticks(rotation=90)
plt.savefig('/home/cynthia/chat_bot/database/top_music_genres_by_mbti.png')  # 指定保存路徑
plt.close()

# 關閉MongoDB連接
client.close()
