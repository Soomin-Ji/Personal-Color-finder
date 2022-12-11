import cv2
import numpy as np

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(False):
    print("Webcam is not running")
    exit()

time_num = 0
image_num = 0

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cat_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
    status, frame = cap.read()
    time_num = time_num + 1

    cv2.imshow('webcam', img)

    if time_num == 30:
        image_num = image_num + 1

    cv2.imwrite('img'+str(image_num)+'.png', frame) #-- 본인 편의에 맞게 경로 설정 및 이미지 이름 변경
    time_num = 0
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.distroyAllWindows()
