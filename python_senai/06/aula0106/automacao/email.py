# Automação mandar email
# Biblioteca Selenium
# Biblioteca webdriver
# Baixar Chrome Driver

# 01 - Baixar chome Driver e coloca-lo na mesma pasta do python
# 02 - Instalar biblioteca Selenium 
# - pip install selenium
# 03 - Instalar webdriver_manager
# - pip install webdriver_manager

#================================================================
# importar biblioteca selenium 
from selenium import webdriver

# importar biblioteca webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

# importando serviço de utilização do navegador
from selenium.webdriver.chrome.service import Service

# criando um serviço do chrome
servico = Service(ChromeDriverManager().install())

# criar uma variavel para usar o navegador 
navegarEmail = webdriver.Chrome(service=servico)

# abrindo o site do mercado livre 
navegarEmail.get("https://www.youtube.com/")

# pausa no programa
input("Digite enter para fechar")
