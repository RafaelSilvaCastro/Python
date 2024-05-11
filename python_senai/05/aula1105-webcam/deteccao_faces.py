# https://github.com/opencv/opencv/tree/master/data/haarcascades
# pip install openv-python

import cv2 

imagem_original = cv2.imread("python_senai/05/aula1105-webcam/midias/pessoas.jpg")

# testar
cv2.imshow("Pessoas", imagem_original)
cv2.waitKey(0)