import cv2
import numpy as np

cat_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#img = cv2.imread("./photo.jpg")

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
    #cv2.imwrite("capture.jpg", img)
    #break

    #break

src = cv2.imread("./capture.jpg", cv2.IMREAD_COLOR)
dst = src[x:x+w, y:y+h].copy() #얼굴만 잘라낸 사진
resized = cv2.resize(dst, dsize=(300,300), interpolation = cv2.INTER_AREA)


#배경 이미지의 위치, 로고 크기만큼 컷팅
sw = spring_warm[400:700, 400:700]
sc = summer_cool[400:700, 400:700]
aw = autumn_warm[400:700, 400:700]
wc = winter_cool[400:700, 400:700]

print("어떤 색깔과 비교해보시겠습니까?")
num = int(input("1. 봄웜, 2. 여름쿨, 3. 가을웜, 4.겨울쿨 / 숫자를 입력해주세요"))

if num == 1:
    add = cv2.add(sw,resized)
    spring_warm[400:700, 400:700] = add
    cv2.imshow("1", spring_warm)

if num == 2:
    add = cv2.add(sc,resized)
    summer_cool[400:700, 400:700] = add
    cv2.imshow("1", summer_cool)

if num == 3:
    add = cv2.add(aw,resized)
    autumn_warm[400:700, 400:700] = add
    cv2.imshow("1", autumn_warm)

if num == 4:
    add = cv2.add(wc,resized)
    winter_cool[400:700, 400:700] = add
    cv2.imshow("1", winter_cool)


#cap.release()
#cv2.distroyAllWindows()
