def mbti_card(mbti): 
    res = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": mbti['url'],
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
                "type": "text",
                "weight": "bold",
                "size": "xl",
                "text": mbti['cname']
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
                        "text": mbti['feature'],
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
        }
    }
    return res

def card(track):
  res = {
    "type": "bubble",
    "hero": {
      "type": "image",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "url": track['image']
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "sm",
      "contents": [
        {
          "type": "text",
          "text": track['track name'],
          "wrap": True,
          "weight": "bold",
          "size": "xl",
          "style": "italic"
        },
        {
          "type": "box",
          "layout": "baseline",
          "contents": [
            {
              "type": "text",
              "text": track['artist name'],
              "wrap": True,
              "weight": "bold",
              "size": "md",
              "flex": 0
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
          "action": {
            "type": "message",
            "label": "artist information",
            "text": "Information-" + track['artist name']
          }
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "Spotify URL",
            "uri": track['spotify url']
          },
          "style": "primary",
          "color": "#7384C0"
        }
      ]
    }
  }
  return res

def mbti_song(mbti, search_result):
  res = { 
    "type": "carousel",
    "contents": [
      mbti_card(mbti)
    ] + [card(track) for track in search_result["tracks"][:5]]
  }
  return res