# pip install opencv-python
# pip install pyqt6

# importando as bibliotecas opencv-python, sys e PyQt6 com seus elementos 
import sys
import cv2
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

# criando a tela de monitoriamento veicular
app = QApplication(sys.argv)
janela = QWidget()
janela.resize(400,400)
janela.setWindowTitle("Monitoramento Veicular")

# chamar o css no python
with open("python_senai/05/aula1105-webcam/monitoriamento_veicular/style.css", "r") as file:
    app.setStyleSheet(file.read())
    
   
def abrirCamera():
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
    

# criando os campos da tela  
lblNome = QLabel("Monitoramento Veicular", janela)
lblNome.move(90, 30)
lblNome.setStyleSheet("font-size: 20px")

lblNome = QLabel("Nome", janela)
lblNome.move(50, 85)

txtNome = QLineEdit("",janela)
txtNome.setGeometry(150, 80, 200, 30)

lblModelo = QLabel("Modelo", janela)
lblModelo.move(50, 135)

txtNome = QLineEdit("",janela)
txtNome.setGeometry(150, 130, 200, 30)

lblPlaca = QLabel("Placa", janela)
lblPlaca.move(50, 185)

txtNome = QLineEdit("",janela)
txtNome.setGeometry(150, 180, 200, 30)

lblAno = QLabel("Ano Veículo", janela)
lblAno.move(50, 235)

txtNome = QLineEdit("",janela)
txtNome.setGeometry(150, 230, 200, 30)

# criando o botao responsavel para abri a camera 
btnEntrar = QPushButton("Abrir Câmera", janela)
btnEntrar.setGeometry(90, 300, 230, 50)
btnEntrar.clicked.connect(abrirCamera) # responsavel por chamar a funçao para abrir a camera


# executando o monitoriamento
janela.show()
app.exec()