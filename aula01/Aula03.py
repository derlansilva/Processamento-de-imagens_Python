import  cv2

branco = (255 , 255 , 255)
image = cv2.imread('../imagens/baloes.jpg')

#altera todos os pikeus da imgem para a cor que esta na variavel
#for i in range(0 , image.shape[0], 1):
 #   for x in range(0 , image.shape[1] , 10 ):
  #      image[i][x] = branco

#cv2.imshow('image' , image)
#cv2.waitKey(0)

#da posicão j mais 5 pikels e posição a + 5 pikels pulando de 20 em 20 ficaram na cor branca
#for j in range(0 , image.shape[0] , 20):
 #   for a in range(0 , image.shape[1], 20):
  #      image[j:j+5 , a:a+5]= branco
#cv2.imshow('img' , image)
#cv2.waitKey(0)

for i in range(0 , image.shape[0]):
    for x in range(0 , image.shape[1]):
        if image[i][x][0] ==  (255):
            image[i][x] = branco

cv2.imshow('image' , image)
cv2.waitKey(0)