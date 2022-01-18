import cv2 as cv
from cv2 import RETR_LIST
import numpy as np

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")

blank= np.zeros(img.shape,dtype= 'uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray,(1,1),cv.BORDER_DEFAULT)  #To reduce the no. of contours
canny = cv.Canny(gray,125,175)


#USING TRESHOLD METHOD
ret, tresh = cv.threshold(canny,125,255, cv.THRESH_BINARY)




contours, hieararchies = cv.findContours(canny, RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} number of contour(s) are found!! ')


#Drawing contours on blank
cv.drawContours(blank, contours,-1,(0,0,255),1)

# cv.imshow('Canny',canny)
cv.imshow('Draw contours',blank)
# cv.imshow("TRESH", tresh)

cv.waitKey(0)