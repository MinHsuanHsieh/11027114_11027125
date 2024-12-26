def show():
    res = {
        
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "已加入收藏清單",
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
                    "style": "primary",
                    "color": "#7384C0",
                    "action": {
                    "type": "message",
                    "label": "Show Favorites",
                    "text": "Show Favorites"
                    }
                }
                ]
            }
            }
        ]
        
    }
    
    return res