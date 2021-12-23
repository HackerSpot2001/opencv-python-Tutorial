import cv2
import numpy as np

img = cv2.imread("1.jpg")
h,w = img.shape[:2]

qh = h/4
qw = w/4

T = np.float32([[1,0,qw],[0,1,qh]])
img_translation = cv2.warpAffine(img,T,(w,h))
# img_translation = cv2.warpAffine(img,T,(w,h))
cv2.imshow("Original", img)
cv2.imshow("Translation", img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()