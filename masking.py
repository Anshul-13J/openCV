import cv2 as cv
import numpy as np

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")
cv.imshow("Image",img)
blank = np.zeros(img.shape[:2],dtype = 'uint8')
mask = cv.circle(blank, (img.shape[1]//2-170, img.shape[0]//2- 145), 130, 255, -1)

masked = cv.bitwise_and(img, img, mask= mask)

cv.imshow("Masked", masked)



cv.waitKey(0)