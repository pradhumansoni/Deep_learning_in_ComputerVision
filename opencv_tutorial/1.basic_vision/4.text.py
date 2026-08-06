import cv2

img = cv2.imread("reading/test.jpeg")

cv2.putText(
    img,
    text="Hello Kapill Sir",
    org=(500, 700), # (x,y)
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(0, 0, 200),   # BGR
    thickness=2
)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()