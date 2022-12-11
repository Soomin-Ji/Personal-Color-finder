#이미지 불러오기

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = cv2.imread('zd.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

#HSV
 #cv2.cvtColor : 불러온 이미지를 HSV로 변환한다.
 # cv2.inRange : 참고 git hub에서 사용한  HSV 값으로 Skin 영역을 추출할 mask를 생성한다.
 # cv2.morphologyEx : 마스크를 좀 더 부드럽게 해 줌
 # cv2.bitwise_and : 비트 and 연산으로 Skin 영역 추출 (mask와 원본 이미지 모두 1인 부분 추출)

img_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

HSV_mask = cv2.inRange(img_HSV, (7, 15, 0), (17,255,255))
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)) 

HSV_result = cv2.bitwise_and(img, img, mask=HSV_mask)

fig = plt.figure(figsize=(30,10))

ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.imshow(HSV_mask, cmap='gray')
ax2.imshow(HSV_result)
ax3.imshow(img)

#YCbCr
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

YCrCb_mask = cv2.inRange(img_YCrCb, (60, 135, 85), (255,180,135))
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

YCrCb_result = cv2.bitwise_and(img, img, mask=YCrCb_mask)

fig = plt.figure(figsize=(30,10))

ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.imshow(YCrCb_mask, cmap='gray')
ax2.imshow(YCrCb_result)
ax3.imshow(img)

#HSV+YCbCr
#cv2.bitwise_or: 위 두 마스크를 합친다. 

global_mask = cv2.bitwise_or(YCrCb_mask, HSV_mask)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

global_result=cv2.bitwise_and(img, img, mask=global_mask)

fig = plt.figure(figsize=(30,10))

ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.imshow(global_mask, cmap='gray')
ax2.imshow(global_result)
ax3.imshow(img)

#Gray
#gray scale은 이미지의 밝기만을 고려한다.
#조명으로 인해 밝은 부위만 추출한다.  (200, 255) 값을 줌

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

result = cv2.bitwise_and(img, img, mask=binary)

fig = plt.figure(figsize=(30,10))

ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.imshow(binary, cmap='gray')
ax2.imshow(result)
ax3.imshow(img)

#HSV+YCbCr+Gray
post_global_mask = cv2.bitwise_or(global_mask, binary)
post_global_mask = cv2.morphologyEx(post_global_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))

post_global_result=cv2.bitwise_and(img, img, mask=post_global_mask)

fig = plt.figure(figsize=(30,10))

ax = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax.imshow(post_global_mask, cmap='gray')
ax2.imshow(post_global_result)
ax3.imshow(img)

#Gray scale로 뽑아낸 빛나는 영역까지 합쳐 skin 영역만 잘 추출됨

# 출처 openCV - 색 기반 얼굴 피부 영역 추출 : python, HSV, YCbCr, Gray|작성자 yunnaa