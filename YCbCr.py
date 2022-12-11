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