import cv2

img = cv2.imread("1.jpg",0)
cv2.imshow("Gray Scale Image",img)
ret,black_white = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",black_white)
cv2.waitKey(0)
cv2.destroyAllWindows()