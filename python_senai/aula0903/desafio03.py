#3 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

import random
for num_ale in range(5):
    num_ale = (random.randint(1,100)) #cria numeros aleatorios
    print(num_ale)