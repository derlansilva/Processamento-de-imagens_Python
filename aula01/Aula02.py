import  cv2

imagem = cv2.imread("../imagens/baloes.jpg")
for i in range(0 , 100):
    for x in range(0 , 100):
        imagem[i][x] = (255, 255,255)

imagem[100:110, :]= (233, 233  , 233)

print(imagem[2][1])
cv2.imshow('imagem' , imagem)
cv2.waitKey(0)