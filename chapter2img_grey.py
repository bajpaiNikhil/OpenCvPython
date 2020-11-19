import cv2
import numpy as np

img=cv2.imread("resources/chotiii.png")
kernel=np.ones((5,5),np.uint8)


imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(imgGrey.shape)
# imgBlur=cv2.GaussianBlur(imgGrey,(7,7),0)
# imgCanny=cv2.Canny(img,150,200)
# imgDialation=cv2.dilate(imgCanny,kernel,iterations=5)
# imgErode=cv2.erode(imgDialation,kernel,iterations=1)

#cv2.imshow("Blur",imgBlur)
#
cv2.putText(imgGrey," I am Stupid",(100,150),cv2.FONT_ITALIC,1,(0,0,150),5)
cv2.imshow("Grey",imgGrey)
# cv2.imshow("Canny",imgCanny)
# cv2.imshow("dialation",imgDialation)
# cv2.imshow("Erode",imgErode)
cv2.waitKey(0)