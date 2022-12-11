import cv2

cap = cv2.VideoCpature(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = 1-frame

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
