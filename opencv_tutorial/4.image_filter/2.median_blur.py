import cv2

img = cv2.imread("4.image_filter/test_img.jpg")

if img is None:
    print("Could NOt open image")
else:
    img = img[300:800 , 100:900]
    cv2.imshow('Original',img)
    blurred = cv2.medianBlur(img , 3)
    cv2.imshow("New Image" , blurred)
    cv2.imwrite("images/median_blurred_img.jpg", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()