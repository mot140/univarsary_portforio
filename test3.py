import cv2
from pyzbar.pyzbar import decode

# カメラを起動
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが起動できません")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームの取得に失敗しました")
        break

    # pyzbarでバーコードを検出
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        text = f'{barcode_type}: {barcode_data}'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        print(f'検出: {text}')

    cv2.imshow('Barcode Scanner', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()