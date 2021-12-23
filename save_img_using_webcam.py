#!/usr/bin/python3
import cv2
from matplotlib import pyplot as plt

device = cv2.VideoCapture(0)
if device.isOpened():
    ret,frame = device.read()
    print(ret)
    print(frame)

else:
    ret = False

img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("Camera Image 1")
plt.xticks([])
plt.yticks([])
plt.imshow()
device.release()