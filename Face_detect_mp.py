import cv2 as cv
import mediapipe as mp
import math
from cvzone.FaceDetectionModule import FaceDetector

detector = FaceDetector(minDetectionCon= 0.45)

img = cv.imread("D:\\Photos\\photos\\opencv\\Vm4h1LhMEMQFGZg4.jpg")

img,bbox = detector.findFaces(img,draw=False)
for face in bbox:
    x,y,w,h = face["bbox"]
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness= 2)
cv.imshow("Image",img)
cv.waitKey(0)