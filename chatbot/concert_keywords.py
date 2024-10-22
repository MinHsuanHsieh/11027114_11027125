from pymongo import MongoClient

def concert_keywords(keywords):

    # 連接到 MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concertdata']
    collection = db['articles']

    # 使用正則表達式查詢包含關鍵字的文檔
    query = {"title": {"$regex": keywords, "$options": "i"}}  # $options: "i" 表示不區分大小寫
    results = collection.find(query)

    # 處理查詢結果
    response = []
    for result in results:
        start_date = result['start_date']
        end_date = result['end_date']
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
