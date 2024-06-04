# Automação abrir o video do titulo mundial do São Paulo de 2005
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

# abrindo o site do youtube
navegarEmail.get("https://www.youtube.com/")

# pegar o botao de pesquisa, e escrever oque deseja
# //*[@id="search-form"]
navegarEmail.find_element('xpath', '//*[@id="search-form"]').send_keys('Mundial Sao Paulo')

# botao de pesquisar
# //*[@id="search-icon-legacy"]
# navegarEmail.find_element('xpath', '//*[@id="search-icon-legacy"]').click()



# pausa no programa
input("Digite enter para fechar")
