import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3),dtype='uint8')

#1. STRIPS

# blank[100:200] = 0,255,0
# blank[0:10,100:200] = 255,255,255
# cv.imshow('BOX',blank)


#2. RECTANGLE

# cv.rectangle(blank,(100,100),(325,400),(255,0,100),thickness=-1)
# cv.imshow('RECTANGLE',blank)


#3. CIRCLES

# cv.circle(blank,(250,250),69,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)


#4. LINE

# cv.line(blank,(0,0),(250,250),(255,100,120),thickness=2)
# cv.imshow('LINE',blank)


#5. TEXT

cv.putText(blank,'HELLO',(blank.shape[1]//2,blank.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1,(210,140,120),2)
cv.imshow('TEXT',blank)

cv.waitKey(0)