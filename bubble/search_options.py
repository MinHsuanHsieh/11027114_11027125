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
                    "url": "https://i.pinimg.com/564x/8f/b3/b5/8fb3b5a87544f51c449b6886ac53f018.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search for concerts",
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
                            "text": "查詢演唱會資訊",
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
                    "text": "Search for concerts"
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
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search for concerts"
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
                    "url": "https://i.pinimg.com/564x/00/7b/53/007b53489b818562f84529a23094ec3f.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search for artists",
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
                            "text": "查詢藝人資訊",
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
                    "label": "Search for artists",
                    "text": "Search for artists"
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
                        "color": "#aaaaaa",
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search for artists"
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
                    "url": "https://i.pinimg.com/564x/35/e1/07/35e1074848a8b2053552fffc6cf875d3.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search for songs",
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
                            "text": "查詢歌曲資訊",
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
                    "label": "Search for songs",
                    "text": "Search for songs"
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
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search for songs"
                        }
                    }
                    ]
                }
                }
            ]
            }
    return res
        
    