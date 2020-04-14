#redimencionamento de imagens

import  cv2

img= cv2.imread('../imagens/baloes.jpg')

largN = 100
altuN = 20

#se a uma das porpoções for maior que a outra a imagem fica distorcida

l = img.shape[1]
a = img.shape[0]
proporcao = float(a/l)
larguraNova = 150
alturaNova = int(larguraNova*proporcao)

image = cv2.resize(img , (largN , altuN))

imagem = cv2.resize(img , (larguraNova , alturaNova))


cv2.imshow('img' , img)
cv2.imshow('image' , imagem)
cv2.imshow('imagem' , imagem)
cv2.waitKey(0)

#redimencionamento não , a imagem diminui , mas não perde nada