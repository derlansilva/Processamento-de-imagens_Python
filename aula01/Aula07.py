#rotacionar imagem na verdade imvertida

import  cv2

img = cv2.imread('../imagens/baloes.jpg')

imgRotacionada = img[: , :: -1]
eixoY = img[::-1 , ::-1]

cv2.imshow('img' , img)
cv2.imshow('imagem' , imgRotacionada)
cv2.imshow('eixo' , eixoY)
cv2.waitKey(0)