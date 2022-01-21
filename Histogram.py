import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")
blank = np.zeros(img.shape[:2])
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2],dtype = 'uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 130, 255, -1)
mask = cv.bitwise_and(gray,gray,mask = circle)
gray_hist = cv.calcHist([gray], [0], mask, [256],[0,256])
cv.imshow("Image",img)
cv.imshow("Mask",mask)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
# colors = ('b','g','r')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,color=col)
#     plt.xlim([0,256])
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
