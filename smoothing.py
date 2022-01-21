import cv2 as cv

img = cv.imread("D:\\Photos\\Cherry\\IMG-20200601-WA0018-01.jpeg")


# Averaging 
# blur = cv.blur(img,(7,7))
# cv.imshow("Blurred", blur)


# Gaussian Blur
Gausblur = cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian Blue", Gausblur)


# Median Blur
# median = cv.medianBlur(img,3)
# cv.imshow("Median Blur",median)


# Bilateral Blur
bilateral = cv.bilateralFilter( img ,5,15, 20)
cv.imshow("Bilateral Blur",bilateral)


cv.imshow("Image",img)
cv.waitKey(0)