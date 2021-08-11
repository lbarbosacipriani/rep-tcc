import funVC as fv
import pyautogui as pd
import math
import numpy as np

#print(fv.verifica_direcao([100,100],[0,0]))
#fv.atuaMouse([100,-100])
#print(pd.position())

ponto_interesse = [5,-2]
if(ponto_interesse[0]<0):
    theta=math.atan(-ponto_interesse[1]/ponto_interesse[0])
    print("cosseno: " + str(-math.cos(theta)))
else:
    theta=math.atan(ponto_interesse[1]/ponto_interesse[0])
    print("cosseno: " + str(math.cos(theta)))
print("angulo theta "+ str(theta))

print("senho : "+ str(math.sin(theta)))