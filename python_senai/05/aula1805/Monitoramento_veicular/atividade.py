# importando biblioteca padrao de sistema
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app =   QApplication(sys.argv)
janela = QWidget()
janela.resize(400,600)
janela.setWindowTitle('Netflix')
# janela.setStyleSheet('background-color: black')

with open("style1.css", "r") as file:
    app.setStyleSheet(file.read())
    
lblNome = QLabel("NETFLIX", janela)
lblNome.move(150, 20)
lblNome.setStyleSheet('color: red; font-size: 32px; font-family: "impact"')

lblNome = QLabel("Entrar", janela)
lblNome.move(70, 100)
lblNome.setStyleSheet('color: white; font-size: 32px; font-family: "impact"')

txtLogin = QLineEdit("", janela)
txtLogin.setGeometry(70, 170, 300, 50)
txtLogin.setPlaceholderText('Email ou numero de telefone')
# txtLogin.setStyleSheet('color: white; background-color: ')

txtSenha = QLineEdit("", janela)
txtSenha.setGeometry(70,250,300,50)
txtSenha.setPlaceholderText('Senha')
# txtSenha.setStyleSheet('color: white; border-radius: ')


btnEntrar = QPushButton("Entrar", janela)
btnEntrar.setGeometry(70, 320, 300, 50)
btnEntrar.setStyleSheet('background-color: red; font-size: 25px; color: white; border-radius: 10px; font-family: impact')

lblOu = QLabel("OU", janela)
lblOu.move(200, 380)
lblOu.setStyleSheet('color: white; font-size: 20px;')

btnUsar = QPushButton("Usar um codigo de acesso", janela)
btnUsar.setGeometry(70, 430, 300, 50)
btnUsar.setStyleSheet('background-color: gray; font-size: 20px; color: black; border-radius: 10px')

lblSenha = QLabel("Esqueceu a senha?", janela)
lblSenha.move(130, 500)
lblSenha.setStyleSheet('color: white; font-size: 20px;')


# txt --> se refere a caixas de texto
# btn --> se refere a botões
# lbl --> se refere a labels(rotulos)

janela.show()
app.exec() 