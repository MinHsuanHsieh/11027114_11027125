def card( url ):
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
                    "text": "請先點選此按鈕進行授權",
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
                    "style": "secondary",
                    "color": "#E6CFE6"
                }
                ]
            }
            },
            {
            
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.pinimg.com/736x/93/82/d9/9382d944e62b95292cf4fabbfb8a47ee.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "https://line.me/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "授權完後按此按鍵進行MBTI預測",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5,
                                "margin": "xxl"
                            }
                            ],
                            "borderWidth": "normal"
                        }
                        ]
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
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "點我看預測結果",
                        "text": "Start prediction"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                    ],
                    "flex": 0
                }
                
            }
        ]
                
    }
    return res