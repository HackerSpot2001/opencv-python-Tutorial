#!/usr/bin/python3
import cv2
import numpy as np

img = cv2.imread("1.png")
cv2.imshow("Original Image", img)
# M = np.ones(img.shape,dtype="uint8") *150
M = np.zeros(img.shape,dtype="uint8") + 150

add = cv2.add(img,M)
cv2.imshow("Added",add)

sub = cv2.subtract(img,M)
cv2.imshow("Subtract",sub)

mul = cv2.multiply(img,M)
cv2.imshow("Multiply",mul)

devide = cv2.divide(img,M)
cv2.imshow("devide",devide)

cv2.waitKey(0)
cv2.destroyAllWindows()
