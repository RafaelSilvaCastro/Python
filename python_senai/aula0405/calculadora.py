# instalar no terminal
# pip install opencv-python
# pip install pyqt6

# importando biblioteca padrão de sistema
import sys
# importando biblioteca PyQt6 com seus elementos 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

# criando a tela da calculadora
app = QApplication(sys.argv)
janela = QWidget
janela.resize(400,600)


# executando a calculadora
janela.show()
app.exec()
