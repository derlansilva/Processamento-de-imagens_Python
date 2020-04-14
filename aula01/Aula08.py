#Separando canais de cores

import  cv2

image = cv2.imread('../imagens/baloes.jpg')

(b,g,r)=cv2.split(image)

cv2.imshow('image' , image )
cv2.imshow('b' , b)
cv2.imshow('img' , g)
cv2.imshow('r' , r)
cv2.waitKey(0)