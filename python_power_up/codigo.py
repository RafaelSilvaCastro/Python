# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
    
# para instalar: pip install pyautogui
import pyautogui
import time

# tempo de delay para executar as tarefas
pyautogui.PAUSE = 1

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> precionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (ctrl c, ctrl v, alt tab)

# abir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundo pra carregar o site 
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=1162, y=437) # achar a posição da caixa de texto do email
pyautogui.write("rafael.castro@gmail.com")

pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("12345")

pyautogui.press("tab") # passou para o botao de logar
pyautogui.press("enter")

time.sleep(3) # garantia para que a proxima pagina abre 

# 3. Abir/Importar a base de dados de produtos para cadastrar 
# pip install pandas numpy openpyxl
import pandas



# 4. Cadastrar um produto
# 5. Repetir isso tudo ate acabar a lista de produtos