import cv2 as cv

# img = cv.imread("D:\\Photos\\innogeeks\\IMG_20200502_133522.jpg")

# cv.imshow('Team', img)

# cv.waitKey(0)

capture = cv.VideoCapture("D:\\Photos\\Untitled 52_720p.mp4")

while True:
    isTrue, frame= capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()