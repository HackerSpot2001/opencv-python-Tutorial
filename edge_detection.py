import cv2
import numpy as np

img = cv2.imread("1.png",0)
cv2.imshow("Original Image",img)
h,w = img.shape[:2]

sobal_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.imshow("Sobal_X Image",sobal_x)

sobal_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow("Sobal_Y Image",sobal_y)

sobal_or = cv2.bitwise_or(sobal_x,sobal_y)
cv2.imshow("Sobal OR image",sobal_or)

laplacain = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Laplacian Image",laplacain)

canny = cv2.Canny(img,20,170)
cv2.imshow("Canny Image",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()