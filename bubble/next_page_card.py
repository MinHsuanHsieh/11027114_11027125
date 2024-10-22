def next_page_card(text):
    res = {
        "type": "bubble",
        "size": "mega",
         "hero": {
            "type": "image",
            "url": "https://i.pinimg.com/736x/84/b3/bf/84b3bfee61eaf2968269d7cae1499db5.jpg",
            "size": "full",
            "aspectRatio": "2:3",
            "aspectMode": "cover",
            "action": {
                "type": "message",
                "label": f"{text}下一頁",
                "text": f"{text}下一頁"
            }
        }
    }
    return res


def next_page_card_detail(text):
    res = {
        "type": "bubble",
        "size": "kilo",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": ">",
                            "size": "5xl",
                            "color": "#777777FF",
                            "offsetBottom": "xs"
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "borderWidth": "bold",
                    "borderColor": "#777777FF",
                    "cornerRadius": "90px",
                    "width": "60%",
                    "action": {
                        "type": "message",
                        "label": f"{text}下一頁",
                        "text": f"{text}下一頁"
                    }
                }
            ],
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor":"#00000000"
        }
    }
    return res