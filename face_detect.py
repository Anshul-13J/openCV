from cgitb import reset
import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (height, width)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("D:\\Photos\\photos\\IMG_20211022_121343644-01.jpeg")
# cv.imshow("Image", img)
img = rescaleFrame(img,0.3)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors = 7)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness =2)

cv.imshow("Recognized faces", img)
print(f"Number of faces recognized: {len(faces_rect)} and their coordinates are {faces_rect}")
cv.waitKey(0)