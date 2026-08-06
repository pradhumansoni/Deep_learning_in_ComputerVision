import cv2
import numpy as np
img = cv2.imread("images/median_blurred_img.jpg")

sample_kernel = np.array([
    [0 , -1 , 0],
    [-1 , 5 , -1],
    [0 , -1 , 0]

])

sharpened = cv2.filter2D(img , ddepth=-1 , kernel = sample_kernel)

cv2.imshow("Original" , img)
cv2.imshow("Sharpened",sharpened)
cv2.imwrite("images/sharpened_img.jpg" , sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()