import cv2
import funVC as fvc
import numpy as np
video = cv2.VideoCapture('videos/v2.mp4')
#video = cv2.VideoCapture(0)
calibracao = False
calibracao_pre = True
# definicao da projecao da visao.
# roi = frame[260:795, 537:1400]
kernel = np.ones((5, 5), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

org = (50, 50)

# fontScale
fontScale = 0.5

# Blue color in BGR
color = (0, 255, 0)

# Line thickness of 2 px
thickness = 2
# video=cv2.VideoCapture(0)
ret, frame = video.read()

# calibracao

while frame is not None:
      if cv2.waitKey(5) & 0xFF == ord('r'):
            calibracao_pre = True
     # frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
      roi = frame[60:280, 100:300]
        # ROI para o video gravado;
      roi = frame[250:500, 40:300]

     # filtro passa baixa:
      frame = np.array(roi)
      rows, cols, _ = frame.shape
      img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     # cv2.line(frame,(0,int(rows/2)),(cols,int(rows/2)),(123,123,123),2)
     #  cv2.line(frame,(int(cols/2),0),(int(cols/2),rows),(123,123,123),2)
        # img_gray=sobel(img_gray)

        # blur para diminuir frequencias zuadas.
      img_gray = cv2.blur(img_gray, (11, 11))
      img_gray = cv2.equalizeHist(img_gray)
     #  img_gray=cv2.erode(img_gray,kernel)

      img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)

        # tratamos os limiares da imagem.
      _, threshold = cv2.threshold(img_gray, 0, 200, cv2.THRESH_BINARY_INV)
        # threshold = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        #      cv2.THRESH_BINARY,11,2)
      contours, hierarchy = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # pegamos o maior contorno e usamos como referencia.
      contours = sorted(
            contours, key=lambda x: cv2.contourArea(x), reverse=True)

      for ctr in contours:
            cv2.moments(ctr)  # momentos estatíticos do contorno.
            (x, y, w, h) = cv2.boundingRect(ctr)  # geramos um retangulo
            # cv2.drawContours(frame,[ctr],-1,(0,0,255),3)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 255, 0),1)
            
            # desenhando o centro do retagngulo:
            cv2.line(frame, (x+int(w/2), 0),
                     (x+int(w/2), rows), (205, 68, 239), 1)
            cv2.line(frame, (0, y+int(h/2)),
                     (cols, y+int(h/2)), (205, 68, 239), 1)
            if(calibracao == False):
                # definir funcao de calibracao por tempo.
                [x_calib_0, y_calib_0] = fvc.defineOrigem(x, y, w, h)
                origem = [x_calib_0, y_calib_0]
                calibracao = True
            cv2.line(frame, (x_calib_0, 0),
                     (x_calib_0, rows), (0,255,0), 1)
            cv2.line(frame, (0, y_calib_0),
                     (cols, y_calib_0), (0,255,0), 1)
            # liga a origem do sistema ao ponto do olho
            cv2.putText(frame, ' F_0', (origem[0] + 2, origem[1] - 2), font, fontScale, color, thickness, cv2.LINE_AA)

            
            cv2.line(frame, (x_calib_0, y_calib_0),
                     (x+int(w/2), y+int(h/2)), (68, 239, 233), 2)
            ponto_interesse = [x+int(w/2), y+int(h/2)]
            cv2.putText(frame, ' F_1', (ponto_interesse[0]+2,ponto_interesse[1] -2), font,
                        fontScale, (205, 68, 239), thickness, cv2.LINE_AA)
          #  print(fvc.verifica_direcao(ponto_interesse,origem))
            direcao = fvc.verifica_direcao(ponto_interesse, origem)
            if calibracao_pre == True:
                fvc.atuaMouse(direcao, origem, ponto_interesse)
          #  fvc.atuaMouse(fvc.verifica_direcao(ponto_interesse,origem))
          #  print("Ponto de interesse: " + str(ponto_interesse))
          #  print("Origem: "+ str(origem))
          #  print("------------")
            break
      if ret == True:
            cv2.imshow('Frame', frame)

      if cv2.waitKey(5) & 0xFF == ord('q'):
            break
      if cv2.waitKey(5) & 0xFF == ord(' '):
            [x_calib_0, y_calib_0] = fvc.defineOrigem(x, y, w, h)
            calibracao = False
      ret, frame = video.read()
      #frame=cv2.flip(frame,1)

fvc.plot_cursor()
cv2.destroyAllWindows()

