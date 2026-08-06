import cv2

img = cv2.imread("images/mumma.png" , cv2.IMREAD_GRAYSCALE)
img = img[:800 , 100:1100]

edges = cv2.Canny(img , 20 , 60)
cv2.imshow("Image",img)
cv2.imshow("Canny",edges)

cv2.imwrite("images/canny_edge.jpeg",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()