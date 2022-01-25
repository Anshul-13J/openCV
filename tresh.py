import cv2 as cv
import numpy as np

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#SIMPLE THRESHOLD
threshold, thresh = cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow("Simple Threshold",thresh)


#ADAPTIVE THRESHOLDING
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11,7)
cv.imshow("Adaptive Thresholding", adaptive_thresh)


cv.waitKey(0)
