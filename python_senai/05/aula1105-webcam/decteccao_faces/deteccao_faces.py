# https://github.com/opencv/opencv/tree/master/data/haarcascades
# pip install opencv-python
# pip install pyqt6

import cv2 

imagem_original = cv2.imread("python_senai/05/aula1105-webcam/midias/sp.jpg")

# testar
cv2.imshow("Sao Paulo Campeao CDB2023", imagem_original)
cv2.waitKey(0)

# carregar o arquivo treinado para detectar faces
cascadeFace = cv2.CascadeClassifier("python_senai/05/haarcascade_frontalface_default.xml")

# converter a imagem para tons de cinza
imagemTonsDeCinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

#teste
cv2.imshow("Tons de cinza", imagemTonsDeCinza)
cv2.waitKey(0)

# utilizar arquivo de detecção
faces = cascadeFace.detectMultiScale(imagemTonsDeCinza, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

# desenhar um retangulo na imagem
for (x,y,w,h) in faces:
    cv2.rectangle(imagem_original, (x,y), (x+w, y+h), (0,255,0), 2)
    
    
cv2.imshow("Resultado", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
