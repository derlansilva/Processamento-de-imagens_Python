# escrever nomes na imagens

import  cv2

image = cv2.imread('../imagens/baloes.jpg')

#A fonte na qual sera escrita
fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL

#dentro da imagem escreva DERLAN no eixo x 100 e y 100 colocar a cor branca
cv2.putText(image , "DERLAN" , (100 , 100) , fonte , 2 , (255 , 255 ,255) , 2 , cv2.LINE_AA)

cv2.imshow('image' , image)
cv2.waitKey(0)