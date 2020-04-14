#recortar imagens

import  cv2

image = cv2.imread('../imagens/baloes.jpg')

imagemRecortar  = image[100 : 200 , 100:200]

cv2.imshow('image' , imagemRecortar)
cv2.imshow('img' , image)
cv2.waitKey(0)

#quando cortamos uma imagens perdemos a parte que foi cortada