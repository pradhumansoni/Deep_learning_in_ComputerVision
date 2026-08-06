import cv2

img = cv2.imread("reading/test.jpeg")

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("ImageColour",img)
cv2.imshow("ImageGray",imgGray)
cv2.waitKey(0)
