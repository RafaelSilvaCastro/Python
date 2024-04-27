# instalar no terminal
# pip install opencv-python
# pip install pyqt6

# importando biblioteca padrão de sistema
import sys
# importando biblioteca PyQt6 com seus elementos 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

# criar uma janela 
app = QApplication(sys.argv)
janela = QWidget()
janela.resize(400, 400)
janela.setWindowTitle("Exemplo Interface")
#janela.setStyleSheet("background-color: black; color: white; font-family: Lucida Console")

# chamar o css no python
with open("style.css", "r") as file:
    app.setStyleSheet(file.read())
    
    

lblNome = QLabel("Exemplo Tela", janela)
lblNome.move(150, 30)
lblNome.setStyleSheet("font-size: 20px")

lblLogin = QLabel("Login:", janela)
lblLogin.move(50, 80)
lblLogin.setStyleSheet("font-size: 15px")

txtLogin = QLineEdit("",janela)
txtLogin.setGeometry(150, 80, 200, 20)
txtLogin.setStyleSheet("background-color: white")

lblSenha = QLabel("Senha:", janela)
lblSenha.move(50, 150)
lblSenha.setStyleSheet("font-size: 15px")

txtSenha = QLineEdit("", janela)
txtSenha.setGeometry(150, 150, 200, 20)
txtSenha.setStyleSheet("background-color: white")

btnEntrar = QPushButton("Entrar", janela)
btnEntrar.setGeometry(50, 220, 300, 50)
btnEntrar.setStyleSheet("background-color: red; font-size: 20px; font-family: arial")

# txt --> se refere a caixas de texto
# btn --> se refere a botoes
# lbl --> se refere a labels(rotulos)



janela.show()
app.exec()