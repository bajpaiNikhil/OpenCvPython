import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):

    contour,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area=cv2.contourArea(cnt)
        #print("area",area)
        if area>500:
            print(area)
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),1)
            perimeter=cv2.arcLength(cnt,True)
            print("perimeter",perimeter)
            approx=cv2.approxPolyDP(cnt,0.03*perimeter,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objCor=="3": objectType="tri"

            elif objCor=="4":
                ratio=w/float(h)
                if ratio>.95 and ratio<1.05:
                    objectType="square"
                else:objectType="rectangle"
            if objCor>4:
                objectType="circle"
            else: objectType=None

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_ITALIC,0.9,(0,0,0),2)



img=cv2.imread("resources/shapesss.png")

imgR=cv2.resize(img,(500,500))
imgContour=imgR.copy()
imgGrey=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGrey,(7,7),1)
imgBlack=np.zeros_like(imgR)
imgCanny=cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

# cv2.imshow("imgageR",imgR)
# cv2.imshow("imgGrey",imgGrey)
# cv2.imshow("imgBlur",imgBlur)

imgStack=stackImages(0.6,([imgR,imgGrey,imgBlur]
                          ,[imgCanny,imgContour,imgBlack]))

cv2.imshow("stackImg",imgStack)

cv2.waitKey(0)