import cv2

cap = cv2.VideoCapture("test.mp4")

while True:

    success,img = cap.read()

    if not success:
        break
    cv2.imshow("Video Title", img)
    cv2.waitKey(1) # 1 means each frame is for 1 millisecond