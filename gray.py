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