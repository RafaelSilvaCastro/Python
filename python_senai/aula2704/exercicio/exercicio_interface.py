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
janela.resize(400, 430)
janela.setWindowTitle("Cadastro")
#janela.setStyleSheet("background-color: black; color: white; font-family: Lucida Console")

# chamar o css no python
with open("python_senai/aula2704/exercicio/style.css", "r") as file:
    app.setStyleSheet(file.read())
    
    
lblTitulo = QLabel("Inscreva-se em nossa", janela)
lblTitulo.move(50, 30)
#lblNome.setStyleSheet("font-size: 20px")

lblSubTitulo = QLabel("newsletter", janela)
lblSubTitulo.move(50, 50)

lblNome = QLabel("Nome:", janela)
lblNome.move(50, 80)
#lblLogin.setStyleSheet("font-size: 15px")

txtNome = QLineEdit("",janela)
txtNome.setGeometry(50, 100, 300, 50)
#txtLogin.setStyleSheet("background-color: white")

lblEmail = QLabel("E-mail:", janela)
lblEmail.move(50, 170)
#lblSenha.setStyleSheet("font-size: 15px")

txtEmail = QLineEdit("", janela)
txtEmail.setGeometry(50, 190, 300, 50)
#txtSenha.setStyleSheet("background-color: white")

lblCpf = QLabel("CPF:", janela)
lblCpf.move(50, 260)

txtCpf = QLineEdit("", janela)
txtCpf.setGeometry(50, 280, 300, 50)

btnEntrar = QPushButton("Inscreva-se", janela)
btnEntrar.setGeometry(50, 350, 300, 50)
#btnEntrar.setStyleSheet("background-color: red; font-size: 20px; font-family: arial")

# txt --> se refere a caixas de texto
# btn --> se refere a botoes
# lbl --> se refere a labels(rotulos)



janela.show()
app.exec()