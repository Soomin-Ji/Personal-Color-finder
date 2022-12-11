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