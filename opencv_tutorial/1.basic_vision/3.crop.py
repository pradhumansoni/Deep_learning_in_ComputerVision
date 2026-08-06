import cv2

img = cv2.imread("reading/test.jpeg")
imgCrop = img[200:800, 600:1200] #this is height 200 to 800 and width 600 to 1200
cv2.imshow("ImageOrg" , img)
cv2.imshow("ImageCrop" , imgCrop)
cv2.waitKey(0)