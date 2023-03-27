#!/usr/bin/python3
import cv2

img = cv2.imread("1.jpg")
cv2.imshow("Original Image",img)

resizedImage = cv2.resize(img,(900,500),interpolation=cv2.INTER_AREA)
cv2.imshow("Scale- Skewed Image",img)

# resizedImage = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# cv2.imshow("Scale- Cubic Image",img)

# resizedImage = cv2.resize(img,None,fx=0.75,fy=0.75)
# cv2.imshow("Scale- Linear Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()