import pyautogui as pd
perc_x = 100;
perc_y=100;


def fybVC():
    return 1


def verifica_direcao(pontoInteresse, origem):
    x_ponto=float (pontoInteresse[0]- origem[0])
    y_ponto=float (pontoInteresse[1]- origem[1])
   # print("Pontos x: "+ str (x_ponto) +" | y: "+ str (y_ponto) )
    if((x_ponto > 0 and y_ponto > 0) or (x_ponto > 0 and y_ponto >= 0) or (x_ponto >= 0 and y_ponto > 0) ):
        #return "Quadrante 1"
        print("Quadrante 1")
        return [100,100]
    if((x_ponto < 0 and y_ponto > 0) or (x_ponto < 0 and y_ponto >= 0) or (x_ponto <= 0 and y_ponto > 0)  ):
       # return "Quadrante 2"
        print("Quadrante 2")
        return [-100,100]
    if((x_ponto < 0 and y_ponto < 0) or (x_ponto < 0 and y_ponto <= 0) or (x_ponto <= 0 and y_ponto < 0) ):
       # return "Quadrante 3"  
        print("Quadrante 3") 
        return [-100,-100]    
    if((x_ponto > 0 and y_ponto < 0)) or (x_ponto > 0 and y_ponto <= 0) or (x_ponto >= 0 and y_ponto < 0):
      #  return "Quadrante 4"
        print("Quadrante 4")
        return[100,-100]
    if(x_ponto == 0 and y_ponto ==0):
        print("Origem!!")
    

def  atuaMouse(posicaoNova ):
    passox,passoy= DefineTaxaMouse()
    posicao_x, posicao_y=pd.position()
    posicaoNova[0]=posicao_x + passox
    posicaoNova[1]=posicao_y + passoy
    pd.moveTo(posicaoNova[0],posicaoNova[1])


def DefineTaxaMouse():
    # infos da camera. 
    x_screen, y_screen = pd.size()
    passo_x=x_screen/perc_x;
    passo_y=y_screen/perc_y;
    print("passo x: " +str (passo_x) + " passo y: " + str(passo_y))
    return (passo_x, passo_y)
