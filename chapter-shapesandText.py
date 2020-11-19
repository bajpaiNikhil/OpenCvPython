import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img.shape)
#
# img[:]=255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),3)
cv2.line(img,(512,0),(0,512),(0,255,0),2)
cv2.rectangle(img,(0,0),(255,255),(0,0,255),cv2.FILLED)
cv2.rectangle(img,(50,60),(300,200),(0,1,123),3)
cv2.circle(img,(400,400),100,(255,255),5)

cv2.putText(img,"  I am Stupid",(100,300),cv2.FONT_ITALIC,1,(0,190,200),5)

cv2.imshow("img",img)



cv2.waitKey(0)