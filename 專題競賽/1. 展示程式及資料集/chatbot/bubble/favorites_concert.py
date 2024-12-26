def result(title, link, image, date, index):
    res = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": image,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": title,
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
                        "text": "Date",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": date,
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
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
                "height": "sm",
                "action": {
                "type": "uri",
                "label": "Url",
                "uri": link
                }
            },
            {
                "type": "button",
                "style": "primary",
                "color": "#7384C0",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "Delete favorite",
                "text": f"演唱會名稱:{title}-delete_favorite-{index}"
                }
            }
            ],
            "flex": 0
        }
        }
    
    return res

def Consert_results(response):
    res = {
      "type": "carousel",
      "contents": [
        result(item['title'], item['link'], item['image'], item['date'], index) 
        for index, item in enumerate(response[:9])
      ]
    }
    
    return res