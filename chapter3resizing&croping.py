import cv2

img=cv2.imread("resources/chotiii.png")
print(img.shape)
imgResize=cv2.resize(img,(500,300))
print(imgResize.shape)
cv2.imshow("imgresize",imgResize)

imgCropped=imgResize[0:200,200:500]
cv2.imshow("imgCropped",imgCropped)
cv2.waitKey(0)