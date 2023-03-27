#!/usr/bin/python3
import cv2

img = cv2.imread("1.jpg")
cv2.imshow("Original Image",img)
cv2.imshow("Original Image",img)

smaller = cv2.pyrDown(img)
big = cv2.pyrUp(img)
cv2.imshow("Smaller Image",smaller)
cv2.imshow("larger Image",big)
cv2.imwrite("1.png",big)

cv2.waitKey(0)
cv2.destroyAllWindows()