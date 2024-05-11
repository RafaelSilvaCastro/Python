# pip install openv-python

import cv2 

# criando uma variavel para capiturar imagens(frames)
# video = cv2.VideoCapture("python_senai/05/aula1105-webcam/midias/video.mp4")

# pegando a camera do computador
camera = cv2.VideoCapture(0)

# loop para percorrer frame a frame, ou imagem por imagem
while True:
    sucesso, frame = camera.read()
    cv2.imshow("imagem video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("s"): # se a teclado do teclado for S ele sai do loop
        break

camera.release()
cv2.destroyAllWindows()
        