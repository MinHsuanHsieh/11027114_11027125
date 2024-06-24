import mysql.connector
import configparser

# 讀取配置檔案
config = configparser.ConfigParser()
config.read('config.ini')

# 設定資料庫連接配置
db_config = {
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'host': config.get('mysql', 'host'),
    'database': config.get('mysql', 'database'),
    'raise_on_warnings': True
}

# 查詢音樂會資訊
def query_concerts(concert_date):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    query = ("SELECT title, link FROM articles WHERE start_date = %s")
    cursor.execute(query, (concert_date,))

    response_message = ''
    for (title, link) in cursor:
        response_message += "{}: {}\n".format(title, link)

    cursor.close()
    cnx.close()

    return response_message if response_message else "No concerts found for this date."