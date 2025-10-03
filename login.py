from db_controll import db_cont
from secret.db_acces import connection
class login:
    @classmethod
    def log(cls, user, password):
        sql = "SELECT password FROM login WHERE unv_mail = %s"
        params = (user,)  # ← タプルで渡す
        a=password
        result = db_cont.select(sql, params)
        print(result)

login.log("yamada@univ.jp","aaa")