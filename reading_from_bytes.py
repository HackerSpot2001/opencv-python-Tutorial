import cv2
import numpy as np



im_path = 'data.jpg'
with open(im_path, 'rb') as fp:
    im_b = fp.read()

image_np = np.frombuffer(im_b, np.uint8)
img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)  
im_cv = cv2.imread(im_path)

cv2.imshow("Data",im_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()