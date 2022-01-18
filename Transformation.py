import cv2 as cv
import numpy as np

img = cv.imread("D:\\College\\innogeeks\\Ec53xzgUMAEz-ME.jpg")

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)



# rotated = rotate(img,90)
# cv.imshow("Rotated",rotated)

# translated = translate(img,50,50)
# cv.imshow("Image",translated)

# resized = cv.resize(img,(500,500),interpolation= cv.INTER_CUBIC)
# cv.imshow('RESIZED', resized)

# fliped = cv.flip(img, -1)
# cv.imshow("Fliped",fliped)





cv.imshow("Normal",img)

cv.waitKey(0)