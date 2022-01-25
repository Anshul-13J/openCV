import cv2 as cv
import numpy as np

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")
cv.imshow("Image",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#LAPLACIAN 
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

#SOBEL METHOD
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combine_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("SobelX",sobelx)
cv.imshow("SobelY",sobely)
cv.imshow("Combined Sobel", combine_sobel)



#CANNY METHOD
canny = cv.Canny(gray, 100,200)
cv.imshow("Canny",canny)

cv.waitKey(0)