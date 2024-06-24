from __future__ import unicode_literals
import os
import mysql.connector

import global_variable as gv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction
import linebot.models
import random
import configparser
import datetime
# from Search_all import search_tracks, search_artists, spotify_authoration
import search_tracks, search_artists, spotify_authoration
from dialog import Dialog_Manager as DM
from bubble import search_song, similar_artist, artist_information, search_options, authoration
from urllib.parse import parse_qs
from search_concerts import query_concerts
from pymongo import MongoClient
from linebot.models import FlexSendMessage
import linebot.models as lineSDK
from MBTI_predict import Mbti_predict, runmodel
from scoring_file_v_2_0_0 import init

app = gv.Flask(__name__)
app.secret_key = '11027114'
config = configparser.ConfigParser()
config.read('config.ini')

# LINE Bot API
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
init()

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
        
DM.set_global_args('Searchall', 'search_result')

@DM.bind('Search')
def search(): 
    return [FlexSendMessage(alt_text='Search',contents=search_options.Searchoption())]

@DM.bind('Search for concerts', [TextSendMessage(text="Please enter the date you want to search for.")])
def search_by_date(event: MessageEvent):
    try:
        concert_date = datetime.datetime.strptime(event, '%Y-%m-%d').date()
        response_message = query_concerts(concert_date)
    except ValueError:
        response_message = '格式錯誤，請輸入 YYYY-MM-DD'
    reply = TextSendMessage(text=response_message)
    return [reply]

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
    

@DM.bind('MBTI')
def mbti():
    #檢查使用者是否授權
    client = MongoClient('mongodb://localhost:27017/')
    # 選擇資料庫
    db1 = client['spotify']
    # 選擇集合（collection）
    collection1 = db1['users']
    #collection1.delete_one({'line_user_id': gv.g.current_user.userID})
    line_user = collection1.find_one({'line_user_id': gv.g.current_user.userID})
    if line_user is None:
        url = f'https://cynweb.lab214b.uk:10000/?lineID={gv.g.current_user.userID}'
        return [FlexSendMessage(alt_text='authoration',contents=authoration.authoration(url))]
    else:
        data_sample = Mbti_predict(gv.g.current_user.userID)
        MBTI = runmodel(data_sample)
        print(gv.g.current_user.userID + "的MBTI是" + MBTI)
        return [TextSendMessage(text="根據您喜愛的歌曲預測您可能的MBTI為: " + MBTI)]

@DM.bind('Feedback', [TextSendMessage(text='Please enter your feekback!' )])
def feedback(feedback: str):
    print(feedback)
    return [TextSendMessage(text="Thank you for your feedback!")] 


@DM.bind('default')
def default():
    return [TextSendMessage(text="I don't understand what you are talking about.")]


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
    spotify_authoration.start_flask_app()
    app.run(host='0.0.0.0')
    