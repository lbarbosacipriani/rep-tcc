import cv2

imagem=cv2.imread("../imagens_artigos/lena_original.png")



img_gray=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
img_gray=cv2.blur(imagem,(7,7))
cv2.imshow('originalk',img_gray)
cv2.waitKey()



_, threshold=cv2.threshold(img_gray,190,255,cv2.THRESH_BINARY)#,cv2.THRESH_BINARY,11,2)
cv2.imshow('originalk',threshold)

cv2.waitKey()