#!/usr/bin/python3
import cv2
import numpy as np

img = cv2.imread("1.png")
cv2.imshow("Orinal",img)

blurr = cv2.blur(img,(3,3))
cv2.imshow("Blurred Image",blurr)

gaussion_blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussion Blur Image",gaussion_blur)

median_blur = cv2.medianBlur(img,5)
cv2.imshow("median Blur Image",median_blur)


biletral  = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bilateral Blur Image",median_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()