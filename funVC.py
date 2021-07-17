#from pyautogui import position as pd
#from pyautogui import moveTo as mt
import win32api as win
perc_x = .1;
perc_y=.1;
dt=3; # velocidade com que o cursor vai andar.


def verifica_direcao(pontoInteresse, origem):
    x_ponto=float (pontoInteresse[0]- origem[0])
    y_ponto=float (pontoInteresse[1]- origem[1])
   # print("Pontos x: "+ str (x_ponto) +" | y: "+ str (y_ponto) )
    if((x_ponto > 0 and y_ponto > 0) or (x_ponto > 0 and y_ponto >= 0) or (x_ponto >= 0 and y_ponto > 0) ):
        #return "Quadrante 1"
     #   print("Quadrante 1")
        return [dt,dt]
    if((x_ponto < 0 and y_ponto > 0) or (x_ponto < 0 and y_ponto >= 0) or (x_ponto <= 0 and y_ponto > 0)  ):
       # return "Quadrante 2"
       # print("Quadrante 2")
        return [-dt,dt]
    if((x_ponto < 0 and y_ponto < 0) or (x_ponto < 0 and y_ponto <= 0) or (x_ponto <= 0 and y_ponto < 0) ):
       # return "Quadrante 3"  
     #   print("Quadrante 3") 
        return [-dt,-dt]    
    if((x_ponto > 0 and y_ponto < 0)) or (x_ponto > 0 and y_ponto <= 0) or (x_ponto >= 0 and y_ponto < 0):
      #  return "Quadrante 4"
       # print("Quadrante 4")
        return[dt,-dt]
    if(x_ponto == 0 and y_ponto ==0):
     #   print("Origem!!")
        return[0,0]
    

def  atuaMouse(posicaoNova):
    #posicao_x, posicao_y=pd()
    #
    posicao_x, posicao_y = win.GetCursorPos()
    # define vetor. 
    posicaoNova[0]=(posicao_x+posicaoNova[0])
    posicaoNova[1]= (posicao_y+posicaoNova[1])
    win.SetCursorPos((posicaoNova[0],posicaoNova[1]))
   # mt(posicaoNova[0],posicaoNova[1])

def defineOrigem(x,y,w,h):
    #funcao para definir nova origem do sistema. 
        x_calib_0=x+int(w/2)
        y_calib_0=y+int(h/2)
        return [x_calib_0,y_calib_0]