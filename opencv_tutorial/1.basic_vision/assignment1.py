import cv2
IMG_DIR = input("Enter the image directory")
img = cv2.imread(IMG_DIR)

if img is not None:
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    if gray is not None:
        ask = int(input("Press 0 to Show the File\nPress 1 To Save the File"))
        if ask==0:

            cv2.imshow("GrayWindow" , gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif ask==1:
            cv2.imwrite("images/grayedImage.jpeg" , gray)
        else:
            print("Enter Either 0 or 1")
    else:
        print("Could Not Convert to GrayScale")

else:
    print("Could Not Load the Image")