import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.set(3,320)
cap.set(4,320)

while True:
    ret, frame = cap.read()

    # BGR -> YCrCb 변환
    YCrCb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    # 피부 검출
    mask_hand = cv2.inRange(YCrCb,np.array([0,133,77]),np.array([255,173,127]))
    # 피부 색 나오도록 연산
    mask_color = cv2.bitwise_and(frame,frame,mask=mask_hand)

    cv2.imshow('Original', frame)
    cv2.imshow('Hand', mask_hand)
    cv2.imshow('Skin', mask_color)

    if cv2.waitKey(1) &0xFF == 27:
        break

cv2.destroyAllWindows()