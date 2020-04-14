import cv2

image = cv2.imread('../imagens/baloes.jpg')
img = cv2.imread('../imagens/image.jpg')

cv2.imshow('imagem' , image)
cv2.waitKey(0)

#for i in range(0, image.shape[0]):
 #   for y in range(0, image.shape[1]):
  #      print(image[i][y])

