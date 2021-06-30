import cv2
import funVC as fvc
import numpy as np
video=cv2.VideoCapture('videos/v1.mp4')   
#video=cv2.VideoCapture(0) 
calibracao= False;
ponto_interesse=[0,0]
origem=[0,0]
# definicao da projecao da visao. 
    #roi = frame[260:795, 537:1400]
kernel = np.ones((5, 5), np.uint8)
#video=cv2.VideoCapture(0)
while True:
    ret, frame=video.read()
    #roi = frame[260:795, 537:1400]
    rows,cols,_=frame.shape
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # cv2.line(frame,(0,int(rows/2)),(cols,int(rows/2)),(123,123,123),2)
  #  cv2.line(frame,(int(cols/2),0),(int(cols/2),rows),(123,123,123),2)
    #img_gray=sobel(img_gray)
    
    
    img_gray =cv2.equalizeHist(img_gray)
    img_gray=cv2.erode(img_gray,kernel)

    img_gray=cv2.GaussianBlur(img_gray,(9,9),0)

    # tratamos os limiares da imagem. 
    _, threshold=cv2.threshold(img_gray,0,256,cv2.THRESH_BINARY_INV)
    #threshold = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
     #      cv2.THRESH_BINARY,11,2)
    contours, hierarchy  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True) # pegamos o maior contorno e usamos como referenica.

    for ctr in contours:
        (x,y,w,h)= cv2.boundingRect(ctr) # geramos um retangulo 
        #cv2.drawContours(frame,[ctr],-1,(0,0,255),3)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # desenhando o centro do retagngulo:
        cv2.line(frame,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(frame,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        if(calibracao==False):
            #definir funcao de calibracao por tempo. 
            x_calib_0=x+int(w/2)
            y_calib_0=y+int(h/2)
            origem = [x_calib_0,y_calib_0]
            calibracao =True
        cv2.line(frame,(x_calib_0,0),(x_calib_0,rows),(123,123,123),2)
        cv2.line(frame,(0,y_calib_0),(cols,y_calib_0),(123,123,123),2)
        fvc.atuaMouse(fvc.verifica_direcao(ponto_interesse,origem))
        #liga a origem do sistema ao ponto do olho
        cv2.line(frame,(x_calib_0,y_calib_0),(x+int(w/2),y+int(h/2)),(0,0,255),2)
        ponto_interesse = [x+int(w/2), y+int(h/2)]
      #  fvc.atuaMouse(fvc.verifica_direcao(ponto_interesse,origem))
 
      #  print("Ponto de interesse: " + str(ponto_interesse))
      #  print("Origem: "+ str(origem))
      #  print("------------")
        break

    if ret ==True:
        cv2.imshow('Frame',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

cv2.destroyAllWindows()
 