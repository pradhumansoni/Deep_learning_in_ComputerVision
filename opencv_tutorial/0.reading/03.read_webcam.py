import cv2

cap = cv2.VideoCapture(0) # 0 means main camera

while True:

    success,img = cap.read()

    if not success:
        break
    cv2.imshow("Video Title", img)
    if cv2.waitKey(1) & 0xFF == ord('q') : #this 0xFF == ord('q') tells to close when q is pressed
        break