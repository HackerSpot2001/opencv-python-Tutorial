import cv2


cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)
# cap = cv2.VideoCapture("butterfly.mp4")

while (1):
    success,frame = cap.read()
    frame = cv2.resize(frame,(1080,1080))
    cv2.imshow("Video",frame)
    cv2.resizeWindow("Video",1080,1080)
    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break


cap.release()