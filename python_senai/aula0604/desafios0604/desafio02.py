# 02 Crie um programa onde 4 jogadores joguem dado e tenha resultado aleatorios. Guarde esses resultados em um dicionario. No final, exiba o nome e o numero daquele que tirou o maior numero(vencedor).

import random
resultado = {}
for i in range(4):
    nome = input('Digite um nome: ')
    num_ale = (random.randint(1,6))
    resultado[nome] = [num_ale]

print(20*'-')
maior_numero = max(resultado.values())
for jogador, resultado in resultado.items():
    if resultado == maior_numero:
        print(f"{jogador} tirou o número {resultado}, sendo o vencedor!")
    else:
        print(f"{jogador} tirou o número {resultado}")
    
