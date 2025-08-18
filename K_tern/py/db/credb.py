import psycopg2

#PostgreSQLに接続
conn = psycopg2.connect(
    dbname="postgres",  # 管理用DBに接続
    user="postgres",
    password="2431",
    host="127.0.0.1",
    port="5432"
)
conn.autocommit = True
#DB作成
cur = conn.cursor()
cur.execute("CREATE DATABASE unvsv")
cur.close()

#接続を閉じる
conn.close()