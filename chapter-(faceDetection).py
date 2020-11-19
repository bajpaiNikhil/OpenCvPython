import cv2

faceCascade=cv2.CascadeClassifier("resources/haarcascade_frontalface_alt.xml")
cap=cv2.VideoCapture(0)

while True:
    sus,img=cap.read()
    imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(imgG , 1.1,4)
  
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),2)


    cv2.imshow("VIDEO",img)
    cv2.waitKey(1)