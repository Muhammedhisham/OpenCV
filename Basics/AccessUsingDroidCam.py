import cv2 as cv
vid=cv.VideoCapture(0)
# vid=cv.VideoCapture('http://ip:port/video') using Droid cam app
# if we have to access any video instead of the http link provide the path where the video is stored
while vid.isOpened():
    # print(frame=vid.read())
    ret,frame=vid.read()
    if ret ==True:
        cv.imshow('video',frame)
    if cv.waitKey(1)==ord('c'):
        break

