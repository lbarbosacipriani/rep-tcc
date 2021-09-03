
#leitura de arquivos. 
import pandas as pd
import statistics
import matplotlib.pyplot as mp
figura_quadrado=pd.read_csv("files_out/saida_posicao_olho_quadrado.txt",sep=",")
figura_cursor=pd.read_csv("files_out/saida_posicao_olho_29_18_57.txt",sep=",")
#figura_cursor=pd.read_csv("files_out/saida_posicao_olho_quadrado.txt",sep=",")
distancias_x=[]
figura_cursor=figura_cursor.iloc[::-1]
figura_quadrado=figura_quadrado.iloc[::-1]
erro_quadratico_aux=[]
erro_pixel=[]
#cálculo de todas as distancias:
print(len(figura_cursor.index))
for j in figura_cursor.index:
    for i in figura_quadrado.index:
        x=figura_cursor['pos_X'][j] - figura_quadrado['pos_X'][i]
        y=figura_cursor['pos_Y'][j] - figura_quadrado['pos_Y'][i]
        #if i == 61:
           # print("oi")
        distancias_x.append((x**2 + y**2)**(1/2))
       # distancias_y.append(abs(figura_cursor['pos_Y'][j] - figura_quadrado['pos_Y'][i]))
        #dist_gera
    erro_pixel.extend([min(distancias_x)])
    distancias_x=[]
#print(distancias)
t=[list(range(0,len(erro_pixel)))]
#print(erro_pixel)
#print(figura_quadrado['pos_X'])
#print(len(erro_pixel))
#print(len(t[0]))
eqm=statistics.mean(erro_pixel)
erro_acumulado=sum(erro_pixel)
desvio_padrao=statistics.stdev(erro_pixel)
print("erro médio: " + str(eqm))
print("erro acumulado: " + str(erro_acumulado))
print("desvio padrao: " + str(desvio_padrao))
#print(t[0])
mp.plot(t[0],erro_pixel)
mp.grid()
mp.show()
#print(erro_pixel)
#print(list(figura_quadrado['pos_X']))
#print(figura_quadrado[' '])

