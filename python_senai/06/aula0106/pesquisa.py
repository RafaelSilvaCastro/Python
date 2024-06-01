# Automação 
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
navegarGoogle = webdriver.Chrome(service=servico)
navegarSenai = webdriver.Chrome(service=servico)
navegarMecadoLivre = webdriver.Chrome(service=servico)

# abrindo o site do google
navegarGoogle.get("https://www.google.com")

# abrindo o site do senai
navegarSenai.get("https://sp.senai.br/unidade/mogidascruzes/")

# abrindo o site do mercado livre 
navegarMecadoLivre.get("https://www.mercadolivre.com.br/")

# pegar o elemento de caixa de pesquisa do site e escrever oque deseja
# //*[@id="cb1-edit"] Xpath do elemento que deseja
navegarMecadoLivre.find_element('xpath', '//*[@id="cb1-edit"]').send_keys('notebook')

# pegar o elemento de pesquisa
# /html/body/header/div/div[2]/form/button
navegarMecadoLivre.find_element('xpath', '/html/body/header/div/div[2]/form/button').click()



# pausa no programa
input("Digite enter para fechar")
