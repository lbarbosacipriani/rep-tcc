import cv2
import matplotlib.pyplot as mp

imagem=cv2.imread('../imagens_artigos/Grayscale.jpg')
imagem =cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
mp.hist(imagem,256,[0,256])
mp.show()
#