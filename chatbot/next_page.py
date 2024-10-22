from typing import Literal
from bubble import next_page_card, concert_result
import math
import json
import linebot.models as lineSDK
import global_variable as gv

def page_bar(current_page: int, num_of_pages: int, function_name: str, width: int = 11):
    middle = math.floor(width / 2)
    start_index = current_page - middle if current_page - middle >= 1 else 1
    end_index = current_page + middle if current_page + middle <= num_of_pages else num_of_pages
    result = []
    if end_index == num_of_pages:
        for i in range(end_index, end_index - width, -1):
            if i <= 0:
                break
            result.insert(0, lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label=i, text=f"{function_name}第{i}頁")))
    else:
        for i in range(start_index, start_index + width):
            if i > num_of_pages:
                break
            result.append(lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label=i, text=f"{function_name}第{i}頁")))

    if current_page > 1:
        result.insert(0, lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='首頁', text=f'{function_name}首頁')))

    if current_page < num_of_pages:
        result.append(lineSDK.QuickReplyButton(action=lineSDK.MessageAction(label='末頁', text=f'{function_name}末頁')))

    return result

def get_concert(card, functionname, result, page=0, mode: Literal['absolute', 'offset'] = 'absolute'):
    reply_arr = []
    try:
        # 設定或更新頁數
        if mode == 'absolute':
            gv.g.current_user.global_args['Search_concert']['page'] = page
        else:
            gv.g.current_user.global_args['Search_concert']['page'] += page
        
        # 獲取目前頁數
        current_page = gv.g.current_user.global_args['Search_concert']['page']
        
        # 計算總頁數
        num_of_result = len(result)
        total_page = math.ceil(num_of_result / gv.BUBBLE_MAX_PAGE)
        
        # 確保頁數在有效範圍內
        if current_page > total_page:
            current_page = total_page
        elif current_page <= 0:
            current_page = 1
        
        # 更新使用者的當前頁數
        gv.g.current_user.global_args['Search_concert']['page'] = current_page
        
        # 取得當前頁面的結果
        start_index = (current_page - 1) * gv.BUBBLE_MAX_PAGE
        end_index = start_index + gv.BUBBLE_MAX_PAGE
        current_results = result[start_index:end_index]
        
        # 如果沒有結果
        if not current_results:
            reply_arr.append(lineSDK.TextSendMessage(text="No concert found."))
            return reply_arr
        
        # 準備回應訊息
        flex_contents = card(current_results)
        # 如果還有下一頁，則添加下一頁卡片
        if current_page < total_page:
            next_card = next_page_card.next_page_card(functionname)
            flex_contents['contents'].append(next_card)
            
        # 生成快速回覆按鈕
        quick_reply_buttons = page_bar(current_page, total_page, functionname)
        
        # 添加快速回覆按鈕和「下一頁」卡片
        flex_message = lineSDK.FlexSendMessage(
            alt_text="查詢結果",
            contents=flex_contents,
            quick_reply=lineSDK.QuickReply(items=quick_reply_buttons)
        )
        reply_arr.append(flex_message)
        
    except Exception as e:
        reply_arr.append(lineSDK.TextSendMessage(text=f"查詢失敗，錯誤訊息：{str(e)}"))
    
    return reply_arr



