from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# 假設 df1 是第一個數據集（Spotify 數據），df2 是第二個數據集（MBTI 數據）
# 兩個 DataFrame 都需要有一個 'user_id' 列以便於合併
client = MongoClient('mongodb://localhost:27017/')
db = client['spotify']
collection = db['users']

# 從集合中提取資料
data = collection.find()

# 轉換資料到 pandas DataFrame
df1 = pd.DataFrame(list(data))

client = MongoClient('mongodb://localhost:27017/')
db = client['line_bot']
collection = db['mbti']
# 從集合中提取資料
data = collection.find()
# 轉換資料到 pandas DataFrame
df2 = pd.DataFrame(list(data))
# 數據合併
combined_df = pd.merge(df1, df2, on='line_user_id')

# 組織數據以進行分析
# 這裡的組織方式將取決於 'top_artists' 和 'top_tracks' 數據的具體結構
# 可以進行資料清洗和轉換
# 例如：轉換 JSON 結構的 top_artists 和 top_tracks
df1['top_artists'] = df1['top_artists'].apply(lambda x: ', '.join(artist['name'] for artist in x))
df1['top_tracks'] = df1['top_tracks'].apply(lambda x: ', '.join(track['name'] for track in x))
# 假設我們想要找出每個 MBTI 類型的用戶最喜歡的藝術家
top_artist_by_mbti = combined_df.groupby('mbti')['top_artists'].apply(lambda x: x.mode())

# 可視化結果
top_artist_by_mbti.plot(kind='bar')
plt.show()
# MongoDB 連線設置

# 將 DataFrame 保存為 Excel 文件
#df.to_excel(r'C:\Users\t9208\桌面\spotifyuser.xlsx', index=False)
print("success")
