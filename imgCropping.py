#!/usr/bin/python3
import cv2

img = cv2.imread("1.png")
cv2.imshow("Original Image",img)

h,w = img.shape[:2]
start_row, start_col = int(h*.25), int(w*.25)
end_row, end_col = int(h*.75), int(w*.75)

cropped_img = img[start_row:end_row,start_col:end_col]
cv2.imshow("Cropped Image",cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()