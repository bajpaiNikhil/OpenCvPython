import cv2
import numpy as np

cap=cv2.VideoCapture(0)

myColors = [[102,81,0,154,255,255],
            [20,115,123,90,255,255]]

myColorValue=[[115,23,18],             ##BGR
               [29,245,148]]

myPoints=[]#x ,y , colorId
def findColor(img , myColors,myColorValue):

    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newPoints=[]
    for color in myColors:

        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv2.inRange(imgHsv,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValue[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):

    contour,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contour:
        area=cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),5)
            perimeter=cv2.arcLength(cnt,True)
            #print("perimeter",perimeter)
            approx=cv2.approxPolyDP(cnt,0.03*perimeter,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w //2,y


def drawOnCanvas(myPoints,myColorValues):

     for points in myPoints:
         cv2.circle(imgResult,(points[0],points[1]),10,myColorValue[points[2]],cv2.FILLED)




while True:
    success,img=cap.read()
    imgResult=img.copy()
    newPoints = findColor(img, myColors,myColorValue)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValue)

    cv2.imshow("result",imgResult)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break