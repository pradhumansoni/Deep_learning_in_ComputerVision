import cv2


img = cv2.imread("0.reading/test.jpeg")

if img is None:

    print("Could Not found the image")

else:

    cv2.putText(img ,"Hello Kapillll Sir!!" , (700,300),cv2.FONT_HERSHEY_SIMPLEX,2.0 ,(0 ,0,255) ,3) #(widthX , heightY)

    cv2.imshow("LineImage" , img)
    cv2.imwrite("images/Text_on_Image.png" , img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
