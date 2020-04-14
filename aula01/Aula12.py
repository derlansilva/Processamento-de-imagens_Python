import  cv2

image = cv2.imread('../imagens/bolas.jpg')

for i in range(0 , image.shape[0] , 10):
    for x in range(0 , image.shape[1] , 10):
        image[i:i+3 , x:x+3]= (255, 255 , 255)

suave = cv2.medianBlur(image , 5)
suave = cv2.medianBlur(image , 11)

cv2.imshow('image' , image)
cv2.imshow('suave' , suave)
cv2.waitKey(0)