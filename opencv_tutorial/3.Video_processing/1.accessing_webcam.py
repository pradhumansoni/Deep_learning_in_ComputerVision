import cv2
def gray_flip(frame):
    flip = cv2.flip(frame , 1) # flips horizontally
    return cv2.cvtColor(flip , cv2.COLOR_BGR2GRAY) # this returns flipped + grayscale frame
cap = cv2.VideoCapture(0) # 0 means main camera source

while True:

    ret , frame = cap.read() # ret = True until last frame 

    if not ret:

        print("Could Not Capture the frame Quitting...")
        break

    else:
        processed_frame = gray_flip(frame) #made function for processing each frame
        cv2.imshow("Live Video Feed" , processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            print("Quitting...")
            break

cap.release()
cv2.destroyAllWindows()



