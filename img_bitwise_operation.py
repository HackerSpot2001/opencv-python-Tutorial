#!/usr/bin/python3
import cv2
import numpy as np

square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow("square",square)

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)

And = cv2.bitwise_and(square,ellipse)
cv2.imshow("And Operator",And)

Xor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor Operator",Xor)

Or = cv2.bitwise_or(square,ellipse)
cv2.imshow("Or Operator",Or)

Not = cv2.bitwise_not(square,ellipse)
cv2.imshow("Not Operator",Not)


cv2.waitKey(0)
cv2.destroyAllWindows()