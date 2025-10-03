from secret.db_access import conne

class db_Set():
    cursor = conne.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS univarsary_portforio")
    cursor.close()
    conne.close()

class db_table:
    @classmethod
    def create_tables(cls):
        from secret.db_acces import connection
        conn = connection()  # ✅ 関数を呼び出して接続オブジェクトを取得
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user(user_id INT PRIMARY KEY AUTO_INCREMENT,user_name VARCHAR(100) NOT NULL,tell_number VARCHAR(20) NOT NULL,address VARCHAR(100) NOT NULL,birth_date DATE NOT NULL,position VARCHAR(20) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS login (login_id INT PRIMARY KEY AUTO_INCREMENT,unv_mail VARCHAR(50) NOT NULL UNIQUE,password VARCHAR(50) NOT NULL,user_id INT NOT NULL,FOREIGN KEY(user_id) REFERENCES user(user_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS sylbas(sylbas_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,class_name VARCHAR(100) NOT NULL,point INT NOT NULL,weekday VARCHAR(10) NOT NULL,first_class TEXT NOT NULL,second_class TEXT NOT NULL,third_class TEXT NOT NULL,four_class TEXT NOT NULL,five_class TEXT NOT NULL,six_class TEXT NOT NULL,seven_class TEXT NOT NULL,eight_class TEXT NOT NULL,nine_class TEXT,ten_class TEXT,eleven_class TEXT,twelve_class TEXT,ttird_class TEXT,tfour_class TEXT,tfive_class TEXT,evalution_way TEXT NOT NULL,coment TEXT NOT NULL,naiy TEXT NOT NULL ,FOREIGN KEY(user_id) REFERENCES user(user_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS es(es_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,rirek_name VARCHAR(1000) NOT NULL,es_file TEXT NOT NULL,quest BOOLEAN NOT NULL,kome TEXT,quest_user BOOLEAN NOT NULL,FOREIGN KEY(user_id) REFERENCES user(user_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS login_his(loghis_id INT PRIMARY KEY AUTO_INCREMENT,login_id INT NOT NULL,login_time DATETIME NOT NULL,FOREIGN KEY(login_id) REFERENCES login(login_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS rirek(rirek_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,rirek_name VARCHAR(1000) NOT NULL,rirek_file VARCHAR(1000) NOT NULL,quest BOOLEAN NOT NULL,kome TEXT,quest_user BOOLEAN NOT NULL,FOREIGN KEY(user_id) REFERENCES user(user_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS class_user(class_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,sylbas_id int NOT NULL,class_name VARCHAR(1000) NOT NULL,FOREIGN KEY(user_id) REFERENCES user(user_id),FOREIGN KEY(sylbas_id) REFERENCES sylbas(sylbas_id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS plan_user(plan_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT NOT NULL,date_plan DATE NOT NULL,time_plan TIME NOT NULL,plan_txt VARCHAR(1000) NOT NULL,FOREIGN KEY(user_id) REFERENCES user(user_id))")
        cursor.close()
        conn.close()
        print("complete!")

class db_cont:
    @classmethod
    def select(cls, query, params=None):
        from secret.db_acces import connection
        conn = connection()  # ✅ 接続オブジェクトを取得
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()  # ✅ 接続も忘れずに閉じる
        print(result)
query="SELECT * FROM login WHERE unv_mail=%s"
params=("yamada@univ.jp",)

db_cont.select(query,params)

db_table.create_tables()