import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="wk",
    password="wkma",
    host="127.0.0.1",
    port="5432"
      )
conn.autocommit = True
#DB作成
cur = conn.cursor()
cur.execute("DROP DATABASE unvsv")
cur.close()

#接続を閉じる
conn.close()      