def no_result():
    res = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://developers-resource.landpress.line.me/fx/clip/clip1.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "text",
                            "text": "No results found",
                            "size": "lg",
                            "align": "center",
                            "margin": "md"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
    }
    
    return res