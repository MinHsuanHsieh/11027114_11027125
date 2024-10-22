from pymongo import MongoClient
from jieba import analyse

def preprocess_text(text):
    # 使用 jieba 進行二元分詞
    words = list(analyse.extract_tags(text, topK=200, withWeight=False, allowPOS=()))
    return " ".join(words)

def add_fulltext_index():
    # 連接到 MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concertdata']
    collection = db['articles']
    
    try:
        # 刪除舊的索引
        collection.drop_index("title_text_introduce_text_start_date_text_end_date_text_location_text")

        # 添加 FULLTEXT 索引到指定欄位
        collection.create_index([
            ('title_processed', 'text'),
            ('introduce_processed', 'text'),
            ('start_date', 'text'),
            ('end_date', 'text'),
            ('location_processed', 'text')
        ])
        print("FULLTEXT index added to collection 'articles' successfully.")
    except Exception as e:
        print(f"The error '{e}' occurred")

def update_documents():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concertdata']
    collection = db['articles']

    # 讀取所有現有文檔
    documents = collection.find()

    for document in documents:
        # 對每個文檔進行二元分詞處理
        title = document.get('title', '')
        introduce = document.get('introduce', '')
        location = document.get('location', '')

        title_processed = preprocess_text(title)
        introduce_processed = preprocess_text(introduce)
        location_processed = preprocess_text(location)

        # 更新文檔中的分詞文本欄位
        collection.update_one(
            {'_id': document['_id']},
            {'$set': {
                'title_processed': title_processed,
                'introduce_processed': introduce_processed,
                'location_processed': location_processed
            }}
        )

    print("Documents updated successfully.")

def search_fulltext(query):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concertdata']
    collection = db['articles']

    # 對查詢文本進行二元分詞處理
    query_processed = preprocess_text(query)

    # 使用正則表達式查詢分詞文本欄位
    results = collection.find({
        "$or": [
            {"title_processed": {"$regex": query_processed, "$options": "i"}},
            {"introduce_processed": {"$regex": query_processed, "$options": "i"}},
            {"location_processed": {"$regex": query_processed, "$options": "i"}}
        ]
    })

    results_found = False
    response = []
    for result in results:
        results_found = True
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
            "date": date,
            "introduce": result['introduce'],
            "location": result['location']
        })
        #response.append(f"Title: {result.get('title', 'N/A')}\nIntroduce: {result.get('introduce', 'N/A')}\nLocation: {result.get('location', 'N/A')}\n")
        #print('-' * 50)

    if not results_found:
        return None
        
    return response


def fulltextsearch(search_query):
    # 添加 FULLTEXT 索引
    # add_fulltext_index()
    # 插入測試文檔
    update_documents()
    # 輸入要搜尋的關鍵字
    #search_query = input("Enter search query: ")

    # 執行全文檢索
    results = search_fulltext(search_query)
    return results

if __name__ == "__main__":
    fulltextsearch("火球")
