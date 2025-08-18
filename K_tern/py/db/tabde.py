import psycopg2
conn = psycopg2.connect(
    dbname="unvsv",  # 管理用DBに接続
    user="postgres",
    password="2431",
    host="127.0.0.1",
    port="5432"
)
conn.autocommit = True
# テーブル作成
cur = conn.cursor()
cur.execute("DROP TABLE Employee")

cur.close()

#接続を閉じる
conn.close()