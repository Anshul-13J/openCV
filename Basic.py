from calendar import c
import cv2 as cv
from cv2 import dilate

# img = cv.imread("D:\\College\\innogeeks\\Ec53xzgUMAEz-ME.jpg")
img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
# canny = cv.Canny(img,10,180)
# dilated = cv.dilate(canny, (3,3), iterations=1)
# eroded = cv.erode(dilated, (3,3) , iterations = 1)
# resized = cv.resize(img, (1920,1080), interpolation= cv.INTER_AREA)
# resized_2 = cv.resize(img, (1920,720), interpolation= cv.INTER_CUBIC)

cv.imshow('Gray',gray)
# cv.imshow("Blur",blur)
# cv.imshow("Canny Image",canny)
# cv.imshow("Dilated",dilated)
# cv.imshow("Eroded",eroded)
# cv.imshow('RESIZED',resized)
# cv.imshow("RESIZED2",resized_2)


cv.imshow('Image',img)

cv.waitKey(0)