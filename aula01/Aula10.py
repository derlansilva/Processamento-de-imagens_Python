#Hostograma, basicamente e um grafico mostrando as camadas

import  cv2
import matplotlib.pyplot as plt #biblioteca que cria um grafico

image = cv2.imread('../imagens/bolas.jpg')
blue = []
green = []
red =[]
Rblue=[]
Rgreen=[]
Rred = []

for i in range(0 , image.shape[0]):
    for x in range(0 , image.shape[1]):
        blue.append(image[i][x][0])
        green.append(image[i][x][0])
        red.append(image[i][x][0])


Lblue =sorted(set(blue))

for i in range(0 , len(Lblue)):
    somatoria = 0
    for x in range(0 , len(blue)):
        if Lblue[i] == blue[x]:
            somatoria +=1

    Rblue.append(somatoria)

Lgreen = sorted(set(green))

for y in  range(0 , len(Lgreen)):
    cont = 0
    for n in range(0 , len(green)):
        if Lgreen[y] == green[n]:
            cont +=1
    Rgreen.append(cont)

Lred = sorted(set(red))

for a in range(0 , len(Lred)):
    contRed=0
    for b in range(0 , len(red)):
        if Lred[a] == red[b]:
            contRed +=1

    Rred.append(contRed)

plt.plot(Rred , color='red')
plt.plot(Rgreen , color='green')
plt.plot(Rblue , color='blue')
plt.show()