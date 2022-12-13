import cv2
import numpy as np

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

spring_warm = cv2.imread('./spring_warm.jpg')
summer_cool = cv2.imread('./summer_cool.jpg')
autumn_warm = cv2.imread('./autumn_warm.jpg')
winter_cool = cv2.imread('./winter_cool.jpg')

x=y=w=h=0

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cat_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
       
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    key = cv2.waitKey(30)
    if key == 26 : #ctrl + z
        print("captured")
        cv2.imwrite("capture.jpg", img)
        break

src = cv2.imread("capture.jpg", cv2.IMREAD_COLOR)
dst = src[x:x+w, y:y+h].copy() #얼굴만 잘라낸 사진 

cv2.imshow("dst", dst)
cap.release()
cv2.distroyAllWindows()
