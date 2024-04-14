#open cv
#pip install opencv-python

import cv2 
#abrir uma imagem 

imagem = cv2.imread("./aula1304/img/campeaosp.jpg")
cv2.imshow("janela", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()