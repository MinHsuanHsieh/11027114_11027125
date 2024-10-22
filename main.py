from __future__ import unicode_literals
import re
import global_variable as gv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
import linebot.models
import random
import configparser
from datetime import datetime
import search_tracks, search_artists, spotify_authoration_new
from dialog import Dialog_Manager as DM
from bubble import search_song, similar_artist, artist_information, search_options, authoration_card, mbti_card, has_authoration, concert_option, concert_result, favorites_concert, show_faavorites, recommadation
from pymongo import MongoClient
from linebot.models import FlexSendMessage
from MBTI_predict import run
import scoring_file_v_2_0_0
from auto_email import email_spotify, chrome, open_spotify, delete_spotify
from fulltext import fulltextsearch
from search_concerts import searchbydate
from MBTI_feature import mbti_feature
import next_page
import mbti_song
import random_recommadation

app = gv.Flask(__name__)
app.secret_key = '11027114'
config = configparser.ConfigParser()
config.read('config.ini')

# LINE Bot API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
scoring_file_v_2_0_0.init()
browser = chrome() # 創建 Chrome 實例
open_spotify(browser) # 打開 Spotify 登入頁面


@app.route("/", methods=['POST'])
def callback():
    signature = gv.request.headers['X-Line-Signature']
    body = gv.request.get_data(as_text=True)
    app.logger.info("gv.request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        gv.abort(400)

    return 'OK'


is_searching = False
search_query = ''
global_user_id = None
DM.set_global_args('Searchall', 'search_result')
DM.set_global_args('Search_concert', 'page')
DM.set_global_args('Search_concert', 'result')
DM.set_global_args('Search_concert', 'favorites')

@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event: MessageEvent):
    reply = []
    result = DM.reply(event.source.user_id, event.message.text)
    global global_user_id
    global_user_id = event.source.user_id
    for msg_list in result:
        for msg in msg_list:
            reply.append(msg)

    if len(reply) > 0:
        line_bot_api.reply_message(event.reply_token, reply)
        
@handler.add(PostbackEvent)
def handle_postback(event: PostbackEvent):
    reply = []
    result = DM.reply(event.source.user_id, '_'.join(['postback', event.postback.params['date']]))
    global global_user_id
    global_user_id = event.source.user_id
    for msg_list in result:
        for msg in msg_list:
            reply.append(msg)

    if len(reply) > 0:
        line_bot_api.reply_message(event.reply_token, reply)
       
@DM.bind(r'postback.*', re=True)
def postback():
    _, selected_date = gv.g.current_user.current_input.split('_')

    # 執行日期查詢
    response = searchbydate(selected_date)
    gv.g.current_user.global_args['Search_concert']['result'] = response
    gv.g.current_user.global_args['Search_concert']['page'] = 1
    if response is None:
        return [TextSendMessage(text="No concert found.")]
    return next_page.get_concert(concert_result.Consert_results, 'Search By date', response, 0, 'offset')

@DM.bind('^Search By date(首|末)頁$', re=True)
def search_jump_page():
    msg = gv.g.current_user.current_input
    target_page = 1 if msg[14] == '首' else 99999
    # 取得當前查詢的結果
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By date', response, target_page, mode='absolute')


@DM.bind('^Search By date第\d+頁$', re=True)
def search_which_page():
    msg = gv.g.current_user.current_input
    page = msg[15:-1]
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By date', response, int(page), mode='absolute')


@DM.bind('Search By date下一頁')
def search_next_page():
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By date', response, 1, mode='offset')


@DM.bind('Search')
def search(): 
    return [FlexSendMessage(alt_text='Search',contents=search_options.Searchoption())]

@DM.bind('Search for concerts')
def search_concerts():
    return [FlexSendMessage(alt_text='Search',contents=concert_option.Searchoption())]

