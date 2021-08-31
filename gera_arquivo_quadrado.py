
import matplotlib.pyplot as mp
from numpy.lib.financial import fv
import pandas as pd
import funVC as fvc
x=[630,630,1191,1191]
y=[279,692,279,692]
lateral1=[]
lateral2=[]
lateral3=[]
lateral4=[]
tamanho=2*561 +2*413 -1

xmax=561
ymax=413
x_1=[]
x_2=[]
valores_1 = pd.DataFrame()
y_1=[]
y_2=[]
j=0
#definir quadrado:
for i in range(x[0],x[2]):
    lateral1.append(i)
    lateral2.append(x[2]-j)
    j=j+1
#lateral1=range(x[0],x[2])
lateral1_y=[]
    
#lateral2=range(x[1],x[3])
lateral2_y=[]

for i in range(y[0],y[1]):
    lateral3.append(i)
#lateral3=range(y[0],y[1])
lateral3_x=[]
for i in range(y[2],y[3]):
    lateral4.append(i)
#lateral4=range(y[2],y[3])
lateral4_x=[]

x_1.append(lateral1) 
x_2.append(lateral2)
y_1.append(lateral3)
y_2.append(lateral4)
print(x_1[0][1])


for i in range(0,xmax):
    valores_1=pd.concat([pd.DataFrame({'pos_X':[x_1[0][i]],'pos_Y':[y[0]]}),valores_1],ignore_index=True)
    valores_1=pd.concat([pd.DataFrame({'pos_X':[x_2[0][i]],'pos_Y':[y[1]]}),valores_1],ignore_index=True)


for i in range(0,ymax):
    valores_1=pd.concat([pd.DataFrame({'pos_X':[x[0]],'pos_Y':[y_1[0][i]]}),valores_1],ignore_index=True)
    valores_1=pd.concat([pd.DataFrame({'pos_X':[x[2]],'pos_Y':[y_2[0][i]]}),valores_1],ignore_index=True)



for i in range(630,1191):
    lateral1_y.append(279)
    lateral2_y.append(692)
for i in range(279,692):
    lateral3_x.append(630)
    lateral4_x.append(1191)
a=[x_1, x_2]
#print(a)
#for i in a:
 #   fvc.tracking([x_1, x_2])
#valores_1.append(pd.DataFrame({'pos_X':[lateral1],
   #                'pos_Y':[lateral1_y] }),ignore_index = True)

#valores_1.append(pd.DataFrame({'pos_X':[lateral2],'pos_Y':[lateral2_y] }),ignore_index = True)
##valores_1.append(pd.DataFrame({'pos_X':[lateral3_x] ,'pos_Y':[lateral3]} ),ignore_index = True)
#valores_1.append(pd.DataFrame({'pos_X':[lateral4_x],'pos_Y':[lateral4]}),ignore_index = True)
#dirsaida="files_out" +"\saida_posicao_olho_quadrado.txt"
valores_1.to_csv("files_out\saida_posicao_olho_quadrado.txt")
#mp.plot(x_1,y[0],'.')
#mp.plot(x_2,y[1],'.')
#mp.plot(x[0],y_1,'.')
#mp.plot(x[2],y_2,'.')
mp.plot(valores_1['pos_X'],valores_1['pos_Y'],'.')
#mp.plot(x_1,y[1],'o')
#mp.plot(x_1,x[0],'o')
#mp.plot(y_1,x[1],'o')
mp.ylim(1080,0)
mp.xlim(0,1920)
mp.grid()
mp.show()