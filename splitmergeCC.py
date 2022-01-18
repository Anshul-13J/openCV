import cv2 as cv
import numpy as np

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")
blank = np.zeros(img.shape[:2], dtype = 'uint8')

cv.imshow("Image",img)

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)


print(b)
print(g)
print(r)
print(img)


merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)
cv.waitKey(0)