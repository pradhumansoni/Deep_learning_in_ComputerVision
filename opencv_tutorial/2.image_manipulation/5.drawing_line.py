import cv2


img = cv2.imread("0.reading/test.jpeg")

if img is None:

    print("Could Not found the image")

else:
    pt1 = (36,100)
    pt2 = (36,700)
    color = (0 , 0 , 255)
    cv2.line(img , pt1 , pt2 , color=color , thickness=4) #(widthX , heightY)

    cv2.imshow("LineImage" , img)
    cv2.imwrite("images/Line_on_Image.png" , img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
