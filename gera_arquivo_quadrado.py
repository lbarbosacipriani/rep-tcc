
import matplotlib.pyplot as mp
from numpy.lib.financial import fv
import pandas as pd
import funVC as fvc
x=[630,630,1191,1191]
y=[279,692,279,692]

x_1=[]
x_2=[]

y_1=[]
y_2=[]
#definir quadrado:
lateral1=range(x[0],x[2])
lateral2=range(x[1],x[3])
lateral3=range(y[0],y[1])
lateral4=range(y[2],y[3])

x_1.append(lateral1) 
x_2.append(lateral2)
y_1.append(lateral3)
y_2.append(lateral4)
a=[x_1, x_2]
print(a)
for i in a:
    fvc.tracking([x_1, x_2])
valores_1= pd.DataFrame({'pos_X':lateral1 ,
                   'pos_Y':y[0] })

valores_1.append(pd.DataFrame({'pos_X':lateral2 ,
                   'pos_Y':y[1] }))
valores_1.append(pd.DataFrame({'pos_X':x[0] ,
                   'pos_Y':lateral3 }))
valores_1.append(pd.DataFrame({'pos_X':x[2] ,
                   'pos_Y':lateral4 }))
#dirsaida="files_out" +"\saida_posicao_olho_quadrado.txt"
valores_1.to_csv("files_out\saida_posicao_olho_quadrado.txt")

p=[400, 1000]
erro = (p)
mp.plot(x_1,y[0],'.')
mp.plot(x_2,y[1],'.')
mp.plot(x[0],y_1,'.')
mp.plot(x[2],y_2,'.')
#mp.plot(x_1,y[1],'o')
#mp.plot(x_1,x[0],'o')
#mp.plot(y_1,x[1],'o')
#mp.show()