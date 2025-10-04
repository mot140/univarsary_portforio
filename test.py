import mysql.connector
from datetime import datetime, date, time
from secret.db_acces import connection
# DB接続
conn=connection()
cursor = conn.cursor()

# 1. user（親テーブル）
users = [
    ("山田太郎", "09011112222", "東京都町田市", date(2000, 1, 1), "student"),
    ("佐藤花子", "08033334444", "神奈川県横浜市", date(1999, 5, 15), "student"),
    ("高橋健", "07055556666", "埼玉県さいたま市", date(2001, 12, 30), "teacher")
]

# user挿入とID取得
user_ids = []
for user in users:
    cursor.execute("""
        INSERT INTO user (user_name, tell_number, address, birth_date, position)
        VALUES (%s, %s, %s, %s, %s)
    """, user)
    user_ids.append(cursor.lastrowid)
logids=[]
# login挿入（取得したIDを使う）
logins = [
    ("yamada@univ.jp", "pass123", user_ids[0],4901777410121),
    ("sato@univ.jp", "pass456", user_ids[1],111111111111),
    ("takahashi@univ.jp", "pass789", user_ids[2],222222222)
]
cursor.executemany("""
    INSERT IGNORE INTO login (unv_mail, password, user_id,barcode)
    VALUES (%s, %s, %s,%s)
""", logins)
logids = [cursor.lastrowid] * len(logins)  # ただし、executemanyではlastrowidは正確に取れない

# 3. sylbas
sylbas = [
    (user_ids[0], "数学基礎", 2, "月", "導入", "計算", "応用", "演習", "確認", "復習", "まとめ", "発展",
     "補足", "資料", "課題", "評価", "コメント", "内容", "補足3", "補足4", "補足5","b"),
    (user_ids[1], "英語表現", 3, "火", "発音", "文法", "会話", "読解", "作文", "演習", "確認", "まとめ",
     "補足", "資料", "課題", "評価", "コメント", "内容", "補足3", "補足4", "補足5","a"),
    (user_ids[2], "情報処理", 2, "水", "PC操作", "Excel", "Word", "PowerPoint", "演習", "確認", "まとめ",
     "補足", "資料", "課題", "評価", "コメント", "内容", "補足3", "補足4", "補足5", "aaa","aa")
]
sylid=[]
for i, row in enumerate(sylbas):
    if len(row) != 21:
        print(f"Row {i+1} has {len(row)} values instead of 22")
    cursor.executemany("""
        INSERT IGNORE INTO sylbas (
            user_id, class_name, point, weekday,
            first_class, second_class, third_class, four_class,
            five_class, six_class, seven_class, eight_class,
            nine_class, ten_class, eleven_class, twelve_class,
            ttird_class, tfour_class, tfive_class,
            evalution_way, coment, naiy
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """, sylbas)
    sylid.append(cursor.lastrowid)

# 4. es
es_data = [
    (user_ids[0], "履歴書1", "ファイル内容1", True, "コメント1", False),
    (user_ids[1], "履歴書2", "ファイル内容2", False, "コメント2", True),
    (user_ids[2], "履歴書3", "ファイル内容3", True, "コメント3", True)
]
cursor.executemany("""
    INSERT INTO es (user_id, rirek_name, es_file, quest, kome, quest_user)
    VALUES (%s, %s, %s, %s, %s, %s)
""", es_data)

# 5. login_his
login_his = [
    (logids[0], datetime(2025, 10, 1, 9, 0)),
    (logids[1], datetime(2025, 10, 1, 10, 30)),
    (logids[2], datetime(2025, 10, 1, 11, 45))
]
cursor.executemany("""
    INSERT INTO login_his (login_id, login_time)
    VALUES (%s, %s)
""", login_his)

# 6. rirek
rirek_data = [
    (user_ids[0], "履歴書A", "fileA.pdf", True, "良いです", False),
    (user_ids[1], "履歴書B", "fileB.pdf", False, "改善点あり", True),
    (user_ids[2], "履歴書C", "fileC.pdf", True, "完璧", True)
]
cursor.executemany("""
    INSERT INTO rirek (user_id, rirek_name, rirek_file, quest, kome, quest_user)
    VALUES (%s, %s, %s, %s, %s, %s)
""", rirek_data)

# 7. class_user
class_user_data = [
    (user_ids[0], sylid[0], "数学基礎"),
    (user_ids[1], sylid[1], "英語表現"),
    (user_ids[2], sylid[2], "情報処理")
]
cursor.executemany("""
    INSERT INTO class_user (user_id, sylbas_id, class_name)
    VALUES (%s, %s, %s)
""", class_user_data)

# 8. plan_user
plan_user_data = [
    (user_ids[0], date(2025, 10, 3), time(9, 0), "ゼミ準備"),
    (user_ids[0], date(2025, 10, 4), time(10, 30), "面接対策"),
    (user_ids[0], date(2025, 10, 5), time(13, 0), "履歴書添削")
]
cursor.executemany("""
    INSERT INTO plan_user (user_id, date_plan, time_plan, plan_txt)
    VALUES (%s, %s, %s, %s)
""", plan_user_data)

# コミットして終了
conn.commit()
cursor.close()
conn.close()