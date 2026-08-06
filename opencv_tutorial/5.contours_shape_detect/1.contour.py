import cv2

img = cv2.imread("5.contours_shape_detect/test.jpg")

cv2.imshow("Image" , img)
# img = cv2.GaussianBlur(img , (1,1) , 0)
canny = cv2.Canny(img , 20 , 60)



_ , binary = cv2.threshold(canny , 100 , 255 , cv2.THRESH_BINARY)


contours , hierarchy  = cv2.findContours(binary , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img , contours , -1 , (0,0,255), 1)
cv2.imshow("Contours" , img)
cv2.imwrite("images/contours.jpg" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()