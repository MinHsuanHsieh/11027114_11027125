from flask import Flask, redirect, request, jsonify, url_for, g, render_template, session
import secrets
import urllib.parse
from pymongo import MongoClient
import requests
import base64
from flask_pymongo import PyMongo
import spotipy
from multiprocessing import Process
import os


os.chdir('/home/cynthia/chat_bot')

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/spotify"
mongo = PyMongo(app)
app.secret_key = os.urandom(24)  # 使用 os.urandom 生成一個隨機的字串作為 secret_key

# Spotify API 資訊
client_id = '777f43889e4643c1928a8a338de98082'
client_secret = '078fc9716eaf484b97f867f9875272b3'
redirect_uri = 'https://cynweb.lab214b.uk:5001/callback'

#登入路由，生成state和scope，然後重定向到Spotify登入頁面
@app.route('/')
def root():
    lineID = request.args.get('lineID')  # 從查詢參數獲取lineID
    state = secrets.token_hex(16) + '|' + lineID  # 將lineID加入到state參數中
    scope = 'user-read-private user-read-email user-read-recently-played user-top-read app-remote-control'
    query_params = urllib.parse.urlencode({
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'redirect_uri': redirect_uri,
        'state': state  # 傳遞修改後的state
    })
    auth_url = f'https://accounts.spotify.com/authorize?{query_params}'
    return redirect(auth_url)


#處理回調路由由
@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state', '')
    
    if not code:
        print("Error: No authorization code received.")
        return jsonify(error="No authorization code received"), 400
    
    try:
        _, lineID = state.split('|', 1)
    except ValueError:
        print("Error: Invalid state parameter format.")
        return jsonify(error="Invalid state parameter format"), 400
    
    auth_token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(auth_token_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        
        if not access_token:
            print("Error: Access token not found in response.")
            return jsonify(error="Failed to retrieve access token"), 400
        
        print(f"Access token: {access_token}")
        try:
            user_data = get_user_data(access_token, lineID)
            if user_data is None:
                return jsonify(error="Fail to get your data!!! Please make sure you enter the right email."), 500
            session['user'] = lineID  # 假設你將用戶資料儲存在 session 中
        except Exception as e:
            print(f"Error retrieving user data: {e}")
            return jsonify(error="Fail to get your data!!! Please make sure you enter the right email."), 500
        
        return render_template('successful_login.html')
    else:
        error_details = response.json().get('error', 'Unknown error')
        print(f"Error retrieving access token, status code {response.status_code}, details: {error_details}")
        return jsonify(error="Failed to retrieve access token"), 400



def get_user_data(access_token, lineID):
    user_info_url = 'https://api.spotify.com/v1/me'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(user_info_url, headers=headers)
    # 檢查響應是否成功
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!{response.status_code}')
    if response.status_code == 200:
        user_data = response.json()  # 取得使用者資料
        # 創建 Spotify 物件
        sp = spotipy.Spotify(auth=access_token)

        # 獲取使用者的 Spotify ID
        user_id = sp.current_user()['id']
        print(f"使用者 Spotify ID: {user_id}", "success find user id")
        existing_user = mongo.db.users.find_one({'spotify_user_id': user_id}) # 檢查使用者是否已存在
        
        # 獲取使用者喜歡的藝人
        top_artists = sp.current_user_top_artists(limit=10)['items']
        print("使用者喜歡的藝人:")
        if len(top_artists) == 0:
            print("unable to find top artists")
        else:   
            for artist in top_artists:
                print(artist['name'])
            print("success find top artists")

        # 獲取使用者喜歡的歌曲
        top_tracks = sp.current_user_top_tracks(limit=10)['items']
        print("使用者喜歡的歌曲:")
        if len(top_tracks) == 0:
            print("unable to find top tracks")
        else:
            for track in top_tracks:
                print(f"{track['name']} - {track['artists'][0]['name']}")
            print("success find top tracks")
        
        client = MongoClient('mongodb://localhost:27017/')
        # 選擇資料庫
        db1 = client['spotify']
        # 選擇集合（collection）
        collection1 = db1['users']
        user = {
            'line_user_id': lineID,
            'access_token': access_token,
            'spotify_user_id': user_id,
            'top_artists': top_artists,
            'top_tracks': top_tracks
        }
        if existing_user is None:
            # 不存在的話，創建使用者資料
            collection1.insert_one(user)
            print("success insert user data")
        else:
            # 已存在的話，更新使用者資料
            collection1.update_one({'spotify_user_id': user_id}, {'$set': user})
            print("success update user data")
        return user,jsonify(user_data=user_data)
    else:
        return None


def run_app():
    app.run(debug=True, port=3000, host='0.0.0.0', use_reloader=False)


def start_flask_app():
    # Create a new process that runs the Flask app
    process = Process(target=run_app)
    # Start the new process
    process.start()
