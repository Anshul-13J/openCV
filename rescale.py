import cv2 as cv

def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (height, width)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
    



# img = cv.imread("D:\\Photos\\innogeeks\\IMG_20200502_133522.jpg")
# img_rescaled = rescaleFrame(img,0.5)
# cv.imshow('INNOGEEKS',img_rescaled)
# cv.waitKey(0)

# capture = cv.VideoCapture("D:\\Photos\\Untitled 52_720p.mp4")

# while True:
#     isTrue, frame= capture.read()
    
#     frame_resized= rescaleFrame(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('Video_RESIZED',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()





live = cv.VideoCapture(0)
live.set(3,1920)
live.set(4,1080)
live.set(10,1000)
while True:
    isTrue, frame= live.read()
    
 #   frame_resized= frame
 #   frame_resized.set(3,1280)
 #   frame_resized.set(4,720)
    cv.imshow('Video',frame)
#  cv.imshow('Video_RESIZED',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
live.release()
cv.destroyAllWindows()