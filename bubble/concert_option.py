def Searchoption():
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
                    "url": "https://i.pinimg.com/564x/69/59/74/695974fd7641f921b6ca1e64c14250c9.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search By Date",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "依日期查詢(結果為選擇日期前後一週資訊)",
                            "wrap": True,
                            "weight": "bold",
                            "size": "md",
                            "flex": 0
                        }
                        ]
                    }
                    ],
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "Search By Date"
                    }
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
                        "type": "datetimepicker",
                        "label": "select",
                        "mode": "date",
                        "data": "Search By Date"
                        }
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": "https://i.pinimg.com/564x/68/30/3c/68303c4b7bab8b335f9600f61f57523b.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search By Keywords",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "flex": 1,
                        "contents": [
                        {
                            "type": "text",
                            "text": "依關鍵字查詢",
                            "wrap": True,
                            "weight": "bold",
                            "size": "md",
                            "flex": 0
                        }
                        ]
                    }
                    ],
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "Search By Keywords"
                    }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "flex": 2,
                        "style": "secondary",
                        "color": "#E6CFE6",
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search By Keywords"
                        }
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": "https://i.pinimg.com/564x/ef/9c/78/ef9c7833e4581b811516b20a06bb20c8.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Show Favorites", 
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "flex": 1,
                        "contents": [
                        {
                            "type": "text",
                            "text": "查看收藏清單",
                            "wrap": True,
                            "weight": "bold",
                            "size": "md",
                            "flex": 0
                        }
                        ]
                    }
                    ],
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "Show Favorites"
                    }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "flex": 2,
                        "style": "primary",
                        "color": "#7384C0",
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Show Favorites"
                        }
                    }
                    ]
                }
                }
                
            ]
            }
    return res
        
    