@DM.bind('Search By Keywords', [TextSendMessage(text="Please enter the keywords.")])
def search_by_keywords(event: MessageEvent):
     # 取得使用者輸入的關鍵字
    keywords = event
    response = fulltextsearch(keywords)
    gv.g.current_user.global_args['Search_concert']['result'] = response
    gv.g.current_user.global_args['Search_concert']['page'] = 1
    if response is None:
        return [TextSendMessage(text="No concert found.")]
    return next_page.get_concert(concert_result.Consert_results, 'Search By Keywords', response, 0, 'offset')


@DM.bind('^Search By Keywords(首|末)頁$', re=True)
def search_jump_page():
    msg = gv.g.current_user.current_input
    target_page = 1 if msg[18] == '首' else 99999
    # 取得當前查詢的結果
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By Keywords', response, target_page, mode='absolute')


@DM.bind('^Search By Keywords第\d+頁$', re=True)
def search_which_page():
    msg = gv.g.current_user.current_input
    page = msg[19:-1]
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By Keywords', response, int(page), mode='absolute')


@DM.bind('Search By Keywords下一頁')
def search_next_page():
    response = gv.g.current_user.global_args['Search_concert']['result']
    return next_page.get_concert(concert_result.Consert_results, 'Search By Keywords', response, 1, mode='offset')

@DM.bind('Concert information')
def concert_information():
    artist_name  = gv.g.current_user.global_args['Searchall']['search_result']['artist name']
    response = fulltextsearch(artist_name)
    gv.g.current_user.global_args['Search_concert']['result'] = response
    if response is None:
        return [TextSendMessage(text="No concert found.")]
    return [FlexSendMessage(alt_text='Search',contents=concert_result.Consert_results(response))]
    
@DM.bind(r"(.+)-add_to_favorites-(\d+)", re=True)
def add_to_favorites():
    # 取得用戶的輸入
    message_text = gv.g.current_user.current_input
    # 使用正則表達式提取消息中的信息
    pattern = r"(\d+)$"
    
    match = re.search(pattern, message_text)
    if match:
        index_str = match.group(1)
        print(f"Extracted Index: {index_str}")
    else:
        print("No number found.")
    
    try:
        index = int(index_str)
        page = gv.g.current_user.global_args['Search_concert']['page']
        index = gv.BUBBLE_MAX_PAGE*(page-1) + index
    except ValueError:
        return [TextSendMessage(text="Invalid index.")]
    
    # 確保用戶先進行了搜尋
    concert_list = gv.g.current_user.global_args['Search_concert']['result']
    #print(concert_list)
    if not concert_list:
        return [TextSendMessage(text="Please search for a concert first.")]
    if index < 0 or index >= len(concert_list):
        return [TextSendMessage(text="Invalid concert index.")]
    
    concert = concert_list[index]
    
    # 連接 MongoDB 並儲存收藏
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    collection = db['predict_result']
    
    user_id = gv.g.current_user.userID
    
    # 更新或插入收藏的演唱會資料
    collection.update_one(
        {'line_user_id': user_id},
        {'$addToSet': {'favorits': concert}},
        upsert=True
    )
    
    return [FlexSendMessage(alt_text='Search',contents=show_faavorites.show())]

@DM.bind(r"演唱會名稱:(.+)-delete_favorite-(.+)", re=True)
def cancel_favorite():
    # 取得用戶的輸入
    message_text = gv.g.current_user.current_input
    # 使用正則表達式提取消息中的信息
    pattern = r"演唱會名稱:(.+)-delete_favorite"
    
    match = re.search(pattern, message_text)
    if match:
        title = match.group(1).strip()
        print(f"Extracted Title: {title}")
    else:
        return [TextSendMessage(text="No title found.")]
    
    # 連接 MongoDB 並移除收藏
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    collection = db['predict_result']
    
    user_id = gv.g.current_user.userID
    
    # 從收藏的演唱會資料中移除
    result = collection.update_one(
        {'line_user_id': user_id},
        {'$pull': {'favorits': {'title': title}}}
    )
    
    if result.modified_count > 0:
        return [TextSendMessage(text="已取消收藏")]
    else:
        return [TextSendMessage(text="未找到指定的收藏項目")]
    
