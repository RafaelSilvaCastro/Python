#criar interface simples de login
import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit


app = QApplication(sys.argv)
janela = QWidget()
janela.resize(400,600)
janela.setWindowTitle("Minha Janela")



titulo = QLabel('Primeira Janela',janela)
titulo.move(160,20)


lbl_nome = QLabel('Nome',janela)
lbl_nome.move(50,100)

txt_nome = QLineEdit('', janela)
txt_nome.setGeometry(100,100,150,50)

btn_enviar = QPushButton('Enviar',janela)
btn_enviar.setGeometry(100,150,100,50)


janela.show()
app.exec()