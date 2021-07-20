import cv2
import funVC as fvc
import numpy as np
#video=cv2.VideoCapture('videos/v2.mp4')   
video=cv2.VideoCapture(0) 
    # or
width  = video.get(3)  # float `width`
height = video.get(4)  # float `height`
print("altura: "+ str (height) + " comprimeirot: "+ str (width))

while True:
    ret, frame=video.read()
    frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    
    #roi=frame[50:400, 100:300]
    #frame=roi
    if ret ==True:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break