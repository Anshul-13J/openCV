import cv2 as cv
from cv2 import COLOR_BGR2HSV

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow("Image",img)
cv.imshow("GRAY",gray)
cv.imshow("HSV",hsv)
cv.imshow("LAB",lab)

cv.waitKey(0)