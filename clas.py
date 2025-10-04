from db_controll import db_cont
import cv2
from pyzbar.pyzbar import decode
# ファイルの先頭に追加

class category:
    detected_barcode = None
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
    def logcamera(cls):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cap.isOpened():
            raise RuntimeError("カメラが起動できません")

        def generate():
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                barcodes = decode(frame)
                for barcode in barcodes:
                    barcode_data = barcode.data.decode('utf-8')
                    cls.detected_barcode = barcode_data  # ← クラス変数に保存
                    print(f"検出: {barcode_data}")
                    break

                _, jpeg = cv2.imencode('.jpg', frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

        return generate()
    @classmethod
    def user(cls,barcode):
        barcode = int(barcode)
        print(barcode)
        sql = "SELECT unv_mail FROM login WHERE barcode = %s"
        params = (barcode,)
        result = db_cont.select(sql, params)
        print("params:", params)
        print("result:", result[0]["unv_mail"])
        if result:
            return result[0]["unv_mail"]
        else:
            return None
    
    @classmethod
    def plan(cls,user):
        sql = "SELECT * FROM plan_user WHERE user_id = %s LIMIT 3"
        params = (user,)
        result = db_cont.select(sql, params)
        print(result)
        return result
    @classmethod
    def user_id(cls, adress):
        sql = "SELECT user_id FROM login WHERE unv_mail = %s"
        params = (adress,)
        result = db_cont.select(sql, params)
        if result:
            return result[0]["user_id"]
        else:
            return None




