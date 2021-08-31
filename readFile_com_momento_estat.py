import cv2
import funVC as fvc
import numpy as np
import pandas as pd
import testes_com_erro as test
import datetime 
import win32api as win
import matplotlib.pyplot as mp

figura_quadrado=pd.read_csv("files_out/saida_posicao_olho_quadrado.txt",sep=",")
t=[range(0,len(figura_quadrado))]
#video = cv2.VideoCapture('videos/v2.mp4')
file_saida= pd.DataFrame()
video = cv2.VideoCapture(0)
calibracao = False
calibracao_pre = False           
# definicao da projecao da visao.
# roi = frame[260:795, 537:1400]
kernel = np.ones((5, 5), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
redefinir_origem=0
limite_redefinir_origem=60
org = (50, 50)

# fontScale
fontScale = 0.5

# Blue color in BGR
color = (0, 255, 0)

# Line thickness of 2 px
thickness = 1
# video=cv2.VideoCapture(0)
ret, frame = video.read()

# calibracao
test.gera_imagem()

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
            M=cv2.moments(ctr)
            if(M['m00'] != 0):
                  cx = int(M['m10']/M['m00'])
                  cy = int(M['m01']/M['m00'])
                  cv2.circle(frame,(cx,cy),10,(255, 255, 0))
            else:
                  (x, y, w, h) = cv2.boundingRect(ctr) 
                  cx=x +int(w/2)
                  cy=y +int(h/2)
            #(x, y, w, h) = cv2.boundingRect(ctr)  # geramos um retangulo
            # cv2.drawContours(frame,[ctr],-1,(0,0,255),3)
           # cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 255, 0),1)
           
            # desenhando o centro do retagngulo:
            cv2.line(frame, (cx, 0),
                     (cx, rows), (205, 68, 239), 1)
            cv2.line(frame, (0, cy),
                     (cols, cy), (205, 68, 239), 1)
            if(calibracao == False):
                # definir funcao de calibracao por tempo.
                [x_calib_0, y_calib_0] = fvc.defineOrigem1(cx, cy)
                origem = [x_calib_0, y_calib_0]
                calibracao = True
            cv2.line(frame, (x_calib_0, 0),
                     (x_calib_0, rows), (0,255,0), 1)
            cv2.line(frame, (0, y_calib_0),
                     (cols, y_calib_0), (0,255,0), 1)
            # liga a origem do sistema ao ponto do olho
            cv2.putText(frame, ' F_0', (origem[0] + 2, origem[1] - 2), font, fontScale, color, thickness, cv2.LINE_AA)

            
            cv2.line(frame, (x_calib_0, y_calib_0),
                     (cx, cy), (68, 239, 233), 2)
            ponto_interesse = [cx, cy]
            cv2.putText(frame, ' F_1', (ponto_interesse[0]+2,ponto_interesse[1] -2), font,
                        fontScale, (205, 68, 239), thickness, cv2.LINE_AA)
          #  print(fvc.verifica_direcao(ponto_interesse,origem))
            direcao = fvc.verifica_direcao(ponto_interesse, origem)
            if calibracao_pre == True:
                  fvc.atuaMouse(direcao, origem, ponto_interesse)
                #salva a posicao do cursor:
                  pontoInteresse=win.GetCursorPos()
                  entrada=pd.DataFrame({'pos_X':[pontoInteresse[0]],'pos_Y':[pontoInteresse[1]]})
                  file_saida=pd.concat([entrada,file_saida],ignore_index=True )
                #file_saida.concat(ponto_interesse)
              #  print(file_saida)
          #  fvc.atuaMouse(fvc.verifica_direcao(ponto_interesse,origem))
          #  print("Ponto de interesse: " + str(ponto_interesse))
          #  print("Origem: "+ str(origem))
          #  print("------------")
            break
      
      if ret == True:
            cv2.imshow('Frame', frame)
      #salvando arquivo de saída:
      if cv2.waitKey(5) & 0xFF == ord('q'):
            break
      if (cv2.waitKey(5) & 0xFF == ord(' '))or redefinir_origem >=limite_redefinir_origem:
            [x_calib_0, y_calib_0] = fvc.defineOrigem1(cx, cy)
            calibracao = False
            redefinir_origem=0
      ret, frame = video.read()
     # redefinir_origem=redefinir_origem+1
      frame=cv2.flip(frame,1) 
#file_saida = fvc.pegaDataframe()
file_saida.to_csv("files_out" +"\saida_posicao_olho_"+str(datetime.datetime.now().day)+ "_" +str(datetime.datetime.now().hour) + "_"+ str(datetime.datetime.now().minute) + ".txt")
#file_saida.to_csv("saida_posicao_olho_quadradorrfrf.txt")
mp.plot(figura_quadrado['pos_X'],figura_quadrado['pos_Y'],'.')
mp.ylim(1080,0)
mp.xlim(0,1920)
mp.grid()
fvc.plot_cursor()
cv2.destroyAllWindows()

