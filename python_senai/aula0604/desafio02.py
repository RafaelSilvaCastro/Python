# 02 Crie um programa onde 4 jogadores joguem dado e tenha resultado aleatorios. Guarde esses resultados em um dicionario. No final, exiba o nome e o numero daquele que tirou o maior numero(vencedor).

import random
resultado = {}
for i in range(4):
    nome = input('Digite um nome: ')
    num_ale = (random.randint(1,10))
    resultado [nome] = [num_ale]

print(20*'-')
for a, b in resultado.items():
    maior = sorted(b)
    print(f"{a} tirou o numero {maior}")