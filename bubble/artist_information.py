def AtristCard(search_result):
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
                "url": search_result.get(f'images', 'https://agirls.aottercdn.com/media/be552c21-d4c2-4ad7-a437-83cf83253d0b.jpg')
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": search_result.get('artist name', 'No result found'), # 這裡要放藝人名稱
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
                        "text": "Genres",
                        "wrap": True,
                        "weight": "bold",
                        "size": "sm",
                        "flex": 1,
                        "decoration": "none",
                        "gravity": "center"
                    },
                    {
                        "type": "text",
                        "text": ", ".join(search_result.get("geners") if search_result.get("geners") else ["No geners found"]),
                        "wrap": True,
                        "weight": "bold",
                        "size": "sm",
                        "flex": 2
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Popularity",
                        "wrap": True,
                        "weight": "bold",
                        "size": "sm",
                        "flex": 1,
                        "decoration": "none",
                        "gravity": "center"
                    },
                    {
                        "type": "text",
                        "text": str(search_result["popularity"]), # 這裡要放藝人的人氣
                        "wrap": True,
                        "weight": "bold",
                        "size": "sm",
                        "flex": 2
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
                    "action": {
                    "type": "uri",
                    "label": "spotify url",
                    "uri": search_result["spotify url"] # 這裡要放藝人的spotify url
                    },
                    "position": "relative",
                    "flex": 0
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
                "url": search_result["lastest album"][0]['image'] # 這裡要放專輯
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": search_result["lastest album"][0]['name'], # 這裡要放專輯名稱
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "contents": []
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
                    "flex": 2,
                    "style": "primary",
                    "color": "#aaaaaa",
                    "action": {
                    "type": "uri",
                    "label": "spotify url",
                    "uri": search_result["lastest album"][0]['spotify_url'] # 這裡要放專輯的spotify url
                    }
                }
                ]
            }
            },
            {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "spacing": "xxl",
                "contents": [
                {
                    "type": "text",
                    "text": "Similar Artists",
                    "wrap": True,
                    "weight": "bold",
                    "size": "4xl",
                    "decoration": "none",
                    "gravity": "center",
                    "action": {
                    "type": "message",
                    "label": "Similar Artists",
                    "text": "Similar Artists"
                    },
                    "margin": "lg"
                }
                ],
                "borderWidth": "normal",
                "cornerRadius": "xxl",
                "backgroundColor": "#DCDCDC",
                "paddingEnd": "xxl"
            },
            "styles": {
                "body": {
                "separator": True
                }
            }
            }
        ]
        }
    return res