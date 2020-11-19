import cv2
import numpy as np

img=cv2.imread("resources/card.png")
width,height=450,550

pts1=np.float32([[100,172],[215,176],[63,325],[250,330]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)

img_wrap=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("card",img)
cv2.imshow("cards2",img_wrap)
cv2.waitKey(0)