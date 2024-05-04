#SENAI Nami Jafet
#Rafael da Silva Castro

# instalar no terminal
# pip install opencv-python
# pip install pyqt6

# importando biblioteca padrão de sistema
import sys
# importando biblioteca PyQt6 com seus elementos 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

# criando a tela da calculadora
app = QApplication(sys.argv)
janela = QWidget()
janela.resize(330,480)
janela.setWindowTitle("Calculadora")

# chamar o css no python
with open("python_senai/aula0405/style.css", "r") as file:
    app.setStyleSheet(file.read())

txtLogin = QLineEdit("",janela)
txtLogin.setGeometry(50, 50, 230, 50)

# primeira linha
btnUm = QPushButton("1", janela)
btnUm.setGeometry(50, 130, 50, 50)

btnDois = QPushButton("2", janela)
btnDois.setGeometry(110, 130, 50, 50)

btnTres = QPushButton("3", janela)
btnTres.setGeometry(170, 130, 50, 50)

btnDividir = QPushButton("/", janela)
btnDividir.setGeometry(230, 130, 50, 50)
btnDividir.setStyleSheet("background-color: rgb(192, 192, 192); font-size: 15px; font-family: Lucida Console")

#segunda linha
btnQuatro= QPushButton("4", janela)
btnQuatro.setGeometry(50, 190, 50, 50)

btnCinco = QPushButton("5", janela)
btnCinco.setGeometry(110, 190, 50, 50)

btnSeis = QPushButton("6", janela)
btnSeis.setGeometry(170, 190, 50, 50)

btnMult = QPushButton("x", janela)
btnMult.setGeometry(230, 190, 50, 50)
btnMult.setStyleSheet("background-color: rgb(192, 192, 192); font-size: 15px; font-family: Lucida Console")

#terceira linha  
btnSete= QPushButton("7", janela)
btnSete.setGeometry(50, 250, 50, 50)

btnOito = QPushButton("8", janela)
btnOito.setGeometry(110, 250, 50, 50)

btnNove = QPushButton("9", janela)
btnNove.setGeometry(170, 250, 50, 50)

btnMenos = QPushButton("-", janela)
btnMenos.setGeometry(230, 250, 50, 50)
btnMenos.setStyleSheet("background-color: rgb(192, 192, 192); font-size: 15px; font-family: Lucida Console")

#quarta linha
btnZero= QPushButton("0", janela)
btnZero.setGeometry(50, 310, 50, 50)

btnVirgula = QPushButton(",", janela)
btnVirgula.setGeometry(110, 310, 50, 50)

btnIgual = QPushButton("=", janela)
btnIgual.setGeometry(170, 310, 50, 50)

btnMais = QPushButton("+", janela)
btnMais.setGeometry(230, 310, 50, 50)
btnMais.setStyleSheet("background-color: rgb(192, 192, 192); font-size: 15px; font-family: Lucida Console")

#quinta linha
btnMaisMenos= QPushButton("+/-", janela)
btnMaisMenos.setGeometry(50, 370, 50, 50)

btnPorcentagem = QPushButton("%", janela)
btnPorcentagem.setGeometry(110, 370, 50, 50)

btnLimpar = QPushButton("C", janela)
btnLimpar.setGeometry(170, 370, 110, 50)
btnLimpar.setStyleSheet("background-color: rgb(192, 192, 192); font-size: 25px; font-family: Lucida Console")



# executando a calculadora
janela.show()
app.exec()
