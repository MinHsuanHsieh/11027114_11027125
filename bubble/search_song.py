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
          "color": "#D0D0D0",
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
          "color": "#000000"
        }
      ]
    }
  }
  return res

def SearchSongs(search_result):
  res = {
    "type": "carousel",
    "contents": [
      card(track) for track in search_result["tracks"]
    ]
  }
  return res