@DM.bind('Show Favorites')
def show_favorites():
    # 取得使用者的 ID
    user_id = gv.g.current_user.userID
    
    # 連接到 MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['line_bot']
    collection = db['predict_result']
    
    # 查詢收藏的演唱會
    result = collection.find_one({'line_user_id': user_id})
    try:
    
        gv.g.current_user.global_args['Search_concert']['favorites'] = result['favorits']
        gv.g.current_user.global_args['Search_concert']['page'] = 1
        # 過濾過期的演唱會
        today = datetime.now().date()
        valid_favorites = []
        for concert in result['favorits']:
            try:
                # 檢查是否是日期範圍
                if ' - ' in concert['date']:
                    # 分割開始日期和結束日期
                    start_date_str, end_date_str = concert['date'].split(' - ')
                    start_date = datetime.strptime(start_date_str.strip(), '%Y-%m-%d').date()
                    end_date = datetime.strptime(end_date_str.strip(), '%Y-%m-%d').date()
                    
                    # 如果當前日期在範圍內則為有效演唱會
                    if today <= end_date:
                        valid_favorites.append(concert)
                else:
                    # 單一日期的處理邏輯
                    concert_date = datetime.strptime(concert['date'], '%Y-%m-%d').date()
                    if concert_date >= today:
                        valid_favorites.append(concert)
            except KeyError as ke:
                print(f"Missing date key in concert: {concert}")
            except ValueError as ve:
                print(f"Date format error in concert: {concert['date']}")
            except Exception as e:
                print(f"Unexpected error with concert: {concert} - {str(e)}")

        # 更新用戶的全域參數
        gv.g.current_user.global_args['Search_concert'] = {
            'favorites': valid_favorites,
            'page': 1
        }
        
        #刪除過期的演唱會
        collection.update_one(
            {'line_user_id': user_id},
            {'$set': {'favorits': valid_favorites}}
        )
        
        # 如果沒有有效的收藏，返回提示訊息
        if not valid_favorites:
            return [TextSendMessage(text="No valid favorites found.")]
                
        return next_page.get_concert(favorites_concert.Consert_results, 'Show Favorites', result['favorits'], 0, 'offset')
    except:
        return [TextSendMessage(text="No valid favorites found.")]
    
@DM.bind('^Show Favorites(首|末)頁$', re=True)
def search_jump_page():
    msg = gv.g.current_user.current_input
    target_page = 1 if msg[14] == '首' else 99999
    # 取得當前查詢的結果
    response = gv.g.current_user.global_args['Search_concert']['favorites']
    return next_page.get_concert(favorites_concert.Consert_results, 'Show Favorites', response, target_page, mode='absolute')


@DM.bind('^Show Favorites第\d+頁$', re=True)
def search_which_page():
    msg = gv.g.current_user.current_input
    page = msg[15:-1]
    response = gv.g.current_user.global_args['Search_concert']['favorites']
    return next_page.get_concert(favorites_concert.Consert_results, 'Show Favorites', response, int(page), mode='absolute')


@DM.bind('Show Favorites下一頁')
def search_next_page():
    response = gv.g.current_user.global_args['Search_concert']['favorites']
    return next_page.get_concert(favorites_concert.Consert_results, 'Show Favorites', response, 1, mode='offset')

@DM.bind('^Information-', re = True)
def show_artist_information():
    search_keyword = gv.g.current_user.current_input[12:]
    return search_by_artist(search_keyword)
    
@DM.bind('Search for artists', [TextSendMessage(text="Please enter the singer name.")])
def search_by_artist(search_keyword: str):
    search_result = search_artists.Search_spotify(search_keyword, search_type='artist')
    if search_result is None:
        return [TextSendMessage(text="No artist found.")]
    else:
        gv.g.current_user.global_args['Searchall']['search_result'] = search_result
        return [FlexSendMessage(alt_text='Search',contents=artist_information.AtristCard(search_result))]

