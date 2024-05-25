import cv2

# criando uma variavel para capturar imagens(frames)

# camera = cv2.VideoCapture("video.mp4")
camera = cv2.VideoCapture(0)

# loop para percorrer frame a frame, imagem por imagem
while True:
    sucesso, frame = camera.read()
    cv2.imshow("imagem video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()