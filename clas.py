from db_controll import db_cont

class category:
    @classmethod
    def log(cls, user, password):
        sql = "SELECT password FROM login WHERE unv_mail = %s"
        params = (user,)
        result = db_cont.select(sql, params)
        print("params:", params)
        print("result:", result)
        if result:
            db_password = result[0]["password"]
            if db_password == password:
                print("✅ ログイン成功")
                return 0
            else:
                print("❌ パスワードが一致しません")
                return 1
        else:
            print("❌ ユーザーが存在しません")
            return 1
    @classmethod
    def user(cls,adress):
        