@DM.bind('Similar Artists')
def show_similar_artist():
    search_result = gv.g.current_user.global_args['Searchall']['search_result']
    if search_result is None:
        return [TextSendMessage(text="Please search for an artist first.")]
    else:
        return [FlexSendMessage(alt_text='Search',contents=similar_artist.SimilarArtists(search_result))]
   
@DM.bind('Search for songs', [TextSendMessage(text="Please enter the song name.")])
def search_songs(search_keyword: str):
    search_result = search_tracks.Search_spotify(search_keyword, search_type='track')
    if search_result is None:
        return [TextSendMessage(text="No song found.")]
    else:
        return [FlexSendMessage(alt_text='Search',contents=search_song.SearchSongs(search_result))]

@DM.bind('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', re=True)
def autho():
    email = gv.g.current_user.current_input
    browser.refresh()
    email_spotify(browser, email, gv.g.current_user.userID)
    delete_spotify(browser)
    url = f'https://cynweb.lab214b.uk:5001/?lineID={gv.g.current_user.userID}'
    return [FlexSendMessage(alt_text='authoration',contents=authoration_card.card(url))]

@DM.bind('重新授權')
def re_authoration():
    #檢查使用者是否授權
    client = MongoClient('mongodb://localhost:27017/')
    # 選擇資料庫
    db1 = client['spotify']
    # 選擇集合（collection）
    collection1 = db1['users']
    collection1.delete_one({'line_user_id': gv.g.current_user.userID})
    db2 = client['line_bot']
    collection2 = db2['predict_result']
    collection2.update_one(
        {'line_user_id': gv.g.current_user.userID},
        {'$unset': {'MBTI': "", 'song': ""}}
    )
    return[TextSendMessage(text="請輸入你在spotify的email: ")]

@DM.bind('MBTI')
def mbti():
    #檢查使用者是否授權
    client = MongoClient('mongodb://localhost:27017/')
    # 選擇資料庫
    db1 = client['spotify']
    # 選擇集合（collection）
    collection1 = db1['users']
    line_user = collection1.find_one({'line_user_id': gv.g.current_user.userID})
    if line_user is None:
        return[FlexSendMessage(alt_text='has_authoration',contents=has_authoration.card2())]
    else:
        return [FlexSendMessage(alt_text='has_authoration',contents=has_authoration.card())]
    
@DM.bind('授權')
def authoration():
    return [TextSendMessage(text="您還未授權，請輸入你在spotify的email: ")]

@DM.bind('Start prediction')
def MBTI_predict():
    #檢查使用者是否授權
    client = MongoClient('mongodb://localhost:27017/')
    # 選擇資料庫
    db1 = client['spotify']
    # 選擇集合（collection）
    collection1 = db1['users']
    db2 = client['line_bot']
    collection2 = db2['predict_result']
    line_user = collection1.find_one({'line_user_id': gv.g.current_user.userID})
    #如果還未授權
    if line_user is None:
        return[TextSendMessage(text="您還未授權，請輸入你在spotify的email: ")]
    
    #如果已經預測過MBTI
    prediction = collection2.find_one({'line_user_id': gv.g.current_user.userID})
    try:
        mbti = mbti_feature(prediction['MBTI'])
        ten_songs = prediction['song']
    except:
        mbti, ten_songs = run(gv.g.current_user.userID)
        if ten_songs is None:
            return [TextSendMessage(text="No data found.")]
        document = {
            'line_user_id': gv.g.current_user.userID,
            'MBTI': mbti['ename'],
            'song': ten_songs
        }
        
        if prediction is not None:
            collection2.update_one(
                {'line_user_id': gv.g.current_user.userID},
                {'$set': document}
            )
        else:
            collection2.insert_one(document)
            
        mbti_song.add_song_to_mbtidb(mbti['ename']) #將歌曲加入MBTI資料庫

    print(gv.g.current_user.userID + "的MBTI是" + mbti['ename'])
    
    return [FlexSendMessage(alt_text='Search',contents=mbti_card.mbti_song(mbti, ten_songs))]
    #return [TextSendMessage(text="根據您喜愛的歌曲預測您可能的MBTI為: " + MBTI)]

