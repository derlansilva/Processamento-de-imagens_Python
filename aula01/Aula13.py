#Rastreando objetos na cor definida

import  cv2
import numpy as np

image = cv2.imread('../imagens/bolas.jpg')

blue = np.array([100 , 67 ,0] , dtype='uint8')
azulclaro = np.array([255 , 128 , 50] , dtype="uint8")

camera = cv2.VideoCapture(0) #capiturar videos da webcam

while True:
    (sucesso , frame) = camera.read()
    if not sucesso:
        break

    obj = cv2.inRange(frame , blue , azulclaro)

    (cnts, _) = cv2.findContours(obj.copy() , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) > 0:
        cnt = sorted(cnts , key=cv2.contourArea , reverse= True)[0]

        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))

        cv2.drawContours(frame , [rect] , -1, (0 , 255 , 255) , 2)

    cv2.imshow("janela" , frame)
    cv2.imshow("obk" , obj)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()