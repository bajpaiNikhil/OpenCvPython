import cv2
import numpy as np


widthImg,heightimg=640,480

cap=cv2.VideoCapture(0)

def preProcessing(img):
    imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imgGrey,(5,5),1)
    imgCanny=cv2.Canny(imgblur,200,200)
    kernel=np.ones((5,5),np.uint8)
    imgDialation=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThreshold=cv2.erode(imgDialation,kernel,iterations=1)

    return imgThreshold

while True:
    src,img=cap.read()
    img=cv2.resize(img,(widthImg,heightimg))
    imgThreshold=preProcessing(img)
    cv2.imshow("result",imgThreshold)

    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
