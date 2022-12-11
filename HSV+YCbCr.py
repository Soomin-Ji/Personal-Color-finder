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