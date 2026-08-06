import cv2
import numpy as np

img1 = np.zeros((300,300) , dtype=np.uint8)
img2 = np.zeros((300,300) , dtype=np.uint8)

cv2.circle(img1 , (100,100) , 70 , 255 , -1)
cv2.rectangle(img2 , (100,100) , (200,200), 255 , -1)

bit_and = cv2.bitwise_and(img1 , img2)
bit_or = cv2.bitwise_or(img1 , img2)
bit_xor = cv2.bitwise_xor(img1 , img2)
bit_not = cv2.bitwise_not(img2)

cv2.imshow('circle',img1)
cv2.imshow('rectangle',img2)
cv2.imshow('bitwise_and',bit_and)
cv2.imshow('bitwise_or',bit_or)
cv2.imshow('bitwise_xor',bit_xor)
cv2.imshow('bitwise_not',bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()