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
                    "url": "https://i.pinimg.com/564x/5e/4e/91/5e4e915572dc9b9a00a4b39e8ab77102.jpg"
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
                        "color": "#7384C0",
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
                    "url": "https://i.pinimg.com/564x/9d/a5/be/9da5be9dcd2e03b6b9856857face1dea.jpg"
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
                        "style": "secondary",
                        "color": "#E6CFE6",
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
                    "url": "https://i.pinimg.com/564x/a6/cf/0c/a6cf0cb8f9b4386a3a13068095eb7449.jpg"
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
                        "color": "#7384C0",
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
        
    