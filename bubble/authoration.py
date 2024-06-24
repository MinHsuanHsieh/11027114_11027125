def authoration( url ):
    res = {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": "https://i.pinimg.com/736x/7b/7e/76/7b7e76377821d053ce135c20c68f9c69.jpg"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "Please Authoration First",
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "select",
                    "uri": url
                    },
                    "style": "primary"
                }
                ]
            }
            }
        ]
                
    }
    return res