import cv2
import numpy as np

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

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


cap.release()
cv2.distroyAllWindows()
