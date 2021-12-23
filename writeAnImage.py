import cv2

img = cv2.imread("download.jpg")
cv2.imshow("Write Image",img)
cv2.imwrite("New.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()