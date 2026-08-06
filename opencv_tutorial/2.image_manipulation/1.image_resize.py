import cv2

img = cv2.imread("0.reading/test.jpeg")
if img is not None:

    img_resized = cv2.resize(img , (300 , 300))  # (width , height)
    # This compresses the whole image into 300x300 matrix

    cv2.imshow("Original Image" , img)
    cv2.imshow("resized Image" , img_resized)
    # saving the resized image
    cv2.imwrite("images/resized_image.png" , img_resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Could Not load the image")

# Let us check the dimensions of the resized image we saved (should be 300x300x3)
new_img = cv2.imread("images/resized_image.png")

print(new_img.shape)