import cv2

camera = cv2.VideoCapture(0)

# these lines give the current width and height of our camera capture frame as numbers
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) 
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID') # create codec

# this records every frame in some fps and save it as a video format

out = cv2.VideoWriter("images/my_video.avi" , codec , 24 , (frame_width,frame_height) , isColor=False)

if not out.isOpened():
    print("VideoWriter failed to open")
while True:

    ret , frame = camera.read() # start reading each frame

    if not ret:
        break
    else:
        frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #this changes the frame to grayscale
        
        out.write(frame) #this saves the each frame
        cv2.imshow("Live Video Feed" , frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

camera.release()
out.release()
cv2.destroyAllWindows()

