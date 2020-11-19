import cv2

cap=cv2.VideoCapture("resources/testVideo.mp4")

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(20)& 0xFF == ord("q"):
        break
