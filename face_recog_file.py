import numpy as np
import cv2 as cv
import os

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (height, width)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = []

for i in os.listdir(r"D:\Photos\openCV"):
    people.append(i)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img =cv.imread(r"D:\Photos\Manali\IMG_20211019_163728714.jpg")
img = rescaleFrame(img,scale = 0.5)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Test Image",gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,8)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (x,y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness =2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow("Detected face",img)
cv.waitKey(0)
