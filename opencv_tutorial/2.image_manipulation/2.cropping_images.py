import cv2


img = cv2.imread("0.reading/test.jpeg")

if img is None:

    print("Could Not found the image")

else:
    # Let us crop the image now

    cropped = img[:1000 , :1200] # (startY:endY , startX:endX)

    cv2.imshow("Cropped_Image" , cropped)
    cv2.imwrite("iamges/cropped_image.png" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    


