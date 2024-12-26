def card():
    res = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "MBTI",
                "weight": "bold",
                "size": "xl"
            },
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
                        "text": "您已經授權過",
                        "color": "#aaaaaa",
                        "size": "xl",
                        "flex": 1,
                        "weight": "bold"
                    }
                    ]
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
                "style": "secondary",
                "color": "#E6CFE6",
                "height": "md",
                "action": {
                "type": "message",
                "label": "重新授權",
                "text": "重新授權"
                },
                "gravity": "top",
                "margin": "none",
                "position": "relative"
            },
            {
                "type": "button",
                "style": "primary",
                "color": "#7384C0",
                "height": "md",
                "action": {
                "type": "message",
                "label": "點我看預測結果",
                "text": "Start prediction"
                },
                "scaling": True,
                "margin": "lg"
            },
            {
                "type": "button",
                "style": "primary",
                "color": "#E6CFE6",
                "height": "md",
                "action": {
                "type": "message",
                "label": "推薦",
                "text": "推薦"
                },
                "scaling": True,
                "margin": "lg"
            }
            ],
            "flex": 0
        }
    }
    
    return res

def card2():
    res = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "MBTI",
                "weight": "bold",
                "size": "xl"
            },
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
                        "text": "您還未授權過",
                        "color": "#aaaaaa",
                        "size": "xl",
                        "flex": 1,
                        "weight": "bold"
                    }
                    ]
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
                "style": "secondary",
                "color": "#E6CFE6",
                "height": "md",
                "action": {
                "type": "message",
                "label": "授權",
                "text": "授權"
                },
                "gravity": "top",
                "margin": "none",
                "position": "relative"
            },
            {
                "type": "button",
                "style": "primary",
                "color": "#7384C0",
                "height": "md",
                "action": {
                "type": "message",
                "label": "範例帳號",
                "text": "範例帳號"
                },
                "scaling": True,
                "margin": "lg"
            },
            {
                "type": "button",
                "style": "secondary",
                "color": "#E6CFE6",
                "height": "md",
                "action": {
                "type": "message",
                "label": "推薦",
                "text": "推薦"
                },
                "scaling": True,
                "margin": "lg"
            }
            ],
            "flex": 0
        }
    }
    
    return res