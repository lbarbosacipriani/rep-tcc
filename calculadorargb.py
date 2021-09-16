import cv2

imagem=cv2.imread("../imagens_artigos/Frame0_grayscale.png")



img_gray=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)


#img_gray=cv2.GaussianBlur(img_gray,(7,7),0)

img_equalizada=cv2.equalizeHist(img_gray)
cv2.imshow('originalk',img_equalizada)
cv2.waitKey()