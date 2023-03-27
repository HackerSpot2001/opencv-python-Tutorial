import cv2

img = cv2.imread("sample.jpg")
cv2.imshow("get Info",img)
h,w,l = img.shape
print("Image Width (in pixels): ",w)
print("Image Height (in pixels): ",h)
print("Image Layers(R,G,B): ",l)

cv2.waitKey(0)
cv2.destroyAllWindows() 