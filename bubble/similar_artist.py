def card(similar_artist):
  res = {
          "type": "bubble",
          "hero": {
            "type": "image",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "url": similar_artist['image']
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": similar_artist['name'],
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "style": "italic"
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
                "action": {
                  "type": "message",
                  "label": "Information",
                  "text": "Information-" + similar_artist['name']
                }
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "Spotify URL",
                  "uri": similar_artist['spotify_url']
                },
                "style": "link"
              }
            ]
          }
        }
  
  return res



def SimilarArtists(search_result):
    res = {
      "type": "carousel",
      "contents": [
        card(similar_artist) for similar_artist in search_result["similar artists"]
      ]
    }
    
    return res