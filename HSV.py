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