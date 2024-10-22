def ways_to_search():
    res = {
        "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.pinimg.com/564x/ae/5a/5a/ae5a5a8b1b338839c391c0aad4a0442b.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search anything u want",
                        "weight": "bold",
                        "size": "lg"
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
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search anything u want"
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
                },
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.pinimg.com/564x/8c/45/c5/8c45c58de4832658e892afd1efe170f9.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Search by category",
                        "weight": "bold",
                        "size": "lg"
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
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "select",
                        "text": "Search by category"
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