@DM.bind('範例帳號')
def example_account():
    line_id = 'U004a5378af172d595493458d69dde0c3'
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client['line_bot']
    collection2 = db2['predict_result']
    prediction = collection2.find_one({'line_user_id': line_id})
    mbti = mbti_feature(prediction['MBTI'])
    ten_songs = prediction['song']
    return [FlexSendMessage(alt_text='Search',contents=mbti_card.mbti_song(mbti, ten_songs))]
    
@DM.bind('推薦')
def recommendation():
    #檢查使用者是否預測過MBTI
    client = MongoClient('mongodb://localhost:27017/')
    db2 = client['line_bot']
    collection2 = db2['predict_result']
    line_user = collection2.find_one({'line_user_id': gv.g.current_user.userID})
    try:
        mbti = line_user['MBTI']
        user_song = line_user['song']
        recommendation_songs = random_recommadation.hasmbti_recommendation(mbti, user_song)
        return [FlexSendMessage(alt_text='Search',contents=recommadation.recommendation_card(recommendation_songs))]
    except:
        recommendation_songs = random_recommadation.random_recommendation()
        return [FlexSendMessage(alt_text='Search',contents=recommadation.recommendation_card(recommendation_songs))] #隨機推薦三首歌

@DM.bind('Feedback', [TextSendMessage(text='Please enter your feedback or visit the following link: https://forms.gle/hJKZnxBwCywAwb2S7' )])
def feedback(feedback: str):
    #檢查使用者是否授權
    client = MongoClient('mongodb://localhost:27017/')
    # 選擇資料庫
    db = client['line_bot']
    # 選擇集合（collection）
    collection = db['feedback']
    document = {
        'line_user_id': gv.g.current_user.userID,
        'feedback': feedback
    }
    
    collection.insert_one(document)
    
    return [TextSendMessage(text="Thank you for your feedback!")] 


@DM.bind('default')
def default():
    return [TextSendMessage(text="I don't understand what you are talking about.")]

@DM.bind('嗨')
def greeting():
    return [TextSendMessage(text="幹嘛")]
@DM.bind('你好')
def greeting():
    return [TextSendMessage(text="有事?")]
@DM.bind('哈囉')
def greeting():
    return [TextSendMessage(text="笑死怎樣")]
@DM.bind('早安')
def greeting():
    return [TextSendMessage(text="晚安")]

@DM.bind('掰掰')
def goodbye():
    return [TextSendMessage(text="掰掰")]

@DM.bind('沒事')
def nothing():
    return [TextSendMessage(text="好的")]

@DM.bind('謝謝')
def nothing():
    return [TextSendMessage(text="不客氣")]

@DM.bind('笨蛋')
def nothing():
    return [TextSendMessage(text="對不起")]

@DM.bind('蛤')
def nothing():
    return [TextSendMessage(text="蛤屁")]
@DM.bind('超好笑')
def laughing():
    return [TextSendMessage(text="多好笑")]

# 貼圖
stickers = {
    446: [1988, 2027],
    789: [10855, 10894],
    1070: [17839, 17878],
    6136: [10551376, 10551399],
    6325: [10979904, 10979927],
    6359: [11069848, 11069871],
    6632: [11825374, 11825398],
    11538: [51626494, 51626533]
}


@handler.add(linebot.models.MessageEvent, message=linebot.models.StickerMessage)
def reply_sticker_message(event: linebot.models.MessageEvent):
    choice = random.choice(list(stickers.keys()))
    reply = linebot.models.StickerSendMessage(package_id=choice, sticker_id=random.choice(
        range(stickers[choice][0], stickers[choice][1] + 1)))
    line_bot_api.reply_message(event.reply_token, reply)

@handler.default()
def default(event):
    app.logger.info(f"Received event: {event}")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="I don't understand what you are talking about.")
    )
# 執行 Flask
if __name__ == "__main__":
    spotify_authoration_new.start_flask_app()
    app.run(host='0.0.0.0')
    