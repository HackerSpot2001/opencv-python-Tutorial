#!/usr/bin/python3
import cv2
import numpy as np

img = cv2.imread("1.png")
cv2.imshow("Original",img)

kernal_3x3 = np.ones((3,3),np.float32)/9
blurred = cv2.filter2D(img,-1,kernal_3x3)
cv2.imshow("3x3 kernal Blurring",blurred)

kernal_7x7 = np.ones((7,7),np.float32)/49
blurred_7x7 = cv2.filter2D(img,-1,kernal_7x7)
cv2.imshow("7x7 kernal Blurring",blurred_7x7)


cv2.waitKey(0)
cv2.destroyAllWindows()