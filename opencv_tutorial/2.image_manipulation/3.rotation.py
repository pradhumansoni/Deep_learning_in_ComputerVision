import cv2


img = cv2.imread("0.reading/test.jpeg")

if img is None:

    print("Could Not found the image")

else:
    (h , w) = img.shape[:2] # This gives us the height and width of the image
    center = (w//2 , h//2) # This gives us the center of the original image
    M = cv2.getRotationMatrix2D(center , angle = 45 , scale = 1.0) #this creates the new matrix
    rotated = cv2.warpAffine(img , M , (w,h)) # this is used to rotate

    cv2.imshow("Rotated_Image" , rotated)
    cv2.imwrite("images/rotated_image.png", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

