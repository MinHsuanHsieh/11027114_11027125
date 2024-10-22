from pymongo import MongoClient
from datetime import datetime, timedelta

def searchbydate(concert_date):
    # 連接到 MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concertdata']
    collection = db['articles']

    # 將傳入的日期字串轉換為 datetime 物件
    target_date = datetime.strptime(concert_date, '%Y-%m-%d')
    
    # 計算查詢的日期範圍（前後 7 天）
    start_date_range = target_date - timedelta(days=7)
    end_date_range = target_date + timedelta(days=7)

    # 查詢指定日期範圍內的文檔
    query = {
        "start_date": {
            "$gte": start_date_range,
            "$lte": end_date_range
        }
    }

    # 使用 pipeline 進行查詢和排序
    pipeline = [
        {"$match": query},
        {"$addFields": {
            "date_diff": {
                "$abs": {
                    "$subtract": [
                        "$start_date",  # 直接使用資料庫中的 datetime 格式日期
                        target_date
                    ]
                }
            }
        }},
        {"$sort": {"date_diff": 1}},
        {"$limit": 10}
    ]

    results = list(collection.aggregate(pipeline))

    # 處理查詢結果
    response = []
    for result in results:
        start_date = result['start_date'].strftime('%Y-%m-%d')
        end_date = result['end_date'].strftime('%Y-%m-%d')
        if start_date == end_date:
            date = start_date
        else:
            date = f"{start_date} - {end_date}"
        response.append({
            "title": result['title'],
            "link": result['articles_link'],
            "image": result['img'],
            "date": date
        })
        
    # 如果沒有找到匹配的結果
    if not response:
        return None

    return response