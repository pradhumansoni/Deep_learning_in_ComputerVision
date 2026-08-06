import cv2

img = cv2.imread("reading/test.jpeg")
imgBlur = cv2.GaussianBlur(img , ksize=(15,15) , sigmaX=5)
cv2.imshow("ImageOrg" , img)
cv2.imshow("ImageBlur" , imgBlur)
cv2.waitKey(0)