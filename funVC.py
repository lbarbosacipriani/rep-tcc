#from pyautogui import position as pd
#from pyautogui import moveTo as mt
import win32api as win
import math
import numpy as np
import matplotlib.pyplot as mp
perc_x = .1;
perc_y=.1;
LimiteDist=10
dt=60; # velocidade com que o cursor vai andar.
eixo_x = []
eixo_y=[]
atuador=[0,0]
def verifica_direcao(pontoInteresse, origem):
    x_ponto=float (pontoInteresse[0]- origem[0])
    y_ponto=float (pontoInteresse[1]- origem[1])
    print("x_pomto: " + str(x_ponto))
    distancia=pow((pow(x_ponto,2) + pow(y_ponto,2)),1/2)
       # print("Pontos x: "+ str (x_ponto) +" | y: "+ str (y_ponto) )
    if(x_ponto*y_ponto==0):
     #   print("Origem!!")
        return[0, 0]
    else:
        
        if(x_ponto<0):
          theta=math.atan(-y_ponto/x_ponto)
          return [(x_ponto-dt*math.cos(theta))/distancia,(y_ponto+ dt*math.sin(theta))/distancia]
        else:
          theta=math.atan(y_ponto/x_ponto)
          return [(x_ponto+dt*math.cos(theta))/distancia,(y_ponto+ dt*math.sin(theta))/distancia]
    


def  atuaMouse(direcao,origem,pontoInteresse):
    #posicao_x, posicao_y=pd()
    #
    if(raioMinimo(origem,pontoInteresse)):
        posicao_x, posicao_y = win.GetCursorPos()
    # define vetor. 
        atuador[0]=(posicao_x+direcao[0])
        atuador[1]= (posicao_y+direcao[1])
        tracking(pontoInteresse)
        win.SetCursorPos([int(atuador[0]), int(atuador[1])])
    else:
        print("Mantem posicao")
   # mt(posicaoNova[0],posicaoNova[1])

   

def defineOrigem(x,y,w,h):
    #funcao para definir nova origem do sistema. 
        x_calib_0=x+int(w/2)
        y_calib_0=y+int(h/2)
        return [x_calib_0,y_calib_0]


def raioMinimo(origem,pontoInteresse):
    posicao_x, posicao_y = origem
    x_raio = pontoInteresse[0] - posicao_x
    y_raio = pontoInteresse[1] - posicao_y
    distancia=pow((pow(x_raio,2) + pow(y_raio,2)),1/2)
    if(distancia >=LimiteDist):
        print("Distancia limite: "+ str(distancia))
        return True
    else:
        return False
 

def tracking(pontoInteresse):
    eixo_x.append(pontoInteresse[0])
    eixo_y.append(pontoInteresse[1])


def plot_cursor():
    mp.plot(eixo_x, eixo_y,'r')
    mp.show()


    
def defineOrigem1(x,y):
    #funcao para definir nova origem do sistema. 
        x_calib_0=x
        y_calib_0=y
        return [x_calib_0,y_calib_0]