import mysql.connector
import psycopg2
# MySQLに接続
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
#従業員テーブル作成
cur.execute("CREATE TABLE Employee(ID INT PRIMARY KEY, Name VARCHAR(50), adress VARCHAR(200) , Pass VARCHAR(100))")
cur.execute("ALTER TABLE Employee ALTER COLUMN name SET NOT NULL")
cur.execute("ALTER TABLE Employee ALTER COLUMN adress SET NOT NULL")
cur.execute("ALTER TABLE Employee ALTER COLUMN Pass SET NOT NULL")


cur.close()

#接続を閉じる
conn.close()
