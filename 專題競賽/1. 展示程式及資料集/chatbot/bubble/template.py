from linebot.models import  TemplateSendMessage, CarouselTemplate,  CarouselColumn
from linebot.models import MessageAction
from linebot.models import URIAction

def Template_search():
    
    return TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/32/06/f2/3206f2586f9bb86fa763f41104ba2992.jpg',
                    title='查詢演唱會資訊',
                    text='狗勾負責',
                    actions=[
                        MessageAction(
                            label='search by date',
                            text='search by date'
                        )
                        
                        
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/58/0d/79/580d79fbcfa11d21cf85c4d3f4b52c48.jpg',
                    title='查詢歌曲或歌手資訊',
                    text='喵喵負責',
                    actions=[
                        MessageAction(
                            label='search on spotify',
                            text='search on spotify'
                        )
                        
                    ]
                )
            ]
        )
    )
    
def Template_artistorsong():
    return TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/32/06/f2/3206f2586f9bb86fa763f41104ba2992.jpg',
                    title='查詢歌手資訊',
                    text='狗勾負責',
                    actions=[
                        MessageAction(
                            label='查詢歌手資訊',
                            text='查詢歌手資訊'
                        )
                        
                        
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/58/0d/79/580d79fbcfa11d21cf85c4d3f4b52c48.jpg',
                    title='查詢歌曲資訊',
                    text='喵喵負責',
                    actions=[
                        MessageAction(
                            label='查詢歌曲資訊',
                            text='查詢歌曲資訊'
                        )
                        
                    ]
                )
            ]
        )
    )

def Template_artist():
    return TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/32/06/f2/3206f2586f9bb86fa763f41104ba2992.jpg',
                    title='藝人資訊',
                    text='狗勾負責',
                    actions=[
                        MessageAction(
                            label='曲風&受歡迎程度',
                            text='曲風&受歡迎程度'
                        ),
                        
                        URIAction(
                            label='Spotify URL',
                            uri='https://steam.oxxostudio.tw'
                        )
                        
                        
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/32/06/f2/3206f2586f9bb86fa763f41104ba2992.jpg',
                    title='最新專輯',
                    text='狗勾負責',
                    actions=[
                        MessageAction(
                            label='more...',
                            text='more...'
                        ) 
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/32/06/f2/3206f2586f9bb86fa763f41104ba2992.jpg',
                    title='相似藝人',
                    text='狗勾負責',
                    actions=[
                        MessageAction(
                            label='相似藝人',
                            text='相似藝人'
                        )
                    ]
                )
            
            ]
        )
    )
    
def Template_song():
    return TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/58/0d/79/580d79fbcfa11d21cf85c4d3f4b52c48.jpg',
                    title='歌曲資訊',
                    text='喵喵負責',
                    actions=[
                        URIAction(
                            label='Spotify URL',
                            uri='https://steam.oxxostudio.tw'
                        ),
                        MessageAction(
                            label='藝人資訊',
                            text='藝人資訊'
                        ),
                        
                        
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/58/0d/79/580d79fbcfa11d21cf85c4d3f4b52c48.jpg',
                    title='歌曲資訊',
                    text='喵喵負責',
                    actions=[
                        URIAction(
                            label='Spotify URL',
                            uri='https://steam.oxxostudio.tw'
                        ),
                        MessageAction(
                            label='藝人資訊',
                            text='藝人資訊'
                        ),
                        
                        
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.pinimg.com/564x/58/0d/79/580d79fbcfa11d21cf85c4d3f4b52c48.jpg',
                    title='歌曲資訊',
                    text='喵喵負責',
                    actions=[
                        URIAction(
                            label='Spotify URL',
                            uri='https://steam.oxxostudio.tw'
                        ),
                        MessageAction(
                            label='藝人資訊',
                            text='藝人資訊'
                        ),
                        
                        
                    ]
                )
            
            ]
        )
    )