import cv2
import funVC as fvc
import numpy as np
#video=cv2.VideoCapture('videos/v2.mp4')   
video=cv2.VideoCapture(0) 
while True:
    ret, frame=video.read()
    if ret ==True:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break