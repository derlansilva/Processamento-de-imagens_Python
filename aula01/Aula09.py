#limiarização

import  cv2

image = cv2.imread('../imagens/baloes.jpg')

for i in range(0 , image.shape[0]):
    for x in range(0 , image.shape[1]):
        image[i][x] = (0 , 0 , 0)


fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image ,'255',(15,65),fonte, 2,(255,255,255),2)
cv2.putText(image , '70' , (125,65) , fonte, 2,(70,70,70),2)
cv2.putText(image, '100' , (255, 65), fonte , 2 , (100 , 100, 100),2)
cv2.putText(image , '1' , (406 , 65) , fonte , 2, (1,1,1),2)

for y in range(0 , image.shape[0]):
    for j in range(0 , image.shape[1]):
        if image[y][j][0]!= 0:
            image[y][j]=(255, 255 ,255)

cv2.imshow('janela' , image)
cv2.waitKey(0)