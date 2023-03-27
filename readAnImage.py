import cv2
import numpy as np

img = "sample.jpg"
data = cv2.imread(img)
cv2.imshow("Sample Image",data)
cv2.waitKey(0)
cv2.destroyAllWindows()