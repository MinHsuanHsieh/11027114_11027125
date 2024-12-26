def generate_category_buttons(current_category):
    categories = ["concert", "artist", "song"]
    category_buttons = []
    
    # 生成每個分類按鈕
    for category in categories:
        button = {
            "type": "bubble",
            "size": "micro",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": category.capitalize(),
                        "size": "xl",
                        "align": "center",
                        "color": "#000000" if category != current_category else "#FF0000"
                    }
                ]
            },
            "action": {
                "type": "message",
                "label": f"{category.capitalize()}",
                "text": f"Show {category.capitalize()}"
            }
        }
        category_buttons.append(button)
    
    return category_buttons

def handle_category_switch(category_content, selected_category):
    # 生成分類按鈕
    category_buttons = generate_category_buttons(selected_category)
    
    # 返回整合了分類按鈕和卡片內容的結構
    if category_content.get('type') == 'carousel':
        final_contents = category_buttons + category_content["contents"]
    else:
        final_contents = category_buttons + [category_content]
    print(final_contents)  # 用來檢查結構是否正確
    return {
        "type": "flex",
        "altText": f"{selected_category.capitalize()} Cards",
        "contents": {
            "type": "carousel",
            "contents": final_contents
        }
    }