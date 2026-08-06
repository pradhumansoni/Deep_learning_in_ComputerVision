import cv2

img = cv2.imread("4.image_filter/test_img.jpg" , cv2.IMREAD_GRAYSCALE)
img = img[:800 , 100:1100]

ret , threshold_img = cv2.threshold(img ,125, 255 , cv2.THRESH_BINARY)

cv2.imshow("original",img) 
cv2.imshow("Threshold",threshold_img)
cv2.imwrite("images/threshold_img.jpg" , threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
