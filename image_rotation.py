#!/bin/python3
import cv2

img = cv2.imread("1.jpg")
# h,w,l = img.shape
# rotation_matrix = cv2.getRotationMatrix2D((w/2,h/2),70,.5)
# rotation_img = cv2.warpAffine(img,rotation_matrix,(w,h))
cv2.imshow("Original Image",img)
# cv2.imshow("Rotated Image",rotation_img)
cv2.waitKey(0)
cv2.destroyAllWindows()