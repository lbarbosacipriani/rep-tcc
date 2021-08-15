import cv2
import funVC as fvc
import numpy as np
import matplotlib.pyplot as mp
video=cv2.VideoCapture('videos/v2.mp4')   
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 0.5
   
# Blue color in BGR
color = (0, 255, 0)
  
# Line thickness of 2 px
thickness = 1
print(type(video))

ret, frame=video.read()
rows,cols,_=frame.shape
frame=frame[250:500, 40:300]
inicio=(300,250)
fim=(20,430)
img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
img_gray= cv2.blur(img_gray,(11,11))
mp.hist(img_gray.ravel(),256,[0,256])
mp.show()
img_gray =cv2.equalizeHist(img_gray)
mp.hist(img_gray.ravel(),256,[0,256])
mp.show()
img_gray=cv2.GaussianBlur(img_gray,(9,9),0)
_, threshold=cv2.threshold(img_gray,0,200,cv2.THRESH_BINARY_INV)
contours, hierarchy  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for ctr in contours:
        M=cv2.moments(ctr)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        #(x,y,w,h)= cv2.boundingRect(ctr) # geramos um retangulo 
        #cv2.drawContours(frame,[ctr],-1,(0,0,255),3)
       # cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 255, 0),1)
        cv2.circle(frame,(cx,cy),10,(255, 255, 0))
        [x_calib_0,y_calib_0]=fvc.defineOrigem1(cx,cy)
        #cv2.rectangle(frame,inicio,fim,(255,0,0),2)
cv2.line(frame,(x_calib_0,0),(x_calib_0,rows),(0,255,0),1)
cv2.line(frame,(0,y_calib_0),(cols,y_calib_0),(0,255,0),1)
org = (cx+4, cy-1)
cv2.putText(frame, ' F_0', org, font, fontScale, color, thickness, cv2.LINE_AA)
#cv2.putText(frame, ' F_0', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('Frame 0',frame)

cv2.waitKey()