import cv2


img = cv2.imread("0.reading/test.jpeg")

if img is None:

    print("Could Not found the image")

else:
    flipped_horizontal = cv2.flip(img , 1) #flips horizontally left to right
    flipped_vertical = cv2.flip(img , 0) #flips vertically top to bottom
    flipped_both = cv2.flip(img , -1) #flips both ways

    cv2.imshow("Original" , img)
    cv2.imshow("Horizontally" , flipped_horizontal)
    cv2.imshow("Vertically" , flipped_vertical)
    cv2.imshow("Flipped Both" , flipped_both)

    cv2.imwrite("images/flipped_horizontal.png" , flipped_horizontal)
    cv2.imwrite("images/flipped_vertical.png" , flipped_vertical)
    cv2.imwrite("images/flipped_horizontal.png" , flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

